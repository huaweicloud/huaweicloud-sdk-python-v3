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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdris'")


class DrisClient(Client):
    def __init__(self):
        super(DrisClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdris.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DrisClient":
                raise TypeError("client type error, support client type is DrisClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_data_channel(self, request):
        r"""创建业务通道

        创建业务通道，用于创建Edge消息上报的数据通道。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.CreateDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateDataChannelResponse`
        """
        http_info = self._create_data_channel_http_info(request)
        return self._call_api(**http_info)

    def create_data_channel_invoker(self, request):
        http_info = self._create_data_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_data_channel_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDataChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def delete_data_channel(self, request):
        r"""删除业务通道

        删除业务通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.DeleteDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteDataChannelResponse`
        """
        http_info = self._delete_data_channel_http_info(request)
        return self._call_api(**http_info)

    def delete_data_channel_invoker(self, request):
        http_info = self._delete_data_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_data_channel_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_data_channel(self, request):
        r"""查询业务通道

        查询业务通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.ShowDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowDataChannelResponse`
        """
        http_info = self._show_data_channel_http_info(request)
        return self._call_api(**http_info)

    def show_data_channel_invoker(self, request):
        http_info = self._show_data_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_channel_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_data_channel(self, request):
        r"""修改业务通道

        修改业务通道
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataChannel
        :type request: :class:`huaweicloudsdkdris.v1.UpdateDataChannelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateDataChannelResponse`
        """
        http_info = self._update_data_channel_http_info(request)
        return self._call_api(**http_info)

    def update_data_channel_invoker(self, request):
        http_info = self._update_data_channel_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_data_channel_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/data-channel",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def create_v2x_edge(self, request):
        r"""创建Edge

        创建Edge
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateV2xEdge
        :type request: :class:`huaweicloudsdkdris.v1.CreateV2xEdgeRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateV2xEdgeResponse`
        """
        http_info = self._create_v2x_edge_http_info(request)
        return self._call_api(**http_info)

    def create_v2x_edge_invoker(self, request):
        http_info = self._create_v2x_edge_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_v2x_edge_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/v2x-edges",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2xEdgeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def delete_v2_x_edge_by_v2x_edge_id(self, request):
        r"""删除Edge

        删除Edge之前需要删除Edge下的业务通道和关联设备。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteV2XEdgeByV2xEdgeId
        :type request: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeByV2xEdgeIdRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeByV2xEdgeIdResponse`
        """
        http_info = self._delete_v2_x_edge_by_v2x_edge_id_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_x_edge_by_v2x_edge_id_invoker(self, request):
        http_info = self._delete_v2_x_edge_by_v2x_edge_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_v2_x_edge_by_v2x_edge_id_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2XEdgeByV2xEdgeIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_v2x_edges(self, request):
        r"""查询Edge列表

        查询Edge列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListV2xEdges
        :type request: :class:`huaweicloudsdkdris.v1.ListV2xEdgesRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListV2xEdgesResponse`
        """
        http_info = self._list_v2x_edges_http_info(request)
        return self._call_api(**http_info)

    def list_v2x_edges_invoker(self, request):
        http_info = self._list_v2x_edges_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_v2x_edges_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edges",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2xEdgesResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_deployment_code(self, request):
        r"""生成部署应用安装命令

        生成部署应用安装命令,然后在ITS800或者ATLAS500上通过Shell执行
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentCode
        :type request: :class:`huaweicloudsdkdris.v1.ShowDeploymentCodeRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowDeploymentCodeResponse`
        """
        http_info = self._show_deployment_code_http_info(request)
        return self._call_api(**http_info)

    def show_deployment_code_invoker(self, request):
        http_info = self._show_deployment_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_deployment_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/deployment-code",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeploymentCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_v2x_edge_detail(self, request):
        r"""查询Edge

        查询Edge
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowV2xEdgeDetail
        :type request: :class:`huaweicloudsdkdris.v1.ShowV2xEdgeDetailRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowV2xEdgeDetailResponse`
        """
        http_info = self._show_v2x_edge_detail_http_info(request)
        return self._call_api(**http_info)

    def show_v2x_edge_detail_invoker(self, request):
        http_info = self._show_v2x_edge_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_v2x_edge_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2xEdgeDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_v2x_edge(self, request):
        r"""修改Edge

        修改Edge
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateV2xEdge
        :type request: :class:`huaweicloudsdkdris.v1.UpdateV2xEdgeRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateV2xEdgeResponse`
        """
        http_info = self._update_v2x_edge_http_info(request)
        return self._call_api(**http_info)

    def update_v2x_edge_invoker(self, request):
        http_info = self._update_v2x_edge_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_v2x_edge_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2xEdgeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def add_forwarding_configs(self, request):
        r"""创建数据转发配置

        创建数据转发配置。当前仅支持数据转发至kafka，数据转发配置成功添加后配置中的Topic消息将会转发至指定的brokers。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddForwardingConfigs
        :type request: :class:`huaweicloudsdkdris.v1.AddForwardingConfigsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.AddForwardingConfigsResponse`
        """
        http_info = self._add_forwarding_configs_http_info(request)
        return self._call_api(**http_info)

    def add_forwarding_configs_invoker(self, request):
        http_info = self._add_forwarding_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_forwarding_configs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/forwarding-configs",
            "request_type": request.__class__.__name__,
            "response_type": "AddForwardingConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def delete_forwarding_config(self, request):
        r"""删除数据转发配置

        根据转发配置的唯一ID（forwarding_config_id）删除数据转发配置，删除后配置中订阅的topic消息将不会被转发至brokers。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteForwardingConfig
        :type request: :class:`huaweicloudsdkdris.v1.DeleteForwardingConfigRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteForwardingConfigResponse`
        """
        http_info = self._delete_forwarding_config_http_info(request)
        return self._call_api(**http_info)

    def delete_forwarding_config_invoker(self, request):
        http_info = self._delete_forwarding_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_forwarding_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/forwarding-configs/{forwarding_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteForwardingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_forwarding_config(self, request):
        r"""查询数据转发配置

        根据转发配置的唯一ID（forwarding_config_id）查询数据转发配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowForwardingConfig
        :type request: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigResponse`
        """
        http_info = self._show_forwarding_config_http_info(request)
        return self._call_api(**http_info)

    def show_forwarding_config_invoker(self, request):
        http_info = self._show_forwarding_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_forwarding_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/forwarding-configs/{forwarding_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowForwardingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_forwarding_configs(self, request):
        r"""查询数据转发配置列表

        查询数据转发配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowForwardingConfigs
        :type request: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowForwardingConfigsResponse`
        """
        http_info = self._show_forwarding_configs_http_info(request)
        return self._call_api(**http_info)

    def show_forwarding_configs_invoker(self, request):
        http_info = self._show_forwarding_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_forwarding_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/forwarding-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowForwardingConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_forwarding_config(self, request):
        r"""修改数据转发配置

        根据转发配置的唯一ID（forwarding_config_id）修改数据转发配置，当前支持更新的字段有topicPrefix、userTopics、brokers，需要把该字段新的对应值全量写入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateForwardingConfig
        :type request: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateForwardingConfigResponse`
        """
        http_info = self._update_forwarding_config_http_info(request)
        return self._call_api(**http_info)

    def update_forwarding_config_invoker(self, request):
        http_info = self._update_forwarding_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_forwarding_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/forwarding-configs/{forwarding_config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateForwardingConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_edge_flows(self, request):
        r"""查询历史交通统计信息列表

        查询历史交通统计信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEdgeFlows
        :type request: :class:`huaweicloudsdkdris.v1.ListEdgeFlowsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListEdgeFlowsResponse`
        """
        http_info = self._list_edge_flows_http_info(request)
        return self._call_api(**http_info)

    def list_edge_flows_invoker(self, request):
        http_info = self._list_edge_flows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_edge_flows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/edge-flow",
            "request_type": request.__class__.__name__,
            "response_type": "ListEdgeFlowsResponse"
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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_history_traffic_events(self, request):
        r"""查询历史交通事件列表

        查询历史交通事件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTrafficEvents
        :type request: :class:`huaweicloudsdkdris.v1.ShowHistoryTrafficEventsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowHistoryTrafficEventsResponse`
        """
        http_info = self._show_history_traffic_events_http_info(request)
        return self._call_api(**http_info)

    def show_history_traffic_events_invoker(self, request):
        http_info = self._show_history_traffic_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_history_traffic_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/history-traffic-events",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTrafficEventsResponse"
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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-app']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_show_ipcs(self, request):
        r"""查询IPC列表

        获取多个IPC资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowIpcs
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowIpcsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowIpcsResponse`
        """
        http_info = self._batch_show_ipcs_http_info(request)
        return self._call_api(**http_info)

    def batch_show_ipcs_invoker(self, request):
        http_info = self._batch_show_ipcs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_ipcs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cameras",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowIpcsResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'v2x_edge_id' in local_var_params:
            query_params.append(('v2x_edge_id', local_var_params['v2x_edge_id']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def show_ipc(self, request):
        r"""查询IPC

        查询IPC
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpc
        :type request: :class:`huaweicloudsdkdris.v1.ShowIpcRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowIpcResponse`
        """
        http_info = self._show_ipc_http_info(request)
        return self._call_api(**http_info)

    def show_ipc_invoker(self, request):
        http_info = self._show_ipc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ipc_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/cameras/{camera_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def batch_show_radars(self, request):
        r"""查询雷达列表

        查询雷达列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowRadars
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowRadarsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowRadarsResponse`
        """
        http_info = self._batch_show_radars_http_info(request)
        return self._call_api(**http_info)

    def batch_show_radars_invoker(self, request):
        http_info = self._batch_show_radars_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_radars_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/radars",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowRadarsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'esn' in local_var_params:
            query_params.append(('esn', local_var_params['esn']))
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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_show_rsus(self, request):
        r"""查询RSU列表

        查询RSU列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowRsus
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowRsusRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowRsusResponse`
        """
        http_info = self._batch_show_rsus_http_info(request)
        return self._call_api(**http_info)

    def batch_show_rsus_invoker(self, request):
        http_info = self._batch_show_rsus_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_rsus_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/rsus",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowRsusResponse"
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

    def create_rsu(self, request):
        r"""创建RSU

        创建RSU
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRsu
        :type request: :class:`huaweicloudsdkdris.v1.CreateRsuRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateRsuResponse`
        """
        http_info = self._create_rsu_http_info(request)
        return self._call_api(**http_info)

    def create_rsu_invoker(self, request):
        http_info = self._create_rsu_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_rsu_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/rsus",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRsuResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def delete_rsu(self, request):
        r"""删除RSU

        删除RSU
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRsu
        :type request: :class:`huaweicloudsdkdris.v1.DeleteRsuRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteRsuResponse`
        """
        http_info = self._delete_rsu_http_info(request)
        return self._call_api(**http_info)

    def delete_rsu_invoker(self, request):
        http_info = self._delete_rsu_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rsu_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/rsus/{rsu_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRsuResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_rsu(self, request):
        r"""修改RSU

        修改RSU
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRsu
        :type request: :class:`huaweicloudsdkdris.v1.UpdateRsuRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateRsuResponse`
        """
        http_info = self._update_rsu_http_info(request)
        return self._call_api(**http_info)

    def update_rsu_invoker(self, request):
        http_info = self._update_rsu_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_rsu_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/rsus/{rsu_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRsuResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def send_immediate_event(self, request):
        r"""创建即时交通事件

        创建即时交通事件，平台分发即时交通事件给目标设备的接口。事件一旦创建便会立即下发且只会下发一次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SendImmediateEvent
        :type request: :class:`huaweicloudsdkdris.v1.SendImmediateEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.SendImmediateEventResponse`
        """
        http_info = self._send_immediate_event_http_info(request)
        return self._call_api(**http_info)

    def send_immediate_event_invoker(self, request):
        http_info = self._send_immediate_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _send_immediate_event_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/immediate-event",
            "request_type": request.__class__.__name__,
            "response_type": "SendImmediateEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def batch_show_traffic_events(self, request):
        r"""查询长期交通事件列表

        条件查询交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowTrafficEvents
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowTrafficEventsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowTrafficEventsResponse`
        """
        http_info = self._batch_show_traffic_events_http_info(request)
        return self._call_api(**http_info)

    def batch_show_traffic_events_invoker(self, request):
        http_info = self._batch_show_traffic_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_traffic_events_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/traffic-events",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowTrafficEventsResponse"
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

    def create_traffic_event(self, request):
        r"""创建长期交通事件

        创建长期交通事件时，平台根据事件的起始时间和结束时间确定当前长期交通事件的状态。对于活跃状态的交通事件会立即下发给在事件影响范围内的RSU，对于未来事件则是在事件开始时间点下发到在事件影响范围内的RSU，过期事件不会下发。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.CreateTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateTrafficEventResponse`
        """
        http_info = self._create_traffic_event_http_info(request)
        return self._call_api(**http_info)

    def create_traffic_event_invoker(self, request):
        http_info = self._create_traffic_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_traffic_event_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/traffic-events",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrafficEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def delete_traffic_event(self, request):
        r"""删除长期交通事件

        刪除长期交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.DeleteTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteTrafficEventResponse`
        """
        http_info = self._delete_traffic_event_http_info(request)
        return self._call_api(**http_info)

    def delete_traffic_event_invoker(self, request):
        http_info = self._delete_traffic_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_traffic_event_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/traffic-events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrafficEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_traffic_event(self, request):
        r"""查询长期交通事件

        查询长期交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.ShowTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowTrafficEventResponse`
        """
        http_info = self._show_traffic_event_http_info(request)
        return self._call_api(**http_info)

    def show_traffic_event_invoker(self, request):
        http_info = self._show_traffic_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_traffic_event_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/traffic-events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrafficEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_traffic_event(self, request):
        r"""修改长期交通事件

        修改长期交通事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrafficEvent
        :type request: :class:`huaweicloudsdkdris.v1.UpdateTrafficEventRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateTrafficEventResponse`
        """
        http_info = self._update_traffic_event_http_info(request)
        return self._call_api(**http_info)

    def update_traffic_event_invoker(self, request):
        http_info = self._update_traffic_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_traffic_event_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/traffic-events/{event_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTrafficEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
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

    def batch_show_traffic_controllers(self, request):
        r"""查询信号机列表

        查询信号机列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowTrafficControllers
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowTrafficControllersRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowTrafficControllersResponse`
        """
        http_info = self._batch_show_traffic_controllers_http_info(request)
        return self._call_api(**http_info)

    def batch_show_traffic_controllers_invoker(self, request):
        http_info = self._batch_show_traffic_controllers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_traffic_controllers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/traffic-controllers",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowTrafficControllersResponse"
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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_traffic_controller(self, request):
        r"""创建信号机

        创建信号机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTrafficController
        :type request: :class:`huaweicloudsdkdris.v1.CreateTrafficControllerRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateTrafficControllerResponse`
        """
        http_info = self._create_traffic_controller_http_info(request)
        return self._call_api(**http_info)

    def create_traffic_controller_invoker(self, request):
        http_info = self._create_traffic_controller_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_traffic_controller_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/traffic-controllers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrafficControllerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_traffic_controller(self, request):
        r"""删除信号机

        删除信号机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTrafficController
        :type request: :class:`huaweicloudsdkdris.v1.DeleteTrafficControllerRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteTrafficControllerResponse`
        """
        http_info = self._delete_traffic_controller_http_info(request)
        return self._call_api(**http_info)

    def delete_traffic_controller_invoker(self, request):
        http_info = self._delete_traffic_controller_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_traffic_controller_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/traffic-controllers/{traffic_controller_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrafficControllerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_traffic_controller(self, request):
        r"""修改信号机

        修改信号机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrafficController
        :type request: :class:`huaweicloudsdkdris.v1.UpdateTrafficControllerRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateTrafficControllerResponse`
        """
        http_info = self._update_traffic_controller_http_info(request)
        return self._call_api(**http_info)

    def update_traffic_controller_invoker(self, request):
        http_info = self._update_traffic_controller_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_traffic_controller_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/traffic-controllers/{traffic_controller_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTrafficControllerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_v2x_edge_app(self, request):
        r"""部署边缘应用

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
        http_info = self._create_v2x_edge_app_http_info(request)
        return self._call_api(**http_info)

    def create_v2x_edge_app_invoker(self, request):
        http_info = self._create_v2x_edge_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_v2x_edge_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateV2xEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_v2_x_edge_app_by_edge_app_id(self, request):
        r"""删除边缘应用

        删除系统应用（$edgetepa）前应先删除业务通道。如删除边缘应用接口调用成功，稍后边缘设备将会自动删除应用无需手动操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteV2XEdgeAppByEdgeAppId
        :type request: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeAppByEdgeAppIdRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteV2XEdgeAppByEdgeAppIdResponse`
        """
        http_info = self._delete_v2_x_edge_app_by_edge_app_id_http_info(request)
        return self._call_api(**http_info)

    def delete_v2_x_edge_app_by_edge_app_id_invoker(self, request):
        http_info = self._delete_v2_x_edge_app_by_edge_app_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_v2_x_edge_app_by_edge_app_id_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps/{edge_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteV2XEdgeAppByEdgeAppIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_v2x_edge_app(self, request):
        r"""查询边缘应用列表

        查询边缘应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListV2xEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.ListV2xEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListV2xEdgeAppResponse`
        """
        http_info = self._list_v2x_edge_app_http_info(request)
        return self._call_api(**http_info)

    def list_v2x_edge_app_invoker(self, request):
        http_info = self._list_v2x_edge_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_v2x_edge_app_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListV2xEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_v2_x_edge_app_detail_by_edge_app_id(self, request):
        r"""查询边缘应用

        查询边缘应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowV2XEdgeAppDetailByEdgeAppId
        :type request: :class:`huaweicloudsdkdris.v1.ShowV2XEdgeAppDetailByEdgeAppIdRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowV2XEdgeAppDetailByEdgeAppIdResponse`
        """
        http_info = self._show_v2_x_edge_app_detail_by_edge_app_id_http_info(request)
        return self._call_api(**http_info)

    def show_v2_x_edge_app_detail_by_edge_app_id_invoker(self, request):
        http_info = self._show_v2_x_edge_app_detail_by_edge_app_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_v2_x_edge_app_detail_by_edge_app_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps/{edge_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowV2XEdgeAppDetailByEdgeAppIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_v2x_edge_app(self, request):
        r"""升级边缘应用

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
        http_info = self._update_v2x_edge_app_http_info(request)
        return self._call_api(**http_info)

    def update_v2x_edge_app_invoker(self, request):
        http_info = self._update_v2x_edge_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_v2x_edge_app_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/v2x-edges/{v2x_edge_id}/apps/{edge_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateV2xEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def batch_show_vehicles(self, request):
        r"""查询车辆列表

        查询车辆列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowVehicles
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowVehiclesRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowVehiclesResponse`
        """
        http_info = self._batch_show_vehicles_http_info(request)
        return self._call_api(**http_info)

    def batch_show_vehicles_invoker(self, request):
        http_info = self._batch_show_vehicles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_vehicles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/vehicles",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowVehiclesResponse"
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
        if 'vehicle_id' in local_var_params:
            query_params.append(('vehicle_id', local_var_params['vehicle_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_vehicle(self, request):
        r"""创建车辆

        创建车辆
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVehicle
        :type request: :class:`huaweicloudsdkdris.v1.CreateVehicleRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateVehicleResponse`
        """
        http_info = self._create_vehicle_http_info(request)
        return self._call_api(**http_info)

    def create_vehicle_invoker(self, request):
        http_info = self._create_vehicle_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_vehicle_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/vehicles",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVehicleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_vehicle(self, request):
        r"""删除车辆

        删除车辆
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVehicle
        :type request: :class:`huaweicloudsdkdris.v1.DeleteVehicleRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteVehicleResponse`
        """
        http_info = self._delete_vehicle_http_info(request)
        return self._call_api(**http_info)

    def delete_vehicle_invoker(self, request):
        http_info = self._delete_vehicle_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_vehicle_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/vehicles/{vehicle_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVehicleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_vehicle(self, request):
        r"""修改车辆

        修改车辆
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVehicle
        :type request: :class:`huaweicloudsdkdris.v1.UpdateVehicleRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateVehicleResponse`
        """
        http_info = self._update_vehicle_http_info(request)
        return self._call_api(**http_info)

    def update_vehicle_invoker(self, request):
        http_info = self._update_vehicle_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_vehicle_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/vehicles/{vehicle_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVehicleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def batch_show_edge_apps(self, request):
        r"""查询应用列表

        查询应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowEdgeApps
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppsResponse`
        """
        http_info = self._batch_show_edge_apps_http_info(request)
        return self._call_api(**http_info)

    def batch_show_edge_apps_invoker(self, request):
        http_info = self._batch_show_edge_apps_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_edge_apps_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edge-apps",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowEdgeAppsResponse"
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

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_app(self, request):
        r"""创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.CreateEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateEdgeAppResponse`
        """
        http_info = self._create_edge_app_http_info(request)
        return self._call_api(**http_info)

    def create_edge_app_invoker(self, request):
        http_info = self._create_edge_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_edge_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/v2x-edge-apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_edge_app(self, request):
        r"""删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.DeleteEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteEdgeAppResponse`
        """
        http_info = self._delete_edge_app_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_app_invoker(self, request):
        http_info = self._delete_edge_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_edge_app_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}",
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
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_edge_app(self, request):
        r"""修改应用

        修改应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeApp
        :type request: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeAppResponse`
        """
        http_info = self._update_edge_app_http_info(request)
        return self._call_api(**http_info)

    def update_edge_app_invoker(self, request):
        http_info = self._update_edge_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_edge_app_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEdgeAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def batch_show_edge_app_versions(self, request):
        r"""查询应用版本列表

        查询应用版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowEdgeAppVersions
        :type request: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppVersionsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.BatchShowEdgeAppVersionsResponse`
        """
        http_info = self._batch_show_edge_app_versions_http_info(request)
        return self._call_api(**http_info)

    def batch_show_edge_app_versions_invoker(self, request):
        http_info = self._batch_show_edge_app_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_edge_app_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowEdgeAppVersionsResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_edge_application_version(self, request):
        r"""创建应用版本

        创建应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.CreateEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateEdgeApplicationVersionResponse`
        """
        http_info = self._create_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def create_edge_application_version_invoker(self, request):
        http_info = self._create_edge_application_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_edge_application_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions",
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
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_edge_application_version(self, request):
        r"""删除应用版本

        删除应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.DeleteEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteEdgeApplicationVersionResponse`
        """
        http_info = self._delete_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def delete_edge_application_version_invoker(self, request):
        http_info = self._delete_edge_application_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_edge_application_version_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}",
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
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_edge_application_version(self, request):
        r"""查询应用版本

        查询应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.ShowEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowEdgeApplicationVersionResponse`
        """
        http_info = self._show_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def show_edge_application_version_invoker(self, request):
        http_info = self._show_edge_application_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_edge_application_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}",
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
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_edge_application_version(self, request):
        r"""修改应用版本

        修改应用版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeApplicationVersion
        :type request: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionResponse`
        """
        http_info = self._update_edge_application_version_http_info(request)
        return self._call_api(**http_info)

    def update_edge_application_version_invoker(self, request):
        http_info = self._update_edge_application_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_edge_application_version_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}",
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
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def update_edge_application_version_state(self, request):
        r"""更新应用版本状态

        更新应用版本状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEdgeApplicationVersionState
        :type request: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionStateRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateEdgeApplicationVersionStateResponse`
        """
        http_info = self._update_edge_application_version_state_http_info(request)
        return self._call_api(**http_info)

    def update_edge_application_version_state_invoker(self, request):
        http_info = self._update_edge_application_version_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_edge_application_version_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/v2x-edge-apps/{edge_app_id}/versions/{version}/state",
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
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def create_rsu_model(self, request):
        r"""创建RSU型号

        调用此接口可创建RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.CreateRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.CreateRsuModelResponse`
        """
        http_info = self._create_rsu_model_http_info(request)
        return self._call_api(**http_info)

    def create_rsu_model_invoker(self, request):
        http_info = self._create_rsu_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_rsu_model_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/rsu-models",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRsuModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'instance_id' in local_var_params:
            header_params['Instance-Id'] = local_var_params['instance_id']

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

    def delete_rsu_model(self, request):
        r"""删除RSU型号

        可调用此接口删除已创建的RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.DeleteRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.DeleteRsuModelResponse`
        """
        http_info = self._delete_rsu_model_http_info(request)
        return self._call_api(**http_info)

    def delete_rsu_model_invoker(self, request):
        http_info = self._delete_rsu_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rsu_model_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/rsu-models/{rsu_model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRsuModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_rsu_models(self, request):
        r"""查询RSU型号列表

        可调用此接口查询已创建RSU型号列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRsuModels
        :type request: :class:`huaweicloudsdkdris.v1.ListRsuModelsRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ListRsuModelsResponse`
        """
        http_info = self._list_rsu_models_http_info(request)
        return self._call_api(**http_info)

    def list_rsu_models_invoker(self, request):
        http_info = self._list_rsu_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rsu_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/rsu-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListRsuModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_rsu_model(self, request):
        r"""查询RSU型号

        可调用此接口查询已创建的RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.ShowRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.ShowRsuModelResponse`
        """
        http_info = self._show_rsu_model_http_info(request)
        return self._call_api(**http_info)

    def show_rsu_model_invoker(self, request):
        http_info = self._show_rsu_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_rsu_model_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/rsu-models/{rsu_model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRsuModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_rsu_model(self, request):
        r"""修改RSU型号

        可调用此接口修改已创建的RSU型号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRsuModel
        :type request: :class:`huaweicloudsdkdris.v1.UpdateRsuModelRequest`
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateRsuModelResponse`
        """
        http_info = self._update_rsu_model_http_info(request)
        return self._call_api(**http_info)

    def update_rsu_model_invoker(self, request):
        http_info = self._update_rsu_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_rsu_model_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/rsu-models/{rsu_model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRsuModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

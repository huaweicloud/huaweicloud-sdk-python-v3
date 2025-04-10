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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmssi'")


class MssiClient(Client):
    def __init__(self):
        super(MssiClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmssi.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MssiClient":
                raise TypeError("client type error, support client type is MssiClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_connection_info(self, request):
        r"""新建Connection

        新建连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnectionInfo
        :type request: :class:`huaweicloudsdkmssi.v1.CreateConnectionInfoRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateConnectionInfoResponse`
        """
        http_info = self._create_connection_info_http_info(request)
        return self._call_api(**http_info)

    def create_connection_info_invoker(self, request):
        http_info = self._create_connection_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connection_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionInfoResponse"
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

    def create_custom_connector_from_openapi(self, request):
        r"""新建自定义连接器(导入swagger方式)

        新建自定义连接器(导入swagger方式)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomConnectorFromOpenapi
        :type request: :class:`huaweicloudsdkmssi.v1.CreateCustomConnectorFromOpenapiRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateCustomConnectorFromOpenapiResponse`
        """
        http_info = self._create_custom_connector_from_openapi_http_info(request)
        return self._call_api(**http_info)

    def create_custom_connector_from_openapi_invoker(self, request):
        http_info = self._create_custom_connector_from_openapi_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_custom_connector_from_openapi_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/connectors/custom-connectors",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomConnectorFromOpenapiResponse"
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

    def create_flow(self, request):
        r"""创建flow

        创建flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlow
        :type request: :class:`huaweicloudsdkmssi.v1.CreateFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateFlowResponse`
        """
        http_info = self._create_flow_http_info(request)
        return self._call_api(**http_info)

    def create_flow_invoker(self, request):
        http_info = self._create_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/flows",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlowResponse"
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

    def create_flow_template_from_flow(self, request):
        r"""根据流创建Flow模板

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlowTemplateFromFlow
        :type request: :class:`huaweicloudsdkmssi.v1.CreateFlowTemplateFromFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateFlowTemplateFromFlowResponse`
        """
        http_info = self._create_flow_template_from_flow_http_info(request)
        return self._call_api(**http_info)

    def create_flow_template_from_flow_invoker(self, request):
        http_info = self._create_flow_template_from_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_flow_template_from_flow_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/flows/{flow_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFlowTemplateFromFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

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

    def delete_connection_info(self, request):
        r"""删除Connection

        删除Connection
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnectionInfo
        :type request: :class:`huaweicloudsdkmssi.v1.DeleteConnectionInfoRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.DeleteConnectionInfoResponse`
        """
        http_info = self._delete_connection_info_http_info(request)
        return self._call_api(**http_info)

    def delete_connection_info_invoker(self, request):
        http_info = self._delete_connection_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_connection_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/connections/{connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectionInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_id' in local_var_params:
            path_params['connect_id'] = local_var_params['connect_id']

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

    def delete_custom_connector(self, request):
        r"""删除自定义连接器

        删除自定义连接器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomConnector
        :type request: :class:`huaweicloudsdkmssi.v1.DeleteCustomConnectorRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.DeleteCustomConnectorResponse`
        """
        http_info = self._delete_custom_connector_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_connector_invoker(self, request):
        http_info = self._delete_custom_connector_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_custom_connector_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/connectors/custom-connectors/{connector_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomConnectorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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

    def delete_flow(self, request):
        r"""删除Flow

        删除Flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlow
        :type request: :class:`huaweicloudsdkmssi.v1.DeleteFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.DeleteFlowResponse`
        """
        http_info = self._delete_flow_http_info(request)
        return self._call_api(**http_info)

    def delete_flow_invoker(self, request):
        http_info = self._delete_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_flow_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/flows/{flow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

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

    def search_flow_by_id(self, request):
        r"""查询特定flow

        查询特定flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchFlowById
        :type request: :class:`huaweicloudsdkmssi.v1.SearchFlowByIdRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.SearchFlowByIdResponse`
        """
        http_info = self._search_flow_by_id_http_info(request)
        return self._call_api(**http_info)

    def search_flow_by_id_invoker(self, request):
        http_info = self._search_flow_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_flow_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/flows/{flow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SearchFlowByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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

    def show_all_connections(self, request):
        r"""查询Connection列表

        查询所有连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllConnections
        :type request: :class:`huaweicloudsdkmssi.v1.ShowAllConnectionsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowAllConnectionsResponse`
        """
        http_info = self._show_all_connections_http_info(request)
        return self._call_api(**http_info)

    def show_all_connections_invoker(self, request):
        http_info = self._show_all_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllConnectionsResponse"
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

    def show_all_flows(self, request):
        r"""查询所有Flow

        查询所有Flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllFlows
        :type request: :class:`huaweicloudsdkmssi.v1.ShowAllFlowsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowAllFlowsResponse`
        """
        http_info = self._show_all_flows_http_info(request)
        return self._call_api(**http_info)

    def show_all_flows_invoker(self, request):
        http_info = self._show_all_flows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_flows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/flows",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllFlowsResponse"
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'have_child_flow' in local_var_params:
            query_params.append(('have_child_flow', local_var_params['have_child_flow']))
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))

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

    def show_connectors(self, request):
        r"""查询Connector列表

        查询Connector列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectors
        :type request: :class:`huaweicloudsdkmssi.v1.ShowConnectorsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowConnectorsResponse`
        """
        http_info = self._show_connectors_http_info(request)
        return self._call_api(**http_info)

    def show_connectors_invoker(self, request):
        http_info = self._show_connectors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connectors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connectors",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectorsResponse"
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
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'operation_type' in local_var_params:
            query_params.append(('operation_type', local_var_params['operation_type']))

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

    def show_custom_connector(self, request):
        r"""发布连接器

        发布连接器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomConnector
        :type request: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorResponse`
        """
        http_info = self._show_custom_connector_http_info(request)
        return self._call_api(**http_info)

    def show_custom_connector_invoker(self, request):
        http_info = self._show_custom_connector_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_custom_connector_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/connectors/custom-connectors/{connector_id}/release",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomConnectorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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

    def show_custom_connectors(self, request):
        r"""查询CustomConnector列表

        查询CustomConnector列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomConnectors
        :type request: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorsResponse`
        """
        http_info = self._show_custom_connectors_http_info(request)
        return self._call_api(**http_info)

    def show_custom_connectors_invoker(self, request):
        http_info = self._show_custom_connectors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_custom_connectors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/connectors/custom-connectors",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomConnectorsResponse"
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

    def show_single_connection(self, request):
        r"""查询单个Connection

        查询单个连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleConnection
        :type request: :class:`huaweicloudsdkmssi.v1.ShowSingleConnectionRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowSingleConnectionResponse`
        """
        http_info = self._show_single_connection_http_info(request)
        return self._call_api(**http_info)

    def show_single_connection_invoker(self, request):
        http_info = self._show_single_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_single_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/connections/{connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSingleConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_id' in local_var_params:
            path_params['connect_id'] = local_var_params['connect_id']

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

    def update_connection_info(self, request):
        r"""修改连接配置内容

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConnectionInfo
        :type request: :class:`huaweicloudsdkmssi.v1.UpdateConnectionInfoRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.UpdateConnectionInfoResponse`
        """
        http_info = self._update_connection_info_http_info(request)
        return self._call_api(**http_info)

    def update_connection_info_invoker(self, request):
        http_info = self._update_connection_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_connection_info_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/connections/{connect_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConnectionInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_id' in local_var_params:
            path_params['connect_id'] = local_var_params['connect_id']

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

    def update_flow(self, request):
        r"""更新flow

        更新flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlow
        :type request: :class:`huaweicloudsdkmssi.v1.UpdateFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.UpdateFlowResponse`
        """
        http_info = self._update_flow_http_info(request)
        return self._call_api(**http_info)

    def update_flow_invoker(self, request):
        http_info = self._update_flow_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_flow_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/flows/{flow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFlowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

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

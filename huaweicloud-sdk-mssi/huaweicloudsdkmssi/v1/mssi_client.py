# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class MssiClient(Client):
    def __init__(self):
        super(MssiClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmssi.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "MssiClient":
            raise TypeError("client type error, support client type is MssiClient")

        return ClientBuilder(clazz)

    def create_connection_info(self, request):
        """新建Connection

        新建连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnectionInfo
        :type request: :class:`huaweicloudsdkmssi.v1.CreateConnectionInfoRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateConnectionInfoResponse`
        """
        return self._create_connection_info_with_http_info(request)

    def _create_connection_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConnectionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_custom_connector_from_openapi(self, request):
        """新建自定义连接器(导入swagger方式)

        新建自定义连接器(导入swagger方式)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomConnectorFromOpenapi
        :type request: :class:`huaweicloudsdkmssi.v1.CreateCustomConnectorFromOpenapiRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateCustomConnectorFromOpenapiResponse`
        """
        return self._create_custom_connector_from_openapi_with_http_info(request)

    def _create_custom_connector_from_openapi_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/custom-connectors',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCustomConnectorFromOpenapiResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flow(self, request):
        """创建flow

        创建flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlow
        :type request: :class:`huaweicloudsdkmssi.v1.CreateFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateFlowResponse`
        """
        return self._create_flow_with_http_info(request)

    def _create_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/flows',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flow_template_from_flow(self, request):
        """根据流创建Flow模板

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFlowTemplateFromFlow
        :type request: :class:`huaweicloudsdkmssi.v1.CreateFlowTemplateFromFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.CreateFlowTemplateFromFlowResponse`
        """
        return self._create_flow_template_from_flow_with_http_info(request)

    def _create_flow_template_from_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

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
            resource_path='/v1/{project_id}/flows/{flow_id}/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlowTemplateFromFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_connection_info(self, request):
        """删除Connection

        删除Connection
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnectionInfo
        :type request: :class:`huaweicloudsdkmssi.v1.DeleteConnectionInfoRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.DeleteConnectionInfoResponse`
        """
        return self._delete_connection_info_with_http_info(request)

    def _delete_connection_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_id' in local_var_params:
            path_params['connect_id'] = local_var_params['connect_id']

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
            resource_path='/v1/{project_id}/connections/{connect_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConnectionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_custom_connector(self, request):
        """删除自定义连接器

        删除自定义连接器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomConnector
        :type request: :class:`huaweicloudsdkmssi.v1.DeleteCustomConnectorRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.DeleteCustomConnectorResponse`
        """
        return self._delete_custom_connector_with_http_info(request)

    def _delete_custom_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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
            resource_path='/v2/{project_id}/connectors/custom-connectors/{connector_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCustomConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_flow(self, request):
        """删除Flow

        删除Flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFlow
        :type request: :class:`huaweicloudsdkmssi.v1.DeleteFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.DeleteFlowResponse`
        """
        return self._delete_flow_with_http_info(request)

    def _delete_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

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
            resource_path='/v1/{project_id}/flows/{flow_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFlowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_flow_by_id(self, request):
        """查询特定flow

        查询特定flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchFlowById
        :type request: :class:`huaweicloudsdkmssi.v1.SearchFlowByIdRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.SearchFlowByIdResponse`
        """
        return self._search_flow_by_id_with_http_info(request)

    def _search_flow_by_id_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/flows/{flow_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchFlowByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_all_connections(self, request):
        """查询Connection列表

        查询所有连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllConnections
        :type request: :class:`huaweicloudsdkmssi.v1.ShowAllConnectionsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowAllConnectionsResponse`
        """
        return self._show_all_connections_with_http_info(request)

    def _show_all_connections_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAllConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_all_flows(self, request):
        """查询所有Flow

        查询所有Flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllFlows
        :type request: :class:`huaweicloudsdkmssi.v1.ShowAllFlowsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowAllFlowsResponse`
        """
        return self._show_all_flows_with_http_info(request)

    def _show_all_flows_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/flows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAllFlowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_connectors(self, request):
        """查询Connector列表

        查询Connector列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectors
        :type request: :class:`huaweicloudsdkmssi.v1.ShowConnectorsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowConnectorsResponse`
        """
        return self._show_connectors_with_http_info(request)

    def _show_connectors_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/connectors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConnectorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_custom_connector(self, request):
        """发布连接器

        发布连接器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomConnector
        :type request: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorResponse`
        """
        return self._show_custom_connector_with_http_info(request)

    def _show_custom_connector_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connector_id' in local_var_params:
            path_params['connector_id'] = local_var_params['connector_id']

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
            resource_path='/v2/{project_id}/connectors/custom-connectors/{connector_id}/release',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCustomConnectorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_custom_connectors(self, request):
        """查询CustomConnector列表

        查询CustomConnector列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomConnectors
        :type request: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorsRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowCustomConnectorsResponse`
        """
        return self._show_custom_connectors_with_http_info(request)

    def _show_custom_connectors_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/connectors/custom-connectors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCustomConnectorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_single_connection(self, request):
        """查询单个Connection

        查询单个连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleConnection
        :type request: :class:`huaweicloudsdkmssi.v1.ShowSingleConnectionRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.ShowSingleConnectionResponse`
        """
        return self._show_single_connection_with_http_info(request)

    def _show_single_connection_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_id' in local_var_params:
            path_params['connect_id'] = local_var_params['connect_id']

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
            resource_path='/v1/{project_id}/connections/{connect_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSingleConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_connection_info(self, request):
        """修改连接配置内容

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConnectionInfo
        :type request: :class:`huaweicloudsdkmssi.v1.UpdateConnectionInfoRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.UpdateConnectionInfoResponse`
        """
        return self._update_connection_info_with_http_info(request)

    def _update_connection_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connect_id' in local_var_params:
            path_params['connect_id'] = local_var_params['connect_id']

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
            resource_path='/v1/{project_id}/connections/{connect_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateConnectionInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_flow(self, request):
        """更新flow

        更新flow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFlow
        :type request: :class:`huaweicloudsdkmssi.v1.UpdateFlowRequest`
        :rtype: :class:`huaweicloudsdkmssi.v1.UpdateFlowResponse`
        """
        return self._update_flow_with_http_info(request)

    def _update_flow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'flow_id' in local_var_params:
            path_params['flow_id'] = local_var_params['flow_id']

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
            resource_path='/v1/{project_id}/flows/{flow_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFlowResponse',
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

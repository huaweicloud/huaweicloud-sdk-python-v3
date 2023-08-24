# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class ErAsyncClient(Client):
    def __init__(self):
        super(ErAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdker.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ErClient":
            raise TypeError("client type error, support client type is ErClient")

        return ClientBuilder(clazz)

    def associate_route_table_async(self, request):
        """创建路由关联

        每个连接只能关联到一张路由表。通过创建关联将连接关联到路由表，从该连接收到的报文会用被关联的路由表进行路由。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRouteTable
        :type request: :class:`huaweicloudsdker.v3.AssociateRouteTableRequest`
        :rtype: :class:`huaweicloudsdker.v3.AssociateRouteTableResponse`
        """
        return self._associate_route_table_with_http_info(request)

    def _associate_route_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}/associate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_route_table_async(self, request):
        """删除路由关联

        解绑连接和路由表的关联关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateRouteTable
        :type request: :class:`huaweicloudsdker.v3.DisassociateRouteTableRequest`
        :rtype: :class:`huaweicloudsdker.v3.DisassociateRouteTableResponse`
        """
        return self._disassociate_route_table_with_http_info(request)

    def _disassociate_route_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}/disassociate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_associations_async(self, request):
        """查询路由关联列表

        查询路由关联列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAssociations
        :type request: :class:`huaweicloudsdker.v3.ListAssociationsRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListAssociationsResponse`
        """
        return self._list_associations_with_http_info(request)

    def _list_associations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'attachment_id' in local_var_params:
            query_params.append(('attachment_id', local_var_params['attachment_id']))
            collection_formats['attachment_id'] = 'multi'
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
            collection_formats['resource_type'] = 'multi'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}/associations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAssociationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def accept_attachment_async(self, request):
        """接受共享连接创建

        接受共享连接创建
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AcceptAttachment
        :type request: :class:`huaweicloudsdker.v3.AcceptAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.AcceptAttachmentResponse`
        """
        return self._accept_attachment_with_http_info(request)

    def _accept_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/attachments/{attachment_id}/accept',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AcceptAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_attachments_async(self, request):
        """查询连接列表

        查询企业路由器实例下的连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAttachments
        :type request: :class:`huaweicloudsdker.v3.ListAttachmentsRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListAttachmentsResponse`
        """
        return self._list_attachments_with_http_info(request)

    def _list_attachments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
            collection_formats['resource_type'] = 'multi'
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
            collection_formats['resource_id'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/attachments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAttachmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reject_attachment_async(self, request):
        """拒绝共享连接创建

        拒绝共享连接创建
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RejectAttachment
        :type request: :class:`huaweicloudsdker.v3.RejectAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.RejectAttachmentResponse`
        """
        return self._reject_attachment_with_http_info(request)

    def _reject_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/attachments/{attachment_id}/reject',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RejectAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_attachment_async(self, request):
        """查询连接详情

        查询连接详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAttachment
        :type request: :class:`huaweicloudsdker.v3.ShowAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowAttachmentResponse`
        """
        return self._show_attachment_with_http_info(request)

    def _show_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/attachments/{attachment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_attachment_async(self, request):
        """更新连接基本信息

        修改连接基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAttachment
        :type request: :class:`huaweicloudsdker.v3.UpdateAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.UpdateAttachmentResponse`
        """
        return self._update_attachment_with_http_info(request)

    def _update_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/attachments/{attachment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zone_async(self, request):
        """查询可用区列表

        查询支持创建企业路由器实例的可用区列表，当可用区状态为available时，表示可以创建企业路由器实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZone
        :type request: :class:`huaweicloudsdker.v3.ListAvailabilityZoneRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListAvailabilityZoneResponse`
        """
        return self._list_availability_zone_with_http_info(request)

    def _list_availability_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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
            resource_path='/v3/{project_id}/enterprise-router/availability-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_availability_zone_async(self, request):
        """更新企业路由器的可用区信息

        更新企业路由器的可用区信息，企业路由器实例状态为available的时候才能更新。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeAvailabilityZone
        :type request: :class:`huaweicloudsdker.v3.ChangeAvailabilityZoneRequest`
        :rtype: :class:`huaweicloudsdker.v3.ChangeAvailabilityZoneResponse`
        """
        return self._change_availability_zone_with_http_info(request)

    def _change_availability_zone_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

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
            resource_path='/v3/{project_id}/enterprise-router/instances/{er_id}/change-availability-zone-ids',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeAvailabilityZoneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_enterprise_router_async(self, request):
        """创建企业路由器

        创建企业路由器实例，如果使能默认关联路由表或使能默认传递路由表，那么系统会默认创建一张路由表，作为默认关联路由表或默认传递路由表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEnterpriseRouter
        :type request: :class:`huaweicloudsdker.v3.CreateEnterpriseRouterRequest`
        :rtype: :class:`huaweicloudsdker.v3.CreateEnterpriseRouterResponse`
        """
        return self._create_enterprise_router_with_http_info(request)

    def _create_enterprise_router_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnterpriseRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_enterprise_router_async(self, request):
        """删除企业路由器

        删除企业路由器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnterpriseRouter
        :type request: :class:`huaweicloudsdker.v3.DeleteEnterpriseRouterRequest`
        :rtype: :class:`huaweicloudsdker.v3.DeleteEnterpriseRouterResponse`
        """
        return self._delete_enterprise_router_with_http_info(request)

    def _delete_enterprise_router_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

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
            resource_path='/v3/{project_id}/enterprise-router/instances/{er_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnterpriseRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_enterprise_routers_async(self, request):
        """查询企业路由器列表

        查询企业路由器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnterpriseRouters
        :type request: :class:`huaweicloudsdker.v3.ListEnterpriseRoutersRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListEnterpriseRoutersResponse`
        """
        return self._list_enterprise_routers_with_http_info(request)

    def _list_enterprise_routers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
            collection_formats['enterprise_project_id'] = 'multi'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
            collection_formats['resource_id'] = 'multi'
        if 'owned_by_self' in local_var_params:
            query_params.append(('owned_by_self', local_var_params['owned_by_self']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnterpriseRoutersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_enterprise_router_async(self, request):
        """查询企业路由器详情

        查询企业路由器详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnterpriseRouter
        :type request: :class:`huaweicloudsdker.v3.ShowEnterpriseRouterRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowEnterpriseRouterResponse`
        """
        return self._show_enterprise_router_with_http_info(request)

    def _show_enterprise_router_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

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
            resource_path='/v3/{project_id}/enterprise-router/instances/{er_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnterpriseRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_enterprise_router_async(self, request):
        """更新企业路由器

        更新企业路由器基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEnterpriseRouter
        :type request: :class:`huaweicloudsdker.v3.UpdateEnterpriseRouterRequest`
        :rtype: :class:`huaweicloudsdker.v3.UpdateEnterpriseRouterResponse`
        """
        return self._update_enterprise_router_with_http_info(request)

    def _update_enterprise_router_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

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
            resource_path='/v3/{project_id}/enterprise-router/instances/{er_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateEnterpriseRouterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_flow_log_async(self, request):
        """创建流日志

        给ER实例创建流日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFlowLog
        :type request: :class:`huaweicloudsdker.v3.CreateFlowLogRequest`
        :rtype: :class:`huaweicloudsdker.v3.CreateFlowLogResponse`
        """
        return self._create_flow_log_with_http_info(request)

    def _create_flow_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_flow_log_async(self, request):
        """删除流日志

        删除流日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFlowLog
        :type request: :class:`huaweicloudsdker.v3.DeleteFlowLogRequest`
        :rtype: :class:`huaweicloudsdker.v3.DeleteFlowLogResponse`
        """
        return self._delete_flow_log_with_http_info(request)

    def _delete_flow_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'flow_log_id' in local_var_params:
            path_params['flow_log_id'] = local_var_params['flow_log_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs/{flow_log_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_flow_log_async(self, request):
        """关闭流日志

        关闭流日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisableFlowLog
        :type request: :class:`huaweicloudsdker.v3.DisableFlowLogRequest`
        :rtype: :class:`huaweicloudsdker.v3.DisableFlowLogResponse`
        """
        return self._disable_flow_log_with_http_info(request)

    def _disable_flow_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'flow_log_id' in local_var_params:
            path_params['flow_log_id'] = local_var_params['flow_log_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs/{flow_log_id}/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_flow_log_async(self, request):
        """开启流日志

        开启流日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableFlowLog
        :type request: :class:`huaweicloudsdker.v3.EnableFlowLogRequest`
        :rtype: :class:`huaweicloudsdker.v3.EnableFlowLogResponse`
        """
        return self._enable_flow_log_with_http_info(request)

    def _enable_flow_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'flow_log_id' in local_var_params:
            path_params['flow_log_id'] = local_var_params['flow_log_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs/{flow_log_id}/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flow_logs_async(self, request):
        """查询流日志列表

        查询企业路由器实例下的流日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlowLogs
        :type request: :class:`huaweicloudsdker.v3.ListFlowLogsRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListFlowLogsResponse`
        """
        return self._list_flow_logs_with_http_info(request)

    def _list_flow_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
            collection_formats['resource_id'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlowLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_flow_log_async(self, request):
        """查询流日志详情

        查询流日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFlowLog
        :type request: :class:`huaweicloudsdker.v3.ShowFlowLogRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowFlowLogResponse`
        """
        return self._show_flow_log_with_http_info(request)

    def _show_flow_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'flow_log_id' in local_var_params:
            path_params['flow_log_id'] = local_var_params['flow_log_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs/{flow_log_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_flow_log_async(self, request):
        """更新流日志基本信息

        更新流日志基本信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFlowLog
        :type request: :class:`huaweicloudsdker.v3.UpdateFlowLogRequest`
        :rtype: :class:`huaweicloudsdker.v3.UpdateFlowLogResponse`
        """
        return self._update_flow_log_with_http_info(request)

    def _update_flow_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'flow_log_id' in local_var_params:
            path_params['flow_log_id'] = local_var_params['flow_log_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/flow-logs/{flow_log_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateFlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_propagation_async(self, request):
        """删除路由传播

        解绑连接和路由表的传播关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisablePropagation
        :type request: :class:`huaweicloudsdker.v3.DisablePropagationRequest`
        :rtype: :class:`huaweicloudsdker.v3.DisablePropagationResponse`
        """
        return self._disable_propagation_with_http_info(request)

    def _disable_propagation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}/disable-propagations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisablePropagationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_propagation_async(self, request):
        """创建路由传播

        每个连接可以和多个路由表建立传播关系，从该连接学习到的路由会应用到具有传播关系的路由表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnablePropagation
        :type request: :class:`huaweicloudsdker.v3.EnablePropagationRequest`
        :rtype: :class:`huaweicloudsdker.v3.EnablePropagationResponse`
        """
        return self._enable_propagation_with_http_info(request)

    def _enable_propagation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}/enable-propagations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnablePropagationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_propagations_async(self, request):
        """查询路由传播列表

        查询路由传播列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPropagations
        :type request: :class:`huaweicloudsdker.v3.ListPropagationsRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListPropagationsResponse`
        """
        return self._list_propagations_with_http_info(request)

    def _list_propagations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'attachment_id' in local_var_params:
            query_params.append(('attachment_id', local_var_params['attachment_id']))
            collection_formats['attachment_id'] = 'multi'
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
            collection_formats['resource_type'] = 'multi'
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}/propagations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPropagationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_async(self, request):
        """查询配额

        查询租户各类资源的使用情况，如企业路由器的使用量，VPC连接的使用量等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdker.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowQuotasResponse`
        """
        return self._show_quotas_with_http_info(request)

    def _show_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
            collection_formats['type'] = 'multi'
        if 'er_id' in local_var_params:
            query_params.append(('erId', local_var_params['er_id']))
            collection_formats['erId'] = 'multi'
        if 'route_table_id' in local_var_params:
            query_params.append(('routeTableId', local_var_params['route_table_id']))
            collection_formats['routeTableId'] = 'multi'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpcId', local_var_params['vpc_id']))
            collection_formats['vpcId'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_static_route_async(self, request):
        """创建静态路由

        创建静态路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStaticRoute
        :type request: :class:`huaweicloudsdker.v3.CreateStaticRouteRequest`
        :rtype: :class:`huaweicloudsdker.v3.CreateStaticRouteResponse`
        """
        return self._create_static_route_with_http_info(request)

    def _create_static_route_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/route-tables/{route_table_id}/static-routes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStaticRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_static_route_async(self, request):
        """删除静态路由

        删除静态路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStaticRoute
        :type request: :class:`huaweicloudsdker.v3.DeleteStaticRouteRequest`
        :rtype: :class:`huaweicloudsdker.v3.DeleteStaticRouteResponse`
        """
        return self._delete_static_route_with_http_info(request)

    def _delete_static_route_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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
            resource_path='/v3/{project_id}/enterprise-router/route-tables/{route_table_id}/static-routes/{route_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStaticRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_effective_routes_async(self, request):
        """查询有效路由列表

        查询有效的路由列表，支持分页查询能力
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEffectiveRoutes
        :type request: :class:`huaweicloudsdker.v3.ListEffectiveRoutesRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListEffectiveRoutesResponse`
        """
        return self._list_effective_routes_with_http_info(request)

    def _list_effective_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
            collection_formats['destination'] = 'multi'
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
            collection_formats['resource_type'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/route-tables/{route_table_id}/routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEffectiveRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_static_routes_async(self, request):
        """查询静态路由列表

        查询静态路由列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStaticRoutes
        :type request: :class:`huaweicloudsdker.v3.ListStaticRoutesRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListStaticRoutesResponse`
        """
        return self._list_static_routes_with_http_info(request)

    def _list_static_routes_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
            collection_formats['destination'] = 'multi'
        if 'attachment_id' in local_var_params:
            query_params.append(('attachment_id', local_var_params['attachment_id']))
            collection_formats['attachment_id'] = 'multi'
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
            collection_formats['resource_type'] = 'multi'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/route-tables/{route_table_id}/static-routes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStaticRoutesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_static_route_async(self, request):
        """查询静态路由详情

        查询静态路由详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStaticRoute
        :type request: :class:`huaweicloudsdker.v3.ShowStaticRouteRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowStaticRouteResponse`
        """
        return self._show_static_route_with_http_info(request)

    def _show_static_route_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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
            resource_path='/v3/{project_id}/enterprise-router/route-tables/{route_table_id}/static-routes/{route_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowStaticRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_static_route_async(self, request):
        """更新静态路由

        更新静态路由
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStaticRoute
        :type request: :class:`huaweicloudsdker.v3.UpdateStaticRouteRequest`
        :rtype: :class:`huaweicloudsdker.v3.UpdateStaticRouteResponse`
        """
        return self._update_static_route_with_http_info(request)

    def _update_static_route_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']
        if 'route_id' in local_var_params:
            path_params['route_id'] = local_var_params['route_id']

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
            resource_path='/v3/{project_id}/enterprise-router/route-tables/{route_table_id}/static-routes/{route_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStaticRouteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_route_table_async(self, request):
        """创建路由表

        路由表是企业路由器收发报文的依据，包含了连接的关联关系，传播关系以及路由信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRouteTable
        :type request: :class:`huaweicloudsdker.v3.CreateRouteTableRequest`
        :rtype: :class:`huaweicloudsdker.v3.CreateRouteTableResponse`
        """
        return self._create_route_table_with_http_info(request)

    def _create_route_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_route_table_async(self, request):
        """删除路由表

        删除路由表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRouteTable
        :type request: :class:`huaweicloudsdker.v3.DeleteRouteTableRequest`
        :rtype: :class:`huaweicloudsdker.v3.DeleteRouteTableResponse`
        """
        return self._delete_route_table_with_http_info(request)

    def _delete_route_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_route_tables_async(self, request):
        """查询路由表列表

        查询路由表列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRouteTables
        :type request: :class:`huaweicloudsdker.v3.ListRouteTablesRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListRouteTablesResponse`
        """
        return self._list_route_tables_with_http_info(request)

    def _list_route_tables_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'is_default_propagation_table' in local_var_params:
            query_params.append(('is_default_propagation_table', local_var_params['is_default_propagation_table']))
        if 'is_default_association_table' in local_var_params:
            query_params.append(('is_default_association_table', local_var_params['is_default_association_table']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRouteTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_route_table_async(self, request):
        """查询路由表详情

        查询路由表详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRouteTable
        :type request: :class:`huaweicloudsdker.v3.ShowRouteTableRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowRouteTableResponse`
        """
        return self._show_route_table_with_http_info(request)

    def _show_route_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_route_table_async(self, request):
        """更新路由表信息

        更新路由表基本信息，如名称，描述等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRouteTable
        :type request: :class:`huaweicloudsdker.v3.UpdateRouteTableRequest`
        :rtype: :class:`huaweicloudsdker.v3.UpdateRouteTableResponse`
        """
        return self._update_route_table_with_http_info(request)

    def _update_route_table_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'route_table_id' in local_var_params:
            path_params['route_table_id'] = local_var_params['route_table_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/route-tables/{route_table_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRouteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_resource_tags_async(self, request):
        """批量添加删除资源标签

        - 为指定实例批量添加或删除标签
        - 标签管理服务需要使用该接口批量管理实例的标签。
        - 一个资源上最多有10个标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceTags
        :type request: :class:`huaweicloudsdker.v3.BatchCreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdker.v3.BatchCreateResourceTagsResponse`
        """
        return self._batch_create_resource_tags_with_http_info(request)

    def _batch_create_resource_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource_tag_async(self, request):
        """创建资源标签

        为特定类型的资源创建标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceTag
        :type request: :class:`huaweicloudsdker.v3.CreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdker.v3.CreateResourceTagResponse`
        """
        return self._create_resource_tag_with_http_info(request)

    def _create_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_tag_async(self, request):
        """删除资源标签

        删除特定类型资源的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdker.v3.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdker.v3.DeleteResourceTagResponse`
        """
        return self._delete_resource_tag_with_http_info(request)

    def _delete_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_tags_async(self, request):
        """查询项目标签

        查询特定类型资源的标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdker.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListProjectTagsResponse`
        """
        return self._list_project_tags_with_http_info(request)

    def _list_project_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_tag_async(self, request):
        """查询资源标签

        查询特定类型资源的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourceTag
        :type request: :class:`huaweicloudsdker.v3.ShowResourceTagRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowResourceTagResponse`
        """
        return self._show_resource_tag_with_http_info(request)

    def _show_resource_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v3/{project_id}/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vpc_attachment_async(self, request):
        """创建VPC连接

        给ER实例创建VPC连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVpcAttachment
        :type request: :class:`huaweicloudsdker.v3.CreateVpcAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.CreateVpcAttachmentResponse`
        """
        return self._create_vpc_attachment_with_http_info(request)

    def _create_vpc_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Client-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/vpc-attachments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVpcAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vpc_attachment_async(self, request):
        """删除VPC连接

        删除VPC连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVpcAttachment
        :type request: :class:`huaweicloudsdker.v3.DeleteVpcAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.DeleteVpcAttachmentResponse`
        """
        return self._delete_vpc_attachment_with_http_info(request)

    def _delete_vpc_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'vpc_attachment_id' in local_var_params:
            path_params['vpc_attachment_id'] = local_var_params['vpc_attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/vpc-attachments/{vpc_attachment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVpcAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_attachments_async(self, request):
        """查询VPC连接列表

        查询企业路由器实例下的VPC连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcAttachments
        :type request: :class:`huaweicloudsdker.v3.ListVpcAttachmentsRequest`
        :rtype: :class:`huaweicloudsdker.v3.ListVpcAttachmentsResponse`
        """
        return self._list_vpc_attachments_with_http_info(request)

    def _list_vpc_attachments_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
            collection_formats['state'] = 'multi'
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'csv'
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
            collection_formats['sort_key'] = 'multi'
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
            collection_formats['sort_dir'] = 'multi'
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
            collection_formats['vpc_id'] = 'multi'

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/vpc-attachments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVpcAttachmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vpc_attachment_async(self, request):
        """查询VPC连接详情

        查询VPC连接详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVpcAttachment
        :type request: :class:`huaweicloudsdker.v3.ShowVpcAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.ShowVpcAttachmentResponse`
        """
        return self._show_vpc_attachment_with_http_info(request)

    def _show_vpc_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'vpc_attachment_id' in local_var_params:
            path_params['vpc_attachment_id'] = local_var_params['vpc_attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/vpc-attachments/{vpc_attachment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVpcAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vpc_attachment_async(self, request):
        """更新VPC连接基本信息

        修改VPC连接基本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVpcAttachment
        :type request: :class:`huaweicloudsdker.v3.UpdateVpcAttachmentRequest`
        :rtype: :class:`huaweicloudsdker.v3.UpdateVpcAttachmentResponse`
        """
        return self._update_vpc_attachment_with_http_info(request)

    def _update_vpc_attachment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'er_id' in local_var_params:
            path_params['er_id'] = local_var_params['er_id']
        if 'vpc_attachment_id' in local_var_params:
            path_params['vpc_attachment_id'] = local_var_params['vpc_attachment_id']

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
            resource_path='/v3/{project_id}/enterprise-router/{er_id}/vpc-attachments/{vpc_attachment_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVpcAttachmentResponse',
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

# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CfwClient(Client):
    def __init__(self):
        super(CfwClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcfw.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CfwClient":
                raise TypeError("client type error, support client type is CfwClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_address_item(self, request):
        """添加地址组成员

        添加地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAddressItem
        :type request: :class:`huaweicloudsdkcfw.v1.AddAddressItemRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAddressItemResponse`
        """
        return self._add_address_item_with_http_info(request)

    def _add_address_item_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-items',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddAddressItemResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_address_set(self, request):
        """添加地址组

        添加地址组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAddressSet
        :type request: :class:`huaweicloudsdkcfw.v1.AddAddressSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAddressSetResponse`
        """
        return self._add_address_set_with_http_info(request)

    def _add_address_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-set',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddAddressSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_black_white_list(self, request):
        """创建黑白名单规则

        创建黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddBlackWhiteList
        :type request: :class:`huaweicloudsdkcfw.v1.AddBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddBlackWhiteListResponse`
        """
        return self._add_black_white_list_with_http_info(request)

    def _add_black_white_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/black-white-list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_domain_set(self, request):
        """添加域名组

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.AddDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddDomainSetResponse`
        """
        return self._add_domain_set_with_http_info(request)

    def _add_domain_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/domain-set',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddDomainSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_domains(self, request):
        """添加域名列表

        添加域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDomains
        :type request: :class:`huaweicloudsdkcfw.v1.AddDomainsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddDomainsResponse`
        """
        return self._add_domains_with_http_info(request)

    def _add_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/domain-set/domains/{set_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_service_items(self, request):
        """新建服务成员

        批量添加服务组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddServiceItems
        :type request: :class:`huaweicloudsdkcfw.v1.AddServiceItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddServiceItemsResponse`
        """
        return self._add_service_items_with_http_info(request)

    def _add_service_items_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-items',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddServiceItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_service_set(self, request):
        """新建服务组

        创建服务组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.AddServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddServiceSetResponse`
        """
        return self._add_service_set_with_http_info(request)

    def _add_service_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-set',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddServiceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_address_items(self, request):
        """批量删除地址组成员

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAddressItems
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteAddressItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteAddressItemsResponse`
        """
        return self._batch_delete_address_items_with_http_info(request)

    def _batch_delete_address_items_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-items',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAddressItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_service_items(self, request):
        """批量删除服务组成员信息

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteServiceItems
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteServiceItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteServiceItemsResponse`
        """
        return self._batch_delete_service_items_with_http_info(request)

    def _batch_delete_service_items_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-items',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteServiceItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_east_west_firewall_status(self, request):
        """修改东西向防火墙防护状态

        东西向防护资源防护开启/关闭
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEastWestFirewallStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeEastWestFirewallStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeEastWestFirewallStatusResponse`
        """
        return self._change_east_west_firewall_status_with_http_info(request)

    def _change_east_west_firewall_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/firewall/east-west/protect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeEastWestFirewallStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_address_item(self, request):
        """删除地址组成员

        删除地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAddressItem
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAddressItemRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAddressItemResponse`
        """
        return self._delete_address_item_with_http_info(request)

    def _delete_address_item_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item_id'] = local_var_params['item_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-items/{item_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAddressItemResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_address_set(self, request):
        """删除地址组

        删除地址组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAddressSet
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAddressSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAddressSetResponse`
        """
        return self._delete_address_set_with_http_info(request)

    def _delete_address_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-sets/{set_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAddressSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_black_white_list(self, request):
        """删除黑白名单规则

        删除黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBlackWhiteList
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteBlackWhiteListResponse`
        """
        return self._delete_black_white_list_with_http_info(request)

    def _delete_black_white_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/black-white-list/{list_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain_set(self, request):
        """删除域名组

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteDomainSetResponse`
        """
        return self._delete_domain_set_with_http_info(request)

    def _delete_domain_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/domain-set/{set_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domains(self, request):
        """删除域名列表

        删除域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomains
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteDomainsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteDomainsResponse`
        """
        return self._delete_domains_with_http_info(request)

    def _delete_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/domain-set/domains/{set_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_service_item(self, request):
        """删除服务成员

        删除服务组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceItem
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteServiceItemRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteServiceItemResponse`
        """
        return self._delete_service_item_with_http_info(request)

    def _delete_service_item_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'item_id' in local_var_params:
            path_params['item_id'] = local_var_params['item_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-items/{item_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServiceItemResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_service_set(self, request):
        """删除服务组

        删除服务组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteServiceSetResponse`
        """
        return self._delete_service_set_with_http_info(request)

    def _delete_service_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-sets/{set_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServiceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_access_control_logs(self, request):
        """查询访问控制日志

        查询访问控制日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccessControlLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListAccessControlLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAccessControlLogsResponse`
        """
        return self._list_access_control_logs_with_http_info(request)

    def _list_access_control_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'src_port' in local_var_params:
            query_params.append(('src_port', local_var_params['src_port']))
        if 'dst_ip' in local_var_params:
            query_params.append(('dst_ip', local_var_params['dst_ip']))
        if 'dst_port' in local_var_params:
            query_params.append(('dst_port', local_var_params['dst_port']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'next_date' in local_var_params:
            query_params.append(('next_date', local_var_params['next_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'dst_host' in local_var_params:
            query_params.append(('dst_host', local_var_params['dst_host']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

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
            resource_path='/v1/{project_id}/cfw/logs/access-control',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccessControlLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_address_items(self, request):
        """查询地址组成员

        查询地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddressItems
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressItemsResponse`
        """
        return self._list_address_items_with_http_info(request)

    def _list_address_items_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'set_id' in local_var_params:
            query_params.append(('set_id', local_var_params['set_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-items',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAddressItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_address_set_detail(self, request):
        """查询地址组详细信息

        查询地址组详细
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddressSetDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressSetDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressSetDetailResponse`
        """
        return self._list_address_set_detail_with_http_info(request)

    def _list_address_set_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-sets/{set_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAddressSetDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_address_sets(self, request):
        """查询地址组列表

        查询地址组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAddressSets
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressSetsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressSetsResponse`
        """
        return self._list_address_sets_with_http_info(request)

    def _list_address_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-sets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAddressSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_attack_logs(self, request):
        """查询攻击日志

        查询攻击日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttackLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListAttackLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAttackLogsResponse`
        """
        return self._list_attack_logs_with_http_info(request)

    def _list_attack_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'src_port' in local_var_params:
            query_params.append(('src_port', local_var_params['src_port']))
        if 'dst_ip' in local_var_params:
            query_params.append(('dst_ip', local_var_params['dst_ip']))
        if 'dst_port' in local_var_params:
            query_params.append(('dst_port', local_var_params['dst_port']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'next_date' in local_var_params:
            query_params.append(('next_date', local_var_params['next_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'attack_type' in local_var_params:
            query_params.append(('attack_type', local_var_params['attack_type']))
        if 'attack_rule' in local_var_params:
            query_params.append(('attack_rule', local_var_params['attack_rule']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'dst_host' in local_var_params:
            query_params.append(('dst_host', local_var_params['dst_host']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))

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
            resource_path='/v1/{project_id}/cfw/logs/attack',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAttackLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_black_white_lists(self, request):
        """查询黑白名单列表

        查询黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBlackWhiteLists
        :type request: :class:`huaweicloudsdkcfw.v1.ListBlackWhiteListsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListBlackWhiteListsResponse`
        """
        return self._list_black_white_lists_with_http_info(request)

    def _list_black_white_lists_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'list_type' in local_var_params:
            query_params.append(('list_type', local_var_params['list_type']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'address' in local_var_params:
            query_params.append(('address', local_var_params['address']))
        if 'port' in local_var_params:
            query_params.append(('port', local_var_params['port']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/black-white-lists',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBlackWhiteListsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dns_servers(self, request):
        """查询dns服务器列表

        查询dns服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDnsServers
        :type request: :class:`huaweicloudsdkcfw.v1.ListDnsServersRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDnsServersResponse`
        """
        return self._list_dns_servers_with_http_info(request)

    def _list_dns_servers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/dns/servers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDnsServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_parse_detail(self, request):
        """查询域名解析ip地址

        测试域名有效性
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainParseDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainParseDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainParseDetailResponse`
        """
        return self._list_domain_parse_detail_with_http_info(request)

    def _list_domain_parse_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_name' in local_var_params:
            path_params['domain_name'] = local_var_params['domain_name']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))

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
            resource_path='/v1/{project_id}/domain/parse/{domain_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainParseDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_sets(self, request):
        """查询域名组列表

        查询域名组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainSets
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainSetsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainSetsResponse`
        """
        return self._list_domain_sets_with_http_info(request)

    def _list_domain_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'domain_set_type' in local_var_params:
            query_params.append(('domain_set_type', local_var_params['domain_set_type']))
        if 'config_status' in local_var_params:
            query_params.append(('config_status', local_var_params['config_status']))

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
            resource_path='/v1/{project_id}/domain-sets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domains(self, request):
        """获取域名组下域名列表

        获取域名组下域名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomains
        :type request: :class:`huaweicloudsdkcfw.v1.ListDomainsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDomainsResponse`
        """
        return self._list_domains_with_http_info(request)

    def _list_domains_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_set_id' in local_var_params:
            path_params['domain_set_id'] = local_var_params['domain_set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
        if 'set_id' in local_var_params:
            query_params.append(('set_id', local_var_params['set_id']))
        if 'object_id' in local_var_params:
            query_params.append(('object_Id', local_var_params['object_id']))

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
            resource_path='/v1/{project_id}/domain-set/domains/{domain_set_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_east_west_firewall(self, request):
        """获取东西向防火墙信息

        获取东西向防火墙信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEastWestFirewall
        :type request: :class:`huaweicloudsdkcfw.v1.ListEastWestFirewallRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEastWestFirewallResponse`
        """
        return self._list_east_west_firewall_with_http_info(request)

    def _list_east_west_firewall_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/firewall/east-west',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEastWestFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_firewall_detail(self, request):
        """查询防火墙详细信息

        查询防火墙实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFirewallDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListFirewallDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFirewallDetailResponse`
        """
        return self._list_firewall_detail_with_http_info(request)

    def _list_firewall_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/firewall/exist',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFirewallDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_firewall_list(self, request):
        """查询防火墙列表

        查询防火墙列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFirewallList
        :type request: :class:`huaweicloudsdkcfw.v1.ListFirewallListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFirewallListResponse`
        """
        return self._list_firewall_list_with_http_info(request)

    def _list_firewall_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/firewalls/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFirewallListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flow_logs(self, request):
        """查询流日志

        查询流日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlowLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListFlowLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFlowLogsResponse`
        """
        return self._list_flow_logs_with_http_info(request)

    def _list_flow_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'src_ip' in local_var_params:
            query_params.append(('src_ip', local_var_params['src_ip']))
        if 'src_port' in local_var_params:
            query_params.append(('src_port', local_var_params['src_port']))
        if 'dst_ip' in local_var_params:
            query_params.append(('dst_ip', local_var_params['dst_ip']))
        if 'dst_port' in local_var_params:
            query_params.append(('dst_port', local_var_params['dst_port']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'app' in local_var_params:
            query_params.append(('app', local_var_params['app']))
        if 'log_id' in local_var_params:
            query_params.append(('log_id', local_var_params['log_id']))
        if 'next_date' in local_var_params:
            query_params.append(('next_date', local_var_params['next_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'dst_host' in local_var_params:
            query_params.append(('dst_host', local_var_params['dst_host']))

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
            resource_path='/v1/{project_id}/cfw/logs/flow',
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

    def list_protected_vpcs(self, request):
        """查询防护VPC数

        查询防护vpc信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProtectedVpcs
        :type request: :class:`huaweicloudsdkcfw.v1.ListProtectedVpcsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListProtectedVpcsResponse`
        """
        return self._list_protected_vpcs_with_http_info(request)

    def _list_protected_vpcs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/vpcs/protection',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectedVpcsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_items(self, request):
        """查询服务成员列表

        查询服务组成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceItems
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceItemsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceItemsResponse`
        """
        return self._list_service_items_with_http_info(request)

    def _list_service_items_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'set_id' in local_var_params:
            query_params.append(('set_id', local_var_params['set_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-items',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServiceItemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_set_detail(self, request):
        """查询服务组详情

        查询服务组细节
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceSetDetail
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceSetDetailRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceSetDetailResponse`
        """
        return self._list_service_set_detail_with_http_info(request)

    def _list_service_set_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-sets/{set_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServiceSetDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_sets(self, request):
        """获取服务组列表

        获取服务组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServiceSets
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceSetsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceSetsResponse`
        """
        return self._list_service_sets_with_http_info(request)

    def _list_service_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-sets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServiceSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_address_set(self, request):
        """更新地址组信息

        更新地址组信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAddressSet
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetResponse`
        """
        return self._update_address_set_with_http_info(request)

    def _update_address_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/address-sets/{set_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAddressSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_black_white_list(self, request):
        """更新黑白名单列表

        更新黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBlackWhiteList
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListResponse`
        """
        return self._update_black_white_list_with_http_info(request)

    def _update_black_white_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/black-white-list/{list_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBlackWhiteListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dns_servers(self, request):
        """更新dns服务器列表

        更新dns服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDnsServers
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateDnsServersRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateDnsServersResponse`
        """
        return self._update_dns_servers_with_http_info(request)

    def _update_dns_servers_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/dns/servers',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDnsServersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_set(self, request):
        """更新域名组

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainSet
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateDomainSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateDomainSetResponse`
        """
        return self._update_domain_set_with_http_info(request)

    def _update_domain_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/domain-set/{set_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_service_set(self, request):
        """修改服务组

        更新服务组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateServiceSetResponse`
        """
        return self._update_service_set_with_http_info(request)

    def _update_service_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'set_id' in local_var_params:
            path_params['set_id'] = local_var_params['set_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/service-sets/{set_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateServiceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_acl_rule(self, request):
        """创建ACL规则

        创建ACL规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAclRule
        :type request: :class:`huaweicloudsdkcfw.v1.AddAclRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAclRuleResponse`
        """
        return self._add_acl_rule_with_http_info(request)

    def _add_acl_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddAclRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_acl_rules(self, request):
        """批量删除Acl规则

        批量删除Acl规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteAclRules
        :type request: :class:`huaweicloudsdkcfw.v1.BatchDeleteAclRulesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchDeleteAclRulesResponse`
        """
        return self._batch_delete_acl_rules_with_http_info(request)

    def _batch_delete_acl_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteAclRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_acl_rule_actions(self, request):
        """批量更新规则动作

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateAclRuleActions
        :type request: :class:`huaweicloudsdkcfw.v1.BatchUpdateAclRuleActionsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.BatchUpdateAclRuleActionsResponse`
        """
        return self._batch_update_acl_rule_actions_with_http_info(request)

    def _batch_update_acl_rule_actions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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
            resource_path='/v1/{project_id}/acl-rule/action',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateAclRuleActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_acl_rule(self, request):
        """删除ACL规则

        删除ACL规则组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAclRule
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleResponse`
        """
        return self._delete_acl_rule_with_http_info(request)

    def _delete_acl_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'acl_rule_id' in local_var_params:
            path_params['acl_rule_id'] = local_var_params['acl_rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule/{acl_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAclRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_acl_rule_hit_count(self, request):
        """删除规则击中次数

        清除规则击中次数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAclRuleHitCount
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleHitCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleHitCountResponse`
        """
        return self._delete_acl_rule_hit_count_with_http_info(request)

    def _delete_acl_rule_hit_count_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule/count',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAclRuleHitCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_rule_hit_count(self, request):
        """获取规则击中次数

        获取规则击中次数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclRuleHitCount
        :type request: :class:`huaweicloudsdkcfw.v1.ListAclRuleHitCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAclRuleHitCountResponse`
        """
        return self._list_acl_rule_hit_count_with_http_info(request)

    def _list_acl_rule_hit_count_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule/count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAclRuleHitCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_rules(self, request):
        """查询防护规则

        查询防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclRules
        :type request: :class:`huaweicloudsdkcfw.v1.ListAclRulesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAclRulesResponse`
        """
        return self._list_acl_rules_with_http_info(request)

    def _list_acl_rules_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'direction' in local_var_params:
            query_params.append(('direction', local_var_params['direction']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'action_type' in local_var_params:
            query_params.append(('action_type', local_var_params['action_type']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'tags_id' in local_var_params:
            query_params.append(('tags_id', local_var_params['tags_id']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))
        if 'destination' in local_var_params:
            query_params.append(('destination', local_var_params['destination']))
        if 'service' in local_var_params:
            query_params.append(('service', local_var_params['service']))

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
            resource_path='/v1/{project_id}/acl-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAclRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_acl_tags(self, request):
        """查询规则标签

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRuleAclTags
        :type request: :class:`huaweicloudsdkcfw.v1.ListRuleAclTagsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListRuleAclTagsResponse`
        """
        return self._list_rule_acl_tags_with_http_info(request)

    def _list_rule_acl_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
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
            resource_path='/v2/{project_id}/cfw-acl/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRuleAclTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_rule(self, request):
        """更新ACL规则

        更新ACL规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclRule
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleResponse`
        """
        return self._update_acl_rule_with_http_info(request)

    def _update_acl_rule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'acl_rule_id' in local_var_params:
            path_params['acl_rule_id'] = local_var_params['acl_rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule/{acl_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAclRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_rule_order(self, request):
        """ACL防护规则优先级设置

        ACL防护规则优先级设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclRuleOrder
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleOrderRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAclRuleOrderResponse`
        """
        return self._update_acl_rule_order_with_http_info(request)

    def _update_acl_rule_order_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'acl_rule_id' in local_var_params:
            path_params['acl_rule_id'] = local_var_params['acl_rule_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/acl-rule/order/{acl_rule_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAclRuleOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_eip_status(self, request):
        """弹性IP开启关闭

        开启关闭EIP,客户购买EIP后首次开启EIP防护前需使用ListEips同步EIP资产，sync字段设置为1。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeEipStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeEipStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeEipStatusResponse`
        """
        return self._change_eip_status_with_http_info(request)

    def _change_eip_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/eip/protect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeEipStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_eip_count(self, request):
        """查询Eip个数

        查询Eip个数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEipCount
        :type request: :class:`huaweicloudsdkcfw.v1.ListEipCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEipCountResponse`
        """
        return self._list_eip_count_with_http_info(request)

    def _list_eip_count_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'object_id' in local_var_params:
            path_params['object_id'] = local_var_params['object_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/eip-count/{object_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEipCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_eips(self, request):
        """弹性IP列表查询

        弹性IP列表查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEips
        :type request: :class:`huaweicloudsdkcfw.v1.ListEipsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEipsResponse`
        """
        return self._list_eips_with_http_info(request)

    def _list_eips_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sync' in local_var_params:
            query_params.append(('sync', local_var_params['sync']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'device_key' in local_var_params:
            query_params.append(('device_key', local_var_params['device_key']))
        if 'address_type' in local_var_params:
            query_params.append(('address_type', local_var_params['address_type']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))
        if 'fw_key_word' in local_var_params:
            query_params.append(('fw_key_word', local_var_params['fw_key_word']))
        if 'eps_id' in local_var_params:
            query_params.append(('eps_id', local_var_params['eps_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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
            resource_path='/v1/{project_id}/eips/protect',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ips_protect_mode(self, request):
        """切换防护模式

        切换防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIpsProtectMode
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsProtectModeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsProtectModeResponse`
        """
        return self._change_ips_protect_mode_with_http_info(request)

    def _change_ips_protect_mode_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/ips/protect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeIpsProtectModeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ips_switch_status(self, request):
        """IPS特性开关操作

        切换开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeIpsSwitchStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsSwitchStatusResponse`
        """
        return self._change_ips_switch_status_with_http_info(request)

    def _change_ips_switch_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/ips/switch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeIpsSwitchStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ips_protect_mode(self, request):
        """查询防护模式

        查询防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpsProtectMode
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsProtectModeRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsProtectModeResponse`
        """
        return self._list_ips_protect_mode_with_http_info(request)

    def _list_ips_protect_mode_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/ips/protect',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIpsProtectModeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ips_switch_status(self, request):
        """查询IPS特性开关状态

        查询IPS特性开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIpsSwitchStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsSwitchStatusResponse`
        """
        return self._list_ips_switch_status_with_http_info(request)

    def _list_ips_switch_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'fw_instance_id' in local_var_params:
            query_params.append(('fw_instance_id', local_var_params['fw_instance_id']))

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
            resource_path='/v1/{project_id}/ips/switch',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIpsSwitchStatusResponse',
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

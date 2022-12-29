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


class CfwAsyncClient(Client):
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
        super(CfwAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcfw.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CfwClient":
            raise TypeError("client type error, support client type is CfwClient")

        return ClientBuilder(clazz)

    def add_address_items_using_post_async(self, request):
        """添加地址组成员

        添加地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAddressItemsUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.AddAddressItemsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAddressItemsUsingPostResponse`
        """
        return self.add_address_items_using_post_with_http_info(request)

    def add_address_items_using_post_with_http_info(self, request):
        all_params = ['add_address_items_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AddAddressItemsUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_address_set_info_using_post_async(self, request):
        """添加地址组

        添加地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddAddressSetInfoUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.AddAddressSetInfoUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddAddressSetInfoUsingPostResponse`
        """
        return self.add_address_set_info_using_post_with_http_info(request)

    def add_address_set_info_using_post_with_http_info(self, request):
        all_params = ['add_address_set_info_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AddAddressSetInfoUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_black_white_list_using_post_async(self, request):
        """创建黑白名单规则

        创建黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddBlackWhiteListUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.AddBlackWhiteListUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddBlackWhiteListUsingPostResponse`
        """
        return self.add_black_white_list_using_post_with_http_info(request)

    def add_black_white_list_using_post_with_http_info(self, request):
        all_params = ['add_black_white_list_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AddBlackWhiteListUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_service_items_using_post_async(self, request):
        """新建服务成员

        批量添加服务组成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddServiceItemsUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.AddServiceItemsUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddServiceItemsUsingPostResponse`
        """
        return self.add_service_items_using_post_with_http_info(request)

    def add_service_items_using_post_with_http_info(self, request):
        all_params = ['add_service_items_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AddServiceItemsUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_service_set_using_post_async(self, request):
        """新建服务组

        创建服务组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddServiceSetUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.AddServiceSetUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddServiceSetUsingPostResponse`
        """
        return self.add_service_set_using_post_with_http_info(request)

    def add_service_set_using_post_with_http_info(self, request):
        all_params = ['add_service_set_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AddServiceSetUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ew_protect_status_async(self, request):
        """修改东西向防火墙防护状态

        东西向防护资源防护开启/关闭
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeEwProtectStatus
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeEwProtectStatusRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeEwProtectStatusResponse`
        """
        return self.change_ew_protect_status_with_http_info(request)

    def change_ew_protect_status_with_http_info(self, request):
        all_params = ['change_ew_protect_status_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeEwProtectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ips_protect_mode_using_post_async(self, request):
        """切换防护模式

        切换防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeIpsProtectModeUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsProtectModeUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsProtectModeUsingPostResponse`
        """
        return self.change_ips_protect_mode_using_post_with_http_info(request)

    def change_ips_protect_mode_using_post_with_http_info(self, request):
        all_params = ['change_ips_protect_mode_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeIpsProtectModeUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_acl_rule_count_async(self, request):
        """删除规则击中次数

        清除规则击中次数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAclRuleCount
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAclRuleCountResponse`
        """
        return self.delete_acl_rule_count_with_http_info(request)

    def delete_acl_rule_count_with_http_info(self, request):
        all_params = ['delete_acl_rule_count_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteAclRuleCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_address_item_using_delete_async(self, request):
        """删除地址组成员

        删除地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAddressItemUsingDelete
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAddressItemUsingDeleteRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAddressItemUsingDeleteResponse`
        """
        return self.delete_address_item_using_delete_with_http_info(request)

    def delete_address_item_using_delete_with_http_info(self, request):
        all_params = ['item_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteAddressItemUsingDeleteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_address_set_info_using_delete_async(self, request):
        """删除地址组

        删除地址组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAddressSetInfoUsingDelete
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteAddressSetInfoUsingDeleteRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteAddressSetInfoUsingDeleteResponse`
        """
        return self.delete_address_set_info_using_delete_with_http_info(request)

    def delete_address_set_info_using_delete_with_http_info(self, request):
        all_params = ['set_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteAddressSetInfoUsingDeleteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_black_white_list_using_delete_async(self, request):
        """删除黑白名单规则

        删除黑白名单规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBlackWhiteListUsingDelete
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteBlackWhiteListUsingDeleteRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteBlackWhiteListUsingDeleteResponse`
        """
        return self.delete_black_white_list_using_delete_with_http_info(request)

    def delete_black_white_list_using_delete_with_http_info(self, request):
        all_params = ['list_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteBlackWhiteListUsingDeleteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_service_item_using_delete_async(self, request):
        """删除服务成员

        删除服务组成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServiceItemUsingDelete
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteServiceItemUsingDeleteRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteServiceItemUsingDeleteResponse`
        """
        return self.delete_service_item_using_delete_with_http_info(request)

    def delete_service_item_using_delete_with_http_info(self, request):
        all_params = ['item_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteServiceItemUsingDeleteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_service_set_using_delete_async(self, request):
        """删除服务组

        删除服务组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServiceSetUsingDelete
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteServiceSetUsingDeleteRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteServiceSetUsingDeleteResponse`
        """
        return self.delete_service_set_using_delete_with_http_info(request)

    def delete_service_set_using_delete_with_http_info(self, request):
        all_params = ['set_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteServiceSetUsingDeleteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_access_control_logs_async(self, request):
        """查询访问控制日志

        查询访问控制日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccessControlLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListAccessControlLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAccessControlLogsResponse`
        """
        return self.list_access_control_logs_with_http_info(request)

    def list_access_control_logs_with_http_info(self, request):
        all_params = ['fw_instance_id', 'start_time', 'end_time', 'limit', 'rule_id', 'src_ip', 'src_port', 'dst_ip', 'dst_port', 'protocol', 'app', 'log_id', 'next_date', 'offset', 'log_type', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_address_items_using_get_async(self, request):
        """查询地址组成员

        查询地址组成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAddressItemsUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressItemsUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressItemsUsingGetResponse`
        """
        return self.list_address_items_using_get_with_http_info(request)

    def list_address_items_using_get_with_http_info(self, request):
        all_params = ['set_id', 'limit', 'offset', 'key_word', 'address', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListAddressItemsUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_address_set_detail_using_get_async(self, request):
        """查询地址组详细信息

        查询地址组详细
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAddressSetDetailUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressSetDetailUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressSetDetailUsingGetResponse`
        """
        return self.list_address_set_detail_using_get_with_http_info(request)

    def list_address_set_detail_using_get_with_http_info(self, request):
        all_params = ['set_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListAddressSetDetailUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_address_set_list_using_get_async(self, request):
        """查询地址组列表

        查询地址组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAddressSetListUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListAddressSetListUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAddressSetListUsingGetResponse`
        """
        return self.list_address_set_list_using_get_with_http_info(request)

    def list_address_set_list_using_get_with_http_info(self, request):
        all_params = ['object_id', 'limit', 'offset', 'key_word', 'address', 'address_type', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListAddressSetListUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_attack_logs_async(self, request):
        """查询攻击日志

        查询攻击日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAttackLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListAttackLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListAttackLogsResponse`
        """
        return self.list_attack_logs_with_http_info(request)

    def list_attack_logs_with_http_info(self, request):
        all_params = ['start_time', 'end_time', 'limit', 'fw_instance_id', 'src_ip', 'src_port', 'dst_ip', 'dst_port', 'protocol', 'app', 'log_id', 'next_date', 'offset', 'action', 'direction', 'attack_type', 'attack_rule', 'level', 'source', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_black_white_lists_using_get_async(self, request):
        """查询黑白名单列表

        查询黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBlackWhiteListsUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListBlackWhiteListsUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListBlackWhiteListsUsingGetResponse`
        """
        return self.list_black_white_lists_using_get_with_http_info(request)

    def list_black_white_lists_using_get_with_http_info(self, request):
        all_params = ['object_id', 'list_type', 'limit', 'offset', 'address_type', 'address', 'port', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListBlackWhiteListsUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dns_servers_async(self, request):
        """查询dns服务器列表

        查询dns服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDnsServers
        :type request: :class:`huaweicloudsdkcfw.v1.ListDnsServersRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListDnsServersResponse`
        """
        return self.list_dns_servers_with_http_info(request)

    def list_dns_servers_with_http_info(self, request):
        all_params = ['limit', 'offset', 'fw_instance_id', 'enterprise_project_id']
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

    def list_east_west_firewall_async(self, request):
        """获取东西向防火墙信息

        查询东西向防火墙信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEastWestFirewall
        :type request: :class:`huaweicloudsdkcfw.v1.ListEastWestFirewallRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEastWestFirewallResponse`
        """
        return self.list_east_west_firewall_with_http_info(request)

    def list_east_west_firewall_with_http_info(self, request):
        all_params = ['limit', 'offset', 'enterprise_project_id', 'fw_instance_id']
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

    def list_firewall_using_get_async(self, request):
        """查询防火墙实例

        查询防火墙实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFirewallUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListFirewallUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFirewallUsingGetResponse`
        """
        return self.list_firewall_using_get_with_http_info(request)

    def list_firewall_using_get_with_http_info(self, request):
        all_params = ['offset', 'limit', 'service_type', 'enterprise_project_id', 'fw_instance_id']
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
            response_type='ListFirewallUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flow_logs_async(self, request):
        """查询流日志

        查询流日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlowLogs
        :type request: :class:`huaweicloudsdkcfw.v1.ListFlowLogsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListFlowLogsResponse`
        """
        return self.list_flow_logs_with_http_info(request)

    def list_flow_logs_with_http_info(self, request):
        all_params = ['fw_instance_id', 'start_time', 'end_time', 'limit', 'direction', 'log_type', 'src_ip', 'src_port', 'dst_ip', 'dst_port', 'protocol', 'app', 'log_id', 'next_date', 'offset', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def list_ips_protect_mode_using_post_async(self, request):
        """查询防护模式

        查询防护模式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIpsProtectModeUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsProtectModeUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsProtectModeUsingPostResponse`
        """
        return self.list_ips_protect_mode_using_post_with_http_info(request)

    def list_ips_protect_mode_using_post_with_http_info(self, request):
        all_params = ['object_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListIpsProtectModeUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_parse_domain_details_async(self, request):
        """查询域名解析ip地址

        测试域名有效性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListParseDomainDetails
        :type request: :class:`huaweicloudsdkcfw.v1.ListParseDomainDetailsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListParseDomainDetailsResponse`
        """
        return self.list_parse_domain_details_with_http_info(request)

    def list_parse_domain_details_with_http_info(self, request):
        all_params = ['domain_name', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListParseDomainDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_hit_count_async(self, request):
        """获取规则击中次数

        获取规则击中次数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuleHitCount
        :type request: :class:`huaweicloudsdkcfw.v1.ListRuleHitCountRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListRuleHitCountResponse`
        """
        return self.list_rule_hit_count_with_http_info(request)

    def list_rule_hit_count_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'fw_instance_id', 'list_rule_hit_count_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListRuleHitCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_items_details_async(self, request):
        """查询服务成员列表

        查询服务组成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceItemsDetails
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceItemsDetailsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceItemsDetailsResponse`
        """
        return self.list_service_items_details_with_http_info(request)

    def list_service_items_details_with_http_info(self, request):
        all_params = ['set_id', 'limit', 'offset', 'key_word', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListServiceItemsDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_set_async(self, request):
        """获取服务组列表

        获取服务组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceSet
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceSetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceSetResponse`
        """
        return self.list_service_set_with_http_info(request)

    def list_service_set_with_http_info(self, request):
        all_params = ['object_id', 'limit', 'offset', 'key_word', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListServiceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_service_set_details_async(self, request):
        """查询服务组详情

        查询服务组细节
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServiceSetDetails
        :type request: :class:`huaweicloudsdkcfw.v1.ListServiceSetDetailsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListServiceSetDetailsResponse`
        """
        return self.list_service_set_details_with_http_info(request)

    def list_service_set_details_with_http_info(self, request):
        all_params = ['set_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListServiceSetDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_address_set_info_using_put_async(self, request):
        """更新地址组信息

        更新地址组信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAddressSetInfoUsingPut
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetInfoUsingPutRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateAddressSetInfoUsingPutResponse`
        """
        return self.update_address_set_info_using_put_with_http_info(request)

    def update_address_set_info_using_put_with_http_info(self, request):
        all_params = ['set_id', 'update_address_set_info_using_put_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateAddressSetInfoUsingPutResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_black_white_list_using_put_async(self, request):
        """更新黑白名单列表

        更新黑白名单列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBlackWhiteListUsingPut
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListUsingPutRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateBlackWhiteListUsingPutResponse`
        """
        return self.update_black_white_list_using_put_with_http_info(request)

    def update_black_white_list_using_put_with_http_info(self, request):
        all_params = ['list_id', 'update_black_white_list_using_put_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateBlackWhiteListUsingPutResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dns_servers_async(self, request):
        """更新dns服务器列表

        更新dns服务器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDnsServers
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateDnsServersRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateDnsServersResponse`
        """
        return self.update_dns_servers_with_http_info(request)

    def update_dns_servers_with_http_info(self, request):
        all_params = ['update_dns_servers_request_body', 'fw_instance_id', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_service_set_using_put_async(self, request):
        """修改服务组

        更新服务组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServiceSetUsingPut
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateServiceSetUsingPutRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateServiceSetUsingPutResponse`
        """
        return self.update_service_set_using_put_with_http_info(request)

    def update_service_set_using_put_with_http_info(self, request):
        all_params = ['set_id', 'update_service_set_using_put_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateServiceSetUsingPutResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_rule_acl_using_post_async(self, request):
        """创建ACL规则

        创建ACL规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRuleAclUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.AddRuleAclUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.AddRuleAclUsingPostResponse`
        """
        return self.add_rule_acl_using_post_with_http_info(request)

    def add_rule_acl_using_post_with_http_info(self, request):
        all_params = ['add_rule_acl_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='AddRuleAclUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule_acl_using_delete_async(self, request):
        """删除ACL规则组

        删除ACL规则组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRuleAclUsingDelete
        :type request: :class:`huaweicloudsdkcfw.v1.DeleteRuleAclUsingDeleteRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.DeleteRuleAclUsingDeleteResponse`
        """
        return self.delete_rule_acl_using_delete_with_http_info(request)

    def delete_rule_acl_using_delete_with_http_info(self, request):
        all_params = ['acl_rule_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteRuleAclUsingDeleteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_acl_using_put_async(self, request):
        """ACL防护规则优先级设置

        ACL防护规则优先级设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuleAclUsingPut
        :type request: :class:`huaweicloudsdkcfw.v1.ListRuleAclUsingPutRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListRuleAclUsingPutResponse`
        """
        return self.list_rule_acl_using_put_with_http_info(request)

    def list_rule_acl_using_put_with_http_info(self, request):
        all_params = ['acl_rule_id', 'list_rule_acl_using_put_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListRuleAclUsingPutResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_acls_using_get_async(self, request):
        """查询防护规则

        查询防护规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuleAclsUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListRuleAclsUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListRuleAclsUsingGetResponse`
        """
        return self.list_rule_acls_using_get_with_http_info(request)

    def list_rule_acls_using_get_with_http_info(self, request):
        all_params = ['object_id', 'limit', 'offset', 'type', 'protocol', 'ip', 'name', 'direction', 'status', 'action_type', 'address_type', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListRuleAclsUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_rule_acl_using_put_async(self, request):
        """更新ACL规则

        更新ACL规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRuleAclUsingPut
        :type request: :class:`huaweicloudsdkcfw.v1.UpdateRuleAclUsingPutRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.UpdateRuleAclUsingPutResponse`
        """
        return self.update_rule_acl_using_put_with_http_info(request)

    def update_rule_acl_using_put_with_http_info(self, request):
        all_params = ['acl_rule_id', 'update_rule_acl_using_put_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateRuleAclUsingPutResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ips_switch_using_post_async(self, request):
        """IPS特性开关操作

        切换开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeIpsSwitchUsingPost
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeIpsSwitchUsingPostRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeIpsSwitchUsingPostResponse`
        """
        return self.change_ips_switch_using_post_with_http_info(request)

    def change_ips_switch_using_post_with_http_info(self, request):
        all_params = ['change_ips_switch_using_post_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeIpsSwitchUsingPostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ips_switch_status_using_get_async(self, request):
        """查询IPS特性开关状态

        查询IPS特性开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListIpsSwitchStatusUsingGet
        :type request: :class:`huaweicloudsdkcfw.v1.ListIpsSwitchStatusUsingGetRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListIpsSwitchStatusUsingGetResponse`
        """
        return self.list_ips_switch_status_using_get_with_http_info(request)

    def list_ips_switch_status_using_get_with_http_info(self, request):
        all_params = ['object_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListIpsSwitchStatusUsingGetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_protect_eip_async(self, request):
        """弹性IP开启关闭

        开启关闭EIP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeProtectEip
        :type request: :class:`huaweicloudsdkcfw.v1.ChangeProtectEipRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ChangeProtectEipResponse`
        """
        return self.change_protect_eip_with_http_info(request)

    def change_protect_eip_with_http_info(self, request):
        all_params = ['change_protect_eip_request_body', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ChangeProtectEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_eips_async(self, request):
        """查询Eip个数

        查询Eip个数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountEips
        :type request: :class:`huaweicloudsdkcfw.v1.CountEipsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.CountEipsResponse`
        """
        return self.count_eips_with_http_info(request)

    def count_eips_with_http_info(self, request):
        all_params = ['object_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CountEipsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_eip_resources_async(self, request):
        """弹性IP列表查询

        弹性IP列表查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEipResources
        :type request: :class:`huaweicloudsdkcfw.v1.ListEipResourcesRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListEipResourcesResponse`
        """
        return self.list_eip_resources_with_http_info(request)

    def list_eip_resources_with_http_info(self, request):
        all_params = ['object_id', 'limit', 'offset', 'key_word', 'status', 'sync', 'enterprise_project_id', 'device_key', 'address_type', 'fw_instance_id', 'fw_key_word', 'eps_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListEipResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vpc_protects_async(self, request):
        """查询防护VPC数

        查询防护vpc信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVpcProtects
        :type request: :class:`huaweicloudsdkcfw.v1.ListVpcProtectsRequest`
        :rtype: :class:`huaweicloudsdkcfw.v1.ListVpcProtectsResponse`
        """
        return self.list_vpc_protects_with_http_info(request)

    def list_vpc_protects_with_http_info(self, request):
        all_params = ['object_id', 'enterprise_project_id', 'fw_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListVpcProtectsResponse',
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

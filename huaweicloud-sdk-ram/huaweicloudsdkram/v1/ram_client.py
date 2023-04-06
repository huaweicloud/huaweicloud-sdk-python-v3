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


class RamClient(Client):
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
        super(RamClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkram.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "RamClient":
            raise TypeError("client type error, support client type is RamClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def associate_resource_share_permission(self, request):
        """绑定或替换共享资源权限

        为资源共享实例中包含的资源类型绑定或替换共享资源权限。 对于资源共享实例中的每一种资源类型，您可以设置唯一权限。仅当资源共享实例中当前没有该资源类型的资源时，您才能绑定新的共享资源权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateResourceSharePermission
        :type request: :class:`huaweicloudsdkram.v1.AssociateResourceSharePermissionRequest`
        :rtype: :class:`huaweicloudsdkram.v1.AssociateResourceSharePermissionResponse`
        """
        return self.associate_resource_share_permission_with_http_info(request)

    def associate_resource_share_permission_with_http_info(self, request):
        all_params = ['resource_share_id', 'associate_permission_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/associate-permission',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateResourceSharePermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_resource_share_permission(self, request):
        """移除共享资源权限

        移除资源共享实例绑定的共享资源权限。权限更改立即生效。只有当目前资源共享实例中没有绑定相关资源类型时，您才能从资源共享实例中移除共享资源权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateResourceSharePermission
        :type request: :class:`huaweicloudsdkram.v1.DisassociateResourceSharePermissionRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DisassociateResourceSharePermissionResponse`
        """
        return self.disassociate_resource_share_permission_with_http_info(request)

    def disassociate_resource_share_permission_with_http_info(self, request):
        all_params = ['resource_share_id', 'disassociate_permission_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/disassociate-permission',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateResourceSharePermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_share_permissions(self, request):
        """检索绑定的共享资源权限

        检索资源共享实例关联的共享资源权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceSharePermissions
        :type request: :class:`huaweicloudsdkram.v1.ListResourceSharePermissionsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceSharePermissionsResponse`
        """
        return self.list_resource_share_permissions_with_http_info(request)

    def list_resource_share_permissions_with_http_info(self, request):
        all_params = ['resource_share_id', 'permission_name', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

        query_params = []
        if 'permission_name' in local_var_params:
            query_params.append(('permission_name', local_var_params['permission_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/associated-permissions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceSharePermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_organization_share(self, request):
        """关闭与组织共享

        关闭与组织共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableOrganizationShare
        :type request: :class:`huaweicloudsdkram.v1.DisableOrganizationShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DisableOrganizationShareResponse`
        """
        return self.disable_organization_share_with_http_info(request)

    def disable_organization_share_with_http_info(self, request):
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organization-share/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableOrganizationShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_organization_share(self, request):
        """启用与组织共享

        启用与组织共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableOrganizationShare
        :type request: :class:`huaweicloudsdkram.v1.EnableOrganizationShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.EnableOrganizationShareResponse`
        """
        return self.enable_organization_share_with_http_info(request)

    def enable_organization_share_with_http_info(self, request):
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organization-share/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableOrganizationShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization_share(self, request):
        """检索是否启用与组织共享

        检索是否启用与组织共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganizationShare
        :type request: :class:`huaweicloudsdkram.v1.ShowOrganizationShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ShowOrganizationShareResponse`
        """
        return self.show_organization_share_with_http_info(request)

    def show_organization_share_with_http_info(self, request):
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organization-share',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permissions(self, request):
        """检索共享资源权限列表

        检索指定资源类型的共享资源权限列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissions
        :type request: :class:`huaweicloudsdkram.v1.ListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListPermissionsResponse`
        """
        return self.list_permissions_with_http_info(request)

    def list_permissions_with_http_info(self, request):
        all_params = ['limit', 'marker', 'resource_type']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/permissions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_permission(self, request):
        """检索资源共享权限内容

        检索指定资源类型的共享资源权限内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPermission
        :type request: :class:`huaweicloudsdkram.v1.ShowPermissionRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ShowPermissionResponse`
        """
        return self.show_permission_with_http_info(request)

    def show_permission_with_http_info(self, request):
        all_params = ['permission_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'permission_id' in local_var_params:
            path_params['permission_id'] = local_var_params['permission_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/permissions/{permission_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_distinct_principals(self, request):
        """检索去重的共享的角色

        检索您正在共享资源的不同角色或被共享资源给您的不同角色。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDistinctPrincipals
        :type request: :class:`huaweicloudsdkram.v1.SearchDistinctPrincipalsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchDistinctPrincipalsResponse`
        """
        return self.search_distinct_principals_with_http_info(request)

    def search_distinct_principals_with_http_info(self, request):
        all_params = ['search_distinct_shared_principals_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/shared-principals/search-distinct-principal',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchDistinctPrincipalsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_shared_principals(self, request):
        """检索资源使用者

        检索共享资源的使用者。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchSharedPrincipals
        :type request: :class:`huaweicloudsdkram.v1.SearchSharedPrincipalsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchSharedPrincipalsResponse`
        """
        return self.search_shared_principals_with_http_info(request)

    def search_shared_principals_with_http_info(self, request):
        all_params = ['search_shared_principals_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/shared-principals/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchSharedPrincipalsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_distinct_shared_resources(self, request):
        """检索去重的共享的资源

        检索您添加到资源共享或被共享给您的不同资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchDistinctSharedResources
        :type request: :class:`huaweicloudsdkram.v1.SearchDistinctSharedResourcesRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchDistinctSharedResourcesResponse`
        """
        return self.search_distinct_shared_resources_with_http_info(request)

    def search_distinct_shared_resources_with_http_info(self, request):
        all_params = ['search_distinct_shared_resources_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/shared-resources/search-distinct-resource',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchDistinctSharedResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_shared_resources(self, request):
        """检索共享的资源

        检索您共享的或共享给您的资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchSharedResources
        :type request: :class:`huaweicloudsdkram.v1.SearchSharedResourcesRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchSharedResourcesResponse`
        """
        return self.search_shared_resources_with_http_info(request)

    def search_shared_resources_with_http_info(self, request):
        all_params = ['search_shared_resources_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/shared-resources/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchSharedResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource_share(self, request):
        """创建资源共享实例

        创建一个资源共享实例。您可以指定需要共享的资源列表，资源使用者列表，以及授予资源使用者的权限列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.CreateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.CreateResourceShareResponse`
        """
        return self.create_resource_share_with_http_info(request)

    def create_resource_share_with_http_info(self, request):
        all_params = ['create_resource_share_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_resource_share(self, request):
        """删除资源共享实例

        删除指定的资源共享实例。此操作不会删除实体资源，仅停止向其他帐号共享资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResourceShare
        :type request: :class:`huaweicloudsdkram.v1.DeleteResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DeleteResourceShareResponse`
        """
        return self.delete_resource_share_with_http_info(request)

    def delete_resource_share_with_http_info(self, request):
        all_params = ['resource_share_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_resource_shares(self, request):
        """检索资源共享实例

        检索您创建的或者共享给您的资源共享实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchResourceShares
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceSharesRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceSharesResponse`
        """
        return self.search_resource_shares_with_http_info(request)

    def search_resource_shares_with_http_info(self, request):
        all_params = ['search_resource_shares_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchResourceSharesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_resource_share(self, request):
        """更新资源共享实例

        修改资源共享实例的特定属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.UpdateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.UpdateResourceShareResponse`
        """
        return self.update_resource_share_with_http_info(request)

    def update_resource_share_with_http_info(self, request):
        all_params = ['resource_share_id', 'update_resource_share_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateResourceShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_resource_share(self, request):
        """绑定资源使用者和共享资源

        向资源共享实例绑定指定的资源使用者列表或共享资源列表。对于新增的共享资源，有权访问此资源共享实例的资源使用者获得该共享资源的访问权限。对于新增的资源使用者，获得对此资源共享实例中共享资源的访问权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.AssociateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.AssociateResourceShareResponse`
        """
        return self.associate_resource_share_with_http_info(request)

    def associate_resource_share_with_http_info(self, request):
        all_params = ['resource_share_id', 'resource_share_association_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/associate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateResourceShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disassociate_resource_share(self, request):
        """移除资源使用者和共享资源

        将指定的资源使用者或共享资源从指定的资源共享实例中移除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateResourceShare
        :type request: :class:`huaweicloudsdkram.v1.DisassociateResourceShareRequest`
        :rtype: :class:`huaweicloudsdkram.v1.DisassociateResourceShareResponse`
        """
        return self.disassociate_resource_share_with_http_info(request)

    def disassociate_resource_share_with_http_info(self, request):
        all_params = ['resource_share_id', 'resource_share_association_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/disassociate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisassociateResourceShareResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_resource_share_associations(self, request):
        """检索绑定的资源使用者和共享资源

        检索您拥有的资源共享实例中绑定的共享资源和资源使用者。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchResourceShareAssociations
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceShareAssociationsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceShareAssociationsResponse`
        """
        return self.search_resource_share_associations_with_http_info(request)

    def search_resource_share_associations_with_http_info(self, request):
        all_params = ['search_resource_share_associations_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-share-associations/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchResourceShareAssociationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def accept_resource_share_invitation(self, request):
        """接受共享邀请

        接受来自其他帐号的资源共享邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AcceptResourceShareInvitation
        :type request: :class:`huaweicloudsdkram.v1.AcceptResourceShareInvitationRequest`
        :rtype: :class:`huaweicloudsdkram.v1.AcceptResourceShareInvitationResponse`
        """
        return self.accept_resource_share_invitation_with_http_info(request)

    def accept_resource_share_invitation_with_http_info(self, request):
        all_params = ['resource_share_invitation_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_invitation_id' in local_var_params:
            path_params['resource_share_invitation_id'] = local_var_params['resource_share_invitation_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-share-invitations/{resource_share_invitation_id}/accept',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AcceptResourceShareInvitationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reject_resource_share_invitation(self, request):
        """拒绝共享邀请

        拒绝来自其他帐号的资源共享邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RejectResourceShareInvitation
        :type request: :class:`huaweicloudsdkram.v1.RejectResourceShareInvitationRequest`
        :rtype: :class:`huaweicloudsdkram.v1.RejectResourceShareInvitationResponse`
        """
        return self.reject_resource_share_invitation_with_http_info(request)

    def reject_resource_share_invitation_with_http_info(self, request):
        all_params = ['resource_share_invitation_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_invitation_id' in local_var_params:
            path_params['resource_share_invitation_id'] = local_var_params['resource_share_invitation_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-share-invitations/{resource_share_invitation_id}/reject',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RejectResourceShareInvitationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_resource_share_invitation(self, request):
        """检索共享邀请

        通过条件检索资源共享邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchResourceShareInvitation
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceShareInvitationRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceShareInvitationResponse`
        """
        return self.search_resource_share_invitation_with_http_info(request)

    def search_resource_share_invitation_with_http_info(self, request):
        all_params = ['search_resource_share_invitation_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-share-invitations/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchResourceShareInvitationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_resource_share_tags(self, request):
        """资源共享实例增加标签

        资源共享实例增加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateResourceShareTags
        :type request: :class:`huaweicloudsdkram.v1.BatchCreateResourceShareTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.BatchCreateResourceShareTagsResponse`
        """
        return self.batch_create_resource_share_tags_with_http_info(request)

    def batch_create_resource_share_tags_with_http_info(self, request):
        all_params = ['resource_share_id', 'tag_resource_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateResourceShareTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_resource_share_tags(self, request):
        """删除资源共享实例的标签

        删除资源共享实例指定的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceShareTags
        :type request: :class:`huaweicloudsdkram.v1.BatchDeleteResourceShareTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.BatchDeleteResourceShareTagsResponse`
        """
        return self.batch_delete_resource_share_tags_with_http_info(request)

    def batch_delete_resource_share_tags_with_http_info(self, request):
        all_params = ['resource_share_id', 'untag_resource_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_share_id' in local_var_params:
            path_params['resource_share_id'] = local_var_params['resource_share_id']

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/{resource_share_id}/tags/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteResourceShareTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_share_tags(self, request):
        """查询已经使用的标签列表

        查询的标签相信列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceShareTags
        :type request: :class:`huaweicloudsdkram.v1.ListResourceShareTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceShareTagsResponse`
        """
        return self.list_resource_share_tags_with_http_info(request)

    def list_resource_share_tags_with_http_info(self, request):
        all_params = ['limit', 'marker']
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceShareTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_shares_by_tags(self, request):
        """根据标签信息查询实例列表

        根据标签信息查询实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceSharesByTags
        :type request: :class:`huaweicloudsdkram.v1.ListResourceSharesByTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.ListResourceSharesByTagsResponse`
        """
        return self.list_resource_shares_by_tags_with_http_info(request)

    def list_resource_shares_by_tags_with_http_info(self, request):
        all_params = ['resource_shares_by_tags_req_body', 'limit', 'offset']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/resource-instances/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceSharesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_resource_share_count_by_tags(self, request):
        """根据标签信息查询实例数量

        根据标签信息查询实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchResourceShareCountByTags
        :type request: :class:`huaweicloudsdkram.v1.SearchResourceShareCountByTagsRequest`
        :rtype: :class:`huaweicloudsdkram.v1.SearchResourceShareCountByTagsResponse`
        """
        return self.search_resource_share_count_by_tags_with_http_info(request)

    def search_resource_share_count_by_tags_with_http_info(self, request):
        all_params = ['resource_shares_by_tags_req_body']
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/resource-shares/resource-instances/count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchResourceShareCountByTagsResponse',
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

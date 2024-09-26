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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodehub'")


class CodeHubAsyncClient(Client):
    def __init__(self):
        super(CodeHubAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodehub.v4.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeHubAsyncClient":
                raise TypeError("client type error, support client type is CodeHubAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def associate_group_user_group_async(self, request):
        """关联代码组与成员组

        关联代码组与成员组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateGroupUserGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.AssociateGroupUserGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AssociateGroupUserGroupResponse`
        """
        http_info = self._associate_group_user_group_http_info(request)
        return self._call_api(**http_info)

    def associate_group_user_group_async_invoker(self, request):
        http_info = self._associate_group_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_group_user_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/groups/{group_id}/user-group/{user_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateGroupUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'user_group_id' in local_var_params:
            path_params['user_group_id'] = local_var_params['user_group_id']

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

    def associate_repository_user_group_async(self, request):
        """关联仓库与成员组

        关联仓库与成员组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRepositoryUserGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.AssociateRepositoryUserGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AssociateRepositoryUserGroupResponse`
        """
        http_info = self._associate_repository_user_group_http_info(request)
        return self._call_api(**http_info)

    def associate_repository_user_group_async_invoker(self, request):
        http_info = self._associate_repository_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_repository_user_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/repositories/{repository_id}/user-group/{user_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRepositoryUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'user_group_id' in local_var_params:
            path_params['user_group_id'] = local_var_params['user_group_id']

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

    def create_group_async(self, request):
        """创建代码组

        创建代码组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateGroupResponse`
        """
        http_info = self._create_group_http_info(request)
        return self._call_api(**http_info)

    def create_group_async_invoker(self, request):
        http_info = self._create_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def delete_group_async(self, request):
        """删除代码组

        删除代码组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteGroupResponse`
        """
        http_info = self._delete_group_http_info(request)
        return self._call_api(**http_info)

    def delete_group_async_invoker(self, request):
        http_info = self._delete_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/{project_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_manageable_groups_async(self, request):
        """项目下拥有创建权限的代码组列表

        项目下拥有创建权限的代码组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListManageableGroups
        :type request: :class:`huaweicloudsdkcodehub.v4.ListManageableGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListManageableGroupsResponse`
        """
        http_info = self._list_manageable_groups_http_info(request)
        return self._call_api(**http_info)

    def list_manageable_groups_async_invoker(self, request):
        http_info = self._list_manageable_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_manageable_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{project_id}/manageable-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListManageableGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_group_async(self, request):
        """获取代码组信息

        获取代码组信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupResponse`
        """
        http_info = self._show_group_http_info(request)
        return self._call_api(**http_info)

    def show_group_async_invoker(self, request):
        http_info = self._show_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{project_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def add_trusted_ip_address_async(self, request):
        """添加仓库ip白名单

        添加仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressResponse`
        """
        http_info = self._add_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def add_trusted_ip_address_async_invoker(self, request):
        http_info = self._add_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "AddTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_trusted_ip_address_async(self, request):
        """删除仓库ip白名单

        删除仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteTrustedIpAddressResponse`
        """
        http_info = self._delete_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def delete_trusted_ip_address_async_invoker(self, request):
        http_info = self._delete_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def list_trusted_ip_addresses_async(self, request):
        """获取仓库ip白名单

        获取仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrustedIpAddresses
        :type request: :class:`huaweicloudsdkcodehub.v4.ListTrustedIpAddressesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListTrustedIpAddressesResponse`
        """
        http_info = self._list_trusted_ip_addresses_http_info(request)
        return self._call_api(**http_info)

    def list_trusted_ip_addresses_async_invoker(self, request):
        http_info = self._list_trusted_ip_addresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_trusted_ip_addresses_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrustedIpAddressesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

        response_headers = ["X-Total", ]

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

    def lock_repository_async(self, request):
        """根据仓库短ID锁定仓库

        根据仓库短ID锁定仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LockRepository
        :type request: :class:`huaweicloudsdkcodehub.v4.LockRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.LockRepositoryResponse`
        """
        http_info = self._lock_repository_http_info(request)
        return self._call_api(**http_info)

    def lock_repository_async_invoker(self, request):
        http_info = self._lock_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _lock_repository_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/repositories/{repository_id}/lock",
            "request_type": request.__class__.__name__,
            "response_type": "LockRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def unlock_repository_async(self, request):
        """根据仓库短ID解锁仓库

        根据仓库短ID解锁仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnlockRepository
        :type request: :class:`huaweicloudsdkcodehub.v4.UnlockRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UnlockRepositoryResponse`
        """
        http_info = self._unlock_repository_http_info(request)
        return self._call_api(**http_info)

    def unlock_repository_async_invoker(self, request):
        http_info = self._unlock_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unlock_repository_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/repositories/{repository_id}/unlock",
            "request_type": request.__class__.__name__,
            "response_type": "UnlockRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def update_trusted_ip_address_async(self, request):
        """修改仓库ip白名单

        修改仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateTrustedIpAddressResponse`
        """
        http_info = self._update_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def update_trusted_ip_address_async_invoker(self, request):
        http_info = self._update_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def add_tenant_trusted_ip_address_async(self, request):
        """添加租户ip白名单

        添加租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddTenantTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.AddTenantTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddTenantTrustedIpAddressResponse`
        """
        http_info = self._add_tenant_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def add_tenant_trusted_ip_address_async_invoker(self, request):
        http_info = self._add_tenant_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_tenant_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/tenant/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "AddTenantTrustedIpAddressResponse"
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

    def delete_tenant_trusted_ip_address_async(self, request):
        """删除租户ip白名单

        删除租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTenantTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteTenantTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteTenantTrustedIpAddressResponse`
        """
        http_info = self._delete_tenant_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def delete_tenant_trusted_ip_address_async_invoker(self, request):
        http_info = self._delete_tenant_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tenant_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/tenant/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTenantTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def list_tenant_trusted_ip_addresses_async(self, request):
        """获取租户ip白名单

        获取租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTenantTrustedIpAddresses
        :type request: :class:`huaweicloudsdkcodehub.v4.ListTenantTrustedIpAddressesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListTenantTrustedIpAddressesResponse`
        """
        http_info = self._list_tenant_trusted_ip_addresses_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_trusted_ip_addresses_async_invoker(self, request):
        http_info = self._list_tenant_trusted_ip_addresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tenant_trusted_ip_addresses_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/tenant/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantTrustedIpAddressesResponse"
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

        response_headers = ["X-Total", ]

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

    def update_tenant_trusted_ip_address_async(self, request):
        """修改租户ip白名单

        修改租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTenantTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateTenantTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateTenantTrustedIpAddressResponse`
        """
        http_info = self._update_tenant_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def update_tenant_trusted_ip_address_async_invoker(self, request):
        http_info = self._update_tenant_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_tenant_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/tenant/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTenantTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

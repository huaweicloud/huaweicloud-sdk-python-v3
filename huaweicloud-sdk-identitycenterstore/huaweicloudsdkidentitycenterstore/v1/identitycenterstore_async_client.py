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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidentitycenterstore'")


class IdentityCenterStoreAsyncClient(Client):
    def __init__(self):
        super(IdentityCenterStoreAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidentitycenterstore.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IdentityCenterStoreAsyncClient":
                raise TypeError("client type error, support client type is IdentityCenterStoreAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_group_async(self, request):
        """创建用户组

        在指定的身份源中创建一个IAM身份中心用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupResponse`
        """
        http_info = self._create_group_http_info(request)
        return self._call_api(**http_info)

    def create_group_async_invoker(self, request):
        http_info = self._create_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

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
        """删除用户组

        根据用户组ID，删除对应的IAM身份中心用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupResponse`
        """
        http_info = self._delete_group_http_info(request)
        return self._call_api(**http_info)

    def delete_group_async_invoker(self, request):
        http_info = self._delete_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def describe_group_async(self, request):
        """查询用户组详情

        根据用户组ID，查询IAM身份中心用户组的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribeGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupResponse`
        """
        http_info = self._describe_group_http_info(request)
        return self._call_api(**http_info)

    def describe_group_async_invoker(self, request):
        http_info = self._describe_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _describe_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_group_id_async(self, request):
        """查询用户组ID

        根据显示名或外部身份源ID，以精确匹配的方式查询用户组ID。显示名和外部身份源ID两种查询方式二选一，不支持同时传入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetGroupId
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupIdRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupIdResponse`
        """
        http_info = self._get_group_id_http_info(request)
        return self._call_api(**http_info)

    def get_group_id_async_invoker(self, request):
        http_info = self._get_group_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_group_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups/retrieve-group-id",
            "request_type": request.__class__.__name__,
            "response_type": "GetGroupIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_groups_async(self, request):
        """列出用户组

        查询指定身份源下的IAM身份中心用户组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroups
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupsResponse`
        """
        http_info = self._list_groups_http_info(request)
        return self._call_api(**http_info)

    def list_groups_async_invoker(self, request):
        http_info = self._list_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'display_name' in local_var_params:
            query_params.append(('display_name', local_var_params['display_name']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_group_async(self, request):
        """更新用户组

        根据用户组ID，更新对应IAM身份中心用户组的属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupResponse`
        """
        http_info = self._update_group_http_info(request)
        return self._call_api(**http_info)

    def update_group_async_invoker(self, request):
        http_info = self._update_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_group_membership_async(self, request):
        """绑定用户和组

        将用户添加到用户组中，用户和用户组必须在同一身份源下。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGroupMembership
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupMembershipRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupMembershipResponse`
        """
        http_info = self._create_group_membership_http_info(request)
        return self._call_api(**http_info)

    def create_group_membership_async_invoker(self, request):
        http_info = self._create_group_membership_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_group_membership_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/group-memberships",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupMembershipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_group_membership_async(self, request):
        """解绑用户和组

        根据关联关系ID解绑用户和用户组，也就是将用户移出用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGroupMembership
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupMembershipRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupMembershipResponse`
        """
        http_info = self._delete_group_membership_http_info(request)
        return self._call_api(**http_info)

    def delete_group_membership_async_invoker(self, request):
        http_info = self._delete_group_membership_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_group_membership_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/group-memberships/{membership_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupMembershipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'membership_id' in local_var_params:
            path_params['membership_id'] = local_var_params['membership_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def describe_group_membership_async(self, request):
        """查询绑定关系详情

        根据关联关系ID，查询此关联关系的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribeGroupMembership
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupMembershipRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupMembershipResponse`
        """
        http_info = self._describe_group_membership_http_info(request)
        return self._call_api(**http_info)

    def describe_group_membership_async_invoker(self, request):
        http_info = self._describe_group_membership_http_info(request)
        return AsyncInvoker(self, http_info)

    def _describe_group_membership_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/group-memberships/{membership_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeGroupMembershipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'membership_id' in local_var_params:
            path_params['membership_id'] = local_var_params['membership_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_group_membership_id_async(self, request):
        """查询绑定关系ID

        根据用户ID和用户组ID，查询对应的关联关系ID。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetGroupMembershipId
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupMembershipIdRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupMembershipIdResponse`
        """
        http_info = self._get_group_membership_id_http_info(request)
        return self._call_api(**http_info)

    def get_group_membership_id_async_invoker(self, request):
        http_info = self._get_group_membership_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_group_membership_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/group-memberships/retrieve-group-membership-id",
            "request_type": request.__class__.__name__,
            "response_type": "GetGroupMembershipIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def is_member_in_groups_async(self, request):
        """查询用户是否为用户组成员

        根据用户ID和用户组ID列表，查询用户是否为用户组的成员。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for IsMemberInGroups
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.IsMemberInGroupsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.IsMemberInGroupsResponse`
        """
        http_info = self._is_member_in_groups_http_info(request)
        return self._call_api(**http_info)

    def is_member_in_groups_async_invoker(self, request):
        http_info = self._is_member_in_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _is_member_in_groups_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/is-member-in-groups",
            "request_type": request.__class__.__name__,
            "response_type": "IsMemberInGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_group_memberships_async(self, request):
        """列出组中的用户

        根据用户组ID，列出用户组中的用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupMemberships
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsResponse`
        """
        http_info = self._list_group_memberships_http_info(request)
        return self._call_api(**http_info)

    def list_group_memberships_async_invoker(self, request):
        http_info = self._list_group_memberships_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_memberships_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/group-memberships",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupMembershipsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_group_memberships_for_member_async(self, request):
        """列出用户加入的组

        根据用户ID，列出用户加入的用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupMembershipsForMember
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsForMemberRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsForMemberResponse`
        """
        http_info = self._list_group_memberships_for_member_http_info(request)
        return self._call_api(**http_info)

    def list_group_memberships_for_member_async_invoker(self, request):
        http_info = self._list_group_memberships_for_member_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_memberships_for_member_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/group-memberships-for-member",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupMembershipsForMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_user_async(self, request):
        """创建用户

        在指定的身份源中创建一个IAM身份中心用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_async_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_user_async(self, request):
        """删除用户

        根据用户ID，删除对应的IAM身份中心用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_async_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def describe_user_async(self, request):
        """查询用户详情

        根据用户ID，查询对应IAM身份中心用户的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribeUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeUserResponse`
        """
        http_info = self._describe_user_http_info(request)
        return self._call_api(**http_info)

    def describe_user_async_invoker(self, request):
        http_info = self._describe_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _describe_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def get_user_id_async(self, request):
        """查询用户ID

        根据用户名或外部身份源ID，以精确匹配的方式查询用户ID。用户名和外部身份源ID两种查询方式二选一，不支持同时传入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for GetUserId
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetUserIdRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetUserIdResponse`
        """
        http_info = self._get_user_id_http_info(request)
        return self._call_api(**http_info)

    def get_user_id_async_invoker(self, request):
        http_info = self._get_user_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _get_user_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/retrieve-user-id",
            "request_type": request.__class__.__name__,
            "response_type": "GetUserIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_users_async(self, request):
        """列出用户

        查询指定身份源下的IAM身份中心用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_async_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_user_async(self, request):
        """更新用户

        根据用户ID，更新对应IAM身份中心用户的属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_async_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

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

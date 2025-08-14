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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidentitycenterstore'")


class IdentityCenterStoreClient(Client):
    def __init__(self):
        super(IdentityCenterStoreClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidentitycenterstore.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IdentityCenterStoreClient":
                raise TypeError("client type error, support client type is IdentityCenterStoreClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_group(self, request):
        r"""创建用户组

        在指定的身份源中创建一个IAM身份中心用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupResponse`
        """
        http_info = self._create_group_http_info(request)
        return self._call_api(**http_info)

    def create_group_invoker(self, request):
        http_info = self._create_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_group_http_info(cls, request):
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

    def delete_group(self, request):
        r"""删除用户组

        根据用户组ID，删除对应的IAM身份中心用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupResponse`
        """
        http_info = self._delete_group_http_info(request)
        return self._call_api(**http_info)

    def delete_group_invoker(self, request):
        http_info = self._delete_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_group_http_info(cls, request):
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

    def describe_group(self, request):
        r"""查询用户组详情

        根据用户组ID，查询IAM身份中心用户组的详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupResponse`
        """
        http_info = self._describe_group_http_info(request)
        return self._call_api(**http_info)

    def describe_group_invoker(self, request):
        http_info = self._describe_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_group_http_info(cls, request):
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

    def describe_groups(self, request):
        r"""批量查询指定用户组详情

        批量查询指定用户组详情。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeGroups
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupsResponse`
        """
        http_info = self._describe_groups_http_info(request)
        return self._call_api(**http_info)

    def describe_groups_invoker(self, request):
        http_info = self._describe_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_groups_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/groups/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeGroupsResponse"
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

    def get_group_id(self, request):
        r"""查询用户组ID

        根据显示名或外部身份源ID，以精确匹配的方式查询用户组ID。显示名和外部身份源ID两种查询方式二选一，不支持同时传入。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetGroupId
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupIdRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupIdResponse`
        """
        http_info = self._get_group_id_http_info(request)
        return self._call_api(**http_info)

    def get_group_id_invoker(self, request):
        http_info = self._get_group_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_group_id_http_info(cls, request):
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

    def list_groups(self, request):
        r"""列出用户组

        查询指定身份源下的IAM身份中心用户组列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroups
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupsResponse`
        """
        http_info = self._list_groups_http_info(request)
        return self._call_api(**http_info)

    def list_groups_invoker(self, request):
        http_info = self._list_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_groups_http_info(cls, request):
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

    def update_group(self, request):
        r"""更新用户组

        根据用户组ID，更新对应IAM身份中心用户组的属性。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGroup
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateGroupResponse`
        """
        http_info = self._update_group_http_info(request)
        return self._call_api(**http_info)

    def update_group_invoker(self, request):
        http_info = self._update_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_group_http_info(cls, request):
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

    def create_group_membership(self, request):
        r"""绑定用户和组

        将用户添加到用户组中，用户和用户组必须在同一身份源下。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGroupMembership
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupMembershipRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateGroupMembershipResponse`
        """
        http_info = self._create_group_membership_http_info(request)
        return self._call_api(**http_info)

    def create_group_membership_invoker(self, request):
        http_info = self._create_group_membership_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_group_membership_http_info(cls, request):
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

    def delete_group_membership(self, request):
        r"""解绑用户和组

        根据关联关系ID解绑用户和用户组，也就是将用户移出用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGroupMembership
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupMembershipRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteGroupMembershipResponse`
        """
        http_info = self._delete_group_membership_http_info(request)
        return self._call_api(**http_info)

    def delete_group_membership_invoker(self, request):
        http_info = self._delete_group_membership_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_group_membership_http_info(cls, request):
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

    def describe_group_membership(self, request):
        r"""查询绑定关系详情

        根据关联关系ID，查询此关联关系的详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeGroupMembership
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupMembershipRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeGroupMembershipResponse`
        """
        http_info = self._describe_group_membership_http_info(request)
        return self._call_api(**http_info)

    def describe_group_membership_invoker(self, request):
        http_info = self._describe_group_membership_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_group_membership_http_info(cls, request):
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

    def get_group_membership_id(self, request):
        r"""查询绑定关系ID

        根据用户ID和用户组ID，查询对应的关联关系ID。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetGroupMembershipId
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupMembershipIdRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetGroupMembershipIdResponse`
        """
        http_info = self._get_group_membership_id_http_info(request)
        return self._call_api(**http_info)

    def get_group_membership_id_invoker(self, request):
        http_info = self._get_group_membership_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_group_membership_id_http_info(cls, request):
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

    def is_member_in_groups(self, request):
        r"""查询用户是否是用户组成员

        根据用户ID和用户组ID列表，查询用户是否为用户组的成员。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for IsMemberInGroups
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.IsMemberInGroupsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.IsMemberInGroupsResponse`
        """
        http_info = self._is_member_in_groups_http_info(request)
        return self._call_api(**http_info)

    def is_member_in_groups_invoker(self, request):
        http_info = self._is_member_in_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _is_member_in_groups_http_info(cls, request):
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

    def list_group_memberships(self, request):
        r"""列出组中的用户

        根据用户组ID，列出用户组中的用户。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroupMemberships
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsResponse`
        """
        http_info = self._list_group_memberships_http_info(request)
        return self._call_api(**http_info)

    def list_group_memberships_invoker(self, request):
        http_info = self._list_group_memberships_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_group_memberships_http_info(cls, request):
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

    def list_group_memberships_for_member(self, request):
        r"""列出用户加入的组

        根据用户ID，列出用户加入的用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroupMembershipsForMember
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsForMemberRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListGroupMembershipsForMemberResponse`
        """
        http_info = self._list_group_memberships_for_member_http_info(request)
        return self._call_api(**http_info)

    def list_group_memberships_for_member_invoker(self, request):
        http_info = self._list_group_memberships_for_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_group_memberships_for_member_http_info(cls, request):
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

    def create_external_id_p_configuration_for_directory(self, request):
        r"""创建外部身份提供商配置

        创建外部身份提供商配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExternalIdPConfigurationForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateExternalIdPConfigurationForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateExternalIdPConfigurationForDirectoryResponse`
        """
        http_info = self._create_external_id_p_configuration_for_directory_http_info(request)
        return self._call_api(**http_info)

    def create_external_id_p_configuration_for_directory_invoker(self, request):
        http_info = self._create_external_id_p_configuration_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_external_id_p_configuration_for_directory_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExternalIdPConfigurationForDirectoryResponse"
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

    def delete_external_id_p_certificate(self, request):
        r"""删除外部身份提供商证书

        删除外部身份提供商证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExternalIdPCertificate
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteExternalIdPCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteExternalIdPCertificateResponse`
        """
        http_info = self._delete_external_id_p_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_external_id_p_certificate_invoker(self, request):
        http_info = self._delete_external_id_p_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_external_id_p_certificate_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}/certificate/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExternalIdPCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def delete_external_id_p_configuration_for_directory(self, request):
        r"""删除外部身份提供商配置

        删除外部身份提供商配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExternalIdPConfigurationForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteExternalIdPConfigurationForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteExternalIdPConfigurationForDirectoryResponse`
        """
        http_info = self._delete_external_id_p_configuration_for_directory_http_info(request)
        return self._call_api(**http_info)

    def delete_external_id_p_configuration_for_directory_invoker(self, request):
        http_info = self._delete_external_id_p_configuration_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_external_id_p_configuration_for_directory_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExternalIdPConfigurationForDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def disable_external_id_p_configuration_for_directory(self, request):
        r"""停用外部身份提供商

        停用外部身份提供商。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableExternalIdPConfigurationForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DisableExternalIdPConfigurationForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DisableExternalIdPConfigurationForDirectoryResponse`
        """
        http_info = self._disable_external_id_p_configuration_for_directory_http_info(request)
        return self._call_api(**http_info)

    def disable_external_id_p_configuration_for_directory_invoker(self, request):
        http_info = self._disable_external_id_p_configuration_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_external_id_p_configuration_for_directory_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableExternalIdPConfigurationForDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def enable_external_id_p_configuration_for_directory(self, request):
        r"""启用外部身份提供商

        启用外部身份提供商。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableExternalIdPConfigurationForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.EnableExternalIdPConfigurationForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.EnableExternalIdPConfigurationForDirectoryResponse`
        """
        http_info = self._enable_external_id_p_configuration_for_directory_http_info(request)
        return self._call_api(**http_info)

    def enable_external_id_p_configuration_for_directory_invoker(self, request):
        http_info = self._enable_external_id_p_configuration_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_external_id_p_configuration_for_directory_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableExternalIdPConfigurationForDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def import_external_id_p_certificate(self, request):
        r"""导入外部身份提供商证书

        导入外部身份提供商证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportExternalIdPCertificate
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ImportExternalIdPCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ImportExternalIdPCertificateResponse`
        """
        http_info = self._import_external_id_p_certificate_http_info(request)
        return self._call_api(**http_info)

    def import_external_id_p_certificate_invoker(self, request):
        http_info = self._import_external_id_p_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_external_id_p_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "ImportExternalIdPCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def list_external_id_p_certificates(self, request):
        r"""列出外部身份提供商证书

        查询外部身份提供商证书列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExternalIdPCertificates
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListExternalIdPCertificatesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListExternalIdPCertificatesResponse`
        """
        http_info = self._list_external_id_p_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_external_id_p_certificates_invoker(self, request):
        http_info = self._list_external_id_p_certificates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_external_id_p_certificates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}/certificate",
            "request_type": request.__class__.__name__,
            "response_type": "ListExternalIdPCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def list_external_id_p_configurations_for_directory(self, request):
        r"""查询外部身份提供商配置

        查询外部身份提供商配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExternalIdPConfigurationsForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListExternalIdPConfigurationsForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListExternalIdPConfigurationsForDirectoryResponse`
        """
        http_info = self._list_external_id_p_configurations_for_directory_http_info(request)
        return self._call_api(**http_info)

    def list_external_id_p_configurations_for_directory_invoker(self, request):
        http_info = self._list_external_id_p_configurations_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_external_id_p_configurations_for_directory_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp",
            "request_type": request.__class__.__name__,
            "response_type": "ListExternalIdPConfigurationsForDirectoryResponse"
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

    def update_external_id_p_configuration_for_directory(self, request):
        r"""更新外部身份提供商配置

        更新外部身份提供商配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateExternalIdPConfigurationForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateExternalIdPConfigurationForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateExternalIdPConfigurationForDirectoryResponse`
        """
        http_info = self._update_external_id_p_configuration_for_directory_http_info(request)
        return self._call_api(**http_info)

    def update_external_id_p_configuration_for_directory_invoker(self, request):
        http_info = self._update_external_id_p_configuration_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_external_id_p_configuration_for_directory_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/identity-stores/{identity_store_id}/external-idp/{idp_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateExternalIdPConfigurationForDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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

    def describe_password_policy(self, request):
        r"""查询自定义密码策略

        查询自定义密码策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribePasswordPolicy
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribePasswordPolicyRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribePasswordPolicyResponse`
        """
        http_info = self._describe_password_policy_http_info(request)
        return self._call_api(**http_info)

    def describe_password_policy_invoker(self, request):
        http_info = self._describe_password_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_password_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/password-policy",
            "request_type": request.__class__.__name__,
            "response_type": "DescribePasswordPolicyResponse"
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

    def update_password_policy(self, request):
        r"""更新自定义密码策略

        更新自定义密码策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePasswordPolicy
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdatePasswordPolicyRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdatePasswordPolicyResponse`
        """
        http_info = self._update_password_policy_http_info(request)
        return self._call_api(**http_info)

    def update_password_policy_invoker(self, request):
        http_info = self._update_password_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_password_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/identity-stores/{identity_store_id}/password-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePasswordPolicyResponse"
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

    def create_sp_certificate(self, request):
        r"""创建服务提供商证书

        创建服务提供商SAML协议签名证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSpCertificate
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateSpCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateSpCertificateResponse`
        """
        http_info = self._create_sp_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_sp_certificate_invoker(self, request):
        http_info = self._create_sp_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sp_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/saml-certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSpCertificateResponse"
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

    def delete_sp_certificate(self, request):
        r"""删除服务提供商证书

        删除服务提供商SAML协议签名证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSpCertificate
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteSpCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteSpCertificateResponse`
        """
        http_info = self._delete_sp_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_sp_certificate_invoker(self, request):
        http_info = self._delete_sp_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sp_certificate_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/saml-certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSpCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def get_sp_configuration_for_directory(self, request):
        r"""查询服务提供商配置

        查询服务提供商配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetSpConfigurationForDirectory
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetSpConfigurationForDirectoryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetSpConfigurationForDirectoryResponse`
        """
        http_info = self._get_sp_configuration_for_directory_http_info(request)
        return self._call_api(**http_info)

    def get_sp_configuration_for_directory_invoker(self, request):
        http_info = self._get_sp_configuration_for_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_sp_configuration_for_directory_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/sp-config",
            "request_type": request.__class__.__name__,
            "response_type": "GetSpConfigurationForDirectoryResponse"
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

    def list_sp_certificates(self, request):
        r"""列出服务提供商证书

        查询服务提供商SAML协议签名证书
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpCertificates
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListSpCertificatesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListSpCertificatesResponse`
        """
        http_info = self._list_sp_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_sp_certificates_invoker(self, request):
        http_info = self._list_sp_certificates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sp_certificates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/saml-certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpCertificatesResponse"
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

    def update_sp_active_certificate(self, request):
        r"""激活服务提供商证书

        激活服务提供商SAML协议签名证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSpActiveCertificate
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateSpActiveCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateSpActiveCertificateResponse`
        """
        http_info = self._update_sp_active_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_sp_active_certificate_invoker(self, request):
        http_info = self._update_sp_active_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sp_active_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/saml-certificates/{certificate_id}/active",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSpActiveCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'certificate_id' in local_var_params:
            path_params['certificate_id'] = local_var_params['certificate_id']

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

    def get_identity_store_summary(self, request):
        r"""查询身份源配额信息

        查询身份源配额信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetIdentityStoreSummary
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetIdentityStoreSummaryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetIdentityStoreSummaryResponse`
        """
        http_info = self._get_identity_store_summary_http_info(request)
        return self._call_api(**http_info)

    def get_identity_store_summary_invoker(self, request):
        http_info = self._get_identity_store_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_identity_store_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/identity-store-summary",
            "request_type": request.__class__.__name__,
            "response_type": "GetIdentityStoreSummaryResponse"
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

    def create_bearer_token(self, request):
        r"""创建访问令牌

        创建访问令牌。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBearerToken
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateBearerTokenRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateBearerTokenResponse`
        """
        http_info = self._create_bearer_token_http_info(request)
        return self._call_api(**http_info)

    def create_bearer_token_invoker(self, request):
        http_info = self._create_bearer_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_bearer_token_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/tenant/{tenant_id}/bearer-token",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBearerTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

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

    def create_provisioning_tenant(self, request):
        r"""启用自动预置

        启用自动预置，开启SCIM协议自动同步功能。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProvisioningTenant
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateProvisioningTenantRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateProvisioningTenantResponse`
        """
        http_info = self._create_provisioning_tenant_http_info(request)
        return self._call_api(**http_info)

    def create_provisioning_tenant_invoker(self, request):
        http_info = self._create_provisioning_tenant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_provisioning_tenant_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/provision-tenant",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProvisioningTenantResponse"
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

    def delete_bearer_token(self, request):
        r"""删除访问令牌

        删除访问令牌。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBearerToken
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteBearerTokenRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteBearerTokenResponse`
        """
        http_info = self._delete_bearer_token_http_info(request)
        return self._call_api(**http_info)

    def delete_bearer_token_invoker(self, request):
        http_info = self._delete_bearer_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bearer_token_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/tenant/{tenant_id}/bearer-token/{token_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBearerTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'token_id' in local_var_params:
            path_params['token_id'] = local_var_params['token_id']

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

    def delete_provisioning_tenant(self, request):
        r"""删除自动预置

        删除自动预置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProvisioningTenant
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteProvisioningTenantRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteProvisioningTenantResponse`
        """
        http_info = self._delete_provisioning_tenant_http_info(request)
        return self._call_api(**http_info)

    def delete_provisioning_tenant_invoker(self, request):
        http_info = self._delete_provisioning_tenant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_provisioning_tenant_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/tenant/{tenant_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProvisioningTenantResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

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

    def list_bearer_tokens(self, request):
        r"""列出访问令牌

        查询访问令牌列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBearerTokens
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListBearerTokensRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListBearerTokensResponse`
        """
        http_info = self._list_bearer_tokens_http_info(request)
        return self._call_api(**http_info)

    def list_bearer_tokens_invoker(self, request):
        http_info = self._list_bearer_tokens_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bearer_tokens_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/tenant/{tenant_id}/bearer-token",
            "request_type": request.__class__.__name__,
            "response_type": "ListBearerTokensResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

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

    def list_provisioning_tenants(self, request):
        r"""查询自动预置信息

        查询是否开启自动预置，返回具体SCIM自动预配配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProvisioningTenants
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListProvisioningTenantsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListProvisioningTenantsResponse`
        """
        http_info = self._list_provisioning_tenants_http_info(request)
        return self._call_api(**http_info)

    def list_provisioning_tenants_invoker(self, request):
        http_info = self._list_provisioning_tenants_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_provisioning_tenants_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/provision-tenant",
            "request_type": request.__class__.__name__,
            "response_type": "ListProvisioningTenantsResponse"
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

    def batch_delete_sessions(self, request):
        r"""批量删除用户登录会话

        批量删除用户登录会话。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteSessions
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.BatchDeleteSessionsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.BatchDeleteSessionsResponse`
        """
        http_info = self._batch_delete_sessions_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_sessions_invoker(self, request):
        http_info = self._batch_delete_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_sessions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/sessions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteSessionsResponse"
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

    def batch_list_mfa_devices_for_user(self, request):
        r"""列出用户MFA设备

        查询指定用户的MFA设备列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchListMfaDevicesForUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.BatchListMfaDevicesForUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.BatchListMfaDevicesForUserResponse`
        """
        http_info = self._batch_list_mfa_devices_for_user_http_info(request)
        return self._call_api(**http_info)

    def batch_list_mfa_devices_for_user_invoker(self, request):
        http_info = self._batch_list_mfa_devices_for_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_list_mfa_devices_for_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/retrieve-mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListMfaDevicesForUserResponse"
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

    def create_user(self, request):
        r"""创建用户

        在指定的身份源中创建一个IAM身份中心用户。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_user_http_info(cls, request):
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

    def delete_mfa_device_for_user(self, request):
        r"""删除用户MFA设备

        删除用户绑定的MFA设备。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMfaDeviceForUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteMfaDeviceForUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteMfaDeviceForUserResponse`
        """
        http_info = self._delete_mfa_device_for_user_http_info(request)
        return self._call_api(**http_info)

    def delete_mfa_device_for_user_invoker(self, request):
        http_info = self._delete_mfa_device_for_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_mfa_device_for_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/mfa-devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMfaDeviceForUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def delete_user(self, request):
        r"""删除用户

        根据用户ID，删除对应的IAM身份中心用户。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DeleteUserResponse`
        """
        http_info = self._delete_user_http_info(request)
        return self._call_api(**http_info)

    def delete_user_invoker(self, request):
        http_info = self._delete_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_http_info(cls, request):
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

    def describe_user(self, request):
        r"""查询用户详情

        根据用户ID，查询对应IAM身份中心用户的详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeUserResponse`
        """
        http_info = self._describe_user_http_info(request)
        return self._call_api(**http_info)

    def describe_user_invoker(self, request):
        http_info = self._describe_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_user_http_info(cls, request):
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

    def describe_users(self, request):
        r"""批量查询指定用户详情

        批量查询指定用户详情。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeUsers
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeUsersRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DescribeUsersResponse`
        """
        http_info = self._describe_users_http_info(request)
        return self._call_api(**http_info)

    def describe_users_invoker(self, request):
        http_info = self._describe_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/batch-query",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeUsersResponse"
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

    def disable_user(self, request):
        r"""禁用用户

        禁用IAM身份中心的用户。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.DisableUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.DisableUserResponse`
        """
        http_info = self._disable_user_http_info(request)
        return self._call_api(**http_info)

    def disable_user_invoker(self, request):
        http_info = self._disable_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableUserResponse"
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

    def enable_user(self, request):
        r"""启用用户

        启用IAM身份中心的用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.EnableUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.EnableUserResponse`
        """
        http_info = self._enable_user_http_info(request)
        return self._call_api(**http_info)

    def enable_user_invoker(self, request):
        http_info = self._enable_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableUserResponse"
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

    def get_user_id(self, request):
        r"""查询用户ID

        根据用户名或外部身份源ID，以精确匹配的方式查询用户ID。用户名和外部身份源ID两种查询方式二选一，不支持同时传入。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetUserId
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.GetUserIdRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.GetUserIdResponse`
        """
        http_info = self._get_user_id_http_info(request)
        return self._call_api(**http_info)

    def get_user_id_invoker(self, request):
        http_info = self._get_user_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_user_id_http_info(cls, request):
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

    def list_sessions(self, request):
        r"""列出用户登录会话

        查询指定用户的登录会话信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSessions
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListSessionsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListSessionsResponse`
        """
        http_info = self._list_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_sessions_invoker(self, request):
        http_info = self._list_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sessions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSessionsResponse"
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

    def list_users(self, request):
        r"""列出用户

        查询指定身份源下的IAM身份中心用户列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_users_http_info(cls, request):
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

    def register_mfa_device_for_user(self, request):
        r"""注册MFA设备

        为用户发起注册MFA设备，返回一个MFA注册地址。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterMfaDeviceForUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.RegisterMfaDeviceForUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.RegisterMfaDeviceForUserResponse`
        """
        http_info = self._register_mfa_device_for_user_http_info(request)
        return self._call_api(**http_info)

    def register_mfa_device_for_user_invoker(self, request):
        http_info = self._register_mfa_device_for_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_mfa_device_for_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/mfa-devices/register-mfa-device",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterMfaDeviceForUserResponse"
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

    def reset_pwd_mode(self, request):
        r"""通过电子邮件发送密码重置链接或生成用户的一次性密码

        通过电子邮件发送密码重置链接或生成用户的一次性密码。。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPwdMode
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.ResetPwdModeRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ResetPwdModeResponse`
        """
        http_info = self._reset_pwd_mode_http_info(request)
        return self._call_api(**http_info)

    def reset_pwd_mode_invoker(self, request):
        http_info = self._reset_pwd_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_pwd_mode_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/reset-password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPwdModeResponse"
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

    def update_mfa_device_for_user(self, request):
        r"""更新MFA设备显示名称

        更新MFA设备显示名称。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMfaDeviceForUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateMfaDeviceForUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateMfaDeviceForUserResponse`
        """
        http_info = self._update_mfa_device_for_user_http_info(request)
        return self._call_api(**http_info)

    def update_mfa_device_for_user_invoker(self, request):
        http_info = self._update_mfa_device_for_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_mfa_device_for_user_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/mfa-devices/{device_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMfaDeviceForUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'identity_store_id' in local_var_params:
            path_params['identity_store_id'] = local_var_params['identity_store_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'device_id' in local_var_params:
            path_params['device_id'] = local_var_params['device_id']

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

    def update_user(self, request):
        r"""更新用户

        根据用户ID，更新对应IAM身份中心用户的属性。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_http_info(cls, request):
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

    def verify_email(self, request):
        r"""验证用户邮箱

        验证用户邮箱。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for VerifyEmail
        :type request: :class:`huaweicloudsdkidentitycenterstore.v1.VerifyEmailRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.VerifyEmailResponse`
        """
        http_info = self._verify_email_http_info(request)
        return self._call_api(**http_info)

    def verify_email_invoker(self, request):
        http_info = self._verify_email_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _verify_email_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/identity-stores/{identity_store_id}/users/{user_id}/verify-email",
            "request_type": request.__class__.__name__,
            "response_type": "VerifyEmailResponse"
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

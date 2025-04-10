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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidentitycenterscim'")


class IdentityCenterSCIMClient(Client):
    def __init__(self):
        super(IdentityCenterSCIMClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidentitycenterscim.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "IdentityCenterSCIMCredentials")
        else:
            if clazz.__name__ != "IdentityCenterSCIMClient":
                raise TypeError("client type error, support client type is IdentityCenterSCIMClient")
            client_builder = ClientBuilder(clazz, "IdentityCenterSCIMCredentials")

        

        return client_builder

    def create_group(self, request):
        r"""创建用户组

        使用SCIM协议，同步用户组到IAM身份中心。
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - displayName、schemas为必填项
        - 在单个请求中最多可以添加100个成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.CreateGroupResponse`
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
            "resource_path": "/{tenant_id}/scim/v2/Groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def delete_group(self, request):
        r"""删除用户组

        删除现有用户组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.DeleteGroupResponse`
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
            "resource_path": "/{tenant_id}/scim/v2/Groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def get_group(self, request):
        r"""查询用户组详情

        查询现有用户组的详情信息。
        暂不支持
        IAM身份中心暂不支持此API操作的以下方面。
        - 查询用户组详情接口和列出用户组接口返回空成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetGroup
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.GetGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.GetGroupResponse`
        """
        http_info = self._get_group_http_info(request)
        return self._call_api(**http_info)

    def get_group_invoker(self, request):
        http_info = self._get_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{tenant_id}/scim/v2/Groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def list_groups(self, request):
        r"""列出用户组

        对现有用户组列表执行筛选查询，最多只能返回50个结果。
        暂不支持
        IAM身份中心暂不支持此API操作的以下方面。
        - 查询用户组详情接口和列出用户组接口返回空成员列表
        
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - 目前，列出用户组接口最多只能返回50个结果
        - 支持的筛选器组合：(displayName)、(id)。请注意，使用id作为单个过滤器虽然有效，但应避免使用，因为已经有一个查询用户组详情接口可用
        - 过滤器中支持的比较运算符：eq
        - 必须按如下方式指定筛选器：&lt;filterAttribute&gt; eq \&quot;&lt;filterValue&gt;\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroups
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.ListGroupsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.ListGroupsResponse`
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
            "resource_path": "/{tenant_id}/scim/v2/Groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def patch_group(self, request):
        r"""部分更新用户组

        修改现有用户组的部分属性，和管理用户组中的用户。
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - 请求中只允许使用displayName、 members和externalId属性
        - 单个请求中最多允许100个成员更改
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PatchGroup
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.PatchGroupRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.PatchGroupResponse`
        """
        http_info = self._patch_group_http_info(request)
        return self._call_api(**http_info)

    def patch_group_invoker(self, request):
        http_info = self._patch_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _patch_group_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/{tenant_id}/scim/v2/Groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "PatchGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def service_provider_config(self, request):
        r"""查询服务提供商配置

        查询IAM身份中心的SCIM相关配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ServiceProviderConfig
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.ServiceProviderConfigRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.ServiceProviderConfigResponse`
        """
        http_info = self._service_provider_config_http_info(request)
        return self._call_api(**http_info)

    def service_provider_config_invoker(self, request):
        http_info = self._service_provider_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _service_provider_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{tenant_id}/scim/v2/ServiceProviderConfig",
            "request_type": request.__class__.__name__,
            "response_type": "ServiceProviderConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def create_user(self, request):
        r"""创建用户

        使用SCIM协议，同步用户到IAM身份中心。
        暂不支持
        IAM身份中心暂不支持此API操作的以下方面。
        - ims、photos、x509Certificates、entitlements和password属性
        - manager的displayName子属性
        - emails、addresses和phoneNumbers的display子属性
        
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - 必须填写userName、displayName、schemas属性，name属性中的familyName、givenName子属性，emails属性中的value、primary、type子属性
        - addresses可以包含字母、重音字符、符号、数字、标点符号、空格（正常和不换行）
        - 我们不支持多值属性中的多个值（例如emails,addresses,phoneNumbers）。只允许单个值
        - emails属性值必须标记为primary
        - 不能指定groups字段
        - userName字段可以包含字母、数字和部分符号_+&#x3D;,.@-
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.CreateUserResponse`
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
            "resource_path": "/{tenant_id}/scim/v2/Users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def delete_user(self, request):
        r"""删除用户

        删除现有用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.DeleteUserResponse`
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
            "resource_path": "/{tenant_id}/scim/v2/Users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def get_user(self, request):
        r"""查询用户详情

        查询现有用户的详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetUser
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.GetUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.GetUserResponse`
        """
        http_info = self._get_user_http_info(request)
        return self._call_api(**http_info)

    def get_user_invoker(self, request):
        http_info = self._get_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{tenant_id}/scim/v2/Users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def list_users(self, request):
        r"""列出用户

        对现有用户列表执行筛选查询，最多只能返回50个结果。
        暂不支持
        IAM身份中心不支持此API操作的以下方面。
        - startIndex,attributes,excludedAttributes（虽在SCIM协议中列出）
        
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - 目前，列出用户接口最多只能返回50个结果
        - 支持的筛选器组合：(userName)、(id)。请注意，使用id作为单个过滤器虽然有效，但应避免使用，因为已经有一个查询用户详情接口可用
        - 过滤器中支持的比较运算符：eq
        - 必须按如下方式指定筛选器：&lt;filterAttribute&gt; eq \&quot;&lt;filterValue&gt;\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.ListUsersResponse`
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
            "resource_path": "/{tenant_id}/scim/v2/Users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def patch_user(self, request):
        r"""部分更新用户

        修改现有用户的部分属性。
        暂不支持
        IAM身份中心暂不支持此API操作的以下方面。
        - 对userName或active属性执行多个PATCH操作
        - ims、photos、x509Certificates、entitlements和password属性
        - manager的displayName子属性
        - emails、addresses和phoneNumbers的display子属性
        
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - 支持的操作是add、replace和remove
        - 必须指定操作
        - remove操作需要指定属性路径
        - add和replace操作需要指定属性的值
        - 仅允许修改userName、active、externalId、displayName、nickName、profileUrl、title、userType、preferredLanguage、locale、timezone、name、enterprise、emails、addresses和phoneNumbers属性
        - 过滤器中仅支持eq运算符
        - userName或active属性不支持remove操作
        - 我们不支持多值属性中的多个值（例如emails,addresses,phoneNumbers）。这些属性中的每一个都只允许有一个值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PatchUser
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.PatchUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.PatchUserResponse`
        """
        http_info = self._patch_user_http_info(request)
        return self._call_api(**http_info)

    def patch_user_invoker(self, request):
        http_info = self._patch_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _patch_user_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/{tenant_id}/scim/v2/Users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "PatchUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

    def put_user(self, request):
        r"""更新用户

        更新现有用户。
        暂不支持
        IAM身份中心暂不支持此API操作的以下方面。
        - ims、photos、x509Certificates、entitlements和password属性
        - manager的displayName子属性
        - emails、addresses和phoneNumbers的display子属性
        
        约束条件
        IAM身份中心对此API操作具有以下约束。
        - 必须填写userName、displayName、schemas属性，name属性中的familyName、givenName子属性，emails属性中的value、primary、type子属性
        - addresses可以包含字母、重音字符、符号、数字、标点符号、空格（正常和不换行）
        - 我们不支持多值属性中的多个值（例如emails,addresses,phoneNumbers）
        - emails属性值必须标记为primary
        - 不能指定groups属性
        - userName字段可以包含字母、数字和部分符号_+&#x3D;,.@-
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutUser
        :type request: :class:`huaweicloudsdkidentitycenterscim.v1.PutUserRequest`
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.PutUserResponse`
        """
        http_info = self._put_user_http_info(request)
        return self._call_api(**http_info)

    def put_user_invoker(self, request):
        http_info = self._put_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_user_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/{tenant_id}/scim/v2/Users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "PutUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

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

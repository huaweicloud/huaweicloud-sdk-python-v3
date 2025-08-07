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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkorganizations'")


class OrganizationsClient(Client):
    def __init__(self):
        super(OrganizationsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkorganizations.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "OrganizationsClient":
                raise TypeError("client type error, support client type is OrganizationsClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def close_account(self, request):
        r"""关闭账号

        关闭账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CloseAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.CloseAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CloseAccountResponse`
        """
        http_info = self._close_account_http_info(request)
        return self._call_api(**http_info)

    def close_account_invoker(self, request):
        http_info = self._close_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _close_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/accounts/{account_id}/close",
            "request_type": request.__class__.__name__,
            "response_type": "CloseAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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

    def create_account(self, request):
        r"""创建账号

        创建一个账号，生成的账号将自动成为调用此接口的账号所属组织的成员。此操作只能由组织的管理账号调用。组织云服务将在新账号中创建所需的服务关联委托和账号访问委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateAccountResponse`
        """
        http_info = self._create_account_http_info(request)
        return self._call_api(**http_info)

    def create_account_invoker(self, request):
        http_info = self._create_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def create_resource_account(self, request):
        r"""创建帐号

        创建一个帐号，不携带手机号邮箱联系方式，生成的帐号将自动成为调用此接口的帐号所属组织的成员。此操作只能由组织的管理帐号调用。组织云服务将在新帐号中创建所需的服务关联委托和帐号访问委托。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResourceAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateResourceAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateResourceAccountResponse`
        """
        http_info = self._create_resource_account_http_info(request)
        return self._call_api(**http_info)

    def create_resource_account_invoker(self, request):
        http_info = self._create_resource_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resource_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/organizations/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def invite_account(self, request):
        r"""邀请账号加入组织

        向另一个账号发送邀请，受邀账号将以成员账号加入您的组织。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.InviteAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.InviteAccountResponse`
        """
        http_info = self._invite_account_http_info(request)
        return self._call_api(**http_info)

    def invite_account_invoker(self, request):
        http_info = self._invite_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invite_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/accounts/invite",
            "request_type": request.__class__.__name__,
            "response_type": "InviteAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_accounts(self, request):
        r"""列出组织中的账号

        列出组织中的账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。如果指定父级组织单元，则将获得作为父级直系子级的所有账号的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccounts
        :type request: :class:`huaweicloudsdkorganizations.v1.ListAccountsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListAccountsResponse`
        """
        http_info = self._list_accounts_http_info(request)
        return self._call_api(**http_info)

    def list_accounts_invoker(self, request):
        http_info = self._list_accounts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_accounts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'with_register_contact_info' in local_var_params:
            query_params.append(('with_register_contact_info', local_var_params['with_register_contact_info']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_close_account_statuses(self, request):
        r"""列出关闭账号的状态

        列出组织中指定状态的账号关闭请求。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloseAccountStatuses
        :type request: :class:`huaweicloudsdkorganizations.v1.ListCloseAccountStatusesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListCloseAccountStatusesResponse`
        """
        http_info = self._list_close_account_statuses_http_info(request)
        return self._call_api(**http_info)

    def list_close_account_statuses_invoker(self, request):
        http_info = self._list_close_account_statuses_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_close_account_statuses_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/close-account-status",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloseAccountStatusesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'states' in local_var_params:
            query_params.append(('states', local_var_params['states']))
            collection_formats['states'] = 'multi'

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

    def list_create_account_statuses(self, request):
        r"""列出创建账号的状态

        列出组织中指定状态的账号创建请求。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCreateAccountStatuses
        :type request: :class:`huaweicloudsdkorganizations.v1.ListCreateAccountStatusesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListCreateAccountStatusesResponse`
        """
        http_info = self._list_create_account_statuses_http_info(request)
        return self._call_api(**http_info)

    def list_create_account_statuses_invoker(self, request):
        http_info = self._list_create_account_statuses_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_create_account_statuses_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/create-account-status",
            "request_type": request.__class__.__name__,
            "response_type": "ListCreateAccountStatusesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'states' in local_var_params:
            query_params.append(('states', local_var_params['states']))
            collection_formats['states'] = 'multi'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def move_account(self, request):
        r"""移动账号

        将账号从其当前源位置（根或组织单元）移动到指定的目标位置（根或组织单元）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MoveAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.MoveAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.MoveAccountResponse`
        """
        http_info = self._move_account_http_info(request)
        return self._call_api(**http_info)

    def move_account_invoker(self, request):
        http_info = self._move_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _move_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/accounts/{account_id}/move",
            "request_type": request.__class__.__name__,
            "response_type": "MoveAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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

    def remove_account(self, request):
        r"""移除指定的账号

        从组织中移除指定的账号。移除的账号将成为一个独立账号，该账号不是任何组织的成员。此操作只能由组织的管理账号调用。只有当账号配置了作为独立账号运行所需的信息时，您才能从组织中移除账号。注意，要移除的账号不能是组织启用的任何服务的委托管理员账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.RemoveAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.RemoveAccountResponse`
        """
        http_info = self._remove_account_http_info(request)
        return self._call_api(**http_info)

    def remove_account_invoker(self, request):
        http_info = self._remove_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/accounts/{account_id}/remove",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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

    def show_account(self, request):
        r"""查询账号信息

        查询有关指定账号的信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowAccountResponse`
        """
        http_info = self._show_account_http_info(request)
        return self._call_api(**http_info)

    def show_account_invoker(self, request):
        http_info = self._show_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/accounts/{account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

        query_params = []
        if 'with_register_contact_info' in local_var_params:
            query_params.append(('with_register_contact_info', local_var_params['with_register_contact_info']))

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

    def show_create_account_status(self, request):
        r"""查询有关创建账号状态的信息

        检索创建账号的异步请求的当前状态。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCreateAccountStatus
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowCreateAccountStatusRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowCreateAccountStatusResponse`
        """
        http_info = self._show_create_account_status_http_info(request)
        return self._call_api(**http_info)

    def show_create_account_status_invoker(self, request):
        http_info = self._show_create_account_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_create_account_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/create-account-status/{create_account_status_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCreateAccountStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'create_account_status_id' in local_var_params:
            path_params['create_account_status_id'] = local_var_params['create_account_status_id']

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

    def update_account(self, request):
        r"""更新账号信息

        更新指定的账号信息。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.UpdateAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdateAccountResponse`
        """
        http_info = self._update_account_http_info(request)
        return self._call_api(**http_info)

    def update_account_invoker(self, request):
        http_info = self._update_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_account_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/organizations/accounts/{account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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

    def deregister_delegated_administrator(self, request):
        r"""注销服务的委托管理员

        删除指定成员账号作为指定服务的委托管理员。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeregisterDelegatedAdministrator
        :type request: :class:`huaweicloudsdkorganizations.v1.DeregisterDelegatedAdministratorRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeregisterDelegatedAdministratorResponse`
        """
        http_info = self._deregister_delegated_administrator_http_info(request)
        return self._call_api(**http_info)

    def deregister_delegated_administrator_invoker(self, request):
        http_info = self._deregister_delegated_administrator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _deregister_delegated_administrator_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/delegated-administrators/deregister",
            "request_type": request.__class__.__name__,
            "response_type": "DeregisterDelegatedAdministratorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_delegated_administrators(self, request):
        r"""列出此组织中指定为委托管理员的账号

        列出在此组织中指定为委派管理员的账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDelegatedAdministrators
        :type request: :class:`huaweicloudsdkorganizations.v1.ListDelegatedAdministratorsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListDelegatedAdministratorsResponse`
        """
        http_info = self._list_delegated_administrators_http_info(request)
        return self._call_api(**http_info)

    def list_delegated_administrators_invoker(self, request):
        http_info = self._list_delegated_administrators_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_delegated_administrators_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/delegated-administrators",
            "request_type": request.__class__.__name__,
            "response_type": "ListDelegatedAdministratorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_principal' in local_var_params:
            query_params.append(('service_principal', local_var_params['service_principal']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_delegated_services(self, request):
        r"""列出指定账号是其委托管理员的服务

        列出指定账号是其委托管理员的服务。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDelegatedServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListDelegatedServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListDelegatedServicesResponse`
        """
        http_info = self._list_delegated_services_http_info(request)
        return self._call_api(**http_info)

    def list_delegated_services_invoker(self, request):
        http_info = self._list_delegated_services_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_delegated_services_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/accounts/{account_id}/delegated-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListDelegatedServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def register_delegated_administrator(self, request):
        r"""注册作为服务委托管理员

        指定成员账号能够管理指定服务的组织功能。此接口授予委托管理员对组织服务数据的只读访问权限。委托管理员账号中的IAM用户仍需要IAM权限才能访问和管理服务。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDelegatedAdministrator
        :type request: :class:`huaweicloudsdkorganizations.v1.RegisterDelegatedAdministratorRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.RegisterDelegatedAdministratorResponse`
        """
        http_info = self._register_delegated_administrator_http_info(request)
        return self._call_api(**http_info)

    def register_delegated_administrator_invoker(self, request):
        http_info = self._register_delegated_administrator_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_delegated_administrator_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/delegated-administrators/register",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterDelegatedAdministratorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def accept_handshake(self, request):
        r"""接受邀请

        向邀请的发起方发送应答，接受加入组织邀请。在您接受邀请后，此邀请信息将继续保留并出现在相关API的返回结果中，保留期限为30天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AcceptHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.AcceptHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.AcceptHandshakeResponse`
        """
        http_info = self._accept_handshake_http_info(request)
        return self._call_api(**http_info)

    def accept_handshake_invoker(self, request):
        http_info = self._accept_handshake_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _accept_handshake_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/received-handshakes/{handshake_id}/accept",
            "request_type": request.__class__.__name__,
            "response_type": "AcceptHandshakeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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

    def cancel_handshake(self, request):
        r"""取消邀请

        取消邀请，此时邀请状态将设置为已取消。此接口只能由发起邀请的账号调用。取消邀请后，此邀请信息将继续保留并出现在相关API的返回结果中，保留期限为30天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.CancelHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CancelHandshakeResponse`
        """
        http_info = self._cancel_handshake_http_info(request)
        return self._call_api(**http_info)

    def cancel_handshake_invoker(self, request):
        http_info = self._cancel_handshake_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_handshake_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/handshakes/{handshake_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelHandshakeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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

    def decline_handshake(self, request):
        r"""拒绝邀请

        拒绝邀请请求。受邀账号拒绝邀请，此时当前邀请状态将设置为拒绝，邀请停止。此接口只能由受邀账号调用。邀请发起者无法再次激活被拒绝的邀请，但可以重新发送新的邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeclineHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.DeclineHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeclineHandshakeResponse`
        """
        http_info = self._decline_handshake_http_info(request)
        return self._call_api(**http_info)

    def decline_handshake_invoker(self, request):
        http_info = self._decline_handshake_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _decline_handshake_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/received-handshakes/{handshake_id}/decline",
            "request_type": request.__class__.__name__,
            "response_type": "DeclineHandshakeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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

    def list_handshakes(self, request):
        r"""列出发送的邀请

        列出所属组织发送的邀请。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHandshakes
        :type request: :class:`huaweicloudsdkorganizations.v1.ListHandshakesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListHandshakesResponse`
        """
        http_info = self._list_handshakes_http_info(request)
        return self._call_api(**http_info)

    def list_handshakes_invoker(self, request):
        http_info = self._list_handshakes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_handshakes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/handshakes",
            "request_type": request.__class__.__name__,
            "response_type": "ListHandshakesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_received_handshakes(self, request):
        r"""列出收到的邀请

        列出账号收到的所有邀请。此操作可以由任何账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReceivedHandshakes
        :type request: :class:`huaweicloudsdkorganizations.v1.ListReceivedHandshakesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListReceivedHandshakesResponse`
        """
        http_info = self._list_received_handshakes_http_info(request)
        return self._call_api(**http_info)

    def list_received_handshakes_invoker(self, request):
        http_info = self._list_received_handshakes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_received_handshakes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/received-handshakes",
            "request_type": request.__class__.__name__,
            "response_type": "ListReceivedHandshakesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_handshake(self, request):
        r"""查询邀请相关信息

        查询组织中已有账号邀请的相关信息。此接口可以由组织中的任何账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowHandshakeResponse`
        """
        http_info = self._show_handshake_http_info(request)
        return self._call_api(**http_info)

    def show_handshake_invoker(self, request):
        http_info = self._show_handshake_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_handshake_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/handshakes/{handshake_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHandshakeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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

    def list_entities(self, request):
        r"""列出组织中的根、组织单元和账号

        列出组织中包含的所有根、组织单元和账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。您可以通过指定父ID和子ID参数来过滤实体。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEntities
        :type request: :class:`huaweicloudsdkorganizations.v1.ListEntitiesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListEntitiesResponse`
        """
        http_info = self._list_entities_http_info(request)
        return self._call_api(**http_info)

    def list_entities_invoker(self, request):
        http_info = self._list_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_entities_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/entities",
            "request_type": request.__class__.__name__,
            "response_type": "ListEntitiesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'child_id' in local_var_params:
            query_params.append(('child_id', local_var_params['child_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_quotas(self, request):
        r"""列出租户的组织配额

        列出租户的组织配额。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkorganizations.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_services(self, request):
        r"""列出所有可以与组织服务集成的云服务

        列出所有可以与组织服务集成的云服务。集成后云服务将成为组织的可信服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListServicesResponse`
        """
        http_info = self._list_services_http_info(request)
        return self._call_api(**http_info)

    def list_services_invoker(self, request):
        http_info = self._list_services_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_services_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/services",
            "request_type": request.__class__.__name__,
            "response_type": "ListServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_tag_policy_services(self, request):
        r"""列出被添加到标签策略强制执行的资源类型

        列出被添加到标签策略强制执行的资源类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagPolicyServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTagPolicyServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTagPolicyServicesResponse`
        """
        http_info = self._list_tag_policy_services_http_info(request)
        return self._call_api(**http_info)

    def list_tag_policy_services_invoker(self, request):
        http_info = self._list_tag_policy_services_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tag_policy_services_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/tag-policy-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagPolicyServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_effective_policies(self, request):
        r"""查询有效的策略

        查询指定策略类型和账号的有效策略信息。当前此接口不支持查询服务控制策略（service_control_policy）。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEffectivePolicies
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowEffectivePoliciesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowEffectivePoliciesResponse`
        """
        http_info = self._show_effective_policies_http_info(request)
        return self._call_api(**http_info)

    def show_effective_policies_invoker(self, request):
        http_info = self._show_effective_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_effective_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/entities/effective-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEffectivePoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'entity_id' in local_var_params:
            query_params.append(('entity_id', local_var_params['entity_id']))
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))

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

    def create_organization(self, request):
        r"""创建组织

        创建组织。调用此接口的账号将自动成为新组织的管理账号，调用此接口的账号凭证必须是新组织管理账号的账号凭证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationResponse`
        """
        http_info = self._create_organization_http_info(request)
        return self._call_api(**http_info)

    def create_organization_invoker(self, request):
        http_info = self._create_organization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_organization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrganizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def delete_organization(self, request):
        r"""删除组织

        删除组织。您必须使用管理账号才能删除组织，并且先移除组织中的所有账号、组织单元和策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationResponse`
        """
        http_info = self._delete_organization_http_info(request)
        return self._call_api(**http_info)

    def delete_organization_invoker(self, request):
        http_info = self._delete_organization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_organization_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/organizations",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOrganizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def leave_organization(self, request):
        r"""离开当前组织

        此操作只能由组织的成员账号调用。只有当组织账号配置了作为独立账号运行所需的信息时，您才能作为成员账号离开组织。要离开的账号不能是组织启用的任何服务的委托管理员账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LeaveOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.LeaveOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.LeaveOrganizationResponse`
        """
        http_info = self._leave_organization_http_info(request)
        return self._call_api(**http_info)

    def leave_organization_invoker(self, request):
        http_info = self._leave_organization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _leave_organization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/leave",
            "request_type": request.__class__.__name__,
            "response_type": "LeaveOrganizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_roots(self, request):
        r"""列出组织的根

        列出当前组织的根。此接口只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRoots
        :type request: :class:`huaweicloudsdkorganizations.v1.ListRootsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListRootsResponse`
        """
        http_info = self._list_roots_http_info(request)
        return self._call_api(**http_info)

    def list_roots_invoker(self, request):
        http_info = self._list_roots_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_roots_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/roots",
            "request_type": request.__class__.__name__,
            "response_type": "ListRootsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_organization(self, request):
        r"""查询所属组织信息

        查询账号所属组织的信息。此操作可以由组织中的任何账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationResponse`
        """
        http_info = self._show_organization_http_info(request)
        return self._call_api(**http_info)

    def show_organization_invoker(self, request):
        http_info = self._show_organization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_organization_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def create_organizational_unit(self, request):
        r"""创建组织单元

        在根或父组织单元中创建组织单元。组织单元是账号的容器，使您能够对账号进行分组管理，并根据业务要求应用策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationalUnitResponse`
        """
        http_info = self._create_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def create_organizational_unit_invoker(self, request):
        http_info = self._create_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/organizational-units",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def delete_organizational_unit(self, request):
        r"""删除组织单元

        从根或其他组织单元中删除组织单元。前提是您必须先移除该组织单元中的所有成员账号或将成员账号移动至其他组织单元，必须删除该组织单元中的所有子组织单元。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationalUnitResponse`
        """
        http_info = self._delete_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def delete_organizational_unit_invoker(self, request):
        http_info = self._delete_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/organizations/organizational-units/{organizational_unit_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organizational_unit_id' in local_var_params:
            path_params['organizational_unit_id'] = local_var_params['organizational_unit_id']

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

    def list_organizational_units(self, request):
        r"""列出组织单元

        列出组织中的所有组织单元。如果指定父级组织单元，则将获得父级直系子级的组织单元列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrganizationalUnits
        :type request: :class:`huaweicloudsdkorganizations.v1.ListOrganizationalUnitsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListOrganizationalUnitsResponse`
        """
        http_info = self._list_organizational_units_http_info(request)
        return self._call_api(**http_info)

    def list_organizational_units_invoker(self, request):
        http_info = self._list_organizational_units_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_organizational_units_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/organizational-units",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrganizationalUnitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_organizational_unit(self, request):
        r"""查询有关组织单元的信息

        查询有关组织单元的信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationalUnitResponse`
        """
        http_info = self._show_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def show_organizational_unit_invoker(self, request):
        http_info = self._show_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/organizational-units/{organizational_unit_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organizational_unit_id' in local_var_params:
            path_params['organizational_unit_id'] = local_var_params['organizational_unit_id']

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

    def update_organizational_unit(self, request):
        r"""更改组织单元名称

        重命名指定的组织单元。重命名后组织单元ID不变，下属子组织单元和下属账号不变，组织单元绑定的策略不变。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitResponse`
        """
        http_info = self._update_organizational_unit_http_info(request)
        return self._call_api(**http_info)

    def update_organizational_unit_invoker(self, request):
        http_info = self._update_organizational_unit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_organizational_unit_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/organizations/organizational-units/{organizational_unit_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOrganizationalUnitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organizational_unit_id' in local_var_params:
            path_params['organizational_unit_id'] = local_var_params['organizational_unit_id']

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

    def attach_policy(self, request):
        r"""将策略跟实体绑定

        绑定策略到根、组织单元或个人账号。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.AttachPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.AttachPolicyResponse`
        """
        http_info = self._attach_policy_http_info(request)
        return self._call_api(**http_info)

    def attach_policy_invoker(self, request):
        http_info = self._attach_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/policies/{policy_id}/attach",
            "request_type": request.__class__.__name__,
            "response_type": "AttachPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def create_policy(self, request):
        r"""创建策略

        创建指定类型的策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreatePolicyResponse`
        """
        http_info = self._create_policy_http_info(request)
        return self._call_api(**http_info)

    def create_policy_invoker(self, request):
        http_info = self._create_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_policy(self, request):
        r"""删除策略

        从组织中删除指定的策略。在执行此操作之前，必须首先将策略跟所有组织单元、根和账号解绑。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeletePolicyResponse`
        """
        http_info = self._delete_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_policy_invoker(self, request):
        http_info = self._delete_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/organizations/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def detach_policy(self, request):
        r"""将策略跟实体解绑

        从根、组织单元或账号解绑策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.DetachPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DetachPolicyResponse`
        """
        http_info = self._detach_policy_http_info(request)
        return self._call_api(**http_info)

    def detach_policy_invoker(self, request):
        http_info = self._detach_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/policies/{policy_id}/detach",
            "request_type": request.__class__.__name__,
            "response_type": "DetachPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def disable_policy_type(self, request):
        r"""禁用根中的策略类型

        禁用根中的策略类型。只有在根中启用了特定类型的策略，才能将该类型的策略绑定到根中的实体。执行此操作后，您不能再将指定类型的策略绑定到该根或该根中的任何组织单元或账号。这是在后台执行的异步请求。您可以使用ListRoots查看指定根的策略类型的状态。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisablePolicyType
        :type request: :class:`huaweicloudsdkorganizations.v1.DisablePolicyTypeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DisablePolicyTypeResponse`
        """
        http_info = self._disable_policy_type_http_info(request)
        return self._call_api(**http_info)

    def disable_policy_type_invoker(self, request):
        http_info = self._disable_policy_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_policy_type_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/policies/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisablePolicyTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def enable_policy_type(self, request):
        r"""在根中启用策略类型

        在根中启用策略类型。在根中启用策略类型后，您可以将该类型的策略绑定到根、或该根中的任何组织单元和账号。这是在后台执行的异步请求。您可以使用ListRoots查看指定根的策略类型的状态。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnablePolicyType
        :type request: :class:`huaweicloudsdkorganizations.v1.EnablePolicyTypeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.EnablePolicyTypeResponse`
        """
        http_info = self._enable_policy_type_http_info(request)
        return self._call_api(**http_info)

    def enable_policy_type_invoker(self, request):
        http_info = self._enable_policy_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_policy_type_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/policies/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnablePolicyTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_entities_for_policy(self, request):
        r"""列出跟指定策略绑定的所有实体

        列出跟指定策略绑定的所有根、组织单元和账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEntitiesForPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.ListEntitiesForPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListEntitiesForPolicyResponse`
        """
        http_info = self._list_entities_for_policy_http_info(request)
        return self._call_api(**http_info)

    def list_entities_for_policy_invoker(self, request):
        http_info = self._list_entities_for_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_entities_for_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/policies/{policy_id}/attached-entities",
            "request_type": request.__class__.__name__,
            "response_type": "ListEntitiesForPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_policies(self, request):
        r"""列出策略

        列出组织中的所有策略。如果指定了资源ID，例如组织单元ID或账号ID，则将获得该资源已绑定的策略列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicies
        :type request: :class:`huaweicloudsdkorganizations.v1.ListPoliciesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListPoliciesResponse`
        """
        http_info = self._list_policies_http_info(request)
        return self._call_api(**http_info)

    def list_policies_invoker(self, request):
        http_info = self._list_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'attached_entity_id' in local_var_params:
            query_params.append(('attached_entity_id', local_var_params['attached_entity_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_policy(self, request):
        r"""查询策略相关信息

        检索策略的相关信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowPolicyResponse`
        """
        http_info = self._show_policy_http_info(request)
        return self._call_api(**http_info)

    def show_policy_invoker(self, request):
        http_info = self._show_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_policy(self, request):
        r"""更新策略

        更新策略，可以更新策略的名称、描述或内容。如果不提供任何参数，则策略将保持不变。您不能更改策略的类型。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdatePolicyResponse`
        """
        http_info = self._update_policy_http_info(request)
        return self._call_api(**http_info)

    def update_policy_invoker(self, request):
        http_info = self._update_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_policy_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/organizations/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_security_token' in local_var_params:
            header_params['X-Security-Token'] = local_var_params['x_security_token']
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_tag_resource(self, request):
        r"""为指定资源类型添加标签

        向指定的资源类型添加一个或多个标签。目前，您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateTagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateTagResourceResponse`
        """
        http_info = self._create_tag_resource_http_info(request)
        return self._call_api(**http_info)

    def create_tag_resource_invoker(self, request):
        http_info = self._create_tag_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tag_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def delete_tag_resource(self, request):
        r"""从指定资源类型中删除指定主键标签

        从指定资源类型中删除具有指定主键的任何标签。您可以将标签绑定到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.DeleteTagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeleteTagResourceResponse`
        """
        http_info = self._delete_tag_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_resource_invoker(self, request):
        http_info = self._delete_tag_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def list_resource_instances(self, request):
        r"""根据资源类型及标签信息查询实例列表

        根据资源类型及标签信息查询实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkorganizations.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListResourceInstancesResponse`
        """
        http_info = self._list_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instances_invoker(self, request):
        http_info = self._list_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_resource_tags(self, request):
        r"""查询资源标签

        查询资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkorganizations.v1.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListResourceTagsResponse`
        """
        http_info = self._list_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_tags_invoker(self, request):
        http_info = self._list_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_tag_resources(self, request):
        r"""列出绑定到指定资源类型的标签

        列出绑定到指定资源类型的标签。您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagResources
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTagResourcesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTagResourcesResponse`
        """
        http_info = self._list_tag_resources_http_info(request)
        return self._call_api(**http_info)

    def list_tag_resources_invoker(self, request):
        http_info = self._list_tag_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tag_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_tags_for_resource(self, request):
        r"""列出绑定到指定资源的标签

        列出绑定到指定资源的标签。您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagsForResource
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTagsForResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTagsForResourceResponse`
        """
        http_info = self._list_tags_for_resource_http_info(request)
        return self._call_api(**http_info)

    def list_tags_for_resource_invoker(self, request):
        http_info = self._list_tags_for_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tags_for_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/resources/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsForResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def show_resource_instances_count(self, request):
        r"""根据资源类型及标签信息查询实例数量

        根据资源类型及标签信息查询实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceInstancesCount
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowResourceInstancesCountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowResourceInstancesCountResponse`
        """
        http_info = self._show_resource_instances_count_http_info(request)
        return self._call_api(**http_info)

    def show_resource_instances_count_invoker(self, request):
        http_info = self._show_resource_instances_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_instances_count_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceInstancesCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def tag_resource(self, request):
        r"""为指定资源添加标签

        向指定的资源添加一个或多个标签。目前，您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.TagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.TagResourceResponse`
        """
        http_info = self._tag_resource_http_info(request)
        return self._call_api(**http_info)

    def tag_resource_invoker(self, request):
        http_info = self._tag_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _tag_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/resources/{resource_id}/tag",
            "request_type": request.__class__.__name__,
            "response_type": "TagResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def untag_resource(self, request):
        r"""从指定资源中删除指定主键标签

        从指定资源中删除具有指定主键的任何标签。您可以将标签绑定到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.UntagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UntagResourceResponse`
        """
        http_info = self._untag_resource_http_info(request)
        return self._call_api(**http_info)

    def untag_resource_invoker(self, request):
        http_info = self._untag_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _untag_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/resources/{resource_id}/untag",
            "request_type": request.__class__.__name__,
            "response_type": "UntagResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def disable_trusted_service(self, request):
        r"""禁用受信任服务

        禁用服务（由service_principal指定的服务）与组织的集成。禁用可信服务后，指定服务将不可以在组织中的新账号中创建服务关联委托。这意味着该服务无法代表您对组织中的任何新账号执行操作。在服务完成从组织中的清理之前，服务仍可以在旧账号中执行操作。此接口只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableTrustedService
        :type request: :class:`huaweicloudsdkorganizations.v1.DisableTrustedServiceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DisableTrustedServiceResponse`
        """
        http_info = self._disable_trusted_service_http_info(request)
        return self._call_api(**http_info)

    def disable_trusted_service_invoker(self, request):
        http_info = self._disable_trusted_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disable_trusted_service_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/trusted-services/disable",
            "request_type": request.__class__.__name__,
            "response_type": "DisableTrustedServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def enable_trusted_service(self, request):
        r"""启用可信服务

        启用服务（由service_principal指定的服务）与组织的集成。启用可信服务后，允许指定的可信服务对组织中的所有账号创建服务关联委托。这允许可信服务代表您在组织及其账号中执行操作。此接口只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableTrustedService
        :type request: :class:`huaweicloudsdkorganizations.v1.EnableTrustedServiceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.EnableTrustedServiceResponse`
        """
        http_info = self._enable_trusted_service_http_info(request)
        return self._call_api(**http_info)

    def enable_trusted_service_invoker(self, request):
        http_info = self._enable_trusted_service_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_trusted_service_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/organizations/trusted-services/enable",
            "request_type": request.__class__.__name__,
            "response_type": "EnableTrustedServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_trusted_services(self, request):
        r"""列出组织的可信服务列表

        返回启用与组织集成的可信服务列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTrustedServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTrustedServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTrustedServicesResponse`
        """
        http_info = self._list_trusted_services_http_info(request)
        return self._call_api(**http_info)

    def list_trusted_services_invoker(self, request):
        http_info = self._list_trusted_services_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_trusted_services_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/organizations/trusted-services",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrustedServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

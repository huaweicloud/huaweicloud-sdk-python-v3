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


class OrganizationsClient(Client):
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
        super(OrganizationsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkorganizations.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "OrganizationsClient":
            raise TypeError("client type error, support client type is OrganizationsClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def invite_account(self, request):
        """邀请帐号加入组织

        向另一个帐号发送邀请，受邀帐号将以成员帐号加入您的组织。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InviteAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.InviteAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.InviteAccountResponse`
        """
        return self.invite_account_with_http_info(request)

    def invite_account_with_http_info(self, request):
        all_params = ['invite_account_req_body']
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
            resource_path='/v1/organizations/accounts/invite',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InviteAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_accounts(self, request):
        """列出组织中的帐号

        列出组织中的帐号。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。如果指定父级组织单元，则将获得作为父级直系子级的所有帐号的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccounts
        :type request: :class:`huaweicloudsdkorganizations.v1.ListAccountsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListAccountsResponse`
        """
        return self.list_accounts_with_http_info(request)

    def list_accounts_with_http_info(self, request):
        all_params = ['parent_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/accounts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccountsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_create_account_statuses(self, request):
        """列出创建帐号的状态

        列出组织中指定状态的帐号创建请求。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCreateAccountStatuses
        :type request: :class:`huaweicloudsdkorganizations.v1.ListCreateAccountStatusesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListCreateAccountStatusesResponse`
        """
        return self.list_create_account_statuses_with_http_info(request)

    def list_create_account_statuses_with_http_info(self, request):
        all_params = ['states', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/create-account-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCreateAccountStatusesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def move_account(self, request):
        """移动帐号

        将帐号从其当前源位置（根或组织单元）移动到指定的目标位置（根或组织单元）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MoveAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.MoveAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.MoveAccountResponse`
        """
        return self.move_account_with_http_info(request)

    def move_account_with_http_info(self, request):
        all_params = ['account_id', 'move_account_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v1/organizations/accounts/{account_id}/move',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MoveAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_account(self, request):
        """移除指定的帐号

        从组织中移除指定的帐号。移除的帐号将成为一个独立帐号，该帐号不是任何组织的成员。此操作只能由组织的管理帐号调用。只有当帐号配置了作为独立帐号运行所需的信息时，您才能从组织中移除帐号。注意，要移除的帐号不能是组织启用的任何服务的委托管理员帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.RemoveAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.RemoveAccountResponse`
        """
        return self.remove_account_with_http_info(request)

    def remove_account_with_http_info(self, request):
        all_params = ['account_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v1/organizations/accounts/{account_id}/remove',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_account(self, request):
        """查询帐号信息

        查询有关指定帐号的信息。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccount
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowAccountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowAccountResponse`
        """
        return self.show_account_with_http_info(request)

    def show_account_with_http_info(self, request):
        all_params = ['account_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v1/organizations/accounts/{account_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_create_account_status(self, request):
        """查询有关创建帐号状态的信息

        检索创建帐号的异步请求的当前状态。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCreateAccountStatus
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowCreateAccountStatusRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowCreateAccountStatusResponse`
        """
        return self.show_create_account_status_with_http_info(request)

    def show_create_account_status_with_http_info(self, request):
        all_params = ['create_account_status_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'create_account_status_id' in local_var_params:
            path_params['create_account_status_id'] = local_var_params['create_account_status_id']

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
            resource_path='/v1/organizations/create-account-status/{create_account_status_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCreateAccountStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def deregister_delegated_administrator(self, request):
        """注销服务的委托管理员

        删除指定成员帐号作为指定服务的委托管理员。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeregisterDelegatedAdministrator
        :type request: :class:`huaweicloudsdkorganizations.v1.DeregisterDelegatedAdministratorRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeregisterDelegatedAdministratorResponse`
        """
        return self.deregister_delegated_administrator_with_http_info(request)

    def deregister_delegated_administrator_with_http_info(self, request):
        all_params = ['delegated_administrator_req_body']
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
            resource_path='/v1/organizations/delegated-administrators/deregister',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeregisterDelegatedAdministratorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_delegated_administrators(self, request):
        """列出此组织中指定为委托管理员的帐号

        列出在此组织中指定为委派管理员的帐号。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDelegatedAdministrators
        :type request: :class:`huaweicloudsdkorganizations.v1.ListDelegatedAdministratorsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListDelegatedAdministratorsResponse`
        """
        return self.list_delegated_administrators_with_http_info(request)

    def list_delegated_administrators_with_http_info(self, request):
        all_params = ['service_principal', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/delegated-administrators',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDelegatedAdministratorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_delegated_services(self, request):
        """列出指定帐号是其委托管理员的服务

        列出指定帐号是其委托管理员的服务。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDelegatedServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListDelegatedServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListDelegatedServicesResponse`
        """
        return self.list_delegated_services_with_http_info(request)

    def list_delegated_services_with_http_info(self, request):
        all_params = ['account_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/accounts/{account_id}/delegated-services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDelegatedServicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_delegated_administrator(self, request):
        """注册作为服务委托管理员

        指定成员帐号能够管理指定服务的组织功能。此接口授予委托管理员对组织服务数据的只读访问权限。委托管理员帐号中的IAM用户仍需要IAM权限才能访问和管理服务。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDelegatedAdministrator
        :type request: :class:`huaweicloudsdkorganizations.v1.RegisterDelegatedAdministratorRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.RegisterDelegatedAdministratorResponse`
        """
        return self.register_delegated_administrator_with_http_info(request)

    def register_delegated_administrator_with_http_info(self, request):
        all_params = ['delegated_administrator_req_body']
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
            resource_path='/v1/organizations/delegated-administrators/register',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RegisterDelegatedAdministratorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def accept_handshake(self, request):
        """接受邀请

        向邀请的发起方发送应答，接受加入组织邀请。在您接受邀请后，此邀请信息将继续保留并出现在相关API的返回结果中，保留期限为30天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AcceptHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.AcceptHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.AcceptHandshakeResponse`
        """
        return self.accept_handshake_with_http_info(request)

    def accept_handshake_with_http_info(self, request):
        all_params = ['handshake_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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
            resource_path='/v1/received-handshakes/{handshake_id}/accept',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AcceptHandshakeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_handshake(self, request):
        """取消邀请

        取消邀请，此时邀请状态将设置为已取消。此接口只能由发起邀请的帐号调用。取消邀请后，此邀请信息将继续保留并出现在相关API的返回结果中，保留期限为30天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.CancelHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CancelHandshakeResponse`
        """
        return self.cancel_handshake_with_http_info(request)

    def cancel_handshake_with_http_info(self, request):
        all_params = ['handshake_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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
            resource_path='/v1/organizations/handshakes/{handshake_id}/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelHandshakeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def decline_handshake(self, request):
        """拒绝邀请

        拒绝邀请请求。受邀帐号拒绝邀请，此时当前邀请状态将设置为拒绝，邀请停止。此接口只能由受邀帐号调用。邀请发起者无法再次激活被拒绝的邀请，但可以重新发送新的邀请。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeclineHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.DeclineHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeclineHandshakeResponse`
        """
        return self.decline_handshake_with_http_info(request)

    def decline_handshake_with_http_info(self, request):
        all_params = ['handshake_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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
            resource_path='/v1/received-handshakes/{handshake_id}/decline',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeclineHandshakeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_handshakes(self, request):
        """列出发送的邀请

        列出所属组织发送的邀请。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHandshakes
        :type request: :class:`huaweicloudsdkorganizations.v1.ListHandshakesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListHandshakesResponse`
        """
        return self.list_handshakes_with_http_info(request)

    def list_handshakes_with_http_info(self, request):
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
            resource_path='/v1/organizations/handshakes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHandshakesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_received_handshakes(self, request):
        """列出收到的邀请

        列出帐号收到的所有邀请。此操作可以由任何帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReceivedHandshakes
        :type request: :class:`huaweicloudsdkorganizations.v1.ListReceivedHandshakesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListReceivedHandshakesResponse`
        """
        return self.list_received_handshakes_with_http_info(request)

    def list_received_handshakes_with_http_info(self, request):
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
            resource_path='/v1/received-handshakes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListReceivedHandshakesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_handshake(self, request):
        """查询邀请相关信息

        查询组织中已有帐号邀请的相关信息。此接口可以由组织中的任何帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHandshake
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowHandshakeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowHandshakeResponse`
        """
        return self.show_handshake_with_http_info(request)

    def show_handshake_with_http_info(self, request):
        all_params = ['handshake_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'handshake_id' in local_var_params:
            path_params['handshake_id'] = local_var_params['handshake_id']

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
            resource_path='/v1/organizations/handshakes/{handshake_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHandshakeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_entities(self, request):
        """列出组织中的根、组织单元和帐号

        列出组织中包含的所有根、组织单元和帐号。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。您可以通过指定父ID和子ID参数来过滤实体。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEntities
        :type request: :class:`huaweicloudsdkorganizations.v1.ListEntitiesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListEntitiesResponse`
        """
        return self.list_entities_with_http_info(request)

    def list_entities_with_http_info(self, request):
        all_params = ['parent_id', 'child_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/entities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEntitiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_services(self, request):
        """列出所有可以与组织服务集成的云服务

        列出所有可以与组织服务集成的云服务。集成后云服务将成为组织的可信服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListServicesResponse`
        """
        return self.list_services_with_http_info(request)

    def list_services_with_http_info(self, request):
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
            resource_path='/v1/organizations/services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListServicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tag_policy_services(self, request):
        """列出被添加到标签策略强制执行的资源类型

        List all services and resource type that could integrate with tag policy.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagPolicyServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTagPolicyServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTagPolicyServicesResponse`
        """
        return self.list_tag_policy_services_with_http_info(request)

    def list_tag_policy_services_with_http_info(self, request):
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
            resource_path='/v1/organizations/tag-policy-services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagPolicyServicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_effective_policies(self, request):
        """查询有效的策略

        查询指定策略类型和帐户的有效策略信息。当前此接口不支持查询服务控制策略（service_control_policy）。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEffectivePolicies
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowEffectivePoliciesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowEffectivePoliciesResponse`
        """
        return self.show_effective_policies_with_http_info(request)

    def show_effective_policies_with_http_info(self, request):
        all_params = ['entity_id', 'policy_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'entity_id' in local_var_params:
            query_params.append(('entity_id', local_var_params['entity_id']))
        if 'policy_type' in local_var_params:
            query_params.append(('policy_type', local_var_params['policy_type']))

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
            resource_path='/v1/organizations/entities/effective-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEffectivePoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_organization(self, request):
        """创建组织

        创建组织。调用此接口的帐号将自动成为新组织的管理帐号，调用此接口的帐号凭证必须是新组织管理帐号的帐号凭证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationResponse`
        """
        return self.create_organization_with_http_info(request)

    def create_organization_with_http_info(self, request):
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
            resource_path='/v1/organizations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrganizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_organization(self, request):
        """删除组织

        删除组织。您必须使用管理帐号才能删除组织，并且先移除组织中的所有帐号、组织单元和策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationResponse`
        """
        return self.delete_organization_with_http_info(request)

    def delete_organization_with_http_info(self, request):
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
            resource_path='/v1/organizations',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteOrganizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def leave_organization(self, request):
        """离开当前组织

        此操作只能由组织的成员帐号调用。只有当组织帐号配置了作为独立帐号运行所需的信息时，您才能作为成员账户离开组织。要离开的帐号不能是组织启用的任何服务的委托管理员帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LeaveOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.LeaveOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.LeaveOrganizationResponse`
        """
        return self.leave_organization_with_http_info(request)

    def leave_organization_with_http_info(self, request):
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
            resource_path='/v1/organizations/leave',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='LeaveOrganizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_roots(self, request):
        """列出组织的根

        列出当前组织的根。此接口只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRoots
        :type request: :class:`huaweicloudsdkorganizations.v1.ListRootsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListRootsResponse`
        """
        return self.list_roots_with_http_info(request)

    def list_roots_with_http_info(self, request):
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
            resource_path='/v1/organizations/roots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRootsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organization(self, request):
        """查询所属组织信息

        查询帐号所属组织的信息。此操作可以由组织中的任何帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganization
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationResponse`
        """
        return self.show_organization_with_http_info(request)

    def show_organization_with_http_info(self, request):
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
            resource_path='/v1/organizations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_organizational_unit(self, request):
        """创建组织单元

        在根或父组织单元中创建组织单元。组织单元是帐号的容器，使您能够对帐号进行分组管理，并根据业务要求应用策略。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateOrganizationalUnitResponse`
        """
        return self.create_organizational_unit_with_http_info(request)

    def create_organizational_unit_with_http_info(self, request):
        all_params = ['create_organizational_unit_req_body']
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
            resource_path='/v1/organizations/organizational-units',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOrganizationalUnitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_organizational_unit(self, request):
        """删除组织单元

        从根或其他组织单元中删除组织单元。前提是您必须先移除该组织单元中的所有成员帐号或将成员帐号移动至其他组织单元，必须删除该组织单元中的所有子组织单元。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeleteOrganizationalUnitResponse`
        """
        return self.delete_organizational_unit_with_http_info(request)

    def delete_organizational_unit_with_http_info(self, request):
        all_params = ['organizational_unit_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organizational_unit_id' in local_var_params:
            path_params['organizational_unit_id'] = local_var_params['organizational_unit_id']

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
            resource_path='/v1/organizations/organizational-units/{organizational_unit_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteOrganizationalUnitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_organizational_units(self, request):
        """列出组织单元

        列出组织中的所有组织单元。如果指定父级组织单元，则将获得父级直系子级的组织单元列表。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrganizationalUnits
        :type request: :class:`huaweicloudsdkorganizations.v1.ListOrganizationalUnitsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListOrganizationalUnitsResponse`
        """
        return self.list_organizational_units_with_http_info(request)

    def list_organizational_units_with_http_info(self, request):
        all_params = ['parent_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/organizational-units',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOrganizationalUnitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_organizational_unit(self, request):
        """查询有关组织单元的信息

        查询有关组织单元的信息。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowOrganizationalUnitResponse`
        """
        return self.show_organizational_unit_with_http_info(request)

    def show_organizational_unit_with_http_info(self, request):
        all_params = ['organizational_unit_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organizational_unit_id' in local_var_params:
            path_params['organizational_unit_id'] = local_var_params['organizational_unit_id']

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
            resource_path='/v1/organizations/organizational-units/{organizational_unit_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOrganizationalUnitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_organizational_unit(self, request):
        """更改组织单元名称

        重命名指定的组织单元。重命名后组织单元ID不变，下属子组织单元和下属帐号不变，组织单元绑定的策略不变。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOrganizationalUnit
        :type request: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdateOrganizationalUnitResponse`
        """
        return self.update_organizational_unit_with_http_info(request)

    def update_organizational_unit_with_http_info(self, request):
        all_params = ['organizational_unit_id', 'update_organizational_unit_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'organizational_unit_id' in local_var_params:
            path_params['organizational_unit_id'] = local_var_params['organizational_unit_id']

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
            resource_path='/v1/organizations/organizational-units/{organizational_unit_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateOrganizationalUnitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_policy(self, request):
        """将策略跟实体绑定

        绑定策略到根、组织单元或个人账户。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.AttachPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.AttachPolicyResponse`
        """
        return self.attach_policy_with_http_info(request)

    def attach_policy_with_http_info(self, request):
        all_params = ['policy_id', 'policy_tach_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/organizations/policies/{policy_id}/attach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_policy(self, request):
        """创建策略

        创建指定类型的策略。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.CreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreatePolicyResponse`
        """
        return self.create_policy_with_http_info(request)

    def create_policy_with_http_info(self, request):
        all_params = ['create_policy_req_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v1/organizations/policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_policy(self, request):
        """删除策略

        从组织中删除指定的策略。在执行此操作之前，必须首先将策略跟所有组织单元、根和帐号解绑。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.DeletePolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeletePolicyResponse`
        """
        return self.delete_policy_with_http_info(request)

    def delete_policy_with_http_info(self, request):
        all_params = ['policy_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/organizations/policies/{policy_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_policy(self, request):
        """将策略跟实体解绑

        从根、组织单元或帐号解绑策略。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.DetachPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DetachPolicyResponse`
        """
        return self.detach_policy_with_http_info(request)

    def detach_policy_with_http_info(self, request):
        all_params = ['policy_id', 'policy_tach_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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
            resource_path='/v1/organizations/policies/{policy_id}/detach',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_policy_type(self, request):
        """禁用根中的策略类型

        禁用根中的策略类型。只有在根中启用了特定类型的策略，才能将该类型的策略绑定到根中的实体。执行此操作后，您不能再将指定类型的策略绑定到该根或该根中的任何组织单元或帐号。这是在后台执行的异步请求。您可以使用ListRoots查看指定根的策略类型的状态。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisablePolicyType
        :type request: :class:`huaweicloudsdkorganizations.v1.DisablePolicyTypeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DisablePolicyTypeResponse`
        """
        return self.disable_policy_type_with_http_info(request)

    def disable_policy_type_with_http_info(self, request):
        all_params = ['policy_type_req_body']
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
            resource_path='/v1/organizations/policies/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisablePolicyTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_policy_type(self, request):
        """在根中启用策略类型

        在根中启用策略类型。在根中启用策略类型后，您可以将该类型的策略绑定到根、或该根中的任何组织单元和帐号。这是在后台执行的异步请求。您可以使用ListRoots查看指定根的策略类型的状态。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnablePolicyType
        :type request: :class:`huaweicloudsdkorganizations.v1.EnablePolicyTypeRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.EnablePolicyTypeResponse`
        """
        return self.enable_policy_type_with_http_info(request)

    def enable_policy_type_with_http_info(self, request):
        all_params = ['policy_type_req_body']
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
            resource_path='/v1/organizations/policies/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnablePolicyTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_entities_for_policy(self, request):
        """列出跟指定策略绑定的所有实体

        列出跟指定策略绑定的所有根、组织单元和帐号。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEntitiesForPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.ListEntitiesForPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListEntitiesForPolicyResponse`
        """
        return self.list_entities_for_policy_with_http_info(request)

    def list_entities_for_policy_with_http_info(self, request):
        all_params = ['policy_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/policies/{policy_id}/attached-entities',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEntitiesForPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_policies(self, request):
        """列出策略

        列出组织中的所有策略。如果指定了资源ID，例如组织单元ID或帐号ID，则将获得该资源已绑定的策略列表。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPolicies
        :type request: :class:`huaweicloudsdkorganizations.v1.ListPoliciesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListPoliciesResponse`
        """
        return self.list_policies_with_http_info(request)

    def list_policies_with_http_info(self, request):
        all_params = ['attached_entity_id', 'limit', 'marker', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_policy(self, request):
        """查询策略相关信息

        检索策略的相关信息。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowPolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowPolicyResponse`
        """
        return self.show_policy_with_http_info(request)

    def show_policy_with_http_info(self, request):
        all_params = ['policy_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/policies/{policy_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_policy(self, request):
        """更新策略

        更新策略，可以更新策略的名称、描述或内容。如果不提供任何参数，则策略将保持不变。您不能更改策略的类型。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePolicy
        :type request: :class:`huaweicloudsdkorganizations.v1.UpdatePolicyRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UpdatePolicyResponse`
        """
        return self.update_policy_with_http_info(request)

    def update_policy_with_http_info(self, request):
        all_params = ['policy_id', 'update_policy_req_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v1/organizations/policies/{policy_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_tag_resource(self, request):
        """为指定资源添加标签

        向指定的资源添加一个或多个标签。目前，您可以将标签附加到组织中的帐号、组织单元、根和策略。此操作只能由组织的管理帐号调用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.CreateTagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateTagResourceResponse`
        """
        return self.create_tag_resource_with_http_info(request)

    def create_tag_resource_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'tag_resource_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/organizations/{resource_type}/{resource_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTagResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag_resource(self, request):
        """从指定资源中删除指定主键标签

        从指定资源中删除具有指定主键的任何标签。您可以将标签绑定到组织中的帐号、组织单元、根和策略。此操作只能由组织的管理帐号调用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.DeleteTagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DeleteTagResourceResponse`
        """
        return self.delete_tag_resource_with_http_info(request)

    def delete_tag_resource_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'tag_resource_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/organizations/{resource_type}/{resource_id}/tags/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_instances(self, request):
        """根据资源类型及标签信息查询实例列表

        根据资源类型及标签信息查询实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdkorganizations.v1.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListResourceInstancesResponse`
        """
        return self.list_resource_instances_with_http_info(request)

    def list_resource_instances_with_http_info(self, request):
        all_params = ['resource_type', 'resource_instance_req_body', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v1/organizations/{resource_type}/resource-instances/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_tags(self, request):
        """查询项目标签

        查询项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdkorganizations.v1.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListResourceTagsResponse`
        """
        return self.list_resource_tags_with_http_info(request)

    def list_resource_tags_with_http_info(self, request):
        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tag_resources(self, request):
        """列出绑定到指定资源的标签

        列出绑定到指定资源的标签。您可以将标签附加到组织中的帐号、组织单元、根和策略。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagResources
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTagResourcesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTagResourcesResponse`
        """
        return self.list_tag_resources_with_http_info(request)

    def list_tag_resources_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/{resource_type}/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_for_resource(self, request):
        """列出绑定到指定资源的标签

        列出绑定到指定资源的标签。您可以将标签附加到组织中的帐号、组织单元、根和策略。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagsForResource
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTagsForResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTagsForResourceResponse`
        """
        return self.list_tags_for_resource_with_http_info(request)

    def list_tags_for_resource_with_http_info(self, request):
        all_params = ['resource_id', 'limit', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/resources/{resource_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsForResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_instances_count(self, request):
        """根据资源类型及标签信息查询实例数量

        根据资源类型及标签信息查询实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceInstancesCount
        :type request: :class:`huaweicloudsdkorganizations.v1.ShowResourceInstancesCountRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ShowResourceInstancesCountResponse`
        """
        return self.show_resource_instances_count_with_http_info(request)

    def show_resource_instances_count_with_http_info(self, request):
        all_params = ['resource_type', 'resource_instance_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
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

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/organizations/{resource_type}/resource-instances/count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceInstancesCountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def tag_resource(self, request):
        """为指定资源添加标签

        向指定的资源添加一个或多个标签。目前，您可以将标签附加到组织中的帐号、组织单元、根和策略。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.TagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.TagResourceResponse`
        """
        return self.tag_resource_with_http_info(request)

    def tag_resource_with_http_info(self, request):
        all_params = ['resource_id', 'tag_resource_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/organizations/resources/{resource_id}/tag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TagResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def untag_resource(self, request):
        """从指定资源中删除指定主键标签

        从指定资源中删除具有指定主键的任何标签。您可以将标签绑定到组织中的帐号、组织单元、根和策略。此操作只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UntagResource
        :type request: :class:`huaweicloudsdkorganizations.v1.UntagResourceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.UntagResourceResponse`
        """
        return self.untag_resource_with_http_info(request)

    def untag_resource_with_http_info(self, request):
        all_params = ['resource_id', 'untag_resource_req_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/organizations/resources/{resource_id}/untag',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UntagResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def disable_trusted_service(self, request):
        """禁用受信任服务

        禁用服务（由service_principal指定的服务）与组织的集成。禁用可信服务后，指定服务将不可以在组织中的新帐号中创建服务关联委托。这意味着该服务无法代表您对组织中的任何新帐号执行操作。在服务完成从组织中的清理之前，服务仍可以在旧帐号中执行操作。此接口只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisableTrustedService
        :type request: :class:`huaweicloudsdkorganizations.v1.DisableTrustedServiceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.DisableTrustedServiceResponse`
        """
        return self.disable_trusted_service_with_http_info(request)

    def disable_trusted_service_with_http_info(self, request):
        all_params = ['trusted_service_req_body']
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
            resource_path='/v1/organizations/trusted-services/disable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DisableTrustedServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_trusted_service(self, request):
        """启用可信服务

        启用服务（由service_principal指定的服务）与组织的集成。启用可信服务后，允许指定的可信服务对组织中的所有帐号创建服务关联委托。这允许可信服务代表您在组织及其帐号中执行操作。此接口只能由组织的管理帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableTrustedService
        :type request: :class:`huaweicloudsdkorganizations.v1.EnableTrustedServiceRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.EnableTrustedServiceResponse`
        """
        return self.enable_trusted_service_with_http_info(request)

    def enable_trusted_service_with_http_info(self, request):
        all_params = ['trusted_service_req_body']
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
            resource_path='/v1/organizations/trusted-services/enable',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableTrustedServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_trusted_services(self, request):
        """列出组织的可信服务列表

        返回启用与组织集成的可信服务列表。此操作只能由组织的管理帐号或作为服务委托管理员的成员帐号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTrustedServices
        :type request: :class:`huaweicloudsdkorganizations.v1.ListTrustedServicesRequest`
        :rtype: :class:`huaweicloudsdkorganizations.v1.ListTrustedServicesResponse`
        """
        return self.list_trusted_services_with_http_info(request)

    def list_trusted_services_with_http_info(self, request):
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
            resource_path='/v1/organizations/trusted-services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTrustedServicesResponse',
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

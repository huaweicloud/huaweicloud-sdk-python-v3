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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkidentitycenter'")


class IdentityCenterClient(Client):
    def __init__(self):
        super(IdentityCenterClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidentitycenter.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "IdentityCenterClient":
                raise TypeError("client type error, support client type is IdentityCenterClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def create_account_assignment(self, request):
        r"""创建账户分配

        使用指定的权限集为指定账户分配对应主体的访问权限，主体可为IdentityCenter用户或IdentityCenter用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccountAssignment
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentResponse`
        """
        http_info = self._create_account_assignment_http_info(request)
        return self._call_api(**http_info)

    def create_account_assignment_invoker(self, request):
        http_info = self._create_account_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_account_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/account-assignments/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccountAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_account_assignment(self, request):
        r"""删除账号分配

        使用指定的权限集从指定的账号删除主体的访问权限，主体可为IAM身份中心用户或用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAccountAssignment
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteAccountAssignmentRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteAccountAssignmentResponse`
        """
        http_info = self._delete_account_assignment_http_info(request)
        return self._call_api(**http_info)

    def delete_account_assignment_invoker(self, request):
        http_info = self._delete_account_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_account_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/account-assignments/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAccountAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def describe_account_assignment_creation_status(self, request):
        r"""查询账户分配创建状态详情

        根据请求ID，查询指定IAM Identity Center实例下的账户分配创建状态详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeAccountAssignmentCreationStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentCreationStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentCreationStatusResponse`
        """
        http_info = self._describe_account_assignment_creation_status_http_info(request)
        return self._call_api(**http_info)

    def describe_account_assignment_creation_status_invoker(self, request):
        http_info = self._describe_account_assignment_creation_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_account_assignment_creation_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/account-assignments/creation-status/{request_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeAccountAssignmentCreationStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

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

    def describe_account_assignment_deletion_status(self, request):
        r"""查询账户分配删除状态详情

        根据请求ID，查询指定IAM Identity Center实例下的账户分配删除状态详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeAccountAssignmentDeletionStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentDeletionStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentDeletionStatusResponse`
        """
        http_info = self._describe_account_assignment_deletion_status_http_info(request)
        return self._call_api(**http_info)

    def describe_account_assignment_deletion_status_invoker(self, request):
        http_info = self._describe_account_assignment_deletion_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_account_assignment_deletion_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/account-assignments/deletion-status/{request_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeAccountAssignmentDeletionStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

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

    def disassociate_profile(self, request):
        r"""解除与用户或组绑定的所有账号授权关联

        解除与用户或组绑定的所有账号授权关联。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DisassociateProfile
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DisassociateProfileRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DisassociateProfileResponse`
        """
        http_info = self._disassociate_profile_http_info(request)
        return self._call_api(**http_info)

    def disassociate_profile_invoker(self, request):
        http_info = self._disassociate_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _disassociate_profile_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/disassociate-profile",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_account_assignment_creation_status(self, request):
        r"""列出账户分配创建状态

        查询指定IAM Identity Center实例下的账户分配的创建状态列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccountAssignmentCreationStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentCreationStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentCreationStatusResponse`
        """
        http_info = self._list_account_assignment_creation_status_http_info(request)
        return self._call_api(**http_info)

    def list_account_assignment_creation_status_invoker(self, request):
        http_info = self._list_account_assignment_creation_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_account_assignment_creation_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/account-assignments/creation-statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountAssignmentCreationStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_account_assignment_deletion_status(self, request):
        r"""列出账户分配删除状态

        查询指定IAM Identity Center实例下的账户分配的删除状态列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccountAssignmentDeletionStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentDeletionStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentDeletionStatusResponse`
        """
        http_info = self._list_account_assignment_deletion_status_http_info(request)
        return self._call_api(**http_info)

    def list_account_assignment_deletion_status_invoker(self, request):
        http_info = self._list_account_assignment_deletion_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_account_assignment_deletion_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/account-assignments/deletion-statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountAssignmentDeletionStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_account_assignments(self, request):
        r"""列出账户和权限集关联的用户或用户组

        列出与指定账户以及指定权限集关联的用户或用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccountAssignments
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentsResponse`
        """
        http_info = self._list_account_assignments_http_info(request)
        return self._call_api(**http_info)

    def list_account_assignments_invoker(self, request):
        http_info = self._list_account_assignments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_account_assignments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/account-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountAssignmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))
        if 'permission_set_id' in local_var_params:
            query_params.append(('permission_set_id', local_var_params['permission_set_id']))

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

    def list_account_assignments_for_principal(self, request):
        r"""检索与用户或用户组关联的账号列表

        检索与用户或用户组关联的账号列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccountAssignmentsForPrincipal
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentsForPrincipalRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentsForPrincipalResponse`
        """
        http_info = self._list_account_assignments_for_principal_http_info(request)
        return self._call_api(**http_info)

    def list_account_assignments_for_principal_invoker(self, request):
        http_info = self._list_account_assignments_for_principal_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_account_assignments_for_principal_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/account-assignments-for-principals",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountAssignmentsForPrincipalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'principal_id' in local_var_params:
            query_params.append(('principal_id', local_var_params['principal_id']))
        if 'principal_type' in local_var_params:
            query_params.append(('principal_type', local_var_params['principal_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))

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

    def create_application_instance(self, request):
        r"""创建应用程序实例

        创建应用程序实例。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApplicationInstance
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateApplicationInstanceRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateApplicationInstanceResponse`
        """
        http_info = self._create_application_instance_http_info(request)
        return self._call_api(**http_info)

    def create_application_instance_invoker(self, request):
        http_info = self._create_application_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_application_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/application-instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_application_instance(self, request):
        r"""删除应用程序实例

        删除应用程序实例。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplicationInstance
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteApplicationInstanceRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteApplicationInstanceResponse`
        """
        http_info = self._delete_application_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_application_instance_invoker(self, request):
        http_info = self._delete_application_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def delete_profile(self, request):
        r"""删除应用程序实例与用户或用户组关联关系

        删除应用程序实例与用户或用户组关联关系。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProfile
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteProfileRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteProfileResponse`
        """
        http_info = self._delete_profile_http_info(request)
        return self._call_api(**http_info)

    def delete_profile_invoker(self, request):
        http_info = self._delete_profile_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_profile_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/profiles/{profile_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProfileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']
        if 'profile_id' in local_var_params:
            path_params['profile_id'] = local_var_params['profile_id']

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

    def describe_application(self, request):
        r"""查询应用程序详情

        查询应用程序详情。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeApplication
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeApplicationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeApplicationResponse`
        """
        http_info = self._describe_application_http_info(request)
        return self._call_api(**http_info)

    def describe_application_invoker(self, request):
        http_info = self._describe_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_application_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/applications/{application_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def describe_application_provider(self, request):
        r"""查询应用程序提供者详情

        查询应用程序提供者详情。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeApplicationProvider
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeApplicationProviderRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeApplicationProviderResponse`
        """
        http_info = self._describe_application_provider_http_info(request)
        return self._call_api(**http_info)

    def describe_application_provider_invoker(self, request):
        http_info = self._describe_application_provider_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_application_provider_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/application-providers/{application_provider_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeApplicationProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_provider_id' in local_var_params:
            path_params['application_provider_id'] = local_var_params['application_provider_id']

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

    def get_application_assignment_configuration(self, request):
        r"""查询应用程序分配属性配置

        查询应用程序分配属性配置，目的为用户或者用户组分配对应用程序的访问权限。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetApplicationAssignmentConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetApplicationAssignmentConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetApplicationAssignmentConfigurationResponse`
        """
        http_info = self._get_application_assignment_configuration_http_info(request)
        return self._call_api(**http_info)

    def get_application_assignment_configuration_invoker(self, request):
        http_info = self._get_application_assignment_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_application_assignment_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/applications/{application_instance_id}/assignments-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "GetApplicationAssignmentConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def get_application_instance(self, request):
        r"""查询应用程序实例详情

        查询应用程序实例详情。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetApplicationInstance
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetApplicationInstanceRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetApplicationInstanceResponse`
        """
        http_info = self._get_application_instance_http_info(request)
        return self._call_api(**http_info)

    def get_application_instance_invoker(self, request):
        http_info = self._get_application_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_application_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "GetApplicationInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def import_application_instance_service_provider_metadata(self, request):
        r"""上传应用程序实例元数据文件

        上传应用程序实例元数据文件。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportApplicationInstanceServiceProviderMetadata
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ImportApplicationInstanceServiceProviderMetadataRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ImportApplicationInstanceServiceProviderMetadataResponse`
        """
        http_info = self._import_application_instance_service_provider_metadata_http_info(request)
        return self._call_api(**http_info)

    def import_application_instance_service_provider_metadata_invoker(self, request):
        http_info = self._import_application_instance_service_provider_metadata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_application_instance_service_provider_metadata_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ImportApplicationInstanceServiceProviderMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def list_application_instances(self, request):
        r"""列出应用程序实例

        列出应用程序实例。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationInstances
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationInstancesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationInstancesResponse`
        """
        http_info = self._list_application_instances_http_info(request)
        return self._call_api(**http_info)

    def list_application_instances_invoker(self, request):
        http_info = self._list_application_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/application-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_application_providers(self, request):
        r"""列出应用程序提供者

        查询应用程序提供者列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationProviders
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationProvidersRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationProvidersResponse`
        """
        http_info = self._list_application_providers_http_info(request)
        return self._call_api(**http_info)

    def list_application_providers_invoker(self, request):
        http_info = self._list_application_providers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_providers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/application-providers",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationProvidersResponse"
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

    def list_application_templates(self, request):
        r"""列出应用程序模板

        查询应用程序模板列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationTemplates
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationTemplatesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationTemplatesResponse`
        """
        http_info = self._list_application_templates_http_info(request)
        return self._call_api(**http_info)

    def list_application_templates_invoker(self, request):
        http_info = self._list_application_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/application-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'application_id' in local_var_params:
            query_params.append(('application_id', local_var_params['application_id']))

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

    def list_applications(self, request):
        r"""列出应用程序

        查询应用程序列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationsResponse`
        """
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_invoker(self, request):
        http_info = self._list_applications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_applications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_catalog_applications(self, request):
        r"""列出应用程序目录中的预置应用模板

        列出应用程序目录中的预置应用模板。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCatalogApplications
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListCatalogApplicationsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListCatalogApplicationsResponse`
        """
        http_info = self._list_catalog_applications_http_info(request)
        return self._call_api(**http_info)

    def list_catalog_applications_invoker(self, request):
        http_info = self._list_catalog_applications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_catalog_applications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/catalog/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListCatalogApplicationsResponse"
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

    def list_profiles(self, request):
        r"""列出应用程序实例与用户或用户组存在的关联关系

        列出应用程序实例与用户或用户组存在的关联关系。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProfiles
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListProfilesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListProfilesResponse`
        """
        http_info = self._list_profiles_http_info(request)
        return self._call_api(**http_info)

    def list_profiles_invoker(self, request):
        http_info = self._list_profiles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_profiles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/profiles",
            "request_type": request.__class__.__name__,
            "response_type": "ListProfilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_display_data(self, request):
        r"""更新应用程序实例显示信息

        更新应用程序实例显示信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceDisplayData
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceDisplayDataRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceDisplayDataResponse`
        """
        http_info = self._update_application_instance_display_data_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_display_data_invoker(self, request):
        http_info = self._update_application_instance_display_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_display_data_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/display-data",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceDisplayDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_response_configuration(self, request):
        r"""更新应用程序属性配置

        更新应用程序属性配置信息，更新应用程序中的属性映射、中继状态以及会话过期时间。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceResponseConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceResponseConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceResponseConfigurationResponse`
        """
        http_info = self._update_application_instance_response_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_response_configuration_invoker(self, request):
        http_info = self._update_application_instance_response_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_response_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/response-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceResponseConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_response_schema_configuration(self, request):
        r"""更新应用程序Schema属性映射配置

        更新应用程序Schema属性映射配置，支持SAML断言中Subject属性映射以及Subject NameID格式。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceResponseSchemaConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceResponseSchemaConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceResponseSchemaConfigurationResponse`
        """
        http_info = self._update_application_instance_response_schema_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_response_schema_configuration_invoker(self, request):
        http_info = self._update_application_instance_response_schema_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_response_schema_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/response-schema-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceResponseSchemaConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_security_configuration(self, request):
        r"""更新应用程序实例证书配置

        更新应用程序实例证书配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceSecurityConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceSecurityConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceSecurityConfigurationResponse`
        """
        http_info = self._update_application_instance_security_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_security_configuration_invoker(self, request):
        http_info = self._update_application_instance_security_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_security_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/security-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceSecurityConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_service_provider_configuration(self, request):
        r"""更新应用程序实例服务提供商配置

        更新应用程序实例服务提供商配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceServiceProviderConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceServiceProviderConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceServiceProviderConfigurationResponse`
        """
        http_info = self._update_application_instance_service_provider_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_service_provider_configuration_invoker(self, request):
        http_info = self._update_application_instance_service_provider_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_service_provider_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/service-provider-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceServiceProviderConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_status(self, request):
        r"""更新应用程序实例状态

        更新应用程序实例状态。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceStatusResponse`
        """
        http_info = self._update_application_instance_status_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_status_invoker(self, request):
        http_info = self._update_application_instance_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def create_application_assignment(self, request):
        r"""应用程序分配用户或用户组

        应用程序分配用户或用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApplicationAssignment
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateApplicationAssignmentRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateApplicationAssignmentResponse`
        """
        http_info = self._create_application_assignment_http_info(request)
        return self._call_api(**http_info)

    def create_application_assignment_invoker(self, request):
        http_info = self._create_application_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_application_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/applications/{application_instance_id}/assignments/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def delete_application_assignment(self, request):
        r"""删除应用程序已分配用户或用户组

        删除应用程序已分配用户或用户组。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplicationAssignment
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteApplicationAssignmentRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteApplicationAssignmentResponse`
        """
        http_info = self._delete_application_assignment_http_info(request)
        return self._call_api(**http_info)

    def delete_application_assignment_invoker(self, request):
        http_info = self._delete_application_assignment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_assignment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/applications/{application_instance_id}/assignments/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationAssignmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def list_application_assignments(self, request):
        r"""查询应用程序已分配的用户或用户组列表

        查询应用程序已分配的用户或用户组列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationAssignments
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationAssignmentsResponse`
        """
        http_info = self._list_application_assignments_http_info(request)
        return self._call_api(**http_info)

    def list_application_assignments_invoker(self, request):
        http_info = self._list_application_assignments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_assignments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/applications/{application_instance_id}/assignments",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationAssignmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def list_application_assignments_for_principal(self, request):
        r"""检索与用户或用户组关联的应用程序列表

        检索与用户或用户组关联的应用程序列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationAssignmentsForPrincipal
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationAssignmentsForPrincipalRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationAssignmentsForPrincipalResponse`
        """
        http_info = self._list_application_assignments_for_principal_http_info(request)
        return self._call_api(**http_info)

    def list_application_assignments_for_principal_invoker(self, request):
        http_info = self._list_application_assignments_for_principal_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_assignments_for_principal_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/application-assignments-for-principals",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationAssignmentsForPrincipalResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'principal_id' in local_var_params:
            query_params.append(('principal_id', local_var_params['principal_id']))
        if 'principal_type' in local_var_params:
            query_params.append(('principal_type', local_var_params['principal_type']))
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

    def create_application_instance_certificate(self, request):
        r"""创建应用程序实例证书

        创建应用程序实例证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApplicationInstanceCertificate
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateApplicationInstanceCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateApplicationInstanceCertificateResponse`
        """
        http_info = self._create_application_instance_certificate_http_info(request)
        return self._call_api(**http_info)

    def create_application_instance_certificate_invoker(self, request):
        http_info = self._create_application_instance_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_application_instance_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationInstanceCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def delete_application_instance_certificate(self, request):
        r"""删除应用程序实例证书

        删除应用程序实例证书。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplicationInstanceCertificate
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteApplicationInstanceCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteApplicationInstanceCertificateResponse`
        """
        http_info = self._delete_application_instance_certificate_http_info(request)
        return self._call_api(**http_info)

    def delete_application_instance_certificate_invoker(self, request):
        http_info = self._delete_application_instance_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_instance_certificate_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationInstanceCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']
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

    def list_application_instance_certificates(self, request):
        r"""列出应用程序实例证书

        查询应用程序实例证书列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApplicationInstanceCertificates
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationInstanceCertificatesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListApplicationInstanceCertificatesResponse`
        """
        http_info = self._list_application_instance_certificates_http_info(request)
        return self._call_api(**http_info)

    def list_application_instance_certificates_invoker(self, request):
        http_info = self._list_application_instance_certificates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_application_instance_certificates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/certificates",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationInstanceCertificatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']

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

    def update_application_instance_active_certificate(self, request):
        r"""激活应用程序实例证书

        激活应用程序实例证书，实现证书轮转。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApplicationInstanceActiveCertificate
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceActiveCertificateRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateApplicationInstanceActiveCertificateResponse`
        """
        http_info = self._update_application_instance_active_certificate_http_info(request)
        return self._call_api(**http_info)

    def update_application_instance_active_certificate_invoker(self, request):
        http_info = self._update_application_instance_active_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_application_instance_active_certificate_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/application-instances/{application_instance_id}/certificates/{certificate_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationInstanceActiveCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'application_instance_id' in local_var_params:
            path_params['application_instance_id'] = local_var_params['application_instance_id']
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

    def get_sso_configuration(self, request):
        r"""查询实例配置信息

        查询IAM身份中心实例配置信息，包括身份认证配置和会话管理配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetSsoConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetSsoConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetSsoConfigurationResponse`
        """
        http_info = self._get_sso_configuration_http_info(request)
        return self._call_api(**http_info)

    def get_sso_configuration_invoker(self, request):
        http_info = self._get_sso_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_sso_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/sso-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "GetSsoConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_sso_configuration(self, request):
        r"""设置实例配置信息

        设置IAM身份中心服务实例配置信息，包括身份认证配置和会话管理配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSsoConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateSsoConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateSsoConfigurationResponse`
        """
        http_info = self._update_sso_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_sso_configuration_invoker(self, request):
        http_info = self._update_sso_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sso_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/sso-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSsoConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_alias(self, request):
        r"""自定义访问门户URL

        自定义访问门户URL，默认情况下，您可以使用遵循以下格式的 URL访问门户：idcenter.huaweicloud.com/d-xxxxxxxxxx/portal，您可以按如下方式更改为自定义 URL：idcenter.huaweicloud.com/your_subdomain/portal。设置自定义访问门户URL是一次性操作，无法撤销。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAlias
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateAliasRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateAliasResponse`
        """
        http_info = self._create_alias_http_info(request)
        return self._call_api(**http_info)

    def create_alias_invoker(self, request):
        http_info = self._create_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_alias_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/alias",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAliasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_identity_center(self, request):
        r"""删除服务实例

        删除IAM Identity Center服务实例。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIdentityCenter
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteIdentityCenterRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteIdentityCenterResponse`
        """
        http_info = self._delete_identity_center_http_info(request)
        return self._call_api(**http_info)

    def delete_identity_center_invoker(self, request):
        http_info = self._delete_identity_center_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_identity_center_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/service/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIdentityCenterResponse"
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

    def describe_registered_regions(self, request):
        r"""查询服务实例开通所在区域

        查询IAM身份中心服务实例开通后，具体开通所在区域。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeRegisteredRegions
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeRegisteredRegionsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeRegisteredRegionsResponse`
        """
        http_info = self._describe_registered_regions_http_info(request)
        return self._call_api(**http_info)

    def describe_registered_regions_invoker(self, request):
        http_info = self._describe_registered_regions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_registered_regions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/registered-regions",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeRegisteredRegionsResponse"
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

    def get_ha_configuration(self, request):
        r"""查询高可用功能配置

        查询高可用功能配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetHaConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetHaConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetHaConfigurationResponse`
        """
        http_info = self._get_ha_configuration_http_info(request)
        return self._call_api(**http_info)

    def get_ha_configuration_invoker(self, request):
        http_info = self._get_ha_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_ha_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/disaster-recovery-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "GetHaConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def get_identity_center_service_status(self, request):
        r"""查询服务实例状态

        查询IAM Identity Center服务实例状态信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetIdentityCenterServiceStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetIdentityCenterServiceStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetIdentityCenterServiceStatusResponse`
        """
        http_info = self._get_identity_center_service_status_http_info(request)
        return self._call_api(**http_info)

    def get_identity_center_service_status_invoker(self, request):
        http_info = self._get_identity_center_service_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_identity_center_service_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/identity-center-service/status",
            "request_type": request.__class__.__name__,
            "response_type": "GetIdentityCenterServiceStatusResponse"
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

    def list_identity_store_association(self, request):
        r"""获取身份源配置

        获取IAM身份中心服务实例中的身份源配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIdentityStoreAssociation
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListIdentityStoreAssociationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListIdentityStoreAssociationResponse`
        """
        http_info = self._list_identity_store_association_http_info(request)
        return self._call_api(**http_info)

    def list_identity_store_association_invoker(self, request):
        http_info = self._list_identity_store_association_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_identity_store_association_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/identity-store-associations",
            "request_type": request.__class__.__name__,
            "response_type": "ListIdentityStoreAssociationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instances(self, request):
        r"""列出实例

        查询IAM身份中心的实例列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
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

    def register_region(self, request):
        r"""选择服务实例开通区域

        IAM身份中心服务实例开通前，需要选择服务实例具体开通在某一区域。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterRegion
        :type request: :class:`huaweicloudsdkidentitycenter.v1.RegisterRegionRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.RegisterRegionResponse`
        """
        http_info = self._register_region_http_info(request)
        return self._call_api(**http_info)

    def register_region_invoker(self, request):
        http_info = self._register_region_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_region_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/register-regions",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterRegionResponse"
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

    def start_identity_center(self, request):
        r"""开通服务实例

        开通IAM Identity Center服务实例。此操作只能由组织的管理账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartIdentityCenter
        :type request: :class:`huaweicloudsdkidentitycenter.v1.StartIdentityCenterRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.StartIdentityCenterResponse`
        """
        http_info = self._start_identity_center_http_info(request)
        return self._call_api(**http_info)

    def start_identity_center_invoker(self, request):
        http_info = self._start_identity_center_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_identity_center_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/service/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartIdentityCenterResponse"
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

    def update_ha_configuration(self, request):
        r"""更新高可用功能配置

        授权启用或者禁用高可用功能配置。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHaConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateHaConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateHaConfigurationResponse`
        """
        http_info = self._update_ha_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_ha_configuration_invoker(self, request):
        http_info = self._update_ha_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ha_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/disaster-recovery-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHaConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_access_control_attribute_configuration(self, request):
        r"""启用指定实例的访问控制功能

        启用指定实例的访问控制功能。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceAccessControlAttributeConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateInstanceAccessControlAttributeConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateInstanceAccessControlAttributeConfigurationResponse`
        """
        http_info = self._create_instance_access_control_attribute_configuration_http_info(request)
        return self._call_api(**http_info)

    def create_instance_access_control_attribute_configuration_invoker(self, request):
        http_info = self._create_instance_access_control_attribute_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_access_control_attribute_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/access-control-attribute-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceAccessControlAttributeConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_instance_access_control_attribute_configuration(self, request):
        r"""解除指定实例的访问控制属性配置

        禁用指定IAM Identity Center实例的基于属性的访问控制（ABAC）功能，并删除已配置的所有属性映射。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceAccessControlAttributeConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteInstanceAccessControlAttributeConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteInstanceAccessControlAttributeConfigurationResponse`
        """
        http_info = self._delete_instance_access_control_attribute_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_access_control_attribute_configuration_invoker(self, request):
        http_info = self._delete_instance_access_control_attribute_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_access_control_attribute_configuration_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/access-control-attribute-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceAccessControlAttributeConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def describe_instance_access_control_attribute_configuration(self, request):
        r"""获取指定实例的访问控制属性配置

        返回已配置为与指定IAM Identity Center实例的基于属性的访问控制（ABAC）一起使用的IAM Identity Center身份存储属性列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeInstanceAccessControlAttributeConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeInstanceAccessControlAttributeConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeInstanceAccessControlAttributeConfigurationResponse`
        """
        http_info = self._describe_instance_access_control_attribute_configuration_http_info(request)
        return self._call_api(**http_info)

    def describe_instance_access_control_attribute_configuration_invoker(self, request):
        http_info = self._describe_instance_access_control_attribute_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_instance_access_control_attribute_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/access-control-attribute-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeInstanceAccessControlAttributeConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_instance_access_control_attribute_configuration(self, request):
        r"""更新指定实例的访问控制属性配置

        更新可与IAM Identity Center实例一起使用的IAM Identity Center身份存储属性，以进行基于属性的访问控制（ABAC）。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceAccessControlAttributeConfiguration
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdateInstanceAccessControlAttributeConfigurationRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdateInstanceAccessControlAttributeConfigurationResponse`
        """
        http_info = self._update_instance_access_control_attribute_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_instance_access_control_attribute_configuration_invoker(self, request):
        http_info = self._update_instance_access_control_attribute_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_access_control_attribute_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/access-control-attribute-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceAccessControlAttributeConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def get_mfa_device_management_for_identity_store(self, request):
        r"""查询MFA管理配置信息

        查询MFA管理配置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetMfaDeviceManagementForIdentityStore
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetMfaDeviceManagementForIdentityStoreRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetMfaDeviceManagementForIdentityStoreResponse`
        """
        http_info = self._get_mfa_device_management_for_identity_store_http_info(request)
        return self._call_api(**http_info)

    def get_mfa_device_management_for_identity_store_invoker(self, request):
        http_info = self._get_mfa_device_management_for_identity_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_mfa_device_management_for_identity_store_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/mfa-devices/management-settings",
            "request_type": request.__class__.__name__,
            "response_type": "GetMfaDeviceManagementForIdentityStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def put_mfa_device_management_for_identity_store(self, request):
        r"""设置MFA管理设置信息

        设置MFA管理设置信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutMfaDeviceManagementForIdentityStore
        :type request: :class:`huaweicloudsdkidentitycenter.v1.PutMfaDeviceManagementForIdentityStoreRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PutMfaDeviceManagementForIdentityStoreResponse`
        """
        http_info = self._put_mfa_device_management_for_identity_store_http_info(request)
        return self._call_api(**http_info)

    def put_mfa_device_management_for_identity_store_invoker(self, request):
        http_info = self._put_mfa_device_management_for_identity_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_mfa_device_management_for_identity_store_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/mfa-devices/management-settings",
            "request_type": request.__class__.__name__,
            "response_type": "PutMfaDeviceManagementForIdentityStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def attach_managed_policy_to_permission_set(self, request):
        r"""添加系统身份策略

        在指定的权限集中添加系统身份策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachManagedPolicyToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.AttachManagedPolicyToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AttachManagedPolicyToPermissionSetResponse`
        """
        http_info = self._attach_managed_policy_to_permission_set_http_info(request)
        return self._call_api(**http_info)

    def attach_managed_policy_to_permission_set_invoker(self, request):
        http_info = self._attach_managed_policy_to_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_managed_policy_to_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/attach-managed-policy",
            "request_type": request.__class__.__name__,
            "response_type": "AttachManagedPolicyToPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def attach_managed_role_to_permission_set(self, request):
        r"""附加系统策略到权限集

        将系统策略附加到权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachManagedRoleToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.AttachManagedRoleToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AttachManagedRoleToPermissionSetResponse`
        """
        http_info = self._attach_managed_role_to_permission_set_http_info(request)
        return self._call_api(**http_info)

    def attach_managed_role_to_permission_set_invoker(self, request):
        http_info = self._attach_managed_role_to_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_managed_role_to_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/attach-managed-role",
            "request_type": request.__class__.__name__,
            "response_type": "AttachManagedRoleToPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def create_permission_set(self, request):
        r"""创建权限集

        在指定的IAM Identity Center实例中创建一个权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreatePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreatePermissionSetResponse`
        """
        http_info = self._create_permission_set_http_info(request)
        return self._call_api(**http_info)

    def create_permission_set_invoker(self, request):
        http_info = self._create_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_custom_policy_from_permission_set(self, request):
        r"""删除指定权限集中的自定义身份策略

        删除指定权限集中的自定义身份策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomPolicyFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteCustomPolicyFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteCustomPolicyFromPermissionSetResponse`
        """
        http_info = self._delete_custom_policy_from_permission_set_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_policy_from_permission_set_invoker(self, request):
        http_info = self._delete_custom_policy_from_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_custom_policy_from_permission_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/custom-policy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomPolicyFromPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def delete_custom_role_from_permission_set(self, request):
        r"""删除指定权限集中的自定义策略

        删除指定权限集中的自定义策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomRoleFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteCustomRoleFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteCustomRoleFromPermissionSetResponse`
        """
        http_info = self._delete_custom_role_from_permission_set_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_role_from_permission_set_invoker(self, request):
        http_info = self._delete_custom_role_from_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_custom_role_from_permission_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/custom-role",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomRoleFromPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def delete_permission_set(self, request):
        r"""删除权限集

        根据权限集ID，删除指定的权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeletePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeletePermissionSetResponse`
        """
        http_info = self._delete_permission_set_http_info(request)
        return self._call_api(**http_info)

    def delete_permission_set_invoker(self, request):
        http_info = self._delete_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_permission_set_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def describe_permission_set(self, request):
        r"""查询权限集详情

        根据权限集ID，查询指定权限集的详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetResponse`
        """
        http_info = self._describe_permission_set_http_info(request)
        return self._call_api(**http_info)

    def describe_permission_set_invoker(self, request):
        http_info = self._describe_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribePermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def describe_permission_set_provisioning_status(self, request):
        r"""查询权限集预分配状态详情

        根据请求Id，查询权限集预分配状态的详情信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribePermissionSetProvisioningStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetProvisioningStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetProvisioningStatusResponse`
        """
        http_info = self._describe_permission_set_provisioning_status_http_info(request)
        return self._call_api(**http_info)

    def describe_permission_set_provisioning_status_invoker(self, request):
        http_info = self._describe_permission_set_provisioning_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_permission_set_provisioning_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/provisioning-status/{request_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DescribePermissionSetProvisioningStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'request_id' in local_var_params:
            path_params['request_id'] = local_var_params['request_id']

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

    def detach_managed_policy_from_permission_set(self, request):
        r"""从权限集分离系统身份策略

        将附加的系统身份策略从指定的权限集中分离。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachManagedPolicyFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DetachManagedPolicyFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DetachManagedPolicyFromPermissionSetResponse`
        """
        http_info = self._detach_managed_policy_from_permission_set_http_info(request)
        return self._call_api(**http_info)

    def detach_managed_policy_from_permission_set_invoker(self, request):
        http_info = self._detach_managed_policy_from_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_managed_policy_from_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/detach-managed-policy",
            "request_type": request.__class__.__name__,
            "response_type": "DetachManagedPolicyFromPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def detach_managed_role_from_permission_set(self, request):
        r"""从权限集分离系统策略

        将附加的系统策略从指定的权限集中分离。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachManagedRoleFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DetachManagedRoleFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DetachManagedRoleFromPermissionSetResponse`
        """
        http_info = self._detach_managed_role_from_permission_set_http_info(request)
        return self._call_api(**http_info)

    def detach_managed_role_from_permission_set_invoker(self, request):
        http_info = self._detach_managed_role_from_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_managed_role_from_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/detach-managed-role",
            "request_type": request.__class__.__name__,
            "response_type": "DetachManagedRoleFromPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def get_custom_policy_for_permission_set(self, request):
        r"""获取分配给权限集的自定义身份策略

        获取分配给权限集的自定义身份策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetCustomPolicyForPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetCustomPolicyForPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetCustomPolicyForPermissionSetResponse`
        """
        http_info = self._get_custom_policy_for_permission_set_http_info(request)
        return self._call_api(**http_info)

    def get_custom_policy_for_permission_set_invoker(self, request):
        http_info = self._get_custom_policy_for_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_custom_policy_for_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/custom-policy",
            "request_type": request.__class__.__name__,
            "response_type": "GetCustomPolicyForPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def get_custom_role_for_permission_set(self, request):
        r"""获取分配给权限集的自定义策略

        获取分配给权限集的自定义策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetCustomRoleForPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetCustomRoleForPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetCustomRoleForPermissionSetResponse`
        """
        http_info = self._get_custom_role_for_permission_set_http_info(request)
        return self._call_api(**http_info)

    def get_custom_role_for_permission_set_invoker(self, request):
        http_info = self._get_custom_role_for_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_custom_role_for_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/custom-role",
            "request_type": request.__class__.__name__,
            "response_type": "GetCustomRoleForPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def get_permission_set_summary(self, request):
        r"""查询权限集配额信息

        查询权限集配额信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetPermissionSetSummary
        :type request: :class:`huaweicloudsdkidentitycenter.v1.GetPermissionSetSummaryRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.GetPermissionSetSummaryResponse`
        """
        http_info = self._get_permission_set_summary_http_info(request)
        return self._call_api(**http_info)

    def get_permission_set_summary_invoker(self, request):
        http_info = self._get_permission_set_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_permission_set_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-set-summary",
            "request_type": request.__class__.__name__,
            "response_type": "GetPermissionSetSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_accounts_for_provisioned_permission_set(self, request):
        r"""列出权限集关联的账号

        查询与指定权限集关联的账户列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAccountsForProvisionedPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountsForProvisionedPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountsForProvisionedPermissionSetResponse`
        """
        http_info = self._list_accounts_for_provisioned_permission_set_http_info(request)
        return self._call_api(**http_info)

    def list_accounts_for_provisioned_permission_set_invoker(self, request):
        http_info = self._list_accounts_for_provisioned_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_accounts_for_provisioned_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAccountsForProvisionedPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))

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

    def list_managed_policies_in_permission_set(self, request):
        r"""列出权限集中附加的系统身份策略

        获取附加到指定权限集的系统身份策略列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagedPoliciesInPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListManagedPoliciesInPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListManagedPoliciesInPermissionSetResponse`
        """
        http_info = self._list_managed_policies_in_permission_set_http_info(request)
        return self._call_api(**http_info)

    def list_managed_policies_in_permission_set_invoker(self, request):
        http_info = self._list_managed_policies_in_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_managed_policies_in_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/managed-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagedPoliciesInPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def list_managed_roles_in_permission_set(self, request):
        r"""列出权限集中附加的系统策略

        获取附加到指定权限集的系统策略列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListManagedRolesInPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListManagedRolesInPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListManagedRolesInPermissionSetResponse`
        """
        http_info = self._list_managed_roles_in_permission_set_http_info(request)
        return self._call_api(**http_info)

    def list_managed_roles_in_permission_set_invoker(self, request):
        http_info = self._list_managed_roles_in_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_managed_roles_in_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/managed-roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListManagedRolesInPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def list_permission_set_provisioning_status(self, request):
        r"""列出权限集预分配状态

        查询指定实例中的权限集预分配状态列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissionSetProvisioningStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetProvisioningStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetProvisioningStatusResponse`
        """
        http_info = self._list_permission_set_provisioning_status_http_info(request)
        return self._call_api(**http_info)

    def list_permission_set_provisioning_status_invoker(self, request):
        http_info = self._list_permission_set_provisioning_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_permission_set_provisioning_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/provisioning-statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionSetProvisioningStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_permission_sets(self, request):
        r"""列出权限集

        查询指定实例下的权限集列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissionSets
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsResponse`
        """
        http_info = self._list_permission_sets_http_info(request)
        return self._call_api(**http_info)

    def list_permission_sets_invoker(self, request):
        http_info = self._list_permission_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_permission_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionSetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'permission_set_id' in local_var_params:
            query_params.append(('permission_set_id', local_var_params['permission_set_id']))
        if 'permission_urn' in local_var_params:
            query_params.append(('permission_urn', local_var_params['permission_urn']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_permission_sets_provisioned_to_account(self, request):
        r"""列出分配给账户的权限集

        查询分配给指定账户的权限集列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermissionSetsProvisionedToAccount
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsProvisionedToAccountRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsProvisionedToAccountResponse`
        """
        http_info = self._list_permission_sets_provisioned_to_account_http_info(request)
        return self._call_api(**http_info)

    def list_permission_sets_provisioned_to_account_invoker(self, request):
        http_info = self._list_permission_sets_provisioned_to_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_permission_sets_provisioned_to_account_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/provisioned-to-accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionSetsProvisionedToAccountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'account_id' in local_var_params:
            query_params.append(('account_id', local_var_params['account_id']))
        if 'provisioning_status' in local_var_params:
            query_params.append(('provisioning_status', local_var_params['provisioning_status']))

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

    def provision_permission_set(self, request):
        r"""预分配权限集

        将指定权限集预分配给指定账户。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ProvisionPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ProvisionPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ProvisionPermissionSetResponse`
        """
        http_info = self._provision_permission_set_http_info(request)
        return self._call_api(**http_info)

    def provision_permission_set_invoker(self, request):
        http_info = self._provision_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _provision_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/provision",
            "request_type": request.__class__.__name__,
            "response_type": "ProvisionPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def put_custom_policy_to_permission_set(self, request):
        r"""将自定义身份策略附加到权限集

        将自定义身份策略附加到权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutCustomPolicyToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.PutCustomPolicyToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PutCustomPolicyToPermissionSetResponse`
        """
        http_info = self._put_custom_policy_to_permission_set_http_info(request)
        return self._call_api(**http_info)

    def put_custom_policy_to_permission_set_invoker(self, request):
        http_info = self._put_custom_policy_to_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_custom_policy_to_permission_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/custom-policy",
            "request_type": request.__class__.__name__,
            "response_type": "PutCustomPolicyToPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def put_custom_role_to_permission_set(self, request):
        r"""将自定义策略附加到权限集

        将自定义策略附加到权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutCustomRoleToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.PutCustomRoleToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PutCustomRoleToPermissionSetResponse`
        """
        http_info = self._put_custom_role_to_permission_set_http_info(request)
        return self._call_api(**http_info)

    def put_custom_role_to_permission_set_invoker(self, request):
        http_info = self._put_custom_role_to_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_custom_role_to_permission_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/custom-role",
            "request_type": request.__class__.__name__,
            "response_type": "PutCustomRoleToPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def update_permission_set(self, request):
        r"""更新权限集

        根据权限集ID，更新指定权限集的属性。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdatePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdatePermissionSetResponse`
        """
        http_info = self._update_permission_set_http_info(request)
        return self._call_api(**http_info)

    def update_permission_set_invoker(self, request):
        http_info = self._update_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_permission_set_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']

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

    def create_tag_resource(self, request):
        r"""为指定资源添加标签

        向指定的资源添加一个或多个标签。目前，您可以将标签附加到实例中的权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTagResource
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateTagResourceRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateTagResourceResponse`
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
            "resource_path": "/v1/instances/{resource_type}/{resource_id}/tags/create",
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
        r"""从指定资源中删除指定主键标签

        从指定资源中删除具有指定主键的任何标签。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTagResource
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteTagResourceRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteTagResourceResponse`
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
            "resource_path": "/v1/instances/{resource_type}/{resource_id}/tags/delete",
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

    def list_tag_resources(self, request):
        r"""列出绑定到指定资源的标签

        列出绑定到指定资源的标签。您可以将标签附加到实例中的权限集。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagResources
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListTagResourcesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListTagResourcesResponse`
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
            "resource_path": "/v1/instances/{resource_type}/{resource_id}/tags",
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

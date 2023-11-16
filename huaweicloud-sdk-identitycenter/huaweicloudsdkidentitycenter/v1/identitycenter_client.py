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
        """创建帐户分配

        使用指定的权限集为指定帐户分配对应主体的访问权限，主体可为IdentityCenter用户或IdentityCenter用户组
        
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
        """使用指定的权限集从指定帐户删除主体的访问权限

        使用指定的权限集从指定帐户删除主体的访问权限
        
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
        """查询账号分配请求的状态

        根据请求ID，查询指定IAM Identity Center实例下的帐户分配创建状态详情信息
        
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
        """查询账户分配删除状态详情

        根据请求ID，查询指定IAM Identity Center实例下的帐户分配删除状态详情信息
        
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

    def list_account_assignment_creation_status(self, request):
        """列出账户分配创建状态

        查询指定IAM Identity Center实例下的帐户分配的创建状态列表
        
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
        """列出账户分配删除状态

        查询指定IAM Identity Center实例下的帐户分配的删除状态列表
        
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
        """列出与指定权限集以及指定帐户关联的用户/用户组

        列出与指定权限集以及指定帐户关联的用户/用户组
        
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

    def list_profile_associations(self, request):
        """查询profile关联的用户或组列表

        查询profile关联的用户或组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProfileAssociations
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListProfileAssociationsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListProfileAssociationsResponse`
        """
        http_info = self._list_profile_associations_http_info(request)
        return self._call_api(**http_info)

    def list_profile_associations_invoker(self, request):
        http_info = self._list_profile_associations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_profile_associations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/profile-associations",
            "request_type": request.__class__.__name__,
            "response_type": "ListProfileAssociationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'profile_id' in local_var_params:
            query_params.append(('profile_id', local_var_params['profile_id']))

        header_params = {}

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
        """查询实例列表

        查询 IAM Identity Center的资源实例列表.
        
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

    def attach_customer_managed_policy_to_permission_set(self, request):
        """将指定的客户自定义管理策略附加到指定的权限集

        将指定的客户自定义管理策略附加到指定的权限集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachCustomerManagedPolicyToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.AttachCustomerManagedPolicyToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AttachCustomerManagedPolicyToPermissionSetResponse`
        """
        http_info = self._attach_customer_managed_policy_to_permission_set_http_info(request)
        return self._call_api(**http_info)

    def attach_customer_managed_policy_to_permission_set_invoker(self, request):
        http_info = self._attach_customer_managed_policy_to_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_customer_managed_policy_to_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/attach-customer-managed-policy",
            "request_type": request.__class__.__name__,
            "response_type": "AttachCustomerManagedPolicyToPermissionSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'permission_set_id' in local_var_params:
            path_params['permission_set_id'] = local_var_params['permission_set_id']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
        """将系统管理策略附加到权限集

        将系统管理策略附加到权限集
        
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
        """在指定的IAM Identity Center实例中创建权限集

        在指定的IAM Identity Center实例中创建一个权限集
        
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

    def delete_permission_set(self, request):
        """删除指定实例的权限集

        删除指定实例的权限集
        
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
        """查询权限集详情

        根据权限集ID，查询指定权限集的详情信息
        
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
        """查询权限集预分配状态详情

        根据请求Id，查询权限集预分配状态的详情信息
        
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

    def detach_customer_managed_policy_reference_from_permission_set(self, request):
        """将附加的客户自定义管理策略从指定的权限集中分离

        将附加的客户自定义管理策略从指定的权限集中分离
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetachCustomerManagedPolicyReferenceFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DetachCustomerManagedPolicyReferenceFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DetachCustomerManagedPolicyReferenceFromPermissionSetResponse`
        """
        http_info = self._detach_customer_managed_policy_reference_from_permission_set_http_info(request)
        return self._call_api(**http_info)

    def detach_customer_managed_policy_reference_from_permission_set_invoker(self, request):
        http_info = self._detach_customer_managed_policy_reference_from_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _detach_customer_managed_policy_reference_from_permission_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/detach-customer-managed-policy",
            "request_type": request.__class__.__name__,
            "response_type": "DetachCustomerManagedPolicyReferenceFromPermissionSetResponse"
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

    def detach_managed_policy_from_permission_set(self, request):
        """将附加的系统策略从指定的权限集中分离

        将附加的系统策略从指定的权限集中分离
        
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

    def list_accounts_for_provisioned_permission_set(self, request):
        """列出权限集关联的账户

        查询与指定权限集关联的账户列表
        
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

    def list_customer_managed_policy_references_in_permission_set(self, request):
        """获取附加到指定权限集的所有客户自定义策略列表

        获取附加到指定权限集的所有客户自定义策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomerManagedPolicyReferencesInPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListCustomerManagedPolicyReferencesInPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListCustomerManagedPolicyReferencesInPermissionSetResponse`
        """
        http_info = self._list_customer_managed_policy_references_in_permission_set_http_info(request)
        return self._call_api(**http_info)

    def list_customer_managed_policy_references_in_permission_set_invoker(self, request):
        http_info = self._list_customer_managed_policy_references_in_permission_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_customer_managed_policy_references_in_permission_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/instances/{instance_id}/permission-sets/{permission_set_id}/customer-managed-policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomerManagedPolicyReferencesInPermissionSetResponse"
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
        """列出权限集中附加的系统管理策略

        列出权限集中附加的系统管理策略
        
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
        """列出权限集预分配状态

        查询指定实例中的权限集预分配状态列表
        
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
        """列出指定实例的权限集列表

        列出指定实例的权限集列表
        
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
        """列出分配给指定帐户的权限集列表

        列出分配给指定帐户的权限集列表
        
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

    def update_permission_set(self, request):
        """更新权限集

        根据权限集ID，删除指定权限集的属性
        
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

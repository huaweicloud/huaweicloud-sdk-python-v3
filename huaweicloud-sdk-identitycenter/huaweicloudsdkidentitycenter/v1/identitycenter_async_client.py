# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class IdentityCenterAsyncClient(Client):
    def __init__(self):
        super(IdentityCenterAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkidentitycenter.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "IdentityCenterClient":
            raise TypeError("client type error, support client type is IdentityCenterClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def create_account_assignment_async(self, request):
        """创建帐户分配

        使用指定的权限集为指定帐户分配对应主体的访问权限，主体可为IdentityCenter用户或IdentityCenter用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAccountAssignment
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreateAccountAssignmentResponse`
        """
        return self._create_account_assignment_with_http_info(request)

    def _create_account_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/instances/{instance_id}/account-assignments/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAccountAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_account_assignment_async(self, request):
        """使用指定的权限集从指定帐户删除主体的访问权限

        使用指定的权限集从指定帐户删除主体的访问权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAccountAssignment
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeleteAccountAssignmentRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeleteAccountAssignmentResponse`
        """
        return self._delete_account_assignment_with_http_info(request)

    def _delete_account_assignment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/instances/{instance_id}/account-assignments/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAccountAssignmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def describe_account_assignment_creation_status_async(self, request):
        """查询账号分配请求的状态

        根据请求ID，查询指定IAM Identity Center实例下的帐户分配创建状态详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribeAccountAssignmentCreationStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentCreationStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentCreationStatusResponse`
        """
        return self._describe_account_assignment_creation_status_with_http_info(request)

    def _describe_account_assignment_creation_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/account-assignments/creation-status/{request_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DescribeAccountAssignmentCreationStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def describe_account_assignment_deletion_status_async(self, request):
        """查询账户分配删除状态详情

        根据请求ID，查询指定IAM Identity Center实例下的帐户分配删除状态详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribeAccountAssignmentDeletionStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentDeletionStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribeAccountAssignmentDeletionStatusResponse`
        """
        return self._describe_account_assignment_deletion_status_with_http_info(request)

    def _describe_account_assignment_deletion_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/account-assignments/deletion-status/{request_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DescribeAccountAssignmentDeletionStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_account_assignment_creation_status_async(self, request):
        """列出账户分配创建状态

        查询指定IAM Identity Center实例下的帐户分配的创建状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccountAssignmentCreationStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentCreationStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentCreationStatusResponse`
        """
        return self._list_account_assignment_creation_status_with_http_info(request)

    def _list_account_assignment_creation_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/account-assignments/creation-statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccountAssignmentCreationStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_account_assignment_deletion_status_async(self, request):
        """列出账户分配删除状态

        查询指定IAM Identity Center实例下的帐户分配的删除状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccountAssignmentDeletionStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentDeletionStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentDeletionStatusResponse`
        """
        return self._list_account_assignment_deletion_status_with_http_info(request)

    def _list_account_assignment_deletion_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/account-assignments/deletion-statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccountAssignmentDeletionStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_account_assignments_async(self, request):
        """列出与指定权限集以及指定帐户关联的用户/用户组

        列出与指定权限集以及指定帐户关联的用户/用户组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccountAssignments
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountAssignmentsResponse`
        """
        return self._list_account_assignments_with_http_info(request)

    def _list_account_assignments_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/account-assignments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccountAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_profile_associations_async(self, request):
        """查询profile关联的用户或组列表

        查询profile关联的用户或组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProfileAssociations
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListProfileAssociationsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListProfileAssociationsResponse`
        """
        return self._list_profile_associations_with_http_info(request)

    def _list_profile_associations_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/profile-associations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProfileAssociationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_async(self, request):
        """查询实例列表

        查询 IAM Identity Center的资源实例列表.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListInstancesResponse`
        """
        return self._list_instances_with_http_info(request)

    def _list_instances_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_customer_managed_policy_to_permission_set_async(self, request):
        """将指定的客户自定义管理策略附加到指定的权限集

        将指定的客户自定义管理策略附加到指定的权限集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachCustomerManagedPolicyToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.AttachCustomerManagedPolicyToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AttachCustomerManagedPolicyToPermissionSetResponse`
        """
        return self._attach_customer_managed_policy_to_permission_set_with_http_info(request)

    def _attach_customer_managed_policy_to_permission_set_with_http_info(self, request):
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
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/attach-customer-managed-policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachCustomerManagedPolicyToPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_managed_policy_to_permission_set_async(self, request):
        """将系统管理策略附加到权限集

        将系统管理策略附加到权限集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachManagedPolicyToPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.AttachManagedPolicyToPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.AttachManagedPolicyToPermissionSetResponse`
        """
        return self._attach_managed_policy_to_permission_set_with_http_info(request)

    def _attach_managed_policy_to_permission_set_with_http_info(self, request):
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
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/attach-managed-policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachManagedPolicyToPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_permission_set_async(self, request):
        """在指定的IAM Identity Center实例中创建权限集

        在指定的IAM Identity Center实例中创建一个权限集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.CreatePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.CreatePermissionSetResponse`
        """
        return self._create_permission_set_with_http_info(request)

    def _create_permission_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v1/instances/{instance_id}/permission-sets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_permission_set_async(self, request):
        """删除指定实例的权限集

        删除指定实例的权限集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DeletePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DeletePermissionSetResponse`
        """
        return self._delete_permission_set_with_http_info(request)

    def _delete_permission_set_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def describe_permission_set_async(self, request):
        """查询权限集详情

        根据权限集ID，查询指定权限集的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetResponse`
        """
        return self._describe_permission_set_with_http_info(request)

    def _describe_permission_set_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DescribePermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def describe_permission_set_provisioning_status_async(self, request):
        """查询权限集预分配状态详情

        根据请求Id，查询权限集预分配状态的详情信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DescribePermissionSetProvisioningStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetProvisioningStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DescribePermissionSetProvisioningStatusResponse`
        """
        return self._describe_permission_set_provisioning_status_with_http_info(request)

    def _describe_permission_set_provisioning_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/provisioning-status/{request_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DescribePermissionSetProvisioningStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_customer_managed_policy_reference_from_permission_set_async(self, request):
        """将附加的客户自定义管理策略从指定的权限集中分离

        将附加的客户自定义管理策略从指定的权限集中分离
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachCustomerManagedPolicyReferenceFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DetachCustomerManagedPolicyReferenceFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DetachCustomerManagedPolicyReferenceFromPermissionSetResponse`
        """
        return self._detach_customer_managed_policy_reference_from_permission_set_with_http_info(request)

    def _detach_customer_managed_policy_reference_from_permission_set_with_http_info(self, request):
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
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/detach-customer-managed-policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachCustomerManagedPolicyReferenceFromPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_managed_policy_from_permission_set_async(self, request):
        """将附加的系统策略从指定的权限集中分离

        将附加的系统策略从指定的权限集中分离
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachManagedPolicyFromPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.DetachManagedPolicyFromPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DetachManagedPolicyFromPermissionSetResponse`
        """
        return self._detach_managed_policy_from_permission_set_with_http_info(request)

    def _detach_managed_policy_from_permission_set_with_http_info(self, request):
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
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/detach-managed-policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachManagedPolicyFromPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_accounts_for_provisioned_permission_set_async(self, request):
        """列出权限集关联的账户

        查询与指定权限集关联的账户列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAccountsForProvisionedPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListAccountsForProvisionedPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListAccountsForProvisionedPermissionSetResponse`
        """
        return self._list_accounts_for_provisioned_permission_set_with_http_info(request)

    def _list_accounts_for_provisioned_permission_set_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/accounts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAccountsForProvisionedPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_customer_managed_policy_references_in_permission_set_async(self, request):
        """获取附加到指定权限集的所有客户自定义策略列表

        获取附加到指定权限集的所有客户自定义策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomerManagedPolicyReferencesInPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListCustomerManagedPolicyReferencesInPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListCustomerManagedPolicyReferencesInPermissionSetResponse`
        """
        return self._list_customer_managed_policy_references_in_permission_set_with_http_info(request)

    def _list_customer_managed_policy_references_in_permission_set_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/customer-managed-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCustomerManagedPolicyReferencesInPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_managed_policies_in_permission_set_async(self, request):
        """列出权限集中附加的系统管理策略

        列出权限集中附加的系统管理策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListManagedPoliciesInPermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListManagedPoliciesInPermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListManagedPoliciesInPermissionSetResponse`
        """
        return self._list_managed_policies_in_permission_set_with_http_info(request)

    def _list_managed_policies_in_permission_set_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}/managed-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListManagedPoliciesInPermissionSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permission_set_provisioning_status_async(self, request):
        """列出权限集预分配状态

        查询指定实例中的权限集预分配状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermissionSetProvisioningStatus
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetProvisioningStatusRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetProvisioningStatusResponse`
        """
        return self._list_permission_set_provisioning_status_with_http_info(request)

    def _list_permission_set_provisioning_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/provisioning-statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPermissionSetProvisioningStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permission_sets_async(self, request):
        """列出指定实例的权限集列表

        列出指定实例的权限集列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermissionSets
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsResponse`
        """
        return self._list_permission_sets_with_http_info(request)

    def _list_permission_sets_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPermissionSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permission_sets_provisioned_to_account_async(self, request):
        """列出分配给指定帐户的权限集列表

        列出分配给指定帐户的权限集列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermissionSetsProvisionedToAccount
        :type request: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsProvisionedToAccountRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ListPermissionSetsProvisionedToAccountResponse`
        """
        return self._list_permission_sets_provisioned_to_account_with_http_info(request)

    def _list_permission_sets_provisioned_to_account_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['AccessKeyAuth']

        return self.call_api(
            resource_path='/v1/instances/{instance_id}/permission-sets/provisioned-to-accounts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPermissionSetsProvisionedToAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_permission_set_async(self, request):
        """更新权限集

        根据权限集ID，删除指定权限集的属性
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePermissionSet
        :type request: :class:`huaweicloudsdkidentitycenter.v1.UpdatePermissionSetRequest`
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.UpdatePermissionSetResponse`
        """
        return self._update_permission_set_with_http_info(request)

    def _update_permission_set_with_http_info(self, request):
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
            resource_path='/v1/instances/{instance_id}/permission-sets/{permission_set_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePermissionSetResponse',
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

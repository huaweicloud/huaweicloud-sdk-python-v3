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
        """创建账号分配

        使用指定的权限集为指定账号分配对应主体的访问权限，主体可为IAM身份中心用户或用户组。
        
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
        """删除账号分配

        使用指定的权限集从指定的账号删除主体的访问权限，主体可为IAM身份中心用户或用户组。
        
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
        """查询账号分配创建状态详情

        根据请求ID，查询指定IAM身份中心实例下的账号分配创建状态详情信息。
        
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
        """查询账号分配删除状态详情

        根据请求ID，查询指定IAM身份中心实例下的账号分配删除状态详情信息。
        
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

    def list_account_assignment_creation_status(self, request):
        """列出账号分配创建状态

        查询指定IAM身份中心实例下的账号分配的创建状态列表。
        
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
        """列出账号分配删除状态

        查询指定IAM身份中心实例下的账号分配的删除状态列表。
        
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
        """列出账号和权限集关联的用户或用户组

        列出与指定账号以及指定权限集关联的用户或用户组。
        
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

    def list_instances(self, request):
        """列出实例

        查询IAM身份中心的实例列表。
        
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

    def create_instance_access_control_attribute_configuration(self, request):
        """启用指定实例的访问控制功能

        启用指定实例的访问控制功能。
        
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
        """解除指定实例的访问控制属性配置

        禁用指定IAM身份中心实例的基于属性的访问控制（ABAC）功能，并删除已配置的所有属性映射。
        
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
        """获取指定实例的访问控制属性配置

        返回已配置为与指定IAM身份中心实例的基于属性的访问控制（ABAC）一起使用的IAM身份中心身份源属性列表。
        
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
        """更新指定实例的访问控制属性配置

        更新可与IAM身份中心实例一起使用的IAM身份中心身份源属性，以进行基于属性的访问控制（ABAC）。
        
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

    def attach_managed_policy_to_permission_set(self, request):
        """添加系统身份策略

        在指定的权限集中添加系统身份策略。
        
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

    def create_permission_set(self, request):
        """创建权限集

        在指定的IAM身份中心实例中创建一个权限集。
        
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
        """删除自定义身份策略

        删除指定权限集中的自定义身份策略。
        
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
        """删除指定权限集中的自定义策略

        删除指定权限集中的自定义策略
        
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
        """删除权限集

        根据权限集ID，删除指定的权限集。
        
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
        """查询权限集详情

        根据权限集ID，查询指定权限集的详情信息。
        
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
        """查询权限集预分配状态详情

        根据请求ID，查询权限集预分配状态的详情信息。
        
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
        """删除系统身份策略

        删除指定权限集中的系统身份策略。
        
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

    def get_custom_policy_for_permission_set(self, request):
        """查询自定义身份策略详情

        查询指定权限集中的自定义身份策略详情。
        
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
        """获取分配给权限集的自定义策略

        获取分配给权限集的自定义策略
        
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

    def list_accounts_for_provisioned_permission_set(self, request):
        """列出权限集关联的账号

        查询与指定权限集关联的账号列表。
        
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
        """列出系统身份策略

        获取添加到指定权限集中的系统身份策略列表。
        
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

    def list_permission_set_provisioning_status(self, request):
        """列出权限集预分配状态

        查询指定实例中的权限集预分配状态列表。
        
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
        """列出权限集

        查询指定实例下的权限集列表。
        
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
        """列出分配给账号的权限集

        查询分配给指定账号的权限集列表。
        
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
        """预分配权限集

        将指定权限集预分配给指定账号。
        
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
        """添加自定义身份策略

        在指定的权限集中添加自定义身份策略。
        
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
        """将自定义策略附加到权限集

        将自定义策略附加到权限集
        
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
        """更新权限集

        根据权限集ID，更新指定权限集的属性。
        
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
        """为指定资源添加标签

        给指定的资源添加一个或多个标签。当前支持为权限集添加标签。
        
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
        """删除指定资源的指定标签

        从指定资源中删除指定的标签。
        
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
        """列出绑定到指定资源的标签

        列出绑定到指定资源的标签。当前支持为权限集添加标签。
        
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

    def attach_managed_role_to_permission_set(self, request):
        """添加系统策略

        在指定的权限集中添加系统策略。
        
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

    def detach_managed_role_from_permission_set(self, request):
        """删除系统策略

        删除指定权限集中的系统策略。
        
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

    def list_managed_roles_in_permission_set(self, request):
        """列出系统策略

        获取添加到指定权限集中的系统策略列表。
        
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

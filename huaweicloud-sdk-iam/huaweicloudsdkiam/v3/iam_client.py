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


class IamClient(Client):
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
        super(IamClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiam.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials,BasicCredentials,IamCredentials")

        if clazz.__name__ != "IamClient":
            raise TypeError("client type error, support client type is IamClient")

        return ClientBuilder(clazz, "GlobalCredentials,BasicCredentials,IamCredentials")

    def associate_agency_with_all_projects_permission(self, request):
        """为委托授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateAgencyWithAllProjectsPermission
        :type request: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithAllProjectsPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithAllProjectsPermissionResponse`
        """
        return self.associate_agency_with_all_projects_permission_with_http_info(request)

    def associate_agency_with_all_projects_permission_with_http_info(self, request):
        all_params = ['agency_id', 'domain_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateAgencyWithAllProjectsPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_agency_with_domain_permission(self, request):
        """为委托授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateAgencyWithDomainPermission
        :type request: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithDomainPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithDomainPermissionResponse`
        """
        return self.associate_agency_with_domain_permission_with_http_info(request)

    def associate_agency_with_domain_permission_with_http_info(self, request):
        all_params = ['domain_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateAgencyWithDomainPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_agency_with_project_permission(self, request):
        """为委托授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateAgencyWithProjectPermission
        :type request: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithProjectPermissionResponse`
        """
        return self.associate_agency_with_project_permission_with_http_info(request)

    def associate_agency_with_project_permission_with_http_info(self, request):
        all_params = ['project_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateAgencyWithProjectPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_role_to_group_on_enterprise_project(self, request):
        """基于用户组为企业项目授权

        该接口用于基于用户组为企业项目授权。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateRoleToGroupOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.AssociateRoleToGroupOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateRoleToGroupOnEnterpriseProjectResponse`
        """
        return self.associate_role_to_group_on_enterprise_project_with_http_info(request)

    def associate_role_to_group_on_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups/{group_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateRoleToGroupOnEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_role_to_user_on_enterprise_project(self, request):
        """基于用户为企业项目授权

        基于用户为企业项目授权。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateRoleToUserOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.AssociateRoleToUserOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateRoleToUserOnEnterpriseProjectResponse`
        """
        return self.associate_role_to_user_on_enterprise_project_with_http_info(request)

    def associate_role_to_user_on_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'user_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users/{user_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateRoleToUserOnEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_all_projects_permission_for_agency(self, request):
        """检查委托下是否具有所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)检查委托是否具有所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckAllProjectsPermissionForAgency
        :type request: :class:`huaweicloudsdkiam.v3.CheckAllProjectsPermissionForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CheckAllProjectsPermissionForAgencyResponse`
        """
        return self.check_all_projects_permission_for_agency_with_http_info(request)

    def check_all_projects_permission_for_agency_with_http_info(self, request):
        all_params = ['agency_id', 'domain_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckAllProjectsPermissionForAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_domain_permission_for_agency(self, request):
        """查询委托是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDomainPermissionForAgency
        :type request: :class:`huaweicloudsdkiam.v3.CheckDomainPermissionForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CheckDomainPermissionForAgencyResponse`
        """
        return self.check_domain_permission_for_agency_with_http_info(request)

    def check_domain_permission_for_agency_with_http_info(self, request):
        all_params = ['domain_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckDomainPermissionForAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_project_permission_for_agency(self, request):
        """查询委托是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckProjectPermissionForAgency
        :type request: :class:`huaweicloudsdkiam.v3.CheckProjectPermissionForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CheckProjectPermissionForAgencyResponse`
        """
        return self.check_project_permission_for_agency_with_http_info(request)

    def check_project_permission_for_agency_with_http_info(self, request):
        all_params = ['project_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckProjectPermissionForAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_agency(self, request):
        """创建委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdkiam.v3.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateAgencyResponse`
        """
        return self.create_agency_with_http_info(request)

    def create_agency_with_http_info(self, request):
        all_params = ['create_agency_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_agency_custom_policy(self, request):
        """创建委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgencyCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.CreateAgencyCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateAgencyCustomPolicyResponse`
        """
        return self.create_agency_custom_policy_with_http_info(request)

    def create_agency_custom_policy_with_http_info(self, request):
        all_params = ['create_agency_custom_policy_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAgencyCustomPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cloud_service_custom_policy(self, request):
        """创建云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建云服务自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCloudServiceCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.CreateCloudServiceCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateCloudServiceCustomPolicyResponse`
        """
        return self.create_cloud_service_custom_policy_with_http_info(request)

    def create_cloud_service_custom_policy_with_http_info(self, request):
        all_params = ['create_cloud_service_custom_policy_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCloudServiceCustomPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_login_token(self, request):
        """获取自定义代理登录票据

        该接口用于用于获取自定义代理登录票据logintoken。logintoken是系统颁发给自定义代理用户的登录票据，承载用户的身份、session等信息。调用自定义代理URL登录云服务控制台时，可以使用本接口获取的logintoken进行认证。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        &gt; - logintoken的有效期为10分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLoginToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateLoginTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateLoginTokenResponse`
        """
        return self.create_login_token_with_http_info(request)

    def create_login_token_with_http_info(self, request):
        all_params = ['create_login_token_request_body']
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

        response_headers = ["X-Subject-LoginToken", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AUTH/securitytoken/logintokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLoginTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_metadata(self, request):
        """导入Metadata文件

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)导入Metadata文件。
        
        账号在使用联邦认证功能前，需要先将Metadata文件导入到IAM中。Metadata文件是SAML 2.0协议约定的接口文件，包含访问接口地址和证书信息，请找企业管理员获取企业IdP的Metadata文件。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMetadata
        :type request: :class:`huaweicloudsdkiam.v3.CreateMetadataRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateMetadataResponse`
        """
        return self.create_metadata_with_http_info(request)

    def create_metadata_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id', 'create_metadata_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3-ext/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}/metadata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_open_id_connect_config(self, request):
        """创建OpenId Connect身份提供商配置

        创建OpenId Connect身份提供商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOpenIdConnectConfig
        :type request: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigResponse`
        """
        return self.create_open_id_connect_config_with_http_info(request)

    def create_open_id_connect_config_with_http_info(self, request):
        all_params = ['idp_id', 'create_open_id_connect_config_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-FEDERATION/identity-providers/{idp_id}/openid-connect-config',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOpenIdConnectConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_token_with_id_token(self, request):
        """获取联邦认证token(OpenId Connect Id token方式)

        获取联邦认证token(OpenId Connect Id token方式)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTokenWithIdToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateTokenWithIdTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateTokenWithIdTokenResponse`
        """
        return self.create_token_with_id_token_with_http_info(request)

    def create_token_with_id_token_with_http_info(self, request):
        all_params = ['x_idp_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_idp_id' in local_var_params:
            header_params['X-Idp-Id'] = local_var_params['x_idp_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AUTH/id-token/tokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTokenWithIdTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_unscoped_token_with_id_token(self, request):
        """获取联邦认证unscoped token(OpenId Connect Id token方式)

        获取联邦认证token(OpenId Connect Id token方式)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUnscopedTokenWithIdToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateUnscopedTokenWithIdTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateUnscopedTokenWithIdTokenResponse`
        """
        return self.create_unscoped_token_with_id_token_with_http_info(request)

    def create_unscoped_token_with_id_token_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id', 'authorization']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

        query_params = []

        header_params = {}
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}/auth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateUnscopedTokenWithIdTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_agency(self, request):
        """删除委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除委托。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAgency
        :type request: :class:`huaweicloudsdkiam.v3.DeleteAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteAgencyResponse`
        """
        return self.delete_agency_with_http_info(request)

    def delete_agency_with_http_info(self, request):
        all_params = ['agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies/{agency_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_custom_policy(self, request):
        """删除自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.DeleteCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteCustomPolicyResponse`
        """
        return self.delete_custom_policy_with_http_info(request)

    def delete_custom_policy_with_http_info(self, request):
        all_params = ['role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCustomPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_domain_group_inherited_role(self, request):
        """移除用户组的所有项目服务权限

        该接口可以用于移除用户组的所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainGroupInheritedRole
        :type request: :class:`huaweicloudsdkiam.v3.DeleteDomainGroupInheritedRoleRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteDomainGroupInheritedRoleResponse`
        """
        return self.delete_domain_group_inherited_role_with_http_info(request)

    def delete_domain_group_inherited_role_with_http_info(self, request):
        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDomainGroupInheritedRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_add_user_to_group(self, request):
        """添加IAM用户到用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)添加IAM用户到用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneAddUserToGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneAddUserToGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneAddUserToGroupResponse`
        """
        return self.keystone_add_user_to_group_with_http_info(request)

    def keystone_add_user_to_group_with_http_info(self, request):
        all_params = ['group_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneAddUserToGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_associate_group_with_domain_permission(self, request):
        """为用户组授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneAssociateGroupWithDomainPermission
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithDomainPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithDomainPermissionResponse`
        """
        return self.keystone_associate_group_with_domain_permission_with_http_info(request)

    def keystone_associate_group_with_domain_permission_with_http_info(self, request):
        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneAssociateGroupWithDomainPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_associate_group_with_project_permission(self, request):
        """为用户组授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneAssociateGroupWithProjectPermission
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithProjectPermissionResponse`
        """
        return self.keystone_associate_group_with_project_permission_with_http_info(request)

    def keystone_associate_group_with_project_permission_with_http_info(self, request):
        all_params = ['project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneAssociateGroupWithProjectPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_check_domain_permission_for_group(self, request):
        """查询用户组是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCheckDomainPermissionForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckDomainPermissionForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckDomainPermissionForGroupResponse`
        """
        return self.keystone_check_domain_permission_for_group_with_http_info(request)

    def keystone_check_domain_permission_for_group_with_http_info(self, request):
        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCheckDomainPermissionForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_check_project_permission_for_group(self, request):
        """查询用户组是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCheckProjectPermissionForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckProjectPermissionForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckProjectPermissionForGroupResponse`
        """
        return self.keystone_check_project_permission_for_group_with_http_info(request)

    def keystone_check_project_permission_for_group_with_http_info(self, request):
        all_params = ['project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCheckProjectPermissionForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_check_user_in_group(self, request):
        """查询IAM用户是否在用户组中

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户是否在用户组中。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCheckUserInGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckUserInGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckUserInGroupResponse`
        """
        return self.keystone_check_user_in_group_with_http_info(request)

    def keystone_check_user_in_group_with_http_info(self, request):
        all_params = ['group_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users/{user_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCheckUserInGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_checkrole_for_group(self, request):
        """查询用户组是否拥有所有项目指定权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有所有项目指定权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCheckroleForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckroleForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckroleForGroupResponse`
        """
        return self.keystone_checkrole_for_group_with_http_info(request)

    def keystone_checkrole_for_group_with_http_info(self, request):
        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCheckroleForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_group(self, request):
        """创建用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateGroupResponse`
        """
        return self.keystone_create_group_with_http_info(request)

    def keystone_create_group_with_http_info(self, request):
        all_params = ['keystone_create_group_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_identity_provider(self, request):
        """注册身份提供商

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册身份提供商。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateIdentityProviderResponse`
        """
        return self.keystone_create_identity_provider_with_http_info(request)

    def keystone_create_identity_provider_with_http_info(self, request):
        all_params = ['id', 'keystone_create_identity_provider_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateIdentityProviderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_mapping(self, request):
        """注册映射

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册映射。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingResponse`
        """
        return self.keystone_create_mapping_with_http_info(request)

    def keystone_create_mapping_with_http_info(self, request):
        all_params = ['id', 'keystone_create_mapping_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/mappings/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_project(self, request):
        """创建项目

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建项目。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateProject
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateProjectResponse`
        """
        return self.keystone_create_project_with_http_info(request)

    def keystone_create_project_with_http_info(self, request):
        all_params = ['keystone_create_project_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_protocol(self, request):
        """注册协议

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册协议（将协议关联到某一身份提供商）。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateProtocolResponse`
        """
        return self.keystone_create_protocol_with_http_info(request)

    def keystone_create_protocol_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id', 'keystone_create_protocol_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateProtocolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_scoped_token(self, request):
        """获取联邦认证scoped token

        该接口可以用于通过联邦认证方式获取scoped token。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateScopedToken
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateScopedTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateScopedTokenResponse`
        """
        return self.keystone_create_scoped_token_with_http_info(request)

    def keystone_create_scoped_token_with_http_info(self, request):
        all_params = ['keystone_create_scoped_token_request_body']
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

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/tokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateScopedTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_delete_group(self, request):
        """删除用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneDeleteGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteGroupResponse`
        """
        return self.keystone_delete_group_with_http_info(request)

    def keystone_delete_group_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneDeleteGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_delete_identity_provider(self, request):
        """删除身份提供商

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) 删除身份提供商。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneDeleteIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteIdentityProviderResponse`
        """
        return self.keystone_delete_identity_provider_with_http_info(request)

    def keystone_delete_identity_provider_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneDeleteIdentityProviderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_delete_mapping(self, request):
        """删除映射

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除映射。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneDeleteMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteMappingResponse`
        """
        return self.keystone_delete_mapping_with_http_info(request)

    def keystone_delete_mapping_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/mappings/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneDeleteMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_delete_protocol(self, request):
        """删除协议

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除协议。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneDeleteProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteProtocolResponse`
        """
        return self.keystone_delete_protocol_with_http_info(request)

    def keystone_delete_protocol_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneDeleteProtocolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_all_project_permissions_for_group(self, request):
        """查询用户组的所有项目权限列表

        该接口可以用于管理员查询用户组所有项目服务权限列表。 该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListAllProjectPermissionsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListAllProjectPermissionsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListAllProjectPermissionsForGroupResponse`
        """
        return self.keystone_list_all_project_permissions_for_group_with_http_info(request)

    def keystone_list_all_project_permissions_for_group_with_http_info(self, request):
        all_params = ['domain_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/inherited_to_projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListAllProjectPermissionsForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_auth_domains(self, request):
        """查询IAM用户可以访问的账号详情

        该接口可以用于查询IAM用户可以用访问的账号详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListAuthDomains
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListAuthDomainsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListAuthDomainsResponse`
        """
        return self.keystone_list_auth_domains_with_http_info(request)

    def keystone_list_auth_domains_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListAuthDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_auth_projects(self, request):
        """查询IAM用户可以访问的项目列表

        该接口可以用于查询IAM用户可以访问的项目列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListAuthProjects
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListAuthProjectsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListAuthProjectsResponse`
        """
        return self.keystone_list_auth_projects_with_http_info(request)

    def keystone_list_auth_projects_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListAuthProjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_domain_permissions_for_group(self, request):
        """查询全局服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的用户组权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListDomainPermissionsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListDomainPermissionsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListDomainPermissionsForGroupResponse`
        """
        return self.keystone_list_domain_permissions_for_group_with_http_info(request)

    def keystone_list_domain_permissions_for_group_with_http_info(self, request):
        all_params = ['domain_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListDomainPermissionsForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_endpoints(self, request):
        """查询终端节点列表

        该接口可以用于查询终端节点列表。终端节点用来提供服务访问入口。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListEndpoints
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListEndpointsResponse`
        """
        return self.keystone_list_endpoints_with_http_info(request)

    def keystone_list_endpoints_with_http_info(self, request):
        all_params = ['interface', 'service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'interface' in local_var_params:
            query_params.append(('interface', local_var_params['interface']))
        if 'service_id' in local_var_params:
            query_params.append(('service_id', local_var_params['service_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/endpoints',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListEndpointsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_federation_domains(self, request):
        """查询联邦用户可以访问的账号列表

        该接口用于查询联邦用户可以访问的账号列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        &gt; - 推荐使用[查询IAM用户可以访问的账号详情](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;IAM&amp;api&#x3D;KeystoneQueryAccessibleDomainDetailsToUser)，该接口可以返回相同的响应格式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListFederationDomains
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListFederationDomainsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListFederationDomainsResponse`
        """
        return self.keystone_list_federation_domains_with_http_info(request)

    def keystone_list_federation_domains_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListFederationDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_groups(self, request):
        """查询用户组列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListGroups
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsResponse`
        """
        return self.keystone_list_groups_with_http_info(request)

    def keystone_list_groups_with_http_info(self, request):
        all_params = ['domain_id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_identity_providers(self, request):
        """查询身份提供商列表

        该接口可以用于查询身份提供商列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListIdentityProviders
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListIdentityProvidersRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListIdentityProvidersResponse`
        """
        return self.keystone_list_identity_providers_with_http_info(request)

    def keystone_list_identity_providers_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListIdentityProvidersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_mappings(self, request):
        """查询映射列表

        该接口可以用于查询映射列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListMappings
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListMappingsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListMappingsResponse`
        """
        return self.keystone_list_mappings_with_http_info(request)

    def keystone_list_mappings_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/mappings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListMappingsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_permissions(self, request):
        """查询权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListPermissions
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListPermissionsResponse`
        """
        return self.keystone_list_permissions_with_http_info(request)

    def keystone_list_permissions_with_http_info(self, request):
        all_params = ['name', 'domain_id', 'page', 'per_page', 'permission_type', 'display_name', 'type', 'catalog']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'permission_type' in local_var_params:
            query_params.append(('permission_type', local_var_params['permission_type']))
        if 'display_name' in local_var_params:
            query_params.append(('display_name', local_var_params['display_name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'catalog' in local_var_params:
            query_params.append(('catalog', local_var_params['catalog']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListPermissionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_project_permissions_for_group(self, request):
        """查询项目服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的用户组权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListProjectPermissionsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProjectPermissionsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProjectPermissionsForGroupResponse`
        """
        return self.keystone_list_project_permissions_for_group_with_http_info(request)

    def keystone_list_project_permissions_for_group_with_http_info(self, request):
        all_params = ['project_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListProjectPermissionsForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_projects(self, request):
        """查询指定条件下的项目列表

        该接口可以用于查询指定条件下的项目列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListProjects
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsResponse`
        """
        return self.keystone_list_projects_with_http_info(request)

    def keystone_list_projects_with_http_info(self, request):
        all_params = ['domain_id', 'name', 'parent_id', 'enabled', 'is_domain', 'page', 'per_page']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'is_domain' in local_var_params:
            query_params.append(('is_domain', local_var_params['is_domain']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListProjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_projects_for_user(self, request):
        """查询指定IAM用户的项目列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的项目列表，或IAM用户查询自己的项目列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListProjectsForUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsForUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsForUserResponse`
        """
        return self.keystone_list_projects_for_user_with_http_info(request)

    def keystone_list_projects_for_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListProjectsForUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_protocols(self, request):
        """查询协议列表

        该接口可以用于查询协议列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListProtocols
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProtocolsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProtocolsResponse`
        """
        return self.keystone_list_protocols_with_http_info(request)

    def keystone_list_protocols_with_http_info(self, request):
        all_params = ['idp_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListProtocolsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_regions(self, request):
        """查询区域列表

        该接口可以用于查询区域列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListRegions
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListRegionsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListRegionsResponse`
        """
        return self.keystone_list_regions_with_http_info(request)

    def keystone_list_regions_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListRegionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_services(self, request):
        """查询服务列表

        该接口可以用于查询服务列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListServices
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListServicesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListServicesResponse`
        """
        return self.keystone_list_services_with_http_info(request)

    def keystone_list_services_with_http_info(self, request):
        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListServicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_users_for_group_by_admin(self, request):
        """管理员查询用户组所包含的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组中所包含的IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListUsersForGroupByAdmin
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListUsersForGroupByAdminRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListUsersForGroupByAdminResponse`
        """
        return self.keystone_list_users_for_group_by_admin_with_http_info(request)

    def keystone_list_users_for_group_by_admin_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListUsersForGroupByAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_versions(self, request):
        """查询版本信息列表

        该接口用于查询Keystone API的版本信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListVersions
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListVersionsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListVersionsResponse`
        """
        return self.keystone_list_versions_with_http_info(request)

    def keystone_list_versions_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_remove_domain_permission_from_group(self, request):
        """移除用户组的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneRemoveDomainPermissionFromGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneRemoveDomainPermissionFromGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneRemoveDomainPermissionFromGroupResponse`
        """
        return self.keystone_remove_domain_permission_from_group_with_http_info(request)

    def keystone_remove_domain_permission_from_group_with_http_info(self, request):
        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneRemoveDomainPermissionFromGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_remove_project_permission_from_group(self, request):
        """移除用户组的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneRemoveProjectPermissionFromGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneRemoveProjectPermissionFromGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneRemoveProjectPermissionFromGroupResponse`
        """
        return self.keystone_remove_project_permission_from_group_with_http_info(request)

    def keystone_remove_project_permission_from_group_with_http_info(self, request):
        all_params = ['project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneRemoveProjectPermissionFromGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_remove_user_from_group(self, request):
        """移除用户组中的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组中的IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneRemoveUserFromGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneRemoveUserFromGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneRemoveUserFromGroupResponse`
        """
        return self.keystone_remove_user_from_group_with_http_info(request)

    def keystone_remove_user_from_group_with_http_info(self, request):
        all_params = ['group_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneRemoveUserFromGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_catalog(self, request):
        """查询服务目录

        该接口可以用于查询请求头中X-Auth-Token对应的服务目录。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowCatalog
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowCatalogRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowCatalogResponse`
        """
        return self.keystone_show_catalog_with_http_info(request)

    def keystone_show_catalog_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/catalog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowCatalogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_endpoint(self, request):
        """查询终端节点详情

        该接口可以用于查询终端节点详情。终端节点用来提供服务访问入口。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowEndpoint
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowEndpointRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowEndpointResponse`
        """
        return self.keystone_show_endpoint_with_http_info(request)

    def keystone_show_endpoint_with_http_info(self, request):
        all_params = ['endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/endpoints/{endpoint_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowEndpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_group(self, request):
        """查询用户组详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowGroupResponse`
        """
        return self.keystone_show_group_with_http_info(request)

    def keystone_show_group_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_identity_provider(self, request):
        """查询身份提供商详情

        该接口可以用于查询身份提供商详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowIdentityProviderResponse`
        """
        return self.keystone_show_identity_provider_with_http_info(request)

    def keystone_show_identity_provider_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowIdentityProviderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_mapping(self, request):
        """查询映射详情

        该接口可以用于查询映射详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowMappingResponse`
        """
        return self.keystone_show_mapping_with_http_info(request)

    def keystone_show_mapping_with_http_info(self, request):
        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/mappings/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_permission(self, request):
        """查询权限详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowPermission
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowPermissionResponse`
        """
        return self.keystone_show_permission_with_http_info(request)

    def keystone_show_permission_with_http_info(self, request):
        all_params = ['role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/roles/{role_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowPermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_project(self, request):
        """查询项目详情

        该接口可以用于查询项目详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowProject
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowProjectResponse`
        """
        return self.keystone_show_project_with_http_info(request)

    def keystone_show_project_with_http_info(self, request):
        all_params = ['project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_protocol(self, request):
        """查询协议详情

        该接口可以用于查询协议详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowProtocolResponse`
        """
        return self.keystone_show_protocol_with_http_info(request)

    def keystone_show_protocol_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowProtocolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_region(self, request):
        """查询区域详情

        该接口可以用于查询区域详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowRegion
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowRegionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowRegionResponse`
        """
        return self.keystone_show_region_with_http_info(request)

    def keystone_show_region_with_http_info(self, request):
        all_params = ['region_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/regions/{region_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowRegionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_security_compliance(self, request):
        """查询账号密码强度策略

        该接口可以用于查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowSecurityCompliance
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceResponse`
        """
        return self.keystone_show_security_compliance_with_http_info(request)

    def keystone_show_security_compliance_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/config/security_compliance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowSecurityComplianceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_security_compliance_by_option(self, request):
        """按条件查询账号密码强度策略

        该接口可以用于按条件查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowSecurityComplianceByOption
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceByOptionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceByOptionResponse`
        """
        return self.keystone_show_security_compliance_by_option_with_http_info(request)

    def keystone_show_security_compliance_by_option_with_http_info(self, request):
        all_params = ['domain_id', 'option']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'option' in local_var_params:
            path_params['option'] = local_var_params['option']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/config/security_compliance/{option}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowSecurityComplianceByOptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_service(self, request):
        """查询服务详情

        该接口可以用于查询服务详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowService
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowServiceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowServiceResponse`
        """
        return self.keystone_show_service_with_http_info(request)

    def keystone_show_service_with_http_info(self, request):
        all_params = ['service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/services/{service_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowServiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_version(self, request):
        """查询版本信息

        该接口用于查询Keystone API的3.0版本的信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowVersion
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowVersionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowVersionResponse`
        """
        return self.keystone_show_version_with_http_info(request)

    def keystone_show_version_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_group(self, request):
        """更新用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新用户组信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateGroupResponse`
        """
        return self.keystone_update_group_with_http_info(request)

    def keystone_update_group_with_http_info(self, request):
        all_params = ['group_id', 'keystone_update_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_identity_provider(self, request):
        """更新身份提供商

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新身份提供商。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateIdentityProviderResponse`
        """
        return self.keystone_update_identity_provider_with_http_info(request)

    def keystone_update_identity_provider_with_http_info(self, request):
        all_params = ['id', 'keystone_update_identity_provider_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateIdentityProviderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_mapping(self, request):
        """更新映射

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新映射。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateMappingResponse`
        """
        return self.keystone_update_mapping_with_http_info(request)

    def keystone_update_mapping_with_http_info(self, request):
        all_params = ['id', 'keystone_update_mapping_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/mappings/{id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_project(self, request):
        """修改项目信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改项目信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateProject
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProjectResponse`
        """
        return self.keystone_update_project_with_http_info(request)

    def keystone_update_project_with_http_info(self, request):
        all_params = ['project_id', 'keystone_update_project_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_protocol(self, request):
        """更新协议

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新协议。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProtocolResponse`
        """
        return self.keystone_update_protocol_with_http_info(request)

    def keystone_update_protocol_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id', 'keystone_update_protocol_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateProtocolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_agencies(self, request):
        """查询指定条件下的委托列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkiam.v3.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListAgenciesResponse`
        """
        return self.list_agencies_with_http_info(request)

    def list_agencies_with_http_info(self, request):
        all_params = ['domain_id', 'trust_domain_id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'trust_domain_id' in local_var_params:
            query_params.append(('trust_domain_id', local_var_params['trust_domain_id']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAgenciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_projects_permissions_for_agency(self, request):
        """查询委托下的所有项目服务权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托所有项目服务权限列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllProjectsPermissionsForAgency
        :type request: :class:`huaweicloudsdkiam.v3.ListAllProjectsPermissionsForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListAllProjectsPermissionsForAgencyResponse`
        """
        return self.list_all_projects_permissions_for_agency_with_http_info(request)

    def list_all_projects_permissions_for_agency_with_http_info(self, request):
        all_params = ['agency_id', 'domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/inherited_to_projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllProjectsPermissionsForAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_custom_policies(self, request):
        """查询自定义策略列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCustomPolicies
        :type request: :class:`huaweicloudsdkiam.v3.ListCustomPoliciesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListCustomPoliciesResponse`
        """
        return self.list_custom_policies_with_http_info(request)

    def list_custom_policies_with_http_info(self, request):
        all_params = ['page', 'per_page']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCustomPoliciesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_permissions_for_agency(self, request):
        """查询全局服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的委托权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainPermissionsForAgency
        :type request: :class:`huaweicloudsdkiam.v3.ListDomainPermissionsForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListDomainPermissionsForAgencyResponse`
        """
        return self.list_domain_permissions_for_agency_with_http_info(request)

    def list_domain_permissions_for_agency_with_http_info(self, request):
        all_params = ['domain_id', 'agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainPermissionsForAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_enterprise_projects_for_group(self, request):
        """查询用户组关联的企业项目

        该接口可用于查询用户组所关联的企业项目。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseProjectsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForGroupResponse`
        """
        return self.list_enterprise_projects_for_group_with_http_info(request)

    def list_enterprise_projects_for_group_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/groups/{group_id}/enterprise-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnterpriseProjectsForGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_enterprise_projects_for_user(self, request):
        """查询用户关联的企业项目

        该接口可用于查询用户所关联的企业项目。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseProjectsForUser
        :type request: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForUserResponse`
        """
        return self.list_enterprise_projects_for_user_with_http_info(request)

    def list_enterprise_projects_for_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/users/{user_id}/enterprise-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnterpriseProjectsForUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_groups_for_enterprise_project(self, request):
        """查询企业项目关联的用户组

        该接口可用于查询企业项目关联的用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroupsForEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListGroupsForEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListGroupsForEnterpriseProjectResponse`
        """
        return self.list_groups_for_enterprise_project_with_http_info(request)

    def list_groups_for_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGroupsForEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_permissions_for_agency(self, request):
        """查询项目服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的委托权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectPermissionsForAgency
        :type request: :class:`huaweicloudsdkiam.v3.ListProjectPermissionsForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListProjectPermissionsForAgencyResponse`
        """
        return self.list_project_permissions_for_agency_with_http_info(request)

    def list_project_permissions_for_agency_with_http_info(self, request):
        all_params = ['project_id', 'agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectPermissionsForAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_roles_for_group_on_enterprise_project(self, request):
        """查询企业项目已关联用户组的权限

        该接口可用于查询企业项目已关联用户组的权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRolesForGroupOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListRolesForGroupOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListRolesForGroupOnEnterpriseProjectResponse`
        """
        return self.list_roles_for_group_on_enterprise_project_with_http_info(request)

    def list_roles_for_group_on_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups/{group_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRolesForGroupOnEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_roles_for_user_on_enterprise_project(self, request):
        """查询企业项目直接关联用户的权限

        该接口可用于查询企业项目直接关联用户的权限。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRolesForUserOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListRolesForUserOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListRolesForUserOnEnterpriseProjectResponse`
        """
        return self.list_roles_for_user_on_enterprise_project_with_http_info(request)

    def list_roles_for_user_on_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users/{user_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRolesForUserOnEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_users_for_enterprise_project(self, request):
        """查询企业项目直接关联用户

        该接口可用于查询企业项目直接关联的用户。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUsersForEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListUsersForEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListUsersForEnterpriseProjectResponse`
        """
        return self.list_users_for_enterprise_project_with_http_info(request)

    def list_users_for_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUsersForEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_all_projects_permission_from_agency(self, request):
        """移除委托下的所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveAllProjectsPermissionFromAgency
        :type request: :class:`huaweicloudsdkiam.v3.RemoveAllProjectsPermissionFromAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RemoveAllProjectsPermissionFromAgencyResponse`
        """
        return self.remove_all_projects_permission_from_agency_with_http_info(request)

    def remove_all_projects_permission_from_agency_with_http_info(self, request):
        all_params = ['agency_id', 'domain_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveAllProjectsPermissionFromAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_domain_permission_from_agency(self, request):
        """移除委托的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveDomainPermissionFromAgency
        :type request: :class:`huaweicloudsdkiam.v3.RemoveDomainPermissionFromAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RemoveDomainPermissionFromAgencyResponse`
        """
        return self.remove_domain_permission_from_agency_with_http_info(request)

    def remove_domain_permission_from_agency_with_http_info(self, request):
        all_params = ['domain_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveDomainPermissionFromAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_project_permission_from_agency(self, request):
        """移除委托的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveProjectPermissionFromAgency
        :type request: :class:`huaweicloudsdkiam.v3.RemoveProjectPermissionFromAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RemoveProjectPermissionFromAgencyResponse`
        """
        return self.remove_project_permission_from_agency_with_http_info(request)

    def remove_project_permission_from_agency_with_http_info(self, request):
        all_params = ['project_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveProjectPermissionFromAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def revoke_role_from_group_on_enterprise_project(self, request):
        """删除企业项目关联用户组的权限

        该接口用于删除企业项目关联用户组的权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeRoleFromGroupOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.RevokeRoleFromGroupOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RevokeRoleFromGroupOnEnterpriseProjectResponse`
        """
        return self.revoke_role_from_group_on_enterprise_project_with_http_info(request)

    def revoke_role_from_group_on_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups/{group_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RevokeRoleFromGroupOnEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def revoke_role_from_user_on_enterprise_project(self, request):
        """删除企业项目直接关联用户的权限

        删除企业项目直接关联用户的权限。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeRoleFromUserOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.RevokeRoleFromUserOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RevokeRoleFromUserOnEnterpriseProjectResponse`
        """
        return self.revoke_role_from_user_on_enterprise_project_with_http_info(request)

    def revoke_role_from_user_on_enterprise_project_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'user_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users/{user_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RevokeRoleFromUserOnEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_agency(self, request):
        """查询委托详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdkiam.v3.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowAgencyResponse`
        """
        return self.show_agency_with_http_info(request)

    def show_agency_with_http_info(self, request):
        all_params = ['agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies/{agency_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_custom_policy(self, request):
        """查询自定义策略详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowCustomPolicyResponse`
        """
        return self.show_custom_policy_with_http_info(request)

    def show_custom_policy_with_http_info(self, request):
        all_params = ['role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles/{role_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCustomPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_api_acl_policy(self, request):
        """查询账号接口访问策略

        该接口可以用于查询账号接口访问控制策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainApiAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainApiAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainApiAclPolicyResponse`
        """
        return self.show_domain_api_acl_policy_with_http_info(request)

    def show_domain_api_acl_policy_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/api-acl-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainApiAclPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_console_acl_policy(self, request):
        """查询账号控制台访问策略

        该接口可以用于查询账号控制台访问控制策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainConsoleAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainConsoleAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainConsoleAclPolicyResponse`
        """
        return self.show_domain_console_acl_policy_with_http_info(request)

    def show_domain_console_acl_policy_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/console-acl-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainConsoleAclPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_login_policy(self, request):
        """查询账号登录策略

        该接口可以用于查询账号登录策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainLoginPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainLoginPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainLoginPolicyResponse`
        """
        return self.show_domain_login_policy_with_http_info(request)

    def show_domain_login_policy_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/login-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainLoginPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_password_policy(self, request):
        """查询账号密码策略

        该接口可以用于查询账号密码策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainPasswordPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainPasswordPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainPasswordPolicyResponse`
        """
        return self.show_domain_password_policy_with_http_info(request)

    def show_domain_password_policy_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/password-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainPasswordPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_protect_policy(self, request):
        """查询账号操作保护策略

        该接口可以用于查询账号操作保护策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainProtectPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainProtectPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainProtectPolicyResponse`
        """
        return self.show_domain_protect_policy_with_http_info(request)

    def show_domain_protect_policy_with_http_info(self, request):
        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/protect-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainProtectPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_quota(self, request):
        """查询账号配额

        该接口可以用于查询账号配额。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainQuota
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainQuotaRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainQuotaResponse`
        """
        return self.show_domain_quota_with_http_info(request)

    def show_domain_quota_with_http_info(self, request):
        all_params = ['domain_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-QUOTA/domains/{domain_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_role_assignments(self, request):
        """查询指定账号中的授权记录

        该接口用于查询指定账号中的授权记录。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainRoleAssignments
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainRoleAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainRoleAssignmentsResponse`
        """
        return self.show_domain_role_assignments_with_http_info(request)

    def show_domain_role_assignments_with_http_info(self, request):
        all_params = ['domain_id', 'role_id', 'subject', 'subject_user_id', 'subject_group_id', 'subject_agency_id', 'scope', 'scope_project_id', 'scope_domain_id', 'scope_enterprise_projects_id', 'is_inherited', 'include_group', 'page', 'per_page']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'role_id' in local_var_params:
            query_params.append(('role_id', local_var_params['role_id']))
        if 'subject' in local_var_params:
            query_params.append(('subject', local_var_params['subject']))
        if 'subject_user_id' in local_var_params:
            query_params.append(('subject.user_id', local_var_params['subject_user_id']))
        if 'subject_group_id' in local_var_params:
            query_params.append(('subject.group_id', local_var_params['subject_group_id']))
        if 'subject_agency_id' in local_var_params:
            query_params.append(('subject.agency_id', local_var_params['subject_agency_id']))
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'scope_project_id' in local_var_params:
            query_params.append(('scope.project_id', local_var_params['scope_project_id']))
        if 'scope_domain_id' in local_var_params:
            query_params.append(('scope.domain_id', local_var_params['scope_domain_id']))
        if 'scope_enterprise_projects_id' in local_var_params:
            query_params.append(('scope.enterprise_projects_id', local_var_params['scope_enterprise_projects_id']))
        if 'is_inherited' in local_var_params:
            query_params.append(('is_inherited', local_var_params['is_inherited']))
        if 'include_group' in local_var_params:
            query_params.append(('include_group', local_var_params['include_group']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-PERMISSION/role-assignments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainRoleAssignmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_metadata(self, request):
        """查询Metadata文件

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询身份提供商导入到IAM中的Metadata文件。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetadata
        :type request: :class:`huaweicloudsdkiam.v3.ShowMetadataRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowMetadataResponse`
        """
        return self.show_metadata_with_http_info(request)

    def show_metadata_with_http_info(self, request):
        all_params = ['idp_id', 'protocol_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']
        if 'protocol_id' in local_var_params:
            path_params['protocol_id'] = local_var_params['protocol_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3-ext/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}/metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMetadataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_open_id_connect_config(self, request):
        """查询OpenId Connect身份提供商配置

        查询OpenId Connect身份提供商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOpenIdConnectConfig
        :type request: :class:`huaweicloudsdkiam.v3.ShowOpenIdConnectConfigRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowOpenIdConnectConfigResponse`
        """
        return self.show_open_id_connect_config_with_http_info(request)

    def show_open_id_connect_config_with_http_info(self, request):
        all_params = ['idp_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-FEDERATION/identity-providers/{idp_id}/openid-connect-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOpenIdConnectConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_details_and_status(self, request):
        """查询项目详情与状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目详情与状态。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectDetailsAndStatus
        :type request: :class:`huaweicloudsdkiam.v3.ShowProjectDetailsAndStatusRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowProjectDetailsAndStatusResponse`
        """
        return self.show_project_details_and_status_with_http_info(request)

    def show_project_details_and_status_with_http_info(self, request):
        all_params = ['project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3-ext/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectDetailsAndStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_quota(self, request):
        """查询项目配额

        该接口可以用于查询项目配额。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectQuota
        :type request: :class:`huaweicloudsdkiam.v3.ShowProjectQuotaRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowProjectQuotaResponse`
        """
        return self.show_project_quota_with_http_info(request)

    def show_project_quota_with_http_info(self, request):
        all_params = ['project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-QUOTA/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_agency(self, request):
        """修改委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgency
        :type request: :class:`huaweicloudsdkiam.v3.UpdateAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateAgencyResponse`
        """
        return self.update_agency_with_http_info(request)

    def update_agency_with_http_info(self, request):
        all_params = ['agency_id', 'update_agency_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies/{agency_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_agency_custom_policy(self, request):
        """修改委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgencyCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateAgencyCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateAgencyCustomPolicyResponse`
        """
        return self.update_agency_custom_policy_with_http_info(request)

    def update_agency_custom_policy_with_http_info(self, request):
        all_params = ['role_id', 'update_agency_custom_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles/{role_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAgencyCustomPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_cloud_service_custom_policy(self, request):
        """修改云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改云服务自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCloudServiceCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateCloudServiceCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateCloudServiceCustomPolicyResponse`
        """
        return self.update_cloud_service_custom_policy_with_http_info(request)

    def update_cloud_service_custom_policy_with_http_info(self, request):
        all_params = ['role_id', 'update_cloud_service_custom_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles/{role_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCloudServiceCustomPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_api_acl_policy(self, request):
        """修改账号接口访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号接口访问策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainApiAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainApiAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainApiAclPolicyResponse`
        """
        return self.update_domain_api_acl_policy_with_http_info(request)

    def update_domain_api_acl_policy_with_http_info(self, request):
        all_params = ['domain_id', 'update_domain_api_acl_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/api-acl-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainApiAclPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_console_acl_policy(self, request):
        """修改账号控制台访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号控制台访问策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainConsoleAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainConsoleAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainConsoleAclPolicyResponse`
        """
        return self.update_domain_console_acl_policy_with_http_info(request)

    def update_domain_console_acl_policy_with_http_info(self, request):
        all_params = ['domain_id', 'update_domain_console_acl_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/console-acl-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainConsoleAclPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_group_inherit_role(self, request):
        """为用户组授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainGroupInheritRole
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainGroupInheritRoleRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainGroupInheritRoleResponse`
        """
        return self.update_domain_group_inherit_role_with_http_info(request)

    def update_domain_group_inherit_role_with_http_info(self, request):
        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainGroupInheritRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_login_policy(self, request):
        """修改账号登录策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号登录策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainLoginPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainLoginPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainLoginPolicyResponse`
        """
        return self.update_domain_login_policy_with_http_info(request)

    def update_domain_login_policy_with_http_info(self, request):
        all_params = ['domain_id', 'update_domain_login_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/login-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainLoginPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_password_policy(self, request):
        """修改账号密码策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号密码策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainPasswordPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainPasswordPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainPasswordPolicyResponse`
        """
        return self.update_domain_password_policy_with_http_info(request)

    def update_domain_password_policy_with_http_info(self, request):
        all_params = ['domain_id', 'update_domain_password_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/password-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainPasswordPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_domain_protect_policy(self, request):
        """修改账号操作保护策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainProtectPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainProtectPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainProtectPolicyResponse`
        """
        return self.update_domain_protect_policy_with_http_info(request)

    def update_domain_protect_policy_with_http_info(self, request):
        all_params = ['domain_id', 'update_domain_protect_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/protect-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDomainProtectPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_open_id_connect_config(self, request):
        """修改OpenId Connect身份提供商配置

        修改OpenId Connect身份提供商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateOpenIdConnectConfig
        :type request: :class:`huaweicloudsdkiam.v3.UpdateOpenIdConnectConfigRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateOpenIdConnectConfigResponse`
        """
        return self.update_open_id_connect_config_with_http_info(request)

    def update_open_id_connect_config_with_http_info(self, request):
        all_params = ['idp_id', 'update_open_id_connect_config_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-FEDERATION/identity-providers/{idp_id}/openid-connect-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateOpenIdConnectConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project_status(self, request):
        """设置项目状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)设置项目状态。项目状态包括：正常、冻结。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectStatus
        :type request: :class:`huaweicloudsdkiam.v3.UpdateProjectStatusRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateProjectStatusResponse`
        """
        return self.update_project_status_with_http_info(request)

    def update_project_status_with_http_info(self, request):
        all_params = ['project_id', 'update_project_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3-ext/projects/{project_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProjectStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_permanent_access_key(self, request):
        """创建永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)给IAM用户创建永久访问密钥，或IAM用户给自己创建永久访问密钥。
        
        访问密钥（Access Key ID/Secret Access Key，简称AK/SK），是您通过开发工具（API、CLI、SDK）访问华为云时的身份凭证，不用于登录控制台。系统通过AK识别访问用户的身份，通过SK进行签名验证，通过加密签名验证可以确保请求的机密性、完整性和请求者身份的正确性。在控制台创建访问密钥的方式请参见：[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html) 。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.CreatePermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreatePermanentAccessKeyResponse`
        """
        return self.create_permanent_access_key_with_http_info(request)

    def create_permanent_access_key_with_http_info(self, request):
        all_params = ['create_permanent_access_key_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePermanentAccessKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_temporary_access_key_by_agency(self, request):
        """通过委托获取临时访问密钥

        该接口可以用于通过委托来获取临时访问密钥（临时AK/SK）和securitytoken。
        
        临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html) 。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemporaryAccessKeyByAgency
        :type request: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByAgencyResponse`
        """
        return self.create_temporary_access_key_by_agency_with_http_info(request)

    def create_temporary_access_key_by_agency_with_http_info(self, request):
        all_params = ['create_temporary_access_key_by_agency_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/securitytokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTemporaryAccessKeyByAgencyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_temporary_access_key_by_token(self, request):
        """通过token获取临时访问密钥

        该接口可以用于通过token来获取临时AK/SK和securitytoken。
        
        临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html)。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemporaryAccessKeyByToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByTokenResponse`
        """
        return self.create_temporary_access_key_by_token_with_http_info(request)

    def create_temporary_access_key_by_token_with_http_info(self, request):
        all_params = ['create_temporary_access_key_by_token_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/securitytokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTemporaryAccessKeyByTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_permanent_access_key(self, request):
        """删除指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除IAM用户的指定永久访问密钥，或IAM用户删除自己的指定永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.DeletePermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeletePermanentAccessKeyResponse`
        """
        return self.delete_permanent_access_key_with_http_info(request)

    def delete_permanent_access_key_with_http_info(self, request):
        all_params = ['access_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key' in local_var_params:
            path_params['access_key'] = local_var_params['access_key']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials/{access_key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePermanentAccessKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_permanent_access_keys(self, request):
        """查询所有永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的所有永久访问密钥，或IAM用户查询自己的所有永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPermanentAccessKeys
        :type request: :class:`huaweicloudsdkiam.v3.ListPermanentAccessKeysRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListPermanentAccessKeysResponse`
        """
        return self.list_permanent_access_keys_with_http_info(request)

    def list_permanent_access_keys_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPermanentAccessKeysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_permanent_access_key(self, request):
        """查询指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的指定永久访问密钥，或IAM用户查询自己的指定永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.ShowPermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowPermanentAccessKeyResponse`
        """
        return self.show_permanent_access_key_with_http_info(request)

    def show_permanent_access_key_with_http_info(self, request):
        all_params = ['access_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key' in local_var_params:
            path_params['access_key'] = local_var_params['access_key']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials/{access_key}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPermanentAccessKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_permanent_access_key(self, request):
        """修改指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户的指定永久访问密钥，或IAM用户修改自己的指定永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyResponse`
        """
        return self.update_permanent_access_key_with_http_info(request)

    def update_permanent_access_key_with_http_info(self, request):
        all_params = ['access_key', 'update_permanent_access_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key' in local_var_params:
            path_params['access_key'] = local_var_params['access_key']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials/{access_key}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePermanentAccessKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_binding_device(self, request):
        """绑定MFA设备

        该接口可以用于绑定MFA设备。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBindingDevice
        :type request: :class:`huaweicloudsdkiam.v3.CreateBindingDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateBindingDeviceResponse`
        """
        return self.create_binding_device_with_http_info(request)

    def create_binding_device_with_http_info(self, request):
        all_params = ['create_binding_device_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/mfa-devices/bind',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBindingDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_mfa_device(self, request):
        """创建MFA设备

        该接口可以用于创建MFA设备。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMfaDevice
        :type request: :class:`huaweicloudsdkiam.v3.CreateMfaDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateMfaDeviceResponse`
        """
        return self.create_mfa_device_with_http_info(request)

    def create_mfa_device_with_http_info(self, request):
        all_params = ['create_mfa_device_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/virtual-mfa-devices',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateMfaDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_user(self, request):
        """管理员创建IAM用户（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkiam.v3.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateUserResponse`
        """
        return self.create_user_with_http_info(request)

    def create_user_with_http_info(self, request):
        all_params = ['create_user_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_binding_device(self, request):
        """解绑MFA设备

        该接口可以用于解绑MFA设备
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBindingDevice
        :type request: :class:`huaweicloudsdkiam.v3.DeleteBindingDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteBindingDeviceResponse`
        """
        return self.delete_binding_device_with_http_info(request)

    def delete_binding_device_with_http_info(self, request):
        all_params = ['delete_binding_device_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/mfa-devices/unbind',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBindingDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_mfa_device(self, request):
        """删除MFA设备

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除MFA设备。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMfaDevice
        :type request: :class:`huaweicloudsdkiam.v3.DeleteMfaDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteMfaDeviceResponse`
        """
        return self.delete_mfa_device_with_http_info(request)

    def delete_mfa_device_with_http_info(self, request):
        all_params = ['user_id', 'serial_number']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'serial_number' in local_var_params:
            query_params.append(('serial_number', local_var_params['serial_number']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/virtual-mfa-devices',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMfaDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_user(self, request):
        """管理员创建IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。IAM用户首次登录时需要修改密码。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserResponse`
        """
        return self.keystone_create_user_with_http_info(request)

    def keystone_create_user_with_http_info(self, request):
        all_params = ['keystone_create_user_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_delete_user(self, request):
        """管理员删除IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除指定IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneDeleteUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteUserResponse`
        """
        return self.keystone_delete_user_with_http_info(request)

    def keystone_delete_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneDeleteUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_groups_for_user(self, request):
        """查询IAM用户所属用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户所属用户组，或IAM用户查询自己所属用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListGroupsForUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsForUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsForUserResponse`
        """
        return self.keystone_list_groups_for_user_with_http_info(request)

    def keystone_list_groups_for_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListGroupsForUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_list_users(self, request):
        """管理员查询IAM用户列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneListUsers
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListUsersRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListUsersResponse`
        """
        return self.keystone_list_users_with_http_info(request)

    def keystone_list_users_with_http_info(self, request):
        all_params = ['domain_id', 'enabled', 'name', 'password_expires_at']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'password_expires_at' in local_var_params:
            query_params.append(('password_expires_at', local_var_params['password_expires_at']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneListUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_show_user(self, request):
        """查询IAM用户详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的用户详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneShowUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowUserResponse`
        """
        return self.keystone_show_user_with_http_info(request)

    def keystone_show_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneShowUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_user_by_admin(self, request):
        """管理员修改IAM用户信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateUserByAdmin
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserByAdminRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserByAdminResponse`
        """
        return self.keystone_update_user_by_admin_with_http_info(request)

    def keystone_update_user_by_admin_with_http_info(self, request):
        all_params = ['user_id', 'keystone_update_user_by_admin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateUserByAdminResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_update_user_password(self, request):
        """修改IAM用户密码

        该接口可以用于IAM用户修改自己的密码。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneUpdateUserPassword
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserPasswordResponse`
        """
        return self.keystone_update_user_password_with_http_info(request)

    def keystone_update_user_password_with_http_info(self, request):
        all_params = ['user_id', 'keystone_update_user_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneUpdateUserPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_login_protects(self, request):
        """查询IAM用户的登录保护状态信息列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的登录保护状态列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserLoginProtects
        :type request: :class:`huaweicloudsdkiam.v3.ListUserLoginProtectsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListUserLoginProtectsResponse`
        """
        return self.list_user_login_protects_with_http_info(request)

    def list_user_login_protects_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/login-protects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserLoginProtectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_mfa_devices(self, request):
        """该接口可以用于获取MFA设备。

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的MFA绑定信息列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserMfaDevices
        :type request: :class:`huaweicloudsdkiam.v3.ListUserMfaDevicesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListUserMfaDevicesResponse`
        """
        return self.list_user_mfa_devices_with_http_info(request)

    def list_user_mfa_devices_with_http_info(self, request):
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

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/virtual-mfa-devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserMfaDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user(self, request):
        """查询IAM用户详情（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkiam.v3.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowUserResponse`
        """
        return self.show_user_with_http_info(request)

    def show_user_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_login_protect(self, request):
        """查询指定IAM用户的登录保护状态信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的登录保护状态信息，或IAM用户查询自己的登录保护状态信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserLoginProtect
        :type request: :class:`huaweicloudsdkiam.v3.ShowUserLoginProtectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowUserLoginProtectResponse`
        """
        return self.show_user_login_protect_with_http_info(request)

    def show_user_login_protect_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}/login-protect',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserLoginProtectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_mfa_device(self, request):
        """查询指定IAM用户的MFA绑定信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的MFA绑定信息，或IAM用户查询自己的MFA绑定信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserMfaDevice
        :type request: :class:`huaweicloudsdkiam.v3.ShowUserMfaDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowUserMfaDeviceResponse`
        """
        return self.show_user_mfa_device_with_http_info(request)

    def show_user_mfa_device_with_http_info(self, request):
        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/users/{user_id}/virtual-mfa-device',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserMfaDeviceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_login_protect(self, request):
        """修改IAM用户登录保护状态信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLoginProtect
        :type request: :class:`huaweicloudsdkiam.v3.UpdateLoginProtectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateLoginProtectResponse`
        """
        return self.update_login_protect_with_http_info(request)

    def update_login_protect_with_http_info(self, request):
        all_params = ['user_id', 'update_login_protect_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}/login-protect',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateLoginProtectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user(self, request):
        """管理员修改IAM用户信息（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息 。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkiam.v3.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateUserResponse`
        """
        return self.update_user_with_http_info(request)

    def update_user_with_http_info(self, request):
        all_params = ['user_id', 'update_user_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_information(self, request):
        """修改IAM用户信息（推荐）

        该接口可以用于IAM用户修改自己的用户信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserInformation
        :type request: :class:`huaweicloudsdkiam.v3.UpdateUserInformationRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateUserInformationResponse`
        """
        return self.update_user_information_with_http_info(request)

    def update_user_information_with_http_info(self, request):
        all_params = ['user_id', 'update_user_information_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}/info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserInformationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_agency_token(self, request):
        """获取委托Token

        该接口可以用于获取委托方的token。
        
        例如：A账号希望B账号管理自己的某些资源，所以A账号创建了委托给B账号，则A账号为委托方，B账号为被委托方。那么B账号可以通过该接口获取委托token。B账号仅能使用该token管理A账号的委托资源，不能管理自己账号中的资源。如果B账号需要管理自己账号中的资源，则需要获取自己的用户token。
        
        token是系统颁发给用户的访问令牌，承载用户的身份、权限等信息。调用IAM以及其他云服务的接口时，可以使用本接口获取的token进行鉴权。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。如果使用全局区域的Endpoint调用，该token可以在所有区域使用；如果使用非全局区域的Endpoint调用，则该token仅在该区域生效，不能跨区域使用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        &gt; - token的有效期为24小时，建议进行缓存，避免频繁调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateAgencyToken
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateAgencyTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateAgencyTokenResponse`
        """
        return self.keystone_create_agency_token_with_http_info(request)

    def keystone_create_agency_token_with_http_info(self, request):
        all_params = ['keystone_create_agency_token_request_body', 'nocatalog']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/tokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateAgencyTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_user_token_by_password(self, request):
        """获取IAM用户Token（使用密码）

        该接口可以用于通过用户名/密码的方式进行认证来获取IAM用户token。
        
        token是系统颁发给IAM用户的访问令牌，承载用户的身份、权限等信息。调用IAM以及其他云服务的接口时，可以使用本接口获取的IAM用户token进行鉴权。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。如果使用全局区域的Endpoint调用，该token可以在所有区域使用；如果使用非全局区域的Endpoint调用，则该token仅在该区域生效，不能跨区域使用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        &gt; - token的有效期为24小时，建议进行缓存，避免频繁调用。
        &gt; - 通过Postman获取用户token示例请参见：[如何通过Postman获取用户token](https://support.huaweicloud.com/iam_faq/iam_01_034.html)。
        &gt; - 如果需要获取具有Security Administrator权限的token，请参见：[IAM 常见问题](https://support.huaweicloud.com/iam_faq/iam_01_0608.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateUserTokenByPassword
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserTokenByPasswordRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserTokenByPasswordResponse`
        """
        return self.keystone_create_user_token_by_password_with_http_info(request)

    def keystone_create_user_token_by_password_with_http_info(self, request):
        all_params = ['keystone_create_user_token_by_password_request_body', 'nocatalog']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/tokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateUserTokenByPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_create_user_token_by_password_and_mfa(self, request):
        """获取IAM用户Token（使用密码+虚拟MFA）

        该接口可以用于通过用户名/密码+虚拟MFA的方式进行认证，在IAM用户开启了的登录保护功能，并选择通过虚拟MFA验证时获取IAM用户token。
        
        token是系统颁发给用户的访问令牌，承载用户的身份、权限等信息。调用IAM以及其他云服务的接口时，可以使用本接口获取的token进行鉴权。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。如果使用全局区域的Endpoint调用，该token可以在所有区域使用；如果使用非全局区域的Endpoint调用，则该token仅在该区域生效，不能跨区域使用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        &gt; - token的有效期为24小时，建议进行缓存，避免频繁调用。
        &gt; - 通过Postman获取用户token示例请参见：[如何通过Postman获取用户token](https://support.huaweicloud.com/iam_faq/iam_01_034.html)。
        &gt; - 如果需要获取具有Security Administrator权限的token，请参见：[IAM 常见问题](https://support.huaweicloud.com/iam_faq/iam_01_0608.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneCreateUserTokenByPasswordAndMfa
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserTokenByPasswordAndMfaRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserTokenByPasswordAndMfaResponse`
        """
        return self.keystone_create_user_token_by_password_and_mfa_with_http_info(request)

    def keystone_create_user_token_by_password_and_mfa_with_http_info(self, request):
        all_params = ['keystone_create_user_token_by_password_and_mfa_request_body', 'nocatalog']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/tokens',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneCreateUserTokenByPasswordAndMfaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def keystone_validate_token(self, request):
        """校验Token的有效性

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)校验本账号中IAM用户token的有效性，或IAM用户校验自己token的有效性。管理员仅能校验本账号中IAM用户token的有效性，不能校验其他账号中IAM用户token的有效性。如果被校验的token有效，则返回该token的详细信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for KeystoneValidateToken
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneValidateTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneValidateTokenResponse`
        """
        return self.keystone_validate_token_with_http_info(request)

    def keystone_validate_token_with_http_info(self, request):
        all_params = ['x_subject_token', 'nocatalog']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}
        if 'x_subject_token' in local_var_params:
            header_params['X-Subject-Token'] = local_var_params['x_subject_token']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/tokens',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='KeystoneValidateTokenResponse',
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

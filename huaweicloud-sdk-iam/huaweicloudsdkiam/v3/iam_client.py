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
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz, "GlobalCredentials,BasicCredentials")

    def associate_agency_with_all_projects_permission(self, request):
        """为委托授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param AssociateAgencyWithAllProjectsPermissionRequest request
        :return: AssociateAgencyWithAllProjectsPermissionResponse
        """
        return self.associate_agency_with_all_projects_permission_with_http_info(request)

    def associate_agency_with_all_projects_permission_with_http_info(self, request):
        """为委托授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param AssociateAgencyWithAllProjectsPermissionRequest request
        :return: AssociateAgencyWithAllProjectsPermissionResponse
        """

        all_params = ['agency_id', 'domain_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateAgencyWithAllProjectsPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def associate_agency_with_domain_permission(self, request):
        """为委托授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param AssociateAgencyWithDomainPermissionRequest request
        :return: AssociateAgencyWithDomainPermissionResponse
        """
        return self.associate_agency_with_domain_permission_with_http_info(request)

    def associate_agency_with_domain_permission_with_http_info(self, request):
        """为委托授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param AssociateAgencyWithDomainPermissionRequest request
        :return: AssociateAgencyWithDomainPermissionResponse
        """

        all_params = ['domain_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateAgencyWithDomainPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def associate_agency_with_project_permission(self, request):
        """为委托授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param AssociateAgencyWithProjectPermissionRequest request
        :return: AssociateAgencyWithProjectPermissionResponse
        """
        return self.associate_agency_with_project_permission_with_http_info(request)

    def associate_agency_with_project_permission_with_http_info(self, request):
        """为委托授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param AssociateAgencyWithProjectPermissionRequest request
        :return: AssociateAgencyWithProjectPermissionResponse
        """

        all_params = ['project_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AssociateAgencyWithProjectPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_all_projects_permission_for_agency(self, request):
        """检查委托下是否具有所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)检查委托是否具有所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CheckAllProjectsPermissionForAgencyRequest request
        :return: CheckAllProjectsPermissionForAgencyResponse
        """
        return self.check_all_projects_permission_for_agency_with_http_info(request)

    def check_all_projects_permission_for_agency_with_http_info(self, request):
        """检查委托下是否具有所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)检查委托是否具有所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CheckAllProjectsPermissionForAgencyRequest request
        :return: CheckAllProjectsPermissionForAgencyResponse
        """

        all_params = ['agency_id', 'domain_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckAllProjectsPermissionForAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_domain_permission_for_agency(self, request):
        """查询委托是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CheckDomainPermissionForAgencyRequest request
        :return: CheckDomainPermissionForAgencyResponse
        """
        return self.check_domain_permission_for_agency_with_http_info(request)

    def check_domain_permission_for_agency_with_http_info(self, request):
        """查询委托是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CheckDomainPermissionForAgencyRequest request
        :return: CheckDomainPermissionForAgencyResponse
        """

        all_params = ['domain_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckDomainPermissionForAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_project_permission_for_agency(self, request):
        """查询委托是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CheckProjectPermissionForAgencyRequest request
        :return: CheckProjectPermissionForAgencyResponse
        """
        return self.check_project_permission_for_agency_with_http_info(request)

    def check_project_permission_for_agency_with_http_info(self, request):
        """查询委托是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CheckProjectPermissionForAgencyRequest request
        :return: CheckProjectPermissionForAgencyResponse
        """

        all_params = ['project_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CheckProjectPermissionForAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_agency(self, request):
        """创建委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateAgencyRequest request
        :return: CreateAgencyResponse
        """
        return self.create_agency_with_http_info(request)

    def create_agency_with_http_info(self, request):
        """创建委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateAgencyRequest request
        :return: CreateAgencyResponse
        """

        all_params = ['create_agency_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_agency_custom_policy(self, request):
        """创建委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateAgencyCustomPolicyRequest request
        :return: CreateAgencyCustomPolicyResponse
        """
        return self.create_agency_custom_policy_with_http_info(request)

    def create_agency_custom_policy_with_http_info(self, request):
        """创建委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateAgencyCustomPolicyRequest request
        :return: CreateAgencyCustomPolicyResponse
        """

        all_params = ['create_agency_custom_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateAgencyCustomPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cloud_service_custom_policy(self, request):
        """创建云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建云服务自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateCloudServiceCustomPolicyRequest request
        :return: CreateCloudServiceCustomPolicyResponse
        """
        return self.create_cloud_service_custom_policy_with_http_info(request)

    def create_cloud_service_custom_policy_with_http_info(self, request):
        """创建云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建云服务自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateCloudServiceCustomPolicyRequest request
        :return: CreateCloudServiceCustomPolicyResponse
        """

        all_params = ['create_cloud_service_custom_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateCloudServiceCustomPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_agency(self, request):
        """删除委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除委托。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param DeleteAgencyRequest request
        :return: DeleteAgencyResponse
        """
        return self.delete_agency_with_http_info(request)

    def delete_agency_with_http_info(self, request):
        """删除委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除委托。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param DeleteAgencyRequest request
        :return: DeleteAgencyResponse
        """

        all_params = ['agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies/{agency_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_custom_policy(self, request):
        """删除自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param DeleteCustomPolicyRequest request
        :return: DeleteCustomPolicyResponse
        """
        return self.delete_custom_policy_with_http_info(request)

    def delete_custom_policy_with_http_info(self, request):
        """删除自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param DeleteCustomPolicyRequest request
        :return: DeleteCustomPolicyResponse
        """

        all_params = ['role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteCustomPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_add_user_to_group(self, request):
        """添加IAM用户到用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)添加IAM用户到用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAddUserToGroupRequest request
        :return: KeystoneAddUserToGroupResponse
        """
        return self.keystone_add_user_to_group_with_http_info(request)

    def keystone_add_user_to_group_with_http_info(self, request):
        """添加IAM用户到用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)添加IAM用户到用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAddUserToGroupRequest request
        :return: KeystoneAddUserToGroupResponse
        """

        all_params = ['group_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneAddUserToGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_associate_group_with_all_project_permission(self, request):
        """为用户组授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAssociateGroupWithAllProjectPermissionRequest request
        :return: KeystoneAssociateGroupWithAllProjectPermissionResponse
        """
        return self.keystone_associate_group_with_all_project_permission_with_http_info(request)

    def keystone_associate_group_with_all_project_permission_with_http_info(self, request):
        """为用户组授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAssociateGroupWithAllProjectPermissionRequest request
        :return: KeystoneAssociateGroupWithAllProjectPermissionResponse
        """

        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneAssociateGroupWithAllProjectPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_associate_group_with_domain_permission(self, request):
        """为用户组授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAssociateGroupWithDomainPermissionRequest request
        :return: KeystoneAssociateGroupWithDomainPermissionResponse
        """
        return self.keystone_associate_group_with_domain_permission_with_http_info(request)

    def keystone_associate_group_with_domain_permission_with_http_info(self, request):
        """为用户组授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAssociateGroupWithDomainPermissionRequest request
        :return: KeystoneAssociateGroupWithDomainPermissionResponse
        """

        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneAssociateGroupWithDomainPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_associate_group_with_project_permission(self, request):
        """为用户组授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAssociateGroupWithProjectPermissionRequest request
        :return: KeystoneAssociateGroupWithProjectPermissionResponse
        """
        return self.keystone_associate_group_with_project_permission_with_http_info(request)

    def keystone_associate_group_with_project_permission_with_http_info(self, request):
        """为用户组授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneAssociateGroupWithProjectPermissionRequest request
        :return: KeystoneAssociateGroupWithProjectPermissionResponse
        """

        all_params = ['project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneAssociateGroupWithProjectPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_check_domain_permission_for_group(self, request):
        """查询用户组是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCheckDomainPermissionForGroupRequest request
        :return: KeystoneCheckDomainPermissionForGroupResponse
        """
        return self.keystone_check_domain_permission_for_group_with_http_info(request)

    def keystone_check_domain_permission_for_group_with_http_info(self, request):
        """查询用户组是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCheckDomainPermissionForGroupRequest request
        :return: KeystoneCheckDomainPermissionForGroupResponse
        """

        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneCheckDomainPermissionForGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_check_project_permission_for_group(self, request):
        """查询用户组是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCheckProjectPermissionForGroupRequest request
        :return: KeystoneCheckProjectPermissionForGroupResponse
        """
        return self.keystone_check_project_permission_for_group_with_http_info(request)

    def keystone_check_project_permission_for_group_with_http_info(self, request):
        """查询用户组是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCheckProjectPermissionForGroupRequest request
        :return: KeystoneCheckProjectPermissionForGroupResponse
        """

        all_params = ['project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneCheckProjectPermissionForGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_check_user_in_group(self, request):
        """查询IAM用户是否在用户组中

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户是否在用户组中。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCheckUserInGroupRequest request
        :return: KeystoneCheckUserInGroupResponse
        """
        return self.keystone_check_user_in_group_with_http_info(request)

    def keystone_check_user_in_group_with_http_info(self, request):
        """查询IAM用户是否在用户组中

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户是否在用户组中。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCheckUserInGroupRequest request
        :return: KeystoneCheckUserInGroupResponse
        """

        all_params = ['group_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users/{user_id}',
            method='HEAD',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneCheckUserInGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_create_group(self, request):
        """创建用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCreateGroupRequest request
        :return: KeystoneCreateGroupResponse
        """
        return self.keystone_create_group_with_http_info(request)

    def keystone_create_group_with_http_info(self, request):
        """创建用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCreateGroupRequest request
        :return: KeystoneCreateGroupResponse
        """

        all_params = ['keystone_create_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneCreateGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_create_project(self, request):
        """创建项目

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建项目。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCreateProjectRequest request
        :return: KeystoneCreateProjectResponse
        """
        return self.keystone_create_project_with_http_info(request)

    def keystone_create_project_with_http_info(self, request):
        """创建项目

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建项目。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCreateProjectRequest request
        :return: KeystoneCreateProjectResponse
        """

        all_params = ['keystone_create_project_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneCreateProjectResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_delete_group(self, request):
        """删除用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneDeleteGroupRequest request
        :return: KeystoneDeleteGroupResponse
        """
        return self.keystone_delete_group_with_http_info(request)

    def keystone_delete_group_with_http_info(self, request):
        """删除用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneDeleteGroupRequest request
        :return: KeystoneDeleteGroupResponse
        """

        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneDeleteGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_auth_domains(self, request):
        """查询IAM用户可以访问的账号详情

        该接口可以用于查询IAM用户可以用访问的账号详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListAuthDomainsRequest request
        :return: KeystoneListAuthDomainsResponse
        """
        return self.keystone_list_auth_domains_with_http_info(request)

    def keystone_list_auth_domains_with_http_info(self, request):
        """查询IAM用户可以访问的账号详情

        该接口可以用于查询IAM用户可以用访问的账号详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListAuthDomainsRequest request
        :return: KeystoneListAuthDomainsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListAuthDomainsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_auth_projects(self, request):
        """查询IAM用户可以访问的项目列表

        该接口可以用于查询IAM用户可以访问的项目列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListAuthProjectsRequest request
        :return: KeystoneListAuthProjectsResponse
        """
        return self.keystone_list_auth_projects_with_http_info(request)

    def keystone_list_auth_projects_with_http_info(self, request):
        """查询IAM用户可以访问的项目列表

        该接口可以用于查询IAM用户可以访问的项目列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListAuthProjectsRequest request
        :return: KeystoneListAuthProjectsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListAuthProjectsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_domain_permissions_for_group(self, request):
        """查询全局服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的用户组权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListDomainPermissionsForGroupRequest request
        :return: KeystoneListDomainPermissionsForGroupResponse
        """
        return self.keystone_list_domain_permissions_for_group_with_http_info(request)

    def keystone_list_domain_permissions_for_group_with_http_info(self, request):
        """查询全局服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的用户组权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListDomainPermissionsForGroupRequest request
        :return: KeystoneListDomainPermissionsForGroupResponse
        """

        all_params = ['domain_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListDomainPermissionsForGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_endpoints(self, request):
        """查询终端节点列表

        该接口可以用于查询终端节点列表。终端节点用来提供服务访问入口。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListEndpointsRequest request
        :return: KeystoneListEndpointsResponse
        """
        return self.keystone_list_endpoints_with_http_info(request)

    def keystone_list_endpoints_with_http_info(self, request):
        """查询终端节点列表

        该接口可以用于查询终端节点列表。终端节点用来提供服务访问入口。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListEndpointsRequest request
        :return: KeystoneListEndpointsResponse
        """

        all_params = ['interface', 'service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/endpoints',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListEndpointsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_groups(self, request):
        """查询用户组列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListGroupsRequest request
        :return: KeystoneListGroupsResponse
        """
        return self.keystone_list_groups_with_http_info(request)

    def keystone_list_groups_with_http_info(self, request):
        """查询用户组列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListGroupsRequest request
        :return: KeystoneListGroupsResponse
        """

        all_params = ['domain_id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListGroupsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_permissions(self, request):
        """查询权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListPermissionsRequest request
        :return: KeystoneListPermissionsResponse
        """
        return self.keystone_list_permissions_with_http_info(request)

    def keystone_list_permissions_with_http_info(self, request):
        """查询权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListPermissionsRequest request
        :return: KeystoneListPermissionsResponse
        """

        all_params = ['name', 'domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListPermissionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_project_permissions_for_group(self, request):
        """查询项目服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的用户组权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListProjectPermissionsForGroupRequest request
        :return: KeystoneListProjectPermissionsForGroupResponse
        """
        return self.keystone_list_project_permissions_for_group_with_http_info(request)

    def keystone_list_project_permissions_for_group_with_http_info(self, request):
        """查询项目服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的用户组权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListProjectPermissionsForGroupRequest request
        :return: KeystoneListProjectPermissionsForGroupResponse
        """

        all_params = ['project_id', 'group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListProjectPermissionsForGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_projects(self, request):
        """查询指定条件下的项目列表

        该接口可以用于查询指定条件下的项目列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListProjectsRequest request
        :return: KeystoneListProjectsResponse
        """
        return self.keystone_list_projects_with_http_info(request)

    def keystone_list_projects_with_http_info(self, request):
        """查询指定条件下的项目列表

        该接口可以用于查询指定条件下的项目列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListProjectsRequest request
        :return: KeystoneListProjectsResponse
        """

        all_params = ['domain_id', 'name', 'parent_id', 'enabled', 'is_domain', 'page', 'per_page']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListProjectsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_projects_for_user(self, request):
        """查询指定IAM用户的项目列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的项目列表，或IAM用户查询自己的项目列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListProjectsForUserRequest request
        :return: KeystoneListProjectsForUserResponse
        """
        return self.keystone_list_projects_for_user_with_http_info(request)

    def keystone_list_projects_for_user_with_http_info(self, request):
        """查询指定IAM用户的项目列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的项目列表，或IAM用户查询自己的项目列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListProjectsForUserRequest request
        :return: KeystoneListProjectsForUserResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListProjectsForUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_regions(self, request):
        """查询区域列表

        该接口可以用于查询区域列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListRegionsRequest request
        :return: KeystoneListRegionsResponse
        """
        return self.keystone_list_regions_with_http_info(request)

    def keystone_list_regions_with_http_info(self, request):
        """查询区域列表

        该接口可以用于查询区域列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListRegionsRequest request
        :return: KeystoneListRegionsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/regions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListRegionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_services(self, request):
        """查询服务列表

        该接口可以用于查询服务列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListServicesRequest request
        :return: KeystoneListServicesResponse
        """
        return self.keystone_list_services_with_http_info(request)

    def keystone_list_services_with_http_info(self, request):
        """查询服务列表

        该接口可以用于查询服务列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListServicesRequest request
        :return: KeystoneListServicesResponse
        """

        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/services',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListServicesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_users_for_group_by_admin(self, request):
        """管理员查询用户组所包含的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组中所包含的IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListUsersForGroupByAdminRequest request
        :return: KeystoneListUsersForGroupByAdminResponse
        """
        return self.keystone_list_users_for_group_by_admin_with_http_info(request)

    def keystone_list_users_for_group_by_admin_with_http_info(self, request):
        """管理员查询用户组所包含的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组中所包含的IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListUsersForGroupByAdminRequest request
        :return: KeystoneListUsersForGroupByAdminResponse
        """

        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListUsersForGroupByAdminResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_versions(self, request):
        """查询版本信息列表

        该接口用于查询Keystone API的版本信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListVersionsRequest request
        :return: KeystoneListVersionsResponse
        """
        return self.keystone_list_versions_with_http_info(request)

    def keystone_list_versions_with_http_info(self, request):
        """查询版本信息列表

        该接口用于查询Keystone API的版本信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListVersionsRequest request
        :return: KeystoneListVersionsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListVersionsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_remove_domain_permission_from_group(self, request):
        """移除用户组的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneRemoveDomainPermissionFromGroupRequest request
        :return: KeystoneRemoveDomainPermissionFromGroupResponse
        """
        return self.keystone_remove_domain_permission_from_group_with_http_info(request)

    def keystone_remove_domain_permission_from_group_with_http_info(self, request):
        """移除用户组的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneRemoveDomainPermissionFromGroupRequest request
        :return: KeystoneRemoveDomainPermissionFromGroupResponse
        """

        all_params = ['domain_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneRemoveDomainPermissionFromGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_remove_project_permission_from_group(self, request):
        """移除用户组的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneRemoveProjectPermissionFromGroupRequest request
        :return: KeystoneRemoveProjectPermissionFromGroupResponse
        """
        return self.keystone_remove_project_permission_from_group_with_http_info(request)

    def keystone_remove_project_permission_from_group_with_http_info(self, request):
        """移除用户组的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneRemoveProjectPermissionFromGroupRequest request
        :return: KeystoneRemoveProjectPermissionFromGroupResponse
        """

        all_params = ['project_id', 'group_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneRemoveProjectPermissionFromGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_remove_user_from_group(self, request):
        """移除用户组中的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组中的IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneRemoveUserFromGroupRequest request
        :return: KeystoneRemoveUserFromGroupResponse
        """
        return self.keystone_remove_user_from_group_with_http_info(request)

    def keystone_remove_user_from_group_with_http_info(self, request):
        """移除用户组中的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组中的IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneRemoveUserFromGroupRequest request
        :return: KeystoneRemoveUserFromGroupResponse
        """

        all_params = ['group_id', 'user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneRemoveUserFromGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_catalog(self, request):
        """查询服务目录

        该接口可以用于查询请求头中X-Auth-Token对应的服务目录。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowCatalogRequest request
        :return: KeystoneShowCatalogResponse
        """
        return self.keystone_show_catalog_with_http_info(request)

    def keystone_show_catalog_with_http_info(self, request):
        """查询服务目录

        该接口可以用于查询请求头中X-Auth-Token对应的服务目录。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowCatalogRequest request
        :return: KeystoneShowCatalogResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3/auth/catalog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowCatalogResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_endpoint(self, request):
        """查询终端节点详情

        该接口可以用于查询终端节点详情。终端节点用来提供服务访问入口。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowEndpointRequest request
        :return: KeystoneShowEndpointResponse
        """
        return self.keystone_show_endpoint_with_http_info(request)

    def keystone_show_endpoint_with_http_info(self, request):
        """查询终端节点详情

        该接口可以用于查询终端节点详情。终端节点用来提供服务访问入口。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowEndpointRequest request
        :return: KeystoneShowEndpointResponse
        """

        all_params = ['endpoint_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/endpoints/{endpoint_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowEndpointResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_group(self, request):
        """查询用户组详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowGroupRequest request
        :return: KeystoneShowGroupResponse
        """
        return self.keystone_show_group_with_http_info(request)

    def keystone_show_group_with_http_info(self, request):
        """查询用户组详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowGroupRequest request
        :return: KeystoneShowGroupResponse
        """

        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_permission(self, request):
        """查询权限详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowPermissionRequest request
        :return: KeystoneShowPermissionResponse
        """
        return self.keystone_show_permission_with_http_info(request)

    def keystone_show_permission_with_http_info(self, request):
        """查询权限详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowPermissionRequest request
        :return: KeystoneShowPermissionResponse
        """

        all_params = ['role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/roles/{role_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowPermissionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_project(self, request):
        """查询项目详情

        该接口可以用于查询项目详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowProjectRequest request
        :return: KeystoneShowProjectResponse
        """
        return self.keystone_show_project_with_http_info(request)

    def keystone_show_project_with_http_info(self, request):
        """查询项目详情

        该接口可以用于查询项目详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowProjectRequest request
        :return: KeystoneShowProjectResponse
        """

        all_params = ['project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowProjectResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_region(self, request):
        """查询区域详情

        该接口可以用于查询区域详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowRegionRequest request
        :return: KeystoneShowRegionResponse
        """
        return self.keystone_show_region_with_http_info(request)

    def keystone_show_region_with_http_info(self, request):
        """查询区域详情

        该接口可以用于查询区域详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowRegionRequest request
        :return: KeystoneShowRegionResponse
        """

        all_params = ['region_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/regions/{region_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowRegionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_security_compliance(self, request):
        """查询账号密码强度策略

        该接口可以用于查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowSecurityComplianceRequest request
        :return: KeystoneShowSecurityComplianceResponse
        """
        return self.keystone_show_security_compliance_with_http_info(request)

    def keystone_show_security_compliance_with_http_info(self, request):
        """查询账号密码强度策略

        该接口可以用于查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowSecurityComplianceRequest request
        :return: KeystoneShowSecurityComplianceResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/config/security_compliance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowSecurityComplianceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_security_compliance_by_option(self, request):
        """按条件查询账号密码强度策略

        该接口可以用于按条件查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowSecurityComplianceByOptionRequest request
        :return: KeystoneShowSecurityComplianceByOptionResponse
        """
        return self.keystone_show_security_compliance_by_option_with_http_info(request)

    def keystone_show_security_compliance_by_option_with_http_info(self, request):
        """按条件查询账号密码强度策略

        该接口可以用于按条件查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowSecurityComplianceByOptionRequest request
        :return: KeystoneShowSecurityComplianceByOptionResponse
        """

        all_params = ['domain_id', 'option']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/domains/{domain_id}/config/security_compliance/{option}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowSecurityComplianceByOptionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_service(self, request):
        """查询服务详情

        该接口可以用于查询服务详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowServiceRequest request
        :return: KeystoneShowServiceResponse
        """
        return self.keystone_show_service_with_http_info(request)

    def keystone_show_service_with_http_info(self, request):
        """查询服务详情

        该接口可以用于查询服务详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowServiceRequest request
        :return: KeystoneShowServiceResponse
        """

        all_params = ['service_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/services/{service_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowServiceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_version(self, request):
        """查询版本信息

        该接口用于查询Keystone API的3.0版本的信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowVersionRequest request
        :return: KeystoneShowVersionResponse
        """
        return self.keystone_show_version_with_http_info(request)

    def keystone_show_version_with_http_info(self, request):
        """查询版本信息

        该接口用于查询Keystone API的3.0版本的信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowVersionRequest request
        :return: KeystoneShowVersionResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowVersionResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_update_group(self, request):
        """更新用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新用户组信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateGroupRequest request
        :return: KeystoneUpdateGroupResponse
        """
        return self.keystone_update_group_with_http_info(request)

    def keystone_update_group_with_http_info(self, request):
        """更新用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新用户组信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateGroupRequest request
        :return: KeystoneUpdateGroupResponse
        """

        all_params = ['group_id', 'keystone_update_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneUpdateGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_update_project(self, request):
        """修改项目信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改项目信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateProjectRequest request
        :return: KeystoneUpdateProjectResponse
        """
        return self.keystone_update_project_with_http_info(request)

    def keystone_update_project_with_http_info(self, request):
        """修改项目信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改项目信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateProjectRequest request
        :return: KeystoneUpdateProjectResponse
        """

        all_params = ['project_id', 'keystone_update_project_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneUpdateProjectResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_agencies(self, request):
        """查询指定条件下的委托列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListAgenciesRequest request
        :return: ListAgenciesResponse
        """
        return self.list_agencies_with_http_info(request)

    def list_agencies_with_http_info(self, request):
        """查询指定条件下的委托列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListAgenciesRequest request
        :return: ListAgenciesResponse
        """

        all_params = ['domain_id', 'trust_domain_id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAgenciesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_all_projects_permissions_for_agency(self, request):
        """查询委托下的所有项目服务权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托所有项目服务权限列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListAllProjectsPermissionsForAgencyRequest request
        :return: ListAllProjectsPermissionsForAgencyResponse
        """
        return self.list_all_projects_permissions_for_agency_with_http_info(request)

    def list_all_projects_permissions_for_agency_with_http_info(self, request):
        """查询委托下的所有项目服务权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托所有项目服务权限列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListAllProjectsPermissionsForAgencyRequest request
        :return: ListAllProjectsPermissionsForAgencyResponse
        """

        all_params = ['agency_id', 'domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/inherited_to_projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAllProjectsPermissionsForAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_custom_policies(self, request):
        """查询自定义策略列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListCustomPoliciesRequest request
        :return: ListCustomPoliciesResponse
        """
        return self.list_custom_policies_with_http_info(request)

    def list_custom_policies_with_http_info(self, request):
        """查询自定义策略列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListCustomPoliciesRequest request
        :return: ListCustomPoliciesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCustomPoliciesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domain_permissions_for_agency(self, request):
        """查询全局服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的委托权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListDomainPermissionsForAgencyRequest request
        :return: ListDomainPermissionsForAgencyResponse
        """
        return self.list_domain_permissions_for_agency_with_http_info(request)

    def list_domain_permissions_for_agency_with_http_info(self, request):
        """查询全局服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的委托权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListDomainPermissionsForAgencyRequest request
        :return: ListDomainPermissionsForAgencyResponse
        """

        all_params = ['domain_id', 'agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDomainPermissionsForAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_permissions_for_agency(self, request):
        """查询项目服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的委托权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListProjectPermissionsForAgencyRequest request
        :return: ListProjectPermissionsForAgencyResponse
        """
        return self.list_project_permissions_for_agency_with_http_info(request)

    def list_project_permissions_for_agency_with_http_info(self, request):
        """查询项目服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的委托权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListProjectPermissionsForAgencyRequest request
        :return: ListProjectPermissionsForAgencyResponse
        """

        all_params = ['project_id', 'agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectPermissionsForAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_all_projects_permission_from_agency(self, request):
        """移除委托下的所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param RemoveAllProjectsPermissionFromAgencyRequest request
        :return: RemoveAllProjectsPermissionFromAgencyResponse
        """
        return self.remove_all_projects_permission_from_agency_with_http_info(request)

    def remove_all_projects_permission_from_agency_with_http_info(self, request):
        """移除委托下的所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的所有项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param RemoveAllProjectsPermissionFromAgencyRequest request
        :return: RemoveAllProjectsPermissionFromAgencyResponse
        """

        all_params = ['agency_id', 'domain_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveAllProjectsPermissionFromAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_domain_permission_from_agency(self, request):
        """移除委托的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param RemoveDomainPermissionFromAgencyRequest request
        :return: RemoveDomainPermissionFromAgencyResponse
        """
        return self.remove_domain_permission_from_agency_with_http_info(request)

    def remove_domain_permission_from_agency_with_http_info(self, request):
        """移除委托的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的全局服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param RemoveDomainPermissionFromAgencyRequest request
        :return: RemoveDomainPermissionFromAgencyResponse
        """

        all_params = ['domain_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveDomainPermissionFromAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_project_permission_from_agency(self, request):
        """移除委托的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param RemoveProjectPermissionFromAgencyRequest request
        :return: RemoveProjectPermissionFromAgencyResponse
        """
        return self.remove_project_permission_from_agency_with_http_info(request)

    def remove_project_permission_from_agency_with_http_info(self, request):
        """移除委托的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的项目服务权限。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param RemoveProjectPermissionFromAgencyRequest request
        :return: RemoveProjectPermissionFromAgencyResponse
        """

        all_params = ['project_id', 'agency_id', 'role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveProjectPermissionFromAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_agency(self, request):
        """查询委托详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowAgencyRequest request
        :return: ShowAgencyResponse
        """
        return self.show_agency_with_http_info(request)

    def show_agency_with_http_info(self, request):
        """查询委托详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowAgencyRequest request
        :return: ShowAgencyResponse
        """

        all_params = ['agency_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-AGENCY/agencies/{agency_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_custom_policy(self, request):
        """查询自定义策略详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowCustomPolicyRequest request
        :return: ShowCustomPolicyResponse
        """
        return self.show_custom_policy_with_http_info(request)

    def show_custom_policy_with_http_info(self, request):
        """查询自定义策略详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowCustomPolicyRequest request
        :return: ShowCustomPolicyResponse
        """

        all_params = ['role_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-ROLE/roles/{role_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCustomPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_api_acl_policy(self, request):
        """查询账号接口访问策略

        该接口可以用于查询账号接口访问控制策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainApiAclPolicyRequest request
        :return: ShowDomainApiAclPolicyResponse
        """
        return self.show_domain_api_acl_policy_with_http_info(request)

    def show_domain_api_acl_policy_with_http_info(self, request):
        """查询账号接口访问策略

        该接口可以用于查询账号接口访问控制策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainApiAclPolicyRequest request
        :return: ShowDomainApiAclPolicyResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/api-acl-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainApiAclPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_console_acl_policy(self, request):
        """查询账号控制台访问策略

        该接口可以用于查询账号控制台访问控制策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainConsoleAclPolicyRequest request
        :return: ShowDomainConsoleAclPolicyResponse
        """
        return self.show_domain_console_acl_policy_with_http_info(request)

    def show_domain_console_acl_policy_with_http_info(self, request):
        """查询账号控制台访问策略

        该接口可以用于查询账号控制台访问控制策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainConsoleAclPolicyRequest request
        :return: ShowDomainConsoleAclPolicyResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/console-acl-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainConsoleAclPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_login_policy(self, request):
        """查询账号登录策略

        该接口可以用于查询账号登录策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainLoginPolicyRequest request
        :return: ShowDomainLoginPolicyResponse
        """
        return self.show_domain_login_policy_with_http_info(request)

    def show_domain_login_policy_with_http_info(self, request):
        """查询账号登录策略

        该接口可以用于查询账号登录策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainLoginPolicyRequest request
        :return: ShowDomainLoginPolicyResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/login-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainLoginPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_password_policy(self, request):
        """查询账号密码策略

        该接口可以用于查询账号密码策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainPasswordPolicyRequest request
        :return: ShowDomainPasswordPolicyResponse
        """
        return self.show_domain_password_policy_with_http_info(request)

    def show_domain_password_policy_with_http_info(self, request):
        """查询账号密码策略

        该接口可以用于查询账号密码策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainPasswordPolicyRequest request
        :return: ShowDomainPasswordPolicyResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/password-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainPasswordPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_protect_policy(self, request):
        """查询账号操作保护策略

        该接口可以用于查询账号操作保护策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainProtectPolicyRequest request
        :return: ShowDomainProtectPolicyResponse
        """
        return self.show_domain_protect_policy_with_http_info(request)

    def show_domain_protect_policy_with_http_info(self, request):
        """查询账号操作保护策略

        该接口可以用于查询账号操作保护策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainProtectPolicyRequest request
        :return: ShowDomainProtectPolicyResponse
        """

        all_params = ['domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/protect-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainProtectPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_domain_quota(self, request):
        """查询账号配额

        该接口可以用于查询账号配额。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainQuotaRequest request
        :return: ShowDomainQuotaResponse
        """
        return self.show_domain_quota_with_http_info(request)

    def show_domain_quota_with_http_info(self, request):
        """查询账号配额

        该接口可以用于查询账号配额。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowDomainQuotaRequest request
        :return: ShowDomainQuotaResponse
        """

        all_params = ['domain_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-QUOTA/domains/{domain_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDomainQuotaResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_details_and_status(self, request):
        """查询项目详情与状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目详情与状态。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowProjectDetailsAndStatusRequest request
        :return: ShowProjectDetailsAndStatusResponse
        """
        return self.show_project_details_and_status_with_http_info(request)

    def show_project_details_and_status_with_http_info(self, request):
        """查询项目详情与状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目详情与状态。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowProjectDetailsAndStatusRequest request
        :return: ShowProjectDetailsAndStatusResponse
        """

        all_params = ['project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3-ext/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectDetailsAndStatusResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_quota(self, request):
        """查询项目配额

        该接口可以用于查询项目配额。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowProjectQuotaRequest request
        :return: ShowProjectQuotaResponse
        """
        return self.show_project_quota_with_http_info(request)

    def show_project_quota_with_http_info(self, request):
        """查询项目配额

        该接口可以用于查询项目配额。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowProjectQuotaRequest request
        :return: ShowProjectQuotaResponse
        """

        all_params = ['project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-QUOTA/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowProjectQuotaResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_agency(self, request):
        """修改委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateAgencyRequest request
        :return: UpdateAgencyResponse
        """
        return self.update_agency_with_http_info(request)

    def update_agency_with_http_info(self, request):
        """修改委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateAgencyRequest request
        :return: UpdateAgencyResponse
        """

        all_params = ['agency_id', 'update_agency_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_agency_custom_policy(self, request):
        """修改委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateAgencyCustomPolicyRequest request
        :return: UpdateAgencyCustomPolicyResponse
        """
        return self.update_agency_custom_policy_with_http_info(request)

    def update_agency_custom_policy_with_http_info(self, request):
        """修改委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateAgencyCustomPolicyRequest request
        :return: UpdateAgencyCustomPolicyResponse
        """

        all_params = ['role_id', 'update_agency_custom_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateAgencyCustomPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cloud_service_custom_policy(self, request):
        """修改云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改云服务自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateCloudServiceCustomPolicyRequest request
        :return: UpdateCloudServiceCustomPolicyResponse
        """
        return self.update_cloud_service_custom_policy_with_http_info(request)

    def update_cloud_service_custom_policy_with_http_info(self, request):
        """修改云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改云服务自定义策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateCloudServiceCustomPolicyRequest request
        :return: UpdateCloudServiceCustomPolicyResponse
        """

        all_params = ['role_id', 'update_cloud_service_custom_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateCloudServiceCustomPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_api_acl_policy(self, request):
        """修改账号接口访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号接口访问策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainApiAclPolicyRequest request
        :return: UpdateDomainApiAclPolicyResponse
        """
        return self.update_domain_api_acl_policy_with_http_info(request)

    def update_domain_api_acl_policy_with_http_info(self, request):
        """修改账号接口访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号接口访问策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainApiAclPolicyRequest request
        :return: UpdateDomainApiAclPolicyResponse
        """

        all_params = ['domain_id', 'update_domain_api_acl_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainApiAclPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_console_acl_policy(self, request):
        """修改账号控制台访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号控制台访问策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainConsoleAclPolicyRequest request
        :return: UpdateDomainConsoleAclPolicyResponse
        """
        return self.update_domain_console_acl_policy_with_http_info(request)

    def update_domain_console_acl_policy_with_http_info(self, request):
        """修改账号控制台访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号控制台访问策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainConsoleAclPolicyRequest request
        :return: UpdateDomainConsoleAclPolicyResponse
        """

        all_params = ['domain_id', 'update_domain_console_acl_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainConsoleAclPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_login_policy(self, request):
        """修改账号登录策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号登录策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainLoginPolicyRequest request
        :return: UpdateDomainLoginPolicyResponse
        """
        return self.update_domain_login_policy_with_http_info(request)

    def update_domain_login_policy_with_http_info(self, request):
        """修改账号登录策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号登录策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainLoginPolicyRequest request
        :return: UpdateDomainLoginPolicyResponse
        """

        all_params = ['domain_id', 'update_domain_login_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainLoginPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_password_policy(self, request):
        """修改账号密码策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号密码策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainPasswordPolicyRequest request
        :return: UpdateDomainPasswordPolicyResponse
        """
        return self.update_domain_password_policy_with_http_info(request)

    def update_domain_password_policy_with_http_info(self, request):
        """修改账号密码策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号密码策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainPasswordPolicyRequest request
        :return: UpdateDomainPasswordPolicyResponse
        """

        all_params = ['domain_id', 'update_domain_password_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainPasswordPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_domain_protect_policy(self, request):
        """修改账号操作保护策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainProtectPolicyRequest request
        :return: UpdateDomainProtectPolicyResponse
        """
        return self.update_domain_protect_policy_with_http_info(request)

    def update_domain_protect_policy_with_http_info(self, request):
        """修改账号操作保护策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护策略。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateDomainProtectPolicyRequest request
        :return: UpdateDomainProtectPolicyResponse
        """

        all_params = ['domain_id', 'update_domain_protect_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateDomainProtectPolicyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_project_status(self, request):
        """设置项目状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)设置项目状态。项目状态包括：正常、冻结。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateProjectStatusRequest request
        :return: UpdateProjectStatusResponse
        """
        return self.update_project_status_with_http_info(request)

    def update_project_status_with_http_info(self, request):
        """设置项目状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)设置项目状态。项目状态包括：正常、冻结。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateProjectStatusRequest request
        :return: UpdateProjectStatusResponse
        """

        all_params = ['project_id', 'update_project_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateProjectStatusResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_permanent_access_key(self, request):
        """创建永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)给IAM用户创建永久访问密钥，或IAM用户给自己创建永久访问密钥。    访问密钥（Access Key ID/Secret Access Key，简称AK/SK），是您通过开发工具（API、CLI、SDK）访问华为云时的身份凭证，不用于登录控制台。系统通过AK识别访问用户的身份，通过SK进行签名验证，通过加密签名验证可以确保请求的机密性、完整性和请求者身份的正确性。在控制台创建访问密钥的方式请参见：[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html)  。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreatePermanentAccessKeyRequest request
        :return: CreatePermanentAccessKeyResponse
        """
        return self.create_permanent_access_key_with_http_info(request)

    def create_permanent_access_key_with_http_info(self, request):
        """创建永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)给IAM用户创建永久访问密钥，或IAM用户给自己创建永久访问密钥。    访问密钥（Access Key ID/Secret Access Key，简称AK/SK），是您通过开发工具（API、CLI、SDK）访问华为云时的身份凭证，不用于登录控制台。系统通过AK识别访问用户的身份，通过SK进行签名验证，通过加密签名验证可以确保请求的机密性、完整性和请求者身份的正确性。在控制台创建访问密钥的方式请参见：[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html)  。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreatePermanentAccessKeyRequest request
        :return: CreatePermanentAccessKeyResponse
        """

        all_params = ['create_permanent_access_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreatePermanentAccessKeyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_temporary_access_key_by_agency(self, request):
        """通过委托获取临时访问密钥

        该接口可以用于通过委托来获取临时访问密钥（临时AK/SK）和securitytoken。    临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html) 。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateTemporaryAccessKeyByAgencyRequest request
        :return: CreateTemporaryAccessKeyByAgencyResponse
        """
        return self.create_temporary_access_key_by_agency_with_http_info(request)

    def create_temporary_access_key_by_agency_with_http_info(self, request):
        """通过委托获取临时访问密钥

        该接口可以用于通过委托来获取临时访问密钥（临时AK/SK）和securitytoken。    临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html) 。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateTemporaryAccessKeyByAgencyRequest request
        :return: CreateTemporaryAccessKeyByAgencyResponse
        """

        all_params = ['create_temporary_access_key_by_agency_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateTemporaryAccessKeyByAgencyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_temporary_access_key_by_token(self, request):
        """通过token获取临时访问密钥

        该接口可以用于通过token来获取临时AK/SK和securitytoken。    临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html)。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateTemporaryAccessKeyByTokenRequest request
        :return: CreateTemporaryAccessKeyByTokenResponse
        """
        return self.create_temporary_access_key_by_token_with_http_info(request)

    def create_temporary_access_key_by_token_with_http_info(self, request):
        """通过token获取临时访问密钥

        该接口可以用于通过token来获取临时AK/SK和securitytoken。    临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html)。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateTemporaryAccessKeyByTokenRequest request
        :return: CreateTemporaryAccessKeyByTokenResponse
        """

        all_params = ['create_temporary_access_key_by_token_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateTemporaryAccessKeyByTokenResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_permanent_access_key(self, request):
        """删除指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除IAM用户的指定永久访问密钥，或IAM用户删除自己的指定永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param DeletePermanentAccessKeyRequest request
        :return: DeletePermanentAccessKeyResponse
        """
        return self.delete_permanent_access_key_with_http_info(request)

    def delete_permanent_access_key_with_http_info(self, request):
        """删除指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除IAM用户的指定永久访问密钥，或IAM用户删除自己的指定永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param DeletePermanentAccessKeyRequest request
        :return: DeletePermanentAccessKeyResponse
        """

        all_params = ['access_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials/{access_key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePermanentAccessKeyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_permanent_access_keys(self, request):
        """查询所有永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的所有永久访问密钥，或IAM用户查询自己的所有永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListPermanentAccessKeysRequest request
        :return: ListPermanentAccessKeysResponse
        """
        return self.list_permanent_access_keys_with_http_info(request)

    def list_permanent_access_keys_with_http_info(self, request):
        """查询所有永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的所有永久访问密钥，或IAM用户查询自己的所有永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListPermanentAccessKeysRequest request
        :return: ListPermanentAccessKeysResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPermanentAccessKeysResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_permanent_access_key(self, request):
        """查询指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的指定永久访问密钥，或IAM用户查询自己的指定永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowPermanentAccessKeyRequest request
        :return: ShowPermanentAccessKeyResponse
        """
        return self.show_permanent_access_key_with_http_info(request)

    def show_permanent_access_key_with_http_info(self, request):
        """查询指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的指定永久访问密钥，或IAM用户查询自己的指定永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowPermanentAccessKeyRequest request
        :return: ShowPermanentAccessKeyResponse
        """

        all_params = ['access_key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-CREDENTIAL/credentials/{access_key}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPermanentAccessKeyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_permanent_access_key(self, request):
        """修改指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户的指定永久访问密钥，或IAM用户修改自己的指定永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdatePermanentAccessKeyRequest request
        :return: UpdatePermanentAccessKeyResponse
        """
        return self.update_permanent_access_key_with_http_info(request)

    def update_permanent_access_key_with_http_info(self, request):
        """修改指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户的指定永久访问密钥，或IAM用户修改自己的指定永久访问密钥。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdatePermanentAccessKeyRequest request
        :return: UpdatePermanentAccessKeyResponse
        """

        all_params = ['access_key', 'update_permanent_access_key_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdatePermanentAccessKeyResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_user(self, request):
        """管理员创建IAM用户（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateUserRequest request
        :return: CreateUserResponse
        """
        return self.create_user_with_http_info(request)

    def create_user_with_http_info(self, request):
        """管理员创建IAM用户（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param CreateUserRequest request
        :return: CreateUserResponse
        """

        all_params = ['create_user_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreateUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_create_user(self, request):
        """管理员创建IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。IAM用户首次登录时需要修改密码。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCreateUserRequest request
        :return: KeystoneCreateUserResponse
        """
        return self.keystone_create_user_with_http_info(request)

    def keystone_create_user_with_http_info(self, request):
        """管理员创建IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。IAM用户首次登录时需要修改密码。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneCreateUserRequest request
        :return: KeystoneCreateUserResponse
        """

        all_params = ['keystone_create_user_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneCreateUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_delete_user(self, request):
        """管理员删除IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除指定IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneDeleteUserRequest request
        :return: KeystoneDeleteUserResponse
        """
        return self.keystone_delete_user_with_http_info(request)

    def keystone_delete_user_with_http_info(self, request):
        """管理员删除IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除指定IAM用户。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneDeleteUserRequest request
        :return: KeystoneDeleteUserResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneDeleteUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_groups_for_user(self, request):
        """查询IAM用户所属用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户所属用户组，或IAM用户查询自己所属用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListGroupsForUserRequest request
        :return: KeystoneListGroupsForUserResponse
        """
        return self.keystone_list_groups_for_user_with_http_info(request)

    def keystone_list_groups_for_user_with_http_info(self, request):
        """查询IAM用户所属用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户所属用户组，或IAM用户查询自己所属用户组。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListGroupsForUserRequest request
        :return: KeystoneListGroupsForUserResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListGroupsForUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_list_users(self, request):
        """管理员查询IAM用户列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListUsersRequest request
        :return: KeystoneListUsersResponse
        """
        return self.keystone_list_users_with_http_info(request)

    def keystone_list_users_with_http_info(self, request):
        """管理员查询IAM用户列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneListUsersRequest request
        :return: KeystoneListUsersResponse
        """

        all_params = ['domain_id', 'enabled', 'name', 'password_expires_at']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneListUsersResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_show_user(self, request):
        """查询IAM用户详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的用户详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowUserRequest request
        :return: KeystoneShowUserResponse
        """
        return self.keystone_show_user_with_http_info(request)

    def keystone_show_user_with_http_info(self, request):
        """查询IAM用户详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的用户详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneShowUserRequest request
        :return: KeystoneShowUserResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='KeystoneShowUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_update_user_by_admin(self, request):
        """管理员修改IAM用户信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateUserByAdminRequest request
        :return: KeystoneUpdateUserByAdminResponse
        """
        return self.keystone_update_user_by_admin_with_http_info(request)

    def keystone_update_user_by_admin_with_http_info(self, request):
        """管理员修改IAM用户信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateUserByAdminRequest request
        :return: KeystoneUpdateUserByAdminResponse
        """

        all_params = ['user_id', 'keystone_update_user_by_admin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneUpdateUserByAdminResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def keystone_update_user_password(self, request):
        """修改IAM用户密码

        该接口可以用于IAM用户修改自己的密码。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateUserPasswordRequest request
        :return: KeystoneUpdateUserPasswordResponse
        """
        return self.keystone_update_user_password_with_http_info(request)

    def keystone_update_user_password_with_http_info(self, request):
        """修改IAM用户密码

        该接口可以用于IAM用户修改自己的密码。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param KeystoneUpdateUserPasswordRequest request
        :return: KeystoneUpdateUserPasswordResponse
        """

        all_params = ['user_id', 'keystone_update_user_password_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='KeystoneUpdateUserPasswordResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_user_login_protects(self, request):
        """查询IAM用户的登录保护状态信息列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的登录保护状态列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListUserLoginProtectsRequest request
        :return: ListUserLoginProtectsResponse
        """
        return self.list_user_login_protects_with_http_info(request)

    def list_user_login_protects_with_http_info(self, request):
        """查询IAM用户的登录保护状态信息列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的登录保护状态列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListUserLoginProtectsRequest request
        :return: ListUserLoginProtectsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/login-protects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUserLoginProtectsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_user_mfa_devices(self, request):
        """查询IAM用户的MFA绑定信息列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的MFA绑定信息列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListUserMfaDevicesRequest request
        :return: ListUserMfaDevicesResponse
        """
        return self.list_user_mfa_devices_with_http_info(request)

    def list_user_mfa_devices_with_http_info(self, request):
        """查询IAM用户的MFA绑定信息列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的MFA绑定信息列表。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ListUserMfaDevicesRequest request
        :return: ListUserMfaDevicesResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/virtual-mfa-devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUserMfaDevicesResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user(self, request):
        """查询IAM用户详情（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowUserRequest request
        :return: ShowUserResponse
        """
        return self.show_user_with_http_info(request)

    def show_user_with_http_info(self, request):
        """查询IAM用户详情（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的详情。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowUserRequest request
        :return: ShowUserResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user_login_protect(self, request):
        """查询指定IAM用户的登录保护状态信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的登录保护状态信息，或IAM用户查询自己的登录保护状态信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowUserLoginProtectRequest request
        :return: ShowUserLoginProtectResponse
        """
        return self.show_user_login_protect_with_http_info(request)

    def show_user_login_protect_with_http_info(self, request):
        """查询指定IAM用户的登录保护状态信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的登录保护状态信息，或IAM用户查询自己的登录保护状态信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowUserLoginProtectRequest request
        :return: ShowUserLoginProtectResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-USER/users/{user_id}/login-protect',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserLoginProtectResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user_mfa_device(self, request):
        """查询指定IAM用户的MFA绑定信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的MFA绑定信息，或IAM用户查询自己的MFA绑定信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowUserMfaDeviceRequest request
        :return: ShowUserMfaDeviceResponse
        """
        return self.show_user_mfa_device_with_http_info(request)

    def show_user_mfa_device_with_http_info(self, request):
        """查询指定IAM用户的MFA绑定信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的MFA绑定信息，或IAM用户查询自己的MFA绑定信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param ShowUserMfaDeviceRequest request
        :return: ShowUserMfaDeviceResponse
        """

        all_params = ['user_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = []

        return self.call_api(
            resource_path='/v3.0/OS-MFA/users/{user_id}/virtual-mfa-device',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserMfaDeviceResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_user(self, request):
        """管理员修改IAM用户信息（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息 。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateUserRequest request
        :return: UpdateUserResponse
        """
        return self.update_user_with_http_info(request)

    def update_user_with_http_info(self, request):
        """管理员修改IAM用户信息（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息 。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateUserRequest request
        :return: UpdateUserResponse
        """

        all_params = ['user_id', 'update_user_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateUserResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_user_information(self, request):
        """修改IAM用户信息（推荐）

        该接口可以用于IAM用户修改自己的用户信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateUserInformationRequest request
        :return: UpdateUserInformationResponse
        """
        return self.update_user_information_with_http_info(request)

    def update_user_information_with_http_info(self, request):
        """修改IAM用户信息（推荐）

        该接口可以用于IAM用户修改自己的用户信息。    该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。

        :param UpdateUserInformationRequest request
        :return: UpdateUserInformationResponse
        """

        all_params = ['user_id', 'update_user_information_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateUserInformationResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
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
            response_type=response_type,
            collection_formats=collection_formats,
            request_type=request_type)

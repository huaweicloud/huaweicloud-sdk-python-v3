# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiam'")


class IamAsyncClient(Client):
    def __init__(self):
        super(IamAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiam.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials,BasicCredentials,IamCredentials")
        else:
            if clazz.__name__ != "IamAsyncClient":
                raise TypeError("client type error, support client type is IamAsyncClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials,BasicCredentials,IamCredentials")

        

        return client_builder

    def associate_agency_with_all_projects_permission_async(self, request):
        """为委托授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateAgencyWithAllProjectsPermission
        :type request: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithAllProjectsPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithAllProjectsPermissionResponse`
        """
        http_info = self._associate_agency_with_all_projects_permission_http_info(request)
        return self._call_api(**http_info)

    def associate_agency_with_all_projects_permission_async_invoker(self, request):
        http_info = self._associate_agency_with_all_projects_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_agency_with_all_projects_permission_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateAgencyWithAllProjectsPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def associate_agency_with_domain_permission_async(self, request):
        """为委托授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateAgencyWithDomainPermission
        :type request: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithDomainPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithDomainPermissionResponse`
        """
        http_info = self._associate_agency_with_domain_permission_http_info(request)
        return self._call_api(**http_info)

    def associate_agency_with_domain_permission_async_invoker(self, request):
        http_info = self._associate_agency_with_domain_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_agency_with_domain_permission_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateAgencyWithDomainPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def associate_agency_with_project_permission_async(self, request):
        """为委托授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为委托授予项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateAgencyWithProjectPermission
        :type request: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateAgencyWithProjectPermissionResponse`
        """
        http_info = self._associate_agency_with_project_permission_http_info(request)
        return self._call_api(**http_info)

    def associate_agency_with_project_permission_async_invoker(self, request):
        http_info = self._associate_agency_with_project_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_agency_with_project_permission_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateAgencyWithProjectPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def associate_role_to_agency_on_enterprise_project_async(self, request):
        """application/json

        该接口可以基于委托为企业项目授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRoleToAgencyOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.AssociateRoleToAgencyOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateRoleToAgencyOnEnterpriseProjectResponse`
        """
        http_info = self._associate_role_to_agency_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def associate_role_to_agency_on_enterprise_project_async_invoker(self, request):
        http_info = self._associate_role_to_agency_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_role_to_agency_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-PERMISSION/subjects/agency/scopes/enterprise-project/role-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRoleToAgencyOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def associate_role_to_group_on_enterprise_project_async(self, request):
        """基于用户组为企业项目授权

        该接口用于基于用户组为企业项目授权。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRoleToGroupOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.AssociateRoleToGroupOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateRoleToGroupOnEnterpriseProjectResponse`
        """
        http_info = self._associate_role_to_group_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def associate_role_to_group_on_enterprise_project_async_invoker(self, request):
        http_info = self._associate_role_to_group_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_role_to_group_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRoleToGroupOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def associate_role_to_user_on_enterprise_project_async(self, request):
        """基于用户为企业项目授权

        基于用户为企业项目授权。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRoleToUserOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.AssociateRoleToUserOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.AssociateRoleToUserOnEnterpriseProjectResponse`
        """
        http_info = self._associate_role_to_user_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def associate_role_to_user_on_enterprise_project_async_invoker(self, request):
        http_info = self._associate_role_to_user_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_role_to_user_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users/{user_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRoleToUserOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def check_all_projects_permission_for_agency_async(self, request):
        """检查委托下是否具有所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)检查委托是否具有所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckAllProjectsPermissionForAgency
        :type request: :class:`huaweicloudsdkiam.v3.CheckAllProjectsPermissionForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CheckAllProjectsPermissionForAgencyResponse`
        """
        http_info = self._check_all_projects_permission_for_agency_http_info(request)
        return self._call_api(**http_info)

    def check_all_projects_permission_for_agency_async_invoker(self, request):
        http_info = self._check_all_projects_permission_for_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_all_projects_permission_for_agency_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAllProjectsPermissionForAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def check_domain_permission_for_agency_async(self, request):
        """查询委托是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDomainPermissionForAgency
        :type request: :class:`huaweicloudsdkiam.v3.CheckDomainPermissionForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CheckDomainPermissionForAgencyResponse`
        """
        http_info = self._check_domain_permission_for_agency_http_info(request)
        return self._call_api(**http_info)

    def check_domain_permission_for_agency_async_invoker(self, request):
        http_info = self._check_domain_permission_for_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_domain_permission_for_agency_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDomainPermissionForAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def check_project_permission_for_agency_async(self, request):
        """查询委托是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托是否拥有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckProjectPermissionForAgency
        :type request: :class:`huaweicloudsdkiam.v3.CheckProjectPermissionForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CheckProjectPermissionForAgencyResponse`
        """
        http_info = self._check_project_permission_for_agency_http_info(request)
        return self._call_api(**http_info)

    def check_project_permission_for_agency_async_invoker(self, request):
        http_info = self._check_project_permission_for_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_project_permission_for_agency_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckProjectPermissionForAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_agency_async(self, request):
        """创建委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgency
        :type request: :class:`huaweicloudsdkiam.v3.CreateAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateAgencyResponse`
        """
        http_info = self._create_agency_http_info(request)
        return self._call_api(**http_info)

    def create_agency_async_invoker(self, request):
        http_info = self._create_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-AGENCY/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_agency_custom_policy_async(self, request):
        """创建委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建委托自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgencyCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.CreateAgencyCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateAgencyCustomPolicyResponse`
        """
        http_info = self._create_agency_custom_policy_http_info(request)
        return self._call_api(**http_info)

    def create_agency_custom_policy_async_invoker(self, request):
        http_info = self._create_agency_custom_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agency_custom_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-ROLE/roles",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgencyCustomPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_cloud_service_custom_policy_async(self, request):
        """创建云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建云服务自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCloudServiceCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.CreateCloudServiceCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateCloudServiceCustomPolicyResponse`
        """
        http_info = self._create_cloud_service_custom_policy_http_info(request)
        return self._call_api(**http_info)

    def create_cloud_service_custom_policy_async_invoker(self, request):
        http_info = self._create_cloud_service_custom_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_cloud_service_custom_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-ROLE/roles",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCloudServiceCustomPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_login_token_async(self, request):
        """获取自定义代理登录票据

        该接口用于用于获取自定义代理登录票据logintoken。logintoken是系统颁发给自定义代理用户的登录票据，承载用户的身份、session等信息。调用自定义代理URL登录云服务控制台时，可以使用本接口获取的logintoken进行认证。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        &gt; - logintoken的有效期为10分钟。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLoginToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateLoginTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateLoginTokenResponse`
        """
        http_info = self._create_login_token_http_info(request)
        return self._call_api(**http_info)

    def create_login_token_async_invoker(self, request):
        http_info = self._create_login_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_login_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-AUTH/securitytoken/logintokens",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLoginTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-LoginToken", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_metadata_async(self, request):
        """导入Metadata文件

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)导入Metadata文件。
        
        账号在使用联邦认证功能前，需要先将Metadata文件导入到IAM中。Metadata文件是SAML 2.0协议约定的接口文件，包含访问接口地址和证书信息，请找企业管理员获取企业IdP的Metadata文件。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMetadata
        :type request: :class:`huaweicloudsdkiam.v3.CreateMetadataRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateMetadataResponse`
        """
        http_info = self._create_metadata_http_info(request)
        return self._call_api(**http_info)

    def create_metadata_async_invoker(self, request):
        http_info = self._create_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_metadata_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3-ext/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_open_id_connect_config_async(self, request):
        """创建OpenId Connect身份提供商配置

        创建OpenId Connect身份提供商配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOpenIdConnectConfig
        :type request: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateOpenIdConnectConfigResponse`
        """
        http_info = self._create_open_id_connect_config_http_info(request)
        return self._call_api(**http_info)

    def create_open_id_connect_config_async_invoker(self, request):
        http_info = self._create_open_id_connect_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_open_id_connect_config_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-FEDERATION/identity-providers/{idp_id}/openid-connect-config",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOpenIdConnectConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_token_with_id_token_async(self, request):
        """获取联邦认证token(OpenId Connect Id token方式)

        获取联邦认证token(OpenId Connect Id token方式)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTokenWithIdToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateTokenWithIdTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateTokenWithIdTokenResponse`
        """
        http_info = self._create_token_with_id_token_http_info(request)
        return self._call_api(**http_info)

    def create_token_with_id_token_async_invoker(self, request):
        http_info = self._create_token_with_id_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_token_with_id_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-AUTH/id-token/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTokenWithIdTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_idp_id' in local_var_params:
            header_params['X-Idp-Id'] = local_var_params['x_idp_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def create_unscoped_token_with_id_token_async(self, request):
        """获取联邦认证unscoped token(OpenId Connect Id token方式)

        获取联邦认证token(OpenId Connect Id token方式)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUnscopedTokenWithIdToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateUnscopedTokenWithIdTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateUnscopedTokenWithIdTokenResponse`
        """
        http_info = self._create_unscoped_token_with_id_token_http_info(request)
        return self._call_api(**http_info)

    def create_unscoped_token_with_id_token_async_invoker(self, request):
        http_info = self._create_unscoped_token_with_id_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_unscoped_token_with_id_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}/auth",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUnscopedTokenWithIdTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

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

    def delete_agency_async(self, request):
        """删除委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除委托。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAgency
        :type request: :class:`huaweicloudsdkiam.v3.DeleteAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteAgencyResponse`
        """
        http_info = self._delete_agency_http_info(request)
        return self._call_api(**http_info)

    def delete_agency_async_invoker(self, request):
        http_info = self._delete_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-AGENCY/agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

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

    def delete_custom_policy_async(self, request):
        """删除自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.DeleteCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteCustomPolicyResponse`
        """
        http_info = self._delete_custom_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_custom_policy_async_invoker(self, request):
        http_info = self._delete_custom_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_custom_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-ROLE/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCustomPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

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

    def delete_domain_group_inherited_role_async(self, request):
        """移除用户组的所有项目服务权限

        该接口可以用于移除用户组的所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDomainGroupInheritedRole
        :type request: :class:`huaweicloudsdkiam.v3.DeleteDomainGroupInheritedRoleRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteDomainGroupInheritedRoleResponse`
        """
        http_info = self._delete_domain_group_inherited_role_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_group_inherited_role_async_invoker(self, request):
        http_info = self._delete_domain_group_inherited_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_domain_group_inherited_role_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainGroupInheritedRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_add_user_to_group_async(self, request):
        """添加IAM用户到用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)添加IAM用户到用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneAddUserToGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneAddUserToGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneAddUserToGroupResponse`
        """
        http_info = self._keystone_add_user_to_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_add_user_to_group_async_invoker(self, request):
        http_info = self._keystone_add_user_to_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_add_user_to_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/groups/{group_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneAddUserToGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_associate_group_with_domain_permission_async(self, request):
        """为用户组授予全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneAssociateGroupWithDomainPermission
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithDomainPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithDomainPermissionResponse`
        """
        http_info = self._keystone_associate_group_with_domain_permission_http_info(request)
        return self._call_api(**http_info)

    def keystone_associate_group_with_domain_permission_async_invoker(self, request):
        http_info = self._keystone_associate_group_with_domain_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_associate_group_with_domain_permission_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneAssociateGroupWithDomainPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_associate_group_with_project_permission_async(self, request):
        """为用户组授予项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneAssociateGroupWithProjectPermission
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithProjectPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneAssociateGroupWithProjectPermissionResponse`
        """
        http_info = self._keystone_associate_group_with_project_permission_http_info(request)
        return self._call_api(**http_info)

    def keystone_associate_group_with_project_permission_async_invoker(self, request):
        http_info = self._keystone_associate_group_with_project_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_associate_group_with_project_permission_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneAssociateGroupWithProjectPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_check_domain_permission_for_group_async(self, request):
        """查询用户组是否拥有全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCheckDomainPermissionForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckDomainPermissionForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckDomainPermissionForGroupResponse`
        """
        http_info = self._keystone_check_domain_permission_for_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_check_domain_permission_for_group_async_invoker(self, request):
        http_info = self._keystone_check_domain_permission_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_check_domain_permission_for_group_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCheckDomainPermissionForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_check_project_permission_for_group_async(self, request):
        """查询用户组是否拥有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCheckProjectPermissionForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckProjectPermissionForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckProjectPermissionForGroupResponse`
        """
        http_info = self._keystone_check_project_permission_for_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_check_project_permission_for_group_async_invoker(self, request):
        http_info = self._keystone_check_project_permission_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_check_project_permission_for_group_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCheckProjectPermissionForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_check_user_in_group_async(self, request):
        """查询IAM用户是否在用户组中

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户是否在用户组中。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCheckUserInGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckUserInGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckUserInGroupResponse`
        """
        http_info = self._keystone_check_user_in_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_check_user_in_group_async_invoker(self, request):
        http_info = self._keystone_check_user_in_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_check_user_in_group_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3/groups/{group_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCheckUserInGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_checkrole_for_group_async(self, request):
        """查询用户组是否拥有所有项目指定权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组是否拥有所有项目指定权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCheckroleForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCheckroleForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCheckroleForGroupResponse`
        """
        http_info = self._keystone_checkrole_for_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_checkrole_for_group_async_invoker(self, request):
        http_info = self._keystone_checkrole_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_checkrole_for_group_http_info(self, request):
        http_info = {
            "method": "HEAD",
            "resource_path": "/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCheckroleForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_create_group_async(self, request):
        """创建用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateGroupResponse`
        """
        http_info = self._keystone_create_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_group_async_invoker(self, request):
        http_info = self._keystone_create_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/groups",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def keystone_create_identity_provider_async(self, request):
        """注册身份提供商

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册身份提供商。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateIdentityProviderResponse`
        """
        http_info = self._keystone_create_identity_provider_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_identity_provider_async_invoker(self, request):
        http_info = self._keystone_create_identity_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_identity_provider_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateIdentityProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_create_mapping_async(self, request):
        """注册映射

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册映射。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateMappingResponse`
        """
        http_info = self._keystone_create_mapping_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_mapping_async_invoker(self, request):
        http_info = self._keystone_create_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_mapping_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/OS-FEDERATION/mappings/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_create_project_async(self, request):
        """创建项目

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建项目。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateProject
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateProjectResponse`
        """
        http_info = self._keystone_create_project_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_project_async_invoker(self, request):
        http_info = self._keystone_create_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_project_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/projects",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def keystone_create_protocol_async(self, request):
        """注册协议

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)注册协议（将协议关联到某一身份提供商）。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateProtocolResponse`
        """
        http_info = self._keystone_create_protocol_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_protocol_async_invoker(self, request):
        http_info = self._keystone_create_protocol_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_protocol_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateProtocolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def keystone_create_scoped_token_async(self, request):
        """获取联邦认证scoped token

        该接口可以用于通过联邦认证方式获取scoped token。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateScopedToken
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateScopedTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateScopedTokenResponse`
        """
        http_info = self._keystone_create_scoped_token_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_scoped_token_async_invoker(self, request):
        http_info = self._keystone_create_scoped_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_scoped_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/auth/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateScopedTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def keystone_delete_group_async(self, request):
        """删除用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneDeleteGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteGroupResponse`
        """
        http_info = self._keystone_delete_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_delete_group_async_invoker(self, request):
        http_info = self._keystone_delete_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_delete_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneDeleteGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

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

    def keystone_delete_identity_provider_async(self, request):
        """删除身份提供商

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html) 删除身份提供商。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneDeleteIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteIdentityProviderResponse`
        """
        http_info = self._keystone_delete_identity_provider_http_info(request)
        return self._call_api(**http_info)

    def keystone_delete_identity_provider_async_invoker(self, request):
        http_info = self._keystone_delete_identity_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_delete_identity_provider_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneDeleteIdentityProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

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

    def keystone_delete_mapping_async(self, request):
        """删除映射

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除映射。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneDeleteMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteMappingResponse`
        """
        http_info = self._keystone_delete_mapping_http_info(request)
        return self._call_api(**http_info)

    def keystone_delete_mapping_async_invoker(self, request):
        http_info = self._keystone_delete_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_delete_mapping_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/OS-FEDERATION/mappings/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneDeleteMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

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

    def keystone_delete_protocol_async(self, request):
        """删除协议

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除协议。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneDeleteProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteProtocolResponse`
        """
        http_info = self._keystone_delete_protocol_http_info(request)
        return self._call_api(**http_info)

    def keystone_delete_protocol_async_invoker(self, request):
        http_info = self._keystone_delete_protocol_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_delete_protocol_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneDeleteProtocolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_all_project_permissions_for_group_async(self, request):
        """查询用户组的所有项目权限列表

        该接口可以用于管理员查询用户组所有项目服务权限列表。 该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListAllProjectPermissionsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListAllProjectPermissionsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListAllProjectPermissionsForGroupResponse`
        """
        http_info = self._keystone_list_all_project_permissions_for_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_all_project_permissions_for_group_async_invoker(self, request):
        http_info = self._keystone_list_all_project_permissions_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_all_project_permissions_for_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListAllProjectPermissionsForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_auth_domains_async(self, request):
        """查询IAM用户可以访问的账号详情

        该接口可以用于查询IAM用户可以用访问的账号详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListAuthDomains
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListAuthDomainsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListAuthDomainsResponse`
        """
        http_info = self._keystone_list_auth_domains_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_auth_domains_async_invoker(self, request):
        http_info = self._keystone_list_auth_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_auth_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/auth/domains",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListAuthDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_list_auth_projects_async(self, request):
        """查询IAM用户可以访问的项目列表

        该接口可以用于查询IAM用户可以访问的项目列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListAuthProjects
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListAuthProjectsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListAuthProjectsResponse`
        """
        http_info = self._keystone_list_auth_projects_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_auth_projects_async_invoker(self, request):
        http_info = self._keystone_list_auth_projects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_auth_projects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/auth/projects",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListAuthProjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_list_domain_permissions_for_group_async(self, request):
        """查询全局服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的用户组权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListDomainPermissionsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListDomainPermissionsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListDomainPermissionsForGroupResponse`
        """
        http_info = self._keystone_list_domain_permissions_for_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_domain_permissions_for_group_async_invoker(self, request):
        http_info = self._keystone_list_domain_permissions_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_domain_permissions_for_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/domains/{domain_id}/groups/{group_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListDomainPermissionsForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_endpoints_async(self, request):
        """查询终端节点列表

        该接口可以用于查询终端节点列表。终端节点用来提供服务访问入口。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListEndpoints
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListEndpointsResponse`
        """
        http_info = self._keystone_list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_endpoints_async_invoker(self, request):
        http_info = self._keystone_list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_federation_domains_async(self, request):
        """查询联邦用户可以访问的账号列表

        该接口用于查询联邦用户可以访问的账号列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        &gt; - 推荐使用[查询IAM用户可以访问的账号详情](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;IAM&amp;api&#x3D;KeystoneQueryAccessibleDomainDetailsToUser)，该接口可以返回相同的响应格式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListFederationDomains
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListFederationDomainsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListFederationDomainsResponse`
        """
        http_info = self._keystone_list_federation_domains_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_federation_domains_async_invoker(self, request):
        http_info = self._keystone_list_federation_domains_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_federation_domains_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/domains",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListFederationDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_list_groups_async(self, request):
        """查询用户组列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListGroups
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsResponse`
        """
        http_info = self._keystone_list_groups_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_groups_async_invoker(self, request):
        http_info = self._keystone_list_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/groups",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_identity_providers_async(self, request):
        """查询身份提供商列表

        该接口可以用于查询身份提供商列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListIdentityProviders
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListIdentityProvidersRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListIdentityProvidersResponse`
        """
        http_info = self._keystone_list_identity_providers_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_identity_providers_async_invoker(self, request):
        http_info = self._keystone_list_identity_providers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_identity_providers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/identity_providers",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListIdentityProvidersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_list_mappings_async(self, request):
        """查询映射列表

        该接口可以用于查询映射列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListMappings
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListMappingsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListMappingsResponse`
        """
        http_info = self._keystone_list_mappings_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_mappings_async_invoker(self, request):
        http_info = self._keystone_list_mappings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_mappings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/mappings",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListMappingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_list_permissions_async(self, request):
        """查询权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListPermissions
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListPermissionsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListPermissionsResponse`
        """
        http_info = self._keystone_list_permissions_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_permissions_async_invoker(self, request):
        http_info = self._keystone_list_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/roles",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_project_permissions_for_group_async(self, request):
        """查询项目服务中的用户组权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的用户组权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListProjectPermissionsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProjectPermissionsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProjectPermissionsForGroupResponse`
        """
        http_info = self._keystone_list_project_permissions_for_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_project_permissions_for_group_async_invoker(self, request):
        http_info = self._keystone_list_project_permissions_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_project_permissions_for_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/projects/{project_id}/groups/{group_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListProjectPermissionsForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_projects_async(self, request):
        """查询指定条件下的项目列表

        该接口可以用于查询指定条件下的项目列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListProjects
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsResponse`
        """
        http_info = self._keystone_list_projects_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_projects_async_invoker(self, request):
        http_info = self._keystone_list_projects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_projects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/projects",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListProjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_list_projects_for_user_async(self, request):
        """查询指定IAM用户的项目列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的项目列表，或IAM用户查询自己的项目列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListProjectsForUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsForUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProjectsForUserResponse`
        """
        http_info = self._keystone_list_projects_for_user_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_projects_for_user_async_invoker(self, request):
        http_info = self._keystone_list_projects_for_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_projects_for_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/users/{user_id}/projects",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListProjectsForUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def keystone_list_protocols_async(self, request):
        """查询协议列表

        该接口可以用于查询协议列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListProtocols
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListProtocolsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListProtocolsResponse`
        """
        http_info = self._keystone_list_protocols_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_protocols_async_invoker(self, request):
        http_info = self._keystone_list_protocols_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_protocols_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListProtocolsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

        query_params = []

        header_params = {}

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

    def keystone_list_regions_async(self, request):
        """查询区域列表

        该接口可以用于查询区域列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListRegions
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListRegionsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListRegionsResponse`
        """
        http_info = self._keystone_list_regions_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_regions_async_invoker(self, request):
        http_info = self._keystone_list_regions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_regions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/regions",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListRegionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_list_services_async(self, request):
        """查询服务列表

        该接口可以用于查询服务列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListServices
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListServicesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListServicesResponse`
        """
        http_info = self._keystone_list_services_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_services_async_invoker(self, request):
        http_info = self._keystone_list_services_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_services_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/services",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListServicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

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

    def keystone_list_users_for_group_by_admin_async(self, request):
        """管理员查询用户组所包含的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组中所包含的IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListUsersForGroupByAdmin
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListUsersForGroupByAdminRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListUsersForGroupByAdminResponse`
        """
        http_info = self._keystone_list_users_for_group_by_admin_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_users_for_group_by_admin_async_invoker(self, request):
        http_info = self._keystone_list_users_for_group_by_admin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_users_for_group_by_admin_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/groups/{group_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListUsersForGroupByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

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

    def keystone_list_versions_async(self, request):
        """查询版本信息列表

        该接口用于查询Keystone API的版本信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListVersions
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListVersionsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListVersionsResponse`
        """
        http_info = self._keystone_list_versions_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_versions_async_invoker(self, request):
        http_info = self._keystone_list_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_remove_domain_permission_from_group_async(self, request):
        """移除用户组的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneRemoveDomainPermissionFromGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneRemoveDomainPermissionFromGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneRemoveDomainPermissionFromGroupResponse`
        """
        http_info = self._keystone_remove_domain_permission_from_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_remove_domain_permission_from_group_async_invoker(self, request):
        http_info = self._keystone_remove_domain_permission_from_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_remove_domain_permission_from_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/domains/{domain_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneRemoveDomainPermissionFromGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_remove_project_permission_from_group_async(self, request):
        """移除用户组的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组的项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneRemoveProjectPermissionFromGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneRemoveProjectPermissionFromGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneRemoveProjectPermissionFromGroupResponse`
        """
        http_info = self._keystone_remove_project_permission_from_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_remove_project_permission_from_group_async_invoker(self, request):
        http_info = self._keystone_remove_project_permission_from_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_remove_project_permission_from_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/projects/{project_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneRemoveProjectPermissionFromGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_remove_user_from_group_async(self, request):
        """移除用户组中的IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除用户组中的IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneRemoveUserFromGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneRemoveUserFromGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneRemoveUserFromGroupResponse`
        """
        http_info = self._keystone_remove_user_from_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_remove_user_from_group_async_invoker(self, request):
        http_info = self._keystone_remove_user_from_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_remove_user_from_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/groups/{group_id}/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneRemoveUserFromGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_show_catalog_async(self, request):
        """查询服务目录

        该接口可以用于查询请求头中X-Auth-Token对应的服务目录。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowCatalog
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowCatalogRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowCatalogResponse`
        """
        http_info = self._keystone_show_catalog_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_catalog_async_invoker(self, request):
        http_info = self._keystone_show_catalog_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_catalog_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/auth/catalog",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowCatalogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_show_endpoint_async(self, request):
        """查询终端节点详情

        该接口可以用于查询终端节点详情。终端节点用来提供服务访问入口。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowEndpoint
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowEndpointRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowEndpointResponse`
        """
        http_info = self._keystone_show_endpoint_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_endpoint_async_invoker(self, request):
        http_info = self._keystone_show_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_endpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

        query_params = []

        header_params = {}

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

    def keystone_show_group_async(self, request):
        """查询用户组详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询用户组详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowGroupResponse`
        """
        http_info = self._keystone_show_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_group_async_invoker(self, request):
        http_info = self._keystone_show_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

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

    def keystone_show_identity_provider_async(self, request):
        """查询身份提供商详情

        该接口可以用于查询身份提供商详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowIdentityProviderResponse`
        """
        http_info = self._keystone_show_identity_provider_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_identity_provider_async_invoker(self, request):
        http_info = self._keystone_show_identity_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_identity_provider_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowIdentityProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

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

    def keystone_show_mapping_async(self, request):
        """查询映射详情

        该接口可以用于查询映射详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowMappingResponse`
        """
        http_info = self._keystone_show_mapping_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_mapping_async_invoker(self, request):
        http_info = self._keystone_show_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_mapping_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/mappings/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []

        header_params = {}

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

    def keystone_show_permission_async(self, request):
        """查询权限详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询权限详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowPermission
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowPermissionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowPermissionResponse`
        """
        http_info = self._keystone_show_permission_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_permission_async_invoker(self, request):
        http_info = self._keystone_show_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

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

    def keystone_show_project_async(self, request):
        """查询项目详情

        该接口可以用于查询项目详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowProject
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowProjectResponse`
        """
        http_info = self._keystone_show_project_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_project_async_invoker(self, request):
        http_info = self._keystone_show_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

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

    def keystone_show_protocol_async(self, request):
        """查询协议详情

        该接口可以用于查询协议详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowProtocolResponse`
        """
        http_info = self._keystone_show_protocol_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_protocol_async_invoker(self, request):
        http_info = self._keystone_show_protocol_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_protocol_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowProtocolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_show_region_async(self, request):
        """查询区域详情

        该接口可以用于查询区域详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowRegion
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowRegionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowRegionResponse`
        """
        http_info = self._keystone_show_region_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_region_async_invoker(self, request):
        http_info = self._keystone_show_region_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_region_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/regions/{region_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowRegionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

        query_params = []

        header_params = {}

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

    def keystone_show_security_compliance_async(self, request):
        """查询账号密码强度策略

        该接口可以用于查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowSecurityCompliance
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceResponse`
        """
        http_info = self._keystone_show_security_compliance_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_security_compliance_async_invoker(self, request):
        http_info = self._keystone_show_security_compliance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_security_compliance_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/domains/{domain_id}/config/security_compliance",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowSecurityComplianceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

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

    def keystone_show_security_compliance_by_option_async(self, request):
        """按条件查询账号密码强度策略

        该接口可以用于按条件查询账号密码强度策略，查询结果包括密码强度策略的正则表达式及其描述。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowSecurityComplianceByOption
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceByOptionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowSecurityComplianceByOptionResponse`
        """
        http_info = self._keystone_show_security_compliance_by_option_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_security_compliance_by_option_async_invoker(self, request):
        http_info = self._keystone_show_security_compliance_by_option_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_security_compliance_by_option_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/domains/{domain_id}/config/security_compliance/{option}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowSecurityComplianceByOptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_show_service_async(self, request):
        """查询服务详情

        该接口可以用于查询服务详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowService
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowServiceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowServiceResponse`
        """
        http_info = self._keystone_show_service_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_service_async_invoker(self, request):
        http_info = self._keystone_show_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_service_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

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

    def keystone_show_version_async(self, request):
        """查询版本信息

        该接口用于查询Keystone API的3.0版本的信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowVersion
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowVersionRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowVersionResponse`
        """
        http_info = self._keystone_show_version_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_version_async_invoker(self, request):
        http_info = self._keystone_show_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def keystone_update_group_async(self, request):
        """更新用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新用户组信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateGroup
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateGroupResponse`
        """
        http_info = self._keystone_update_group_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_group_async_invoker(self, request):
        http_info = self._keystone_update_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_group_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_update_identity_provider_async(self, request):
        """更新身份提供商

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新身份提供商。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateIdentityProvider
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateIdentityProviderRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateIdentityProviderResponse`
        """
        http_info = self._keystone_update_identity_provider_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_identity_provider_async_invoker(self, request):
        http_info = self._keystone_update_identity_provider_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_identity_provider_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateIdentityProviderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_update_mapping_async(self, request):
        """更新映射

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新映射。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateMapping
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateMappingRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateMappingResponse`
        """
        http_info = self._keystone_update_mapping_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_mapping_async_invoker(self, request):
        http_info = self._keystone_update_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_mapping_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3/OS-FEDERATION/mappings/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateMappingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_update_project_async(self, request):
        """修改项目信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改项目信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateProject
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProjectResponse`
        """
        http_info = self._keystone_update_project_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_project_async_invoker(self, request):
        http_info = self._keystone_update_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_project_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_update_protocol_async(self, request):
        """更新协议

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)更新协议。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateProtocol
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProtocolRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateProtocolResponse`
        """
        http_info = self._keystone_update_protocol_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_protocol_async_invoker(self, request):
        http_info = self._keystone_update_protocol_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_protocol_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateProtocolResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def list_agencies_async(self, request):
        """查询指定条件下的委托列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定条件下的委托列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkiam.v3.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListAgenciesResponse`
        """
        http_info = self._list_agencies_http_info(request)
        return self._call_api(**http_info)

    def list_agencies_async_invoker(self, request):
        http_info = self._list_agencies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agencies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-AGENCY/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgenciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_all_projects_permissions_for_agency_async(self, request):
        """查询委托下的所有项目服务权限列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托所有项目服务权限列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAllProjectsPermissionsForAgency
        :type request: :class:`huaweicloudsdkiam.v3.ListAllProjectsPermissionsForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListAllProjectsPermissionsForAgencyResponse`
        """
        http_info = self._list_all_projects_permissions_for_agency_http_info(request)
        return self._call_api(**http_info)

    def list_all_projects_permissions_for_agency_async_invoker(self, request):
        http_info = self._list_all_projects_permissions_for_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_all_projects_permissions_for_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllProjectsPermissionsForAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_custom_policies_async(self, request):
        """查询自定义策略列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCustomPolicies
        :type request: :class:`huaweicloudsdkiam.v3.ListCustomPoliciesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListCustomPoliciesResponse`
        """
        http_info = self._list_custom_policies_http_info(request)
        return self._call_api(**http_info)

    def list_custom_policies_async_invoker(self, request):
        http_info = self._list_custom_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_custom_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-ROLE/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListCustomPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_domain_permissions_for_agency_async(self, request):
        """查询全局服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询全局服务中的委托权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDomainPermissionsForAgency
        :type request: :class:`huaweicloudsdkiam.v3.ListDomainPermissionsForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListDomainPermissionsForAgencyResponse`
        """
        http_info = self._list_domain_permissions_for_agency_http_info(request)
        return self._call_api(**http_info)

    def list_domain_permissions_for_agency_async_invoker(self, request):
        http_info = self._list_domain_permissions_for_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_domain_permissions_for_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainPermissionsForAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_enterprise_projects_for_group_async(self, request):
        """查询用户组关联的企业项目

        该接口可用于查询用户组所关联的企业项目。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnterpriseProjectsForGroup
        :type request: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForGroupRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForGroupResponse`
        """
        http_info = self._list_enterprise_projects_for_group_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_projects_for_group_async_invoker(self, request):
        http_info = self._list_enterprise_projects_for_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_enterprise_projects_for_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/groups/{group_id}/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseProjectsForGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}

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

    def list_enterprise_projects_for_user_async(self, request):
        """查询用户关联的企业项目

        该接口可用于查询用户所关联的企业项目。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEnterpriseProjectsForUser
        :type request: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListEnterpriseProjectsForUserResponse`
        """
        http_info = self._list_enterprise_projects_for_user_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_projects_for_user_async_invoker(self, request):
        http_info = self._list_enterprise_projects_for_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_enterprise_projects_for_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/users/{user_id}/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseProjectsForUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def list_groups_for_enterprise_project_async(self, request):
        """查询企业项目关联的用户组

        该接口可用于查询企业项目关联的用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupsForEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListGroupsForEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListGroupsForEnterpriseProjectResponse`
        """
        http_info = self._list_groups_for_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def list_groups_for_enterprise_project_async_invoker(self, request):
        http_info = self._list_groups_for_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_groups_for_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsForEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

        query_params = []

        header_params = {}

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

    def list_project_permissions_for_agency_async(self, request):
        """查询项目服务中的委托权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目服务中的委托权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectPermissionsForAgency
        :type request: :class:`huaweicloudsdkiam.v3.ListProjectPermissionsForAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListProjectPermissionsForAgencyResponse`
        """
        http_info = self._list_project_permissions_for_agency_http_info(request)
        return self._call_api(**http_info)

    def list_project_permissions_for_agency_async_invoker(self, request):
        http_info = self._list_project_permissions_for_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_permissions_for_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectPermissionsForAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_roles_for_group_on_enterprise_project_async(self, request):
        """查询企业项目已关联用户组的权限

        该接口可用于查询企业项目已关联用户组的权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRolesForGroupOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListRolesForGroupOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListRolesForGroupOnEnterpriseProjectResponse`
        """
        http_info = self._list_roles_for_group_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def list_roles_for_group_on_enterprise_project_async_invoker(self, request):
        http_info = self._list_roles_for_group_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_roles_for_group_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups/{group_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListRolesForGroupOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_roles_for_user_on_enterprise_project_async(self, request):
        """查询企业项目直接关联用户的权限

        该接口可用于查询企业项目直接关联用户的权限。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRolesForUserOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListRolesForUserOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListRolesForUserOnEnterpriseProjectResponse`
        """
        http_info = self._list_roles_for_user_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def list_roles_for_user_on_enterprise_project_async_invoker(self, request):
        http_info = self._list_roles_for_user_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_roles_for_user_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users/{user_id}/roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListRolesForUserOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_users_for_enterprise_project_async(self, request):
        """查询企业项目直接关联用户

        该接口可用于查询企业项目直接关联的用户。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsersForEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.ListUsersForEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListUsersForEnterpriseProjectResponse`
        """
        http_info = self._list_users_for_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def list_users_for_enterprise_project_async_invoker(self, request):
        http_info = self._list_users_for_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_for_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersForEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'enterprise_project_id' in local_var_params:
            path_params['enterprise_project_id'] = local_var_params['enterprise_project_id']

        query_params = []

        header_params = {}

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

    def remove_all_projects_permission_from_agency_async(self, request):
        """移除委托下的所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveAllProjectsPermissionFromAgency
        :type request: :class:`huaweicloudsdkiam.v3.RemoveAllProjectsPermissionFromAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RemoveAllProjectsPermissionFromAgencyResponse`
        """
        http_info = self._remove_all_projects_permission_from_agency_http_info(request)
        return self._call_api(**http_info)

    def remove_all_projects_permission_from_agency_async_invoker(self, request):
        http_info = self._remove_all_projects_permission_from_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_all_projects_permission_from_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-INHERIT/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveAllProjectsPermissionFromAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def remove_domain_permission_from_agency_async(self, request):
        """移除委托的全局服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的全局服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveDomainPermissionFromAgency
        :type request: :class:`huaweicloudsdkiam.v3.RemoveDomainPermissionFromAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RemoveDomainPermissionFromAgencyResponse`
        """
        http_info = self._remove_domain_permission_from_agency_http_info(request)
        return self._call_api(**http_info)

    def remove_domain_permission_from_agency_async_invoker(self, request):
        http_info = self._remove_domain_permission_from_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_domain_permission_from_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-AGENCY/domains/{domain_id}/agencies/{agency_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveDomainPermissionFromAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def remove_project_permission_from_agency_async(self, request):
        """移除委托的项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)移除委托的项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveProjectPermissionFromAgency
        :type request: :class:`huaweicloudsdkiam.v3.RemoveProjectPermissionFromAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RemoveProjectPermissionFromAgencyResponse`
        """
        http_info = self._remove_project_permission_from_agency_http_info(request)
        return self._call_api(**http_info)

    def remove_project_permission_from_agency_async_invoker(self, request):
        http_info = self._remove_project_permission_from_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_project_permission_from_agency_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-AGENCY/projects/{project_id}/agencies/{agency_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveProjectPermissionFromAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def revoke_role_from_agency_on_enterprise_project_async(self, request):
        """revoke_role_from_agency_on_enterprise_project

        该接口可以删除企业项目委托上的授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokeRoleFromAgencyOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.RevokeRoleFromAgencyOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RevokeRoleFromAgencyOnEnterpriseProjectResponse`
        """
        http_info = self._revoke_role_from_agency_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def revoke_role_from_agency_on_enterprise_project_async_invoker(self, request):
        http_info = self._revoke_role_from_agency_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_role_from_agency_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-PERMISSION/subjects/agency/scopes/enterprise-project/role-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeRoleFromAgencyOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def revoke_role_from_group_on_enterprise_project_async(self, request):
        """删除企业项目关联用户组的权限

        该接口用于删除企业项目关联用户组的权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokeRoleFromGroupOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.RevokeRoleFromGroupOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RevokeRoleFromGroupOnEnterpriseProjectResponse`
        """
        http_info = self._revoke_role_from_group_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def revoke_role_from_group_on_enterprise_project_async_invoker(self, request):
        http_info = self._revoke_role_from_group_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_role_from_group_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/groups/{group_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeRoleFromGroupOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def revoke_role_from_user_on_enterprise_project_async(self, request):
        """删除企业项目直接关联用户的权限

        删除企业项目直接关联用户的权限。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokeRoleFromUserOnEnterpriseProject
        :type request: :class:`huaweicloudsdkiam.v3.RevokeRoleFromUserOnEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.RevokeRoleFromUserOnEnterpriseProjectResponse`
        """
        http_info = self._revoke_role_from_user_on_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def revoke_role_from_user_on_enterprise_project_async_invoker(self, request):
        http_info = self._revoke_role_from_user_on_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_role_from_user_on_enterprise_project_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-PERMISSION/enterprise-projects/{enterprise_project_id}/users/{user_id}/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeRoleFromUserOnEnterpriseProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_agency_async(self, request):
        """查询委托详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询委托详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAgency
        :type request: :class:`huaweicloudsdkiam.v3.ShowAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowAgencyResponse`
        """
        http_info = self._show_agency_http_info(request)
        return self._call_api(**http_info)

    def show_agency_async_invoker(self, request):
        http_info = self._show_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_agency_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-AGENCY/agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

        query_params = []

        header_params = {}

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

    def show_custom_policy_async(self, request):
        """查询自定义策略详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询自定义策略详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowCustomPolicyResponse`
        """
        http_info = self._show_custom_policy_http_info(request)
        return self._call_api(**http_info)

    def show_custom_policy_async_invoker(self, request):
        http_info = self._show_custom_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_custom_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-ROLE/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCustomPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

        query_params = []

        header_params = {}

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

    def show_domain_api_acl_policy_async(self, request):
        """查询账号接口访问策略

        该接口可以用于查询账号接口访问控制策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainApiAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainApiAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainApiAclPolicyResponse`
        """
        http_info = self._show_domain_api_acl_policy_http_info(request)
        return self._call_api(**http_info)

    def show_domain_api_acl_policy_async_invoker(self, request):
        http_info = self._show_domain_api_acl_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_api_acl_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/api-acl-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainApiAclPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

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

    def show_domain_console_acl_policy_async(self, request):
        """查询账号控制台访问策略

        该接口可以用于查询账号控制台访问控制策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainConsoleAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainConsoleAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainConsoleAclPolicyResponse`
        """
        http_info = self._show_domain_console_acl_policy_http_info(request)
        return self._call_api(**http_info)

    def show_domain_console_acl_policy_async_invoker(self, request):
        http_info = self._show_domain_console_acl_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_console_acl_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/console-acl-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainConsoleAclPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

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

    def show_domain_login_policy_async(self, request):
        """查询账号登录策略

        该接口可以用于查询账号登录策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainLoginPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainLoginPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainLoginPolicyResponse`
        """
        http_info = self._show_domain_login_policy_http_info(request)
        return self._call_api(**http_info)

    def show_domain_login_policy_async_invoker(self, request):
        http_info = self._show_domain_login_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_login_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/login-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainLoginPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

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

    def show_domain_password_policy_async(self, request):
        """查询账号密码策略

        该接口可以用于查询账号密码策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainPasswordPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainPasswordPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainPasswordPolicyResponse`
        """
        http_info = self._show_domain_password_policy_http_info(request)
        return self._call_api(**http_info)

    def show_domain_password_policy_async_invoker(self, request):
        http_info = self._show_domain_password_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_password_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/password-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainPasswordPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

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

    def show_domain_protect_policy_async(self, request):
        """查询账号操作保护策略

        该接口可以用于查询账号操作保护策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainProtectPolicy
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainProtectPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainProtectPolicyResponse`
        """
        http_info = self._show_domain_protect_policy_http_info(request)
        return self._call_api(**http_info)

    def show_domain_protect_policy_async_invoker(self, request):
        http_info = self._show_domain_protect_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_protect_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/protect-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainProtectPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

        query_params = []

        header_params = {}

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

    def show_domain_quota_async(self, request):
        """查询账号配额

        该接口可以用于查询账号配额。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainQuota
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainQuotaRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainQuotaResponse`
        """
        http_info = self._show_domain_quota_http_info(request)
        return self._call_api(**http_info)

    def show_domain_quota_async_invoker(self, request):
        http_info = self._show_domain_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-QUOTA/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_domain_role_assignments_async(self, request):
        """查询指定账号中的授权记录

        该接口用于查询指定账号中的授权记录。
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainRoleAssignments
        :type request: :class:`huaweicloudsdkiam.v3.ShowDomainRoleAssignmentsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowDomainRoleAssignmentsResponse`
        """
        http_info = self._show_domain_role_assignments_http_info(request)
        return self._call_api(**http_info)

    def show_domain_role_assignments_async_invoker(self, request):
        http_info = self._show_domain_role_assignments_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_domain_role_assignments_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-PERMISSION/role-assignments",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainRoleAssignmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_metadata_async(self, request):
        """查询Metadata文件

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询身份提供商导入到IAM中的Metadata文件。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMetadata
        :type request: :class:`huaweicloudsdkiam.v3.ShowMetadataRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowMetadataResponse`
        """
        http_info = self._show_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_metadata_async_invoker(self, request):
        http_info = self._show_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_metadata_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3-ext/OS-FEDERATION/identity_providers/{idp_id}/protocols/{protocol_id}/metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_open_id_connect_config_async(self, request):
        """查询OpenId Connect身份提供商配置

        查询OpenId Connect身份提供商配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOpenIdConnectConfig
        :type request: :class:`huaweicloudsdkiam.v3.ShowOpenIdConnectConfigRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowOpenIdConnectConfigResponse`
        """
        http_info = self._show_open_id_connect_config_http_info(request)
        return self._call_api(**http_info)

    def show_open_id_connect_config_async_invoker(self, request):
        http_info = self._show_open_id_connect_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_open_id_connect_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-FEDERATION/identity-providers/{idp_id}/openid-connect-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpenIdConnectConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

        query_params = []

        header_params = {}

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

    def show_project_details_and_status_async(self, request):
        """查询项目详情与状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询项目详情与状态。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectDetailsAndStatus
        :type request: :class:`huaweicloudsdkiam.v3.ShowProjectDetailsAndStatusRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowProjectDetailsAndStatusResponse`
        """
        http_info = self._show_project_details_and_status_http_info(request)
        return self._call_api(**http_info)

    def show_project_details_and_status_async_invoker(self, request):
        http_info = self._show_project_details_and_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_details_and_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3-ext/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectDetailsAndStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

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

    def show_project_quota_async(self, request):
        """查询项目配额

        该接口可以用于查询项目配额。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectQuota
        :type request: :class:`huaweicloudsdkiam.v3.ShowProjectQuotaRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowProjectQuotaResponse`
        """
        http_info = self._show_project_quota_http_info(request)
        return self._call_api(**http_info)

    def show_project_quota_async_invoker(self, request):
        http_info = self._show_project_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-QUOTA/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectQuotaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}

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

    def update_agency_async(self, request):
        """修改委托

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAgency
        :type request: :class:`huaweicloudsdkiam.v3.UpdateAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateAgencyResponse`
        """
        http_info = self._update_agency_http_info(request)
        return self._call_api(**http_info)

    def update_agency_async_invoker(self, request):
        http_info = self._update_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_agency_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-AGENCY/agencies/{agency_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agency_id' in local_var_params:
            path_params['agency_id'] = local_var_params['agency_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_agency_custom_policy_async(self, request):
        """修改委托自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改委托自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAgencyCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateAgencyCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateAgencyCustomPolicyResponse`
        """
        http_info = self._update_agency_custom_policy_http_info(request)
        return self._call_api(**http_info)

    def update_agency_custom_policy_async_invoker(self, request):
        http_info = self._update_agency_custom_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_agency_custom_policy_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3.0/OS-ROLE/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgencyCustomPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_cloud_service_custom_policy_async(self, request):
        """修改云服务自定义策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改云服务自定义策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCloudServiceCustomPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateCloudServiceCustomPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateCloudServiceCustomPolicyResponse`
        """
        http_info = self._update_cloud_service_custom_policy_http_info(request)
        return self._call_api(**http_info)

    def update_cloud_service_custom_policy_async_invoker(self, request):
        http_info = self._update_cloud_service_custom_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_cloud_service_custom_policy_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3.0/OS-ROLE/roles/{role_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCloudServiceCustomPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'role_id' in local_var_params:
            path_params['role_id'] = local_var_params['role_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_domain_api_acl_policy_async(self, request):
        """修改账号接口访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号接口访问策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainApiAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainApiAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainApiAclPolicyResponse`
        """
        http_info = self._update_domain_api_acl_policy_http_info(request)
        return self._call_api(**http_info)

    def update_domain_api_acl_policy_async_invoker(self, request):
        http_info = self._update_domain_api_acl_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_api_acl_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/api-acl-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainApiAclPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_domain_console_acl_policy_async(self, request):
        """修改账号控制台访问策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号控制台访问策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainConsoleAclPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainConsoleAclPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainConsoleAclPolicyResponse`
        """
        http_info = self._update_domain_console_acl_policy_http_info(request)
        return self._call_api(**http_info)

    def update_domain_console_acl_policy_async_invoker(self, request):
        http_info = self._update_domain_console_acl_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_console_acl_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/console-acl-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainConsoleAclPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_domain_group_inherit_role_async(self, request):
        """为用户组授予所有项目服务权限

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)为用户组授予所有项目服务权限。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainGroupInheritRole
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainGroupInheritRoleRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainGroupInheritRoleResponse`
        """
        http_info = self._update_domain_group_inherit_role_http_info(request)
        return self._call_api(**http_info)

    def update_domain_group_inherit_role_async_invoker(self, request):
        http_info = self._update_domain_group_inherit_role_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_group_inherit_role_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/OS-INHERIT/domains/{domain_id}/groups/{group_id}/roles/{role_id}/inherited_to_projects",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainGroupInheritRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_domain_login_policy_async(self, request):
        """修改账号登录策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号登录策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainLoginPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainLoginPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainLoginPolicyResponse`
        """
        http_info = self._update_domain_login_policy_http_info(request)
        return self._call_api(**http_info)

    def update_domain_login_policy_async_invoker(self, request):
        http_info = self._update_domain_login_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_login_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/login-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainLoginPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_domain_password_policy_async(self, request):
        """修改账号密码策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号密码策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainPasswordPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainPasswordPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainPasswordPolicyResponse`
        """
        http_info = self._update_domain_password_policy_http_info(request)
        return self._call_api(**http_info)

    def update_domain_password_policy_async_invoker(self, request):
        http_info = self._update_domain_password_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_password_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/password-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainPasswordPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_domain_protect_policy_async(self, request):
        """修改账号操作保护策略

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护策略。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDomainProtectPolicy
        :type request: :class:`huaweicloudsdkiam.v3.UpdateDomainProtectPolicyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateDomainProtectPolicyResponse`
        """
        http_info = self._update_domain_protect_policy_http_info(request)
        return self._call_api(**http_info)

    def update_domain_protect_policy_async_invoker(self, request):
        http_info = self._update_domain_protect_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_domain_protect_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-SECURITYPOLICY/domains/{domain_id}/protect-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainProtectPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_open_id_connect_config_async(self, request):
        """修改OpenId Connect身份提供商配置

        修改OpenId Connect身份提供商配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateOpenIdConnectConfig
        :type request: :class:`huaweicloudsdkiam.v3.UpdateOpenIdConnectConfigRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateOpenIdConnectConfigResponse`
        """
        http_info = self._update_open_id_connect_config_http_info(request)
        return self._call_api(**http_info)

    def update_open_id_connect_config_async_invoker(self, request):
        http_info = self._update_open_id_connect_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_open_id_connect_config_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-FEDERATION/identity-providers/{idp_id}/openid-connect-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateOpenIdConnectConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'idp_id' in local_var_params:
            path_params['idp_id'] = local_var_params['idp_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_project_status_async(self, request):
        """设置项目状态

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)设置项目状态。项目状态包括：正常、冻结。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectStatus
        :type request: :class:`huaweicloudsdkiam.v3.UpdateProjectStatusRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateProjectStatusResponse`
        """
        http_info = self._update_project_status_http_info(request)
        return self._call_api(**http_info)

    def update_project_status_async_invoker(self, request):
        http_info = self._update_project_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_status_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3-ext/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            ['application/json;charset=UTF-8'])

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

    def create_permanent_access_key_async(self, request):
        """创建永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)给IAM用户创建永久访问密钥，或IAM用户给自己创建永久访问密钥。
        
        访问密钥（Access Key ID/Secret Access Key，简称AK/SK），是您通过开发工具（API、CLI、SDK）访问华为云时的身份凭证，不用于登录控制台。系统通过AK识别访问用户的身份，通过SK进行签名验证，通过加密签名验证可以确保请求的机密性、完整性和请求者身份的正确性。在控制台创建访问密钥的方式请参见：[访问密钥](https://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606340.html) 。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.CreatePermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreatePermanentAccessKeyResponse`
        """
        http_info = self._create_permanent_access_key_http_info(request)
        return self._call_api(**http_info)

    def create_permanent_access_key_async_invoker(self, request):
        http_info = self._create_permanent_access_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_permanent_access_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-CREDENTIAL/credentials",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePermanentAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_temporary_access_key_by_agency_async(self, request):
        """通过委托获取临时访问密钥

        该接口可以用于通过委托来获取临时访问密钥（临时AK/SK）和securitytoken。
        
        临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html) 。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemporaryAccessKeyByAgency
        :type request: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByAgencyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByAgencyResponse`
        """
        http_info = self._create_temporary_access_key_by_agency_http_info(request)
        return self._call_api(**http_info)

    def create_temporary_access_key_by_agency_async_invoker(self, request):
        http_info = self._create_temporary_access_key_by_agency_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_temporary_access_key_by_agency_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-CREDENTIAL/securitytokens",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemporaryAccessKeyByAgencyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_temporary_access_key_by_token_async(self, request):
        """通过token获取临时访问密钥

        该接口可以用于通过token来获取临时AK/SK和securitytoken。
        
        临时AK/SK和securitytoken是系统颁发给IAM用户的临时访问令牌，有效期为15分钟至24小时，过期后需要重新获取。临时AK/SK和securitytoken遵循权限最小化原则。鉴权时，临时AK/SK和securitytoken必须同时使用，请求头中需要添加“x-security-token”字段，使用方法详情请参考：[API签名参考](https://support.huaweicloud.com/devg-apisign/api-sign-provide.html)。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemporaryAccessKeyByToken
        :type request: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateTemporaryAccessKeyByTokenResponse`
        """
        http_info = self._create_temporary_access_key_by_token_http_info(request)
        return self._call_api(**http_info)

    def create_temporary_access_key_by_token_async_invoker(self, request):
        http_info = self._create_temporary_access_key_by_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_temporary_access_key_by_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-CREDENTIAL/securitytokens",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemporaryAccessKeyByTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def delete_permanent_access_key_async(self, request):
        """删除指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除IAM用户的指定永久访问密钥，或IAM用户删除自己的指定永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.DeletePermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeletePermanentAccessKeyResponse`
        """
        http_info = self._delete_permanent_access_key_http_info(request)
        return self._call_api(**http_info)

    def delete_permanent_access_key_async_invoker(self, request):
        http_info = self._delete_permanent_access_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_permanent_access_key_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-CREDENTIAL/credentials/{access_key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePermanentAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key' in local_var_params:
            path_params['access_key'] = local_var_params['access_key']

        query_params = []

        header_params = {}

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

    def list_permanent_access_keys_async(self, request):
        """查询所有永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的所有永久访问密钥，或IAM用户查询自己的所有永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermanentAccessKeys
        :type request: :class:`huaweicloudsdkiam.v3.ListPermanentAccessKeysRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListPermanentAccessKeysResponse`
        """
        http_info = self._list_permanent_access_keys_http_info(request)
        return self._call_api(**http_info)

    def list_permanent_access_keys_async_invoker(self, request):
        http_info = self._list_permanent_access_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_permanent_access_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-CREDENTIAL/credentials",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermanentAccessKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))

        header_params = {}

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

    def show_permanent_access_key_async(self, request):
        """查询指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的指定永久访问密钥，或IAM用户查询自己的指定永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.ShowPermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowPermanentAccessKeyResponse`
        """
        http_info = self._show_permanent_access_key_http_info(request)
        return self._call_api(**http_info)

    def show_permanent_access_key_async_invoker(self, request):
        http_info = self._show_permanent_access_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_permanent_access_key_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-CREDENTIAL/credentials/{access_key}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPermanentAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key' in local_var_params:
            path_params['access_key'] = local_var_params['access_key']

        query_params = []

        header_params = {}

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

    def update_permanent_access_key_async(self, request):
        """修改指定永久访问密钥

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户的指定永久访问密钥，或IAM用户修改自己的指定永久访问密钥。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePermanentAccessKey
        :type request: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyResponse`
        """
        http_info = self._update_permanent_access_key_http_info(request)
        return self._call_api(**http_info)

    def update_permanent_access_key_async_invoker(self, request):
        http_info = self._update_permanent_access_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_permanent_access_key_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-CREDENTIAL/credentials/{access_key}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePermanentAccessKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'access_key' in local_var_params:
            path_params['access_key'] = local_var_params['access_key']

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
            ['application/json;charset=UTF-8'])

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

    def create_binding_device_async(self, request):
        """绑定MFA设备

        该接口可以用于绑定MFA设备。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBindingDevice
        :type request: :class:`huaweicloudsdkiam.v3.CreateBindingDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateBindingDeviceResponse`
        """
        http_info = self._create_binding_device_http_info(request)
        return self._call_api(**http_info)

    def create_binding_device_async_invoker(self, request):
        http_info = self._create_binding_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_binding_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-MFA/mfa-devices/bind",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBindingDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_mfa_device_async(self, request):
        """创建MFA设备

        该接口可以用于创建MFA设备。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMfaDevice
        :type request: :class:`huaweicloudsdkiam.v3.CreateMfaDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateMfaDeviceResponse`
        """
        http_info = self._create_mfa_device_http_info(request)
        return self._call_api(**http_info)

    def create_mfa_device_async_invoker(self, request):
        http_info = self._create_mfa_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_mfa_device_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-MFA/virtual-mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMfaDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def create_user_async(self, request):
        """管理员创建IAM用户（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkiam.v3.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.CreateUserResponse`
        """
        http_info = self._create_user_http_info(request)
        return self._call_api(**http_info)

    def create_user_async_invoker(self, request):
        http_info = self._create_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.0/OS-USER/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def delete_binding_device_async(self, request):
        """解绑MFA设备

        该接口可以用于解绑MFA设备
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBindingDevice
        :type request: :class:`huaweicloudsdkiam.v3.DeleteBindingDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteBindingDeviceResponse`
        """
        http_info = self._delete_binding_device_http_info(request)
        return self._call_api(**http_info)

    def delete_binding_device_async_invoker(self, request):
        http_info = self._delete_binding_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_binding_device_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-MFA/mfa-devices/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBindingDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def delete_mfa_device_async(self, request):
        """删除MFA设备

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除MFA设备。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMfaDevice
        :type request: :class:`huaweicloudsdkiam.v3.DeleteMfaDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.DeleteMfaDeviceResponse`
        """
        http_info = self._delete_mfa_device_http_info(request)
        return self._call_api(**http_info)

    def delete_mfa_device_async_invoker(self, request):
        http_info = self._delete_mfa_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_mfa_device_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.0/OS-MFA/virtual-mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMfaDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_create_user_async(self, request):
        """管理员创建IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)创建IAM用户。IAM用户首次登录时需要修改密码。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneCreateUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneCreateUserResponse`
        """
        http_info = self._keystone_create_user_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_user_async_invoker(self, request):
        http_info = self._keystone_create_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/users",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            ['application/json;charset=UTF-8'])

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

    def keystone_delete_user_async(self, request):
        """管理员删除IAM用户

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)删除指定IAM用户。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneDeleteUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneDeleteUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneDeleteUserResponse`
        """
        http_info = self._keystone_delete_user_http_info(request)
        return self._call_api(**http_info)

    def keystone_delete_user_async_invoker(self, request):
        http_info = self._keystone_delete_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_delete_user_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneDeleteUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def keystone_list_groups_for_user_async(self, request):
        """查询IAM用户所属用户组

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户所属用户组，或IAM用户查询自己所属用户组。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListGroupsForUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsForUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListGroupsForUserResponse`
        """
        http_info = self._keystone_list_groups_for_user_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_groups_for_user_async_invoker(self, request):
        http_info = self._keystone_list_groups_for_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_groups_for_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/users/{user_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListGroupsForUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def keystone_list_users_async(self, request):
        """管理员查询IAM用户列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneListUsers
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneListUsersRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneListUsersResponse`
        """
        http_info = self._keystone_list_users_http_info(request)
        return self._call_api(**http_info)

    def keystone_list_users_async_invoker(self, request):
        http_info = self._keystone_list_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_list_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/users",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneListUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def keystone_show_user_async(self, request):
        """查询IAM用户详情

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的用户详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneShowUser
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneShowUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneShowUserResponse`
        """
        http_info = self._keystone_show_user_http_info(request)
        return self._call_api(**http_info)

    def keystone_show_user_async_invoker(self, request):
        http_info = self._keystone_show_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_show_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneShowUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def keystone_update_user_by_admin_async(self, request):
        """管理员修改IAM用户信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateUserByAdmin
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserByAdminRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserByAdminResponse`
        """
        http_info = self._keystone_update_user_by_admin_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_user_by_admin_async_invoker(self, request):
        http_info = self._keystone_update_user_by_admin_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_user_by_admin_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v3/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateUserByAdminResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_update_user_password_async(self, request):
        """修改IAM用户密码

        该接口可以用于IAM用户修改自己的密码。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneUpdateUserPassword
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneUpdateUserPasswordResponse`
        """
        http_info = self._keystone_update_user_password_http_info(request)
        return self._call_api(**http_info)

    def keystone_update_user_password_async_invoker(self, request):
        http_info = self._keystone_update_user_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_update_user_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/users/{user_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneUpdateUserPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

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

    def list_user_login_protects_async(self, request):
        """查询IAM用户的登录保护状态信息列表

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的登录保护状态列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserLoginProtects
        :type request: :class:`huaweicloudsdkiam.v3.ListUserLoginProtectsRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListUserLoginProtectsResponse`
        """
        http_info = self._list_user_login_protects_http_info(request)
        return self._call_api(**http_info)

    def list_user_login_protects_async_invoker(self, request):
        http_info = self._list_user_login_protects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_login_protects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-USER/login-protects",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserLoginProtectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def list_user_mfa_devices_async(self, request):
        """该接口可以用于获取MFA设备。

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户的MFA绑定信息列表。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserMfaDevices
        :type request: :class:`huaweicloudsdkiam.v3.ListUserMfaDevicesRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ListUserMfaDevicesResponse`
        """
        http_info = self._list_user_mfa_devices_http_info(request)
        return self._call_api(**http_info)

    def list_user_mfa_devices_async_invoker(self, request):
        http_info = self._list_user_mfa_devices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_mfa_devices_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-MFA/virtual-mfa-devices",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserMfaDevicesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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

    def show_user_async(self, request):
        """查询IAM用户详情（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询IAM用户详情，或IAM用户查询自己的详情。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkiam.v3.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowUserResponse`
        """
        http_info = self._show_user_http_info(request)
        return self._call_api(**http_info)

    def show_user_async_invoker(self, request):
        http_info = self._show_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-USER/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def show_user_login_protect_async(self, request):
        """查询指定IAM用户的登录保护状态信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的登录保护状态信息，或IAM用户查询自己的登录保护状态信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserLoginProtect
        :type request: :class:`huaweicloudsdkiam.v3.ShowUserLoginProtectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowUserLoginProtectResponse`
        """
        http_info = self._show_user_login_protect_http_info(request)
        return self._call_api(**http_info)

    def show_user_login_protect_async_invoker(self, request):
        http_info = self._show_user_login_protect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_login_protect_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-USER/users/{user_id}/login-protect",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserLoginProtectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def show_user_mfa_device_async(self, request):
        """查询指定IAM用户的MFA绑定信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询指定IAM用户的MFA绑定信息，或IAM用户查询自己的MFA绑定信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserMfaDevice
        :type request: :class:`huaweicloudsdkiam.v3.ShowUserMfaDeviceRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.ShowUserMfaDeviceResponse`
        """
        http_info = self._show_user_mfa_device_http_info(request)
        return self._call_api(**http_info)

    def show_user_mfa_device_async_invoker(self, request):
        http_info = self._show_user_mfa_device_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_mfa_device_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.0/OS-MFA/users/{user_id}/virtual-mfa-device",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserMfaDeviceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

        query_params = []

        header_params = {}

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

    def update_login_protect_async(self, request):
        """修改IAM用户登录保护状态信息

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改账号操作保护。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLoginProtect
        :type request: :class:`huaweicloudsdkiam.v3.UpdateLoginProtectRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateLoginProtectResponse`
        """
        http_info = self._update_login_protect_http_info(request)
        return self._call_api(**http_info)

    def update_login_protect_async_invoker(self, request):
        http_info = self._update_login_protect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_login_protect_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-USER/users/{user_id}/login-protect",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLoginProtectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_user_async(self, request):
        """管理员修改IAM用户信息（推荐）

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)修改IAM用户信息 。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkiam.v3.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateUserResponse`
        """
        http_info = self._update_user_http_info(request)
        return self._call_api(**http_info)

    def update_user_async_invoker(self, request):
        http_info = self._update_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-USER/users/{user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_user_information_async(self, request):
        """修改IAM用户信息（推荐）

        该接口可以用于IAM用户修改自己的用户信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserInformation
        :type request: :class:`huaweicloudsdkiam.v3.UpdateUserInformationRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.UpdateUserInformationResponse`
        """
        http_info = self._update_user_information_http_info(request)
        return self._call_api(**http_info)

    def update_user_information_async_invoker(self, request):
        http_info = self._update_user_information_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_information_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.0/OS-USER/users/{user_id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserInformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            ['application/json;charset=UTF-8'])

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

    def keystone_create_agency_token_async(self, request):
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
        http_info = self._keystone_create_agency_token_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_agency_token_async_invoker(self, request):
        http_info = self._keystone_create_agency_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_agency_token_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/auth/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateAgencyTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def keystone_create_user_token_by_password_async(self, request):
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
        http_info = self._keystone_create_user_token_by_password_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_user_token_by_password_async_invoker(self, request):
        http_info = self._keystone_create_user_token_by_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_user_token_by_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/auth/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateUserTokenByPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def keystone_create_user_token_by_password_and_mfa_async(self, request):
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
        http_info = self._keystone_create_user_token_by_password_and_mfa_http_info(request)
        return self._call_api(**http_info)

    def keystone_create_user_token_by_password_and_mfa_async_invoker(self, request):
        http_info = self._keystone_create_user_token_by_password_and_mfa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_create_user_token_by_password_and_mfa_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/auth/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneCreateUserTokenByPasswordAndMfaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'nocatalog' in local_var_params:
            query_params.append(('nocatalog', local_var_params['nocatalog']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def keystone_validate_token_async(self, request):
        """校验Token的有效性

        该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)校验本账号中IAM用户token的有效性，或IAM用户校验自己token的有效性。管理员仅能校验本账号中IAM用户token的有效性，不能校验其他账号中IAM用户token的有效性。如果被校验的token有效，则返回该token的详细信息。
        
        该接口可以使用全局区域的Endpoint和其他区域的Endpoint调用。IAM的Endpoint请参见：[地区和终端节点](https://developer.huaweicloud.com/endpoint?IAM)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for KeystoneValidateToken
        :type request: :class:`huaweicloudsdkiam.v3.KeystoneValidateTokenRequest`
        :rtype: :class:`huaweicloudsdkiam.v3.KeystoneValidateTokenResponse`
        """
        http_info = self._keystone_validate_token_http_info(request)
        return self._call_api(**http_info)

    def keystone_validate_token_async_invoker(self, request):
        http_info = self._keystone_validate_token_http_info(request)
        return AsyncInvoker(self, http_info)

    def _keystone_validate_token_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/auth/tokens",
            "request_type": request.__class__.__name__,
            "response_type": "KeystoneValidateTokenResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Subject-Token", ]

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
            kwargs["async_request"] = True
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

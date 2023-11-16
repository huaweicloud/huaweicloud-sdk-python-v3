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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkprojectman'")


class ProjectManClient(Client):
    def __init__(self):
        super(ProjectManClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkprojectman.v4.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ProjectManClient":
                raise TypeError("client type error, support client type is ProjectManClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_apply_join_project_for_agc(self, request):
        """AGC调用 当前用户申请加入项目

        AGC调用 当前用户申请加入项目, 申请的用户id写在header中
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddApplyJoinProjectForAgc
        :type request: :class:`huaweicloudsdkprojectman.v4.AddApplyJoinProjectForAgcRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.AddApplyJoinProjectForAgcResponse`
        """
        http_info = self._add_apply_join_project_for_agc_http_info(request)
        return self._call_api(**http_info)

    def add_apply_join_project_for_agc_invoker(self, request):
        http_info = self._add_apply_join_project_for_agc_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_apply_join_project_for_agc_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/members/agc-join",
            "request_type": request.__class__.__name__,
            "response_type": "AddApplyJoinProjectForAgcResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'domain_id' in local_var_params:
            header_params['Domain-Id'] = local_var_params['domain_id']
        if 'user_id' in local_var_params:
            header_params['User-Id'] = local_var_params['user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_member_v4(self, request):
        """添加项目成员

        添加项目成员,可以添加跨租户成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddMemberV4
        :type request: :class:`huaweicloudsdkprojectman.v4.AddMemberV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.AddMemberV4Response`
        """
        http_info = self._add_member_v4_http_info(request)
        return self._call_api(**http_info)

    def add_member_v4_invoker(self, request):
        http_info = self._add_member_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_member_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/member",
            "request_type": request.__class__.__name__,
            "response_type": "AddMemberV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_add_members_v4(self, request):
        """批量添加项目成员

        批量添加项目成员，只能添加和项目创建者同一租户下的成员，不正确的用户id会略过，添加的用户超过权限的，默认角色设置为7
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddMembersV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchAddMembersV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchAddMembersV4Response`
        """
        http_info = self._batch_add_members_v4_http_info(request)
        return self._call_api(**http_info)

    def batch_add_members_v4_invoker(self, request):
        http_info = self._batch_add_members_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_members_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddMembersV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_members_v4(self, request):
        """批量删除项目成员

        批量删除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMembersV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchDeleteMembersV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeleteMembersV4Response`
        """
        http_info = self._batch_delete_members_v4_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_members_v4_invoker(self, request):
        http_info = self._batch_delete_members_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_members_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteMembersV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_update_child_nick_names(self, request):
        """更新子用户昵称

        拥有te_admin角色的用户可以更新其他用户的昵称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateChildNickNames
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchUpdateChildNickNamesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchUpdateChildNickNamesResponse`
        """
        http_info = self._batch_update_child_nick_names_http_info(request)
        return self._call_api(**http_info)

    def batch_update_child_nick_names_invoker(self, request):
        http_info = self._batch_update_child_nick_names_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_child_nick_names_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/domain/child-users",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateChildNickNamesResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def check_project_name_v4(self, request):
        """检查项目名称是否存在

        检查项目名称是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckProjectNameV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CheckProjectNameV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CheckProjectNameV4Response`
        """
        http_info = self._check_project_name_v4_http_info(request)
        return self._call_api(**http_info)

    def check_project_name_v4_invoker(self, request):
        http_info = self._check_project_name_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_project_name_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/check-name",
            "request_type": request.__class__.__name__,
            "response_type": "CheckProjectNameV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_project_v4(self, request):
        """创建项目

        创建项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateProjectV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProjectV4Response`
        """
        http_info = self._create_project_v4_http_info(request)
        return self._call_api(**http_info)

    def create_project_v4_invoker(self, request):
        http_info = self._create_project_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/project",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_project_v4(self, request):
        """删除项目

        删除项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProjectV4
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteProjectV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteProjectV4Response`
        """
        http_info = self._delete_project_v4_http_info(request)
        return self._call_api(**http_info)

    def delete_project_v4_invoker(self, request):
        http_info = self._delete_project_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_project_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProjectV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_domain_not_added_projects_v4(self, request):
        """获取租户没有加入的项目

        获取租户没有加入的项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainNotAddedProjectsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4Response`
        """
        http_info = self._list_domain_not_added_projects_v4_http_info(request)
        return self._call_api(**http_info)

    def list_domain_not_added_projects_v4_invoker(self, request):
        http_info = self._list_domain_not_added_projects_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_not_added_projects_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/domain/not-added",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainNotAddedProjectsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_bug_statics_v4(self, request):
        """获取bug统计信息

        获取bug统计信息，按模块统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectBugStaticsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectBugStaticsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectBugStaticsV4Response`
        """
        http_info = self._list_project_bug_statics_v4_http_info(request)
        return self._call_api(**http_info)

    def list_project_bug_statics_v4_invoker(self, request):
        http_info = self._list_project_bug_statics_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_bug_statics_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/bug-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectBugStaticsV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_demand_static_v4(self, request):
        """获取需求统计信息

        获取需求统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectDemandStaticV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectDemandStaticV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectDemandStaticV4Response`
        """
        http_info = self._list_project_demand_static_v4_http_info(request)
        return self._call_api(**http_info)

    def list_project_demand_static_v4_invoker(self, request):
        http_info = self._list_project_demand_static_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_demand_static_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/demand-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectDemandStaticV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_members_v4(self, request):
        """获取指定项目的成员用户列表

        获取项目成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectMembersV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectMembersV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectMembersV4Response`
        """
        http_info = self._list_project_members_v4_http_info(request)
        return self._call_api(**http_info)

    def list_project_members_v4_invoker(self, request):
        http_info = self._list_project_members_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_members_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectMembersV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_projects_v4(self, request):
        """查询项目列表

        查询项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectsV4Response`
        """
        http_info = self._list_projects_v4_http_info(request)
        return self._call_api(**http_info)

    def list_projects_v4_invoker(self, request):
        http_info = self._list_projects_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_projects_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'project_type' in local_var_params:
            query_params.append(('project_type', local_var_params['project_type']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'archive' in local_var_params:
            query_params.append(('archive', local_var_params['archive']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_templates(self, request):
        """查询项目模板

        查询项目模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkprojectman.v4.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workitem_status_records_v4(self, request):
        """查询看板项目下工作项的状态历史记录

        分页查询看板项目下工作项的状态历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkitemStatusRecordsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListWorkitemStatusRecordsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListWorkitemStatusRecordsV4Response`
        """
        http_info = self._list_workitem_status_records_v4_http_info(request)
        return self._call_api(**http_info)

    def list_workitem_status_records_v4_invoker(self, request):
        http_info = self._list_workitem_status_records_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workitem_status_records_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/work-items/status-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkitemStatusRecordsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_workitems(self, request):
        """查询看板项目下的工作项

        查询看板项目下的工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkitems
        :type request: :class:`huaweicloudsdkprojectman.v4.ListWorkitemsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListWorkitemsResponse`
        """
        http_info = self._list_workitems_http_info(request)
        return self._call_api(**http_info)

    def list_workitems_invoker(self, request):
        http_info = self._list_workitems_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_workitems_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/work-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkitemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'created_time_interval' in local_var_params:
            query_params.append(('created_time_interval', local_var_params['created_time_interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def remove_project(self, request):
        """主动退出项目

        项目成员主动退出项目，项目创建者不能退出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveProject
        :type request: :class:`huaweicloudsdkprojectman.v4.RemoveProjectRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.RemoveProjectResponse`
        """
        http_info = self._remove_project_http_info(request)
        return self._call_api(**http_info)

    def remove_project_invoker(self, request):
        http_info = self._remove_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _remove_project_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/quit",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveProjectResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_bug_density_v2(self, request):
        """查询缺陷密度

        查询缺陷密度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBugDensityV2
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowBugDensityV2Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowBugDensityV2Response`
        """
        http_info = self._show_bug_density_v2_http_info(request)
        return self._call_api(**http_info)

    def show_bug_density_v2_invoker(self, request):
        http_info = self._show_bug_density_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bug_density_v2_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/bug-density/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBugDensityV2Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_bugs_per_developer(self, request):
        """查询人均bug

        查询人均bug
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBugsPerDeveloper
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowBugsPerDeveloperRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowBugsPerDeveloperResponse`
        """
        http_info = self._show_bugs_per_developer_http_info(request)
        return self._call_api(**http_info)

    def show_bugs_per_developer_invoker(self, request):
        http_info = self._show_bugs_per_developer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bugs_per_developer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/bugs-per-developer/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBugsPerDeveloperResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_completion_rate(self, request):
        """查询需求按时完成率

        查询需求按时完成率
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCompletionRate
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowCompletionRateRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowCompletionRateResponse`
        """
        http_info = self._show_completion_rate_http_info(request)
        return self._call_api(**http_info)

    def show_completion_rate_invoker(self, request):
        http_info = self._show_completion_rate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_completion_rate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/completion-rate/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCompletionRateResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cur_user_info(self, request):
        """获取当前用户信息

        获取当前用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCurUserInfo
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowCurUserInfoRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowCurUserInfoResponse`
        """
        http_info = self._show_cur_user_info_http_info(request)
        return self._call_api(**http_info)

    def show_cur_user_info_invoker(self, request):
        http_info = self._show_cur_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cur_user_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCurUserInfoResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cur_user_role(self, request):
        """获取当前用户角色

        获取用户在项目中的角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCurUserRole
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowCurUserRoleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowCurUserRoleResponse`
        """
        http_info = self._show_cur_user_role_http_info(request)
        return self._call_api(**http_info)

    def show_cur_user_role_invoker(self, request):
        http_info = self._show_cur_user_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cur_user_role_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/user-role",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCurUserRoleResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_info_v4(self, request):
        """获取项目详情

        获取项目详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectInfoV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowProjectInfoV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowProjectInfoV4Response`
        """
        http_info = self._show_project_info_v4_http_info(request)
        return self._call_api(**http_info)

    def show_project_info_v4_invoker(self, request):
        http_info = self._show_project_info_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_info_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectInfoV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_summary_v4(self, request):
        """获取项目概览

        获取项目概览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectSummaryV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowProjectSummaryV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowProjectSummaryV4Response`
        """
        http_info = self._show_project_summary_v4_http_info(request)
        return self._call_api(**http_info)

    def show_project_summary_v4_invoker(self, request):
        http_info = self._show_project_summary_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_summary_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectSummaryV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_work_item_wrokflow_config(self, request):
        """查询看板项目的工作项流转配置

        查询看板项目的工作项流转配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkItemWrokflowConfig
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowWorkItemWrokflowConfigRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowWorkItemWrokflowConfigResponse`
        """
        http_info = self._show_work_item_wrokflow_config_http_info(request)
        return self._call_api(**http_info)

    def show_work_item_wrokflow_config_invoker(self, request):
        http_info = self._show_work_item_wrokflow_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_work_item_wrokflow_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/work-items/workflow/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWorkItemWrokflowConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'board_id' in local_var_params:
            query_params.append(('board_id', local_var_params['board_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_membes_role_v4(self, request):
        """更新成员在项目中的角色

        更新成员在项目中的角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMembesRoleV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateMembesRoleV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateMembesRoleV4Response`
        """
        http_info = self._update_membes_role_v4_http_info(request)
        return self._call_api(**http_info)

    def update_membes_role_v4_invoker(self, request):
        http_info = self._update_membes_role_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_membes_role_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/members/role",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMembesRoleV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_nick_name_v4(self, request):
        """更新用户昵称

        更新用户昵称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNickNameV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateNickNameV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateNickNameV4Response`
        """
        http_info = self._update_nick_name_v4_http_info(request)
        return self._call_api(**http_info)

    def update_nick_name_v4_invoker(self, request):
        http_info = self._update_nick_name_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_nick_name_v4_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/user",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNickNameV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_project_v4(self, request):
        """更新项目

        更新项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateProjectV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateProjectV4Response`
        """
        http_info = self._update_project_v4_http_info(request)
        return self._call_api(**http_info)

    def update_project_v4_invoker(self, request):
        http_info = self._update_project_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_project_v4_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def add_issue_work_hours(self, request):
        """添加指定工作项工时

        添加指定工作项工时
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddIssueWorkHours
        :type request: :class:`huaweicloudsdkprojectman.v4.AddIssueWorkHoursRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.AddIssueWorkHoursResponse`
        """
        http_info = self._add_issue_work_hours_http_info(request)
        return self._call_api(**http_info)

    def add_issue_work_hours_invoker(self, request):
        http_info = self._add_issue_work_hours_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_issue_work_hours_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/work-hours",
            "request_type": request.__class__.__name__,
            "response_type": "AddIssueWorkHoursResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_issues_v4(self, request):
        """批量删除工作项

        批量删除工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteIssuesV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIssuesV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIssuesV4Response`
        """
        http_info = self._batch_delete_issues_v4_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_issues_v4_invoker(self, request):
        http_info = self._batch_delete_issues_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_issues_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/issues",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteIssuesV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def batch_delete_iterations_v4(self, request):
        """批量删除项目的迭代

        批量删除项目的迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteIterationsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIterationsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIterationsV4Response`
        """
        http_info = self._batch_delete_iterations_v4_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_iterations_v4_invoker(self, request):
        http_info = self._batch_delete_iterations_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_iterations_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/iterations",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteIterationsV4Response"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def cancel_project_domain(self, request):
        """取消领域与项目的关联关系

        取消领域与项目的关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelProjectDomain
        :type request: :class:`huaweicloudsdkprojectman.v4.CancelProjectDomainRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CancelProjectDomainResponse`
        """
        http_info = self._cancel_project_domain_http_info(request)
        return self._call_api(**http_info)

    def cancel_project_domain_invoker(self, request):
        http_info = self._cancel_project_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_project_domain_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelProjectDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_customfields(self, request):
        """创建工作项类型自定义字段

        创建工作项类型自定义字段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomfields
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateCustomfieldsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateCustomfieldsResponse`
        """
        http_info = self._create_customfields_http_info(request)
        return self._call_api(**http_info)

    def create_customfields_invoker(self, request):
        http_info = self._create_customfields_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_customfields_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/custom-fields",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomfieldsResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_issue_v4(self, request):
        """创建工作项

        创建工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueV4Response`
        """
        http_info = self._create_issue_v4_http_info(request)
        return self._call_api(**http_info)

    def create_issue_v4_invoker(self, request):
        http_info = self._create_issue_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_issue_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/issue",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIssueV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_iteration_v4(self, request):
        """创建Scrum项目迭代

        创建Scrum项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIterationV4Response`
        """
        http_info = self._create_iteration_v4_http_info(request)
        return self._call_api(**http_info)

    def create_iteration_v4_invoker(self, request):
        http_info = self._create_iteration_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_iteration_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/iteration",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIterationV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_project_domain(self, request):
        """创建项目的领域

        查询项目的领域列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectDomain
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateProjectDomainRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProjectDomainResponse`
        """
        http_info = self._create_project_domain_http_info(request)
        return self._call_api(**http_info)

    def create_project_domain_invoker(self, request):
        http_info = self._create_project_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_domain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/domain",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectDomainResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_project_module(self, request):
        """创建项目的模块

        查询项目的模块列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectModule
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateProjectModuleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProjectModuleResponse`
        """
        http_info = self._create_project_module_http_info(request)
        return self._call_api(**http_info)

    def create_project_module_invoker(self, request):
        http_info = self._create_project_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_module_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/module",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectModuleResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_system_issue_v4(self, request):
        """细粒度权限用户创建工作项

        拥有IAM细粒度权限（projectmanConfig:systemSettingField:set）且在devcloud项目中有创建工作项的权限的用户可以设置工作项的创建者
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSystemIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateSystemIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateSystemIssueV4Response`
        """
        http_info = self._create_system_issue_v4_http_info(request)
        return self._call_api(**http_info)

    def create_system_issue_v4_invoker(self, request):
        http_info = self._create_system_issue_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_system_issue_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/system/issue",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSystemIssueV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_attachment(self, request):
        """删除附件

        取消工作项与附件关联，如附件为工作项页面上传则删除附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAttachment
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteAttachmentRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteAttachmentResponse`
        """
        http_info = self._delete_attachment_http_info(request)
        return self._call_api(**http_info)

    def delete_attachment_invoker(self, request):
        http_info = self._delete_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_attachment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/attachments/{attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_issue_v4(self, request):
        """删除工作项

        删除工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteIssueV4Response`
        """
        http_info = self._delete_issue_v4_http_info(request)
        return self._call_api(**http_info)

    def delete_issue_v4_invoker(self, request):
        http_info = self._delete_issue_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_issue_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIssueV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_iteration_v4(self, request):
        """删除项目迭代

        删除项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteIterationV4Response`
        """
        http_info = self._delete_iteration_v4_http_info(request)
        return self._call_api(**http_info)

    def delete_iteration_v4_invoker(self, request):
        http_info = self._delete_iteration_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_iteration_v4_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/iterations/{iteration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIterationV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'iteration_id' in local_var_params:
            path_params['iteration_id'] = local_var_params['iteration_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_project_module(self, request):
        """删除项目的模块

        删除项目的模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProjectModule
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteProjectModuleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteProjectModuleResponse`
        """
        http_info = self._delete_project_module_http_info(request)
        return self._call_api(**http_info)

    def delete_project_module_invoker(self, request):
        http_info = self._delete_project_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_project_module_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProjectModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_attachment(self, request):
        """下载工作项附件

        下载工作项附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAttachment
        :type request: :class:`huaweicloudsdkprojectman.v4.DownloadAttachmentRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DownloadAttachmentResponse`
        """
        http_info = self._download_attachment_http_info(request)
        return self._call_api(**http_info)

    def download_attachment_invoker(self, request):
        http_info = self._download_attachment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_attachment_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/attachments/{attachment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAttachmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']
        if 'attachment_id' in local_var_params:
            path_params['attachment_id'] = local_var_params['attachment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def download_image_file(self, request):
        """下载图片

        下载图片
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadImageFile
        :type request: :class:`huaweicloudsdkprojectman.v4.DownloadImageFileRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DownloadImageFileResponse`
        """
        http_info = self._download_image_file_http_info(request)
        return self._call_api(**http_info)

    def download_image_file_invoker(self, request):
        http_info = self._download_image_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_image_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/image-file",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadImageFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'image_uri' in local_var_params:
            query_params.append(('image_uri', local_var_params['image_uri']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_associated_issues(self, request):
        """查询当前工作项已经关联的工作项

        查询当前工作项已经关联的工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssociatedIssues
        :type request: :class:`huaweicloudsdkprojectman.v4.ListAssociatedIssuesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListAssociatedIssuesResponse`
        """
        http_info = self._list_associated_issues_http_info(request)
        return self._call_api(**http_info)

    def list_associated_issues_invoker(self, request):
        http_info = self._list_associated_issues_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_associated_issues_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/associated-issues",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssociatedIssuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_associated_test_cases(self, request):
        """查询关联用例

        查询关联用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssociatedTestCases
        :type request: :class:`huaweicloudsdkprojectman.v4.ListAssociatedTestCasesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListAssociatedTestCasesResponse`
        """
        http_info = self._list_associated_test_cases_http_info(request)
        return self._call_api(**http_info)

    def list_associated_test_cases_invoker(self, request):
        http_info = self._list_associated_test_cases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_associated_test_cases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/associate-test-cases",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssociatedTestCasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_associated_wikis(self, request):
        """查询当前工作项已经关联的关联Wiki

        查询当前工作项已经关联的关联Wiki
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssociatedWikis
        :type request: :class:`huaweicloudsdkprojectman.v4.ListAssociatedWikisRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListAssociatedWikisResponse`
        """
        http_info = self._list_associated_wikis_http_info(request)
        return self._call_api(**http_info)

    def list_associated_wikis_invoker(self, request):
        http_info = self._list_associated_wikis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_associated_wikis_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/associated-wikis",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssociatedWikisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_child_issues_v4(self, request):
        """获取子工作项

        获取子工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListChildIssuesV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListChildIssuesV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListChildIssuesV4Response`
        """
        http_info = self._list_child_issues_v4_http_info(request)
        return self._call_api(**http_info)

    def list_child_issues_v4_invoker(self, request):
        http_info = self._list_child_issues_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_child_issues_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/child",
            "request_type": request.__class__.__name__,
            "response_type": "ListChildIssuesV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_issue_associated_commits(self, request):
        """查询当前工作项已经关联的代码提交记录 / 分支创建记录

        查询当前工作项已经关联的代码提交记录 / 分支创建记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueAssociatedCommits
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueAssociatedCommitsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueAssociatedCommitsResponse`
        """
        http_info = self._list_issue_associated_commits_http_info(request)
        return self._call_api(**http_info)

    def list_issue_associated_commits_invoker(self, request):
        http_info = self._list_issue_associated_commits_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issue_associated_commits_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/associated-commits",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssueAssociatedCommitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_issue_comments_v4(self, request):
        """获取指定工作项的评论列表

        获取工作项的评论
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueCommentsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueCommentsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueCommentsV4Response`
        """
        http_info = self._list_issue_comments_v4_http_info(request)
        return self._call_api(**http_info)

    def list_issue_comments_v4_invoker(self, request):
        http_info = self._list_issue_comments_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issue_comments_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/comments",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssueCommentsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_issue_custom_fields(self, request):
        """查询Scrum工作项自定义字段

        查询Scrum工作项自定义字段的可选列表,符合custom_fields或者names条件的都返回,2个值都不传，返回所有的自定义字段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueCustomFields
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueCustomFieldsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueCustomFieldsResponse`
        """
        http_info = self._list_issue_custom_fields_http_info(request)
        return self._call_api(**http_info)

    def list_issue_custom_fields_invoker(self, request):
        http_info = self._list_issue_custom_fields_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issue_custom_fields_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/issues/custom-fields",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssueCustomFieldsResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_issue_records_v4(self, request):
        """获取工作项历史记录

        获取工作项历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueRecordsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueRecordsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueRecordsV4Response`
        """
        http_info = self._list_issue_records_v4_http_info(request)
        return self._call_api(**http_info)

    def list_issue_records_v4_invoker(self, request):
        http_info = self._list_issue_records_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issue_records_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issue/{issue_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssueRecordsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_issues_sf_v4(self, request):
        """查询项目的工作项

        工作项类型id, 分页参数，创建时间查询项目的工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssuesSfV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssuesSfV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssuesSfV4Response`
        """
        http_info = self._list_issues_sf_v4_http_info(request)
        return self._call_api(**http_info)

    def list_issues_sf_v4_invoker(self, request):
        http_info = self._list_issues_sf_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issues_sf_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssuesSfV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))
        if 'created_time_interval' in local_var_params:
            query_params.append(('created_time_interval', local_var_params['created_time_interval']))
        if 'updated_time_interval' in local_var_params:
            query_params.append(('updated_time_interval', local_var_params['updated_time_interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_issues_v4(self, request):
        """高级查询工作项

        根据筛选条件查询工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssuesV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssuesV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssuesV4Response`
        """
        http_info = self._list_issues_v4_http_info(request)
        return self._call_api(**http_info)

    def list_issues_v4_invoker(self, request):
        http_info = self._list_issues_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_issues_v4_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/issues",
            "request_type": request.__class__.__name__,
            "response_type": "ListIssuesV4Response"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_iteration_histories(self, request):
        """查看迭代历史记录

        查看迭代历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIterationHistories
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIterationHistoriesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIterationHistoriesResponse`
        """
        http_info = self._list_iteration_histories_http_info(request)
        return self._call_api(**http_info)

    def list_iteration_histories_invoker(self, request):
        http_info = self._list_iteration_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_iteration_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/iterations/{iteration_id}/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListIterationHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'iteration_id' in local_var_params:
            path_params['iteration_id'] = local_var_params['iteration_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_domains(self, request):
        """查询项目的领域列表

        查询项目的领域列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectDomains
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectDomainsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectDomainsResponse`
        """
        http_info = self._list_project_domains_http_info(request)
        return self._call_api(**http_info)

    def list_project_domains_invoker(self, request):
        http_info = self._list_project_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_domains_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_issues_records_v4(self, request):
        """查询项目下所有工作项的历史记录

        查询项目下所有工作项的历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectIssuesRecordsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectIssuesRecordsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectIssuesRecordsV4Response`
        """
        http_info = self._list_project_issues_records_v4_http_info(request)
        return self._call_api(**http_info)

    def list_project_issues_records_v4_invoker(self, request):
        http_info = self._list_project_issues_records_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_issues_records_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/records",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectIssuesRecordsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'operated_time_interval' in local_var_params:
            query_params.append(('operated_time_interval', local_var_params['operated_time_interval']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_iterations_v4(self, request):
        """获取指定项目的迭代列表

        获取项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectIterationsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectIterationsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectIterationsV4Response`
        """
        http_info = self._list_project_iterations_v4_http_info(request)
        return self._call_api(**http_info)

    def list_project_iterations_v4_invoker(self, request):
        http_info = self._list_project_iterations_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_iterations_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/iterations",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectIterationsV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'updated_time_interval' in local_var_params:
            query_params.append(('updated_time_interval', local_var_params['updated_time_interval']))
        if 'include_deleted' in local_var_params:
            query_params.append(('include_deleted', local_var_params['include_deleted']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_modules(self, request):
        """查询项目的模块列表

        查询项目的模块列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectModules
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectModulesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectModulesResponse`
        """
        http_info = self._list_project_modules_http_info(request)
        return self._call_api(**http_info)

    def list_project_modules_invoker(self, request):
        http_info = self._list_project_modules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_modules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/modules",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectModulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_work_hours(self, request):
        """按用户查询工时（多项目）

        按用户查询工时（多项目）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectWorkHours
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectWorkHoursRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectWorkHoursResponse`
        """
        http_info = self._list_project_work_hours_http_info(request)
        return self._call_api(**http_info)

    def list_project_work_hours_invoker(self, request):
        http_info = self._list_project_work_hours_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_work_hours_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/work-hours",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectWorkHoursResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_project_work_hours_type(self, request):
        """查询项目下的工时类型

        查询项目下的工时类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectWorkHoursType
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectWorkHoursTypeRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectWorkHoursTypeResponse`
        """
        http_info = self._list_project_work_hours_type_http_info(request)
        return self._call_api(**http_info)

    def list_project_work_hours_type_invoker(self, request):
        http_info = self._list_project_work_hours_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_work_hours_type_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/work-hours-type",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectWorkHoursTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_scrum_project_statuses(self, request):
        """查询项目的状态列表

        查询项目的状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScrumProjectStatuses
        :type request: :class:`huaweicloudsdkprojectman.v4.ListScrumProjectStatusesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListScrumProjectStatusesResponse`
        """
        http_info = self._list_scrum_project_statuses_http_info(request)
        return self._call_api(**http_info)

    def list_scrum_project_statuses_invoker(self, request):
        http_info = self._list_scrum_project_statuses_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scrum_project_statuses_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/statuses",
            "request_type": request.__class__.__name__,
            "response_type": "ListScrumProjectStatusesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_spec_issue_stay_times(self, request):
        """获取指定工作项停留时间

        获取指定工作项停留时间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpecIssueStayTimes
        :type request: :class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesResponse`
        """
        http_info = self._list_spec_issue_stay_times_http_info(request)
        return self._call_api(**http_info)

    def list_spec_issue_stay_times_invoker(self, request):
        http_info = self._list_spec_issue_stay_times_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_spec_issue_stay_times_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/issues/duration",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpecIssueStayTimesResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_status_statistic(self, request):
        """查询迭代下工作项状态的统计数据（处理人维度）

        查询迭代下工作项状态的统计数据（处理人维度）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStatusStatistic
        :type request: :class:`huaweicloudsdkprojectman.v4.ListStatusStatisticRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListStatusStatisticResponse`
        """
        http_info = self._list_status_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_status_statistic_invoker(self, request):
        http_info = self._list_status_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_status_statistic_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/status-statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatusStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'iteration_id' in local_var_params:
            query_params.append(('iteration_id', local_var_params['iteration_id']))
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))
        if 'status_id' in local_var_params:
            query_params.append(('status_id', local_var_params['status_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def search_issues(self, request):
        """高级查询我的待办工作项

        高级查询我的待办工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchIssues
        :type request: :class:`huaweicloudsdkprojectman.v4.SearchIssuesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.SearchIssuesResponse`
        """
        http_info = self._search_issues_http_info(request)
        return self._call_api(**http_info)

    def search_issues_invoker(self, request):
        http_info = self._search_issues_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_issues_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/issues",
            "request_type": request.__class__.__name__,
            "response_type": "SearchIssuesResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_issue_completion_rate(self, request):
        """获取工作项完成率

        获取工作项的完成率
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssueCompletionRate
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIssueCompletionRateRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIssueCompletionRateResponse`
        """
        http_info = self._show_issue_completion_rate_http_info(request)
        return self._call_api(**http_info)

    def show_issue_completion_rate_invoker(self, request):
        http_info = self._show_issue_completion_rate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_issue_completion_rate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issue-completion-rate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIssueCompletionRateResponse"
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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_issue_v4(self, request):
        """查询工作项详情

        查询工作项详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIssueV4Response`
        """
        http_info = self._show_issue_v4_http_info(request)
        return self._call_api(**http_info)

    def show_issue_v4_invoker(self, request):
        http_info = self._show_issue_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_issue_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIssueV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_issues_wrok_flow_config(self, request):
        """查询Scrum项目的工作项流转配置

        查询Scrum项目的工作项流转配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssuesWrokFlowConfig
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIssuesWrokFlowConfigRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIssuesWrokFlowConfigResponse`
        """
        http_info = self._show_issues_wrok_flow_config_http_info(request)
        return self._call_api(**http_info)

    def show_issues_wrok_flow_config_invoker(self, request):
        http_info = self._show_issues_wrok_flow_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_issues_wrok_flow_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/issues/workflow/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIssuesWrokFlowConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_iteration_v4(self, request):
        """查看迭代详情

        查看迭代详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIterationV4Response`
        """
        http_info = self._show_iteration_v4_http_info(request)
        return self._call_api(**http_info)

    def show_iteration_v4_invoker(self, request):
        http_info = self._show_iteration_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_iteration_v4_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/iterations/{iteration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIterationV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'iteration_id' in local_var_params:
            path_params['iteration_id'] = local_var_params['iteration_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_work_hours(self, request):
        """按用户查询工时（单项目）

        按用户查询工时（单项目）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectWorkHours
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursResponse`
        """
        http_info = self._show_project_work_hours_http_info(request)
        return self._call_api(**http_info)

    def show_project_work_hours_invoker(self, request):
        http_info = self._show_project_work_hours_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_work_hours_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/work-hours",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectWorkHoursResponse"
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_issue_v4(self, request):
        """更新工作项

        更新工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateIssueV4Response`
        """
        http_info = self._update_issue_v4_http_info(request)
        return self._call_api(**http_info)

    def update_issue_v4_invoker(self, request):
        http_info = self._update_issue_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_issue_v4_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIssueV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_iteration_v4(self, request):
        """更新Scrum项目迭代

        更新Scrum项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateIterationV4Response`
        """
        http_info = self._update_iteration_v4_http_info(request)
        return self._call_api(**http_info)

    def update_iteration_v4_invoker(self, request):
        http_info = self._update_iteration_v4_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_iteration_v4_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/iterations/{iteration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIterationV4Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'iteration_id' in local_var_params:
            path_params['iteration_id'] = local_var_params['iteration_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_project_domain(self, request):
        """更新项目的领域

        更新项目的领域
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectDomain
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateProjectDomainRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateProjectDomainResponse`
        """
        http_info = self._update_project_domain_http_info(request)
        return self._call_api(**http_info)

    def update_project_domain_invoker(self, request):
        http_info = self._update_project_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_project_domain_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/domains/{domain_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_project_module(self, request):
        """更新项目的模块

        更新项目的模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectModule
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateProjectModuleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateProjectModuleResponse`
        """
        http_info = self._update_project_module_http_info(request)
        return self._call_api(**http_info)

    def update_project_module_invoker(self, request):
        http_info = self._update_project_module_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_project_module_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/modules/{module_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectModuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'module_id' in local_var_params:
            path_params['module_id'] = local_var_params['module_id']

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

        auth_settings = ['apig-auth-iam']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def upload_attachments(self, request):
        """上传工作项附件

        上传工作项附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAttachments
        :type request: :class:`huaweicloudsdkprojectman.v4.UploadAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UploadAttachmentsResponse`
        """
        http_info = self._upload_attachments_http_info(request)
        return self._call_api(**http_info)

    def upload_attachments_invoker(self, request):
        http_info = self._upload_attachments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_attachments_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/issues/{issue_id}/attachments/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadAttachmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'issue_id' in local_var_params:
            path_params['issue_id'] = local_var_params['issue_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'attachment' in local_var_params:
            form_params['attachment'] = local_var_params['attachment']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def upload_issue_img(self, request):
        """上传图片

        上传图片
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadIssueImg
        :type request: :class:`huaweicloudsdkprojectman.v4.UploadIssueImgRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UploadIssueImgResponse`
        """
        http_info = self._upload_issue_img_http_info(request)
        return self._call_api(**http_info)

    def upload_issue_img_invoker(self, request):
        http_info = self._upload_issue_img_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_issue_img_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/img",
            "request_type": request.__class__.__name__,
            "response_type": "UploadIssueImgResponse"
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = ['apig-auth-iam']

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

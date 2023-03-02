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


class ProjectManClient(Client):
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
        super(ProjectManClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkprojectman.v4.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ProjectManClient":
            raise TypeError("client type error, support client type is ProjectManClient")

        return ClientBuilder(clazz)

    def add_apply_join_project_for_agc(self, request):
        """AGC调用 当前用户申请加入项目

        AGC调用 当前用户申请加入项目, 申请的用户id写在header中
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddApplyJoinProjectForAgc
        :type request: :class:`huaweicloudsdkprojectman.v4.AddApplyJoinProjectForAgcRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.AddApplyJoinProjectForAgcResponse`
        """
        return self.add_apply_join_project_for_agc_with_http_info(request)

    def add_apply_join_project_for_agc_with_http_info(self, request):
        all_params = ['domain_id', 'user_id', 'project_id']
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
        if 'domain_id' in local_var_params:
            header_params['Domain-Id'] = local_var_params['domain_id']
        if 'user_id' in local_var_params:
            header_params['User-Id'] = local_var_params['user_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/members/agc-join',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddApplyJoinProjectForAgcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_member_v4(self, request):
        """添加项目成员

        添加项目成员,可以添加跨租户成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddMemberV4
        :type request: :class:`huaweicloudsdkprojectman.v4.AddMemberV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.AddMemberV4Response`
        """
        return self.add_member_v4_with_http_info(request)

    def add_member_v4_with_http_info(self, request):
        all_params = ['project_id', 'add_member_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/member',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddMemberV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_members_v4(self, request):
        """批量添加项目成员

        批量添加项目成员，只能添加和项目创建者同一租户下的成员，不正确的用户id会略过，添加的用户超过权限的，默认角色设置为7
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddMembersV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchAddMembersV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchAddMembersV4Response`
        """
        return self.batch_add_members_v4_with_http_info(request)

    def batch_add_members_v4_with_http_info(self, request):
        all_params = ['project_id', 'batch_add_members_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddMembersV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_members_v4(self, request):
        """批量删除项目成员

        批量删除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMembersV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchDeleteMembersV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeleteMembersV4Response`
        """
        return self.batch_delete_members_v4_with_http_info(request)

    def batch_delete_members_v4_with_http_info(self, request):
        all_params = ['project_id', 'batch_delete_members_v4_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/members',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteMembersV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_child_nick_names(self, request):
        """更新子用户昵称

        拥有te_admin角色的用户可以更新其他用户的昵称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateChildNickNames
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchUpdateChildNickNamesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchUpdateChildNickNamesResponse`
        """
        return self.batch_update_child_nick_names_with_http_info(request)

    def batch_update_child_nick_names_with_http_info(self, request):
        all_params = ['batch_update_child_nick_names_requestbody']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/domain/child-users',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateChildNickNamesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_project_name_v4(self, request):
        """检查项目名称是否存在

        检查项目名称是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckProjectNameV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CheckProjectNameV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CheckProjectNameV4Response`
        """
        return self.check_project_name_v4_with_http_info(request)

    def check_project_name_v4_with_http_info(self, request):
        all_params = ['check_project_name_v4_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/check-name',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckProjectNameV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project_v4(self, request):
        """创建项目

        创建项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateProjectV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProjectV4Response`
        """
        return self.create_project_v4_with_http_info(request)

    def create_project_v4_with_http_info(self, request):
        all_params = ['create_project_v4_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/project',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_project_v4(self, request):
        """删除项目

        删除项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProjectV4
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteProjectV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteProjectV4Response`
        """
        return self.delete_project_v4_with_http_info(request)

    def delete_project_v4_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProjectV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_domain_not_added_projects_v4(self, request):
        """获取租户没有加入的项目

        获取租户没有加入的项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainNotAddedProjectsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListDomainNotAddedProjectsV4Response`
        """
        return self.list_domain_not_added_projects_v4_with_http_info(request)

    def list_domain_not_added_projects_v4_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/domain/not-added',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDomainNotAddedProjectsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_bug_statics_v4(self, request):
        """获取bug统计信息

        获取bug统计信息，按模块统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectBugStaticsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectBugStaticsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectBugStaticsV4Response`
        """
        return self.list_project_bug_statics_v4_with_http_info(request)

    def list_project_bug_statics_v4_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/bug-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectBugStaticsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_demand_static_v4(self, request):
        """获取需求统计信息

        获取需求统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectDemandStaticV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectDemandStaticV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectDemandStaticV4Response`
        """
        return self.list_project_demand_static_v4_with_http_info(request)

    def list_project_demand_static_v4_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/demand-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectDemandStaticV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_members_v4(self, request):
        """获取指定项目的成员用户列表

        获取项目成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectMembersV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectMembersV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectMembersV4Response`
        """
        return self.list_project_members_v4_with_http_info(request)

    def list_project_members_v4_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectMembersV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_projects_v4(self, request):
        """查询项目列表

        查询项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectsV4Response`
        """
        return self.list_projects_v4_with_http_info(request)

    def list_projects_v4_with_http_info(self, request):
        all_params = ['offset', 'limit', 'search', 'project_type', 'sort', 'archive', 'query_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workitem_status_records_v4(self, request):
        """查询看板项目下工作项的状态历史记录

        分页查询看板项目下工作项的状态历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkitemStatusRecordsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListWorkitemStatusRecordsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListWorkitemStatusRecordsV4Response`
        """
        return self.list_workitem_status_records_v4_with_http_info(request)

    def list_workitem_status_records_v4_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/work-items/status-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkitemStatusRecordsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workitems(self, request):
        """查询看板项目下的工作项

        查询看板项目下的工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkitems
        :type request: :class:`huaweicloudsdkprojectman.v4.ListWorkitemsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListWorkitemsResponse`
        """
        return self.list_workitems_with_http_info(request)

    def list_workitems_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit', 'created_time_interval']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'created_time_interval' in local_var_params:
            query_params.append(('created_time_interval', local_var_params['created_time_interval']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/work-items',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkitemsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_project(self, request):
        """主动退出项目

        项目成员主动退出项目，项目创建者不能退出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemoveProject
        :type request: :class:`huaweicloudsdkprojectman.v4.RemoveProjectRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.RemoveProjectResponse`
        """
        return self.remove_project_with_http_info(request)

    def remove_project_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/quit',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemoveProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bug_density_v2(self, request):
        """查询缺陷密度

        查询缺陷密度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBugDensityV2
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowBugDensityV2Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowBugDensityV2Response`
        """
        return self.show_bug_density_v2_with_http_info(request)

    def show_bug_density_v2_with_http_info(self, request):
        all_params = ['project_id', 'show_bug_density_v2_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/bug-density/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBugDensityV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bugs_per_developer(self, request):
        """查询人均bug

        查询人均bug
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBugsPerDeveloper
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowBugsPerDeveloperRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowBugsPerDeveloperResponse`
        """
        return self.show_bugs_per_developer_with_http_info(request)

    def show_bugs_per_developer_with_http_info(self, request):
        all_params = ['project_id', 'show_bugs_per_developer_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/bugs-per-developer/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBugsPerDeveloperResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_completion_rate(self, request):
        """查询需求按时完成率

        查询需求按时完成率
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCompletionRate
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowCompletionRateRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowCompletionRateResponse`
        """
        return self.show_completion_rate_with_http_info(request)

    def show_completion_rate_with_http_info(self, request):
        all_params = ['project_id', 'show_completion_rate_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/{project_id}/completion-rate/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCompletionRateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cur_user_info(self, request):
        """获取当前用户信息

        获取当前用户信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCurUserInfo
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowCurUserInfoRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowCurUserInfoResponse`
        """
        return self.show_cur_user_info_with_http_info(request)

    def show_cur_user_info_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCurUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cur_user_role(self, request):
        """获取当前用户角色

        获取用户在项目中的角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCurUserRole
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowCurUserRoleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowCurUserRoleResponse`
        """
        return self.show_cur_user_role_with_http_info(request)

    def show_cur_user_role_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/user-role',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCurUserRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_info_v4(self, request):
        """获取项目详情

        获取项目详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectInfoV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowProjectInfoV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowProjectInfoV4Response`
        """
        return self.show_project_info_v4_with_http_info(request)

    def show_project_info_v4_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectInfoV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_summary_v4(self, request):
        """获取项目概览

        获取项目概览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectSummaryV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowProjectSummaryV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowProjectSummaryV4Response`
        """
        return self.show_project_summary_v4_with_http_info(request)

    def show_project_summary_v4_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectSummaryV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_work_item_wrokflow_config(self, request):
        """查询看板项目的工作项流转配置

        查询看板项目的工作项流转配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkItemWrokflowConfig
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowWorkItemWrokflowConfigRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowWorkItemWrokflowConfigResponse`
        """
        return self.show_work_item_wrokflow_config_with_http_info(request)

    def show_work_item_wrokflow_config_with_http_info(self, request):
        all_params = ['project_id', 'board_id']
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
        if 'board_id' in local_var_params:
            query_params.append(('board_id', local_var_params['board_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/work-items/workflow/config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkItemWrokflowConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_membes_role_v4(self, request):
        """更新成员在项目中的角色

        更新成员在项目中的角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMembesRoleV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateMembesRoleV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateMembesRoleV4Response`
        """
        return self.update_membes_role_v4_with_http_info(request)

    def update_membes_role_v4_with_http_info(self, request):
        all_params = ['project_id', 'update_membes_role_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/members/role',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMembesRoleV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nick_name_v4(self, request):
        """更新用户昵称

        更新用户昵称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNickNameV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateNickNameV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateNickNameV4Response`
        """
        return self.update_nick_name_v4_with_http_info(request)

    def update_nick_name_v4_with_http_info(self, request):
        all_params = ['update_nick_name_v4_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/user',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNickNameV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project_v4(self, request):
        """更新项目

        更新项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateProjectV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateProjectV4Response`
        """
        return self.update_project_v4_with_http_info(request)

    def update_project_v4_with_http_info(self, request):
        all_params = ['project_id', 'update_project_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProjectV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_issues_v4(self, request):
        """批量删除工作项

        批量删除工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteIssuesV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIssuesV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIssuesV4Response`
        """
        return self.batch_delete_issues_v4_with_http_info(request)

    def batch_delete_issues_v4_with_http_info(self, request):
        all_params = ['project_id', 'batch_delete_issues_v4_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteIssuesV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_iterations_v4(self, request):
        """批量删除项目的迭代

        批量删除项目的迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteIterationsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIterationsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.BatchDeleteIterationsV4Response`
        """
        return self.batch_delete_iterations_v4_with_http_info(request)

    def batch_delete_iterations_v4_with_http_info(self, request):
        all_params = ['project_id', 'batch_delete_iterations_v4_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/iterations',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteIterationsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_project_domain(self, request):
        """取消领域与项目的关联关系

        取消领域与项目的关联关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelProjectDomain
        :type request: :class:`huaweicloudsdkprojectman.v4.CancelProjectDomainRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CancelProjectDomainResponse`
        """
        return self.cancel_project_domain_with_http_info(request)

    def cancel_project_domain_with_http_info(self, request):
        all_params = ['project_id', 'domain_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/domains/{domain_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelProjectDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_customfields(self, request):
        """创建工作项类型自定义字段

        创建工作项类型自定义字段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomfields
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateCustomfieldsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateCustomfieldsResponse`
        """
        return self.create_customfields_with_http_info(request)

    def create_customfields_with_http_info(self, request):
        all_params = ['project_id', 'create_custom_fields_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/{project_id}/custom-fields',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCustomfieldsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_issue_v4(self, request):
        """创建工作项

        创建工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIssueV4Response`
        """
        return self.create_issue_v4_with_http_info(request)

    def create_issue_v4_with_http_info(self, request):
        all_params = ['project_id', 'create_issue_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issue',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_iteration_v4(self, request):
        """创建Scrum项目迭代

        创建Scrum项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateIterationV4Response`
        """
        return self.create_iteration_v4_with_http_info(request)

    def create_iteration_v4_with_http_info(self, request):
        all_params = ['project_id', 'create_iteration_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/iteration',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project_domain(self, request):
        """创建项目的领域

        查询项目的领域列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectDomain
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateProjectDomainRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProjectDomainResponse`
        """
        return self.create_project_domain_with_http_info(request)

    def create_project_domain_with_http_info(self, request):
        all_params = ['project_id', 'create_project_domain_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/domain',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project_module(self, request):
        """创建项目的模块

        查询项目的模块列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectModule
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateProjectModuleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateProjectModuleResponse`
        """
        return self.create_project_module_with_http_info(request)

    def create_project_module_with_http_info(self, request):
        all_params = ['project_id', 'create_project_module_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/module',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_system_issue_v4(self, request):
        """细粒度权限用户创建工作项

        拥有IAM细粒度权限（projectmanConfig:systemSettingField:set）且在devcloud项目中有创建工作项的权限的用户可以设置工作项的创建者
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSystemIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.CreateSystemIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.CreateSystemIssueV4Response`
        """
        return self.create_system_issue_v4_with_http_info(request)

    def create_system_issue_v4_with_http_info(self, request):
        all_params = ['project_id', 'create_system_issue_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/system/issue',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSystemIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_attachment(self, request):
        """删除附件

        取消工作项与附件关联，如附件为工作项页面上传则删除附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAttachment
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteAttachmentRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteAttachmentResponse`
        """
        return self.delete_attachment_with_http_info(request)

    def delete_attachment_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'attachment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/attachments/{attachment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_issue_v4(self, request):
        """删除工作项

        删除工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteIssueV4Response`
        """
        return self.delete_issue_v4_with_http_info(request)

    def delete_issue_v4_with_http_info(self, request):
        all_params = ['project_id', 'issue_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_iteration_v4(self, request):
        """删除项目迭代

        删除项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteIterationV4Response`
        """
        return self.delete_iteration_v4_with_http_info(request)

    def delete_iteration_v4_with_http_info(self, request):
        all_params = ['project_id', 'iteration_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/iterations/{iteration_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_project_module(self, request):
        """删除项目的模块

        删除项目的模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProjectModule
        :type request: :class:`huaweicloudsdkprojectman.v4.DeleteProjectModuleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DeleteProjectModuleResponse`
        """
        return self.delete_project_module_with_http_info(request)

    def delete_project_module_with_http_info(self, request):
        all_params = ['project_id', 'module_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/modules/{module_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProjectModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_attachment(self, request):
        """下载工作项附件

        下载工作项附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAttachment
        :type request: :class:`huaweicloudsdkprojectman.v4.DownloadAttachmentRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DownloadAttachmentResponse`
        """
        return self.download_attachment_with_http_info(request)

    def download_attachment_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'attachment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/attachments/{attachment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadAttachmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_image_file(self, request):
        """下载图片

        下载图片
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadImageFile
        :type request: :class:`huaweicloudsdkprojectman.v4.DownloadImageFileRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.DownloadImageFileResponse`
        """
        return self.download_image_file_with_http_info(request)

    def download_image_file_with_http_info(self, request):
        all_params = ['project_id', 'image_uri']
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
        if 'image_uri' in local_var_params:
            query_params.append(('image_uri', local_var_params['image_uri']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/image-file',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadImageFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_associated_issues(self, request):
        """查询当前工作项已经关联的工作项

        查询当前工作项已经关联的工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssociatedIssues
        :type request: :class:`huaweicloudsdkprojectman.v4.ListAssociatedIssuesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListAssociatedIssuesResponse`
        """
        return self.list_associated_issues_with_http_info(request)

    def list_associated_issues_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/associated-issues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAssociatedIssuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_associated_test_cases(self, request):
        """查询关联用例

        查询关联用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssociatedTestCases
        :type request: :class:`huaweicloudsdkprojectman.v4.ListAssociatedTestCasesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListAssociatedTestCasesResponse`
        """
        return self.list_associated_test_cases_with_http_info(request)

    def list_associated_test_cases_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/associate-test-cases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAssociatedTestCasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_associated_wikis(self, request):
        """查询当前工作项已经关联的关联Wiki

        查询当前工作项已经关联的关联Wiki
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssociatedWikis
        :type request: :class:`huaweicloudsdkprojectman.v4.ListAssociatedWikisRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListAssociatedWikisResponse`
        """
        return self.list_associated_wikis_with_http_info(request)

    def list_associated_wikis_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/associated-wikis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAssociatedWikisResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_child_issues_v4(self, request):
        """获取子工作项

        获取子工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListChildIssuesV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListChildIssuesV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListChildIssuesV4Response`
        """
        return self.list_child_issues_v4_with_http_info(request)

    def list_child_issues_v4_with_http_info(self, request):
        all_params = ['project_id', 'issue_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/child',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListChildIssuesV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_issue_associated_commits(self, request):
        """查询当前工作项已经关联的代码提交记录 / 分支创建记录

        查询当前工作项已经关联的代码提交记录 / 分支创建记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueAssociatedCommits
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueAssociatedCommitsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueAssociatedCommitsResponse`
        """
        return self.list_issue_associated_commits_with_http_info(request)

    def list_issue_associated_commits_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'type', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/associated-commits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIssueAssociatedCommitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_issue_comments_v4(self, request):
        """获取指定工作项的评论列表

        获取工作项的评论
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueCommentsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueCommentsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueCommentsV4Response`
        """
        return self.list_issue_comments_v4_with_http_info(request)

    def list_issue_comments_v4_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/comments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIssueCommentsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_issue_custom_fields(self, request):
        """查询Scrum工作项自定义字段

        查询Scrum工作项自定义字段的可选列表,符合custom_fields或者names条件的都返回,2个值都不传，返回所有的自定义字段列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueCustomFields
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueCustomFieldsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueCustomFieldsResponse`
        """
        return self.list_issue_custom_fields_with_http_info(request)

    def list_issue_custom_fields_with_http_info(self, request):
        all_params = ['project_id', 'list_issue_custom_fields_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/custom-fields',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIssueCustomFieldsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_issue_records_v4(self, request):
        """获取工作项历史记录

        获取工作项历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssueRecordsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssueRecordsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssueRecordsV4Response`
        """
        return self.list_issue_records_v4_with_http_info(request)

    def list_issue_records_v4_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issue/{issue_id}/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIssueRecordsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_issues_sf_v4(self, request):
        """查询项目的工作项

        工作项类型id, 分页参数，创建时间查询项目的工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssuesSfV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssuesSfV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssuesSfV4Response`
        """
        return self.list_issues_sf_v4_with_http_info(request)

    def list_issues_sf_v4_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit', 'tracker_id', 'created_time_interval', 'updated_time_interval']
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIssuesSfV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_issues_v4(self, request):
        """高级查询工作项

        根据筛选条件查询工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIssuesV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIssuesV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIssuesV4Response`
        """
        return self.list_issues_v4_with_http_info(request)

    def list_issues_v4_with_http_info(self, request):
        all_params = ['project_id', 'list_issues_v4_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIssuesV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_iteration_histories(self, request):
        """查看迭代历史记录

        查看迭代历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIterationHistories
        :type request: :class:`huaweicloudsdkprojectman.v4.ListIterationHistoriesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListIterationHistoriesResponse`
        """
        return self.list_iteration_histories_with_http_info(request)

    def list_iteration_histories_with_http_info(self, request):
        all_params = ['iteration_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/iterations/{iteration_id}/histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIterationHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_domains(self, request):
        """查询项目的领域列表

        查询项目的领域列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectDomains
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectDomainsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectDomainsResponse`
        """
        return self.list_project_domains_with_http_info(request)

    def list_project_domains_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_issues_records_v4(self, request):
        """查询项目下所有工作项的历史记录

        查询项目下所有工作项的历史记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectIssuesRecordsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectIssuesRecordsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectIssuesRecordsV4Response`
        """
        return self.list_project_issues_records_v4_with_http_info(request)

    def list_project_issues_records_v4_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit', 'operated_time_interval']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'operated_time_interval' in local_var_params:
            query_params.append(('operated_time_interval', local_var_params['operated_time_interval']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectIssuesRecordsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_iterations_v4(self, request):
        """获取指定项目的迭代列表

        获取项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectIterationsV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectIterationsV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectIterationsV4Response`
        """
        return self.list_project_iterations_v4_with_http_info(request)

    def list_project_iterations_v4_with_http_info(self, request):
        all_params = ['project_id', 'updated_time_interval', 'include_deleted']
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
        if 'updated_time_interval' in local_var_params:
            query_params.append(('updated_time_interval', local_var_params['updated_time_interval']))
        if 'include_deleted' in local_var_params:
            query_params.append(('include_deleted', local_var_params['include_deleted']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/iterations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectIterationsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_modules(self, request):
        """查询项目的模块列表

        查询项目的模块列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectModules
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectModulesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectModulesResponse`
        """
        return self.list_project_modules_with_http_info(request)

    def list_project_modules_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/modules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectModulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_work_hours(self, request):
        """按用户查询工时（多项目）

        按用户查询工时（多项目）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectWorkHours
        :type request: :class:`huaweicloudsdkprojectman.v4.ListProjectWorkHoursRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListProjectWorkHoursResponse`
        """
        return self.list_project_work_hours_with_http_info(request)

    def list_project_work_hours_with_http_info(self, request):
        all_params = ['list_project_work_hours_request_body']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/work-hours',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectWorkHoursResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_scrum_project_statuses(self, request):
        """查询项目的状态列表

        查询项目的状态列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScrumProjectStatuses
        :type request: :class:`huaweicloudsdkprojectman.v4.ListScrumProjectStatusesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListScrumProjectStatusesResponse`
        """
        return self.list_scrum_project_statuses_with_http_info(request)

    def list_scrum_project_statuses_with_http_info(self, request):
        all_params = ['project_id', 'offset', 'limit', 'tracker_id']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/statuses',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListScrumProjectStatusesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_spec_issue_stay_times(self, request):
        """获取指定工作项停留时间

        获取指定工作项停留时间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpecIssueStayTimes
        :type request: :class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListSpecIssueStayTimesResponse`
        """
        return self.list_spec_issue_stay_times_with_http_info(request)

    def list_spec_issue_stay_times_with_http_info(self, request):
        all_params = ['list_spec_issue_stay_times_request']
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/issues/duration',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSpecIssueStayTimesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_status_statistic(self, request):
        """查询迭代下工作项状态的统计数据（处理人维度）

        查询迭代下工作项状态的统计数据（处理人维度）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStatusStatistic
        :type request: :class:`huaweicloudsdkprojectman.v4.ListStatusStatisticRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ListStatusStatisticResponse`
        """
        return self.list_status_statistic_with_http_info(request)

    def list_status_statistic_with_http_info(self, request):
        all_params = ['project_id', 'iteration_id', 'tracker_id', 'status_id']
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
        if 'iteration_id' in local_var_params:
            query_params.append(('iteration_id', local_var_params['iteration_id']))
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))
        if 'status_id' in local_var_params:
            query_params.append(('status_id', local_var_params['status_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/status-statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStatusStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_issue_completion_rate(self, request):
        """获取工作项完成率

        获取工作项的完成率
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssueCompletionRate
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIssueCompletionRateRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIssueCompletionRateResponse`
        """
        return self.show_issue_completion_rate_with_http_info(request)

    def show_issue_completion_rate_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issue-completion-rate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIssueCompletionRateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_issue_v4(self, request):
        """查询工作项详情

        查询工作项详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIssueV4Response`
        """
        return self.show_issue_v4_with_http_info(request)

    def show_issue_v4_with_http_info(self, request):
        all_params = ['project_id', 'issue_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_issues_wrok_flow_config(self, request):
        """查询Scrum项目的工作项流转配置

        查询Scrum项目的工作项流转配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIssuesWrokFlowConfig
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIssuesWrokFlowConfigRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIssuesWrokFlowConfigResponse`
        """
        return self.show_issues_wrok_flow_config_with_http_info(request)

    def show_issues_wrok_flow_config_with_http_info(self, request):
        all_params = ['project_id', 'tracker_id']
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
        if 'tracker_id' in local_var_params:
            query_params.append(('tracker_id', local_var_params['tracker_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/workflow/config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIssuesWrokFlowConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_iteration_v4(self, request):
        """查看迭代详情

        查看迭代详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIterationV4Response`
        """
        return self.show_iteration_v4_with_http_info(request)

    def show_iteration_v4_with_http_info(self, request):
        all_params = ['iteration_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'iteration_id' in local_var_params:
            path_params['iteration_id'] = local_var_params['iteration_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/iterations/{iteration_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_work_hours(self, request):
        """按用户查询工时（单项目）

        按用户查询工时（单项目）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectWorkHours
        :type request: :class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowProjectWorkHoursResponse`
        """
        return self.show_project_work_hours_with_http_info(request)

    def show_project_work_hours_with_http_info(self, request):
        all_params = ['project_id', 'show_project_work_hours_request_body']
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
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/work-hours',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectWorkHoursResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_issue_v4(self, request):
        """更新工作项

        更新工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIssueV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateIssueV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateIssueV4Response`
        """
        return self.update_issue_v4_with_http_info(request)

    def update_issue_v4_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'update_issue_v4_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_iteration_v4(self, request):
        """更新Scrum项目迭代

        更新Scrum项目迭代
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIterationV4
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateIterationV4Request`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateIterationV4Response`
        """
        return self.update_iteration_v4_with_http_info(request)

    def update_iteration_v4_with_http_info(self, request):
        all_params = ['project_id', 'iteration_id', 'update_iteration_v4_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/iterations/{iteration_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project_domain(self, request):
        """更新项目的领域

        更新项目的领域
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectDomain
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateProjectDomainRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateProjectDomainResponse`
        """
        return self.update_project_domain_with_http_info(request)

    def update_project_domain_with_http_info(self, request):
        all_params = ['project_id', 'domain_id', 'update_project_domain_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/domains/{domain_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProjectDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project_module(self, request):
        """更新项目的模块

        更新项目的模块
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectModule
        :type request: :class:`huaweicloudsdkprojectman.v4.UpdateProjectModuleRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UpdateProjectModuleResponse`
        """
        return self.update_project_module_with_http_info(request)

    def update_project_module_with_http_info(self, request):
        all_params = ['project_id', 'module_id', 'update_project_module_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/modules/{module_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProjectModuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_attachments(self, request):
        """上传工作项附件

        上传工作项附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadAttachments
        :type request: :class:`huaweicloudsdkprojectman.v4.UploadAttachmentsRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UploadAttachmentsResponse`
        """
        return self.upload_attachments_with_http_info(request)

    def upload_attachments_with_http_info(self, request):
        all_params = ['project_id', 'issue_id', 'attachment']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/attachments/upload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadAttachmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_issue_img(self, request):
        """上传图片

        上传图片
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadIssueImg
        :type request: :class:`huaweicloudsdkprojectman.v4.UploadIssueImgRequest`
        :rtype: :class:`huaweicloudsdkprojectman.v4.UploadIssueImgResponse`
        """
        return self.upload_issue_img_with_http_info(request)

    def upload_issue_img_with_http_info(self, request):
        all_params = ['project_id', 'file']
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v2/{project_id}/img',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadIssueImgResponse',
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

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


class ProjectManAsyncClient(Client):
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
        super(ProjectManAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkprojectman.v4.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def create_project_v4_async(self, request):
        """创建项目

        创建项目

        :param CreateProjectV4Request request
        :return: CreateProjectV4Response
        """
        return self.create_project_v4_with_http_info(request)

    def create_project_v4_with_http_info(self, request):
        """创建项目

        创建项目

        :param CreateProjectV4Request request
        :return: CreateProjectV4Response
        """

        all_params = ['create_project_v4_request_body']
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
            response_type='CreateProjectV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domain_not_added_projects_v4_async(self, request):
        """获取租户没有加入的项目

        获取租户没有加入的项目

        :param ListDomainNotAddedProjectsV4Request request
        :return: ListDomainNotAddedProjectsV4Response
        """
        return self.list_domain_not_added_projects_v4_with_http_info(request)

    def list_domain_not_added_projects_v4_with_http_info(self, request):
        """获取租户没有加入的项目

        获取租户没有加入的项目

        :param ListDomainNotAddedProjectsV4Request request
        :return: ListDomainNotAddedProjectsV4Response
        """

        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/domain/not-added',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDomainNotAddedProjectsV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issue_comments_v4_async(self, request):
        """获取指定工作项的评论列表

        获取工作项的评论

        :param ListIssueCommentsV4Request request
        :return: ListIssueCommentsV4Response
        """
        return self.list_issue_comments_v4_with_http_info(request)

    def list_issue_comments_v4_with_http_info(self, request):
        """获取指定工作项的评论列表

        获取工作项的评论

        :param ListIssueCommentsV4Request request
        :return: ListIssueCommentsV4Response
        """

        all_params = ['project_id', 'issue_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issues/{issue_id}/comments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIssueCommentsV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issue_records_v4_async(self, request):
        """获取工作项历史记录

        获取项目成员列表

        :param ListIssueRecordsV4Request request
        :return: ListIssueRecordsV4Response
        """
        return self.list_issue_records_v4_with_http_info(request)

    def list_issue_records_v4_with_http_info(self, request):
        """获取工作项历史记录

        获取项目成员列表

        :param ListIssueRecordsV4Request request
        :return: ListIssueRecordsV4Response
        """

        all_params = ['project_id', 'issue_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issue/{issue_id}/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListIssueRecordsV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_members_v4_async(self, request):
        """获取指定项目的成员用户列表

        获取项目成员列表

        :param ListProjectMembersV4Request request
        :return: ListProjectMembersV4Response
        """
        return self.list_project_members_v4_with_http_info(request)

    def list_project_members_v4_with_http_info(self, request):
        """获取指定项目的成员用户列表

        获取项目成员列表

        :param ListProjectMembersV4Request request
        :return: ListProjectMembersV4Response
        """

        all_params = ['project_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectMembersV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_versions_v4_async(self, request):
        """获取指定项目的迭代列表

        获取项目迭代

        :param ListProjectVersionsV4Request request
        :return: ListProjectVersionsV4Response
        """
        return self.list_project_versions_v4_with_http_info(request)

    def list_project_versions_v4_with_http_info(self, request):
        """获取指定项目的迭代列表

        获取项目迭代

        :param ListProjectVersionsV4Request request
        :return: ListProjectVersionsV4Response
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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/iterations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectVersionsV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_work_hours_async(self, request):
        """按用户查询工时（多项目）

        按用户查询工时（多项目）

        :param ListProjectWorkHoursRequest request
        :return: ListProjectWorkHoursResponse
        """
        return self.list_project_work_hours_with_http_info(request)

    def list_project_work_hours_with_http_info(self, request):
        """按用户查询工时（多项目）

        按用户查询工时（多项目）

        :param ListProjectWorkHoursRequest request
        :return: ListProjectWorkHoursResponse
        """

        all_params = ['list_project_work_hours_request_body']
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
            response_type='ListProjectWorkHoursResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_projects_v4_async(self, request):
        """查询项目列表

        查询项目列表

        :param ListProjectsV4Request request
        :return: ListProjectsV4Response
        """
        return self.list_projects_v4_with_http_info(request)

    def list_projects_v4_with_http_info(self, request):
        """查询项目列表

        查询项目列表

        :param ListProjectsV4Request request
        :return: ListProjectsV4Response
        """

        all_params = ['offset', 'limit', 'search', 'project_type', 'sort', 'archive', 'query_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectsV4Response',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_project_async(self, request):
        """主动退出项目

        项目成员主动退出项目，项目创建者不能退出

        :param RemoveProjectRequest request
        :return: RemoveProjectResponse
        """
        return self.remove_project_with_http_info(request)

    def remove_project_with_http_info(self, request):
        """主动退出项目

        项目成员主动退出项目，项目创建者不能退出

        :param RemoveProjectRequest request
        :return: RemoveProjectResponse
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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/quit',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemoveProjectResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cur_user_info_async(self, request):
        """获取当前用户信息

        获取当前用户信息

        :param ShowCurUserInfoRequest request
        :return: ShowCurUserInfoResponse
        """
        return self.show_cur_user_info_with_http_info(request)

    def show_cur_user_info_with_http_info(self, request):
        """获取当前用户信息

        获取当前用户信息

        :param ShowCurUserInfoRequest request
        :return: ShowCurUserInfoResponse
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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCurUserInfoResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cur_user_role_async(self, request):
        """获取当前用户角色

        获取用户在项目中的角色

        :param ShowCurUserRoleRequest request
        :return: ShowCurUserRoleResponse
        """
        return self.show_cur_user_role_with_http_info(request)

    def show_cur_user_role_with_http_info(self, request):
        """获取当前用户角色

        获取用户在项目中的角色

        :param ShowCurUserRoleRequest request
        :return: ShowCurUserRoleResponse
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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/user-role',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCurUserRoleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_work_hours_async(self, request):
        """按用户查询工时（单项目）

        按用户查询工时（单项目）

        :param ShowProjectWorkHoursRequest request
        :return: ShowProjectWorkHoursResponse
        """
        return self.show_project_work_hours_with_http_info(request)

    def show_project_work_hours_with_http_info(self, request):
        """按用户查询工时（单项目）

        按用户查询工时（单项目）

        :param ShowProjectWorkHoursRequest request
        :return: ShowProjectWorkHoursResponse
        """

        all_params = ['project_id', 'show_project_work_hours_request_body']
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
            response_type='ShowProjectWorkHoursResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def showt_issue_completion_rate_async(self, request):
        """获取工作项完成率

        获取工作项的完成率

        :param ShowtIssueCompletionRateRequest request
        :return: ShowtIssueCompletionRateResponse
        """
        return self.showt_issue_completion_rate_with_http_info(request)

    def showt_issue_completion_rate_with_http_info(self, request):
        """获取工作项完成率

        获取工作项的完成率

        :param ShowtIssueCompletionRateRequest request
        :return: ShowtIssueCompletionRateResponse
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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v4/projects/{project_id}/issue-completion-rate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowtIssueCompletionRateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_membes_role_v4_async(self, request):
        """更新成员在项目中的角色

        更新成员在项目中的角色

        :param UpdateMembesRoleV4Request request
        :return: UpdateMembesRoleV4Response
        """
        return self.update_membes_role_v4_with_http_info(request)

    def update_membes_role_v4_with_http_info(self, request):
        """更新成员在项目中的角色

        更新成员在项目中的角色

        :param UpdateMembesRoleV4Request request
        :return: UpdateMembesRoleV4Response
        """

        all_params = ['project_id', 'update_membes_role_v4_request_body']
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
            response_type='UpdateMembesRoleV4Response',
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
            request_type=request_type,
	    async_request=True)

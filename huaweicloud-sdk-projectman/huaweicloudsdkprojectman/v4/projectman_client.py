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

        :param AddApplyJoinProjectForAgcRequest request
        :return: AddApplyJoinProjectForAgcResponse
        """
        return self.add_apply_join_project_for_agc_with_http_info(request)

    def add_apply_join_project_for_agc_with_http_info(self, request):
        """AGC调用 当前用户申请加入项目

        AGC调用 当前用户申请加入项目, 申请的用户id写在header中

        :param AddApplyJoinProjectForAgcRequest request
        :return: AddApplyJoinProjectForAgcResponse
        """

        all_params = ['domain_id', 'user_id', 'project_id']
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
            response_type='AddApplyJoinProjectForAgcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_member_v4(self, request):
        """添加项目成员

        添加项目成员,可以添加跨租户成员

        :param AddMemberV4Request request
        :return: AddMemberV4Response
        """
        return self.add_member_v4_with_http_info(request)

    def add_member_v4_with_http_info(self, request):
        """添加项目成员

        添加项目成员,可以添加跨租户成员

        :param AddMemberV4Request request
        :return: AddMemberV4Response
        """

        all_params = ['project_id', 'add_member_v4_request_body']
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
            response_type='AddMemberV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_add_members_v4(self, request):
        """批量添加项目成员

        批量添加项目成员，只能添加和项目创建者同一租户下的成员，不正确的用户id会略过，添加的用户超过权限的，默认角色设置为7

        :param BatchAddMembersV4Request request
        :return: BatchAddMembersV4Response
        """
        return self.batch_add_members_v4_with_http_info(request)

    def batch_add_members_v4_with_http_info(self, request):
        """批量添加项目成员

        批量添加项目成员，只能添加和项目创建者同一租户下的成员，不正确的用户id会略过，添加的用户超过权限的，默认角色设置为7

        :param BatchAddMembersV4Request request
        :return: BatchAddMembersV4Response
        """

        all_params = ['project_id', 'batch_add_members_v4_request_body']
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
            response_type='BatchAddMembersV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_iterations_v4(self, request):
        """批量删除项目的迭代

        批量删除项目的迭代

        :param BatchDeleteIterationsV4Request request
        :return: BatchDeleteIterationsV4Response
        """
        return self.batch_delete_iterations_v4_with_http_info(request)

    def batch_delete_iterations_v4_with_http_info(self, request):
        """批量删除项目的迭代

        批量删除项目的迭代

        :param BatchDeleteIterationsV4Request request
        :return: BatchDeleteIterationsV4Response
        """

        all_params = ['project_id', 'batch_delete_iterations_v4_request_body']
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
            response_type='BatchDeleteIterationsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_members_v4(self, request):
        """批量删除项目成员

        批量删除项目成员

        :param BatchDeleteMembersV4Request request
        :return: BatchDeleteMembersV4Response
        """
        return self.batch_delete_members_v4_with_http_info(request)

    def batch_delete_members_v4_with_http_info(self, request):
        """批量删除项目成员

        批量删除项目成员

        :param BatchDeleteMembersV4Request request
        :return: BatchDeleteMembersV4Response
        """

        all_params = ['project_id', 'batch_delete_members_v4_request_body']
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
            response_type='BatchDeleteMembersV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def check_project_name_v4(self, request):
        """检查项目名称是否存在

        更新项目

        :param CheckProjectNameV4Request request
        :return: CheckProjectNameV4Response
        """
        return self.check_project_name_v4_with_http_info(request)

    def check_project_name_v4_with_http_info(self, request):
        """检查项目名称是否存在

        更新项目

        :param CheckProjectNameV4Request request
        :return: CheckProjectNameV4Response
        """

        all_params = ['check_project_name_v4_request_body']
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
            response_type='CheckProjectNameV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_iteration_v4(self, request):
        """创建Scrum项目迭代

        创建Scrum项目迭代

        :param CreateIterationV4Request request
        :return: CreateIterationV4Response
        """
        return self.create_iteration_v4_with_http_info(request)

    def create_iteration_v4_with_http_info(self, request):
        """创建Scrum项目迭代

        创建Scrum项目迭代

        :param CreateIterationV4Request request
        :return: CreateIterationV4Response
        """

        all_params = ['project_id', 'create_iteration_v4_request_body']
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
            response_type='CreateIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_project_v4(self, request):
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
            response_type='CreateProjectV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_iteration_v4(self, request):
        """删除项目迭代

        删除项目迭代

        :param DeleteIterationV4Request request
        :return: DeleteIterationV4Response
        """
        return self.delete_iteration_v4_with_http_info(request)

    def delete_iteration_v4_with_http_info(self, request):
        """删除项目迭代

        删除项目迭代

        :param DeleteIterationV4Request request
        :return: DeleteIterationV4Response
        """

        all_params = ['project_id', 'iteration_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='DeleteIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_project_v4(self, request):
        """删除项目

        删除项目

        :param DeleteProjectV4Request request
        :return: DeleteProjectV4Response
        """
        return self.delete_project_v4_with_http_info(request)

    def delete_project_v4_with_http_info(self, request):
        """删除项目

        删除项目

        :param DeleteProjectV4Request request
        :return: DeleteProjectV4Response
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
            response_type='DeleteProjectV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_domain_not_added_projects_v4(self, request):
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
            response_type='ListDomainNotAddedProjectsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_bug_statics_v4(self, request):
        """获取bug统计信息

        获取bug统计信息，按模块统计

        :param ListProjectBugStaticsV4Request request
        :return: ListProjectBugStaticsV4Response
        """
        return self.list_project_bug_statics_v4_with_http_info(request)

    def list_project_bug_statics_v4_with_http_info(self, request):
        """获取bug统计信息

        获取bug统计信息，按模块统计

        :param ListProjectBugStaticsV4Request request
        :return: ListProjectBugStaticsV4Response
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
            response_type='ListProjectBugStaticsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_demand_static_v4(self, request):
        """获取需求统计信息

        获取需求统计信息

        :param ListProjectDemandStaticV4Request request
        :return: ListProjectDemandStaticV4Response
        """
        return self.list_project_demand_static_v4_with_http_info(request)

    def list_project_demand_static_v4_with_http_info(self, request):
        """获取需求统计信息

        获取需求统计信息

        :param ListProjectDemandStaticV4Request request
        :return: ListProjectDemandStaticV4Response
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
            response_type='ListProjectDemandStaticV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_iterations_v4(self, request):
        """获取指定项目的迭代列表

        获取项目迭代

        :param ListProjectIterationsV4Request request
        :return: ListProjectIterationsV4Response
        """
        return self.list_project_iterations_v4_with_http_info(request)

    def list_project_iterations_v4_with_http_info(self, request):
        """获取指定项目的迭代列表

        获取项目迭代

        :param ListProjectIterationsV4Request request
        :return: ListProjectIterationsV4Response
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
            response_type='ListProjectIterationsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_members_v4(self, request):
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
            response_type='ListProjectMembersV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_projects_v4(self, request):
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
            response_type='ListProjectsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_project(self, request):
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
            response_type='RemoveProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cur_user_info(self, request):
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
            response_type='ShowCurUserInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cur_user_role(self, request):
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
            response_type='ShowCurUserRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_iteration_v4(self, request):
        """查看迭代详情

        查看迭代详情

        :param ShowIterationV4Request request
        :return: ShowIterationV4Response
        """
        return self.show_iteration_v4_with_http_info(request)

    def show_iteration_v4_with_http_info(self, request):
        """查看迭代详情

        查看迭代详情

        :param ShowIterationV4Request request
        :return: ShowIterationV4Response
        """

        all_params = ['iteration_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_summary_v4(self, request):
        """获取项目概览

        获取项目概览

        :param ShowProjectSummaryV4Request request
        :return: ShowProjectSummaryV4Response
        """
        return self.show_project_summary_v4_with_http_info(request)

    def show_project_summary_v4_with_http_info(self, request):
        """获取项目概览

        获取项目概览

        :param ShowProjectSummaryV4Request request
        :return: ShowProjectSummaryV4Response
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
            response_type='ShowProjectSummaryV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_iteration_v4(self, request):
        """更新Scrum项目迭代

        更新Scrum项目迭代

        :param UpdateIterationV4Request request
        :return: UpdateIterationV4Response
        """
        return self.update_iteration_v4_with_http_info(request)

    def update_iteration_v4_with_http_info(self, request):
        """更新Scrum项目迭代

        更新Scrum项目迭代

        :param UpdateIterationV4Request request
        :return: UpdateIterationV4Response
        """

        all_params = ['project_id', 'iteration_id', 'update_iteration_v4_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='UpdateIterationV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_membes_role_v4(self, request):
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
            response_type='UpdateMembesRoleV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_nick_name_v4(self, request):
        """更新用户昵称

        更新用户昵称

        :param UpdateNickNameV4Request request
        :return: UpdateNickNameV4Response
        """
        return self.update_nick_name_v4_with_http_info(request)

    def update_nick_name_v4_with_http_info(self, request):
        """更新用户昵称

        更新用户昵称

        :param UpdateNickNameV4Request request
        :return: UpdateNickNameV4Response
        """

        all_params = ['update_nick_name_v4_request_body']
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
            response_type='UpdateNickNameV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_project_v4(self, request):
        """更新项目

        更新项目

        :param UpdateProjectV4Request request
        :return: UpdateProjectV4Response
        """
        return self.update_project_v4_with_http_info(request)

    def update_project_v4_with_http_info(self, request):
        """更新项目

        更新项目

        :param UpdateProjectV4Request request
        :return: UpdateProjectV4Response
        """

        all_params = ['project_id', 'update_project_v4_request_body']
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
            response_type='UpdateProjectV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_issues_v4(self, request):
        """批量删除工作项

        批量删除工作项

        :param BatchDeleteIssuesV4Request request
        :return: BatchDeleteIssuesV4Response
        """
        return self.batch_delete_issues_v4_with_http_info(request)

    def batch_delete_issues_v4_with_http_info(self, request):
        """批量删除工作项

        批量删除工作项

        :param BatchDeleteIssuesV4Request request
        :return: BatchDeleteIssuesV4Response
        """

        all_params = ['project_id', 'batch_delete_issues_v4_request_body']
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
            response_type='BatchDeleteIssuesV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_issue_v4(self, request):
        """创建工作项

        创建工作项

        :param CreateIssueV4Request request
        :return: CreateIssueV4Response
        """
        return self.create_issue_v4_with_http_info(request)

    def create_issue_v4_with_http_info(self, request):
        """创建工作项

        创建工作项

        :param CreateIssueV4Request request
        :return: CreateIssueV4Response
        """

        all_params = ['project_id', 'create_issue_v4_request_body']
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
            response_type='CreateIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_issue_v4(self, request):
        """删除工作项

        删除工作项

        :param DeleteIssueV4Request request
        :return: DeleteIssueV4Response
        """
        return self.delete_issue_v4_with_http_info(request)

    def delete_issue_v4_with_http_info(self, request):
        """删除工作项

        删除工作项

        :param DeleteIssueV4Request request
        :return: DeleteIssueV4Response
        """

        all_params = ['project_id', 'issue_id']
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
            response_type='DeleteIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_child_issues_v4(self, request):
        """获取子工作项

        获取子工作项

        :param ListChildIssuesV4Request request
        :return: ListChildIssuesV4Response
        """
        return self.list_child_issues_v4_with_http_info(request)

    def list_child_issues_v4_with_http_info(self, request):
        """获取子工作项

        获取子工作项

        :param ListChildIssuesV4Request request
        :return: ListChildIssuesV4Response
        """

        all_params = ['project_id', 'issue_id']
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
            response_type='ListChildIssuesV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issue_comments_v4(self, request):
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
            response_type='ListIssueCommentsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issue_records_v4(self, request):
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
            response_type='ListIssueRecordsV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_issues_v4(self, request):
        """高级查询工作项

        高级查询工作项,根据筛选条件查询工作中

        :param ListIssuesV4Request request
        :return: ListIssuesV4Response
        """
        return self.list_issues_v4_with_http_info(request)

    def list_issues_v4_with_http_info(self, request):
        """高级查询工作项

        高级查询工作项,根据筛选条件查询工作中

        :param ListIssuesV4Request request
        :return: ListIssuesV4Response
        """

        all_params = ['project_id', 'list_issues_v4_request_body']
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
            response_type='ListIssuesV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_work_hours(self, request):
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
            response_type='ListProjectWorkHoursResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_issue_v4(self, request):
        """查询工作项详情

        查询工作项详情

        :param ShowIssueV4Request request
        :return: ShowIssueV4Response
        """
        return self.show_issue_v4_with_http_info(request)

    def show_issue_v4_with_http_info(self, request):
        """查询工作项详情

        查询工作项详情

        :param ShowIssueV4Request request
        :return: ShowIssueV4Response
        """

        all_params = ['project_id', 'issue_id']
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
            response_type='ShowIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_project_work_hours(self, request):
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
            response_type='ShowProjectWorkHoursResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def showt_issue_completion_rate(self, request):
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
            response_type='ShowtIssueCompletionRateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_issue_v4(self, request):
        """更新工作项

        更新工作项

        :param UpdateIssueV4Request request
        :return: UpdateIssueV4Response
        """
        return self.update_issue_v4_with_http_info(request)

    def update_issue_v4_with_http_info(self, request):
        """更新工作项

        更新工作项

        :param UpdateIssueV4Request request
        :return: UpdateIssueV4Response
        """

        all_params = ['project_id', 'issue_id', 'update_issue_v4_request_body']
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
            response_type='UpdateIssueV4Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

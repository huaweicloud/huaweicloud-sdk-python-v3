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


class CodeHubClient(Client):
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
        super(CodeHubClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodehub.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CodeHubClient":
            raise TypeError("client type error, support client type is CodeHubClient")

        return ClientBuilder(clazz)

    def create_commit(self, request):
        """创建提交

        能够一次提交位于不同目录的多个文件，目录不存在时，能自动创建目录。支持强制覆盖选项，当选择强制覆盖标志为true时，忽略冲突，强制提交。

        :param CreateCommitRequest request
        :return: CreateCommitResponse
        """
        return self.create_commit_with_http_info(request)

    def create_commit_with_http_info(self, request):
        """创建提交

        能够一次提交位于不同目录的多个文件，目录不存在时，能自动创建目录。支持强制覆盖选项，当选择强制覆盖标志为true时，忽略冲突，强制提交。

        :param CreateCommitRequest request
        :return: CreateCommitResponse
        """

        all_params = ['repo_id', 'create_commit_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']

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
            resource_path='/v2/projects/{repo_id}/repository/commits',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_commits(self, request):
        """查询某个仓库的提交信息

        根据仓库短ID获取提交信息，支持根据文件路径，查询这个路径下所有的commits列表。

        :param ListCommitsRequest request
        :return: ListCommitsResponse
        """
        return self.list_commits_with_http_info(request)

    def list_commits_with_http_info(self, request):
        """查询某个仓库的提交信息

        根据仓库短ID获取提交信息，支持根据文件路径，查询这个路径下所有的commits列表。

        :param ListCommitsRequest request
        :return: ListCommitsResponse
        """

        all_params = ['repo_id', 'ref_name', 'since', 'until', 'path', 'all', 'with_stats']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']

        query_params = []
        if 'ref_name' in local_var_params:
            query_params.append(('ref_name', local_var_params['ref_name']))
        if 'since' in local_var_params:
            query_params.append(('since', local_var_params['since']))
        if 'until' in local_var_params:
            query_params.append(('until', local_var_params['until']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'all' in local_var_params:
            query_params.append(('all', local_var_params['all']))
        if 'with_stats' in local_var_params:
            query_params.append(('with_stats', local_var_params['with_stats']))

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
            resource_path='/v2/projects/{repo_id}/repository/commits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCommitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_diff_commit(self, request):
        """查询某个仓库的提交差异信息

        根据commit id查询提交差异信息。

        :param ShowDiffCommitRequest request
        :return: ShowDiffCommitResponse
        """
        return self.show_diff_commit_with_http_info(request)

    def show_diff_commit_with_http_info(self, request):
        """查询某个仓库的提交差异信息

        根据commit id查询提交差异信息。

        :param ShowDiffCommitRequest request
        :return: ShowDiffCommitResponse
        """

        all_params = ['repo_id', 'sha']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']
        if 'sha' in local_var_params:
            path_params['sha'] = local_var_params['sha']

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
            resource_path='/v2/projects/{repo_id}/repository/commits/{sha}/diff',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDiffCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_single_commit(self, request):
        """查询某个仓库的特定提交信息

        获取由commit id或分支或标记的名称标识的特定提交。

        :param ShowSingleCommitRequest request
        :return: ShowSingleCommitResponse
        """
        return self.show_single_commit_with_http_info(request)

    def show_single_commit_with_http_info(self, request):
        """查询某个仓库的特定提交信息

        获取由commit id或分支或标记的名称标识的特定提交。

        :param ShowSingleCommitRequest request
        :return: ShowSingleCommitResponse
        """

        all_params = ['repo_id', 'sha', 'stats']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']
        if 'sha' in local_var_params:
            path_params['sha'] = local_var_params['sha']

        query_params = []
        if 'stats' in local_var_params:
            query_params.append(('stats', local_var_params['stats']))

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
            resource_path='/v2/projects/{repo_id}/repository/commits/{sha}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSingleCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_file(self, request):
        """查询某个仓库的文件信息

        获取仓库中文件的信息，如名称、大小、内容。请注意，文件内容是Base64编码的。

        :param ShowFileRequest request
        :return: ShowFileResponse
        """
        return self.show_file_with_http_info(request)

    def show_file_with_http_info(self, request):
        """查询某个仓库的文件信息

        获取仓库中文件的信息，如名称、大小、内容。请注意，文件内容是Base64编码的。

        :param ShowFileRequest request
        :return: ShowFileResponse
        """

        all_params = ['repo_id', 'file_path', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']
        if 'file_path' in local_var_params:
            path_params['file_path'] = local_var_params['file_path']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))

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
            resource_path='/v2/projects/{repo_id}/repository/files/{file_path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def get_all_repository_by_project_id(self, request):
        """获取项目下所有仓库信息

        获取仓库列表 模糊查询支持范围,如果未传入project_id，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配。

        :param GetAllRepositoryByProjectIdRequest request
        :return: GetAllRepositoryByProjectIdResponse
        """
        return self.get_all_repository_by_project_id_with_http_info(request)

    def get_all_repository_by_project_id_with_http_info(self, request):
        """获取项目下所有仓库信息

        获取仓库列表 模糊查询支持范围,如果未传入project_id，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配。

        :param GetAllRepositoryByProjectIdRequest request
        :return: GetAllRepositoryByProjectIdResponse
        """

        all_params = ['project_uuid', 'page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

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
            resource_path='/v1/projects/{project_uuid}/repositories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GetAllRepositoryByProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def get_product_templates(self, request):
        """获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表

        :param GetProductTemplatesRequest request
        :return: GetProductTemplatesResponse
        """
        return self.get_product_templates_with_http_info(request)

    def get_product_templates_with_http_info(self, request):
        """获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表

        :param GetProductTemplatesRequest request
        :return: GetProductTemplatesResponse
        """

        all_params = ['project_uuid', 'page_no', 'page_size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']

        query_params = []
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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
            resource_path='/v1/projects/{project_uuid}/repositories/template_status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GetProductTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_product_two_templates(self, request):
        """获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表

        :param ListProductTwoTemplatesRequest request
        :return: ListProductTwoTemplatesResponse
        """
        return self.list_product_two_templates_with_http_info(request)

    def list_product_two_templates_with_http_info(self, request):
        """获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表

        :param ListProductTwoTemplatesRequest request
        :return: ListProductTwoTemplatesResponse
        """

        all_params = ['project_uuid', 'page_no', 'page_size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']

        query_params = []
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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
            resource_path='/v2/projects/{project_uuid}/repositories/template-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProductTwoTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_repository_name_exist(self, request):
        """校验指定项目下的仓库名

        一般创建仓库时调用。通过传入项目uuid,仓库名，调用CoudeHubAdapter接口，查询数据库来判断仓库是否重名。

        :param ShowRepositoryNameExistRequest request
        :return: ShowRepositoryNameExistResponse
        """
        return self.show_repository_name_exist_with_http_info(request)

    def show_repository_name_exist_with_http_info(self, request):
        """校验指定项目下的仓库名

        一般创建仓库时调用。通过传入项目uuid,仓库名，调用CoudeHubAdapter接口，查询数据库来判断仓库是否重名。

        :param ShowRepositoryNameExistRequest request
        :return: ShowRepositoryNameExistResponse
        """

        all_params = ['project_uuid', 'repository_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

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
            resource_path='/v1/projects/{project_uuid}/repositories/validation/{repository_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRepositoryNameExistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_repo_members(self, request):
        """添加仓库成员

        调用方codehubportal,添加仓库成员。

        :param AddRepoMembersRequest request
        :return: AddRepoMembersResponse
        """
        return self.add_repo_members_with_http_info(request)

    def add_repo_members_with_http_info(self, request):
        """添加仓库成员

        调用方codehubportal,添加仓库成员。

        :param AddRepoMembersRequest request
        :return: AddRepoMembersResponse
        """

        all_params = ['repository_uuid', 'create_repo_member_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/members',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddRepoMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_repo_member(self, request):
        """删除仓库成员

        删除仓库成员

        :param DeleteRepoMemberRequest request
        :return: DeleteRepoMemberResponse
        """
        return self.delete_repo_member_with_http_info(request)

    def delete_repo_member_with_http_info(self, request):
        """删除仓库成员

        删除仓库成员

        :param DeleteRepoMemberRequest request
        :return: DeleteRepoMemberResponse
        """

        all_params = ['member_id', 'repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/members/{member_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRepoMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_repo_members(self, request):
        """获取仓库所有成员记录

        获取仓库成员列表,可通过关键字搜索某成员。

        :param ListRepoMembersRequest request
        :return: ListRepoMembersResponse
        """
        return self.list_repo_members_with_http_info(request)

    def list_repo_members_with_http_info(self, request):
        """获取仓库所有成员记录

        获取仓库成员列表,可通过关键字搜索某成员。

        :param ListRepoMembersRequest request
        :return: ListRepoMembersResponse
        """

        all_params = ['repository_uuid', 'page_index', 'page_size', 'subject']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'subject' in local_var_params:
            query_params.append(('subject', local_var_params['subject']))

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
            resource_path='/v1/repositories/{repository_uuid}/members',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRepoMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_repo_role(self, request):
        """设置成员在仓库中的角色

        给仓库中成员设置仓库的操作权限，

        :param SetRepoRoleRequest request
        :return: SetRepoRoleResponse
        """
        return self.set_repo_role_with_http_info(request)

    def set_repo_role_with_http_info(self, request):
        """设置成员在仓库中的角色

        给仓库中成员设置仓库的操作权限，

        :param SetRepoRoleRequest request
        :return: SetRepoRoleResponse
        """

        all_params = ['member_id', 'repository_uuid', 'set_repo_role_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'member_id' in local_var_params:
            path_params['member_id'] = local_var_params['member_id']
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/members/{member_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetRepoRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_deploy_key(self, request):
        """添加部署密钥

        添加部署密钥

        :param AddDeployKeyRequest request
        :return: AddDeployKeyResponse
        """
        return self.add_deploy_key_with_http_info(request)

    def add_deploy_key_with_http_info(self, request):
        """添加部署密钥

        添加部署密钥

        :param AddDeployKeyRequest request
        :return: AddDeployKeyResponse
        """

        all_params = ['repository_id', 'add_deploy_key_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v1/repositories/{repository_id}/deploy_keys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeployKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_deploy_key_v2(self, request):
        """添加部署密钥

        添加部署密钥

        :param AddDeployKeyV2Request request
        :return: AddDeployKeyV2Response
        """
        return self.add_deploy_key_v2_with_http_info(request)

    def add_deploy_key_v2_with_http_info(self, request):
        """添加部署密钥

        添加部署密钥

        :param AddDeployKeyV2Request request
        :return: AddDeployKeyV2Response
        """

        all_params = ['repository_id', 'add_deploy_key_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v2/repositories/{repository_id}/deploy-keys',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDeployKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_repository(self, request):
        """创建仓库

        用指定的名称在指定项目上创建仓库。传入参数：仓库名、模板id、是否导入项目成员、归属项目

        :param CreateRepositoryRequest request
        :return: CreateRepositoryResponse
        """
        return self.create_repository_with_http_info(request)

    def create_repository_with_http_info(self, request):
        """创建仓库

        用指定的名称在指定项目上创建仓库。传入参数：仓库名、模板id、是否导入项目成员、归属项目

        :param CreateRepositoryRequest request
        :return: CreateRepositoryResponse
        """

        all_params = ['create_repo_request']
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
            resource_path='/v1/repositories',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_deploy_key(self, request):
        """删除仓库部署密钥

        删除仓库部署密钥

        :param DeleteDeployKeyRequest request
        :return: DeleteDeployKeyResponse
        """
        return self.delete_deploy_key_with_http_info(request)

    def delete_deploy_key_with_http_info(self, request):
        """删除仓库部署密钥

        删除仓库部署密钥

        :param DeleteDeployKeyRequest request
        :return: DeleteDeployKeyResponse
        """

        all_params = ['key_id', 'repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v1/repositories/{repository_id}/deploy_keys/{key_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeployKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_deploy_key_v2(self, request):
        """删除仓库部署密钥

        删除仓库部署密钥

        :param DeleteDeployKeyV2Request request
        :return: DeleteDeployKeyV2Response
        """
        return self.delete_deploy_key_v2_with_http_info(request)

    def delete_deploy_key_v2_with_http_info(self, request):
        """删除仓库部署密钥

        删除仓库部署密钥

        :param DeleteDeployKeyV2Request request
        :return: DeleteDeployKeyV2Response
        """

        all_params = ['key_id', 'repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v2/repositories/{repository_id}/deploy-keys/{key_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeployKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_repository(self, request):
        """删除仓库

        根据仓库32位uuid删除指定的仓库

        :param DeleteRepositoryRequest request
        :return: DeleteRepositoryResponse
        """
        return self.delete_repository_with_http_info(request)

    def delete_repository_with_http_info(self, request):
        """删除仓库

        根据仓库32位uuid删除指定的仓库

        :param DeleteRepositoryRequest request
        :return: DeleteRepositoryResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def get_repository_by_project_id(self, request):
        """查询项目下的某个仓库

        不建议再使用,建议使用/{repository_uuid}/status

        :param GetRepositoryByProjectIdRequest request
        :return: GetRepositoryByProjectIdResponse
        """
        return self.get_repository_by_project_id_with_http_info(request)

    def get_repository_by_project_id_with_http_info(self, request):
        """查询项目下的某个仓库

        不建议再使用,建议使用/{repository_uuid}/status

        :param GetRepositoryByProjectIdRequest request
        :return: GetRepositoryByProjectIdResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GetRepositoryByProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def get_templates(self, request):
        """获取公开示例模板列表

        获取公开示例模板列表

        :param GetTemplatesRequest request
        :return: GetTemplatesResponse
        """
        return self.get_templates_with_http_info(request)

    def get_templates_with_http_info(self, request):
        """获取公开示例模板列表

        获取公开示例模板列表

        :param GetTemplatesRequest request
        :return: GetTemplatesResponse
        """

        all_params = ['page_no', 'page_size', 'platform', 'language', 'pipeline', 'entertype', 'search', 'dateorder', 'usedtimeorder', 'type', 'region']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'pipeline' in local_var_params:
            query_params.append(('pipeline', local_var_params['pipeline']))
        if 'entertype' in local_var_params:
            query_params.append(('entertype', local_var_params['entertype']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'dateorder' in local_var_params:
            query_params.append(('dateorder', local_var_params['dateorder']))
        if 'usedtimeorder' in local_var_params:
            query_params.append(('usedtimeorder', local_var_params['usedtimeorder']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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
            resource_path='/v1/repositories/repository_templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='GetTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_commit_statistics(self, request):
        """获取仓库上一次的提交统计信息

        获取仓库上一次的提交统计信息

        :param ListCommitStatisticsRequest request
        :return: ListCommitStatisticsResponse
        """
        return self.list_commit_statistics_with_http_info(request)

    def list_commit_statistics_with_http_info(self, request):
        """获取仓库上一次的提交统计信息

        获取仓库上一次的提交统计信息

        :param ListCommitStatisticsRequest request
        :return: ListCommitStatisticsResponse
        """

        all_params = ['branch_name', 'repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'branch_name' in local_var_params:
            query_params.append(('branch_name', local_var_params['branch_name']))

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
            resource_path='/v1/repositories/{repository_id}/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCommitStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_files(self, request):
        """获取一个仓库下特定分支指定文件内容

        获取一个仓库下特定分支指定文件内容

        :param ListFilesRequest request
        :return: ListFilesResponse
        """
        return self.list_files_with_http_info(request)

    def list_files_with_http_info(self, request):
        """获取一个仓库下特定分支指定文件内容

        获取一个仓库下特定分支指定文件内容

        :param ListFilesRequest request
        :return: ListFilesResponse
        """

        all_params = ['repository_uuid', 'branch_name', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']
        if 'branch_name' in local_var_params:
            path_params['branch_name'] = local_var_params['branch_name']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-none']

        return self.call_api(
            resource_path='/v1/repositories/{repository_uuid}/branch/{branch_name}/file',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_repository_status(self, request):
        """查看仓库的创建状态

        获取仓库状态。

        :param ListRepositoryStatusRequest request
        :return: ListRepositoryStatusResponse
        """
        return self.list_repository_status_with_http_info(request)

    def list_repository_status_with_http_info(self, request):
        """查看仓库的创建状态

        获取仓库状态。

        :param ListRepositoryStatusRequest request
        :return: ListRepositoryStatusResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRepositoryStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_subfiles(self, request):
        """获取分支目录下的文件

        获取分支目录下的文件

        :param ListSubfilesRequest request
        :return: ListSubfilesResponse
        """
        return self.list_subfiles_with_http_info(request)

    def list_subfiles_with_http_info(self, request):
        """获取分支目录下的文件

        获取分支目录下的文件

        :param ListSubfilesRequest request
        :return: ListSubfilesResponse
        """

        all_params = ['repository_uuid', 'branch_name', 'path', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']
        if 'branch_name' in local_var_params:
            path_params['branch_name'] = local_var_params['branch_name']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
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
            resource_path='/v1/repositories/{repository_uuid}/branch/{branch_name}/sub-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubfilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_templates_two(self, request):
        """设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态

        :param ListTemplatesTwoRequest request
        :return: ListTemplatesTwoResponse
        """
        return self.list_templates_two_with_http_info(request)

    def list_templates_two_with_http_info(self, request):
        """设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态

        :param ListTemplatesTwoRequest request
        :return: ListTemplatesTwoResponse
        """

        all_params = ['repository_uuid', 'repository_template_vo2']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v2/repositories/{repository_uuid}/template-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplatesTwoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_two_templates(self, request):
        """获取公开示例模板列表

        获取公开示例模板列表

        :param ListTwoTemplatesRequest request
        :return: ListTwoTemplatesResponse
        """
        return self.list_two_templates_with_http_info(request)

    def list_two_templates_with_http_info(self, request):
        """获取公开示例模板列表

        获取公开示例模板列表

        :param ListTwoTemplatesRequest request
        :return: ListTwoTemplatesResponse
        """

        all_params = ['page_no', 'page_size', 'platform', 'language', 'pipeline', 'enter_type', 'search', 'date_order', 'used_time_order', 'type', 'region']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'pipeline' in local_var_params:
            query_params.append(('pipeline', local_var_params['pipeline']))
        if 'enter_type' in local_var_params:
            query_params.append(('enter_type', local_var_params['enter_type']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'date_order' in local_var_params:
            query_params.append(('date_order', local_var_params['date_order']))
        if 'used_time_order' in local_var_params:
            query_params.append(('used_time_order', local_var_params['used_time_order']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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
            resource_path='/v2/repositories/repository-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTwoTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def share_templates(self, request):
        """设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态

        :param ShareTemplatesRequest request
        :return: ShareTemplatesResponse
        """
        return self.share_templates_with_http_info(request)

    def share_templates_with_http_info(self, request):
        """设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态

        :param ShareTemplatesRequest request
        :return: ShareTemplatesResponse
        """

        all_params = ['repository_uuid', 'repository_template_vo']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/template_status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShareTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_branches_by_repository_id(self, request):
        """查询某仓库对应的分支

        根据仓库id获取指定仓库的分支列表.

        :param ShowBranchesByRepositoryIdRequest request
        :return: ShowBranchesByRepositoryIdResponse
        """
        return self.show_branches_by_repository_id_with_http_info(request)

    def show_branches_by_repository_id_with_http_info(self, request):
        """查询某仓库对应的分支

        根据仓库id获取指定仓库的分支列表.

        :param ShowBranchesByRepositoryIdRequest request
        :return: ShowBranchesByRepositoryIdResponse
        """

        all_params = ['repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v1/repositories/{repository_id}/branches',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBranchesByRepositoryIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_branches_by_two_repository_id(self, request):
        """查询某仓库的标签列表

        查询指定仓库对应的分支。

        :param ShowBranchesByTwoRepositoryIdRequest request
        :return: ShowBranchesByTwoRepositoryIdResponse
        """
        return self.show_branches_by_two_repository_id_with_http_info(request)

    def show_branches_by_two_repository_id_with_http_info(self, request):
        """查询某仓库的标签列表

        查询指定仓库对应的分支。

        :param ShowBranchesByTwoRepositoryIdRequest request
        :return: ShowBranchesByTwoRepositoryIdResponse
        """

        all_params = ['repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v2/repositories/{repository_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBranchesByTwoRepositoryIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_commits_by_branch(self, request):
        """根据组名和仓库名查询某仓库某分支对应的提交

        根据仓库组名、仓库名和分支获取提交列表。

        :param ShowCommitsByBranchRequest request
        :return: ShowCommitsByBranchResponse
        """
        return self.show_commits_by_branch_with_http_info(request)

    def show_commits_by_branch_with_http_info(self, request):
        """根据组名和仓库名查询某仓库某分支对应的提交

        根据仓库组名、仓库名和分支获取提交列表。

        :param ShowCommitsByBranchRequest request
        :return: ShowCommitsByBranchResponse
        """

        all_params = ['group_name', 'ref_name', 'repository_name', 'page_index', 'page_size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_name' in local_var_params:
            path_params['group_name'] = local_var_params['group_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'ref_name' in local_var_params:
            query_params.append(('ref_name', local_var_params['ref_name']))

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
            resource_path='/v1/repositories/{group_name}/{repository_name}/commits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCommitsByBranchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_commits_by_repo_id(self, request):
        """根据仓库id查询仓库某分支对应的提交，提供更多可选参数

        根据仓库id查询仓库某分支对应的提交.

        :param ShowCommitsByRepoIdRequest request
        :return: ShowCommitsByRepoIdResponse
        """
        return self.show_commits_by_repo_id_with_http_info(request)

    def show_commits_by_repo_id_with_http_info(self, request):
        """根据仓库id查询仓库某分支对应的提交，提供更多可选参数

        根据仓库id查询仓库某分支对应的提交.

        :param ShowCommitsByRepoIdRequest request
        :return: ShowCommitsByRepoIdResponse
        """

        all_params = ['ref_name', 'repository_id', 'author', 'begin_date', 'end_date', 'message', 'page_index', 'page_size', 'path', 'stat_format']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'author' in local_var_params:
            query_params.append(('author', local_var_params['author']))
        if 'begin_date' in local_var_params:
            query_params.append(('begin_date', local_var_params['begin_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'message' in local_var_params:
            query_params.append(('message', local_var_params['message']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'ref_name' in local_var_params:
            query_params.append(('ref_name', local_var_params['ref_name']))
        if 'stat_format' in local_var_params:
            query_params.append(('stat_format', local_var_params['stat_format']))

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
            resource_path='/v1/repositories/{repository_id}/commits',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowCommitsByRepoIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_has_pipeline(self, request):
        """修改被流水线引用的仓库状态

        修改被流水线引用的仓库状态

        :param ShowHasPipelineRequest request
        :return: ShowHasPipelineResponse
        """
        return self.show_has_pipeline_with_http_info(request)

    def show_has_pipeline_with_http_info(self, request):
        """修改被流水线引用的仓库状态

        修改被流水线引用的仓库状态

        :param ShowHasPipelineRequest request
        :return: ShowHasPipelineResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/pipeline',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHasPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_image_blob(self, request):
        """获取一个仓库下特定分支的图片文件

        获取一个仓库下特定分支的图片文件

        :param ShowImageBlobRequest request
        :return: ShowImageBlobResponse
        """
        return self.show_image_blob_with_http_info(request)

    def show_image_blob_with_http_info(self, request):
        """获取一个仓库下特定分支的图片文件

        获取一个仓库下特定分支的图片文件

        :param ShowImageBlobRequest request
        :return: ShowImageBlobResponse
        """

        all_params = ['repository_uuid', 'branch_name', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']
        if 'branch_name' in local_var_params:
            path_params['branch_name'] = local_var_params['branch_name']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-none']

        return self.call_api(
            resource_path='/v1/repositories/{repository_uuid}/branch/{branch_name}/image',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageBlobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_master(self, request):
        """判断用户是否有仓库的管理员权限

        判断用户是否有仓库的管理员权限

        :param ShowMasterRequest request
        :return: ShowMasterResponse
        """
        return self.show_master_with_http_info(request)

    def show_master_with_http_info(self, request):
        """判断用户是否有仓库的管理员权限

        判断用户是否有仓库的管理员权限

        :param ShowMasterRequest request
        :return: ShowMasterResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/master',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMasterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_repo_id(self, request):
        """根据仓库名组名获取仓库短id，用以拼接与commitid对应提交详情页面url

        获取仓库短id,用于获取仓库详情页面url

        :param ShowRepoIdRequest request
        :return: ShowRepoIdResponse
        """
        return self.show_repo_id_with_http_info(request)

    def show_repo_id_with_http_info(self, request):
        """根据仓库名组名获取仓库短id，用以拼接与commitid对应提交详情页面url

        获取仓库短id,用于获取仓库详情页面url

        :param ShowRepoIdRequest request
        :return: ShowRepoIdResponse
        """

        all_params = ['group_name', 'repository_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
        if 'repository_name' in local_var_params:
            query_params.append(('repository_name', local_var_params['repository_name']))

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
            resource_path='/v1/repositories/repoid',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRepoIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_repository_archive(self, request):
        """下载仓库

        按照指定格式下载仓库

        :param ShowRepositoryArchiveRequest request
        :return: ShowRepositoryArchiveResponse
        """
        return self.show_repository_archive_with_http_info(request)

    def show_repository_archive_with_http_info(self, request):
        """下载仓库

        按照指定格式下载仓库

        :param ShowRepositoryArchiveRequest request
        :return: ShowRepositoryArchiveResponse
        """

        all_params = ['repository_uuid', 'sha', 'format']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))
        if 'format' in local_var_params:
            query_params.append(('format', local_var_params['format']))

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
            resource_path='/v2/repositories/{repository_uuid}/archive',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRepositoryArchiveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_repository_by_uuid(self, request):
        """查询某个仓库的详细信息

        根据仓库UUID获取仓库信息仓库信息。返回 包含id，name，组名，仓库访问URL。

        :param ShowRepositoryByUuidRequest request
        :return: ShowRepositoryByUuidResponse
        """
        return self.show_repository_by_uuid_with_http_info(request)

    def show_repository_by_uuid_with_http_info(self, request):
        """查询某个仓库的详细信息

        根据仓库UUID获取仓库信息仓库信息。返回 包含id，name，组名，仓库访问URL。

        :param ShowRepositoryByUuidRequest request
        :return: ShowRepositoryByUuidResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v2/repositories/{repository_uuid}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRepositoryByUuidResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_repository_statistics(self, request):
        """仓库统计

        根据仓库短id，查询仓库的代码提交记录统计

        :param ShowRepositoryStatisticsRequest request
        :return: ShowRepositoryStatisticsResponse
        """
        return self.show_repository_statistics_with_http_info(request)

    def show_repository_statistics_with_http_info(self, request):
        """仓库统计

        根据仓库短id，查询仓库的代码提交记录统计

        :param ShowRepositoryStatisticsRequest request
        :return: ShowRepositoryStatisticsResponse
        """

        all_params = ['repository_id', 'show_repository_statistics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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
            resource_path='/v1/repositories/{repository_id}/statistics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRepositoryStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_statistic_commit(self, request):
        """获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数

        :param ShowStatisticCommitRequest request
        :return: ShowStatisticCommitResponse
        """
        return self.show_statistic_commit_with_http_info(request)

    def show_statistic_commit_with_http_info(self, request):
        """获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数

        :param ShowStatisticCommitRequest request
        :return: ShowStatisticCommitResponse
        """

        all_params = ['repository_id', 'ref_name', 'begin_date', 'end_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'ref_name' in local_var_params:
            query_params.append(('ref_name', local_var_params['ref_name']))
        if 'begin_date' in local_var_params:
            query_params.append(('begin_date', local_var_params['begin_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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
            resource_path='/v2/repositories/{repository_id}/commit_lines',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowStatisticCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_statistic_commit_v3(self, request):
        """获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数

        :param ShowStatisticCommitV3Request request
        :return: ShowStatisticCommitV3Response
        """
        return self.show_statistic_commit_v3_with_http_info(request)

    def show_statistic_commit_v3_with_http_info(self, request):
        """获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数

        :param ShowStatisticCommitV3Request request
        :return: ShowStatisticCommitV3Response
        """

        all_params = ['repository_id', 'ref_name', 'begin_date', 'end_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'ref_name' in local_var_params:
            query_params.append(('ref_name', local_var_params['ref_name']))
        if 'begin_date' in local_var_params:
            query_params.append(('begin_date', local_var_params['begin_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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
            resource_path='/v3/repositories/{repository_id}/commit-lines',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowStatisticCommitV3Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_statistical_data(self, request):
        """获取仓库统计数据

        获取仓库统计数据

        :param ShowStatisticalDataRequest request
        :return: ShowStatisticalDataResponse
        """
        return self.show_statistical_data_with_http_info(request)

    def show_statistical_data_with_http_info(self, request):
        """获取仓库统计数据

        获取仓库统计数据

        :param ShowStatisticalDataRequest request
        :return: ShowStatisticalDataResponse
        """

        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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
            resource_path='/v1/repositories/{repository_uuid}/statistic-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowStatisticalDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_ssh_key(self, request):
        """添加ssh key

        添加ssh key

        :param AddSshKeyRequest request
        :return: AddSshKeyResponse
        """
        return self.add_ssh_key_with_http_info(request)

    def add_ssh_key_with_http_info(self, request):
        """添加ssh key

        添加ssh key

        :param AddSshKeyRequest request
        :return: AddSshKeyResponse
        """

        all_params = ['public_key']
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
            resource_path='/v1/users/sshkey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddSshKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_s_shkey(self, request):
        """删除用户公钥

        调用gitlab原生接口删除用户公钥。

        :param DeleteSShkeyRequest request
        :return: DeleteSShkeyResponse
        """
        return self.delete_s_shkey_with_http_info(request)

    def delete_s_shkey_with_http_info(self, request):
        """删除用户公钥

        调用gitlab原生接口删除用户公钥。

        :param DeleteSShkeyRequest request
        :return: DeleteSShkeyResponse
        """

        all_params = ['id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/users/sshkey/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSShkeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ssh_keys(self, request):
        """获取ssh key列表

        获取ssh key列表。

        :param ListSshKeysRequest request
        :return: ListSshKeysResponse
        """
        return self.list_ssh_keys_with_http_info(request)

    def list_ssh_keys_with_http_info(self, request):
        """获取ssh key列表

        获取ssh key列表。

        :param ListSshKeysRequest request
        :return: ListSshKeysResponse
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
            resource_path='/v1/users/sshkey',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSshKeysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_private_key_verify(self, request):
        """检验私钥是否有拉取代码的权限

        检验私钥是否有拉取代码的权限

        :param ShowPrivateKeyVerifyRequest request
        :return: ShowPrivateKeyVerifyResponse
        """
        return self.show_private_key_verify_with_http_info(request)

    def show_private_key_verify_with_http_info(self, request):
        """检验私钥是否有拉取代码的权限

        检验私钥是否有拉取代码的权限

        :param ShowPrivateKeyVerifyRequest request
        :return: ShowPrivateKeyVerifyResponse
        """

        all_params = ['private_key']
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
            resource_path='/v1/users/sshkey/privatekey/verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPrivateKeyVerifyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def validate_https_info(self, request):
        """ https账号密码校验

        调用 gitlab 接口判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。

        :param ValidateHttpsInfoRequest request
        :return: ValidateHttpsInfoResponse
        """
        return self.validate_https_info_with_http_info(request)

    def validate_https_info_with_http_info(self, request):
        """ https账号密码校验

        调用 gitlab 接口判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。

        :param ValidateHttpsInfoRequest request
        :return: ValidateHttpsInfoResponse
        """

        all_params = ['iam_user_uuid', 'password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'iam_user_uuid' in local_var_params:
            path_params['iam_user_uuid'] = local_var_params['iam_user_uuid']

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
            resource_path='/v1/user/{iam_user_uuid}/validateHttpsInfo',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ValidateHttpsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def validate_https_info_v2(self, request):
        """ https账号密码校验

        调用 gitlab 接口判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。

        :param ValidateHttpsInfoV2Request request
        :return: ValidateHttpsInfoV2Response
        """
        return self.validate_https_info_v2_with_http_info(request)

    def validate_https_info_v2_with_http_info(self, request):
        """ https账号密码校验

        调用 gitlab 接口判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。

        :param ValidateHttpsInfoV2Request request
        :return: ValidateHttpsInfoV2Response
        """

        all_params = ['iam_user_uuid', 'password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'iam_user_uuid' in local_var_params:
            path_params['iam_user_uuid'] = local_var_params['iam_user_uuid']

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
            resource_path='/v2/user/{iam_user_uuid}/validate-https-info',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ValidateHttpsInfoV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_project_and_repositories(self, request):
        """创建项目、仓库

        创建项目后，创建仓库组由后台生成方式 传入参数：仓库名、模板id、是否导入项目成员、归属项目

        :param CreateProjectAndRepositoriesRequest request
        :return: CreateProjectAndRepositoriesResponse
        """
        return self.create_project_and_repositories_with_http_info(request)

    def create_project_and_repositories_with_http_info(self, request):
        """创建项目、仓库

        创建项目后，创建仓库组由后台生成方式 传入参数：仓库名、模板id、是否导入项目成员、归属项目

        :param CreateProjectAndRepositoriesRequest request
        :return: CreateProjectAndRepositoriesResponse
        """

        all_params = ['create_info']
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
            resource_path='/v2/projects/repositories',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateProjectAndRepositoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_project_andfork_repositories(self, request):
        """创建项目并fork仓库

        创建仓库后fork仓库 传入参数：仓库名、是否导入项目成员、归属项目

        :param CreateProjectAndforkRepositoriesRequest request
        :return: CreateProjectAndforkRepositoriesResponse
        """
        return self.create_project_andfork_repositories_with_http_info(request)

    def create_project_andfork_repositories_with_http_info(self, request):
        """创建项目并fork仓库

        创建仓库后fork仓库 传入参数：仓库名、是否导入项目成员、归属项目

        :param CreateProjectAndforkRepositoriesRequest request
        :return: CreateProjectAndforkRepositoriesResponse
        """

        all_params = ['create_info']
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
            resource_path='/v2/projects/repositories/fork',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateProjectAndforkRepositoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_user_all_repositories(self, request):
        """查询用户的所有仓库

        获取用户的所有仓库信息

        :param ListUserAllRepositoriesRequest request
        :return: ListUserAllRepositoriesResponse
        """
        return self.list_user_all_repositories_with_http_info(request)

    def list_user_all_repositories_with_http_info(self, request):
        """查询用户的所有仓库

        获取用户的所有仓库信息

        :param ListUserAllRepositoriesRequest request
        :return: ListUserAllRepositoriesResponse
        """

        all_params = ['page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

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
            resource_path='/v2/projects/repositories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUserAllRepositoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_all_repository_by_two_project_id(self, request):
        """查询项目下的所有仓库

        获取仓库列表,模糊查询支持范围,如果未传入project uuid，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配

        :param ShowAllRepositoryByTwoProjectIdRequest request
        :return: ShowAllRepositoryByTwoProjectIdResponse
        """
        return self.show_all_repository_by_two_project_id_with_http_info(request)

    def show_all_repository_by_two_project_id_with_http_info(self, request):
        """查询项目下的所有仓库

        获取仓库列表,模糊查询支持范围,如果未传入project uuid，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配

        :param ShowAllRepositoryByTwoProjectIdRequest request
        :return: ShowAllRepositoryByTwoProjectIdResponse
        """

        all_params = ['project_uuid', 'page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']

        query_params = []
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))

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
            resource_path='/v2/projects/{project_uuid}/repositories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAllRepositoryByTwoProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_hooks(self, request):
        """为指定仓库添加hook

        提交代码自动触发编译构建，添加仓库钩子

        :param AddHooksRequest request
        :return: AddHooksResponse
        """
        return self.add_hooks_with_http_info(request)

    def add_hooks_with_http_info(self, request):
        """为指定仓库添加hook

        提交代码自动触发编译构建，添加仓库钩子

        :param AddHooksRequest request
        :return: AddHooksResponse
        """

        all_params = ['group_name', 'repository_name', 'repository_hook_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_name' in local_var_params:
            path_params['group_name'] = local_var_params['group_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

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
            resource_path='/v1/repositories/{group_name}/{repository_name}/hooks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_hooks(self, request):
        """删除指定仓库的 hook

        提交代码自动触发编译构建，删除仓库钩子

        :param DeleteHooksRequest request
        :return: DeleteHooksResponse
        """
        return self.delete_hooks_with_http_info(request)

    def delete_hooks_with_http_info(self, request):
        """删除指定仓库的 hook

        提交代码自动触发编译构建，删除仓库钩子

        :param DeleteHooksRequest request
        :return: DeleteHooksResponse
        """

        all_params = ['group_name', 'hook_id', 'repository_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_name' in local_var_params:
            path_params['group_name'] = local_var_params['group_name']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

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
            resource_path='/v1/repositories/{group_name}/{repository_name}/hooks/{hook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_hooks(self, request):
        """查询指定仓库的webhook

        获取仓库webhook

        :param ListHooksRequest request
        :return: ListHooksResponse
        """
        return self.list_hooks_with_http_info(request)

    def list_hooks_with_http_info(self, request):
        """查询指定仓库的webhook

        获取仓库webhook

        :param ListHooksRequest request
        :return: ListHooksResponse
        """

        all_params = ['group_name', 'repository_name', 'hook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_name' in local_var_params:
            path_params['group_name'] = local_var_params['group_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

        query_params = []
        if 'hook_id' in local_var_params:
            query_params.append(('hook_id', local_var_params['hook_id']))

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
            resource_path='/v1/repositories/{group_name}/{repository_name}/hooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHooksResponse',
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

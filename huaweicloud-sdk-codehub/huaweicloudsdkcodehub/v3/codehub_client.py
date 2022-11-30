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
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateCommitResponse`
        """
        return self.create_commit_with_http_info(request)

    def create_commit_with_http_info(self, request):
        all_params = ['repo_id', 'create_commit_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='CreateCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_commits(self, request):
        """查询某个仓库的提交信息

        根据仓库短ID获取提交信息，支持根据文件路径，查询这个路径下所有的commits列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCommits
        :type request: :class:`huaweicloudsdkcodehub.v3.ListCommitsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListCommitsResponse`
        """
        return self.list_commits_with_http_info(request)

    def list_commits_with_http_info(self, request):
        all_params = ['repo_id', 'ref_name', 'since', 'until', 'path', 'all', 'with_stats']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListCommitsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_diff_commit(self, request):
        """查询某个仓库的提交差异信息

        根据commit id查询提交差异信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiffCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowDiffCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowDiffCommitResponse`
        """
        return self.show_diff_commit_with_http_info(request)

    def show_diff_commit_with_http_info(self, request):
        all_params = ['repo_id', 'sha']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowDiffCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_single_commit(self, request):
        """查询某个仓库的特定提交信息

        获取由commit id或分支或标记的名称标识的特定提交。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowSingleCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowSingleCommitResponse`
        """
        return self.show_single_commit_with_http_info(request)

    def show_single_commit_with_http_info(self, request):
        all_params = ['repo_id', 'sha', 'stats']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowSingleCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_files_by_query(self, request):
        """查询某个仓库的文件信息

        获取仓库中文件的信息，如名称、大小、内容。请注意，文件内容是Base64编码的。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFilesByQuery
        :type request: :class:`huaweicloudsdkcodehub.v3.ListFilesByQueryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListFilesByQueryResponse`
        """
        return self.list_files_by_query_with_http_info(request)

    def list_files_by_query_with_http_info(self, request):
        all_params = ['repo_id', 'file_path', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
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
            resource_path='/v2/projects/{repo_id}/repository/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFilesByQueryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_file(self, request):
        """查询某个仓库的文件信息

        获取仓库中文件的信息，如名称、大小、内容。请注意，文件内容是Base64编码的。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFile
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowFileResponse`
        """
        return self.show_file_with_http_info(request)

    def show_file_with_http_info(self, request):
        all_params = ['repo_id', 'file_path', 'ref']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_all_repository_by_project_id(self, request):
        """获取项目下所有仓库信息

        获取仓库列表 模糊查询支持范围,如果未传入project_id，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetAllRepositoryByProjectId
        :type request: :class:`huaweicloudsdkcodehub.v3.GetAllRepositoryByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetAllRepositoryByProjectIdResponse`
        """
        return self.get_all_repository_by_project_id_with_http_info(request)

    def get_all_repository_by_project_id_with_http_info(self, request):
        all_params = ['project_uuid', 'page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='GetAllRepositoryByProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_product_templates(self, request):
        """获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetProductTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.GetProductTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetProductTemplatesResponse`
        """
        return self.get_product_templates_with_http_info(request)

    def get_product_templates_with_http_info(self, request):
        all_params = ['project_uuid', 'page_no', 'page_size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='GetProductTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_product_two_templates(self, request):
        """获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProductTwoTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.ListProductTwoTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListProductTwoTemplatesResponse`
        """
        return self.list_product_two_templates_with_http_info(request)

    def list_product_two_templates_with_http_info(self, request):
        all_params = ['project_uuid', 'page_no', 'page_size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListProductTwoTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_repository_name_exist(self, request):
        """校验指定项目下的仓库名

        一般创建仓库时调用。通过传入项目uuid,仓库名，来判断仓库是否重名。仓库存在result:false,仓库不存在result:true。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryNameExist
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryNameExistRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryNameExistResponse`
        """
        return self.show_repository_name_exist_with_http_info(request)

    def show_repository_name_exist_with_http_info(self, request):
        all_params = ['project_uuid', 'repository_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowRepositoryNameExistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_repo_members(self, request):
        """添加仓库成员

        调用方codehubportal,添加仓库成员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRepoMembers
        :type request: :class:`huaweicloudsdkcodehub.v3.AddRepoMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddRepoMembersResponse`
        """
        return self.add_repo_members_with_http_info(request)

    def add_repo_members_with_http_info(self, request):
        all_params = ['repository_uuid', 'create_repo_member_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddRepoMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_repo_member(self, request):
        """删除仓库成员

        删除仓库成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepoMember
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteRepoMemberRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteRepoMemberResponse`
        """
        return self.delete_repo_member_with_http_info(request)

    def delete_repo_member_with_http_info(self, request):
        all_params = ['member_id', 'repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteRepoMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_repo_members(self, request):
        """获取仓库所有成员记录

        获取仓库成员列表,可通过关键字搜索某成员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepoMembers
        :type request: :class:`huaweicloudsdkcodehub.v3.ListRepoMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListRepoMembersResponse`
        """
        return self.list_repo_members_with_http_info(request)

    def list_repo_members_with_http_info(self, request):
        all_params = ['repository_uuid', 'page_index', 'page_size', 'subject']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListRepoMembersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_repo_role(self, request):
        """设置成员在仓库中的角色

        给仓库中成员设置仓库的操作权限，
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRepoRole
        :type request: :class:`huaweicloudsdkcodehub.v3.SetRepoRoleRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.SetRepoRoleResponse`
        """
        return self.set_repo_role_with_http_info(request)

    def set_repo_role_with_http_info(self, request):
        all_params = ['member_id', 'repository_uuid', 'set_repo_role_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='SetRepoRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_deploy_key(self, request):
        """添加部署密钥

        添加部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyResponse`
        """
        return self.add_deploy_key_with_http_info(request)

    def add_deploy_key_with_http_info(self, request):
        all_params = ['repository_id', 'add_deploy_key_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddDeployKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_deploy_key_v2(self, request):
        """添加部署密钥

        添加部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeployKeyV2
        :type request: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyV2Response`
        """
        return self.add_deploy_key_v2_with_http_info(request)

    def add_deploy_key_v2_with_http_info(self, request):
        all_params = ['repository_id', 'add_deploy_key_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddDeployKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_protect_branch_v2(self, request):
        """新建保护分支

        新建保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddProtectBranchV2
        :type request: :class:`huaweicloudsdkcodehub.v3.AddProtectBranchV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddProtectBranchV2Response`
        """
        return self.add_protect_branch_v2_with_http_info(request)

    def add_protect_branch_v2_with_http_info(self, request):
        all_params = ['repository_id', 'branch_name', 'add_protect_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'branch_name' in local_var_params:
            path_params['branch_name'] = local_var_params['branch_name']

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
            resource_path='/v2/repositories/{repository_id}/branch/{branch_name}/protect',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddProtectBranchV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_tag_v2(self, request):
        """新建标签

        新建标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTagV2
        :type request: :class:`huaweicloudsdkcodehub.v3.AddTagV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddTagV2Response`
        """
        return self.add_tag_v2_with_http_info(request)

    def add_tag_v2_with_http_info(self, request):
        all_params = ['repository_id', 'add_tags_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v2/repositories/{repository_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddTagV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_repository(self, request):
        """创建仓库

        用指定的名称在指定项目上创建仓库。传入参数：仓库名、模板id、是否导入项目成员、归属项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRepository
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateRepositoryResponse`
        """
        return self.create_repository_with_http_info(request)

    def create_repository_with_http_info(self, request):
        all_params = ['create_repo_request']
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
            resource_path='/v1/repositories',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deploy_key(self, request):
        """删除仓库部署密钥

        删除仓库部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyResponse`
        """
        return self.delete_deploy_key_with_http_info(request)

    def delete_deploy_key_with_http_info(self, request):
        all_params = ['key_id', 'repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteDeployKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deploy_key_v2(self, request):
        """删除仓库部署密钥

        删除仓库部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployKeyV2
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyV2Response`
        """
        return self.delete_deploy_key_v2_with_http_info(request)

    def delete_deploy_key_v2_with_http_info(self, request):
        all_params = ['key_id', 'repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteDeployKeyV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_repository(self, request):
        """删除仓库

        根据仓库32位uuid删除指定的仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepository
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteRepositoryResponse`
        """
        return self.delete_repository_with_http_info(request)

    def delete_repository_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_repository_by_project_id(self, request):
        """查询项目下的某个仓库

        不建议再使用,建议使用/{repository_uuid}/status
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetRepositoryByProjectId
        :type request: :class:`huaweicloudsdkcodehub.v3.GetRepositoryByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetRepositoryByProjectIdResponse`
        """
        return self.get_repository_by_project_id_with_http_info(request)

    def get_repository_by_project_id_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='GetRepositoryByProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def get_templates(self, request):
        """获取公开示例模板列表

        获取公开示例模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.GetTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetTemplatesResponse`
        """
        return self.get_templates_with_http_info(request)

    def get_templates_with_http_info(self, request):
        all_params = ['page_no', 'page_size', 'platform', 'language', 'pipeline', 'entertype', 'search', 'dateorder', 'usedtimeorder', 'type', 'region']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='GetTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_branches_by_repository_id(self, request):
        """获取仓库分支列表

        获取仓库分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBranchesByRepositoryId
        :type request: :class:`huaweicloudsdkcodehub.v3.ListBranchesByRepositoryIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListBranchesByRepositoryIdResponse`
        """
        return self.list_branches_by_repository_id_with_http_info(request)

    def list_branches_by_repository_id_with_http_info(self, request):
        all_params = ['repository_id', 'page', 'per_page', 'match']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'match' in local_var_params:
            query_params.append(('match', local_var_params['match']))

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
            resource_path='/v2/repositories/{repository_id}/branches',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBranchesByRepositoryIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_commit_statistics(self, request):
        """获取仓库上一次的提交统计信息

        获取仓库上一次的提交统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCommitStatistics
        :type request: :class:`huaweicloudsdkcodehub.v3.ListCommitStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListCommitStatisticsResponse`
        """
        return self.list_commit_statistics_with_http_info(request)

    def list_commit_statistics_with_http_info(self, request):
        all_params = ['branch_name', 'repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListCommitStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_files(self, request):
        """获取一个仓库下特定分支指定文件内容

        获取一个仓库下特定分支指定文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFiles
        :type request: :class:`huaweicloudsdkcodehub.v3.ListFilesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListFilesResponse`
        """
        return self.list_files_with_http_info(request)

    def list_files_with_http_info(self, request):
        all_params = ['repository_uuid', 'branch_name', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_merge_request(self, request):
        """获取仓库合并请求列表

        获取仓库合并请求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v3.ListMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListMergeRequestResponse`
        """
        return self.list_merge_request_with_http_info(request)

    def list_merge_request_with_http_info(self, request):
        all_params = ['repository_id', 'state', 'page', 'per_page', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
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
            resource_path='/v2/repositories/{repository_id}/merge_request',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMergeRequestResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_repository_status(self, request):
        """查看仓库的创建状态

        获取仓库状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepositoryStatus
        :type request: :class:`huaweicloudsdkcodehub.v3.ListRepositoryStatusRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListRepositoryStatusResponse`
        """
        return self.list_repository_status_with_http_info(request)

    def list_repository_status_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListRepositoryStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_subfiles(self, request):
        """获取分支目录下的文件

        获取分支目录下的文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubfiles
        :type request: :class:`huaweicloudsdkcodehub.v3.ListSubfilesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListSubfilesResponse`
        """
        return self.list_subfiles_with_http_info(request)

    def list_subfiles_with_http_info(self, request):
        all_params = ['repository_uuid', 'branch_name', 'path', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListSubfilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_templates_two(self, request):
        """设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplatesTwo
        :type request: :class:`huaweicloudsdkcodehub.v3.ListTemplatesTwoRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListTemplatesTwoResponse`
        """
        return self.list_templates_two_with_http_info(request)

    def list_templates_two_with_http_info(self, request):
        all_params = ['repository_uuid', 'repository_template_vo2']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListTemplatesTwoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_two_templates(self, request):
        """获取公开示例模板列表

        获取公开示例模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTwoTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.ListTwoTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListTwoTemplatesResponse`
        """
        return self.list_two_templates_with_http_info(request)

    def list_two_templates_with_http_info(self, request):
        all_params = ['page_no', 'page_size', 'platform', 'language', 'pipeline', 'enter_type', 'search', 'date_order', 'used_time_order', 'type', 'region']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListTwoTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def share_templates(self, request):
        """设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShareTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.ShareTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShareTemplatesResponse`
        """
        return self.share_templates_with_http_info(request)

    def share_templates_with_http_info(self, request):
        all_params = ['repository_uuid', 'repository_template_vo']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShareTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_branches_by_repository_id(self, request):
        """查询某仓库对应的分支

        根据仓库id获取指定仓库的分支列表.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBranchesByRepositoryId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByRepositoryIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByRepositoryIdResponse`
        """
        return self.show_branches_by_repository_id_with_http_info(request)

    def show_branches_by_repository_id_with_http_info(self, request):
        all_params = ['repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowBranchesByRepositoryIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_branches_by_two_repository_id(self, request):
        """查询某仓库的标签列表

        查询指定仓库对应的分支。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBranchesByTwoRepositoryId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByTwoRepositoryIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByTwoRepositoryIdResponse`
        """
        return self.show_branches_by_two_repository_id_with_http_info(request)

    def show_branches_by_two_repository_id_with_http_info(self, request):
        all_params = ['repository_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowBranchesByTwoRepositoryIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_commits_by_branch(self, request):
        """根据组名和仓库名查询某仓库某分支对应的提交

        根据仓库组名、仓库名和分支获取提交列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCommitsByBranch
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByBranchResponse`
        """
        return self.show_commits_by_branch_with_http_info(request)

    def show_commits_by_branch_with_http_info(self, request):
        all_params = ['group_name', 'ref_name', 'repository_name', 'page_index', 'page_size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowCommitsByBranchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_commits_by_repo_id(self, request):
        """根据仓库id查询仓库某分支对应的提交，提供更多可选参数

        根据仓库id查询仓库某分支对应的提交.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCommitsByRepoId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByRepoIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByRepoIdResponse`
        """
        return self.show_commits_by_repo_id_with_http_info(request)

    def show_commits_by_repo_id_with_http_info(self, request):
        all_params = ['ref_name', 'repository_id', 'author', 'begin_date', 'end_date', 'message', 'page_index', 'page_size', 'path', 'stat_format']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowCommitsByRepoIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_has_pipeline(self, request):
        """修改被流水线引用的仓库状态

        修改被流水线引用的仓库状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHasPipeline
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowHasPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowHasPipelineResponse`
        """
        return self.show_has_pipeline_with_http_info(request)

    def show_has_pipeline_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowHasPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_blob(self, request):
        """获取一个仓库下特定分支的图片文件

        获取一个仓库下特定分支的图片文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageBlob
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowImageBlobRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowImageBlobResponse`
        """
        return self.show_image_blob_with_http_info(request)

    def show_image_blob_with_http_info(self, request):
        all_params = ['repository_uuid', 'branch_name', 'path']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowImageBlobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_master(self, request):
        """判断用户是否有仓库的管理员权限

        判断用户是否有仓库的管理员权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMaster
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowMasterRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowMasterResponse`
        """
        return self.show_master_with_http_info(request)

    def show_master_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowMasterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_merge_request(self, request):
        """获取仓库合并请求详情

        获取仓库合并请求详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowMergeRequestResponse`
        """
        return self.show_merge_request_with_http_info(request)

    def show_merge_request_with_http_info(self, request):
        all_params = ['repository_id', 'merge_request_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_id' in local_var_params:
            path_params['merge_request_id'] = local_var_params['merge_request_id']

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
            resource_path='/v2/repositories/{repository_id}/merge_request/{merge_request_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMergeRequestResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_repo_id(self, request):
        """根据仓库名组名获取仓库短id，用以拼接与commitid对应提交详情页面url

        获取仓库短id,用于获取仓库详情页面url
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepoId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepoIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepoIdResponse`
        """
        return self.show_repo_id_with_http_info(request)

    def show_repo_id_with_http_info(self, request):
        all_params = ['group_name', 'repository_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowRepoIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_repository_archive(self, request):
        """下载仓库

        按照指定格式下载仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryArchive
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryArchiveRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryArchiveResponse`
        """
        return self.show_repository_archive_with_http_info(request)

    def show_repository_archive_with_http_info(self, request):
        all_params = ['repository_uuid', 'sha', 'format']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowRepositoryArchiveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_repository_by_uuid(self, request):
        """查询某个仓库的详细信息

        根据仓库UUID(由CreateRepository接口返回)获取仓库信息仓库信息。返回 包含id，name，组名，仓库访问URL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryByUuid
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryByUuidRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryByUuidResponse`
        """
        return self.show_repository_by_uuid_with_http_info(request)

    def show_repository_by_uuid_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowRepositoryByUuidResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_repository_statistics(self, request):
        """仓库统计

        根据仓库短id，查询仓库的代码提交记录统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryStatistics
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryStatisticsResponse`
        """
        return self.show_repository_statistics_with_http_info(request)

    def show_repository_statistics_with_http_info(self, request):
        all_params = ['repository_id', 'show_repository_statistics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowRepositoryStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_statistic_commit(self, request):
        """获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStatisticCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitResponse`
        """
        return self.show_statistic_commit_with_http_info(request)

    def show_statistic_commit_with_http_info(self, request):
        all_params = ['repository_id', 'ref_name', 'begin_date', 'end_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowStatisticCommitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_statistic_commit_v3(self, request):
        """获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStatisticCommitV3
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitV3Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitV3Response`
        """
        return self.show_statistic_commit_v3_with_http_info(request)

    def show_statistic_commit_v3_with_http_info(self, request):
        all_params = ['repository_id', 'ref_name', 'begin_date', 'end_date']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowStatisticCommitV3Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_statistical_data(self, request):
        """获取仓库统计数据

        获取仓库统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStatisticalData
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowStatisticalDataRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowStatisticalDataResponse`
        """
        return self.show_statistical_data_with_http_info(request)

    def show_statistical_data_with_http_info(self, request):
        all_params = ['repository_uuid']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowStatisticalDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_ssh_key(self, request):
        """添加ssh key

        添加ssh key
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddSshKey
        :type request: :class:`huaweicloudsdkcodehub.v3.AddSshKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddSshKeyResponse`
        """
        return self.add_ssh_key_with_http_info(request)

    def add_ssh_key_with_http_info(self, request):
        all_params = ['public_key']
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
            resource_path='/v1/users/sshkey',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddSshKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_s_shkey(self, request):
        """删除用户公钥

        调用gitlab原生接口删除用户公钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSShkey
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteSShkeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteSShkeyResponse`
        """
        return self.delete_s_shkey_with_http_info(request)

    def delete_s_shkey_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/users/sshkey/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSShkeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ssh_keys(self, request):
        """获取ssh key列表

        获取ssh key列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSshKeys
        :type request: :class:`huaweicloudsdkcodehub.v3.ListSshKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListSshKeysResponse`
        """
        return self.list_ssh_keys_with_http_info(request)

    def list_ssh_keys_with_http_info(self, request):
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
            resource_path='/v1/users/sshkey',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSshKeysResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_private_key_verify(self, request):
        """检验私钥是否有拉取代码的权限

        检验私钥是否有拉取代码的权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateKeyVerify
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowPrivateKeyVerifyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowPrivateKeyVerifyResponse`
        """
        return self.show_private_key_verify_with_http_info(request)

    def show_private_key_verify_with_http_info(self, request):
        all_params = ['private_key']
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
            resource_path='/v1/users/sshkey/privatekey/verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPrivateKeyVerifyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def validate_https_info(self, request):
        """ https账号密码校验

        调用 gitlab 接口判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateHttpsInfo
        :type request: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoResponse`
        """
        return self.validate_https_info_with_http_info(request)

    def validate_https_info_with_http_info(self, request):
        all_params = ['iam_user_uuid', 'password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ValidateHttpsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def validate_https_info_v2(self, request):
        """ https账号密码校验

        调用 gitlab 接口判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateHttpsInfoV2
        :type request: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoV2Response`
        """
        return self.validate_https_info_v2_with_http_info(request)

    def validate_https_info_v2_with_http_info(self, request):
        all_params = ['iam_user_uuid', 'password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ValidateHttpsInfoV2Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def associate_issues(self, request):
        """分支关联工作项

        分支关联工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateIssues
        :type request: :class:`huaweicloudsdkcodehub.v3.AssociateIssuesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AssociateIssuesResponse`
        """
        return self.associate_issues_with_http_info(request)

    def associate_issues_with_http_info(self, request):
        all_params = ['associate_issues_request_body']
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
            resource_path='/v2/projects/issues',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AssociateIssuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project_and_repositories(self, request):
        """创建项目、仓库

        创建项目后，创建仓库组由后台生成方式 传入参数：仓库名、模板id、是否导入项目成员、归属项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectAndRepositories
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndRepositoriesResponse`
        """
        return self.create_project_and_repositories_with_http_info(request)

    def create_project_and_repositories_with_http_info(self, request):
        all_params = ['create_info']
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
            resource_path='/v2/projects/repositories',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectAndRepositoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project_andfork_repositories(self, request):
        """创建项目并fork仓库

        创建仓库后fork仓库 传入参数：仓库名、是否导入项目成员、归属项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectAndforkRepositories
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndforkRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndforkRepositoriesResponse`
        """
        return self.create_project_andfork_repositories_with_http_info(request)

    def create_project_andfork_repositories_with_http_info(self, request):
        all_params = ['create_info']
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
            resource_path='/v2/projects/repositories/fork',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectAndforkRepositoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user_all_repositories(self, request):
        """查询用户的所有仓库

        获取用户的所有仓库信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserAllRepositories
        :type request: :class:`huaweicloudsdkcodehub.v3.ListUserAllRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListUserAllRepositoriesResponse`
        """
        return self.list_user_all_repositories_with_http_info(request)

    def list_user_all_repositories_with_http_info(self, request):
        all_params = ['page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListUserAllRepositoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_all_repository_by_two_project_id(self, request):
        """查询项目下的所有仓库

        获取仓库列表,模糊查询支持范围,如果未传入project uuid，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllRepositoryByTwoProjectId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowAllRepositoryByTwoProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowAllRepositoryByTwoProjectIdResponse`
        """
        return self.show_all_repository_by_two_project_id_with_http_info(request)

    def show_all_repository_by_two_project_id_with_http_info(self, request):
        all_params = ['project_uuid', 'page_index', 'page_size', 'search']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowAllRepositoryByTwoProjectIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_hooks(self, request):
        """为指定仓库添加hook

        提交代码自动触发编译构建，添加仓库钩子
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddHooks
        :type request: :class:`huaweicloudsdkcodehub.v3.AddHooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddHooksResponse`
        """
        return self.add_hooks_with_http_info(request)

    def add_hooks_with_http_info(self, request):
        all_params = ['group_name', 'repository_name', 'repository_hook_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_hooks(self, request):
        """删除指定仓库的 hook

        提交代码自动触发编译构建，删除仓库钩子
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHooks
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteHooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteHooksResponse`
        """
        return self.delete_hooks_with_http_info(request)

    def delete_hooks_with_http_info(self, request):
        all_params = ['group_name', 'hook_id', 'repository_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_hooks(self, request):
        """查询指定仓库的webhook

        获取仓库webhook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHooks
        :type request: :class:`huaweicloudsdkcodehub.v3.ListHooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListHooksResponse`
        """
        return self.list_hooks_with_http_info(request)

    def list_hooks_with_http_info(self, request):
        all_params = ['group_name', 'repository_name', 'hook_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ListHooksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_new_branch(self, request):
        """创建分支

        根据仓库id在指定仓库中创建分支
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNewBranch
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateNewBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateNewBranchResponse`
        """
        return self.create_new_branch_with_http_info(request)

    def create_new_branch_with_http_info(self, request):
        all_params = ['repository_id', 'branch_info']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/repositories/{repository_id}/branches',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNewBranchResponse',
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

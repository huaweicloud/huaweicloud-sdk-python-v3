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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodehub'")


class CodeHubClient(Client):
    def __init__(self):
        super(CodeHubClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodehub.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeHubClient":
                raise TypeError("client type error, support client type is CodeHubClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_commit(self, request):
        r"""创建提交

        能够一次提交位于不同目录的多个文件，目录不存在时，能自动创建目录。支持强制覆盖选项，当选择强制覆盖标志为true时，忽略冲突，强制提交。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateCommitResponse`
        """
        http_info = self._create_commit_http_info(request)
        return self._call_api(**http_info)

    def create_commit_invoker(self, request):
        http_info = self._create_commit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_commit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/projects/{repo_id}/repository/commits",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']

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

    def list_commits(self, request):
        r"""查询某个仓库的提交信息

        根据仓库短ID获取提交信息，支持根据文件路径，查询这个路径下所有的commits列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCommits
        :type request: :class:`huaweicloudsdkcodehub.v3.ListCommitsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListCommitsResponse`
        """
        http_info = self._list_commits_http_info(request)
        return self._call_api(**http_info)

    def list_commits_invoker(self, request):
        http_info = self._list_commits_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_commits_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{repo_id}/repository/commits",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_diff_commit(self, request):
        r"""查询某个仓库的提交差异信息

        根据commit id查询提交差异信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiffCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowDiffCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowDiffCommitResponse`
        """
        http_info = self._show_diff_commit_http_info(request)
        return self._call_api(**http_info)

    def show_diff_commit_invoker(self, request):
        http_info = self._show_diff_commit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_diff_commit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{repo_id}/repository/commits/{sha}/diff",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiffCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_single_commit(self, request):
        r"""查询某个仓库的特定提交信息

        获取由commit id或分支或标记的名称标识的特定提交。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowSingleCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowSingleCommitResponse`
        """
        http_info = self._show_single_commit_http_info(request)
        return self._call_api(**http_info)

    def show_single_commit_invoker(self, request):
        http_info = self._show_single_commit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_single_commit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{repo_id}/repository/commits/{sha}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSingleCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_merge_request_discussion(self, request):
        r"""创建MR检视意见

        创建MR检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMergeRequestDiscussion
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateMergeRequestDiscussionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateMergeRequestDiscussionResponse`
        """
        http_info = self._create_merge_request_discussion_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_discussion_invoker(self, request):
        http_info = self._create_merge_request_discussion_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_merge_request_discussion_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/repositories/{repository_id}/merge_requests/{merge_request_iid}/discussions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeRequestDiscussionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_iid' in local_var_params:
            path_params['merge_request_iid'] = local_var_params['merge_request_iid']

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

    def create_merge_request_discussion_note(self, request):
        r"""回复MR检视意见

        回复MR检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMergeRequestDiscussionNote
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateMergeRequestDiscussionNoteRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateMergeRequestDiscussionNoteResponse`
        """
        http_info = self._create_merge_request_discussion_note_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_discussion_note_invoker(self, request):
        http_info = self._create_merge_request_discussion_note_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_merge_request_discussion_note_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/repositories/{repository_id}/merge_requests/{merge_request_iid}/discussions/{discussion_id}/notes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeRequestDiscussionNoteResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_iid' in local_var_params:
            path_params['merge_request_iid'] = local_var_params['merge_request_iid']
        if 'discussion_id' in local_var_params:
            path_params['discussion_id'] = local_var_params['discussion_id']

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

    def show_review_setting(self, request):
        r"""获取检视意见设置

        获取检视意见设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReviewSetting
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowReviewSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowReviewSettingResponse`
        """
        http_info = self._show_review_setting_http_info(request)
        return self._call_api(**http_info)

    def show_review_setting_invoker(self, request):
        http_info = self._show_review_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_review_setting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/review_setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReviewSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def list_files_by_query(self, request):
        r"""查询某个仓库的文件信息

        获取仓库中文件的信息，如名称、大小、内容。请注意，文件内容是Base64编码的。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFilesByQuery
        :type request: :class:`huaweicloudsdkcodehub.v3.ListFilesByQueryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListFilesByQueryResponse`
        """
        http_info = self._list_files_by_query_http_info(request)
        return self._call_api(**http_info)

    def list_files_by_query_invoker(self, request):
        http_info = self._list_files_by_query_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_files_by_query_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{repo_id}/repository/files",
            "request_type": request.__class__.__name__,
            "response_type": "ListFilesByQueryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_file(self, request):
        r"""查询某个仓库的文件信息

        获取仓库中文件的信息，如名称、大小、内容。请注意，文件内容是Base64编码的。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFile
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowFileResponse`
        """
        warnings.warn("Method 'show_file' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_file_http_info(request)
        return self._call_api(**http_info)

    def show_file_invoker(self, request):
        warnings.warn("Method 'show_file_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{repo_id}/repository/files/{file_path}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def get_all_repository_by_project_id(self, request):
        r"""获取项目下所有仓库信息

        获取仓库列表 模糊查询支持范围,如果未传入project_id，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetAllRepositoryByProjectId
        :type request: :class:`huaweicloudsdkcodehub.v3.GetAllRepositoryByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetAllRepositoryByProjectIdResponse`
        """
        warnings.warn("Method 'get_all_repository_by_project_id' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_all_repository_by_project_id_http_info(request)
        return self._call_api(**http_info)

    def get_all_repository_by_project_id_invoker(self, request):
        warnings.warn("Method 'get_all_repository_by_project_id_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_all_repository_by_project_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_all_repository_by_project_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_uuid}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "GetAllRepositoryByProjectIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def get_product_templates(self, request):
        r"""获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetProductTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.GetProductTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetProductTemplatesResponse`
        """
        warnings.warn("Method 'get_product_templates' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_product_templates_http_info(request)
        return self._call_api(**http_info)

    def get_product_templates_invoker(self, request):
        warnings.warn("Method 'get_product_templates_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_product_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_product_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_uuid}/repositories/template_status",
            "request_type": request.__class__.__name__,
            "response_type": "GetProductTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_product_two_templates(self, request):
        r"""获取一个项目下可以设置为公开状态的仓库列表

        获取一个项目下可以设置为公开状态的仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProductTwoTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.ListProductTwoTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListProductTwoTemplatesResponse`
        """
        http_info = self._list_product_two_templates_http_info(request)
        return self._call_api(**http_info)

    def list_product_two_templates_invoker(self, request):
        http_info = self._list_product_two_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_product_two_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{project_uuid}/repositories/template-status",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductTwoTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_repository_name_exist(self, request):
        r"""校验指定项目下的仓库名

        一般创建仓库时调用。通过传入项目ID，获取方式请参见[获取项目ID](codehub_api_0014.xml)。,仓库名，来判断仓库是否重名。仓库存在result:false,仓库不存在result:true。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryNameExist
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryNameExistRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryNameExistResponse`
        """
        http_info = self._show_repository_name_exist_http_info(request)
        return self._call_api(**http_info)

    def show_repository_name_exist_invoker(self, request):
        http_info = self._show_repository_name_exist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_name_exist_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/projects/{project_uuid}/repositories/validation/{repository_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryNameExistResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def add_repo_members(self, request):
        r"""添加仓库成员

        添加仓库成员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRepoMembers
        :type request: :class:`huaweicloudsdkcodehub.v3.AddRepoMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddRepoMembersResponse`
        """
        http_info = self._add_repo_members_http_info(request)
        return self._call_api(**http_info)

    def add_repo_members_invoker(self, request):
        http_info = self._add_repo_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_repo_members_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/repositories/{repository_uuid}/members",
            "request_type": request.__class__.__name__,
            "response_type": "AddRepoMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def delete_repo_member(self, request):
        r"""删除仓库成员

        删除仓库成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepoMember
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteRepoMemberRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteRepoMemberResponse`
        """
        http_info = self._delete_repo_member_http_info(request)
        return self._call_api(**http_info)

    def delete_repo_member_invoker(self, request):
        http_info = self._delete_repo_member_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_repo_member_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/repositories/{repository_uuid}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepoMemberResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_repo_members(self, request):
        r"""获取仓库所有成员记录

        获取仓库成员列表,可通过关键字搜索某成员。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepoMembers
        :type request: :class:`huaweicloudsdkcodehub.v3.ListRepoMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListRepoMembersResponse`
        """
        http_info = self._list_repo_members_http_info(request)
        return self._call_api(**http_info)

    def list_repo_members_invoker(self, request):
        http_info = self._list_repo_members_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repo_members_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepoMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def set_repo_role(self, request):
        r"""设置成员在仓库中的角色

        给仓库中成员设置仓库的操作权限，
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRepoRole
        :type request: :class:`huaweicloudsdkcodehub.v3.SetRepoRoleRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.SetRepoRoleResponse`
        """
        http_info = self._set_repo_role_http_info(request)
        return self._call_api(**http_info)

    def set_repo_role_invoker(self, request):
        http_info = self._set_repo_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_repo_role_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/repositories/{repository_uuid}/members/{member_id}",
            "request_type": request.__class__.__name__,
            "response_type": "SetRepoRoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def add_deploy_key(self, request):
        r"""添加部署密钥

        添加部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyResponse`
        """
        warnings.warn("Method 'add_deploy_key' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_deploy_key_http_info(request)
        return self._call_api(**http_info)

    def add_deploy_key_invoker(self, request):
        warnings.warn("Method 'add_deploy_key_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._add_deploy_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_deploy_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/repositories/{repository_id}/deploy_keys",
            "request_type": request.__class__.__name__,
            "response_type": "AddDeployKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def add_deploy_key_v2(self, request):
        r"""添加部署密钥

        添加部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDeployKeyV2
        :type request: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddDeployKeyV2Response`
        """
        http_info = self._add_deploy_key_v2_http_info(request)
        return self._call_api(**http_info)

    def add_deploy_key_v2_invoker(self, request):
        http_info = self._add_deploy_key_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_deploy_key_v2_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/repositories/{repository_id}/deploy-keys",
            "request_type": request.__class__.__name__,
            "response_type": "AddDeployKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def add_protect_branch_v2(self, request):
        r"""新建保护分支

        新建保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddProtectBranchV2
        :type request: :class:`huaweicloudsdkcodehub.v3.AddProtectBranchV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddProtectBranchV2Response`
        """
        http_info = self._add_protect_branch_v2_http_info(request)
        return self._call_api(**http_info)

    def add_protect_branch_v2_invoker(self, request):
        http_info = self._add_protect_branch_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_protect_branch_v2_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/repositories/{repository_id}/branch/{branch_name}/protect",
            "request_type": request.__class__.__name__,
            "response_type": "AddProtectBranchV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def add_tag_v2(self, request):
        r"""新建标签

        新建标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTagV2
        :type request: :class:`huaweicloudsdkcodehub.v3.AddTagV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddTagV2Response`
        """
        http_info = self._add_tag_v2_http_info(request)
        return self._call_api(**http_info)

    def add_tag_v2_invoker(self, request):
        http_info = self._add_tag_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_tag_v2_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/repositories/{repository_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "AddTagV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def create_repository(self, request):
        r"""创建仓库

        用指定的名称在指定项目上创建仓库。传入参数：仓库名、模板id、是否导入项目成员、归属项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRepository
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateRepositoryResponse`
        """
        http_info = self._create_repository_http_info(request)
        return self._call_api(**http_info)

    def create_repository_invoker(self, request):
        http_info = self._create_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_repository_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepositoryResponse"
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

    def delete_deploy_key(self, request):
        r"""删除仓库部署密钥

        删除仓库部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyResponse`
        """
        warnings.warn("Method 'delete_deploy_key' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_deploy_key_http_info(request)
        return self._call_api(**http_info)

    def delete_deploy_key_invoker(self, request):
        warnings.warn("Method 'delete_deploy_key_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_deploy_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_deploy_key_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/repositories/{repository_id}/deploy_keys/{key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeployKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_deploy_key_v2(self, request):
        r"""删除仓库部署密钥

        删除仓库部署密钥
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployKeyV2
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteDeployKeyV2Response`
        """
        http_info = self._delete_deploy_key_v2_http_info(request)
        return self._call_api(**http_info)

    def delete_deploy_key_v2_invoker(self, request):
        http_info = self._delete_deploy_key_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_deploy_key_v2_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/repositories/{repository_id}/deploy-keys/{key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeployKeyV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_repository(self, request):
        r"""删除仓库

        根据仓库32位uuid删除指定的仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepository
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteRepositoryResponse`
        """
        http_info = self._delete_repository_http_info(request)
        return self._call_api(**http_info)

    def delete_repository_invoker(self, request):
        http_info = self._delete_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_repository_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/repositories/{repository_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def get_repository_by_project_id(self, request):
        r"""查询项目下的某个仓库

        不建议再使用,建议使用/{repository_uuid}/status
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetRepositoryByProjectId
        :type request: :class:`huaweicloudsdkcodehub.v3.GetRepositoryByProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetRepositoryByProjectIdResponse`
        """
        warnings.warn("Method 'get_repository_by_project_id' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_repository_by_project_id_http_info(request)
        return self._call_api(**http_info)

    def get_repository_by_project_id_invoker(self, request):
        warnings.warn("Method 'get_repository_by_project_id_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_repository_by_project_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_repository_by_project_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "GetRepositoryByProjectIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def get_templates(self, request):
        r"""获取公开示例模板列表

        获取公开示例模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.GetTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.GetTemplatesResponse`
        """
        warnings.warn("Method 'get_templates' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_templates_http_info(request)
        return self._call_api(**http_info)

    def get_templates_invoker(self, request):
        warnings.warn("Method 'get_templates_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._get_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/repository_templates",
            "request_type": request.__class__.__name__,
            "response_type": "GetTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_branches_by_repository_id(self, request):
        r"""获取仓库分支列表

        获取仓库分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBranchesByRepositoryId
        :type request: :class:`huaweicloudsdkcodehub.v3.ListBranchesByRepositoryIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListBranchesByRepositoryIdResponse`
        """
        http_info = self._list_branches_by_repository_id_http_info(request)
        return self._call_api(**http_info)

    def list_branches_by_repository_id_invoker(self, request):
        http_info = self._list_branches_by_repository_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_branches_by_repository_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListBranchesByRepositoryIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_commit_statistics(self, request):
        r"""获取仓库上一次的提交统计信息

        获取仓库上一次的提交统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCommitStatistics
        :type request: :class:`huaweicloudsdkcodehub.v3.ListCommitStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListCommitStatisticsResponse`
        """
        http_info = self._list_commit_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_commit_statistics_invoker(self, request):
        http_info = self._list_commit_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_commit_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommitStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_files(self, request):
        r"""获取一个仓库下特定分支指定文件内容

        获取一个仓库下特定分支指定文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFiles
        :type request: :class:`huaweicloudsdkcodehub.v3.ListFilesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListFilesResponse`
        """
        http_info = self._list_files_http_info(request)
        return self._call_api(**http_info)

    def list_files_invoker(self, request):
        http_info = self._list_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/branch/{branch_name}/file",
            "request_type": request.__class__.__name__,
            "response_type": "ListFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-none']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_merge_changes(self, request):
        r"""获取变更文件

        获取变更文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMergeChanges
        :type request: :class:`huaweicloudsdkcodehub.v3.ListMergeChangesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListMergeChangesResponse`
        """
        http_info = self._list_merge_changes_http_info(request)
        return self._call_api(**http_info)

    def list_merge_changes_invoker(self, request):
        http_info = self._list_merge_changes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_merge_changes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/merge-requests/{merge_request_iid}/changes",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeChangesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_iid' in local_var_params:
            path_params['merge_request_iid'] = local_var_params['merge_request_iid']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'ignore_whitespace_change' in local_var_params:
            query_params.append(('ignore_whitespace_change', local_var_params['ignore_whitespace_change']))
        if 'force_encode' in local_var_params:
            query_params.append(('force_encode', local_var_params['force_encode']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'commit_id' in local_var_params:
            query_params.append(('commit_id', local_var_params['commit_id']))

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

    def list_merge_changes_trees(self, request):
        r"""获取变更文件列表

        获取变更文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMergeChangesTrees
        :type request: :class:`huaweicloudsdkcodehub.v3.ListMergeChangesTreesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListMergeChangesTreesResponse`
        """
        http_info = self._list_merge_changes_trees_http_info(request)
        return self._call_api(**http_info)

    def list_merge_changes_trees_invoker(self, request):
        http_info = self._list_merge_changes_trees_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_merge_changes_trees_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/merge-requests/{merge_request_iid}/changes-trees",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeChangesTreesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_iid' in local_var_params:
            path_params['merge_request_iid'] = local_var_params['merge_request_iid']

        query_params = []
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'commit_id' in local_var_params:
            query_params.append(('commit_id', local_var_params['commit_id']))

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

    def list_merge_request(self, request):
        r"""获取仓库合并请求列表

        获取仓库合并请求列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v3.ListMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListMergeRequestResponse`
        """
        http_info = self._list_merge_request_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_invoker(self, request):
        http_info = self._list_merge_request_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_merge_request_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/merge_request",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_merge_request_reviewers(self, request):
        r"""根据仓库短ID和合并请求短ID获取检视人信息

        根据仓库短ID和合并请求短ID获取检视人信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMergeRequestReviewers
        :type request: :class:`huaweicloudsdkcodehub.v3.ListMergeRequestReviewersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListMergeRequestReviewersResponse`
        """
        http_info = self._list_merge_request_reviewers_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_reviewers_invoker(self, request):
        http_info = self._list_merge_request_reviewers_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_merge_request_reviewers_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/merge-requests/{merge_request_iid}/approval-reviewers",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestReviewersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_iid' in local_var_params:
            path_params['merge_request_iid'] = local_var_params['merge_request_iid']

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

    def list_related_commits(self, request):
        r"""获取关联工作项信息

        获取关联工作项信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelatedCommits
        :type request: :class:`huaweicloudsdkcodehub.v3.ListRelatedCommitsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListRelatedCommitsResponse`
        """
        http_info = self._list_related_commits_http_info(request)
        return self._call_api(**http_info)

    def list_related_commits_invoker(self, request):
        http_info = self._list_related_commits_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_related_commits_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_uuid}/related-commits",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelatedCommitsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
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

    def list_repository_status(self, request):
        r"""查看仓库的创建状态

        获取仓库状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepositoryStatus
        :type request: :class:`huaweicloudsdkcodehub.v3.ListRepositoryStatusRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListRepositoryStatusResponse`
        """
        http_info = self._list_repository_status_http_info(request)
        return self._call_api(**http_info)

    def list_repository_status_invoker(self, request):
        http_info = self._list_repository_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repository_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def list_subfiles(self, request):
        r"""获取分支目录下的文件

        获取分支目录下的文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubfiles
        :type request: :class:`huaweicloudsdkcodehub.v3.ListSubfilesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListSubfilesResponse`
        """
        http_info = self._list_subfiles_http_info(request)
        return self._call_api(**http_info)

    def list_subfiles_invoker(self, request):
        http_info = self._list_subfiles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_subfiles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/branch/{branch_name}/sub-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubfilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_templates_two(self, request):
        r"""设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplatesTwo
        :type request: :class:`huaweicloudsdkcodehub.v3.ListTemplatesTwoRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListTemplatesTwoResponse`
        """
        http_info = self._list_templates_two_http_info(request)
        return self._call_api(**http_info)

    def list_templates_two_invoker(self, request):
        http_info = self._list_templates_two_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_templates_two_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/repositories/{repository_uuid}/template-status",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesTwoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def list_two_templates(self, request):
        r"""获取公开示例模板列表

        获取公开示例模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTwoTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.ListTwoTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListTwoTemplatesResponse`
        """
        http_info = self._list_two_templates_http_info(request)
        return self._call_api(**http_info)

    def list_two_templates_invoker(self, request):
        http_info = self._list_two_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_two_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/repository-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTwoTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def share_templates(self, request):
        r"""设置仓库是公开状态还是私有状态

        设置仓库是公开状态还是私有状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShareTemplates
        :type request: :class:`huaweicloudsdkcodehub.v3.ShareTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShareTemplatesResponse`
        """
        warnings.warn("Method 'share_templates' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._share_templates_http_info(request)
        return self._call_api(**http_info)

    def share_templates_invoker(self, request):
        warnings.warn("Method 'share_templates_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._share_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _share_templates_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/repositories/{repository_uuid}/template_status",
            "request_type": request.__class__.__name__,
            "response_type": "ShareTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def show_branches_by_repository_id(self, request):
        r"""查询某仓库对应的分支

        根据仓库id获取指定仓库的分支列表.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBranchesByRepositoryId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByRepositoryIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByRepositoryIdResponse`
        """
        http_info = self._show_branches_by_repository_id_http_info(request)
        return self._call_api(**http_info)

    def show_branches_by_repository_id_invoker(self, request):
        http_info = self._show_branches_by_repository_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_branches_by_repository_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_id}/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBranchesByRepositoryIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def show_branches_by_two_repository_id(self, request):
        r"""查询某仓库的标签列表

        查询指定仓库对应的分支。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBranchesByTwoRepositoryId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByTwoRepositoryIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowBranchesByTwoRepositoryIdResponse`
        """
        http_info = self._show_branches_by_two_repository_id_http_info(request)
        return self._call_api(**http_info)

    def show_branches_by_two_repository_id_invoker(self, request):
        http_info = self._show_branches_by_two_repository_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_branches_by_two_repository_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBranchesByTwoRepositoryIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def show_commits_by_branch(self, request):
        r"""根据组名和仓库名查询某仓库某分支对应的提交

        根据仓库组名、仓库名和分支获取提交列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCommitsByBranch
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByBranchResponse`
        """
        http_info = self._show_commits_by_branch_http_info(request)
        return self._call_api(**http_info)

    def show_commits_by_branch_invoker(self, request):
        http_info = self._show_commits_by_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_commits_by_branch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{group_name}/{repository_name}/commits",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommitsByBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_commits_by_repo_id(self, request):
        r"""根据仓库id查询仓库某分支对应的提交，提供更多可选参数

        根据仓库id查询仓库某分支对应的提交.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCommitsByRepoId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByRepoIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowCommitsByRepoIdResponse`
        """
        http_info = self._show_commits_by_repo_id_http_info(request)
        return self._call_api(**http_info)

    def show_commits_by_repo_id_invoker(self, request):
        http_info = self._show_commits_by_repo_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_commits_by_repo_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_id}/commits",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommitsByRepoIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_has_pipeline(self, request):
        r"""修改被流水线引用的仓库状态

        修改被流水线引用的仓库状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHasPipeline
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowHasPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowHasPipelineResponse`
        """
        http_info = self._show_has_pipeline_http_info(request)
        return self._call_api(**http_info)

    def show_has_pipeline_invoker(self, request):
        http_info = self._show_has_pipeline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_has_pipeline_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/repositories/{repository_uuid}/pipeline",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHasPipelineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def show_image_blob(self, request):
        r"""获取一个仓库下特定分支的图片文件

        获取一个仓库下特定分支的图片文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageBlob
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowImageBlobRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowImageBlobResponse`
        """
        http_info = self._show_image_blob_http_info(request)
        return self._call_api(**http_info)

    def show_image_blob_invoker(self, request):
        http_info = self._show_image_blob_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_image_blob_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/branch/{branch_name}/image",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageBlobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam-none']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_master(self, request):
        r"""判断用户是否有仓库的管理员权限

        判断用户是否有仓库的管理员权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMaster
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowMasterRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowMasterResponse`
        """
        http_info = self._show_master_http_info(request)
        return self._call_api(**http_info)

    def show_master_invoker(self, request):
        http_info = self._show_master_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_master_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/master",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMasterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def show_merge_request(self, request):
        r"""获取仓库合并请求详情

        获取仓库合并请求详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowMergeRequestResponse`
        """
        http_info = self._show_merge_request_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_invoker(self, request):
        http_info = self._show_merge_request_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_merge_request_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/merge_request/{merge_request_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_repo_id(self, request):
        r"""根据仓库名组名获取仓库短id，用以拼接与commitid对应提交详情页面url

        获取仓库短id,用于获取仓库详情页面url
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepoId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepoIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepoIdResponse`
        """
        http_info = self._show_repo_id_http_info(request)
        return self._call_api(**http_info)

    def show_repo_id_invoker(self, request):
        http_info = self._show_repo_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repo_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/repoid",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepoIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_repository_archive(self, request):
        r"""下载仓库

        按照指定格式下载仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryArchive
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryArchiveRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryArchiveResponse`
        """
        http_info = self._show_repository_archive_http_info(request)
        return self._call_api(**http_info)

    def show_repository_archive_invoker(self, request):
        http_info = self._show_repository_archive_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_archive_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_uuid}/archive",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryArchiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_repository_by_uuid(self, request):
        r"""查询某个仓库的详细信息

        根据仓库UUID(由CreateRepository接口返回)获取仓库信息仓库信息。返回 包含id，name，组名，仓库访问URL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryByUuid
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryByUuidRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryByUuidResponse`
        """
        http_info = self._show_repository_by_uuid_http_info(request)
        return self._call_api(**http_info)

    def show_repository_by_uuid_invoker(self, request):
        http_info = self._show_repository_by_uuid_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_by_uuid_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_uuid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryByUuidResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def show_repository_statistics(self, request):
        r"""仓库统计

        根据仓库短id，查询仓库的代码提交记录统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryStatistics
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowRepositoryStatisticsResponse`
        """
        http_info = self._show_repository_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_repository_statistics_invoker(self, request):
        http_info = self._show_repository_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/repositories/{repository_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def show_statistic_commit(self, request):
        r"""获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStatisticCommit
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitResponse`
        """
        warnings.warn("Method 'show_statistic_commit' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_statistic_commit_http_info(request)
        return self._call_api(**http_info)

    def show_statistic_commit_invoker(self, request):
        warnings.warn("Method 'show_statistic_commit_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_statistic_commit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_statistic_commit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/repositories/{repository_id}/commit_lines",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStatisticCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_statistic_commit_v3(self, request):
        r"""获取代码提交行数

        获取指定日期内代码仓指定分支的代码提交行数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStatisticCommitV3
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitV3Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowStatisticCommitV3Response`
        """
        http_info = self._show_statistic_commit_v3_http_info(request)
        return self._call_api(**http_info)

    def show_statistic_commit_v3_invoker(self, request):
        http_info = self._show_statistic_commit_v3_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_statistic_commit_v3_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/repositories/{repository_id}/commit-lines",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStatisticCommitV3Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_statistical_data(self, request):
        r"""获取仓库统计数据

        获取仓库统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStatisticalData
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowStatisticalDataRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowStatisticalDataResponse`
        """
        http_info = self._show_statistical_data_http_info(request)
        return self._call_api(**http_info)

    def show_statistical_data_invoker(self, request):
        http_info = self._show_statistical_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_statistical_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{repository_uuid}/statistic-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStatisticalDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_uuid' in local_var_params:
            path_params['repository_uuid'] = local_var_params['repository_uuid']

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

    def update_merge_request_approval_state(self, request):
        r"""合并请求代码审核

        合并请求代码审核
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMergeRequestApprovalState
        :type request: :class:`huaweicloudsdkcodehub.v3.UpdateMergeRequestApprovalStateRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.UpdateMergeRequestApprovalStateResponse`
        """
        http_info = self._update_merge_request_approval_state_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_approval_state_invoker(self, request):
        http_info = self._update_merge_request_approval_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_merge_request_approval_state_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/repositories/{repository_id}/merge-requests/{merge_request_iid}/approval",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestApprovalStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'merge_request_iid' in local_var_params:
            path_params['merge_request_iid'] = local_var_params['merge_request_iid']

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

    def add_ssh_key(self, request):
        r"""添加ssh key

        添加ssh key
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddSshKey
        :type request: :class:`huaweicloudsdkcodehub.v3.AddSshKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddSshKeyResponse`
        """
        http_info = self._add_ssh_key_http_info(request)
        return self._call_api(**http_info)

    def add_ssh_key_invoker(self, request):
        http_info = self._add_ssh_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_ssh_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/users/sshkey",
            "request_type": request.__class__.__name__,
            "response_type": "AddSshKeyResponse"
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

    def delete_s_shkey(self, request):
        r"""删除用户公钥

        删除用户公钥。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSShkey
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteSShkeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteSShkeyResponse`
        """
        warnings.warn("Method 'delete_s_shkey' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_s_shkey_http_info(request)
        return self._call_api(**http_info)

    def delete_s_shkey_invoker(self, request):
        warnings.warn("Method 'delete_s_shkey_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_s_shkey_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_s_shkey_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/users/sshkey/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSShkeyResponse"
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

    def list_ssh_keys(self, request):
        r"""获取ssh key列表

        获取ssh key列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSshKeys
        :type request: :class:`huaweicloudsdkcodehub.v3.ListSshKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListSshKeysResponse`
        """
        http_info = self._list_ssh_keys_http_info(request)
        return self._call_api(**http_info)

    def list_ssh_keys_invoker(self, request):
        http_info = self._list_ssh_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ssh_keys_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/users/sshkey",
            "request_type": request.__class__.__name__,
            "response_type": "ListSshKeysResponse"
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

    def show_private_key_verify(self, request):
        r"""检验私钥是否有拉取代码的权限

        检验私钥是否有拉取代码的权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPrivateKeyVerify
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowPrivateKeyVerifyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowPrivateKeyVerifyResponse`
        """
        http_info = self._show_private_key_verify_http_info(request)
        return self._call_api(**http_info)

    def show_private_key_verify_invoker(self, request):
        http_info = self._show_private_key_verify_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_private_key_verify_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/users/sshkey/privatekey/verify",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivateKeyVerifyResponse"
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

    def validate_https_info(self, request):
        r""" https账号密码校验

        判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateHttpsInfo
        :type request: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoResponse`
        """
        warnings.warn("Method 'validate_https_info' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._validate_https_info_http_info(request)
        return self._call_api(**http_info)

    def validate_https_info_invoker(self, request):
        warnings.warn("Method 'validate_https_info_invoker' of CodeHubClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._validate_https_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_https_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/user/{iam_user_uuid}/validateHttpsInfo",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateHttpsInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'iam_user_uuid' in local_var_params:
            path_params['iam_user_uuid'] = local_var_params['iam_user_uuid']

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

    def validate_https_info_v2(self, request):
        r"""https账号密码校验

        判断用户使用 https 上传/下载代码时输入的用户名和密码是否合法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateHttpsInfoV2
        :type request: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoV2Request`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ValidateHttpsInfoV2Response`
        """
        http_info = self._validate_https_info_v2_http_info(request)
        return self._call_api(**http_info)

    def validate_https_info_v2_invoker(self, request):
        http_info = self._validate_https_info_v2_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_https_info_v2_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/user/{iam_user_uuid}/validate-https-info",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateHttpsInfoV2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'iam_user_uuid' in local_var_params:
            path_params['iam_user_uuid'] = local_var_params['iam_user_uuid']

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

    def associate_issues(self, request):
        r"""分支关联工作项

        分支关联工作项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AssociateIssues
        :type request: :class:`huaweicloudsdkcodehub.v3.AssociateIssuesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AssociateIssuesResponse`
        """
        http_info = self._associate_issues_http_info(request)
        return self._call_api(**http_info)

    def associate_issues_invoker(self, request):
        http_info = self._associate_issues_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _associate_issues_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/projects/issues",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateIssuesResponse"
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

    def create_project_and_repositories(self, request):
        r"""创建项目、仓库

        创建项目后，创建仓库组由后台生成方式 传入参数：仓库名、模板id、是否导入项目成员、归属项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectAndRepositories
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndRepositoriesResponse`
        """
        http_info = self._create_project_and_repositories_http_info(request)
        return self._call_api(**http_info)

    def create_project_and_repositories_invoker(self, request):
        http_info = self._create_project_and_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_and_repositories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/projects/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectAndRepositoriesResponse"
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

    def create_project_andfork_repositories(self, request):
        r"""创建项目并fork仓库

        创建仓库后fork仓库 传入参数：仓库名、是否导入项目成员、归属项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectAndforkRepositories
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndforkRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateProjectAndforkRepositoriesResponse`
        """
        http_info = self._create_project_andfork_repositories_http_info(request)
        return self._call_api(**http_info)

    def create_project_andfork_repositories_invoker(self, request):
        http_info = self._create_project_andfork_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_andfork_repositories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/projects/repositories/fork",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectAndforkRepositoriesResponse"
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

    def list_user_all_repositories(self, request):
        r"""查询用户的所有仓库

        获取用户的所有仓库信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserAllRepositories
        :type request: :class:`huaweicloudsdkcodehub.v3.ListUserAllRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListUserAllRepositoriesResponse`
        """
        http_info = self._list_user_all_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_user_all_repositories_invoker(self, request):
        http_info = self._list_user_all_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_all_repositories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserAllRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_all_repository_by_two_project_id(self, request):
        r"""查询项目下的所有仓库

        获取仓库列表,模糊查询支持范围,如果未传入project uuid，则支持按仓库名或项目名模糊查询，否则，只按仓库名模糊匹配
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllRepositoryByTwoProjectId
        :type request: :class:`huaweicloudsdkcodehub.v3.ShowAllRepositoryByTwoProjectIdRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ShowAllRepositoryByTwoProjectIdResponse`
        """
        http_info = self._show_all_repository_by_two_project_id_http_info(request)
        return self._call_api(**http_info)

    def show_all_repository_by_two_project_id_invoker(self, request):
        http_info = self._show_all_repository_by_two_project_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_repository_by_two_project_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/projects/{project_uuid}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllRepositoryByTwoProjectIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def add_hooks(self, request):
        r"""为指定仓库添加hook

        提交代码自动触发编译构建，添加仓库钩子
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddHooks
        :type request: :class:`huaweicloudsdkcodehub.v3.AddHooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.AddHooksResponse`
        """
        http_info = self._add_hooks_http_info(request)
        return self._call_api(**http_info)

    def add_hooks_invoker(self, request):
        http_info = self._add_hooks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_hooks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/repositories/{group_name}/{repository_name}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "AddHooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_hooks(self, request):
        r"""删除指定仓库的 hook

        提交代码自动触发编译构建，删除仓库钩子
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHooks
        :type request: :class:`huaweicloudsdkcodehub.v3.DeleteHooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.DeleteHooksResponse`
        """
        http_info = self._delete_hooks_http_info(request)
        return self._call_api(**http_info)

    def delete_hooks_invoker(self, request):
        http_info = self._delete_hooks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_hooks_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/repositories/{group_name}/{repository_name}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_hooks(self, request):
        r"""查询指定仓库的webhook

        获取仓库webhook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHooks
        :type request: :class:`huaweicloudsdkcodehub.v3.ListHooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.ListHooksResponse`
        """
        http_info = self._list_hooks_http_info(request)
        return self._call_api(**http_info)

    def list_hooks_invoker(self, request):
        http_info = self._list_hooks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_hooks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/repositories/{group_name}/{repository_name}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListHooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_new_branch(self, request):
        r"""创建分支

        根据仓库id在指定仓库中创建分支
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNewBranch
        :type request: :class:`huaweicloudsdkcodehub.v3.CreateNewBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateNewBranchResponse`
        """
        http_info = self._create_new_branch_http_info(request)
        return self._call_api(**http_info)

    def create_new_branch_invoker(self, request):
        http_info = self._create_new_branch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_new_branch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/repositories/{repository_id}/branches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNewBranchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

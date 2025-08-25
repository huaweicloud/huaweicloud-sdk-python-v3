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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodehub'")


class CodeHubAsyncClient(Client):
    def __init__(self):
        super(CodeHubAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodehub.v4.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeHubAsyncClient":
                raise TypeError("client type error, support client type is CodeHubAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_branch_async(self, request):
        r"""创建分支

        创建分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateBranchResponse`
        """
        http_info = self._create_branch_http_info(request)
        return self._call_api(**http_info)

    def create_branch_async_invoker(self, request):
        http_info = self._create_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_branch_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/branches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBranchResponse"
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

    def delete_branch_async(self, request):
        r"""删除分支

        删除分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteBranchResponse`
        """
        http_info = self._delete_branch_http_info(request)
        return self._call_api(**http_info)

    def delete_branch_async_invoker(self, request):
        http_info = self._delete_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_branch_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/repository/branch",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBranchResponse"
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

    def list_branches_async(self, request):
        r"""获取分支列表

        获取分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBranches
        :type request: :class:`huaweicloudsdkcodehub.v4.ListBranchesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListBranchesResponse`
        """
        http_info = self._list_branches_http_info(request)
        return self._call_api(**http_info)

    def list_branches_async_invoker(self, request):
        http_info = self._list_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_branches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListBranchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'branch_type' in local_var_params:
            query_params.append(('branch_type', local_var_params['branch_type']))
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'query_view' in local_var_params:
            query_params.append(('query_view', local_var_params['query_view']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_branch_async(self, request):
        r"""获取分支详情

        获取分支详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowBranchResponse`
        """
        http_info = self._show_branch_http_info(request)
        return self._call_api(**http_info)

    def show_branch_async_invoker(self, request):
        http_info = self._show_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_branch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/branch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBranchResponse"
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

        response_headers = ["X-Total", ]

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

    def update_branch_name_async(self, request):
        r"""分支重命名

        分支重命名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBranchName
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateBranchNameRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateBranchNameResponse`
        """
        http_info = self._update_branch_name_http_info(request)
        return self._call_api(**http_info)

    def update_branch_name_async_invoker(self, request):
        http_info = self._update_branch_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_branch_name_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/repository/branch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBranchNameResponse"
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

    def create_commit_async(self, request):
        r"""创建提交信息

        创建提交信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCommit
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateCommitResponse`
        """
        http_info = self._create_commit_http_info(request)
        return self._call_api(**http_info)

    def create_commit_async_invoker(self, request):
        http_info = self._create_commit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_commit_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCommitResponse"
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

    def create_commit_revert_async(self, request):
        r"""回退提交

        回退提交
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCommitRevert
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateCommitRevertRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateCommitRevertResponse`
        """
        http_info = self._create_commit_revert_http_info(request)
        return self._call_api(**http_info)

    def create_commit_revert_async_invoker(self, request):
        http_info = self._create_commit_revert_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_commit_revert_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits/{sha}/revert",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCommitRevertResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'sha' in local_var_params:
            path_params['sha'] = local_var_params['sha']

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

    def list_commit_associated_refs_async(self, request):
        r"""根据提交ID查询分支、标签列表

        根据提交ID查询分支、标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommitAssociatedRefs
        :type request: :class:`huaweicloudsdkcodehub.v4.ListCommitAssociatedRefsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListCommitAssociatedRefsResponse`
        """
        http_info = self._list_commit_associated_refs_http_info(request)
        return self._call_api(**http_info)

    def list_commit_associated_refs_async_invoker(self, request):
        http_info = self._list_commit_associated_refs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_commit_associated_refs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits/{sha}/refs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommitAssociatedRefsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'sha' in local_var_params:
            path_params['sha'] = local_var_params['sha']

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

    def show_commit_async(self, request):
        r"""获取特定提交信息

        获取特定提交信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommit
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowCommitResponse`
        """
        http_info = self._show_commit_http_info(request)
        return self._call_api(**http_info)

    def show_commit_async_invoker(self, request):
        http_info = self._show_commit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_commit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))
        if 'stats' in local_var_params:
            query_params.append(('stats', local_var_params['stats']))
        if 'show_code_changes' in local_var_params:
            query_params.append(('show_code_changes', local_var_params['show_code_changes']))

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

    def show_commit_diff_metadata_async(self, request):
        r"""获取commit引入的文件变更元数据

        获取commit引入的文件变更元数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommitDiffMetadata
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowCommitDiffMetadataRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowCommitDiffMetadataResponse`
        """
        http_info = self._show_commit_diff_metadata_http_info(request)
        return self._call_api(**http_info)

    def show_commit_diff_metadata_async_invoker(self, request):
        http_info = self._show_commit_diff_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_commit_diff_metadata_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits/diff-metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommitDiffMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))

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

    def show_commit_file_diff_async(self, request):
        r"""获取commit引入的指定文件的变更内容

        获取commit引入的指定文件的变更内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommitFileDiff
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowCommitFileDiffRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowCommitFileDiffResponse`
        """
        http_info = self._show_commit_file_diff_http_info(request)
        return self._call_api(**http_info)

    def show_commit_file_diff_async_invoker(self, request):
        http_info = self._show_commit_file_diff_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_commit_file_diff_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits/file-diff",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommitFileDiffResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'old_path' in local_var_params:
            query_params.append(('old_path', local_var_params['old_path']))
        if 'ignore_whitespace_change' in local_var_params:
            query_params.append(('ignore_whitespace_change', local_var_params['ignore_whitespace_change']))

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

    def show_diff_commit_async(self, request):
        r"""获取提交差异

        获取提交差异
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDiffCommit
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowDiffCommitRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowDiffCommitResponse`
        """
        http_info = self._show_diff_commit_http_info(request)
        return self._call_api(**http_info)

    def show_diff_commit_async_invoker(self, request):
        http_info = self._show_diff_commit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_diff_commit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/commits/diff",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiffCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))
        if 'ignore_whitespace_change' in local_var_params:
            query_params.append(('ignore_whitespace_change', local_var_params['ignore_whitespace_change']))
        if 'not_statistic' in local_var_params:
            query_params.append(('not_statistic', local_var_params['not_statistic']))
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

    def create_merge_request_discussion_async(self, request):
        r"""创建合并请求检视意见

        创建合并请求检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMergeRequestDiscussion
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestDiscussionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestDiscussionResponse`
        """
        http_info = self._create_merge_request_discussion_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_discussion_async_invoker(self, request):
        http_info = self._create_merge_request_discussion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_merge_request_discussion_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/discussions",
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

    def create_merge_request_discussion_response_async(self, request):
        r"""回复合并请求检视意见

        回复合并请求检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMergeRequestDiscussionResponse
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestDiscussionResponseRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestDiscussionResponseResponse`
        """
        http_info = self._create_merge_request_discussion_response_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_discussion_response_async_invoker(self, request):
        http_info = self._create_merge_request_discussion_response_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_merge_request_discussion_response_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/discussions/{discussion_id}/notes",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeRequestDiscussionResponseResponse"
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

    def create_review_setting_async(self, request):
        r"""创建/更新检视意见设置

        创建/更新检视意见设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReviewSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateReviewSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateReviewSettingResponse`
        """
        http_info = self._create_review_setting_http_info(request)
        return self._call_api(**http_info)

    def create_review_setting_async_invoker(self, request):
        http_info = self._create_review_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_review_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/review-settings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateReviewSettingResponse"
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

    def list_default_review_categories_async(self, request):
        r"""获取默认的检视意见分类

        获取默认的检视意见分类
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDefaultReviewCategories
        :type request: :class:`huaweicloudsdkcodehub.v4.ListDefaultReviewCategoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListDefaultReviewCategoriesResponse`
        """
        http_info = self._list_default_review_categories_http_info(request)
        return self._call_api(**http_info)

    def list_default_review_categories_async_invoker(self, request):
        http_info = self._list_default_review_categories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_default_review_categories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/default-review-categories",
            "request_type": request.__class__.__name__,
            "response_type": "ListDefaultReviewCategoriesResponse"
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

    def list_merge_request_discussions_async(self, request):
        r"""获取合并请求检视意见列表

        获取合并请求检视意见列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestDiscussions
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestDiscussionsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestDiscussionsResponse`
        """
        http_info = self._list_merge_request_discussions_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_discussions_async_invoker(self, request):
        http_info = self._list_merge_request_discussions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_discussions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/discussions",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestDiscussionsResponse"
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
        if 'unresolved' in local_var_params:
            query_params.append(('unresolved', local_var_params['unresolved']))
        if 'author_id' in local_var_params:
            query_params.append(('author_id', local_var_params['author_id']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
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

    def list_project_note_required_attributes_async(self, request):
        r"""获取项目检视意见必填项

        获取项目检视意见必填项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectNoteRequiredAttributes
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectNoteRequiredAttributesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectNoteRequiredAttributesResponse`
        """
        http_info = self._list_project_note_required_attributes_http_info(request)
        return self._call_api(**http_info)

    def list_project_note_required_attributes_async_invoker(self, request):
        http_info = self._list_project_note_required_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_note_required_attributes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/setting/note-required-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectNoteRequiredAttributesResponse"
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

    def list_repository_review_authors_async(self, request):
        r"""获取仓库下检视意见作者列表

        获取仓库下检视意见作者列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryReviewAuthors
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryReviewAuthorsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryReviewAuthorsResponse`
        """
        http_info = self._list_repository_review_authors_http_info(request)
        return self._call_api(**http_info)

    def list_repository_review_authors_async_invoker(self, request):
        http_info = self._list_repository_review_authors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_review_authors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/review-authors",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryReviewAuthorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'noteable_type' in local_var_params:
            query_params.append(('noteable_type', local_var_params['noteable_type']))
        if 'resolved_status' in local_var_params:
            query_params.append(('resolved_status', local_var_params['resolved_status']))
        if 'reviewers_filter' in local_var_params:
            query_params.append(('reviewers_filter', local_var_params['reviewers_filter']))
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

    def list_repository_reviews_async(self, request):
        r"""获取仓库检视意见列表

        获取仓库检视意见列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryReviews
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryReviewsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryReviewsResponse`
        """
        http_info = self._list_repository_reviews_http_info(request)
        return self._call_api(**http_info)

    def list_repository_reviews_async_invoker(self, request):
        http_info = self._list_repository_reviews_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_reviews_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/reviews",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryReviewsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'noteable_type' in local_var_params:
            query_params.append(('noteable_type', local_var_params['noteable_type']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'only_count' in local_var_params:
            query_params.append(('only_count', local_var_params['only_count']))
        if 'review_categories' in local_var_params:
            query_params.append(('review_categories', local_var_params['review_categories']))
        if 'review_modules' in local_var_params:
            query_params.append(('review_modules', local_var_params['review_modules']))
        if 'severity' in local_var_params:
            query_params.append(('severity', local_var_params['severity']))
        if 'assignee_id' in local_var_params:
            query_params.append(('assignee_id', local_var_params['assignee_id']))
        if 'proposer_id' in local_var_params:
            query_params.append(('proposer_id', local_var_params['proposer_id']))
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))
        if 'include_reply' in local_var_params:
            query_params.append(('include_reply', local_var_params['include_reply']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
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

    def show_group_note_required_attributes_async(self, request):
        r"""获取代码组检视意见必填项

        获取代码组检视意见必填项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupNoteRequiredAttributes
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupNoteRequiredAttributesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupNoteRequiredAttributesResponse`
        """
        http_info = self._show_group_note_required_attributes_http_info(request)
        return self._call_api(**http_info)

    def show_group_note_required_attributes_async_invoker(self, request):
        http_info = self._show_group_note_required_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_note_required_attributes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/setting/note-required-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupNoteRequiredAttributesResponse"
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

    def show_group_review_settings_async(self, request):
        r"""获取代码组检视意见设置(不含必填项)

        获取代码组检视意见设置(不含必填项)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupReviewSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupReviewSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupReviewSettingsResponse`
        """
        http_info = self._show_group_review_settings_http_info(request)
        return self._call_api(**http_info)

    def show_group_review_settings_async_invoker(self, request):
        http_info = self._show_group_review_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_review_settings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/review-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupReviewSettingsResponse"
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

    def show_merge_request_discussion_async(self, request):
        r"""根据discussion_id获取合并请求检视意见

        根据discussion_id获取合并请求检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeRequestDiscussion
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestDiscussionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestDiscussionResponse`
        """
        http_info = self._show_merge_request_discussion_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_discussion_async_invoker(self, request):
        http_info = self._show_merge_request_discussion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_merge_request_discussion_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/discussions/{discussion_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestDiscussionResponse"
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

    def show_note_required_attributes_async(self, request):
        r"""获取仓库检视意见必填项

        获取仓库检视意见必填项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNoteRequiredAttributes
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowNoteRequiredAttributesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowNoteRequiredAttributesResponse`
        """
        http_info = self._show_note_required_attributes_http_info(request)
        return self._call_api(**http_info)

    def show_note_required_attributes_async_invoker(self, request):
        http_info = self._show_note_required_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_note_required_attributes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/setting/note-required-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNoteRequiredAttributesResponse"
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

    def show_project_review_settings_async(self, request):
        r"""获取项目检视意见设置(不含必填项)

        获取项目检视意见设置(不含必填项)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectReviewSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectReviewSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectReviewSettingsResponse`
        """
        http_info = self._show_project_review_settings_http_info(request)
        return self._call_api(**http_info)

    def show_project_review_settings_async_invoker(self, request):
        http_info = self._show_project_review_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_review_settings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/review-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectReviewSettingsResponse"
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

    def show_review_setting_async(self, request):
        r"""获取检视意见设置

        获取检视意见设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReviewSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowReviewSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowReviewSettingResponse`
        """
        http_info = self._show_review_setting_http_info(request)
        return self._call_api(**http_info)

    def show_review_setting_async_invoker(self, request):
        http_info = self._show_review_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_review_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/review-setting",
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
        if 'with_default_review_categories' in local_var_params:
            query_params.append(('with_default_review_categories', local_var_params['with_default_review_categories']))

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

    def update_group_note_required_attributes_async(self, request):
        r"""创建/更新代码组检视意见必填项

        创建/更新代码组检视意见必填项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroupNoteRequiredAttributes
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateGroupNoteRequiredAttributesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateGroupNoteRequiredAttributesResponse`
        """
        http_info = self._update_group_note_required_attributes_http_info(request)
        return self._call_api(**http_info)

    def update_group_note_required_attributes_async_invoker(self, request):
        http_info = self._update_group_note_required_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_note_required_attributes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/groups/{group_id}/setting/note-required-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupNoteRequiredAttributesResponse"
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

    def update_group_review_settings_async(self, request):
        r"""创建/更新代码组检视意见设置(不含必填项)

        创建/更新代码组检视意见设置(不含必填项)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroupReviewSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateGroupReviewSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateGroupReviewSettingsResponse`
        """
        http_info = self._update_group_review_settings_http_info(request)
        return self._call_api(**http_info)

    def update_group_review_settings_async_invoker(self, request):
        http_info = self._update_group_review_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_review_settings_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/groups/{group_id}/review-settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupReviewSettingsResponse"
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

    def update_merge_request_discussion_async(self, request):
        r"""更新合并请求检视意见

        更新合并请求检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestDiscussion
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestDiscussionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestDiscussionResponse`
        """
        http_info = self._update_merge_request_discussion_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_discussion_async_invoker(self, request):
        http_info = self._update_merge_request_discussion_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_discussion_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/discussions/{discussion_id}/notes/{note_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestDiscussionResponse"
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
        if 'note_id' in local_var_params:
            path_params['note_id'] = local_var_params['note_id']

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

    def update_note_required_attributes_async(self, request):
        r"""创建/更新仓库检视意见必填项

        创建/更新仓库检视意见必填项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNoteRequiredAttributes
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateNoteRequiredAttributesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateNoteRequiredAttributesResponse`
        """
        http_info = self._update_note_required_attributes_http_info(request)
        return self._call_api(**http_info)

    def update_note_required_attributes_async_invoker(self, request):
        http_info = self._update_note_required_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_note_required_attributes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/setting/note-required-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNoteRequiredAttributesResponse"
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

    def update_project_note_required_attributes_async(self, request):
        r"""创建/更新项目检视意见必填项

        创建/更新项目检视意见必填项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectNoteRequiredAttributes
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProjectNoteRequiredAttributesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProjectNoteRequiredAttributesResponse`
        """
        http_info = self._update_project_note_required_attributes_http_info(request)
        return self._call_api(**http_info)

    def update_project_note_required_attributes_async_invoker(self, request):
        http_info = self._update_project_note_required_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_note_required_attributes_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/setting/note-required-attributes",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectNoteRequiredAttributesResponse"
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

    def update_project_review_settings_async(self, request):
        r"""创建/更新项目检视意见设置(不含必填项)

        创建/更新项目检视意见设置(不含必填项)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectReviewSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProjectReviewSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProjectReviewSettingsResponse`
        """
        http_info = self._update_project_review_settings_http_info(request)
        return self._call_api(**http_info)

    def update_project_review_settings_async_invoker(self, request):
        http_info = self._update_project_review_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_review_settings_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/review-settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectReviewSettingsResponse"
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

    def create_file_async(self, request):
        r"""创建文件

        创建文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFile
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateFileResponse`
        """
        http_info = self._create_file_http_info(request)
        return self._call_api(**http_info)

    def create_file_async_invoker(self, request):
        http_info = self._create_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFileResponse"
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

    def delete_file_async(self, request):
        r"""删除文件

        删除文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFile
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteFileResponse`
        """
        http_info = self._delete_file_http_info(request)
        return self._call_api(**http_info)

    def delete_file_async_invoker(self, request):
        http_info = self._delete_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_file_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/repository/file",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'author_name' in local_var_params:
            query_params.append(('author_name', local_var_params['author_name']))
        if 'branch' in local_var_params:
            query_params.append(('branch', local_var_params['branch']))
        if 'commit_message' in local_var_params:
            query_params.append(('commit_message', local_var_params['commit_message']))
        if 'author_email' in local_var_params:
            query_params.append(('author_email', local_var_params['author_email']))

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

    def download_blobs_raw_async(self, request):
        r"""获取仓库单个文件内容(下载单个文件)

        获取仓库单个文件内容(下载单个文件)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBlobsRaw
        :type request: :class:`huaweicloudsdkcodehub.v4.DownloadBlobsRawRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DownloadBlobsRawResponse`
        """
        http_info = self._download_blobs_raw_http_info(request)
        return self._call_api(**http_info)

    def download_blobs_raw_async_invoker(self, request):
        http_info = self._download_blobs_raw_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_blobs_raw_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/blobs/{blob_id}/raw",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadBlobsRawResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'blob_id' in local_var_params:
            path_params['blob_id'] = local_var_params['blob_id']

        query_params = []
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))

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

    def list_file_blame_lines_async(self, request):
        r"""获取文件追溯信息

        获取文件追溯信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFileBlameLines
        :type request: :class:`huaweicloudsdkcodehub.v4.ListFileBlameLinesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListFileBlameLinesResponse`
        """
        http_info = self._list_file_blame_lines_http_info(request)
        return self._call_api(**http_info)

    def list_file_blame_lines_async_invoker(self, request):
        http_info = self._list_file_blame_lines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_file_blame_lines_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/blame",
            "request_type": request.__class__.__name__,
            "response_type": "ListFileBlameLinesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))

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

    def list_file_upper_tree_entries_async(self, request):
        r"""获取当前文件上级树结构

        获取当前文件上级树结构
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFileUpperTreeEntries
        :type request: :class:`huaweicloudsdkcodehub.v4.ListFileUpperTreeEntriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListFileUpperTreeEntriesResponse`
        """
        http_info = self._list_file_upper_tree_entries_http_info(request)
        return self._call_api(**http_info)

    def list_file_upper_tree_entries_async_invoker(self, request):
        http_info = self._list_file_upper_tree_entries_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_file_upper_tree_entries_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/upper-files-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ListFileUpperTreeEntriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
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

    def list_files_async(self, request):
        r"""获取指定分支下所有的文件列表

        获取指定分支下所有的文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFiles
        :type request: :class:`huaweicloudsdkcodehub.v4.ListFilesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListFilesResponse`
        """
        http_info = self._list_files_http_info(request)
        return self._call_api(**http_info)

    def list_files_async_invoker(self, request):
        http_info = self._list_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_files_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/file-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListFilesResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_file_async(self, request):
        r"""查看文件属性与内容

        查看文件属性与内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFile
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowFileResponse`
        """
        http_info = self._show_file_http_info(request)
        return self._call_api(**http_info)

    def show_file_async_invoker(self, request):
        http_info = self._show_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/file",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_file_content_async(self, request):
        r"""获取文件内容

        获取文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFileContent
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowFileContentRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowFileContentResponse`
        """
        http_info = self._show_file_content_http_info(request)
        return self._call_api(**http_info)

    def show_file_content_async_invoker(self, request):
        http_info = self._show_file_content_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_file_content_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/file-content",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileContentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))

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

    def show_readme_file_async(self, request):
        r"""获取仓库默认分支的Readme文件内容

        获取仓库默认分支的Readme文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReadmeFile
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowReadmeFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowReadmeFileResponse`
        """
        http_info = self._show_readme_file_http_info(request)
        return self._call_api(**http_info)

    def show_readme_file_async_invoker(self, request):
        http_info = self._show_readme_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_readme_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/readme-file",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReadmeFileResponse"
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

        response_headers = ["X-Total", ]

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

    def update_file_async(self, request):
        r"""更新文件内容

        修改仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFile
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateFileRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateFileResponse`
        """
        http_info = self._update_file_http_info(request)
        return self._call_api(**http_info)

    def update_file_async_invoker(self, request):
        http_info = self._update_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_file_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/repository/file",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))

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

    def batch_delete_repository_file_push_permissions_async(self, request):
        r"""批量删除仓库文件推送权限

        批量删除仓库文件推送权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteRepositoryFilePushPermissions
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchDeleteRepositoryFilePushPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchDeleteRepositoryFilePushPermissionsResponse`
        """
        http_info = self._batch_delete_repository_file_push_permissions_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_repository_file_push_permissions_async_invoker(self, request):
        http_info = self._batch_delete_repository_file_push_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_repository_file_push_permissions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/file-push-permissions/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteRepositoryFilePushPermissionsResponse"
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

    def batch_update_repository_file_push_permissions_async(self, request):
        r"""批量更新仓库文件推送权限

        批量更新仓库文件推送权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateRepositoryFilePushPermissions
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchUpdateRepositoryFilePushPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchUpdateRepositoryFilePushPermissionsResponse`
        """
        http_info = self._batch_update_repository_file_push_permissions_http_info(request)
        return self._call_api(**http_info)

    def batch_update_repository_file_push_permissions_async_invoker(self, request):
        http_info = self._batch_update_repository_file_push_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_repository_file_push_permissions_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/file-push-permissions",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateRepositoryFilePushPermissionsResponse"
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

    def create_file_push_permission_async(self, request):
        r"""创建仓库文件推送权限

        创建仓库文件推送权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFilePushPermission
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateFilePushPermissionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateFilePushPermissionResponse`
        """
        http_info = self._create_file_push_permission_http_info(request)
        return self._call_api(**http_info)

    def create_file_push_permission_async_invoker(self, request):
        http_info = self._create_file_push_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_file_push_permission_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/file-push-permissions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFilePushPermissionResponse"
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

    def list_repository_file_push_permissions_async(self, request):
        r"""获取仓库文件推送权限列表

        获取仓库文件推送权限列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryFilePushPermissions
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryFilePushPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryFilePushPermissionsResponse`
        """
        http_info = self._list_repository_file_push_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_repository_file_push_permissions_async_invoker(self, request):
        http_info = self._list_repository_file_push_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_file_push_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/file-push-permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryFilePushPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
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

    def associate_group_user_group_async(self, request):
        r"""关联代码组与成员组

        关联代码组与成员组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateGroupUserGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.AssociateGroupUserGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AssociateGroupUserGroupResponse`
        """
        http_info = self._associate_group_user_group_http_info(request)
        return self._call_api(**http_info)

    def associate_group_user_group_async_invoker(self, request):
        http_info = self._associate_group_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_group_user_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/groups/{group_id}/user-group/{user_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateGroupUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'user_group_id' in local_var_params:
            path_params['user_group_id'] = local_var_params['user_group_id']

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

    def create_group_async(self, request):
        r"""创建代码组

        创建代码组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateGroupResponse`
        """
        http_info = self._create_group_http_info(request)
        return self._call_api(**http_info)

    def create_group_async_invoker(self, request):
        http_info = self._create_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupResponse"
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

    def delete_group_async(self, request):
        r"""删除代码组

        删除代码组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteGroupResponse`
        """
        http_info = self._delete_group_http_info(request)
        return self._call_api(**http_info)

    def delete_group_async_invoker(self, request):
        http_info = self._delete_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/{project_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupResponse"
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

    def list_group_addable_members_async(self, request):
        r"""获取代码组下可添加的成员列表

        获取代码组下可添加的成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupAddableMembers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupAddableMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupAddableMembersResponse`
        """
        http_info = self._list_group_addable_members_http_info(request)
        return self._call_api(**http_info)

    def list_group_addable_members_async_invoker(self, request):
        http_info = self._list_group_addable_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_addable_members_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/members/addable-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupAddableMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
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

    def list_group_addable_user_groups_async(self, request):
        r"""获取代码组下可添加的成员组

        获取代码组下可添加的成员组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupAddableUserGroups
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupAddableUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupAddableUserGroupsResponse`
        """
        http_info = self._list_group_addable_user_groups_http_info(request)
        return self._call_api(**http_info)

    def list_group_addable_user_groups_async_invoker(self, request):
        http_info = self._list_group_addable_user_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_addable_user_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/user-groups/addable-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupAddableUserGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
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

    def list_group_members_async(self, request):
        r"""获取代码组下可添加的成员列表

        获取代码组下可添加的成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupMembers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupMembersResponse`
        """
        http_info = self._list_group_members_http_info(request)
        return self._call_api(**http_info)

    def list_group_members_async_invoker(self, request):
        http_info = self._list_group_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_members_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/members/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'join_way' in local_var_params:
            query_params.append(('join_way', local_var_params['join_way']))
        if 'access_level' in local_var_params:
            query_params.append(('access_level', local_var_params['access_level']))
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

    def list_group_permission_resources_async(self, request):
        r"""获取代码组权限资源点列表

        获取代码组权限资源点列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupPermissionResources
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupPermissionResourcesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupPermissionResourcesResponse`
        """
        http_info = self._list_group_permission_resources_http_info(request)
        return self._call_api(**http_info)

    def list_group_permission_resources_async_invoker(self, request):
        http_info = self._list_group_permission_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_permission_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/permissions/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupPermissionResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))

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

    def list_group_subgroups_and_repositories_async(self, request):
        r"""获取代码组下的子代码组和仓库列表

        获取代码组下的子代码组和仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupSubgroupsAndRepositories
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupSubgroupsAndRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupSubgroupsAndRepositoriesResponse`
        """
        http_info = self._list_group_subgroups_and_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_group_subgroups_and_repositories_async_invoker(self, request):
        http_info = self._list_group_subgroups_and_repositories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_subgroups_and_repositories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/subgroups-and-repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupSubgroupsAndRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'archived' in local_var_params:
            query_params.append(('archived', local_var_params['archived']))
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

    def list_groups_async(self, request):
        r"""获取代码组列表

        获取代码组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroups
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupsResponse`
        """
        http_info = self._list_groups_http_info(request)
        return self._call_api(**http_info)

    def list_groups_async_invoker(self, request):
        http_info = self._list_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'all_available' in local_var_params:
            query_params.append(('all_available', local_var_params['all_available']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'starred' in local_var_params:
            query_params.append(('starred', local_var_params['starred']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'owned' in local_var_params:
            query_params.append(('owned', local_var_params['owned']))

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

    def list_impersonation_tokens_async(self, request):
        r"""获取用户的个人访问令牌

        获取用户的个人访问令牌
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImpersonationTokens
        :type request: :class:`huaweicloudsdkcodehub.v4.ListImpersonationTokensRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListImpersonationTokensResponse`
        """
        http_info = self._list_impersonation_tokens_http_info(request)
        return self._call_api(**http_info)

    def list_impersonation_tokens_async_invoker(self, request):
        http_info = self._list_impersonation_tokens_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_impersonation_tokens_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/users/impersonation-tokens",
            "request_type": request.__class__.__name__,
            "response_type": "ListImpersonationTokensResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
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

    def list_product_permission_resources_granted_users_async(self, request):
        r"""获取项目下成员列表

        获取项目下成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProductPermissionResourcesGrantedUsers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProductPermissionResourcesGrantedUsersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProductPermissionResourcesGrantedUsersResponse`
        """
        http_info = self._list_product_permission_resources_granted_users_http_info(request)
        return self._call_api(**http_info)

    def list_product_permission_resources_granted_users_async_invoker(self, request):
        http_info = self._list_product_permission_resources_granted_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_product_permission_resources_granted_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListProductPermissionResourcesGrantedUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
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

    def list_project_subgroups_and_repositories_async(self, request):
        r"""获取项目下的代码组和仓库列表

        获取项目下的代码组和仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectSubgroupsAndRepositories
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectSubgroupsAndRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectSubgroupsAndRepositoriesResponse`
        """
        http_info = self._list_project_subgroups_and_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_project_subgroups_and_repositories_async_invoker(self, request):
        http_info = self._list_project_subgroups_and_repositories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_subgroups_and_repositories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/subgroups-and-repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectSubgroupsAndRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'archived' in local_var_params:
            query_params.append(('archived', local_var_params['archived']))
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

    def show_group_async(self, request):
        r"""获取代码组信息

        获取代码组信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupResponse`
        """
        http_info = self._show_group_http_info(request)
        return self._call_api(**http_info)

    def show_group_async_invoker(self, request):
        http_info = self._show_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{project_id}/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupResponse"
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

    def show_group_general_policy_async(self, request):
        r"""获取指定代码组的基本设置信息

        获取指定代码组的基本设置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupGeneralPolicy
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupGeneralPolicyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupGeneralPolicyResponse`
        """
        http_info = self._show_group_general_policy_http_info(request)
        return self._call_api(**http_info)

    def show_group_general_policy_async_invoker(self, request):
        http_info = self._show_group_general_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_general_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/policies/general",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupGeneralPolicyResponse"
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

    def show_group_permission_inherit_enabled_async(self, request):
        r"""获取代码组继承权限设置开关

        获取代码组继承权限设置开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupPermissionInheritEnabled
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupPermissionInheritEnabledRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupPermissionInheritEnabledResponse`
        """
        http_info = self._show_group_permission_inherit_enabled_http_info(request)
        return self._call_api(**http_info)

    def show_group_permission_inherit_enabled_async_invoker(self, request):
        http_info = self._show_group_permission_inherit_enabled_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_permission_inherit_enabled_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/permission-inherit-enabled",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupPermissionInheritEnabledResponse"
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

    def show_group_settings_inherit_cfg_async(self, request):
        r"""获取代码组继承设置项

        获取代码组继承设置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupSettingsInheritCfg
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupSettingsInheritCfgRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupSettingsInheritCfgResponse`
        """
        http_info = self._show_group_settings_inherit_cfg_http_info(request)
        return self._call_api(**http_info)

    def show_group_settings_inherit_cfg_async_invoker(self, request):
        http_info = self._show_group_settings_inherit_cfg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_settings_inherit_cfg_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/settings-inherit-cfg",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupSettingsInheritCfgResponse"
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

    def show_group_watermark_async(self, request):
        r"""获取代码组水印设置

        获取代码组水印设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupWatermark
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupWatermarkRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupWatermarkResponse`
        """
        http_info = self._show_group_watermark_http_info(request)
        return self._call_api(**http_info)

    def show_group_watermark_async_invoker(self, request):
        http_info = self._show_group_watermark_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_watermark_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupWatermarkResponse"
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

    def show_groups_inherit_async(self, request):
        r"""获取代码组的继承设置

        获取代码组的继承设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupsInherit
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupsInheritRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupsInheritResponse`
        """
        http_info = self._show_groups_inherit_http_info(request)
        return self._call_api(**http_info)

    def show_groups_inherit_async_invoker(self, request):
        http_info = self._show_groups_inherit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_groups_inherit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/inherit",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupsInheritResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'setting_type' in local_var_params:
            query_params.append(('setting_type', local_var_params['setting_type']))

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

    def show_project_general_policy_async(self, request):
        r"""获取指定项目的基本设置信息

        获取指定项目的基本设置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectGeneralPolicy
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectGeneralPolicyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectGeneralPolicyResponse`
        """
        http_info = self._show_project_general_policy_http_info(request)
        return self._call_api(**http_info)

    def show_project_general_policy_async_invoker(self, request):
        http_info = self._show_project_general_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_general_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/policies/general",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectGeneralPolicyResponse"
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

    def show_project_member_setting_async(self, request):
        r"""获取项目成员设置

        获取项目成员设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectMemberSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectMemberSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectMemberSettingResponse`
        """
        http_info = self._show_project_member_setting_http_info(request)
        return self._call_api(**http_info)

    def show_project_member_setting_async_invoker(self, request):
        http_info = self._show_project_member_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_member_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/member-setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectMemberSettingResponse"
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

    def show_resource_permissions_async(self, request):
        r"""获取资源点对应的角色和权限

        获取资源点对应的角色和权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowResourcePermissions
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowResourcePermissionsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowResourcePermissionsResponse`
        """
        http_info = self._show_resource_permissions_http_info(request)
        return self._call_api(**http_info)

    def show_resource_permissions_async_invoker(self, request):
        http_info = self._show_resource_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_resource_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/permissions-resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourcePermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def transfer_group_async(self, request):
        r"""移交代码组

        移交代码组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for TransferGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.TransferGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.TransferGroupResponse`
        """
        http_info = self._transfer_group_http_info(request)
        return self._call_api(**http_info)

    def transfer_group_async_invoker(self, request):
        http_info = self._transfer_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _transfer_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/groups/{group_id}/transfer",
            "request_type": request.__class__.__name__,
            "response_type": "TransferGroupResponse"
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

    def update_group_watermark_async(self, request):
        r"""更新代码组水印设置

        更新代码组水印设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroupWatermark
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateGroupWatermarkRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateGroupWatermarkResponse`
        """
        http_info = self._update_group_watermark_http_info(request)
        return self._call_api(**http_info)

    def update_group_watermark_async_invoker(self, request):
        http_info = self._update_group_watermark_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_watermark_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/groups/{group_id}/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupWatermarkResponse"
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

    def create_repository_label_async(self, request):
        r"""创建仓库标签

        创建仓库标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRepositoryLabel
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateRepositoryLabelRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateRepositoryLabelResponse`
        """
        http_info = self._create_repository_label_http_info(request)
        return self._call_api(**http_info)

    def create_repository_label_async_invoker(self, request):
        http_info = self._create_repository_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_repository_label_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepositoryLabelResponse"
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

    def create_repository_system_labels_async(self, request):
        r"""创建仓库系统标签

        创建仓库系统标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRepositorySystemLabels
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateRepositorySystemLabelsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateRepositorySystemLabelsResponse`
        """
        http_info = self._create_repository_system_labels_http_info(request)
        return self._call_api(**http_info)

    def create_repository_system_labels_async_invoker(self, request):
        http_info = self._create_repository_system_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_repository_system_labels_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/system-labels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepositorySystemLabelsResponse"
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

    def delete_repository_label_async(self, request):
        r"""删除仓库标签

        删除仓库标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRepositoryLabel
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteRepositoryLabelRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteRepositoryLabelResponse`
        """
        http_info = self._delete_repository_label_http_info(request)
        return self._call_api(**http_info)

    def delete_repository_label_async_invoker(self, request):
        http_info = self._delete_repository_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_repository_label_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/label",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepositoryLabelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
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

    def list_repository_labels_async(self, request):
        r"""获取仓库标签列表

        获取仓库标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryLabels
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryLabelsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryLabelsResponse`
        """
        http_info = self._list_repository_labels_http_info(request)
        return self._call_api(**http_info)

    def list_repository_labels_async_invoker(self, request):
        http_info = self._list_repository_labels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_labels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/labels",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryLabelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'include_expired' in local_var_params:
            query_params.append(('include_expired', local_var_params['include_expired']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))

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

    def update_repository_label_async(self, request):
        r"""修改仓库标签

        修改仓库标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepositoryLabel
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryLabelRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryLabelResponse`
        """
        http_info = self._update_repository_label_http_info(request)
        return self._call_api(**http_info)

    def update_repository_label_async_invoker(self, request):
        http_info = self._update_repository_label_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_repository_label_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/label",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepositoryLabelResponse"
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

    def add_repository_members_async(self, request):
        r"""批量添加仓库成员

        批量添加仓库成员
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRepositoryMembers
        :type request: :class:`huaweicloudsdkcodehub.v4.AddRepositoryMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddRepositoryMembersResponse`
        """
        http_info = self._add_repository_members_http_info(request)
        return self._call_api(**http_info)

    def add_repository_members_async_invoker(self, request):
        http_info = self._add_repository_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_repository_members_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "AddRepositoryMembersResponse"
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

    def list_members_async(self, request):
        r"""获取仓库成员列表

        获取仓库成员列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMembers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMembersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMembersResponse`
        """
        http_info = self._list_members_http_info(request)
        return self._call_api(**http_info)

    def list_members_async_invoker(self, request):
        http_info = self._list_members_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_members_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/members",
            "request_type": request.__class__.__name__,
            "response_type": "ListMembersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'permission' in local_var_params:
            query_params.append(('permission', local_var_params['permission']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_repository_user_groups_async(self, request):
        r"""获取成员组列表

        获取成员组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryUserGroups
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryUserGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryUserGroupsResponse`
        """
        http_info = self._list_repository_user_groups_http_info(request)
        return self._call_api(**http_info)

    def list_repository_user_groups_async_invoker(self, request):
        http_info = self._list_repository_user_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_user_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/user-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryUserGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def approval_merge_request_async(self, request):
        r"""审核合并请求

        审核合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApprovalMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v4.ApprovalMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ApprovalMergeRequestResponse`
        """
        http_info = self._approval_merge_request_http_info(request)
        return self._call_api(**http_info)

    def approval_merge_request_async_invoker(self, request):
        http_info = self._approval_merge_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _approval_merge_request_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/approval",
            "request_type": request.__class__.__name__,
            "response_type": "ApprovalMergeRequestResponse"
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

    def create_group_merge_request_approver_setting_async(self, request):
        r"""创建代码组合并请求审核设置

        创建代码组合并请求审核设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGroupMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateGroupMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateGroupMergeRequestApproverSettingResponse`
        """
        http_info = self._create_group_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def create_group_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._create_group_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_group_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/groups/{group_id}/approver-settings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupMergeRequestApproverSettingResponse"
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

    def create_merge_request_async(self, request):
        r"""创建合并请求

        创建合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestResponse`
        """
        http_info = self._create_merge_request_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_async_invoker(self, request):
        http_info = self._create_merge_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_merge_request_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeRequestResponse"
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

    def create_merge_request_approver_setting_async(self, request):
        r"""创建合并请求审核设置

        创建合并请求审核设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestApproverSettingResponse`
        """
        http_info = self._create_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._create_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/approver-settings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeRequestApproverSettingResponse"
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

    def create_merge_request_template_async(self, request):
        r"""创建合并请求模板

        创建合并请求模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMergeRequestTemplate
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateMergeRequestTemplateResponse`
        """
        http_info = self._create_merge_request_template_http_info(request)
        return self._call_api(**http_info)

    def create_merge_request_template_async_invoker(self, request):
        http_info = self._create_merge_request_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_merge_request_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeRequestTemplateResponse"
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

    def create_project_merge_request_approver_setting_async(self, request):
        r"""创建项目合并请求审核设置

        创建项目合并请求审核设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProjectMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateProjectMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateProjectMergeRequestApproverSettingResponse`
        """
        http_info = self._create_project_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def create_project_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._create_project_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_project_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/approver-settings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectMergeRequestApproverSettingResponse"
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

    def delete_group_merge_request_approver_setting_async(self, request):
        r"""删除代码组合并请求审核配置

        删除代码组合并请求审核配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGroupMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteGroupMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteGroupMergeRequestApproverSettingResponse`
        """
        http_info = self._delete_group_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def delete_group_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._delete_group_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_group_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/groups/{group_id}/approver-settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupMergeRequestApproverSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def delete_merge_request_approver_setting_async(self, request):
        r"""删除合并请求审核配置

        删除合并请求审核配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteMergeRequestApproverSettingResponse`
        """
        http_info = self._delete_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def delete_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._delete_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/approver-settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMergeRequestApproverSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def delete_merge_request_template_async(self, request):
        r"""删除合并请求模板

        删除合并请求模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMergeRequestTemplate
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteMergeRequestTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteMergeRequestTemplateResponse`
        """
        http_info = self._delete_merge_request_template_http_info(request)
        return self._call_api(**http_info)

    def delete_merge_request_template_async_invoker(self, request):
        http_info = self._delete_merge_request_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_merge_request_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMergeRequestTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def delete_merge_request_vote_async(self, request):
        r"""删除合并请求打分

        删除合并请求打分
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMergeRequestVote
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteMergeRequestVoteRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteMergeRequestVoteResponse`
        """
        http_info = self._delete_merge_request_vote_http_info(request)
        return self._call_api(**http_info)

    def delete_merge_request_vote_async_invoker(self, request):
        http_info = self._delete_merge_request_vote_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_merge_request_vote_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/vote",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMergeRequestVoteResponse"
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

    def delete_project_merge_request_approver_setting_async(self, request):
        r"""删除项目合并请求审核配置

        删除项目合并请求审核配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProjectMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteProjectMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteProjectMergeRequestApproverSettingResponse`
        """
        http_info = self._delete_project_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def delete_project_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._delete_project_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_project_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/approver-settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProjectMergeRequestApproverSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def import_merge_request_async(self, request):
        r"""导入合并请求

        导入合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v4.ImportMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ImportMergeRequestResponse`
        """
        http_info = self._import_merge_request_http_info(request)
        return self._call_api(**http_info)

    def import_merge_request_async_invoker(self, request):
        http_info = self._import_merge_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_merge_request_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/import-merge-requests",
            "request_type": request.__class__.__name__,
            "response_type": "ImportMergeRequestResponse"
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

    def list_discussion_templates_async(self, request):
        r"""获取检视意见模板列表

        获取检视意见模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiscussionTemplates
        :type request: :class:`huaweicloudsdkcodehub.v4.ListDiscussionTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListDiscussionTemplatesResponse`
        """
        http_info = self._list_discussion_templates_http_info(request)
        return self._call_api(**http_info)

    def list_discussion_templates_async_invoker(self, request):
        http_info = self._list_discussion_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_discussion_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/discussion/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiscussionTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'is_default' in local_var_params:
            query_params.append(('is_default', local_var_params['is_default']))
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

    def list_group_merge_request_approver_settings_async(self, request):
        r"""获取代码组合并请求审核设置列表

        获取代码组合并请求审核设置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupMergeRequestApproverSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupMergeRequestApproverSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupMergeRequestApproverSettingsResponse`
        """
        http_info = self._list_group_merge_request_approver_settings_http_info(request)
        return self._call_api(**http_info)

    def list_group_merge_request_approver_settings_async_invoker(self, request):
        http_info = self._list_group_merge_request_approver_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_merge_request_approver_settings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/approver-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupMergeRequestApproverSettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_group_merge_request_can_be_assigned_reviewers_async(self, request):
        r"""获取代码组检视人

        获取代码组检视人
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupMergeRequestCanBeAssignedReviewers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupMergeRequestCanBeAssignedReviewersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupMergeRequestCanBeAssignedReviewersResponse`
        """
        http_info = self._list_group_merge_request_can_be_assigned_reviewers_http_info(request)
        return self._call_api(**http_info)

    def list_group_merge_request_can_be_assigned_reviewers_async_invoker(self, request):
        http_info = self._list_group_merge_request_can_be_assigned_reviewers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_merge_request_can_be_assigned_reviewers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/merge-requests/reviewers",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupMergeRequestCanBeAssignedReviewersResponse"
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

    def list_group_merge_request_valid_assigned_candidates_async(self, request):
        r"""获取代码组审核人或合并人

        获取代码组审核人或合并人
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupMergeRequestValidAssignedCandidates
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupMergeRequestValidAssignedCandidatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupMergeRequestValidAssignedCandidatesResponse`
        """
        http_info = self._list_group_merge_request_valid_assigned_candidates_http_info(request)
        return self._call_api(**http_info)

    def list_group_merge_request_valid_assigned_candidates_async_invoker(self, request):
        http_info = self._list_group_merge_request_valid_assigned_candidates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_merge_request_valid_assigned_candidates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/merge-requests/assignee-candidates",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupMergeRequestValidAssignedCandidatesResponse"
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

    def list_merge_request_approver_settings_async(self, request):
        r"""获取合并请求审核设置列表

        获取合并请求审核设置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestApproverSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestApproverSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestApproverSettingsResponse`
        """
        http_info = self._list_merge_request_approver_settings_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_approver_settings_async_invoker(self, request):
        http_info = self._list_merge_request_approver_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_approver_settings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/approver-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestApproverSettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'target_type' in local_var_params:
            query_params.append(('target_type', local_var_params['target_type']))
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

    def list_merge_request_approvers_async(self, request):
        r"""获取合并请求审核人列表

        获取合并请求审核人列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestApprovers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestApproversRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestApproversResponse`
        """
        http_info = self._list_merge_request_approvers_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_approvers_async_invoker(self, request):
        http_info = self._list_merge_request_approvers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_approvers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/approval-approvers",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestApproversResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))
        if 'source_branch' in local_var_params:
            query_params.append(('source_branch', local_var_params['source_branch']))
        if 'merge_request_iid' in local_var_params:
            query_params.append(('merge_request_iid', local_var_params['merge_request_iid']))
        if 'target_repository_id' in local_var_params:
            query_params.append(('target_repository_id', local_var_params['target_repository_id']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_merge_request_changes_async(self, request):
        r"""获取合并请求文件变更列表

        获取合并请求文件变更列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestChanges
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestChangesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestChangesResponse`
        """
        http_info = self._list_merge_request_changes_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_changes_async_invoker(self, request):
        http_info = self._list_merge_request_changes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_changes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/changes",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestChangesResponse"
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
        if 'ignore_whitespace_change' in local_var_params:
            query_params.append(('ignore_whitespace_change', local_var_params['ignore_whitespace_change']))
        if 'force_encode' in local_var_params:
            query_params.append(('force_encode', local_var_params['force_encode']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'from_diff_id' in local_var_params:
            query_params.append(('from_diff_id', local_var_params['from_diff_id']))
        if 'to_diff_id' in local_var_params:
            query_params.append(('to_diff_id', local_var_params['to_diff_id']))
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

    def list_merge_request_changes_trees_async(self, request):
        r"""获取合并请求文件变更列表树

        获取合并请求文件变更列表树
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestChangesTrees
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestChangesTreesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestChangesTreesResponse`
        """
        http_info = self._list_merge_request_changes_trees_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_changes_trees_async_invoker(self, request):
        http_info = self._list_merge_request_changes_trees_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_changes_trees_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/changes-trees",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestChangesTreesResponse"
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
        if 'approval_user_id' in local_var_params:
            query_params.append(('approval_user_id', local_var_params['approval_user_id']))
        if 'commit_id' in local_var_params:
            query_params.append(('commit_id', local_var_params['commit_id']))
        if 'from_diff_id' in local_var_params:
            query_params.append(('from_diff_id', local_var_params['from_diff_id']))
        if 'to_diff_id' in local_var_params:
            query_params.append(('to_diff_id', local_var_params['to_diff_id']))
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

    def list_merge_request_commits_async(self, request):
        r"""获取合并请求commit列表

        获取合并请求commit列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestCommits
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestCommitsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestCommitsResponse`
        """
        http_info = self._list_merge_request_commits_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_commits_async_invoker(self, request):
        http_info = self._list_merge_request_commits_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_commits_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/commits",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestCommitsResponse"
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

    def list_merge_request_conflict_files_async(self, request):
        r"""获取所有的冲突文件

        获取所有的冲突文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestConflictFiles
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestConflictFilesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestConflictFilesResponse`
        """
        http_info = self._list_merge_request_conflict_files_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_conflict_files_async_invoker(self, request):
        http_info = self._list_merge_request_conflict_files_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_conflict_files_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/conflict-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestConflictFilesResponse"
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'hide_content' in local_var_params:
            query_params.append(('hide_content', local_var_params['hide_content']))

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

    def list_merge_request_reviewers_async(self, request):
        r"""获取合并请求检视人列表

        获取合并请求检视人列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestReviewers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestReviewersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestReviewersResponse`
        """
        http_info = self._list_merge_request_reviewers_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_reviewers_async_invoker(self, request):
        http_info = self._list_merge_request_reviewers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_reviewers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/approval-reviewers",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestReviewersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))
        if 'source_branch' in local_var_params:
            query_params.append(('source_branch', local_var_params['source_branch']))
        if 'merge_request_iid' in local_var_params:
            query_params.append(('merge_request_iid', local_var_params['merge_request_iid']))
        if 'target_repository_id' in local_var_params:
            query_params.append(('target_repository_id', local_var_params['target_repository_id']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_merge_request_templates_async(self, request):
        r"""获取合并请求模板列表

        获取合并请求模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestTemplates
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestTemplatesResponse`
        """
        http_info = self._list_merge_request_templates_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_templates_async_invoker(self, request):
        http_info = self._list_merge_request_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'template_name' in local_var_params:
            query_params.append(('template_name', local_var_params['template_name']))
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

    def list_merge_request_valid_assigned_candidates_async(self, request):
        r"""获取可选的合并请求检视人

        获取可选的合并请求检视人
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestValidAssignedCandidates
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestValidAssignedCandidatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestValidAssignedCandidatesResponse`
        """
        http_info = self._list_merge_request_valid_assigned_candidates_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_valid_assigned_candidates_async_invoker(self, request):
        http_info = self._list_merge_request_valid_assigned_candidates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_valid_assigned_candidates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/assignee-candidates",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestValidAssignedCandidatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))
        if 'merge_request_iid' in local_var_params:
            query_params.append(('merge_request_iid', local_var_params['merge_request_iid']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'search_by_name_list' in local_var_params:
            query_params.append(('search_by_name_list', local_var_params['search_by_name_list']))
        if 'target_project_id' in local_var_params:
            query_params.append(('target_project_id', local_var_params['target_project_id']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
        if 'only_developers' in local_var_params:
            query_params.append(('only_developers', local_var_params['only_developers']))

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

    def list_project_merge_request_approver_settings_async(self, request):
        r"""获取项目合并请求审核设置列表

        获取项目合并请求审核设置列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectMergeRequestApproverSettings
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectMergeRequestApproverSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectMergeRequestApproverSettingsResponse`
        """
        http_info = self._list_project_merge_request_approver_settings_http_info(request)
        return self._call_api(**http_info)

    def list_project_merge_request_approver_settings_async_invoker(self, request):
        http_info = self._list_project_merge_request_approver_settings_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_merge_request_approver_settings_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/approver-settings",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectMergeRequestApproverSettingsResponse"
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

    def list_project_merge_request_can_be_assigned_reviewers_async(self, request):
        r"""获取项目检视人

        获取代码组检视人
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectMergeRequestCanBeAssignedReviewers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectMergeRequestCanBeAssignedReviewersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectMergeRequestCanBeAssignedReviewersResponse`
        """
        http_info = self._list_project_merge_request_can_be_assigned_reviewers_http_info(request)
        return self._call_api(**http_info)

    def list_project_merge_request_can_be_assigned_reviewers_async_invoker(self, request):
        http_info = self._list_project_merge_request_can_be_assigned_reviewers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_merge_request_can_be_assigned_reviewers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/merge-requests/reviewers",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectMergeRequestCanBeAssignedReviewersResponse"
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

    def list_project_merge_request_can_be_assigned_users_async(self, request):
        r"""获取项目审核人或合并人

        获取代码组审核人或合并人
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectMergeRequestCanBeAssignedUsers
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectMergeRequestCanBeAssignedUsersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectMergeRequestCanBeAssignedUsersResponse`
        """
        http_info = self._list_project_merge_request_can_be_assigned_users_http_info(request)
        return self._call_api(**http_info)

    def list_project_merge_request_can_be_assigned_users_async_invoker(self, request):
        http_info = self._list_project_merge_request_can_be_assigned_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_merge_request_can_be_assigned_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/merge-requests/assignee-candidates",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectMergeRequestCanBeAssignedUsersResponse"
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

    def list_repository_merge_requests_async(self, request):
        r"""获取仓库MR列表

        获取仓库MR列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryMergeRequests
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryMergeRequestsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryMergeRequestsResponse`
        """
        http_info = self._list_repository_merge_requests_http_info(request)
        return self._call_api(**http_info)

    def list_repository_merge_requests_async_invoker(self, request):
        http_info = self._list_repository_merge_requests_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_merge_requests_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryMergeRequestsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'author_id' in local_var_params:
            query_params.append(('author_id', local_var_params['author_id']))
        if 'source_branch' in local_var_params:
            query_params.append(('source_branch', local_var_params['source_branch']))
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'source_repository_id' in local_var_params:
            query_params.append(('source_repository_id', local_var_params['source_repository_id']))
        if 'only_count' in local_var_params:
            query_params.append(('only_count', local_var_params['only_count']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))

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

    def merge_merge_request_async(self, request):
        r"""合入合并请求

        合入合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MergeMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v4.MergeMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.MergeMergeRequestResponse`
        """
        http_info = self._merge_merge_request_http_info(request)
        return self._call_api(**http_info)

    def merge_merge_request_async_invoker(self, request):
        http_info = self._merge_merge_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _merge_merge_request_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/merge",
            "request_type": request.__class__.__name__,
            "response_type": "MergeMergeRequestResponse"
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

    def rebase_merge_request_for_open_api_async(self, request):
        r"""变基合并请求

        变基合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RebaseMergeRequestForOpenApi
        :type request: :class:`huaweicloudsdkcodehub.v4.RebaseMergeRequestForOpenApiRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.RebaseMergeRequestForOpenApiResponse`
        """
        http_info = self._rebase_merge_request_for_open_api_http_info(request)
        return self._call_api(**http_info)

    def rebase_merge_request_for_open_api_async_invoker(self, request):
        http_info = self._rebase_merge_request_for_open_api_http_info(request)
        return AsyncInvoker(self, http_info)

    def _rebase_merge_request_for_open_api_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/rebase",
            "request_type": request.__class__.__name__,
            "response_type": "RebaseMergeRequestForOpenApiResponse"
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

    def resolve_merge_request_conflicts_async(self, request):
        r"""在线解决合并请求冲突

        在线解决合并请求冲突
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResolveMergeRequestConflicts
        :type request: :class:`huaweicloudsdkcodehub.v4.ResolveMergeRequestConflictsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ResolveMergeRequestConflictsResponse`
        """
        http_info = self._resolve_merge_request_conflicts_http_info(request)
        return self._call_api(**http_info)

    def resolve_merge_request_conflicts_async_invoker(self, request):
        http_info = self._resolve_merge_request_conflicts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resolve_merge_request_conflicts_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/resolve-conflicts",
            "request_type": request.__class__.__name__,
            "response_type": "ResolveMergeRequestConflictsResponse"
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

    def review_merge_request_async(self, request):
        r"""检视合并请求

        检视合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ReviewMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v4.ReviewMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ReviewMergeRequestResponse`
        """
        http_info = self._review_merge_request_http_info(request)
        return self._call_api(**http_info)

    def review_merge_request_async_invoker(self, request):
        http_info = self._review_merge_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _review_merge_request_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/approval-review",
            "request_type": request.__class__.__name__,
            "response_type": "ReviewMergeRequestResponse"
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

    def show_actual_head_pipeline_async(self, request):
        r"""获取合并请求关联的最新流水线

        获取合并请求关联的最新流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowActualHeadPipeline
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowActualHeadPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowActualHeadPipelineResponse`
        """
        http_info = self._show_actual_head_pipeline_http_info(request)
        return self._call_api(**http_info)

    def show_actual_head_pipeline_async_invoker(self, request):
        http_info = self._show_actual_head_pipeline_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_actual_head_pipeline_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/actual-head-pipeline",
            "request_type": request.__class__.__name__,
            "response_type": "ShowActualHeadPipelineResponse"
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

    def show_average_evaluation_async(self, request):
        r"""获取合并请求的平均评价

        获取合并请求的平均评价
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAverageEvaluation
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowAverageEvaluationRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowAverageEvaluationResponse`
        """
        http_info = self._show_average_evaluation_http_info(request)
        return self._call_api(**http_info)

    def show_average_evaluation_async_invoker(self, request):
        http_info = self._show_average_evaluation_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_average_evaluation_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/average-evaluation",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAverageEvaluationResponse"
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

    def show_branch_conflict_async(self, request):
        r"""获取分支代码冲突

        获取分支代码冲突
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBranchConflict
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowBranchConflictRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowBranchConflictResponse`
        """
        http_info = self._show_branch_conflict_http_info(request)
        return self._call_api(**http_info)

    def show_branch_conflict_async_invoker(self, request):
        http_info = self._show_branch_conflict_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_branch_conflict_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/conflict",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBranchConflictResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'source_repository_id' in local_var_params:
            query_params.append(('source_repository_id', local_var_params['source_repository_id']))
        if 'source_branch' in local_var_params:
            query_params.append(('source_branch', local_var_params['source_branch']))
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))
        if 'target_repository_id' in local_var_params:
            query_params.append(('target_repository_id', local_var_params['target_repository_id']))

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

    def show_group_merge_request_setting_async(self, request):
        r"""获取代码组合并请求设置

        获取代码组合并请求设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupMergeRequestSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupMergeRequestSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupMergeRequestSettingResponse`
        """
        http_info = self._show_group_merge_request_setting_http_info(request)
        return self._call_api(**http_info)

    def show_group_merge_request_setting_async_invoker(self, request):
        http_info = self._show_group_merge_request_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_merge_request_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/merge-requests/setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupMergeRequestSettingResponse"
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

    def show_merge_request_comments_by_line_async(self, request):
        r"""获取合并请求文件变更页单个文件下的检视意见

        获取合并请求文件变更页单个文件下的检视意见
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeRequestCommentsByLine
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestCommentsByLineRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestCommentsByLineResponse`
        """
        http_info = self._show_merge_request_comments_by_line_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_comments_by_line_async_invoker(self, request):
        http_info = self._show_merge_request_comments_by_line_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_merge_request_comments_by_line_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/comments-by-line",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestCommentsByLineResponse"
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
        if 'line' in local_var_params:
            query_params.append(('line', local_var_params['line']))
        if 'with_commit_comments' in local_var_params:
            query_params.append(('with_commit_comments', local_var_params['with_commit_comments']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'base_sha' in local_var_params:
            query_params.append(('base_sha', local_var_params['base_sha']))
        if 'start_sha' in local_var_params:
            query_params.append(('start_sha', local_var_params['start_sha']))
        if 'head_sha' in local_var_params:
            query_params.append(('head_sha', local_var_params['head_sha']))

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

    def show_merge_request_detail_async(self, request):
        r"""获取MR详情

        获取MR详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeRequestDetail
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestDetailRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestDetailResponse`
        """
        http_info = self._show_merge_request_detail_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_detail_async_invoker(self, request):
        http_info = self._show_merge_request_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_merge_request_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestDetailResponse"
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

    def show_merge_request_setting_async(self, request):
        r"""获取仓库合并请求设置

        获取仓库合并请求设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeRequestSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestSettingResponse`
        """
        http_info = self._show_merge_request_setting_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_setting_async_invoker(self, request):
        http_info = self._show_merge_request_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_merge_request_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestSettingResponse"
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

    def show_merge_request_template_async(self, request):
        r"""获取单个合并请求模板

        获取单个合并请求模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeRequestTemplate
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestTemplateResponse`
        """
        http_info = self._show_merge_request_template_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_template_async_invoker(self, request):
        http_info = self._show_merge_request_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_merge_request_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def show_merge_request_votes_detail_async(self, request):
        r"""获取合并请求打分

        获取合并请求打分
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeRequestVotesDetail
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestVotesDetailRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeRequestVotesDetailResponse`
        """
        http_info = self._show_merge_request_votes_detail_http_info(request)
        return self._call_api(**http_info)

    def show_merge_request_votes_detail_async_invoker(self, request):
        http_info = self._show_merge_request_votes_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_merge_request_votes_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/votes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeRequestVotesDetailResponse"
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

    def show_mergeable_state_outer_async(self, request):
        r"""获取合并请求的可合入状态。

        获取合并请求的可合入状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMergeableStateOuter
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowMergeableStateOuterRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowMergeableStateOuterResponse`
        """
        http_info = self._show_mergeable_state_outer_http_info(request)
        return self._call_api(**http_info)

    def show_mergeable_state_outer_async_invoker(self, request):
        http_info = self._show_mergeable_state_outer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_mergeable_state_outer_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/mergeable-state-out",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeableStateOuterResponse"
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

    def show_project_merge_request_setting_async(self, request):
        r"""获取项目合并请求设置

        获取项目合并请求设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectMergeRequestSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectMergeRequestSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectMergeRequestSettingResponse`
        """
        http_info = self._show_project_merge_request_setting_http_info(request)
        return self._call_api(**http_info)

    def show_project_merge_request_setting_async_invoker(self, request):
        http_info = self._show_project_merge_request_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_merge_request_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/merge-requests/setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectMergeRequestSettingResponse"
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

    def update_group_merge_request_approver_setting_async(self, request):
        r"""更新代码组合并请求审核设置

        更新代码组合并请求审核设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroupMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateGroupMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateGroupMergeRequestApproverSettingResponse`
        """
        http_info = self._update_group_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def update_group_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._update_group_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/groups/{group_id}/approver-settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupMergeRequestApproverSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def update_merge_request_async(self, request):
        r"""更新合并请求

        更新合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequest
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestResponse`
        """
        http_info = self._update_merge_request_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_async_invoker(self, request):
        http_info = self._update_merge_request_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestResponse"
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

    def update_merge_request_approver_setting_async(self, request):
        r"""更新合并请求审核设置

        更新合并请求审核设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestApproverSettingResponse`
        """
        http_info = self._update_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._update_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/approver-settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestApproverSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def update_merge_request_approvers_async(self, request):
        r"""更新合并请求的审核人列表

        更新合并请求的审核人列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestApprovers
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestApproversRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestApproversResponse`
        """
        http_info = self._update_merge_request_approvers_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_approvers_async_invoker(self, request):
        http_info = self._update_merge_request_approvers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_approvers_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/approval-approvers",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestApproversResponse"
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

    def update_merge_request_reviewers_async(self, request):
        r"""更新合并请求的检视人列表

        更新合并请求的检视人列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestReviewers
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestReviewersRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestReviewersResponse`
        """
        http_info = self._update_merge_request_reviewers_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_reviewers_async_invoker(self, request):
        http_info = self._update_merge_request_reviewers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_reviewers_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/approval-reviewers",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestReviewersResponse"
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

    def update_merge_request_setting_async(self, request):
        r"""更新仓库合并请求设置

        更新仓库合并请求设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestSettingResponse`
        """
        http_info = self._update_merge_request_setting_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_setting_async_invoker(self, request):
        http_info = self._update_merge_request_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/setting",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestSettingResponse"
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

    def update_merge_request_template_async(self, request):
        r"""更新合并请求模板

        更新合并请求模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestTemplate
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestTemplateResponse`
        """
        http_info = self._update_merge_request_template_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_template_async_invoker(self, request):
        http_info = self._update_merge_request_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/template/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def update_merge_request_vote_async(self, request):
        r"""更新合并请求打分

        更新合并请求打分
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMergeRequestVote
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestVoteRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateMergeRequestVoteResponse`
        """
        http_info = self._update_merge_request_vote_http_info(request)
        return self._call_api(**http_info)

    def update_merge_request_vote_async_invoker(self, request):
        http_info = self._update_merge_request_vote_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_merge_request_vote_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/vote",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMergeRequestVoteResponse"
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

    def update_project_merge_request_approver_setting_async(self, request):
        r"""更新项目合并请求审核设置

        更新项目合并请求审核设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectMergeRequestApproverSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProjectMergeRequestApproverSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProjectMergeRequestApproverSettingResponse`
        """
        http_info = self._update_project_merge_request_approver_setting_http_info(request)
        return self._call_api(**http_info)

    def update_project_merge_request_approver_setting_async_invoker(self, request):
        http_info = self._update_project_merge_request_approver_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_merge_request_approver_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/approver-settings/{setting_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectMergeRequestApproverSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'setting_id' in local_var_params:
            path_params['setting_id'] = local_var_params['setting_id']

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

    def list_commit_associated_merge_requests_async(self, request):
        r"""获取提交关联的合并请求

        获取提交关联的合并请求
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCommitAssociatedMergeRequests
        :type request: :class:`huaweicloudsdkcodehub.v4.ListCommitAssociatedMergeRequestsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListCommitAssociatedMergeRequestsResponse`
        """
        http_info = self._list_commit_associated_merge_requests_http_info(request)
        return self._call_api(**http_info)

    def list_commit_associated_merge_requests_async_invoker(self, request):
        http_info = self._list_commit_associated_merge_requests_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_commit_associated_merge_requests_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/commits/{sha}/merge-requests",
            "request_type": request.__class__.__name__,
            "response_type": "ListCommitAssociatedMergeRequestsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'sha' in local_var_params:
            path_params['sha'] = local_var_params['sha']

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

    def show_repository_merge_requests_statistic_async(self, request):
        r"""获取仓库合并请求统计数据

        获取仓库合并请求统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryMergeRequestsStatistic
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryMergeRequestsStatisticRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryMergeRequestsStatisticResponse`
        """
        http_info = self._show_repository_merge_requests_statistic_http_info(request)
        return self._call_api(**http_info)

    def show_repository_merge_requests_statistic_async_invoker(self, request):
        http_info = self._show_repository_merge_requests_statistic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_merge_requests_statistic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryMergeRequestsStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'iids' in local_var_params:
            query_params.append(('iids', local_var_params['iids']))
        if 'fields' in local_var_params:
            query_params.append(('fields', local_var_params['fields']))

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

    def list_merge_request_participants_async(self, request):
        r"""获取合并请求参与者

        获取合并请求参与者
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMergeRequestParticipants
        :type request: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestParticipantsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListMergeRequestParticipantsResponse`
        """
        http_info = self._list_merge_request_participants_http_info(request)
        return self._call_api(**http_info)

    def list_merge_request_participants_async_invoker(self, request):
        http_info = self._list_merge_request_participants_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_merge_request_participants_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/merge-requests/{merge_request_iid}/participants",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeRequestParticipantsResponse"
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

    def show_repository_permission_inherit_enabled_async(self, request):
        r"""查询仓库权限配置信息

        查询仓库权限配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryPermissionInheritEnabled
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryPermissionInheritEnabledRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryPermissionInheritEnabledResponse`
        """
        http_info = self._show_repository_permission_inherit_enabled_http_info(request)
        return self._call_api(**http_info)

    def show_repository_permission_inherit_enabled_async_invoker(self, request):
        http_info = self._show_repository_permission_inherit_enabled_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_permission_inherit_enabled_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/permission-inherit-setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryPermissionInheritEnabledResponse"
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

    def update_repository_permission_inherit_enabled_async(self, request):
        r"""更新仓库权限继承配置

        更新仓库权限继承配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepositoryPermissionInheritEnabled
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryPermissionInheritEnabledRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryPermissionInheritEnabledResponse`
        """
        http_info = self._update_repository_permission_inherit_enabled_http_info(request)
        return self._call_api(**http_info)

    def update_repository_permission_inherit_enabled_async_invoker(self, request):
        http_info = self._update_repository_permission_inherit_enabled_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_repository_permission_inherit_enabled_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/permission-inherit-setting",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepositoryPermissionInheritEnabledResponse"
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

    def list_latest_pipeline_jobs_async(self, request):
        r"""获取流水线的关联的最新任务

        获取流水线的关联的最新任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLatestPipelineJobs
        :type request: :class:`huaweicloudsdkcodehub.v4.ListLatestPipelineJobsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListLatestPipelineJobsResponse`
        """
        http_info = self._list_latest_pipeline_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_latest_pipeline_jobs_async_invoker(self, request):
        http_info = self._list_latest_pipeline_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_latest_pipeline_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/pipelines/{pipeline_id}/latest-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLatestPipelineJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def list_pipeline_jobs_async(self, request):
        r"""获取流水线的关联的任务列表

        获取流水线的关联的任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipelineJobs
        :type request: :class:`huaweicloudsdkcodehub.v4.ListPipelineJobsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListPipelineJobsResponse`
        """
        http_info = self._list_pipeline_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_pipeline_jobs_async_invoker(self, request):
        http_info = self._list_pipeline_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pipeline_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/pipelines/{pipeline_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelineJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

        response_headers = ["X-Total", ]

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

    def show_project_settings_inherit_cfg_async(self, request):
        r"""获取项目继承设置项

        获取项目继承设置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectSettingsInheritCfg
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectSettingsInheritCfgRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectSettingsInheritCfgResponse`
        """
        http_info = self._show_project_settings_inherit_cfg_http_info(request)
        return self._call_api(**http_info)

    def show_project_settings_inherit_cfg_async_invoker(self, request):
        http_info = self._show_project_settings_inherit_cfg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_settings_inherit_cfg_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/settings-inherit-cfg",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectSettingsInheritCfgResponse"
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

    def show_project_watermark_async(self, request):
        r"""获取项目水印设置

        获取项目水印设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectWatermark
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectWatermarkRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectWatermarkResponse`
        """
        http_info = self._show_project_watermark_http_info(request)
        return self._call_api(**http_info)

    def show_project_watermark_async_invoker(self, request):
        http_info = self._show_project_watermark_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_watermark_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectWatermarkResponse"
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

    def update_project_settings_inherit_cfg_async(self, request):
        r"""更新项目继承设置项

        更新项目继承设置项
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectSettingsInheritCfg
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProjectSettingsInheritCfgRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProjectSettingsInheritCfgResponse`
        """
        http_info = self._update_project_settings_inherit_cfg_http_info(request)
        return self._call_api(**http_info)

    def update_project_settings_inherit_cfg_async_invoker(self, request):
        http_info = self._update_project_settings_inherit_cfg_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_settings_inherit_cfg_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/settings-inherit-cfg",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectSettingsInheritCfgResponse"
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

    def update_project_watermark_async(self, request):
        r"""更新项目水印设置

        更新项目水印设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectWatermark
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProjectWatermarkRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProjectWatermarkResponse`
        """
        http_info = self._update_project_watermark_http_info(request)
        return self._call_api(**http_info)

    def update_project_watermark_async_invoker(self, request):
        http_info = self._update_project_watermark_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_watermark_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectWatermarkResponse"
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

    def batch_create_protected_branch_async(self, request):
        r"""批量创建仓库保护分支

        批量创建仓库保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateProtectedBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchCreateProtectedBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchCreateProtectedBranchResponse`
        """
        http_info = self._batch_create_protected_branch_http_info(request)
        return self._call_api(**http_info)

    def batch_create_protected_branch_async_invoker(self, request):
        http_info = self._batch_create_protected_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_protected_branch_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/protected-branches",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateProtectedBranchResponse"
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

    def batch_delete_protected_branches_async(self, request):
        r"""批量删除仓库保护分支

        批量删除仓库保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteProtectedBranches
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchDeleteProtectedBranchesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchDeleteProtectedBranchesResponse`
        """
        http_info = self._batch_delete_protected_branches_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_protected_branches_async_invoker(self, request):
        http_info = self._batch_delete_protected_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_protected_branches_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/protected-branches/bulk-deletion",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteProtectedBranchesResponse"
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

    def batch_update_protected_branches_async(self, request):
        r"""批量更新仓库保护分支

        批量更新仓库保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateProtectedBranches
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchUpdateProtectedBranchesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchUpdateProtectedBranchesResponse`
        """
        http_info = self._batch_update_protected_branches_http_info(request)
        return self._call_api(**http_info)

    def batch_update_protected_branches_async_invoker(self, request):
        http_info = self._batch_update_protected_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_protected_branches_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/protected-branches",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateProtectedBranchesResponse"
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

    def create_project_protected_branches_async(self, request):
        r"""创建项目下保护分支

        创建项目下保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProjectProtectedBranches
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateProjectProtectedBranchesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateProjectProtectedBranchesResponse`
        """
        http_info = self._create_project_protected_branches_http_info(request)
        return self._call_api(**http_info)

    def create_project_protected_branches_async_invoker(self, request):
        http_info = self._create_project_protected_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_project_protected_branches_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/protected-branches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectProtectedBranchesResponse"
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

    def delete_protected_branch_async(self, request):
        r"""删除仓库保护分支

        删除仓库保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectedBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteProtectedBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteProtectedBranchResponse`
        """
        http_info = self._delete_protected_branch_http_info(request)
        return self._call_api(**http_info)

    def delete_protected_branch_async_invoker(self, request):
        http_info = self._delete_protected_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_protected_branch_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/protected-branch",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProtectedBranchResponse"
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

    def list_project_protected_branches_async(self, request):
        r"""获取项目下保护分支列表

        获取项目下保护分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectProtectedBranches
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectProtectedBranchesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectProtectedBranchesResponse`
        """
        http_info = self._list_project_protected_branches_http_info(request)
        return self._call_api(**http_info)

    def list_project_protected_branches_async_invoker(self, request):
        http_info = self._list_project_protected_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_protected_branches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/protected-branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectProtectedBranchesResponse"
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
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'user_actions' in local_var_params:
            query_params.append(('user_actions', local_var_params['user_actions']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_protected_branches_async(self, request):
        r"""获取仓库保护分支列表

        获取仓库保护分支列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectedBranches
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProtectedBranchesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProtectedBranchesResponse`
        """
        http_info = self._list_protected_branches_http_info(request)
        return self._call_api(**http_info)

    def list_protected_branches_async_invoker(self, request):
        http_info = self._list_protected_branches_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_protected_branches_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/protected-branches",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectedBranchesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def show_protected_branch_async(self, request):
        r"""获取仓库保护分支

        获取仓库保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProtectedBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProtectedBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProtectedBranchResponse`
        """
        http_info = self._show_protected_branch_http_info(request)
        return self._call_api(**http_info)

    def show_protected_branch_async_invoker(self, request):
        http_info = self._show_protected_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_protected_branch_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/protected-branch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProtectedBranchResponse"
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

    def update_protected_branch_async(self, request):
        r"""更新仓库保护分支

        更新仓库保护分支
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProtectedBranch
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProtectedBranchRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProtectedBranchResponse`
        """
        http_info = self._update_protected_branch_http_info(request)
        return self._call_api(**http_info)

    def update_protected_branch_async_invoker(self, request):
        http_info = self._update_protected_branch_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_protected_branch_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/protected-branch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProtectedBranchResponse"
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

    def batch_create_protected_tags_async(self, request):
        r"""批量创建仓库保护Tag

        批量创建仓库保护Tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateProtectedTags
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchCreateProtectedTagsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchCreateProtectedTagsResponse`
        """
        http_info = self._batch_create_protected_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_protected_tags_async_invoker(self, request):
        http_info = self._batch_create_protected_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_protected_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/protected-tags",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateProtectedTagsResponse"
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

    def batch_delete_protected_tags_async(self, request):
        r"""批量删除仓库保护Tag

        批量删除仓库保护Tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteProtectedTags
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchDeleteProtectedTagsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchDeleteProtectedTagsResponse`
        """
        http_info = self._batch_delete_protected_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_protected_tags_async_invoker(self, request):
        http_info = self._batch_delete_protected_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_protected_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/protected-tags/bulk-deletion",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteProtectedTagsResponse"
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

    def batch_update_protected_tags_async(self, request):
        r"""批量更新仓库保护Tag

        批量更新仓库保护Tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateProtectedTags
        :type request: :class:`huaweicloudsdkcodehub.v4.BatchUpdateProtectedTagsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.BatchUpdateProtectedTagsResponse`
        """
        http_info = self._batch_update_protected_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_update_protected_tags_async_invoker(self, request):
        http_info = self._batch_update_protected_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_protected_tags_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/protected-tags",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateProtectedTagsResponse"
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

    def delete_protected_tag_async(self, request):
        r"""删除仓库保护Tag

        删除仓库保护Tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectedTag
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteProtectedTagRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteProtectedTagResponse`
        """
        http_info = self._delete_protected_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_protected_tag_async_invoker(self, request):
        http_info = self._delete_protected_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_protected_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/protected-tag",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProtectedTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))

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

    def list_protected_tags_async(self, request):
        r"""获取仓库保护Tag列表

        获取仓库保护Tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectedTags
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProtectedTagsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProtectedTagsResponse`
        """
        http_info = self._list_protected_tags_http_info(request)
        return self._call_api(**http_info)

    def list_protected_tags_async_invoker(self, request):
        http_info = self._list_protected_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_protected_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/protected-tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProtectedTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def show_protected_tag_async(self, request):
        r"""获取仓库保护Tag

        获取仓库保护Tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProtectedTag
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProtectedTagRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProtectedTagResponse`
        """
        http_info = self._show_protected_tag_http_info(request)
        return self._call_api(**http_info)

    def show_protected_tag_async_invoker(self, request):
        http_info = self._show_protected_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_protected_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/protected-tag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProtectedTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))

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

    def update_protected_tag_async(self, request):
        r"""更新仓库保护Tag

        更新仓库保护Tag
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProtectedTag
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProtectedTagRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProtectedTagResponse`
        """
        http_info = self._update_protected_tag_http_info(request)
        return self._call_api(**http_info)

    def update_protected_tag_async_invoker(self, request):
        http_info = self._update_protected_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_protected_tag_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/protected-tag",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProtectedTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))

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

    def add_submodule_async(self, request):
        r"""创建子模块

        创建子模块
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSubmodule
        :type request: :class:`huaweicloudsdkcodehub.v4.AddSubmoduleRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddSubmoduleResponse`
        """
        http_info = self._add_submodule_http_info(request)
        return self._call_api(**http_info)

    def add_submodule_async_invoker(self, request):
        http_info = self._add_submodule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_submodule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/submodules",
            "request_type": request.__class__.__name__,
            "response_type": "AddSubmoduleResponse"
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

    def add_trusted_ip_address_async(self, request):
        r"""添加仓库ip白名单

        添加仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddTrustedIpAddressResponse`
        """
        http_info = self._add_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def add_trusted_ip_address_async_invoker(self, request):
        http_info = self._add_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "AddTrustedIpAddressResponse"
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

    def associate_remote_mirror_async(self, request):
        r"""将普通仓库与远程镜像关联

        将普通仓库与远程镜像关联
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRemoteMirror
        :type request: :class:`huaweicloudsdkcodehub.v4.AssociateRemoteMirrorRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AssociateRemoteMirrorResponse`
        """
        http_info = self._associate_remote_mirror_http_info(request)
        return self._call_api(**http_info)

    def associate_remote_mirror_async_invoker(self, request):
        http_info = self._associate_remote_mirror_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_remote_mirror_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/remote-mirror/associate",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRemoteMirrorResponse"
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

    def associate_repository_user_group_async(self, request):
        r"""关联仓库与成员组

        关联仓库与成员组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateRepositoryUserGroup
        :type request: :class:`huaweicloudsdkcodehub.v4.AssociateRepositoryUserGroupRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AssociateRepositoryUserGroupResponse`
        """
        http_info = self._associate_repository_user_group_http_info(request)
        return self._call_api(**http_info)

    def associate_repository_user_group_async_invoker(self, request):
        http_info = self._associate_repository_user_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_repository_user_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/repositories/{repository_id}/user-group/{user_group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateRepositoryUserGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'user_group_id' in local_var_params:
            path_params['user_group_id'] = local_var_params['user_group_id']

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

    def create_dir_async(self, request):
        r"""创建指定分支下的目录

        创建指定分支下的目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDir
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateDirRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateDirResponse`
        """
        http_info = self._create_dir_http_info(request)
        return self._call_api(**http_info)

    def create_dir_async_invoker(self, request):
        http_info = self._create_dir_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dir_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/dir",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDirResponse"
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

    def delete_trusted_ip_address_async(self, request):
        r"""删除仓库ip白名单

        删除仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteTrustedIpAddressResponse`
        """
        http_info = self._delete_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def delete_trusted_ip_address_async_invoker(self, request):
        http_info = self._delete_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def download_archive_async(self, request):
        r"""仓库下载

        仓库下载
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadArchive
        :type request: :class:`huaweicloudsdkcodehub.v4.DownloadArchiveRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DownloadArchiveResponse`
        """
        http_info = self._download_archive_http_info(request)
        return self._call_api(**http_info)

    def download_archive_async_invoker(self, request):
        http_info = self._download_archive_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_archive_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/archive",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadArchiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'archive_format' in local_var_params:
            query_params.append(('archive_format', local_var_params['archive_format']))

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

    def list_current_user_repositories_async(self, request):
        r"""获取当前登录用户仓库

        获取当前登录用户仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCurrentUserRepositories
        :type request: :class:`huaweicloudsdkcodehub.v4.ListCurrentUserRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListCurrentUserRepositoriesResponse`
        """
        http_info = self._list_current_user_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_current_user_repositories_async_invoker(self, request):
        http_info = self._list_current_user_repositories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_current_user_repositories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListCurrentUserRepositoriesResponse"
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

    def list_manageable_groups_async(self, request):
        r"""获取项目下当前用户有管理权限的代码组列表

        获取项目下当前用户有管理权限的代码组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListManageableGroups
        :type request: :class:`huaweicloudsdkcodehub.v4.ListManageableGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListManageableGroupsResponse`
        """
        http_info = self._list_manageable_groups_http_info(request)
        return self._call_api(**http_info)

    def list_manageable_groups_async_invoker(self, request):
        http_info = self._list_manageable_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_manageable_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/{project_id}/manageable-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListManageableGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
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

    def list_personal_repository_import_records_async(self, request):
        r"""查看当前用户仓库导入任务列表

        查看当前用户仓库导入任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPersonalRepositoryImportRecords
        :type request: :class:`huaweicloudsdkcodehub.v4.ListPersonalRepositoryImportRecordsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListPersonalRepositoryImportRecordsResponse`
        """
        http_info = self._list_personal_repository_import_records_http_info(request)
        return self._call_api(**http_info)

    def list_personal_repository_import_records_async_invoker(self, request):
        http_info = self._list_personal_repository_import_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_personal_repository_import_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user/repository-import-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListPersonalRepositoryImportRecordsResponse"
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
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'created_after' in local_var_params:
            query_params.append(('created_after', local_var_params['created_after']))
        if 'created_before' in local_var_params:
            query_params.append(('created_before', local_var_params['created_before']))
        if 'finished_after' in local_var_params:
            query_params.append(('finished_after', local_var_params['finished_after']))
        if 'finished_before' in local_var_params:
            query_params.append(('finished_before', local_var_params['finished_before']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_repository_commit_rules_async(self, request):
        r"""查看仓库提交规则

        查看仓库提交规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryCommitRules
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryCommitRulesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryCommitRulesResponse`
        """
        http_info = self._list_repository_commit_rules_http_info(request)
        return self._call_api(**http_info)

    def list_repository_commit_rules_async_invoker(self, request):
        http_info = self._list_repository_commit_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_commit_rules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/commit-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryCommitRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

        response_headers = ["X-Total", ]

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

    def list_repository_contributors_async(self, request):
        r"""获取仓库贡献者列表

        获取仓库贡献者列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryContributors
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryContributorsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryContributorsResponse`
        """
        http_info = self._list_repository_contributors_http_info(request)
        return self._call_api(**http_info)

    def list_repository_contributors_async_invoker(self, request):
        http_info = self._list_repository_contributors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_contributors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/contributors",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryContributorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'ref_name' in local_var_params:
            query_params.append(('ref_name', local_var_params['ref_name']))
        if 'skip_merge' in local_var_params:
            query_params.append(('skip_merge', local_var_params['skip_merge']))
        if 'author' in local_var_params:
            query_params.append(('author', local_var_params['author']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_repository_events_async(self, request):
        r"""获取仓库动态

        获取仓库动态（当前仅开放推送动态）
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryEvents
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryEventsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryEventsResponse`
        """
        http_info = self._list_repository_events_http_info(request)
        return self._call_api(**http_info)

    def list_repository_events_async_invoker(self, request):
        http_info = self._list_repository_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'author_id' in local_var_params:
            query_params.append(('author_id', local_var_params['author_id']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'before' in local_var_params:
            query_params.append(('before', local_var_params['before']))
        if 'after' in local_var_params:
            query_params.append(('after', local_var_params['after']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_repository_forks_async(self, request):
        r"""获取仓库Fork列表

        获取仓库Fork列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryForks
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryForksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryForksResponse`
        """
        http_info = self._list_repository_forks_http_info(request)
        return self._call_api(**http_info)

    def list_repository_forks_async_invoker(self, request):
        http_info = self._list_repository_forks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_forks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/forks",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryForksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))

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

    def list_repository_languages_async(self, request):
        r"""获取仓库默认分支语言统计

        获取仓库默认分支语言统计
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryLanguages
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryLanguagesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryLanguagesResponse`
        """
        http_info = self._list_repository_languages_http_info(request)
        return self._call_api(**http_info)

    def list_repository_languages_async_invoker(self, request):
        http_info = self._list_repository_languages_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_languages_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/languages",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryLanguagesResponse"
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

        response_headers = ["X-Total", ]

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

    def list_repository_templates_async(self, request):
        r"""模板仓列表

        模板仓列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryTemplates
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryTemplatesResponse`
        """
        http_info = self._list_repository_templates_http_info(request)
        return self._call_api(**http_info)

    def list_repository_templates_async_invoker(self, request):
        http_info = self._list_repository_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repository-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryTemplatesResponse"
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
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))
        if 'pipeline' in local_var_params:
            query_params.append(('pipeline', local_var_params['pipeline']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'enter_type' in local_var_params:
            query_params.append(('enter_type', local_var_params['enter_type']))
        if 'date_order' in local_var_params:
            query_params.append(('date_order', local_var_params['date_order']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_submodules_async(self, request):
        r"""获取仓库指定分支或者标签子模块列表

        获取仓库指定分支或者标签子模块列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubmodules
        :type request: :class:`huaweicloudsdkcodehub.v4.ListSubmodulesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListSubmodulesResponse`
        """
        http_info = self._list_submodules_http_info(request)
        return self._call_api(**http_info)

    def list_submodules_async_invoker(self, request):
        http_info = self._list_submodules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_submodules_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/submodules",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubmodulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'sha' in local_var_params:
            query_params.append(('sha', local_var_params['sha']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_trees_async(self, request):
        r"""查看分支文件列表

        查看分支文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrees
        :type request: :class:`huaweicloudsdkcodehub.v4.ListTreesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListTreesResponse`
        """
        http_info = self._list_trees_http_info(request)
        return self._call_api(**http_info)

    def list_trees_async_invoker(self, request):
        http_info = self._list_trees_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_trees_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/trees",
            "request_type": request.__class__.__name__,
            "response_type": "ListTreesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'ref' in local_var_params:
            query_params.append(('ref', local_var_params['ref']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'recursive' in local_var_params:
            query_params.append(('recursive', local_var_params['recursive']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_trusted_ip_addresses_async(self, request):
        r"""获取仓库ip白名单

        获取仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrustedIpAddresses
        :type request: :class:`huaweicloudsdkcodehub.v4.ListTrustedIpAddressesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListTrustedIpAddressesResponse`
        """
        http_info = self._list_trusted_ip_addresses_http_info(request)
        return self._call_api(**http_info)

    def list_trusted_ip_addresses_async_invoker(self, request):
        http_info = self._list_trusted_ip_addresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_trusted_ip_addresses_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrustedIpAddressesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

        response_headers = ["X-Total", ]

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

    def lock_repository_async(self, request):
        r"""锁定仓库

        锁定仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LockRepository
        :type request: :class:`huaweicloudsdkcodehub.v4.LockRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.LockRepositoryResponse`
        """
        http_info = self._lock_repository_http_info(request)
        return self._call_api(**http_info)

    def lock_repository_async_invoker(self, request):
        http_info = self._lock_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _lock_repository_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/repositories/{repository_id}/lock",
            "request_type": request.__class__.__name__,
            "response_type": "LockRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

    def remove_deploy_key_async(self, request):
        r"""删除仓库部署秘钥

        删除仓库部署秘钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v4.RemoveDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.RemoveDeployKeyResponse`
        """
        http_info = self._remove_deploy_key_http_info(request)
        return self._call_api(**http_info)

    def remove_deploy_key_async_invoker(self, request):
        http_info = self._remove_deploy_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_deploy_key_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/deploy-keys/{key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveDeployKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def show_blobs_async(self, request):
        r"""获取文件内容

        获取文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBlobs
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowBlobsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowBlobsResponse`
        """
        http_info = self._show_blobs_http_info(request)
        return self._call_api(**http_info)

    def show_blobs_async_invoker(self, request):
        http_info = self._show_blobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_blobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/blobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBlobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'blob_id' in local_var_params:
            query_params.append(('blob_id', local_var_params['blob_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_commit_statistics_async(self, request):
        r"""获取仓库指定分支的提交统计信息

        获取仓库指定分支的提交统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommitStatistics
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowCommitStatisticsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowCommitStatisticsResponse`
        """
        http_info = self._show_commit_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_commit_statistics_async_invoker(self, request):
        http_info = self._show_commit_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_commit_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/commit-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommitStatisticsResponse"
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

        response_headers = ["X-Total", ]

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

    def show_diff_lines_async(self, request):
        r"""按行数查询提交文件内容

        按行数查询提交文件内容，最大显示行数为1000行
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDiffLines
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowDiffLinesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowDiffLinesResponse`
        """
        http_info = self._show_diff_lines_http_info(request)
        return self._call_api(**http_info)

    def show_diff_lines_async_invoker(self, request):
        http_info = self._show_diff_lines_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_diff_lines_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/diff-lines",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiffLinesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'commit_id' in local_var_params:
            query_params.append(('commit_id', local_var_params['commit_id']))
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
        if 'end' in local_var_params:
            query_params.append(('end', local_var_params['end']))

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

    def show_last_push_event_in_repository_async(self, request):
        r"""获取仓库最近推送事件

        获取仓库最近推送事件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowLastPushEventInRepository
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowLastPushEventInRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowLastPushEventInRepositoryResponse`
        """
        http_info = self._show_last_push_event_in_repository_http_info(request)
        return self._call_api(**http_info)

    def show_last_push_event_in_repository_async_invoker(self, request):
        http_info = self._show_last_push_event_in_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_last_push_event_in_repository_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/last-push-event",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLastPushEventInRepositoryResponse"
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

    def show_notification_subscription_async(self, request):
        r"""获取仓库通知设置

        获取仓库通知设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotificationSubscription
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowNotificationSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowNotificationSubscriptionResponse`
        """
        http_info = self._show_notification_subscription_http_info(request)
        return self._call_api(**http_info)

    def show_notification_subscription_async_invoker(self, request):
        http_info = self._show_notification_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notification_subscription_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/notification-subscriptions/subscription",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotificationSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

    def show_notification_subscriptions_status_async(self, request):
        r"""获取仓库通知设置启用状态

        获取仓库通知设置启用状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotificationSubscriptionsStatus
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowNotificationSubscriptionsStatusRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowNotificationSubscriptionsStatusResponse`
        """
        http_info = self._show_notification_subscriptions_status_http_info(request)
        return self._call_api(**http_info)

    def show_notification_subscriptions_status_async_invoker(self, request):
        http_info = self._show_notification_subscriptions_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notification_subscriptions_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/notification-subscriptions/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotificationSubscriptionsStatusResponse"
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

    def show_ref_compare_async(self, request):
        r"""分支、tags、提交对比

        分支、tags、提交对比
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRefCompare
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRefCompareRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRefCompareResponse`
        """
        http_info = self._show_ref_compare_http_info(request)
        return self._call_api(**http_info)

    def show_ref_compare_async_invoker(self, request):
        http_info = self._show_ref_compare_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ref_compare_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/compare",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRefCompareResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
        if 'target_id' in local_var_params:
            query_params.append(('target_id', local_var_params['target_id']))
        if 'straight' in local_var_params:
            query_params.append(('straight', local_var_params['straight']))
        if 'ignore_whitespace_change' in local_var_params:
            query_params.append(('ignore_whitespace_change', local_var_params['ignore_whitespace_change']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'only_count' in local_var_params:
            query_params.append(('only_count', local_var_params['only_count']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))
        if 'additional_fields' in local_var_params:
            query_params.append(('additional_fields', local_var_params['additional_fields']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_remote_mirror_async(self, request):
        r"""获取仓库镜像详情

        获取仓库镜像详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRemoteMirror
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRemoteMirrorRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRemoteMirrorResponse`
        """
        http_info = self._show_remote_mirror_http_info(request)
        return self._call_api(**http_info)

    def show_remote_mirror_async_invoker(self, request):
        http_info = self._show_remote_mirror_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_remote_mirror_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/remote-mirror",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRemoteMirrorResponse"
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

    def show_repository_async(self, request):
        r"""获取仓库详情

        获取仓库详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepository
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryResponse`
        """
        http_info = self._show_repository_http_info(request)
        return self._call_api(**http_info)

    def show_repository_async_invoker(self, request):
        http_info = self._show_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryResponse"
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

    def show_repository_general_commit_rule_async(self, request):
        r"""查看仓库通用提交规则

        查看仓库通用提交规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryGeneralCommitRule
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryGeneralCommitRuleRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryGeneralCommitRuleResponse`
        """
        http_info = self._show_repository_general_commit_rule_http_info(request)
        return self._call_api(**http_info)

    def show_repository_general_commit_rule_async_invoker(self, request):
        http_info = self._show_repository_general_commit_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_general_commit_rule_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/general-commit-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryGeneralCommitRuleResponse"
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

    def show_repository_general_policy_async(self, request):
        r"""查看仓库通用策略

        查看仓库通用策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryGeneralPolicy
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryGeneralPolicyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryGeneralPolicyResponse`
        """
        http_info = self._show_repository_general_policy_http_info(request)
        return self._call_api(**http_info)

    def show_repository_general_policy_async_invoker(self, request):
        http_info = self._show_repository_general_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_general_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/general-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryGeneralPolicyResponse"
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

    def show_repository_inherit_setting_async(self, request):
        r"""查看仓库继承设置

        查看仓库继承设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryInheritSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryInheritSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryInheritSettingResponse`
        """
        http_info = self._show_repository_inherit_setting_http_info(request)
        return self._call_api(**http_info)

    def show_repository_inherit_setting_async_invoker(self, request):
        http_info = self._show_repository_inherit_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_inherit_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/inherit-setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryInheritSettingResponse"
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

    def show_repository_inherit_setting_source_async(self, request):
        r"""查看仓库继承设置源

        查看仓库继承设置源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryInheritSettingSource
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryInheritSettingSourceRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryInheritSettingSourceResponse`
        """
        http_info = self._show_repository_inherit_setting_source_http_info(request)
        return self._call_api(**http_info)

    def show_repository_inherit_setting_source_async_invoker(self, request):
        http_info = self._show_repository_inherit_setting_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_inherit_setting_source_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/inherit-setting-source",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryInheritSettingSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
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

    def show_repository_statistics_status_async(self, request):
        r"""获取仓库统计任务状态

        获取仓库统计任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryStatisticsStatus
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryStatisticsStatusRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryStatisticsStatusResponse`
        """
        http_info = self._show_repository_statistics_status_http_info(request)
        return self._call_api(**http_info)

    def show_repository_statistics_status_async_invoker(self, request):
        http_info = self._show_repository_statistics_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_statistics_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/statistics-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryStatisticsStatusResponse"
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

        response_headers = ["X-Total", ]

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

    def show_repository_statistics_summary_async(self, request):
        r"""获取仓库统计摘要

        获取仓库统计摘要
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryStatisticsSummary
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryStatisticsSummaryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryStatisticsSummaryResponse`
        """
        http_info = self._show_repository_statistics_summary_http_info(request)
        return self._call_api(**http_info)

    def show_repository_statistics_summary_async_invoker(self, request):
        http_info = self._show_repository_statistics_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_statistics_summary_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/statistics-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryStatisticsSummaryResponse"
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

    def show_repository_watermark_async(self, request):
        r"""获取仓库水印设置

        获取仓库水印设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryWatermark
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryWatermarkRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryWatermarkResponse`
        """
        http_info = self._show_repository_watermark_http_info(request)
        return self._call_api(**http_info)

    def show_repository_watermark_async_invoker(self, request):
        http_info = self._show_repository_watermark_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_watermark_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryWatermarkResponse"
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

    def show_user_ref_permission_async(self, request):
        r"""获取CR仓库用户分支或标签级权限

        获取CR仓库用户分支或标签级权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserRefPermission
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowUserRefPermissionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowUserRefPermissionResponse`
        """
        http_info = self._show_user_ref_permission_http_info(request)
        return self._call_api(**http_info)

    def show_user_ref_permission_async_invoker(self, request):
        http_info = self._show_user_ref_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_ref_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/user-ref-permission",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserRefPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'target_ref' in local_var_params:
            query_params.append(('target_ref', local_var_params['target_ref']))
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))
        if 'change_request_iid' in local_var_params:
            query_params.append(('change_request_iid', local_var_params['change_request_iid']))

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

    def start_remote_mirror_synchronization_async(self, request):
        r"""启动仓库镜像同步

        启动仓库镜像同步
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartRemoteMirrorSynchronization
        :type request: :class:`huaweicloudsdkcodehub.v4.StartRemoteMirrorSynchronizationRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.StartRemoteMirrorSynchronizationResponse`
        """
        http_info = self._start_remote_mirror_synchronization_http_info(request)
        return self._call_api(**http_info)

    def start_remote_mirror_synchronization_async_invoker(self, request):
        http_info = self._start_remote_mirror_synchronization_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_remote_mirror_synchronization_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/remote-mirror",
            "request_type": request.__class__.__name__,
            "response_type": "StartRemoteMirrorSynchronizationResponse"
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

    def unlock_repository_async(self, request):
        r"""解锁仓库

        解锁仓库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnlockRepository
        :type request: :class:`huaweicloudsdkcodehub.v4.UnlockRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UnlockRepositoryResponse`
        """
        http_info = self._unlock_repository_http_info(request)
        return self._call_api(**http_info)

    def unlock_repository_async_invoker(self, request):
        http_info = self._unlock_repository_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unlock_repository_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/{project_id}/repositories/{repository_id}/unlock",
            "request_type": request.__class__.__name__,
            "response_type": "UnlockRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
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

    def update_notification_subscription_async(self, request):
        r"""修改仓库通知设置

        修改仓库通知设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotificationSubscription
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateNotificationSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateNotificationSubscriptionResponse`
        """
        http_info = self._update_notification_subscription_http_info(request)
        return self._call_api(**http_info)

    def update_notification_subscription_async_invoker(self, request):
        http_info = self._update_notification_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notification_subscription_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/notification-subscriptions/subscription",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotificationSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def update_repository_general_policy_async(self, request):
        r"""修改仓库通用策略

        修改仓库通用策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepositoryGeneralPolicy
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryGeneralPolicyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryGeneralPolicyResponse`
        """
        http_info = self._update_repository_general_policy_http_info(request)
        return self._call_api(**http_info)

    def update_repository_general_policy_async_invoker(self, request):
        http_info = self._update_repository_general_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_repository_general_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/general-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepositoryGeneralPolicyResponse"
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

    def update_repository_inherit_setting_async(self, request):
        r"""修改仓库继承设置

        修改仓库继承设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepositoryInheritSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryInheritSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryInheritSettingResponse`
        """
        http_info = self._update_repository_inherit_setting_http_info(request)
        return self._call_api(**http_info)

    def update_repository_inherit_setting_async_invoker(self, request):
        http_info = self._update_repository_inherit_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_repository_inherit_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/inherit-setting",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepositoryInheritSettingResponse"
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

    def update_repository_watermark_async(self, request):
        r"""更新仓库水印设置

        更新仓库水印设置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepositoryWatermark
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryWatermarkRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryWatermarkResponse`
        """
        http_info = self._update_repository_watermark_http_info(request)
        return self._call_api(**http_info)

    def update_repository_watermark_async_invoker(self, request):
        http_info = self._update_repository_watermark_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_repository_watermark_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepositoryWatermarkResponse"
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

    def update_trusted_ip_address_async(self, request):
        r"""修改仓库ip白名单

        修改仓库ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateTrustedIpAddressResponse`
        """
        http_info = self._update_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def update_trusted_ip_address_async_invoker(self, request):
        http_info = self._update_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{id}/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def create_tag_async(self, request):
        r"""创建标签

        创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkcodehub.v4.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_async_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/repository/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
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

    def delete_tag_async(self, request):
        r"""删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/repository/tag",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))

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

    def list_tags_async(self, request):
        r"""获取标签列表

        获取标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkcodehub.v4.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'search' in local_var_params:
            query_params.append(('search', local_var_params['search']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'view' in local_var_params:
            query_params.append(('view', local_var_params['view']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def show_tag_async(self, request):
        r"""查看标签详情

        查看标签详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTag
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowTagRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowTagResponse`
        """
        http_info = self._show_tag_http_info(request)
        return self._call_api(**http_info)

    def show_tag_async_invoker(self, request):
        http_info = self._show_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tag_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/repository/tag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'tag_name' in local_var_params:
            query_params.append(('tag_name', local_var_params['tag_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def add_tenant_trusted_ip_address_async(self, request):
        r"""添加租户ip白名单

        添加租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddTenantTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.AddTenantTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddTenantTrustedIpAddressResponse`
        """
        http_info = self._add_tenant_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def add_tenant_trusted_ip_address_async_invoker(self, request):
        http_info = self._add_tenant_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_tenant_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/tenant/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "AddTenantTrustedIpAddressResponse"
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

    def delete_tenant_trusted_ip_address_async(self, request):
        r"""删除租户ip白名单

        删除租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTenantTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteTenantTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteTenantTrustedIpAddressResponse`
        """
        http_info = self._delete_tenant_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def delete_tenant_trusted_ip_address_async_invoker(self, request):
        http_info = self._delete_tenant_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tenant_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/tenant/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTenantTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def list_tenant_trusted_ip_addresses_async(self, request):
        r"""获取租户ip白名单

        获取租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTenantTrustedIpAddresses
        :type request: :class:`huaweicloudsdkcodehub.v4.ListTenantTrustedIpAddressesRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListTenantTrustedIpAddressesResponse`
        """
        http_info = self._list_tenant_trusted_ip_addresses_http_info(request)
        return self._call_api(**http_info)

    def list_tenant_trusted_ip_addresses_async_invoker(self, request):
        http_info = self._list_tenant_trusted_ip_addresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tenant_trusted_ip_addresses_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/tenant/trusted-ip-addresses",
            "request_type": request.__class__.__name__,
            "response_type": "ListTenantTrustedIpAddressesResponse"
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

        response_headers = ["X-Total", ]

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

    def update_tenant_trusted_ip_address_async(self, request):
        r"""修改租户ip白名单

        修改租户ip白名单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTenantTrustedIpAddress
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateTenantTrustedIpAddressRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateTenantTrustedIpAddressResponse`
        """
        http_info = self._update_tenant_trusted_ip_address_http_info(request)
        return self._call_api(**http_info)

    def update_tenant_trusted_ip_address_async_invoker(self, request):
        http_info = self._update_tenant_trusted_ip_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_tenant_trusted_ip_address_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/tenant/trusted-ip-addresses/{ip_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTenantTrustedIpAddressResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'ip_id' in local_var_params:
            path_params['ip_id'] = local_var_params['ip_id']

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

    def check_deploy_key_async(self, request):
        r"""校验部署秘钥在上层代码组或项目是否配置

        校验部署秘钥在上层代码组或项目是否配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v4.CheckDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CheckDeployKeyResponse`
        """
        http_info = self._check_deploy_key_http_info(request)
        return self._call_api(**http_info)

    def check_deploy_key_async_invoker(self, request):
        http_info = self._check_deploy_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_deploy_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/deploy-keys/check-key",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDeployKeyResponse"
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

    def check_group_deploy_key_async(self, request):
        r"""校验代码组部署秘钥在上层代码组或项目是否配置

        校验代码组部署秘钥在上层代码组或项目是否配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckGroupDeployKey
        :type request: :class:`huaweicloudsdkcodehub.v4.CheckGroupDeployKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.CheckGroupDeployKeyResponse`
        """
        http_info = self._check_group_deploy_key_http_info(request)
        return self._call_api(**http_info)

    def check_group_deploy_key_async_invoker(self, request):
        http_info = self._check_group_deploy_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_group_deploy_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/groups/{group_id}/deploy-keys/check-key",
            "request_type": request.__class__.__name__,
            "response_type": "CheckGroupDeployKeyResponse"
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

    def list_branch_related_work_items_async(self, request):
        r"""获取仓库下指定分支的关联工作项列表

        获取仓库下指定分支的关联工作项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBranchRelatedWorkItems
        :type request: :class:`huaweicloudsdkcodehub.v4.ListBranchRelatedWorkItemsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListBranchRelatedWorkItemsResponse`
        """
        http_info = self._list_branch_related_work_items_http_info(request)
        return self._call_api(**http_info)

    def list_branch_related_work_items_async_invoker(self, request):
        http_info = self._list_branch_related_work_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_branch_related_work_items_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/branch/work-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListBranchRelatedWorkItemsResponse"
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

    def list_group_deploy_keys_async(self, request):
        r"""获取代码组下部署密钥列表

        获取代码组下部署密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupDeployKeys
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupDeployKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupDeployKeysResponse`
        """
        http_info = self._list_group_deploy_keys_http_info(request)
        return self._call_api(**http_info)

    def list_group_deploy_keys_async_invoker(self, request):
        http_info = self._list_group_deploy_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_deploy_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/deploy-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupDeployKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

        response_headers = ["X-Total", ]

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

    def list_project_deploy_keys_async(self, request):
        r"""获取项目下部署密钥列表

        获取项目下部署密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectDeployKeys
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectDeployKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectDeployKeysResponse`
        """
        http_info = self._list_project_deploy_keys_http_info(request)
        return self._call_api(**http_info)

    def list_project_deploy_keys_async_invoker(self, request):
        http_info = self._list_project_deploy_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_deploy_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/deploy-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectDeployKeysResponse"
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

        response_headers = ["X-Total", ]

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

    def list_repository_deploy_keys_async(self, request):
        r"""获取仓库下部署密钥列表

        获取仓库下部署密钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryDeployKeys
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryDeployKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryDeployKeysResponse`
        """
        http_info = self._list_repository_deploy_keys_http_info(request)
        return self._call_api(**http_info)

    def list_repository_deploy_keys_async_invoker(self, request):
        http_info = self._list_repository_deploy_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_deploy_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/deploy-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryDeployKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

        response_headers = ["X-Total", ]

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

    def list_repository_work_items_async(self, request):
        r"""获取仓库下工作项列表

        获取仓库下工作项列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryWorkItems
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryWorkItemsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryWorkItemsResponse`
        """
        http_info = self._list_repository_work_items_http_info(request)
        return self._call_api(**http_info)

    def list_repository_work_items_async_invoker(self, request):
        http_info = self._list_repository_work_items_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_work_items_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/work-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryWorkItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'is_ipd' in local_var_params:
            query_params.append(('is_ipd', local_var_params['is_ipd']))
        if 'subject' in local_var_params:
            query_params.append(('subject', local_var_params['subject']))
        if 'target_branch' in local_var_params:
            query_params.append(('target_branch', local_var_params['target_branch']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def add_ssh_key_async(self, request):
        r"""添加ssh公钥

        添加ssh公钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSshKey
        :type request: :class:`huaweicloudsdkcodehub.v4.AddSshKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddSshKeyResponse`
        """
        http_info = self._add_ssh_key_http_info(request)
        return self._call_api(**http_info)

    def add_ssh_key_async_invoker(self, request):
        http_info = self._add_ssh_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_ssh_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/user/keys",
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

    def delete_ssh_key_async(self, request):
        r"""删除ssh公钥

        删除ssh公钥
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSshKey
        :type request: :class:`huaweicloudsdkcodehub.v4.DeleteSshKeyRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.DeleteSshKeyResponse`
        """
        http_info = self._delete_ssh_key_http_info(request)
        return self._call_api(**http_info)

    def delete_ssh_key_async_invoker(self, request):
        http_info = self._delete_ssh_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_ssh_key_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/user/keys/{key_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSshKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key_id' in local_var_params:
            path_params['key_id'] = local_var_params['key_id']

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

    def list_user_gpg_keys_async(self, request):
        r"""获取当前用户的gpg_key列表

        获取当前用户的gpg_key列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserGpgKeys
        :type request: :class:`huaweicloudsdkcodehub.v4.ListUserGpgKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListUserGpgKeysResponse`
        """
        http_info = self._list_user_gpg_keys_http_info(request)
        return self._call_api(**http_info)

    def list_user_gpg_keys_async_invoker(self, request):
        http_info = self._list_user_gpg_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_gpg_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user/gpg-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserGpgKeysResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))

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

    def list_user_keys_async(self, request):
        r"""获取当前用户的秘钥列表

        获取当前用户的秘钥列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserKeys
        :type request: :class:`huaweicloudsdkcodehub.v4.ListUserKeysRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListUserKeysResponse`
        """
        http_info = self._list_user_keys_http_info(request)
        return self._call_api(**http_info)

    def list_user_keys_async_invoker(self, request):
        http_info = self._list_user_keys_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_keys_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user/keys",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserKeysResponse"
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
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))

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

    def send_user_email_verify_code_async(self, request):
        r"""发送邮箱验证码

        发送邮箱验证码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendUserEmailVerifyCode
        :type request: :class:`huaweicloudsdkcodehub.v4.SendUserEmailVerifyCodeRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.SendUserEmailVerifyCodeResponse`
        """
        http_info = self._send_user_email_verify_code_http_info(request)
        return self._call_api(**http_info)

    def send_user_email_verify_code_async_invoker(self, request):
        http_info = self._send_user_email_verify_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_user_email_verify_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/user/email-verify-code",
            "request_type": request.__class__.__name__,
            "response_type": "SendUserEmailVerifyCodeResponse"
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

    def show_https_password_setting_async(self, request):
        r"""获取https的验证方式

        获取https的验证方式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpsPasswordSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowHttpsPasswordSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowHttpsPasswordSettingResponse`
        """
        http_info = self._show_https_password_setting_http_info(request)
        return self._call_api(**http_info)

    def show_https_password_setting_async_invoker(self, request):
        http_info = self._show_https_password_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_https_password_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user/https-password-setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpsPasswordSettingResponse"
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

    def show_user_emails_async(self, request):
        r"""获取用户相关邮箱信息

        获取用户相关邮箱信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserEmails
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowUserEmailsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowUserEmailsResponse`
        """
        http_info = self._show_user_emails_http_info(request)
        return self._call_api(**http_info)

    def show_user_emails_async_invoker(self, request):
        http_info = self._show_user_emails_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_user_emails_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/user/emails",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserEmailsResponse"
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

    def update_https_password_setting_async(self, request):
        r"""修改https的验证方式

        修改https的验证方式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHttpsPasswordSetting
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateHttpsPasswordSettingRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateHttpsPasswordSettingResponse`
        """
        http_info = self._update_https_password_setting_http_info(request)
        return self._call_api(**http_info)

    def update_https_password_setting_async_invoker(self, request):
        http_info = self._update_https_password_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_https_password_setting_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/user/https-password-setting",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHttpsPasswordSettingResponse"
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

    def update_user_emails_async(self, request):
        r"""更新邮箱

        更新邮箱
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserEmails
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateUserEmailsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateUserEmailsResponse`
        """
        http_info = self._update_user_emails_http_info(request)
        return self._call_api(**http_info)

    def update_user_emails_async_invoker(self, request):
        http_info = self._update_user_emails_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_user_emails_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/user/emails",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserEmailsResponse"
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

    def add_group_webhook_async(self, request):
        r"""添加代码组下Webhook

        添加代码组下Webhook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddGroupWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.AddGroupWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddGroupWebhookResponse`
        """
        http_info = self._add_group_webhook_http_info(request)
        return self._call_api(**http_info)

    def add_group_webhook_async_invoker(self, request):
        http_info = self._add_group_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_group_webhook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/groups/{group_id}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "AddGroupWebhookResponse"
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

    def add_project_webhook_async(self, request):
        r"""添加项目下Webhook

        添加项目下Webhook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddProjectWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.AddProjectWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddProjectWebhookResponse`
        """
        http_info = self._add_project_webhook_http_info(request)
        return self._call_api(**http_info)

    def add_project_webhook_async_invoker(self, request):
        http_info = self._add_project_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_project_webhook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/projects/{project_id}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "AddProjectWebhookResponse"
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

    def add_repository_webhook_async(self, request):
        r"""添加仓库下Webhook

        添加仓库下Webhook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRepositoryWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.AddRepositoryWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.AddRepositoryWebhookResponse`
        """
        http_info = self._add_repository_webhook_http_info(request)
        return self._call_api(**http_info)

    def add_repository_webhook_async_invoker(self, request):
        http_info = self._add_repository_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_repository_webhook_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v4/repositories/{repository_id}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "AddRepositoryWebhookResponse"
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

    def list_group_webhook_logs_async(self, request):
        r"""获取代码组下指定Webhook的日志列表

        获取代码组下指定Webhook的日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupWebhookLogs
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupWebhookLogsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupWebhookLogsResponse`
        """
        http_info = self._list_group_webhook_logs_http_info(request)
        return self._call_api(**http_info)

    def list_group_webhook_logs_async_invoker(self, request):
        http_info = self._list_group_webhook_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_webhook_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/hooks/{hook_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupWebhookLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'repository_id' in local_var_params:
            query_params.append(('repository_id', local_var_params['repository_id']))
        if 'uuid' in local_var_params:
            query_params.append(('uuid', local_var_params['uuid']))
        if 'created_after' in local_var_params:
            query_params.append(('created_after', local_var_params['created_after']))
        if 'created_before' in local_var_params:
            query_params.append(('created_before', local_var_params['created_before']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_group_webhooks_async(self, request):
        r"""获取代码组下Webhook列表

        获取代码组下Webhook列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupWebhooks
        :type request: :class:`huaweicloudsdkcodehub.v4.ListGroupWebhooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListGroupWebhooksResponse`
        """
        http_info = self._list_group_webhooks_http_info(request)
        return self._call_api(**http_info)

    def list_group_webhooks_async_invoker(self, request):
        http_info = self._list_group_webhooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_group_webhooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupWebhooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

        response_headers = ["X-Total", ]

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

    def list_project_webhook_logs_async(self, request):
        r"""获取项目下指定Webhook的日志列表

        获取项目下指定Webhook的日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectWebhookLogs
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectWebhookLogsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectWebhookLogsResponse`
        """
        http_info = self._list_project_webhook_logs_http_info(request)
        return self._call_api(**http_info)

    def list_project_webhook_logs_async_invoker(self, request):
        http_info = self._list_project_webhook_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_webhook_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/hooks/{hook_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectWebhookLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'repository_id' in local_var_params:
            query_params.append(('repository_id', local_var_params['repository_id']))
        if 'uuid' in local_var_params:
            query_params.append(('uuid', local_var_params['uuid']))
        if 'created_after' in local_var_params:
            query_params.append(('created_after', local_var_params['created_after']))
        if 'created_before' in local_var_params:
            query_params.append(('created_before', local_var_params['created_before']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_project_webhooks_async(self, request):
        r"""获取项目下Webhook列表

        获取项目下Webhook列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectWebhooks
        :type request: :class:`huaweicloudsdkcodehub.v4.ListProjectWebhooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListProjectWebhooksResponse`
        """
        http_info = self._list_project_webhooks_http_info(request)
        return self._call_api(**http_info)

    def list_project_webhooks_async_invoker(self, request):
        http_info = self._list_project_webhooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_webhooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectWebhooksResponse"
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

        response_headers = ["X-Total", ]

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

    def list_repository_webhook_logs_async(self, request):
        r"""获取仓库下指定Webhook的日志列表

        获取仓库下指定Webhook的日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryWebhookLogs
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryWebhookLogsRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryWebhookLogsResponse`
        """
        http_info = self._list_repository_webhook_logs_http_info(request)
        return self._call_api(**http_info)

    def list_repository_webhook_logs_async_invoker(self, request):
        http_info = self._list_repository_webhook_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_webhook_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/hooks/{hook_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryWebhookLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'uuid' in local_var_params:
            query_params.append(('uuid', local_var_params['uuid']))
        if 'created_after' in local_var_params:
            query_params.append(('created_after', local_var_params['created_after']))
        if 'created_before' in local_var_params:
            query_params.append(('created_before', local_var_params['created_before']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Total", ]

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

    def list_repository_webhooks_async(self, request):
        r"""获取仓库下Webhook列表

        获取仓库下Webhook列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryWebhooks
        :type request: :class:`huaweicloudsdkcodehub.v4.ListRepositoryWebhooksRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ListRepositoryWebhooksResponse`
        """
        http_info = self._list_repository_webhooks_http_info(request)
        return self._call_api(**http_info)

    def list_repository_webhooks_async_invoker(self, request):
        http_info = self._list_repository_webhooks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_repository_webhooks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/hooks",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryWebhooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']

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

        response_headers = ["X-Total", ]

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

    def remove_group_webhook_async(self, request):
        r"""删除代码组下单个Webhook

        删除代码组下单个Webhook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveGroupWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.RemoveGroupWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.RemoveGroupWebhookResponse`
        """
        http_info = self._remove_group_webhook_http_info(request)
        return self._call_api(**http_info)

    def remove_group_webhook_async_invoker(self, request):
        http_info = self._remove_group_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_group_webhook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/groups/{group_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveGroupWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def remove_project_webhook_async(self, request):
        r"""删除项目下单个Webhook

        删除项目下单个Webhook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveProjectWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.RemoveProjectWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.RemoveProjectWebhookResponse`
        """
        http_info = self._remove_project_webhook_http_info(request)
        return self._call_api(**http_info)

    def remove_project_webhook_async_invoker(self, request):
        http_info = self._remove_project_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_project_webhook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/projects/{project_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveProjectWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def remove_repository_webhook_async(self, request):
        r"""删除仓库下单个Webhook

        删除仓库下单个Webhook
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemoveRepositoryWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.RemoveRepositoryWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.RemoveRepositoryWebhookResponse`
        """
        http_info = self._remove_repository_webhook_http_info(request)
        return self._call_api(**http_info)

    def remove_repository_webhook_async_invoker(self, request):
        http_info = self._remove_repository_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _remove_repository_webhook_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v4/repositories/{repository_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RemoveRepositoryWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def show_group_webhook_async(self, request):
        r"""获取代码组下单个Webhook数据

        获取代码组下单个Webhook数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupWebhookResponse`
        """
        http_info = self._show_group_webhook_http_info(request)
        return self._call_api(**http_info)

    def show_group_webhook_async_invoker(self, request):
        http_info = self._show_group_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_webhook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def show_group_webhook_log_async(self, request):
        r"""获取代码组下指定Webhook的指定日志详情

        获取代码组下指定Webhook的指定日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGroupWebhookLog
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowGroupWebhookLogRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowGroupWebhookLogResponse`
        """
        http_info = self._show_group_webhook_log_http_info(request)
        return self._call_api(**http_info)

    def show_group_webhook_log_async_invoker(self, request):
        http_info = self._show_group_webhook_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_group_webhook_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/groups/{group_id}/hooks/{hook_id}/logs/{log_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGroupWebhookLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']
        if 'log_id' in local_var_params:
            path_params['log_id'] = local_var_params['log_id']

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

    def show_project_webhook_async(self, request):
        r"""获取项目下单个Webhook数据

        获取项目下单个Webhook数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectWebhookResponse`
        """
        http_info = self._show_project_webhook_http_info(request)
        return self._call_api(**http_info)

    def show_project_webhook_async_invoker(self, request):
        http_info = self._show_project_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_webhook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def show_project_webhook_log_async(self, request):
        r"""获取项目下指定Webhook的指定日志详情

        获取项目下指定Webhook的指定日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectWebhookLog
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowProjectWebhookLogRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowProjectWebhookLogResponse`
        """
        http_info = self._show_project_webhook_log_http_info(request)
        return self._call_api(**http_info)

    def show_project_webhook_log_async_invoker(self, request):
        http_info = self._show_project_webhook_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_webhook_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/projects/{project_id}/hooks/{hook_id}/logs/{log_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectWebhookLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']
        if 'log_id' in local_var_params:
            path_params['log_id'] = local_var_params['log_id']

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

    def show_repository_webhook_async(self, request):
        r"""获取仓库下单个Webhook数据

        获取仓库下单个Webhook数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryWebhookResponse`
        """
        http_info = self._show_repository_webhook_http_info(request)
        return self._call_api(**http_info)

    def show_repository_webhook_async_invoker(self, request):
        http_info = self._show_repository_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_webhook_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def show_repository_webhook_log_async(self, request):
        r"""获取仓库下指定Webhook的指定日志详情

        获取仓库下指定Webhook的指定日志详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepositoryWebhookLog
        :type request: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryWebhookLogRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.ShowRepositoryWebhookLogResponse`
        """
        http_info = self._show_repository_webhook_log_http_info(request)
        return self._call_api(**http_info)

    def show_repository_webhook_log_async_invoker(self, request):
        http_info = self._show_repository_webhook_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_repository_webhook_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v4/repositories/{repository_id}/hooks/{hook_id}/logs/{log_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryWebhookLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']
        if 'log_id' in local_var_params:
            path_params['log_id'] = local_var_params['log_id']

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

    def update_group_webhook_async(self, request):
        r"""更新代码组下单个Webhook数据

        更新代码组下单个Webhook数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGroupWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateGroupWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateGroupWebhookResponse`
        """
        http_info = self._update_group_webhook_http_info(request)
        return self._call_api(**http_info)

    def update_group_webhook_async_invoker(self, request):
        http_info = self._update_group_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_group_webhook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/groups/{group_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def update_project_webhook_async(self, request):
        r"""更新项目下单个Webhook数据

        更新项目下单个Webhook数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProjectWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateProjectWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateProjectWebhookResponse`
        """
        http_info = self._update_project_webhook_http_info(request)
        return self._call_api(**http_info)

    def update_project_webhook_async_invoker(self, request):
        http_info = self._update_project_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_project_webhook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/projects/{project_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

    def update_repository_webhook_async(self, request):
        r"""更新仓库下单个Webhook数据

        更新仓库下单个Webhook数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepositoryWebhook
        :type request: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryWebhookRequest`
        :rtype: :class:`huaweicloudsdkcodehub.v4.UpdateRepositoryWebhookResponse`
        """
        http_info = self._update_repository_webhook_http_info(request)
        return self._call_api(**http_info)

    def update_repository_webhook_async_invoker(self, request):
        http_info = self._update_repository_webhook_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_repository_webhook_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v4/repositories/{repository_id}/hooks/{hook_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepositoryWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'repository_id' in local_var_params:
            path_params['repository_id'] = local_var_params['repository_id']
        if 'hook_id' in local_var_params:
            path_params['hook_id'] = local_var_params['hook_id']

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

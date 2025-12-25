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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartsartifact'")


class CodeArtsArtifactClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsartifact.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsArtifactClient":
                raise TypeError("client type error, support client type is CodeArtsArtifactClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_delete_trashes(self, request):
        r"""批量删除回收站

        批量删除回收站
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTrashes
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.BatchDeleteTrashesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.BatchDeleteTrashesResponse`
        """
        http_info = self._batch_delete_trashes_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_trashes_invoker(self, request):
        http_info = self._batch_delete_trashes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_trashes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/cloudartifact/v5/trashes",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTrashesResponse"
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

    def batch_restore_repo(self, request):
        r"""批量还原回收站

        批量还原回收站
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRestoreRepo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.BatchRestoreRepoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.BatchRestoreRepoResponse`
        """
        http_info = self._batch_restore_repo_http_info(request)
        return self._call_api(**http_info)

    def batch_restore_repo_invoker(self, request):
        http_info = self._batch_restore_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_restore_repo_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/cloudartifact/v5/trashes",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestoreRepoResponse"
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

    def create_artifactory(self, request):
        r"""创建非maven仓库

        创建非maven仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateArtifactory
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.CreateArtifactoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.CreateArtifactoryResponse`
        """
        http_info = self._create_artifactory_http_info(request)
        return self._call_api(**http_info)

    def create_artifactory_invoker(self, request):
        http_info = self._create_artifactory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_artifactory_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/artifact/",
            "request_type": request.__class__.__name__,
            "response_type": "CreateArtifactoryResponse"
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

    def create_attention(self, request):
        r"""关注组件/取消关注组件

        关注组件/取消关注组件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAttention
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.CreateAttentionRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.CreateAttentionResponse`
        """
        http_info = self._create_attention_http_info(request)
        return self._call_api(**http_info)

    def create_attention_invoker(self, request):
        http_info = self._create_attention_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_attention_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/attention",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAttentionResponse"
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

    def create_docker_repositories(self, request):
        r"""创建docker仓库

        创建docker仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDockerRepositories
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.CreateDockerRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.CreateDockerRepositoriesResponse`
        """
        http_info = self._create_docker_repositories_http_info(request)
        return self._call_api(**http_info)

    def create_docker_repositories_invoker(self, request):
        http_info = self._create_docker_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_docker_repositories_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDockerRepositoriesResponse"
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

    def create_maven_repo(self, request):
        r"""创建maven仓库

        创建maven仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMavenRepo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.CreateMavenRepoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.CreateMavenRepoResponse`
        """
        http_info = self._create_maven_repo_http_info(request)
        return self._call_api(**http_info)

    def create_maven_repo_invoker(self, request):
        http_info = self._create_maven_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_maven_repo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/maven/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMavenRepoResponse"
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

    def create_project_related_repository(self, request):
        r"""创建项目关联仓库

        创建项目管理关联仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProjectRelatedRepository
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.CreateProjectRelatedRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.CreateProjectRelatedRepositoryResponse`
        """
        http_info = self._create_project_related_repository_http_info(request)
        return self._call_api(**http_info)

    def create_project_related_repository_invoker(self, request):
        http_info = self._create_project_related_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_related_repository_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/maven/project/repository",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectRelatedRepositoryResponse"
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

    def delete_artifact_file(self, request):
        r"""非maven删除文件

        非maven删除文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteArtifactFile
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.DeleteArtifactFileRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.DeleteArtifactFileResponse`
        """
        http_info = self._delete_artifact_file_http_info(request)
        return self._call_api(**http_info)

    def delete_artifact_file_invoker(self, request):
        http_info = self._delete_artifact_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_artifact_file_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/cloudartifact/v5/file",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteArtifactFileResponse"
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

    def delete_completely_update_file_state(self, request):
        r"""彻底删除文件/文件夹

        根据文件ID彻底删除文件或文件夹，删除后不能恢复，支持批量删除。可使用该接口清理不再需要的文件或文件夹以释放存储空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCompletelyUpdateFileState
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.DeleteCompletelyUpdateFileStateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.DeleteCompletelyUpdateFileStateResponse`
        """
        http_info = self._delete_completely_update_file_state_http_info(request)
        return self._call_api(**http_info)

    def delete_completely_update_file_state_invoker(self, request):
        http_info = self._delete_completely_update_file_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_completely_update_file_state_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/devreposerver/v5/files/compeletion",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCompletelyUpdateFileStateResponse"
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

    def delete_repository(self, request):
        r"""删除仓库到回收站

        删除仓库到回收站
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepository
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.DeleteRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.DeleteRepositoryResponse`
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
            "resource_path": "/cloudartifact/v5/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepositoryResponse"
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

    def list_all_repositories(self, request):
        r"""查询仓库详情，不会去统计仓库下的制品数量

        查询仓库详情，不会去统计仓库下的制品数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllRepositories
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListAllRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListAllRepositoriesResponse`
        """
        http_info = self._list_all_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_all_repositories_invoker(self, request):
        http_info = self._list_all_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_repositories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/{tenant_id}/{project_id}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'qname' in local_var_params:
            query_params.append(('qname', local_var_params['qname']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'format' in local_var_params:
            query_params.append(('format', local_var_params['format']))
        if 'format_list' in local_var_params:
            query_params.append(('format_list', local_var_params['format_list']))
        if 'is_recycle_bin' in local_var_params:
            query_params.append(('is_recycle_bin', local_var_params['is_recycle_bin']))
        if 'is_need_paging' in local_var_params:
            query_params.append(('is_need_paging', local_var_params['is_need_paging']))
        if 'in_project' in local_var_params:
            query_params.append(('in_project', local_var_params['in_project']))

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

    def list_artifactory_component(self, request):
        r"""查询仓库文件详情

        查询仓库文件详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListArtifactoryComponent
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListArtifactoryComponentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListArtifactoryComponentResponse`
        """
        http_info = self._list_artifactory_component_http_info(request)
        return self._call_api(**http_info)

    def list_artifactory_component_invoker(self, request):
        http_info = self._list_artifactory_component_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_artifactory_component_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/{tenant_id}/{project_id}/{repo_name}/file-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListArtifactoryComponentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repo_name' in local_var_params:
            path_params['repo_name'] = local_var_params['repo_name']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'format' in local_var_params:
            query_params.append(('format', local_var_params['format']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_artifactory_storage_statistic(self, request):
        r"""查询存储容量趋势

        查询存储容量趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListArtifactoryStorageStatistic
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListArtifactoryStorageStatisticRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListArtifactoryStorageStatisticResponse`
        """
        http_info = self._list_artifactory_storage_statistic_http_info(request)
        return self._call_api(**http_info)

    def list_artifactory_storage_statistic_invoker(self, request):
        http_info = self._list_artifactory_storage_statistic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_artifactory_storage_statistic_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/{tenant_id}/{project_id}/storageinfo/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListArtifactoryStorageStatisticResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'repo' in local_var_params:
            query_params.append(('repo', local_var_params['repo']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_attentions(self, request):
        r"""查询关注列表

        查询关注列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAttentions
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListAttentionsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListAttentionsResponse`
        """
        http_info = self._list_attentions_http_info(request)
        return self._call_api(**http_info)

    def list_attentions_invoker(self, request):
        http_info = self._list_attentions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_attentions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/attention/artifacts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAttentionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def list_capacity_message_setting(self, request):
        r"""查询租户容量消息通知设置信息

        查询租户容量消息通知设置，包含容量阈值和是否启用邮件通知等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCapacityMessageSetting
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListCapacityMessageSettingRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListCapacityMessageSettingResponse`
        """
        http_info = self._list_capacity_message_setting_http_info(request)
        return self._call_api(**http_info)

    def list_capacity_message_setting_invoker(self, request):
        http_info = self._list_capacity_message_setting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_capacity_message_setting_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/capacity-notice/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ListCapacityMessageSettingResponse"
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

    def list_child_proxy_repositories_list(self, request):
        r"""获取聚合仓下的仓库代理列表

        根据仓库ID获取指定聚合仓的仓库代理列表，包含仓库状态、类型、地址和访问路径白名单等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListChildProxyRepositoriesList
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListChildProxyRepositoriesListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListChildProxyRepositoriesListResponse`
        """
        http_info = self._list_child_proxy_repositories_list_http_info(request)
        return self._call_api(**http_info)

    def list_child_proxy_repositories_list_invoker(self, request):
        http_info = self._list_child_proxy_repositories_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_child_proxy_repositories_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/repositories/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "ListChildProxyRepositoriesListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'repo_id' in local_var_params:
            query_params.append(('repo_id', local_var_params['repo_id']))
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

    def list_domain_ip_config(self, request):
        r"""查询租户级IP白名单

        查询租户级IP白名单列表。在IP白名单的IP才能访问制品仓库，未配置IP白名单时，默认所有IP都可访问。该功能可用于保障制品仓库的安全，对访问IP进行严格控制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainIpConfig
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListDomainIpConfigRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListDomainIpConfigResponse`
        """
        http_info = self._list_domain_ip_config_http_info(request)
        return self._call_api(**http_info)

    def list_domain_ip_config_invoker(self, request):
        http_info = self._list_domain_ip_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_ip_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/domain/ipconfig",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainIpConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_file_build_archives(self, request):
        r"""分页查询构建归档包列表

        当归档包数量庞大时，分页查询构建归档包列表，包含文件名、文件大小、下载地址、MD5校验和、构建地址、构建代码分支等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFileBuildArchives
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListFileBuildArchivesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListFileBuildArchivesResponse`
        """
        http_info = self._list_file_build_archives_http_info(request)
        return self._call_api(**http_info)

    def list_file_build_archives_invoker(self, request):
        http_info = self._list_file_build_archives_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_file_build_archives_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/files/archives",
            "request_type": request.__class__.__name__,
            "response_type": "ListFileBuildArchivesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))
        if 'build_no' in local_var_params:
            query_params.append(('build_no', local_var_params['build_no']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'repo_branch' in local_var_params:
            query_params.append(('repo_branch', local_var_params['repo_branch']))

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

    def list_files(self, request):
        r"""查询文件/项目列表

        当项目或文件数量庞大时，分页查询项目或文件列表。可根据文件名、文件状态和文件的发布状态等参数进行过滤，从而快速找到所需文件，包含文件名、文件大小和下载地址等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFiles
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListFilesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListFilesResponse`
        """
        http_info = self._list_files_http_info(request)
        return self._call_api(**http_info)

    def list_files_invoker(self, request):
        http_info = self._list_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/devreposerver/v5/files/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListFilesResponse"
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

    def list_latest_version_files(self, request):
        r"""查询项目下所有文件的最新版本

        当项目文件数量庞大时，通过该接口可以分页查询项目下所有文件的最新版本，包含文件名、文件大小、文件状态和发布状态等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLatestVersionFiles
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListLatestVersionFilesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListLatestVersionFilesResponse`
        """
        http_info = self._list_latest_version_files_http_info(request)
        return self._call_api(**http_info)

    def list_latest_version_files_invoker(self, request):
        http_info = self._list_latest_version_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_latest_version_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/{project_id}/files/version",
            "request_type": request.__class__.__name__,
            "response_type": "ListLatestVersionFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort_by' in local_var_params:
            query_params.append(('sort_by', local_var_params['sort_by']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
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

    def list_maven_list(self, request):
        r"""查询Maven仓库列表

        查询Maven仓库列表，包含仓库状态、类型、地址和访问路径白名单等信息。支持根据项目ID和仓库ID等参数进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMavenList
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListMavenListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListMavenListResponse`
        """
        http_info = self._list_maven_list_http_info(request)
        return self._call_api(**http_info)

    def list_maven_list_invoker(self, request):
        http_info = self._list_maven_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_maven_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/maven/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListMavenListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'default' in local_var_params:
            query_params.append(('default', local_var_params['default']))
        if 'policy' in local_var_params:
            query_params.append(('policy', local_var_params['policy']))
        if 'repo_ids' in local_var_params:
            query_params.append(('repo_ids', local_var_params['repo_ids']))
        if 'access' in local_var_params:
            query_params.append(('access', local_var_params['access']))

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

    def list_maven_user(self, request):
        r"""查询私有库用户列表

        分页查询私有库用户列表，包含用户名和用户是否启用等信息。可根据用户名进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMavenUser
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListMavenUserRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListMavenUserResponse`
        """
        http_info = self._list_maven_user_http_info(request)
        return self._call_api(**http_info)

    def list_maven_user_invoker(self, request):
        http_info = self._list_maven_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_maven_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/repositories/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListMavenUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
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

    def list_net_proxy(self, request):
        r"""查询网络代理列表

        查询网络代理列表，返回代理源的访问地址及认证信息等，用于代理外部公开的制品资源。通过网络代理，开发人员可以安全、高效地访问所需的外部资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNetProxy
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListNetProxyRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListNetProxyResponse`
        """
        http_info = self._list_net_proxy_http_info(request)
        return self._call_api(**http_info)

    def list_net_proxy_invoker(self, request):
        http_info = self._list_net_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_net_proxy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/tree/net/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "ListNetProxyResponse"
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

    def list_project_role_permissions(self, request):
        r"""查看项目的角色权限设置

        查看项目的角色权限设置，包含上传下载、创建文件夹、清空或者还原回收站和更改软件包状态等设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectRolePermissions
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListProjectRolePermissionsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListProjectRolePermissionsResponse`
        """
        http_info = self._list_project_role_permissions_http_info(request)
        return self._call_api(**http_info)

    def list_project_role_permissions_invoker(self, request):
        http_info = self._list_project_role_permissions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_role_permissions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/project-role/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectRolePermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def list_project_users(self, request):
        r"""查询项目下的用户

        当项目中的用户数量较多时，分页查询指定项目下的用户列表，包含用户名和角色等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectUsers
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListProjectUsersRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListProjectUsersResponse`
        """
        http_info = self._list_project_users_http_info(request)
        return self._call_api(**http_info)

    def list_project_users_invoker(self, request):
        http_info = self._list_project_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/projects/{project_id}/users",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'repo_id' in local_var_params:
            query_params.append(('repo_id', local_var_params['repo_id']))
        if 'scene' in local_var_params:
            query_params.append(('scene', local_var_params['scene']))
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

    def list_sec_guard_list(self, request):
        r"""查询制品安全扫描任务列表

        分页查询制品安全扫描任务列表，包含扫描制品数量、漏洞数量、病毒文件数量和恶意代码文件数量等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSecGuardList
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ListSecGuardListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ListSecGuardListResponse`
        """
        http_info = self._list_sec_guard_list_http_info(request)
        return self._call_api(**http_info)

    def list_sec_guard_list_invoker(self, request):
        http_info = self._list_sec_guard_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sec_guard_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/sec-guard/task/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSecGuardListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))
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

    def modify_repository(self, request):
        r"""编辑仓库

        编辑仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyRepository
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ModifyRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ModifyRepositoryResponse`
        """
        http_info = self._modify_repository_http_info(request)
        return self._call_api(**http_info)

    def modify_repository_invoker(self, request):
        http_info = self._modify_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_repository_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/cloudartifact/v5/repositories/tab/{tab_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tab_id' in local_var_params:
            path_params['tab_id'] = local_var_params['tab_id']

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

    def reset_user_password(self, request):
        r"""重置用户密码

        重置用户密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetUserPassword
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ResetUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ResetUserPasswordResponse`
        """
        http_info = self._reset_user_password_http_info(request)
        return self._call_api(**http_info)

    def reset_user_password_invoker(self, request):
        http_info = self._reset_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_user_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/maven/users/me",
            "request_type": request.__class__.__name__,
            "response_type": "ResetUserPasswordResponse"
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

    def search_artifacts(self, request):
        r"""统筹搜索

        统筹搜索
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchArtifacts
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.SearchArtifactsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.SearchArtifactsResponse`
        """
        http_info = self._search_artifacts_http_info(request)
        return self._call_api(**http_info)

    def search_artifacts_invoker(self, request):
        http_info = self._search_artifacts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_artifacts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/cloudartifact/v5/tree/repos/artifacts",
            "request_type": request.__class__.__name__,
            "response_type": "SearchArtifactsResponse"
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

    def search_by_checksum(self, request):
        r"""通过checksum搜索文件

        通过checksum搜索文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchByChecksum
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.SearchByChecksumRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.SearchByChecksumResponse`
        """
        http_info = self._search_by_checksum_http_info(request)
        return self._call_api(**http_info)

    def search_by_checksum_invoker(self, request):
        http_info = self._search_by_checksum_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_by_checksum_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/search/checksum",
            "request_type": request.__class__.__name__,
            "response_type": "SearchByChecksumResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'checksum' in local_var_params:
            query_params.append(('checksum', local_var_params['checksum']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'format' in local_var_params:
            query_params.append(('format', local_var_params['format']))
        if 'in_project' in local_var_params:
            query_params.append(('in_project', local_var_params['in_project']))
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def show_audit(self, request):
        r"""查询仓库或文件的审计日志信息

        查询仓库或文件的审计日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAudit
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowAuditRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowAuditResponse`
        """
        http_info = self._show_audit_http_info(request)
        return self._call_api(**http_info)

    def show_audit_invoker(self, request):
        http_info = self._show_audit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/{tenant_id}/{project_id}/{module}/{repo}/audit",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'module' in local_var_params:
            path_params['module'] = local_var_params['module']
        if 'repo' in local_var_params:
            path_params['repo'] = local_var_params['repo']

        query_params = []
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_auto_delete_job_settings(self, request):
        r"""查询项目自动删除任务设置

        查询项目自动删除任务设置，包含文件的过期自动删除时间及删除规则。自动删除任务可以自动执行文件清理任务，减少管理员的工作负担，确保存储资源的有效利用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoDeleteJobSettings
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowAutoDeleteJobSettingsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowAutoDeleteJobSettingsResponse`
        """
        http_info = self._show_auto_delete_job_settings_http_info(request)
        return self._call_api(**http_info)

    def show_auto_delete_job_settings_invoker(self, request):
        http_info = self._show_auto_delete_job_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_delete_job_settings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/release/{project_id}/auto-deletion/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoDeleteJobSettingsResponse"
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

    def show_domain_release_repo_storage(self, request):
        r"""查询租户发布库存储容量

        查询租户发布库存储容量，包含已使用存储容量、最大存储容量、套餐类型和仓库数量等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainReleaseRepoStorage
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowDomainReleaseRepoStorageRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowDomainReleaseRepoStorageResponse`
        """
        http_info = self._show_domain_release_repo_storage_http_info(request)
        return self._call_api(**http_info)

    def show_domain_release_repo_storage_invoker(self, request):
        http_info = self._show_domain_release_repo_storage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_release_repo_storage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/storage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainReleaseRepoStorageResponse"
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

    def show_file_detail(self, request):
        r"""根据文件ID查询文件详情

        在日常数据管理工作中，根据文件ID查询指定文件详情，包含文件名、文件大小、下载地址、校验和、文件状态和发布状态等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFileDetail
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowFileDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowFileDetailResponse`
        """
        http_info = self._show_file_detail_http_info(request)
        return self._call_api(**http_info)

    def show_file_detail_invoker(self, request):
        http_info = self._show_file_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_file_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/files/{id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileDetailResponse"
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

    def show_file_detail_by_full_name(self, request):
        r"""根据文件完整路径查询文件详情

        在日常数据管理工作中，根据文件完整路径查询指定文件详情，包含文件名、文件大小、下载地址、校验和、文件状态和发布状态等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFileDetailByFullName
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowFileDetailByFullNameRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowFileDetailByFullNameResponse`
        """
        http_info = self._show_file_detail_by_full_name_http_info(request)
        return self._call_api(**http_info)

    def show_file_detail_by_full_name_invoker(self, request):
        http_info = self._show_file_detail_by_full_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_file_detail_by_full_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/files/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileDetailByFullNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))

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

    def show_file_tree(self, request):
        r"""查询仓库文件夹目录

        查询仓库文件夹目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFileTree
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowFileTreeRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowFileTreeResponse`
        """
        http_info = self._show_file_tree_http_info(request)
        return self._call_api(**http_info)

    def show_file_tree_invoker(self, request):
        http_info = self._show_file_tree_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_file_tree_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/{tenant_id}/{project_id}/{repo_name}/file-tree",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileTreeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repo_name' in local_var_params:
            path_params['repo_name'] = local_var_params['repo_name']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'is_recycle_bin' in local_var_params:
            query_params.append(('is_recycle_bin', local_var_params['is_recycle_bin']))

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

    def show_latest_version_files_count(self, request):
        r"""查询项目下所有文件的数量

        查询项目下所有文件的数量，该接口会识别所有文件的最新版本，从而提供准确的文件数量统计。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLatestVersionFilesCount
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowLatestVersionFilesCountRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowLatestVersionFilesCountResponse`
        """
        http_info = self._show_latest_version_files_count_http_info(request)
        return self._call_api(**http_info)

    def show_latest_version_files_count_invoker(self, request):
        http_info = self._show_latest_version_files_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_latest_version_files_count_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/{project_id}/files/version/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestVersionFilesCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def show_maven_info(self, request):
        r"""查询租户Maven仓库列表和账号密码

        查询租户Maven仓库列表和账号密码，支持跨租户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMavenInfo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowMavenInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowMavenInfoResponse`
        """
        http_info = self._show_maven_info_http_info(request)
        return self._call_api(**http_info)

    def show_maven_info_invoker(self, request):
        http_info = self._show_maven_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_maven_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/maven/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMavenInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'policy' in local_var_params:
            query_params.append(('policy', local_var_params['policy']))
        if 'access' in local_var_params:
            query_params.append(('access', local_var_params['access']))
        if 'default' in local_var_params:
            query_params.append(('default', local_var_params['default']))
        if 'ids' in local_var_params:
            query_params.append(('ids', local_var_params['ids']))

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

    def show_multi_roles_user_permissions(self, request):
        r"""查询多角色用户权限

        查询多角色用户权限，包含上传下载、创建文件夹、清空或者还原回收站和更改软件包状态等权限信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMultiRolesUserPermissions
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowMultiRolesUserPermissionsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowMultiRolesUserPermissionsResponse`
        """
        http_info = self._show_multi_roles_user_permissions_http_info(request)
        return self._call_api(**http_info)

    def show_multi_roles_user_permissions_invoker(self, request):
        http_info = self._show_multi_roles_user_permissions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_multi_roles_user_permissions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/user/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMultiRolesUserPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def show_open_source_enabled(self, request):
        r"""查询中心仓是否启用

        查询中心仓是否启用，用于确定当前局点是否具备中心仓功能，从而确保业务流程的顺利进行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOpenSourceEnabled
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowOpenSourceEnabledRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowOpenSourceEnabledResponse`
        """
        http_info = self._show_open_source_enabled_http_info(request)
        return self._call_api(**http_info)

    def show_open_source_enabled_invoker(self, request):
        http_info = self._show_open_source_enabled_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_open_source_enabled_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/opensource/enabled",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpenSourceEnabledResponse"
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

    def show_package_data_detail(self, request):
        r"""获取当前用户的套餐信息

        获取当前用户的套餐信息，包含总存储容量和已使用存储容量等信息，以便合理规划资源使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPackageDataDetail
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowPackageDataDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowPackageDataDetailResponse`
        """
        http_info = self._show_package_data_detail_http_info(request)
        return self._call_api(**http_info)

    def show_package_data_detail_invoker(self, request):
        http_info = self._show_package_data_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_package_data_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/data/package",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPackageDataDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def show_package_info(self, request):
        r"""获取当前用户的套餐状态

        获取当前用户的套餐状态，包含套餐扩展包的容量和流量规格，如资源类型、套餐状态、剩余天数等信息，帮助用户高效管理云资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPackageInfo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowPackageInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowPackageInfoResponse`
        """
        http_info = self._show_package_info_http_info(request)
        return self._call_api(**http_info)

    def show_package_info_invoker(self, request):
        http_info = self._show_package_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_package_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/data/package/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPackageInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def show_project_list(self, request):
        r"""查询项目管理关联仓库

        查询项目管理关联仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectList
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowProjectListRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowProjectListResponse`
        """
        http_info = self._show_project_list_http_info(request)
        return self._call_api(**http_info)

    def show_project_list_invoker(self, request):
        http_info = self._show_project_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/maven/repository/list",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))

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

    def show_project_release_files(self, request):
        r"""获取项目下文件版本信息列表

        获取项目下文件版本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectReleaseFiles
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowProjectReleaseFilesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowProjectReleaseFilesResponse`
        """
        http_info = self._show_project_release_files_http_info(request)
        return self._call_api(**http_info)

    def show_project_release_files_invoker(self, request):
        http_info = self._show_project_release_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_release_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/release/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectReleaseFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_project_storage_info(self, request):
        r"""查询项目下的制品存储容量信息

        查询项目下的制品存储容量，包含已使用存储容量和文件数量等信息。在项目管理中，可以使用该接口监控项目下的制品存储情况，以确保资源的有效利用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectStorageInfo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowProjectStorageInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowProjectStorageInfoResponse`
        """
        http_info = self._show_project_storage_info_http_info(request)
        return self._call_api(**http_info)

    def show_project_storage_info_invoker(self, request):
        http_info = self._show_project_storage_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_storage_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v5/{project_id}/storage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectStorageInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'parent_id' in local_var_params:
            query_params.append(('parent_id', local_var_params['parent_id']))

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

    def show_release_project_files(self, request):
        r"""获取项目下文件版本信息列表

        获取项目下文件版本信息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReleaseProjectFiles
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowReleaseProjectFilesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowReleaseProjectFilesResponse`
        """
        warnings.warn("Method 'show_release_project_files' of CodeArtsArtifactClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_release_project_files_http_info(request)
        return self._call_api(**http_info)

    def show_release_project_files_invoker(self, request):
        warnings.warn("Method 'show_release_project_files_invoker' of CodeArtsArtifactClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_release_project_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_release_project_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/devreposerver/v2/release/{project_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReleaseProjectFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_repo_user_info(self, request):
        r"""查询租户私有依赖库的账号密码

        在自动化构建场景，用户可调用该接口查询租户私有依赖库的账号密码，以便进行后续的上传下载操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepoUserInfo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowRepoUserInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowRepoUserInfoResponse`
        """
        http_info = self._show_repo_user_info_http_info(request)
        return self._call_api(**http_info)

    def show_repo_user_info_invoker(self, request):
        http_info = self._show_repo_user_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repo_user_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/repositories/user/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepoUserInfoResponse"
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

    def show_repository(self, request):
        r"""查询单个仓库详细信息，会去统计仓库下的制品数量

        查询单个仓库详细信息，会去统计仓库下的制品数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepository
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowRepositoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowRepositoryResponse`
        """
        http_info = self._show_repository_http_info(request)
        return self._call_api(**http_info)

    def show_repository_invoker(self, request):
        http_info = self._show_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/{tenant_id}/{project_id}/{repo_id}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'repo_id' in local_var_params:
            path_params['repo_id'] = local_var_params['repo_id']

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))

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

    def show_repository_info(self, request):
        r"""查看仓库信息

        查看仓库信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepositoryInfo
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowRepositoryInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowRepositoryInfoResponse`
        """
        http_info = self._show_repository_info_http_info(request)
        return self._call_api(**http_info)

    def show_repository_info_invoker(self, request):
        http_info = self._show_repository_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repository_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/repositories/{repo_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryInfoResponse"
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

    def show_storage(self, request):
        r"""仓库用量查询

        仓库用量查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStorage
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowStorageRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowStorageResponse`
        """
        http_info = self._show_storage_http_info(request)
        return self._call_api(**http_info)

    def show_storage_invoker(self, request):
        http_info = self._show_storage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_storage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/storage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStorageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'format_list' in local_var_params:
            query_params.append(('format_list', local_var_params['format_list']))
        if 'in_project' in local_var_params:
            query_params.append(('in_project', local_var_params['in_project']))

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

    def show_user_privileges(self, request):
        r"""查询用户在项目下的权限

        查询用户在项目下的权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserPrivileges
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowUserPrivilegesRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowUserPrivilegesResponse`
        """
        http_info = self._show_user_privileges_http_info(request)
        return self._call_api(**http_info)

    def show_user_privileges_invoker(self, request):
        http_info = self._show_user_privileges_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_privileges_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v3/user/{project_id}/privileges",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserPrivilegesResponse"
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

        auth_settings = ['apig-auth-iam-used-authn5']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_user_ticket(self, request):
        r"""查询用户凭证

        查询用户凭证，该凭证为IDC用户下载制品时使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserTicket
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.ShowUserTicketRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.ShowUserTicketResponse`
        """
        http_info = self._show_user_ticket_http_info(request)
        return self._call_api(**http_info)

    def show_user_ticket_invoker(self, request):
        http_info = self._show_user_ticket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_ticket_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/cloudartifact/v5/ticket",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserTicketResponse"
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

    def update_artifactory(self, request):
        r"""编辑非maven仓库信息

        编辑非maven仓库信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateArtifactory
        :type request: :class:`huaweicloudsdkcodeartsartifact.v2.UpdateArtifactoryRequest`
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.UpdateArtifactoryResponse`
        """
        http_info = self._update_artifactory_http_info(request)
        return self._call_api(**http_info)

    def update_artifactory_invoker(self, request):
        http_info = self._update_artifactory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_artifactory_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/cloudartifact/v5/artifact/",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateArtifactoryResponse"
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

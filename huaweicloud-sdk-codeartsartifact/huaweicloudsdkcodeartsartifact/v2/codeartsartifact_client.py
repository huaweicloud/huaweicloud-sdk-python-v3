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
        super(CodeArtsArtifactClient, self).__init__()
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

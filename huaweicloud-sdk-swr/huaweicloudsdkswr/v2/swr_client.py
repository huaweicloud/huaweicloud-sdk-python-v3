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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkswr'")


class SwrClient(Client):
    def __init__(self):
        super(SwrClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkswr.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SwrClient":
                raise TypeError("client type error, support client type is SwrClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_image_sync_repo(self, request):
        """创建镜像自动同步任务

        创建镜像自动同步任务，帮助您把最新推送的镜像自动同步到其他区域镜像仓库内。 镜像自动同步帮助您把最新推送的镜像自动同步到其他区域镜像仓库内，后期镜像有更新时，目标仓库的镜像也会自动更新，但已有的镜像不会自动同步。已有镜像的同步需要手动操作，详情请参见手动同步镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImageSyncRepo
        :type request: :class:`huaweicloudsdkswr.v2.CreateImageSyncRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateImageSyncRepoResponse`
        """
        http_info = self._create_image_sync_repo_http_info(request)
        return self._call_api(**http_info)

    def create_image_sync_repo_invoker(self, request):
        http_info = self._create_image_sync_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_image_sync_repo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/sync_repo",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageSyncRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def create_manual_image_sync_repo(self, request):
        """手动同步镜像

        对于镜像仓库已有的镜像，如果想在其他区域使用，需要手动触发镜像同步。 判断是否同步成功的方法如下：响应状态码为200，无报错信息，表示同步成功。通过SWR管理控制台或调用查询镜像仓库概要信息接口，在目标区域的目标组织下，若存在所同步的镜像版本表示同步成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateManualImageSyncRepo
        :type request: :class:`huaweicloudsdkswr.v2.CreateManualImageSyncRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateManualImageSyncRepoResponse`
        """
        http_info = self._create_manual_image_sync_repo_http_info(request)
        return self._call_api(**http_info)

    def create_manual_image_sync_repo_invoker(self, request):
        http_info = self._create_manual_image_sync_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_manual_image_sync_repo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/sync_images",
            "request_type": request.__class__.__name__,
            "response_type": "CreateManualImageSyncRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def create_namespace(self, request):
        """创建组织

        创建组织
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNamespace
        :type request: :class:`huaweicloudsdkswr.v2.CreateNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateNamespaceResponse`
        """
        http_info = self._create_namespace_http_info(request)
        return self._call_api(**http_info)

    def create_namespace_invoker(self, request):
        http_info = self._create_namespace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_namespace_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNamespaceResponse"
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

    def create_namespace_auth(self, request):
        """创建组织权限

        创建组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.CreateNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateNamespaceAuthResponse`
        """
        http_info = self._create_namespace_auth_http_info(request)
        return self._call_api(**http_info)

    def create_namespace_auth_invoker(self, request):
        http_info = self._create_namespace_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_namespace_auth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/access",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNamespaceAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def create_repo(self, request):
        """在组织下创建镜像仓库

        在组织下创建镜像仓库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRepo
        :type request: :class:`huaweicloudsdkswr.v2.CreateRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRepoResponse`
        """
        http_info = self._create_repo_http_info(request)
        return self._call_api(**http_info)

    def create_repo_invoker(self, request):
        http_info = self._create_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_repo_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def create_repo_domains(self, request):
        """创建共享帐号

        创建共享帐号。镜像上传后，您可以共享私有镜像给其他帐号，并授予下载该镜像的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.CreateRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRepoDomainsResponse`
        """
        http_info = self._create_repo_domains_http_info(request)
        return self._call_api(**http_info)

    def create_repo_domains_invoker(self, request):
        http_info = self._create_repo_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_repo_domains_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepoDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def create_retention(self, request):
        """创建镜像老化规则

        创建镜像老化规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRetention
        :type request: :class:`huaweicloudsdkswr.v2.CreateRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRetentionResponse`
        """
        http_info = self._create_retention_http_info(request)
        return self._call_api(**http_info)

    def create_retention_invoker(self, request):
        http_info = self._create_retention_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_retention_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/retentions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRetentionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def create_secret(self, request):
        """生成临时登录指令

        调用该接口，通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值，可生成临时登录指令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkswr.v2.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateSecretResponse`
        """
        http_info = self._create_secret_http_info(request)
        return self._call_api(**http_info)

    def create_secret_invoker(self, request):
        http_info = self._create_secret_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_secret_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/utils/secret",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSecretResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'projectname' in local_var_params:
            query_params.append(('projectname', local_var_params['projectname']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Swr-Dockerlogin", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_trigger(self, request):
        """创建触发器

        创建触发器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTrigger
        :type request: :class:`huaweicloudsdkswr.v2.CreateTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateTriggerResponse`
        """
        http_info = self._create_trigger_http_info(request)
        return self._call_api(**http_info)

    def create_trigger_invoker(self, request):
        http_info = self._create_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_trigger_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/triggers",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTriggerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def create_user_repository_auth(self, request):
        """创建镜像权限

        创建镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.CreateUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateUserRepositoryAuthResponse`
        """
        http_info = self._create_user_repository_auth_http_info(request)
        return self._call_api(**http_info)

    def create_user_repository_auth_invoker(self, request):
        http_info = self._create_user_repository_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_user_repository_auth_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/access",
            "request_type": request.__class__.__name__,
            "response_type": "CreateUserRepositoryAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def delete_image_sync_repo(self, request):
        """删除镜像自动同步任务

        根据目标区域、目标组织删除指定的镜像自动同步任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImageSyncRepo
        :type request: :class:`huaweicloudsdkswr.v2.DeleteImageSyncRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteImageSyncRepoResponse`
        """
        http_info = self._delete_image_sync_repo_http_info(request)
        return self._call_api(**http_info)

    def delete_image_sync_repo_invoker(self, request):
        http_info = self._delete_image_sync_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_image_sync_repo_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/sync_repo",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageSyncRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def delete_namespace_auth(self, request):
        """删除组织权限

        删除组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.DeleteNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteNamespaceAuthResponse`
        """
        http_info = self._delete_namespace_auth_http_info(request)
        return self._call_api(**http_info)

    def delete_namespace_auth_invoker(self, request):
        http_info = self._delete_namespace_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_namespace_auth_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/access",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNamespaceAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def delete_namespaces(self, request):
        """删除组织

        删除组织
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNamespaces
        :type request: :class:`huaweicloudsdkswr.v2.DeleteNamespacesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteNamespacesResponse`
        """
        http_info = self._delete_namespaces_http_info(request)
        return self._call_api(**http_info)

    def delete_namespaces_invoker(self, request):
        http_info = self._delete_namespaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_namespaces_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def delete_repo(self, request):
        """删除组织下的镜像仓库

        删除组织下的镜像仓库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepo
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRepoResponse`
        """
        http_info = self._delete_repo_http_info(request)
        return self._call_api(**http_info)

    def delete_repo_invoker(self, request):
        http_info = self._delete_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_repo_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def delete_repo_domains(self, request):
        """删除共享帐号

        删除共享帐号
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRepoDomainsResponse`
        """
        http_info = self._delete_repo_domains_http_info(request)
        return self._call_api(**http_info)

    def delete_repo_domains_invoker(self, request):
        http_info = self._delete_repo_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_repo_domains_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains/{access_domain}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepoDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'access_domain' in local_var_params:
            path_params['access_domain'] = local_var_params['access_domain']

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

    def delete_repo_tag(self, request):
        """删除指定tag的镜像

        删除镜像仓库中指定tag的镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRepoTag
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRepoTagRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRepoTagResponse`
        """
        http_info = self._delete_repo_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_repo_tag_invoker(self, request):
        http_info = self._delete_repo_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_repo_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/tags/{tag}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRepoTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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

    def delete_retention(self, request):
        """删除镜像老化规则

        删除镜像老化规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRetention
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRetentionResponse`
        """
        http_info = self._delete_retention_http_info(request)
        return self._call_api(**http_info)

    def delete_retention_invoker(self, request):
        http_info = self._delete_retention_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_retention_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/{retention_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRetentionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'retention_id' in local_var_params:
            path_params['retention_id'] = local_var_params['retention_id']

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

    def delete_trigger(self, request):
        """删除触发器

        删除触发器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTrigger
        :type request: :class:`huaweicloudsdkswr.v2.DeleteTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteTriggerResponse`
        """
        http_info = self._delete_trigger_http_info(request)
        return self._call_api(**http_info)

    def delete_trigger_invoker(self, request):
        http_info = self._delete_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_trigger_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/triggers/{trigger}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTriggerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'trigger' in local_var_params:
            path_params['trigger'] = local_var_params['trigger']

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

    def delete_user_repository_auth(self, request):
        """删除镜像权限

        删除镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.DeleteUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteUserRepositoryAuthResponse`
        """
        http_info = self._delete_user_repository_auth_http_info(request)
        return self._call_api(**http_info)

    def delete_user_repository_auth_invoker(self, request):
        http_info = self._delete_user_repository_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_user_repository_auth_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/access",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteUserRepositoryAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def list_image_auto_sync_repos_details(self, request):
        """获取镜像自动同步任务列表

        获取为当前镜像仓库所创建的所有自动同步任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImageAutoSyncReposDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListImageAutoSyncReposDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListImageAutoSyncReposDetailsResponse`
        """
        http_info = self._list_image_auto_sync_repos_details_http_info(request)
        return self._call_api(**http_info)

    def list_image_auto_sync_repos_details_invoker(self, request):
        http_info = self._list_image_auto_sync_repos_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_image_auto_sync_repos_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/sync_repo",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageAutoSyncReposDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def list_namespaces(self, request):
        """查询组织列表

        查询组织列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNamespaces
        :type request: :class:`huaweicloudsdkswr.v2.ListNamespacesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListNamespacesResponse`
        """
        http_info = self._list_namespaces_http_info(request)
        return self._call_api(**http_info)

    def list_namespaces_invoker(self, request):
        http_info = self._list_namespaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_namespaces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

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

    def list_quotas(self, request):
        """获取配额信息

        获取配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkswr.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/projects/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
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

    def list_repo_domains(self, request):
        """获取共享帐号列表

        获取共享帐号列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.ListRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRepoDomainsResponse`
        """
        http_info = self._list_repo_domains_http_info(request)
        return self._call_api(**http_info)

    def list_repo_domains_invoker(self, request):
        http_info = self._list_repo_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repo_domains_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepoDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def list_repos_details(self, request):
        """查询镜像仓库列表

        查询镜像仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListReposDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListReposDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListReposDetailsResponse`
        """
        http_info = self._list_repos_details_http_info(request)
        return self._call_api(**http_info)

    def list_repos_details_invoker(self, request):
        http_info = self._list_repos_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repos_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/repos",
            "request_type": request.__class__.__name__,
            "response_type": "ListReposDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_repository_tags(self, request):
        """查询镜像tag列表

        查询镜像tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepositoryTags
        :type request: :class:`huaweicloudsdkswr.v2.ListRepositoryTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRepositoryTagsResponse`
        """
        http_info = self._list_repository_tags_http_info(request)
        return self._call_api(**http_info)

    def list_repository_tags_invoker(self, request):
        http_info = self._list_repository_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repository_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_retention_histories(self, request):
        """获取镜像老化记录

        获取镜像老化记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRetentionHistories
        :type request: :class:`huaweicloudsdkswr.v2.ListRetentionHistoriesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRetentionHistoriesResponse`
        """
        http_info = self._list_retention_histories_http_info(request)
        return self._call_api(**http_info)

    def list_retention_histories_invoker(self, request):
        http_info = self._list_retention_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_retention_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListRetentionHistoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_retentions(self, request):
        """获取镜像老化规则列表

        获取镜像老化规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRetentions
        :type request: :class:`huaweicloudsdkswr.v2.ListRetentionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRetentionsResponse`
        """
        http_info = self._list_retentions_http_info(request)
        return self._call_api(**http_info)

    def list_retentions_invoker(self, request):
        http_info = self._list_retentions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_retentions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/retentions",
            "request_type": request.__class__.__name__,
            "response_type": "ListRetentionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def list_shared_repos_details(self, request):
        """查询共享镜像列表

        查询共享镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSharedReposDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListSharedReposDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListSharedReposDetailsResponse`
        """
        http_info = self._list_shared_repos_details_http_info(request)
        return self._call_api(**http_info)

    def list_shared_repos_details_invoker(self, request):
        http_info = self._list_shared_repos_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_shared_repos_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/shared-repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListSharedReposDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'center' in local_var_params:
            query_params.append(('center', local_var_params['center']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_triggers_details(self, request):
        """获取镜像仓库下的触发器列表

        获取镜像仓库下的触发器列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTriggersDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListTriggersDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListTriggersDetailsResponse`
        """
        http_info = self._list_triggers_details_http_info(request)
        return self._call_api(**http_info)

    def list_triggers_details_invoker(self, request):
        http_info = self._list_triggers_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_triggers_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/triggers",
            "request_type": request.__class__.__name__,
            "response_type": "ListTriggersDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def show_access_domain(self, request):
        """判断共享帐号是否存在

        判断共享租户是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAccessDomain
        :type request: :class:`huaweicloudsdkswr.v2.ShowAccessDomainRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowAccessDomainResponse`
        """
        http_info = self._show_access_domain_http_info(request)
        return self._call_api(**http_info)

    def show_access_domain_invoker(self, request):
        http_info = self._show_access_domain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_access_domain_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains/{access_domain}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAccessDomainResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'access_domain' in local_var_params:
            path_params['access_domain'] = local_var_params['access_domain']

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

    def show_namespace(self, request):
        """获取组织详情

        获取组织详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNamespace
        :type request: :class:`huaweicloudsdkswr.v2.ShowNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowNamespaceResponse`
        """
        http_info = self._show_namespace_http_info(request)
        return self._call_api(**http_info)

    def show_namespace_invoker(self, request):
        http_info = self._show_namespace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_namespace_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNamespaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def show_namespace_auth(self, request):
        """查询组织权限

        查询组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.ShowNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowNamespaceAuthResponse`
        """
        http_info = self._show_namespace_auth_http_info(request)
        return self._call_api(**http_info)

    def show_namespace_auth_invoker(self, request):
        http_info = self._show_namespace_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_namespace_auth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/access",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNamespaceAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def show_repository(self, request):
        """查询镜像仓库概要信息

        查询镜像仓库概要信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepository
        :type request: :class:`huaweicloudsdkswr.v2.ShowRepositoryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowRepositoryResponse`
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
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def show_retention(self, request):
        """获取镜像老化规则记录

        获取镜像老化规则记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRetention
        :type request: :class:`huaweicloudsdkswr.v2.ShowRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowRetentionResponse`
        """
        http_info = self._show_retention_http_info(request)
        return self._call_api(**http_info)

    def show_retention_invoker(self, request):
        http_info = self._show_retention_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_retention_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/{retention_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRetentionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'retention_id' in local_var_params:
            path_params['retention_id'] = local_var_params['retention_id']

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

    def show_sync_job(self, request):
        """获取镜像自动同步任务信息

        创建镜像自动同步任务后，可以通过此接口查询该任务的状态，以判断是否同步成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSyncJob
        :type request: :class:`huaweicloudsdkswr.v2.ShowSyncJobRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowSyncJobResponse`
        """
        http_info = self._show_sync_job_http_info(request)
        return self._call_api(**http_info)

    def show_sync_job_invoker(self, request):
        http_info = self._show_sync_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sync_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/sync_job",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSyncJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_trigger(self, request):
        """获取触发器详情

        获取触发器详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTrigger
        :type request: :class:`huaweicloudsdkswr.v2.ShowTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowTriggerResponse`
        """
        http_info = self._show_trigger_http_info(request)
        return self._call_api(**http_info)

    def show_trigger_invoker(self, request):
        http_info = self._show_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_trigger_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/triggers/{trigger}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTriggerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'trigger' in local_var_params:
            path_params['trigger'] = local_var_params['trigger']

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

    def show_user_repository_auth(self, request):
        """查询镜像权限

        查询镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.ShowUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowUserRepositoryAuthResponse`
        """
        http_info = self._show_user_repository_auth_http_info(request)
        return self._call_api(**http_info)

    def show_user_repository_auth_invoker(self, request):
        http_info = self._show_user_repository_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_user_repository_auth_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/access",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUserRepositoryAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def update_namespace_auth(self, request):
        """更新组织权限

        更新组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.UpdateNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateNamespaceAuthResponse`
        """
        http_info = self._update_namespace_auth_http_info(request)
        return self._call_api(**http_info)

    def update_namespace_auth_invoker(self, request):
        http_info = self._update_namespace_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_namespace_auth_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/manage/namespaces/{namespace}/access",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNamespaceAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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

    def update_repo(self, request):
        """更新镜像仓库的概要信息

        更新租户组织下的镜像概要信息，包括镜像类型、是否公有、描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRepo
        :type request: :class:`huaweicloudsdkswr.v2.UpdateRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRepoResponse`
        """
        http_info = self._update_repo_http_info(request)
        return self._call_api(**http_info)

    def update_repo_invoker(self, request):
        http_info = self._update_repo_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_repo_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def update_repo_domains(self, request):
        """更新共享帐号

        更新共享帐号
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsResponse`
        """
        http_info = self._update_repo_domains_http_info(request)
        return self._call_api(**http_info)

    def update_repo_domains_invoker(self, request):
        http_info = self._update_repo_domains_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_repo_domains_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains/{access_domain}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRepoDomainsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'access_domain' in local_var_params:
            path_params['access_domain'] = local_var_params['access_domain']

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

    def update_retention(self, request):
        """修改镜像老化规则

        修改镜像老化规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateRetention
        :type request: :class:`huaweicloudsdkswr.v2.UpdateRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRetentionResponse`
        """
        http_info = self._update_retention_http_info(request)
        return self._call_api(**http_info)

    def update_retention_invoker(self, request):
        http_info = self._update_retention_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_retention_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/{retention_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRetentionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'retention_id' in local_var_params:
            path_params['retention_id'] = local_var_params['retention_id']

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

    def update_trigger(self, request):
        """更新触发器配置

        更新触发器配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTrigger
        :type request: :class:`huaweicloudsdkswr.v2.UpdateTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateTriggerResponse`
        """
        http_info = self._update_trigger_http_info(request)
        return self._call_api(**http_info)

    def update_trigger_invoker(self, request):
        http_info = self._update_trigger_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_trigger_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/triggers/{trigger}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTriggerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']
        if 'trigger' in local_var_params:
            path_params['trigger'] = local_var_params['trigger']

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

    def update_user_repository_auth(self, request):
        """更新镜像权限

        更新镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.UpdateUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateUserRepositoryAuthResponse`
        """
        http_info = self._update_user_repository_auth_http_info(request)
        return self._call_api(**http_info)

    def update_user_repository_auth_invoker(self, request):
        http_info = self._update_user_repository_auth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_user_repository_auth_http_info(cls, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/access",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateUserRepositoryAuthResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

    def list_api_versions(self, request):
        """查询所有API版本信息

        查询所有API版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkswr.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
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

    def show_api_version(self, request):
        """查询指定API版本信息

        查询指定API版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkswr.v2.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowApiVersionResponse`
        """
        http_info = self._show_api_version_http_info(request)
        return self._call_api(**http_info)

    def show_api_version_invoker(self, request):
        http_info = self._show_api_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{api_version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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

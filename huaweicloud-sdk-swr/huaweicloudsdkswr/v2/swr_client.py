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

    def create_authorization_token(self, request):
        r"""生成增强型登录指令(新)

        调用该接口，通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值，可生成增强型登录指令,注：此接口只支持IAM新平面的调用方式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuthorizationToken
        :type request: :class:`huaweicloudsdkswr.v2.CreateAuthorizationTokenRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateAuthorizationTokenResponse`
        """
        http_info = self._create_authorization_token_http_info(request)
        return self._call_api(**http_info)

    def create_authorization_token_invoker(self, request):
        http_info = self._create_authorization_token_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_authorization_token_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/utils/authorizationtoken",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuthorizationTokenResponse"
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

        response_headers = ["X-Swr-Dockerlogin", "x-swr-expireat", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_image_sync_repo(self, request):
        r"""创建镜像自动同步任务

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
        r"""手动同步镜像

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
        r"""创建组织

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
        r"""创建组织权限

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
        r"""在组织下创建镜像仓库

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
        r"""创建共享帐号

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

    def create_repo_tag(self, request):
        r"""创建镜像tag

        创建镜像tag
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRepoTag
        :type request: :class:`huaweicloudsdkswr.v2.CreateRepoTagRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRepoTagResponse`
        """
        http_info = self._create_repo_tag_http_info(request)
        return self._call_api(**http_info)

    def create_repo_tag_invoker(self, request):
        http_info = self._create_repo_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_repo_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRepoTagResponse"
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
        r"""创建镜像老化规则

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
        r"""生成临时登录指令

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
        r"""创建触发器

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
        r"""创建镜像权限

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
        r"""删除镜像自动同步任务

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
        r"""删除组织权限

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
        r"""删除组织

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
        r"""删除组织下的镜像仓库

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
        r"""删除共享帐号

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
        r"""删除指定tag的镜像

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
        r"""删除镜像老化规则

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
        r"""删除触发器

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
        r"""删除镜像权限

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
        r"""获取镜像自动同步任务列表

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
        r"""查询组织列表

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
        r"""获取配额信息

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

    def list_repo_details(self, request):
        r"""查询镜像仓库列表详情

        查询镜像仓库列表详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepoDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListRepoDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRepoDetailsResponse`
        """
        http_info = self._list_repo_details_http_info(request)
        return self._call_api(**http_info)

    def list_repo_details_invoker(self, request):
        http_info = self._list_repo_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repo_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/manage/repos",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepoDetailsResponse"
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'is_public' in local_var_params:
            query_params.append(('is_public', local_var_params['is_public']))

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
        r"""获取共享帐号列表

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
        r"""查询镜像仓库列表

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

    def list_repository_tag(self, request):
        r"""查询镜像tag列表详情

        查询镜像tag列表详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRepositoryTag
        :type request: :class:`huaweicloudsdkswr.v2.ListRepositoryTagRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRepositoryTagResponse`
        """
        http_info = self._list_repository_tag_http_info(request)
        return self._call_api(**http_info)

    def list_repository_tag_invoker(self, request):
        http_info = self._list_repository_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_repository_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/manage/namespaces/{namespace}/repos/{repository}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListRepositoryTagResponse"
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
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'with_manifest' in local_var_params:
            query_params.append(('with_manifest', local_var_params['with_manifest']))

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

    def list_repository_tags(self, request):
        r"""查询镜像tag列表

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
        r"""获取镜像老化记录

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
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
        r"""获取镜像老化规则列表

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

    def list_shared_repo_details(self, request):
        r"""查询共享镜像列表详情

        查询共享镜像列表详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSharedRepoDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListSharedRepoDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListSharedRepoDetailsResponse`
        """
        http_info = self._list_shared_repo_details_http_info(request)
        return self._call_api(**http_info)

    def list_shared_repo_details_invoker(self, request):
        http_info = self._list_shared_repo_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_shared_repo_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/manage/shared-repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListSharedRepoDetailsResponse"
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
        if 'shared_by' in local_var_params:
            query_params.append(('shared_by', local_var_params['shared_by']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
        r"""查询共享镜像列表

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
        r"""获取镜像仓库下的触发器列表

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
        r"""判断共享帐号是否存在

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

    def show_domain_overview(self, request):
        r"""获取租户总览信息

        获取租户总览信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainOverview
        :type request: :class:`huaweicloudsdkswr.v2.ShowDomainOverviewRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowDomainOverviewResponse`
        """
        http_info = self._show_domain_overview_http_info(request)
        return self._call_api(**http_info)

    def show_domain_overview_invoker(self, request):
        http_info = self._show_domain_overview_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_overview_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainOverviewResponse"
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

    def show_domain_resource_reports(self, request):
        r"""获取租户资源统计信息

        获取租户资源统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainResourceReports
        :type request: :class:`huaweicloudsdkswr.v2.ShowDomainResourceReportsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowDomainResourceReportsResponse`
        """
        http_info = self._show_domain_resource_reports_http_info(request)
        return self._call_api(**http_info)

    def show_domain_resource_reports_invoker(self, request):
        http_info = self._show_domain_resource_reports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_resource_reports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/reports/{resource_type}/{frequency}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainResourceReportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'frequency' in local_var_params:
            path_params['frequency'] = local_var_params['frequency']

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
        r"""获取组织详情

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
        r"""查询组织权限

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

    def show_repo_tag(self, request):
        r"""查询指定tag的镜像详情

        查询镜像仓库中指定tag的镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRepoTag
        :type request: :class:`huaweicloudsdkswr.v2.ShowRepoTagRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowRepoTagResponse`
        """
        http_info = self._show_repo_tag_http_info(request)
        return self._call_api(**http_info)

    def show_repo_tag_invoker(self, request):
        http_info = self._show_repo_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repo_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/namespaces/{namespace}/repos/{repository}/tags/{tag}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRepoTagResponse"
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

    def show_repository(self, request):
        r"""查询镜像仓库概要信息

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
        r"""获取镜像老化规则记录

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

    def show_share_feature_gates(self, request):
        r"""查询服务特性开关信息

        查询服务特性开关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShareFeatureGates
        :type request: :class:`huaweicloudsdkswr.v2.ShowShareFeatureGatesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowShareFeatureGatesResponse`
        """
        http_info = self._show_share_feature_gates_http_info(request)
        return self._call_api(**http_info)

    def show_share_feature_gates_invoker(self, request):
        http_info = self._show_share_feature_gates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_share_feature_gates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/manage/projects/{project_id}/feature-gates",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShareFeatureGatesResponse"
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

    def show_sync_job(self, request):
        r"""获取镜像自动同步任务信息

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
        r"""获取触发器详情

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
        r"""查询镜像权限

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
        r"""更新组织权限

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
        r"""更新镜像仓库的概要信息

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
        r"""更新共享帐号

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
        r"""修改镜像老化规则

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
        r"""更新触发器配置

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
        r"""更新镜像权限

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
        r"""查询所有API版本信息

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
        r"""查询指定API版本信息

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

    def add_domain_name(self, request):
        r"""增加域名

        增加域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDomainName
        :type request: :class:`huaweicloudsdkswr.v2.AddDomainNameRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.AddDomainNameResponse`
        """
        http_info = self._add_domain_name_http_info(request)
        return self._call_api(**http_info)

    def add_domain_name_invoker(self, request):
        http_info = self._add_domain_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_domain_name_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/domainname",
            "request_type": request.__class__.__name__,
            "response_type": "AddDomainNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_immutable_rule(self, request):
        r"""创建不可变Tag策略

        创建不可变Tag策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImmutableRule
        :type request: :class:`huaweicloudsdkswr.v2.CreateImmutableRuleRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateImmutableRuleResponse`
        """
        http_info = self._create_immutable_rule_http_info(request)
        return self._call_api(**http_info)

    def create_immutable_rule_invoker(self, request):
        http_info = self._create_immutable_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_immutable_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/immutabletagrules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImmutableRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def create_instance(self, request):
        r"""创建实例

        创建企业仓库实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
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

    def create_instance_endpoint_policy(self, request):
        r"""开启或关闭公网访问

        开启或关闭公网访问
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceEndpointPolicy
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceEndpointPolicyResponse`
        """
        http_info = self._create_instance_endpoint_policy_http_info(request)
        return self._call_api(**http_info)

    def create_instance_endpoint_policy_invoker(self, request):
        http_info = self._create_instance_endpoint_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_endpoint_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/endpoint-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceEndpointPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_internal_endpoint(self, request):
        r"""新增内网访问

        新增内网访问
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceInternalEndpoint
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceInternalEndpointRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceInternalEndpointResponse`
        """
        http_info = self._create_instance_internal_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_instance_internal_endpoint_invoker(self, request):
        http_info = self._create_instance_internal_endpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_internal_endpoint_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/internal-endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceInternalEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_lt_credential(self, request):
        r"""创建长期访问凭证

        创建长期访问凭证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceLtCredential
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceLtCredentialRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceLtCredentialResponse`
        """
        http_info = self._create_instance_lt_credential_http_info(request)
        return self._call_api(**http_info)

    def create_instance_lt_credential_invoker(self, request):
        http_info = self._create_instance_lt_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_lt_credential_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/long-term-credential",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceLtCredentialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_namespace(self, request):
        r"""创建命名空间

        创建命名空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceNamespace
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceNamespaceResponse`
        """
        http_info = self._create_instance_namespace_http_info(request)
        return self._call_api(**http_info)

    def create_instance_namespace_invoker(self, request):
        http_info = self._create_instance_namespace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_namespace_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceNamespaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_registry(self, request):
        r"""创建镜像同步的目标仓库

        创建镜像同步的目标仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceRegistry
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceRegistryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceRegistryResponse`
        """
        http_info = self._create_instance_registry_http_info(request)
        return self._call_api(**http_info)

    def create_instance_registry_invoker(self, request):
        http_info = self._create_instance_registry_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_registry_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/registries",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceRegistryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_replication_policy(self, request):
        r"""创建镜像同步策略

        创建镜像同步策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceReplicationPolicy
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceReplicationPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceReplicationPolicyResponse`
        """
        http_info = self._create_instance_replication_policy_http_info(request)
        return self._call_api(**http_info)

    def create_instance_replication_policy_invoker(self, request):
        http_info = self._create_instance_replication_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_replication_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceReplicationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_resource_tags(self, request):
        r"""批量添加资源标签

        批量添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceResourceTags
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceResourceTagsResponse`
        """
        http_info = self._create_instance_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def create_instance_resource_tags_invoker(self, request):
        http_info = self._create_instance_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_resource_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def create_instance_retention_policy(self, request):
        r"""创建老化策略

        创建老化策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceRetentionPolicy
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceRetentionPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceRetentionPolicyResponse`
        """
        http_info = self._create_instance_retention_policy_http_info(request)
        return self._call_api(**http_info)

    def create_instance_retention_policy_invoker(self, request):
        http_info = self._create_instance_retention_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_retention_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceRetentionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def create_instance_sign_policy(self, request):
        r"""创建签名策略

        创建签名策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceSignPolicy
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceSignPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceSignPolicyResponse`
        """
        http_info = self._create_instance_sign_policy_http_info(request)
        return self._call_api(**http_info)

    def create_instance_sign_policy_invoker(self, request):
        http_info = self._create_instance_sign_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_sign_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceSignPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def create_instance_temp_credential(self, request):
        r"""获取临时访问凭证

        获取临时访问凭证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceTempCredential
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceTempCredentialRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceTempCredentialResponse`
        """
        http_info = self._create_instance_temp_credential_http_info(request)
        return self._call_api(**http_info)

    def create_instance_temp_credential_invoker(self, request):
        http_info = self._create_instance_temp_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_temp_credential_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/temp-credential",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceTempCredentialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def create_instance_webhook(self, request):
        r"""创建触发器策略

        创建触发器策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceWebhook
        :type request: :class:`huaweicloudsdkswr.v2.CreateInstanceWebhookRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateInstanceWebhookResponse`
        """
        http_info = self._create_instance_webhook_http_info(request)
        return self._call_api(**http_info)

    def create_instance_webhook_invoker(self, request):
        http_info = self._create_instance_webhook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_webhook_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/webhook/policies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def create_sub_resource_tags(self, request):
        r"""批量添加子资源标签

        批量添加子资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSubResourceTags
        :type request: :class:`huaweicloudsdkswr.v2.CreateSubResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateSubResourceTagsResponse`
        """
        http_info = self._create_sub_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def create_sub_resource_tags_invoker(self, request):
        http_info = self._create_sub_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sub_resource_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/{sub_resource_type}/{sub_resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'sub_resource_type' in local_var_params:
            path_params['sub_resource_type'] = local_var_params['sub_resource_type']
        if 'sub_resource_id' in local_var_params:
            path_params['sub_resource_id'] = local_var_params['sub_resource_id']

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

    def delete_domain_name(self, request):
        r"""删除域名

        删除域名，SWR企业仓库的默认域名无法删除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDomainName
        :type request: :class:`huaweicloudsdkswr.v2.DeleteDomainNameRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteDomainNameResponse`
        """
        http_info = self._delete_domain_name_http_info(request)
        return self._call_api(**http_info)

    def delete_domain_name_invoker(self, request):
        http_info = self._delete_domain_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_domain_name_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/domainname/{domainname_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDomainNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'domainname_id' in local_var_params:
            path_params['domainname_id'] = local_var_params['domainname_id']

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

    def delete_immutable_rule(self, request):
        r"""删除不可变Tag策略

        删除不可变Tag策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImmutableRule
        :type request: :class:`huaweicloudsdkswr.v2.DeleteImmutableRuleRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteImmutableRuleResponse`
        """
        http_info = self._delete_immutable_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_immutable_rule_invoker(self, request):
        http_info = self._delete_immutable_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_immutable_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/immutabletagrules/{immutable_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImmutableRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'immutable_rule_id' in local_var_params:
            path_params['immutable_rule_id'] = local_var_params['immutable_rule_id']

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

    def delete_instance(self, request):
        r"""删除实例

        删除实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_instance_artifact(self, request):
        r"""删除制品

        删除制品
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceArtifact
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceArtifactRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceArtifactResponse`
        """
        http_info = self._delete_instance_artifact_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_artifact_invoker(self, request):
        http_info = self._delete_instance_artifact_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_artifact_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}/artifacts/{reference}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceArtifactResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']
        if 'reference' in local_var_params:
            path_params['reference'] = local_var_params['reference']

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

    def delete_instance_internal_endpoint(self, request):
        r"""删除内网访问

        删除内网访问
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceInternalEndpoint
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceInternalEndpointRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceInternalEndpointResponse`
        """
        http_info = self._delete_instance_internal_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_internal_endpoint_invoker(self, request):
        http_info = self._delete_instance_internal_endpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_internal_endpoint_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/internal-endpoints/{internal_endpoints_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceInternalEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'internal_endpoints_id' in local_var_params:
            path_params['internal_endpoints_id'] = local_var_params['internal_endpoints_id']

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

    def delete_instance_job(self, request):
        r"""删除任务

        删除任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceJob
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceJobRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceJobResponse`
        """
        http_info = self._delete_instance_job_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_job_invoker(self, request):
        http_info = self._delete_instance_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def delete_instance_lt_credential(self, request):
        r"""删除长期访问凭证

        删除长期访问凭证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceLtCredential
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceLtCredentialRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceLtCredentialResponse`
        """
        http_info = self._delete_instance_lt_credential_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_lt_credential_invoker(self, request):
        http_info = self._delete_instance_lt_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_lt_credential_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/long-term-credentials/{credential_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceLtCredentialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'credential_id' in local_var_params:
            path_params['credential_id'] = local_var_params['credential_id']

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

    def delete_instance_namespace(self, request):
        r"""删除命名空间

        删除命名空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceNamespace
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceNamespaceResponse`
        """
        http_info = self._delete_instance_namespace_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_namespace_invoker(self, request):
        http_info = self._delete_instance_namespace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_namespace_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceNamespaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def delete_instance_registry(self, request):
        r"""删除镜像同步的目标仓库

        删除同步仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceRegistry
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceRegistryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceRegistryResponse`
        """
        http_info = self._delete_instance_registry_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_registry_invoker(self, request):
        http_info = self._delete_instance_registry_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_registry_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/registries/{registry_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceRegistryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'registry_id' in local_var_params:
            path_params['registry_id'] = local_var_params['registry_id']

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

    def delete_instance_replication_policy(self, request):
        r"""删除镜像同步策略

        删除镜像同步策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceReplicationPolicy
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceReplicationPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceReplicationPolicyResponse`
        """
        http_info = self._delete_instance_replication_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_replication_policy_invoker(self, request):
        http_info = self._delete_instance_replication_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_replication_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceReplicationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_instance_repository(self, request):
        r"""删除制品仓库

        删除仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceRepository
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceRepositoryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceRepositoryResponse`
        """
        http_info = self._delete_instance_repository_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_repository_invoker(self, request):
        http_info = self._delete_instance_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_repository_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_instance_resource_tags(self, request):
        r"""批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceResourceTags
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceResourceTagsResponse`
        """
        http_info = self._delete_instance_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_resource_tags_invoker(self, request):
        http_info = self._delete_instance_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_resource_tags_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def delete_instance_retention_policy(self, request):
        r"""删除老化策略

        删除老化策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceRetentionPolicy
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceRetentionPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceRetentionPolicyResponse`
        """
        http_info = self._delete_instance_retention_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_retention_policy_invoker(self, request):
        http_info = self._delete_instance_retention_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_retention_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceRetentionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_instance_sign_policy(self, request):
        r"""删除签名策略

        删除签名策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceSignPolicy
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceSignPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceSignPolicyResponse`
        """
        http_info = self._delete_instance_sign_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_sign_policy_invoker(self, request):
        http_info = self._delete_instance_sign_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_sign_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceSignPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_instance_webhook(self, request):
        r"""删除触发器策略

        删除触发器策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceWebhook
        :type request: :class:`huaweicloudsdkswr.v2.DeleteInstanceWebhookRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteInstanceWebhookResponse`
        """
        http_info = self._delete_instance_webhook_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_webhook_invoker(self, request):
        http_info = self._delete_instance_webhook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_webhook_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/webhook/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def delete_sub_resource_tags(self, request):
        r"""批量删除子资源标签

        批量删除子资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSubResourceTags
        :type request: :class:`huaweicloudsdkswr.v2.DeleteSubResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteSubResourceTagsResponse`
        """
        http_info = self._delete_sub_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def delete_sub_resource_tags_invoker(self, request):
        http_info = self._delete_sub_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sub_resource_tags_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/{sub_resource_type}/{sub_resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'sub_resource_type' in local_var_params:
            path_params['sub_resource_type'] = local_var_params['sub_resource_type']
        if 'sub_resource_id' in local_var_params:
            path_params['sub_resource_id'] = local_var_params['sub_resource_id']

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

    def execute_instance_replication_policy(self, request):
        r"""手动执行镜像同步策略

        手动执行同步策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteInstanceReplicationPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ExecuteInstanceReplicationPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ExecuteInstanceReplicationPolicyResponse`
        """
        http_info = self._execute_instance_replication_policy_http_info(request)
        return self._call_api(**http_info)

    def execute_instance_replication_policy_invoker(self, request):
        http_info = self._execute_instance_replication_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_instance_replication_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteInstanceReplicationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def execute_instance_retention_policy(self, request):
        r"""执行老化策略

        执行老化策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteInstanceRetentionPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ExecuteInstanceRetentionPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ExecuteInstanceRetentionPolicyResponse`
        """
        http_info = self._execute_instance_retention_policy_http_info(request)
        return self._call_api(**http_info)

    def execute_instance_retention_policy_invoker(self, request):
        http_info = self._execute_instance_retention_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_instance_retention_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteInstanceRetentionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def execute_instance_sign_policy(self, request):
        r"""手动执行签名策略

        手动执行签名策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteInstanceSignPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ExecuteInstanceSignPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ExecuteInstanceSignPolicyResponse`
        """
        http_info = self._execute_instance_sign_policy_http_info(request)
        return self._call_api(**http_info)

    def execute_instance_sign_policy_invoker(self, request):
        http_info = self._execute_instance_sign_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_instance_sign_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteInstanceSignPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_audit_logs(self, request):
        r"""获取上传下载的相关审计日志列表

        获取上传下载的相关审计日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditLogs
        :type request: :class:`huaweicloudsdkswr.v2.ListAuditLogsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListAuditLogsResponse`
        """
        http_info = self._list_audit_logs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_logs_invoker(self, request):
        http_info = self._list_audit_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/audit-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'operation' in local_var_params:
            query_params.append(('operation', local_var_params['operation']))
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

    def list_domain_names(self, request):
        r"""查询所有域名列表

        查询当前实例的所有域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainNames
        :type request: :class:`huaweicloudsdkswr.v2.ListDomainNamesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListDomainNamesResponse`
        """
        http_info = self._list_domain_names_http_info(request)
        return self._call_api(**http_info)

    def list_domain_names_invoker(self, request):
        http_info = self._list_domain_names_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_names_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/domainname",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'uid' in local_var_params:
            query_params.append(('uid', local_var_params['uid']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))

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

    def list_feature_gates(self, request):
        r"""查询特性开关信息

        查询特性开关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFeatureGates
        :type request: :class:`huaweicloudsdkswr.v2.ListFeatureGatesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListFeatureGatesResponse`
        """
        http_info = self._list_feature_gates_http_info(request)
        return self._call_api(**http_info)

    def list_feature_gates_invoker(self, request):
        http_info = self._list_feature_gates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_feature_gates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/feature-gates",
            "request_type": request.__class__.__name__,
            "response_type": "ListFeatureGatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_global_feature_gates(self, request):
        r"""查询全局特性开关信息

        查询全局特性开关信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalFeatureGates
        :type request: :class:`huaweicloudsdkswr.v2.ListGlobalFeatureGatesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListGlobalFeatureGatesResponse`
        """
        http_info = self._list_global_feature_gates_http_info(request)
        return self._call_api(**http_info)

    def list_global_feature_gates_invoker(self, request):
        http_info = self._list_global_feature_gates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_global_feature_gates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/feature-gates",
            "request_type": request.__class__.__name__,
            "response_type": "ListGlobalFeatureGatesResponse"
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

    def list_immutable_rules(self, request):
        r"""获取不可变Tag策略列表

        获取不可变Tag策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImmutableRules
        :type request: :class:`huaweicloudsdkswr.v2.ListImmutableRulesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListImmutableRulesResponse`
        """
        http_info = self._list_immutable_rules_http_info(request)
        return self._call_api(**http_info)

    def list_immutable_rules_invoker(self, request):
        http_info = self._list_immutable_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_immutable_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/immutabletagrules",
            "request_type": request.__class__.__name__,
            "response_type": "ListImmutableRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'namespace_id' in local_var_params:
            query_params.append(('namespace_id', local_var_params['namespace_id']))
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

    def list_instance(self, request):
        r"""查询实例列表

        查询实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceResponse`
        """
        http_info = self._list_instance_http_info(request)
        return self._call_api(**http_info)

    def list_instance_invoker(self, request):
        http_info = self._list_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def list_instance_accessories(self, request):
        r"""获取制品附件列表

        获取制品附件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceAccessories
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceAccessoriesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceAccessoriesResponse`
        """
        http_info = self._list_instance_accessories_http_info(request)
        return self._call_api(**http_info)

    def list_instance_accessories_invoker(self, request):
        http_info = self._list_instance_accessories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_accessories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}/artifacts/{reference}/accessories",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceAccessoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']
        if 'reference' in local_var_params:
            path_params['reference'] = local_var_params['reference']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_instance_all_artifacts(self, request):
        r"""获取仓库实例的所有制品版本列表

        获取仓库实例的所有制品版本列表（此接口只在企业仓库实例版本大于25.6.0以上的版本才支持）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceAllArtifacts
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceAllArtifactsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceAllArtifactsResponse`
        """
        http_info = self._list_instance_all_artifacts_http_info(request)
        return self._call_api(**http_info)

    def list_instance_all_artifacts_invoker(self, request):
        http_info = self._list_instance_all_artifacts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_all_artifacts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/artifacts",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceAllArtifactsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_instance_artifacts(self, request):
        r"""获取制品版本列表

        获取制品版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceArtifacts
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceArtifactsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceArtifactsResponse`
        """
        http_info = self._list_instance_artifacts_http_info(request)
        return self._call_api(**http_info)

    def list_instance_artifacts_invoker(self, request):
        http_info = self._list_instance_artifacts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_artifacts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}/artifacts",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceArtifactsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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

    def list_instance_internal_endpoints(self, request):
        r"""获取内网访问列表

        获取内网访问列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceInternalEndpoints
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceInternalEndpointsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceInternalEndpointsResponse`
        """
        http_info = self._list_instance_internal_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_instance_internal_endpoints_invoker(self, request):
        http_info = self._list_instance_internal_endpoints_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_internal_endpoints_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/internal-endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceInternalEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instance_jobs(self, request):
        r"""获取任务列表

        获取任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceJobs
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceJobsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceJobsResponse`
        """
        http_info = self._list_instance_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_instance_jobs_invoker(self, request):
        http_info = self._list_instance_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_instance_lt_credentials(self, request):
        r"""查询长期访问凭证列表

        查询长期访问凭证列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceLtCredentials
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceLtCredentialsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceLtCredentialsResponse`
        """
        http_info = self._list_instance_lt_credentials_http_info(request)
        return self._call_api(**http_info)

    def list_instance_lt_credentials_invoker(self, request):
        http_info = self._list_instance_lt_credentials_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_lt_credentials_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/long-term-credentials",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceLtCredentialsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instance_namespaces(self, request):
        r"""获取命名空间列表

        获取命名空间列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceNamespaces
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceNamespacesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceNamespacesResponse`
        """
        http_info = self._list_instance_namespaces_http_info(request)
        return self._call_api(**http_info)

    def list_instance_namespaces_invoker(self, request):
        http_info = self._list_instance_namespaces_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_namespaces_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceNamespacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'public' in local_var_params:
            query_params.append(('public', local_var_params['public']))

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

    def list_instance_project_tags(self, request):
        r"""查询项目下所有实例标签

        查询项目下所有实例标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceProjectTags
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceProjectTagsResponse`
        """
        http_info = self._list_instance_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_project_tags_invoker(self, request):
        http_info = self._list_instance_project_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_project_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceProjectTagsResponse"
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

    def list_instance_registries(self, request):
        r"""获取镜像同步的目标仓库列表

        获取镜像同步的目标仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceRegistries
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRegistriesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceRegistriesResponse`
        """
        http_info = self._list_instance_registries_http_info(request)
        return self._call_api(**http_info)

    def list_instance_registries_invoker(self, request):
        http_info = self._list_instance_registries_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_registries_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/registries",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceRegistriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def list_instance_replication_policies(self, request):
        r"""获取镜像同步策略列表

        获取镜像同步策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceReplicationPolicies
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPoliciesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPoliciesResponse`
        """
        http_info = self._list_instance_replication_policies_http_info(request)
        return self._call_api(**http_info)

    def list_instance_replication_policies_invoker(self, request):
        http_info = self._list_instance_replication_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_replication_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceReplicationPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'registry_id' in local_var_params:
            query_params.append(('registry_id', local_var_params['registry_id']))
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

    def list_instance_replication_policy_exec_sub_tasks(self, request):
        r"""获取镜像同步策略执行任务的镜像版本列表

        获取镜像同步策略执行任务的镜像版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceReplicationPolicyExecSubTasks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPolicyExecSubTasksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPolicyExecSubTasksResponse`
        """
        http_info = self._list_instance_replication_policy_exec_sub_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_replication_policy_exec_sub_tasks_invoker(self, request):
        http_info = self._list_instance_replication_policy_exec_sub_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_replication_policy_exec_sub_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/executions/{execution_id}/tasks/{task_id}/subtasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceReplicationPolicyExecSubTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_instance_replication_policy_exec_tasks(self, request):
        r"""获取镜像同步策略执行任务的镜像列表

        获取镜像同步策略执行任务的镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceReplicationPolicyExecTasks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPolicyExecTasksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPolicyExecTasksResponse`
        """
        http_info = self._list_instance_replication_policy_exec_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_replication_policy_exec_tasks_invoker(self, request):
        http_info = self._list_instance_replication_policy_exec_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_replication_policy_exec_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/executions/{execution_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceReplicationPolicyExecTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

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

    def list_instance_replication_policy_executions(self, request):
        r"""获取镜像同步策略执行记录列表

        获取镜像同步策略执行记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceReplicationPolicyExecutions
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPolicyExecutionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceReplicationPolicyExecutionsResponse`
        """
        http_info = self._list_instance_replication_policy_executions_http_info(request)
        return self._call_api(**http_info)

    def list_instance_replication_policy_executions_invoker(self, request):
        http_info = self._list_instance_replication_policy_executions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_replication_policy_executions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceReplicationPolicyExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'policy_id' in local_var_params:
            query_params.append(('policy_id', local_var_params['policy_id']))
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

    def list_instance_repositories(self, request):
        r"""获取制品仓库列表

        获取制品仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceRepositories
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceRepositoriesResponse`
        """
        http_info = self._list_instance_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_instance_repositories_invoker(self, request):
        http_info = self._list_instance_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_repositories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'namespace_id' in local_var_params:
            query_params.append(('namespace_id', local_var_params['namespace_id']))

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

    def list_instance_resource_instances(self, request):
        r"""按照标签检索资源列表

        按照标签检索资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceResourceInstances
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceResourceInstancesResponse`
        """
        http_info = self._list_instance_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instance_resource_instances_invoker(self, request):
        http_info = self._list_instance_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceResourceInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_instance_resource_tags(self, request):
        r"""查询资源标签

        查询资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceResourceTags
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceResourceTagsResponse`
        """
        http_info = self._list_instance_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_resource_tags_invoker(self, request):
        http_info = self._list_instance_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def list_instance_retention_policies(self, request):
        r"""获取老化策略列表

        获取老化策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceRetentionPolicies
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPoliciesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPoliciesResponse`
        """
        http_info = self._list_instance_retention_policies_http_info(request)
        return self._call_api(**http_info)

    def list_instance_retention_policies_invoker(self, request):
        http_info = self._list_instance_retention_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_retention_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/retention/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceRetentionPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'namespace_id' in local_var_params:
            query_params.append(('namespace_id', local_var_params['namespace_id']))
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

    def list_instance_retention_policy_exec_sub_tasks(self, request):
        r"""获取老化策略执行任务的镜像版本列表

        获取老化策略执行任务的镜像版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceRetentionPolicyExecSubTasks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPolicyExecSubTasksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPolicyExecSubTasksResponse`
        """
        http_info = self._list_instance_retention_policy_exec_sub_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_retention_policy_exec_sub_tasks_invoker(self, request):
        http_info = self._list_instance_retention_policy_exec_sub_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_retention_policy_exec_sub_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}/executions/{execution_id}/tasks/{task_id}/subtasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceRetentionPolicyExecSubTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_instance_retention_policy_exec_tasks(self, request):
        r"""获取老化策略执行任务的镜像列表

        获取老化策略执行任务的镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceRetentionPolicyExecTasks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPolicyExecTasksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPolicyExecTasksResponse`
        """
        http_info = self._list_instance_retention_policy_exec_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_retention_policy_exec_tasks_invoker(self, request):
        http_info = self._list_instance_retention_policy_exec_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_retention_policy_exec_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}/executions/{execution_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceRetentionPolicyExecTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_instance_retention_policy_executions(self, request):
        r"""获取老化策略执行记录列表

        获取老化策略执行记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceRetentionPolicyExecutions
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPolicyExecutionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceRetentionPolicyExecutionsResponse`
        """
        http_info = self._list_instance_retention_policy_executions_http_info(request)
        return self._call_api(**http_info)

    def list_instance_retention_policy_executions_invoker(self, request):
        http_info = self._list_instance_retention_policy_executions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_retention_policy_executions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceRetentionPolicyExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_instance_sign_policies(self, request):
        r"""获取签名策略列表

        获取签名策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceSignPolicies
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceSignPoliciesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceSignPoliciesResponse`
        """
        http_info = self._list_instance_sign_policies_http_info(request)
        return self._call_api(**http_info)

    def list_instance_sign_policies_invoker(self, request):
        http_info = self._list_instance_sign_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_sign_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/signature/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSignPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instance_sign_policy_exec_tasks(self, request):
        r"""获取签名执行记录任务的镜像列表

        获取签名执行记录任务的镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceSignPolicyExecTasks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceSignPolicyExecTasksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceSignPolicyExecTasksResponse`
        """
        http_info = self._list_instance_sign_policy_exec_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_sign_policy_exec_tasks_invoker(self, request):
        http_info = self._list_instance_sign_policy_exec_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_sign_policy_exec_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}/executions/{execution_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSignPolicyExecTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

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

    def list_instance_sign_policy_executions(self, request):
        r"""获取签名执行记录列表

        获取签名执行记录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceSignPolicyExecutions
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceSignPolicyExecutionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceSignPolicyExecutionsResponse`
        """
        http_info = self._list_instance_sign_policy_executions_http_info(request)
        return self._call_api(**http_info)

    def list_instance_sign_policy_executions_invoker(self, request):
        http_info = self._list_instance_sign_policy_executions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_sign_policy_executions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}/executions",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSignPolicyExecutionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def list_instance_signature_execution_subtasks(self, request):
        r"""获取签名策略执行任务的镜像版本列表

        获取签名策略执行任务的镜像版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceSignatureExecutionSubtasks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceSignatureExecutionSubtasksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceSignatureExecutionSubtasksResponse`
        """
        http_info = self._list_instance_signature_execution_subtasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_signature_execution_subtasks_invoker(self, request):
        http_info = self._list_instance_signature_execution_subtasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_signature_execution_subtasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}/executions/{execution_id}/tasks/{task_id}/subtasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSignatureExecutionSubtasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_instance_statistics(self, request):
        r"""获取实例统计数据

        获取实例统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceStatistics
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceStatisticsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceStatisticsResponse`
        """
        http_info = self._list_instance_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_instance_statistics_invoker(self, request):
        http_info = self._list_instance_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_instance_tags(self, request):
        r"""获取制品仓库的Tag列表

        获取制品仓库的Tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceTagsResponse`
        """
        http_info = self._list_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_tags_invoker(self, request):
        http_info = self._list_instance_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'is_accessory' in local_var_params:
            query_params.append(('is_accessory', local_var_params['is_accessory']))

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

    def list_instance_webhook_jobs(self, request):
        r"""获取触发器执行任务列表

        获取触发器执行任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceWebhookJobs
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceWebhookJobsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceWebhookJobsResponse`
        """
        http_info = self._list_instance_webhook_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_instance_webhook_jobs_invoker(self, request):
        http_info = self._list_instance_webhook_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_webhook_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/webhook/policies/{policy_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceWebhookJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_instance_webhooks(self, request):
        r"""获取触发器策略列表

        获取触发器策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceWebhooks
        :type request: :class:`huaweicloudsdkswr.v2.ListInstanceWebhooksRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListInstanceWebhooksResponse`
        """
        http_info = self._list_instance_webhooks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_webhooks_invoker(self, request):
        http_info = self._list_instance_webhooks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_webhooks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/webhook/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceWebhooksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'namespace_id' in local_var_params:
            query_params.append(('namespace_id', local_var_params['namespace_id']))
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

    def list_namespace_repositories(self, request):
        r"""获取命名空间下所有制品仓库列表

        获取命名空间下所有制品仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNamespaceRepositories
        :type request: :class:`huaweicloudsdkswr.v2.ListNamespaceRepositoriesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListNamespaceRepositoriesResponse`
        """
        http_info = self._list_namespace_repositories_http_info(request)
        return self._call_api(**http_info)

    def list_namespace_repositories_invoker(self, request):
        http_info = self._list_namespace_repositories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_namespace_repositories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories",
            "request_type": request.__class__.__name__,
            "response_type": "ListNamespaceRepositoriesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))

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

    def list_namespace_tags(self, request):
        r"""查询实例下所有命名空间标签

        查询实例下所有命名空间标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNamespaceTags
        :type request: :class:`huaweicloudsdkswr.v2.ListNamespaceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListNamespaceTagsResponse`
        """
        http_info = self._list_namespace_tags_http_info(request)
        return self._call_api(**http_info)

    def list_namespace_tags_invoker(self, request):
        http_info = self._list_namespace_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_namespace_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces-tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListNamespaceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def list_sub_resource_instances(self, request):
        r"""按照标签检索子资源列表

        按照标签检索子资源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubResourceInstances
        :type request: :class:`huaweicloudsdkswr.v2.ListSubResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListSubResourceInstancesResponse`
        """
        http_info = self._list_sub_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_sub_resource_instances_invoker(self, request):
        http_info = self._list_sub_resource_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_resource_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/{sub_resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubResourceInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'sub_resource_type' in local_var_params:
            path_params['sub_resource_type'] = local_var_params['sub_resource_type']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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

    def list_sub_resource_tags(self, request):
        r"""查询子资源标签

        查询子资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubResourceTags
        :type request: :class:`huaweicloudsdkswr.v2.ListSubResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListSubResourceTagsResponse`
        """
        http_info = self._list_sub_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_sub_resource_tags_invoker(self, request):
        http_info = self._list_sub_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_resource_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/{sub_resource_type}/{sub_resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'sub_resource_type' in local_var_params:
            path_params['sub_resource_type'] = local_var_params['sub_resource_type']
        if 'sub_resource_id' in local_var_params:
            path_params['sub_resource_id'] = local_var_params['sub_resource_id']

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

    def show_instance(self, request):
        r"""获取实例详情

        获取实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceResponse`
        """
        http_info = self._show_instance_http_info(request)
        return self._call_api(**http_info)

    def show_instance_invoker(self, request):
        http_info = self._show_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_instance_artifact(self, request):
        r"""获取制品详情

        获取制品详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceArtifact
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceArtifactRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceArtifactResponse`
        """
        http_info = self._show_instance_artifact_http_info(request)
        return self._call_api(**http_info)

    def show_instance_artifact_invoker(self, request):
        http_info = self._show_instance_artifact_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_artifact_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}/artifacts/{reference}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceArtifactResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']
        if 'reference' in local_var_params:
            path_params['reference'] = local_var_params['reference']

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

    def show_instance_artifact_addition(self, request):
        r"""获取制品附加信息

        获取制品附加信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceArtifactAddition
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceArtifactAdditionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceArtifactAdditionResponse`
        """
        http_info = self._show_instance_artifact_addition_http_info(request)
        return self._call_api(**http_info)

    def show_instance_artifact_addition_invoker(self, request):
        http_info = self._show_instance_artifact_addition_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_artifact_addition_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}/artifacts/{reference}/additions/{addition}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceArtifactAdditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'repository_name' in local_var_params:
            path_params['repository_name'] = local_var_params['repository_name']
        if 'reference' in local_var_params:
            path_params['reference'] = local_var_params['reference']
        if 'addition' in local_var_params:
            path_params['addition'] = local_var_params['addition']

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

    def show_instance_configuration(self, request):
        r"""查看实例配置

        查看实例配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceConfiguration
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceConfigurationResponse`
        """
        http_info = self._show_instance_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_instance_configuration_invoker(self, request):
        http_info = self._show_instance_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_instance_endpoint_policy(self, request):
        r"""获取公网访问信息

        获取公网访问信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceEndpointPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceEndpointPolicyResponse`
        """
        http_info = self._show_instance_endpoint_policy_http_info(request)
        return self._call_api(**http_info)

    def show_instance_endpoint_policy_invoker(self, request):
        http_info = self._show_instance_endpoint_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_endpoint_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/endpoint-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceEndpointPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def show_instance_internal_endpoint(self, request):
        r"""查询内网访问详情

        查询内网访问详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceInternalEndpoint
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceInternalEndpointRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceInternalEndpointResponse`
        """
        http_info = self._show_instance_internal_endpoint_http_info(request)
        return self._call_api(**http_info)

    def show_instance_internal_endpoint_invoker(self, request):
        http_info = self._show_instance_internal_endpoint_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_internal_endpoint_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/internal-endpoints/{internal_endpoints_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceInternalEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'internal_endpoints_id' in local_var_params:
            path_params['internal_endpoints_id'] = local_var_params['internal_endpoints_id']

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

    def show_instance_job(self, request):
        r"""获取任务详情

        获取任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceJob
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceJobRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceJobResponse`
        """
        http_info = self._show_instance_job_http_info(request)
        return self._call_api(**http_info)

    def show_instance_job_invoker(self, request):
        http_info = self._show_instance_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def show_instance_namespace(self, request):
        r"""获取命名空间详情

        获取命名空间详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceNamespace
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceNamespaceResponse`
        """
        http_info = self._show_instance_namespace_http_info(request)
        return self._call_api(**http_info)

    def show_instance_namespace_invoker(self, request):
        http_info = self._show_instance_namespace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_namespace_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceNamespaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def show_instance_registry(self, request):
        r"""获取镜像同步的目标仓库详情

        获取镜像同步的目标仓库详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceRegistry
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceRegistryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceRegistryResponse`
        """
        http_info = self._show_instance_registry_http_info(request)
        return self._call_api(**http_info)

    def show_instance_registry_invoker(self, request):
        http_info = self._show_instance_registry_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_registry_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/registries/{registry_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceRegistryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'registry_id' in local_var_params:
            path_params['registry_id'] = local_var_params['registry_id']

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

    def show_instance_replication_policy(self, request):
        r"""获取镜像同步策略详情

        获取镜像同步策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceReplicationPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceReplicationPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceReplicationPolicyResponse`
        """
        http_info = self._show_instance_replication_policy_http_info(request)
        return self._call_api(**http_info)

    def show_instance_replication_policy_invoker(self, request):
        http_info = self._show_instance_replication_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_replication_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceReplicationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_instance_repository(self, request):
        r"""获取制品仓库详情

        获取制品仓库详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceRepository
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceRepositoryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceRepositoryResponse`
        """
        http_info = self._show_instance_repository_http_info(request)
        return self._call_api(**http_info)

    def show_instance_repository_invoker(self, request):
        http_info = self._show_instance_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_repository_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_resource_instances_count(self, request):
        r"""按照标签检索资源数量

        按照标签检索资源数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceResourceInstancesCount
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceResourceInstancesCountRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceResourceInstancesCountResponse`
        """
        http_info = self._show_instance_resource_instances_count_http_info(request)
        return self._call_api(**http_info)

    def show_instance_resource_instances_count_invoker(self, request):
        http_info = self._show_instance_resource_instances_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_resource_instances_count_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceResourceInstancesCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def show_instance_retention_policy(self, request):
        r"""获取老化策略详情

        获取老化策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceRetentionPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceRetentionPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceRetentionPolicyResponse`
        """
        http_info = self._show_instance_retention_policy_http_info(request)
        return self._call_api(**http_info)

    def show_instance_retention_policy_invoker(self, request):
        http_info = self._show_instance_retention_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_retention_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceRetentionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_instance_sign_policy(self, request):
        r"""获取签名策略详情

        获取签名策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceSignPolicy
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceSignPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceSignPolicyResponse`
        """
        http_info = self._show_instance_sign_policy_http_info(request)
        return self._call_api(**http_info)

    def show_instance_sign_policy_invoker(self, request):
        http_info = self._show_instance_sign_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_sign_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceSignPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_instance_webhook(self, request):
        r"""获取触发器策略详情

        获取触发器策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceWebhook
        :type request: :class:`huaweicloudsdkswr.v2.ShowInstanceWebhookRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowInstanceWebhookResponse`
        """
        http_info = self._show_instance_webhook_http_info(request)
        return self._call_api(**http_info)

    def show_instance_webhook_invoker(self, request):
        http_info = self._show_instance_webhook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_webhook_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/webhook/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def show_sub_resource_instances_count(self, request):
        r"""按照标签检索子资源数量

        按照标签检索子资源数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSubResourceInstancesCount
        :type request: :class:`huaweicloudsdkswr.v2.ShowSubResourceInstancesCountRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowSubResourceInstancesCountResponse`
        """
        http_info = self._show_sub_resource_instances_count_http_info(request)
        return self._call_api(**http_info)

    def show_sub_resource_instances_count_invoker(self, request):
        http_info = self._show_sub_resource_instances_count_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sub_resource_instances_count_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/{sub_resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSubResourceInstancesCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'sub_resource_type' in local_var_params:
            path_params['sub_resource_type'] = local_var_params['sub_resource_type']

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

    def stop_instance_replication_policy_execution(self, request):
        r"""停止镜像同步任务

        停止镜像同步任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopInstanceReplicationPolicyExecution
        :type request: :class:`huaweicloudsdkswr.v2.StopInstanceReplicationPolicyExecutionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.StopInstanceReplicationPolicyExecutionResponse`
        """
        http_info = self._stop_instance_replication_policy_execution_http_info(request)
        return self._call_api(**http_info)

    def stop_instance_replication_policy_execution_invoker(self, request):
        http_info = self._stop_instance_replication_policy_execution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_instance_replication_policy_execution_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/executions/{execution_id}",
            "request_type": request.__class__.__name__,
            "response_type": "StopInstanceReplicationPolicyExecutionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'execution_id' in local_var_params:
            path_params['execution_id'] = local_var_params['execution_id']

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

    def update_domain_name(self, request):
        r"""更新域名

        更新域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDomainName
        :type request: :class:`huaweicloudsdkswr.v2.UpdateDomainNameRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateDomainNameResponse`
        """
        http_info = self._update_domain_name_http_info(request)
        return self._call_api(**http_info)

    def update_domain_name_invoker(self, request):
        http_info = self._update_domain_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_domain_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/domainname/{domainname_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDomainNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'domainname_id' in local_var_params:
            path_params['domainname_id'] = local_var_params['domainname_id']

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

    def update_immutable_rule(self, request):
        r"""修改不可变Tag策略

        修改不可变Tag策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateImmutableRule
        :type request: :class:`huaweicloudsdkswr.v2.UpdateImmutableRuleRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateImmutableRuleResponse`
        """
        http_info = self._update_immutable_rule_http_info(request)
        return self._call_api(**http_info)

    def update_immutable_rule_invoker(self, request):
        http_info = self._update_immutable_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_immutable_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/immutabletagrules/{immutable_rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateImmutableRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'immutable_rule_id' in local_var_params:
            path_params['immutable_rule_id'] = local_var_params['immutable_rule_id']

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

    def update_instance_configuration(self, request):
        r"""修改实例配置

        修改实例配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfiguration
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceConfigurationResponse`
        """
        http_info = self._update_instance_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_instance_configuration_invoker(self, request):
        http_info = self._update_instance_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_instance_endpoint_policy(self, request):
        r"""更新公网访问白名单

        更新公网访问白名单，更新为全量更新方式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceEndpointPolicy
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceEndpointPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceEndpointPolicyResponse`
        """
        http_info = self._update_instance_endpoint_policy_http_info(request)
        return self._call_api(**http_info)

    def update_instance_endpoint_policy_invoker(self, request):
        http_info = self._update_instance_endpoint_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_endpoint_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/endpoint-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceEndpointPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def update_instance_lt_credential(self, request):
        r"""启用/停用长期访问凭证

        启用/停用长期访问凭证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceLtCredential
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceLtCredentialRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceLtCredentialResponse`
        """
        http_info = self._update_instance_lt_credential_http_info(request)
        return self._call_api(**http_info)

    def update_instance_lt_credential_invoker(self, request):
        http_info = self._update_instance_lt_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_lt_credential_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/long-term-credentials/{credential_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceLtCredentialResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'credential_id' in local_var_params:
            path_params['credential_id'] = local_var_params['credential_id']

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

    def update_instance_namespace(self, request):
        r"""修改命名空间

        修改命名空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceNamespace
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceNamespaceResponse`
        """
        http_info = self._update_instance_namespace_http_info(request)
        return self._call_api(**http_info)

    def update_instance_namespace_invoker(self, request):
        http_info = self._update_instance_namespace_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_namespace_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceNamespaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']

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

    def update_instance_registry(self, request):
        r"""修改镜像同步的目标仓库

        修改镜像同步的目标仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceRegistry
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceRegistryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceRegistryResponse`
        """
        http_info = self._update_instance_registry_http_info(request)
        return self._call_api(**http_info)

    def update_instance_registry_invoker(self, request):
        http_info = self._update_instance_registry_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_registry_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/registries/{registry_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceRegistryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'registry_id' in local_var_params:
            path_params['registry_id'] = local_var_params['registry_id']

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

    def update_instance_replication_policy(self, request):
        r"""修改镜像同步策略

        修改镜像同步策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceReplicationPolicy
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceReplicationPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceReplicationPolicyResponse`
        """
        http_info = self._update_instance_replication_policy_http_info(request)
        return self._call_api(**http_info)

    def update_instance_replication_policy_invoker(self, request):
        http_info = self._update_instance_replication_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_replication_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/replication/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceReplicationPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_instance_repository(self, request):
        r"""修改制品仓库

        修改制品仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceRepository
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceRepositoryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceRepositoryResponse`
        """
        http_info = self._update_instance_repository_http_info(request)
        return self._call_api(**http_info)

    def update_instance_repository_invoker(self, request):
        http_info = self._update_instance_repository_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_repository_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/repositories/{repository_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceRepositoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
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

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_retention_policy(self, request):
        r"""修改老化策略

        修改老化策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceRetentionPolicy
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceRetentionPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceRetentionPolicyResponse`
        """
        http_info = self._update_instance_retention_policy_http_info(request)
        return self._call_api(**http_info)

    def update_instance_retention_policy_invoker(self, request):
        http_info = self._update_instance_retention_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_retention_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/retention/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceRetentionPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_instance_sign_policy(self, request):
        r"""修改签名策略

        修改签名策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceSignPolicy
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceSignPolicyRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceSignPolicyResponse`
        """
        http_info = self._update_instance_sign_policy_http_info(request)
        return self._call_api(**http_info)

    def update_instance_sign_policy_invoker(self, request):
        http_info = self._update_instance_sign_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_sign_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/signature/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceSignPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

    def update_instance_webhook(self, request):
        r"""修改触发器策略

        修改触发器策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceWebhook
        :type request: :class:`huaweicloudsdkswr.v2.UpdateInstanceWebhookRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateInstanceWebhookResponse`
        """
        http_info = self._update_instance_webhook_http_info(request)
        return self._call_api(**http_info)

    def update_instance_webhook_invoker(self, request):
        http_info = self._update_instance_webhook_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_webhook_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/namespaces/{namespace_name}/webhook/policies/{policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceWebhookResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'namespace_name' in local_var_params:
            path_params['namespace_name'] = local_var_params['namespace_name']
        if 'policy_id' in local_var_params:
            path_params['policy_id'] = local_var_params['policy_id']

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

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


class SwrAsyncClient(Client):
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
        super(SwrAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkswr.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SwrClient":
            raise TypeError("client type error, support client type is SwrClient")

        return ClientBuilder(clazz)

    def create_image_sync_repo_async(self, request):
        """创建镜像自动同步任务

        创建镜像自动同步任务

        :param CreateImageSyncRepoRequest request
        :return: CreateImageSyncRepoResponse
        """
        return self.create_image_sync_repo_with_http_info(request)

    def create_image_sync_repo_with_http_info(self, request):
        """创建镜像自动同步任务

        创建镜像自动同步任务

        :param CreateImageSyncRepoRequest request
        :return: CreateImageSyncRepoResponse
        """

        all_params = ['namespace', 'repository', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/sync_repo',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateImageSyncRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_namespace_async(self, request):
        """创建组织

        创建组织

        :param CreateNamespaceRequest request
        :return: CreateNamespaceResponse
        """
        return self.create_namespace_with_http_info(request)

    def create_namespace_with_http_info(self, request):
        """创建组织

        创建组织

        :param CreateNamespaceRequest request
        :return: CreateNamespaceResponse
        """

        all_params = ['create_namespace_request_body']
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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNamespaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_namespace_auth_async(self, request):
        """创建组织权限

        创建组织权限

        :param CreateNamespaceAuthRequest request
        :return: CreateNamespaceAuthResponse
        """
        return self.create_namespace_auth_with_http_info(request)

    def create_namespace_auth_with_http_info(self, request):
        """创建组织权限

        创建组织权限

        :param CreateNamespaceAuthRequest request
        :return: CreateNamespaceAuthResponse
        """

        all_params = ['namespace', 'create_namespace_auth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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
            resource_path='/v2/manage/namespaces/{namespace}/access',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_repo_domains_async(self, request):
        """创建共享账号

        创建共享账号。镜像上传后，您可以共享私有镜像给其他帐号，并授予下载该镜像的权限。

        :param CreateRepoDomainsRequest request
        :return: CreateRepoDomainsResponse
        """
        return self.create_repo_domains_with_http_info(request)

    def create_repo_domains_with_http_info(self, request):
        """创建共享账号

        创建共享账号。镜像上传后，您可以共享私有镜像给其他帐号，并授予下载该镜像的权限。

        :param CreateRepoDomainsRequest request
        :return: CreateRepoDomainsResponse
        """

        all_params = ['namespace', 'repository', 'create_repo_domains_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_retention_async(self, request):
        """创建镜像老化规则

        创建镜像老化规则

        :param CreateRetentionRequest request
        :return: CreateRetentionResponse
        """
        return self.create_retention_with_http_info(request)

    def create_retention_with_http_info(self, request):
        """创建镜像老化规则

        创建镜像老化规则

        :param CreateRetentionRequest request
        :return: CreateRetentionResponse
        """

        all_params = ['namespace', 'repository', 'create_retention_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/retentions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_secret_async(self, request):
        """生成临时登录指令

        调用该接口，通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值，可生成临时登录指令。

        :param CreateSecretRequest request
        :return: CreateSecretResponse
        """
        return self.create_secret_with_http_info(request)

    def create_secret_with_http_info(self, request):
        """生成临时登录指令

        调用该接口，通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值，可生成临时登录指令。

        :param CreateSecretRequest request
        :return: CreateSecretResponse
        """

        all_params = ['projectname']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'projectname' in local_var_params:
            query_params.append(('projectname', local_var_params['projectname']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/utils/secret',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_trigger_async(self, request):
        """创建触发器

        创建触发器

        :param CreateTriggerRequest request
        :return: CreateTriggerResponse
        """
        return self.create_trigger_with_http_info(request)

    def create_trigger_with_http_info(self, request):
        """创建触发器

        创建触发器

        :param CreateTriggerRequest request
        :return: CreateTriggerResponse
        """

        all_params = ['namespace', 'repository', 'create_trigger_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/triggers',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_user_repository_auth_async(self, request):
        """创建镜像权限

        创建镜像权限

        :param CreateUserRepositoryAuthRequest request
        :return: CreateUserRepositoryAuthResponse
        """
        return self.create_user_repository_auth_with_http_info(request)

    def create_user_repository_auth_with_http_info(self, request):
        """创建镜像权限

        创建镜像权限

        :param CreateUserRepositoryAuthRequest request
        :return: CreateUserRepositoryAuthResponse
        """

        all_params = ['namespace', 'repository', 'create_user_repository_auth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/access',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_image_sync_repo_async(self, request):
        """删除镜像自动同步任务

        删除镜像自动同步任务

        :param DeleteImageSyncRepoRequest request
        :return: DeleteImageSyncRepoResponse
        """
        return self.delete_image_sync_repo_with_http_info(request)

    def delete_image_sync_repo_with_http_info(self, request):
        """删除镜像自动同步任务

        删除镜像自动同步任务

        :param DeleteImageSyncRepoRequest request
        :return: DeleteImageSyncRepoResponse
        """

        all_params = ['namespace', 'repository', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/sync_repo',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteImageSyncRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_namespace_auth_async(self, request):
        """删除组织权限

        删除组织权限

        :param DeleteNamespaceAuthRequest request
        :return: DeleteNamespaceAuthResponse
        """
        return self.delete_namespace_auth_with_http_info(request)

    def delete_namespace_auth_with_http_info(self, request):
        """删除组织权限

        删除组织权限

        :param DeleteNamespaceAuthRequest request
        :return: DeleteNamespaceAuthResponse
        """

        all_params = ['namespace', 'delete_namespace_auth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

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
            resource_path='/v2/manage/namespaces/{namespace}/access',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_namespaces_async(self, request):
        """删除组织

        删除组织

        :param DeleteNamespacesRequest request
        :return: DeleteNamespacesResponse
        """
        return self.delete_namespaces_with_http_info(request)

    def delete_namespaces_with_http_info(self, request):
        """删除组织

        删除组织

        :param DeleteNamespacesRequest request
        :return: DeleteNamespacesResponse
        """

        all_params = ['namespace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNamespacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_repo_async(self, request):
        """删除组织下的镜像仓库

        删除组织下的镜像仓库。

        :param DeleteRepoRequest request
        :return: DeleteRepoResponse
        """
        return self.delete_repo_with_http_info(request)

    def delete_repo_with_http_info(self, request):
        """删除组织下的镜像仓库

        删除组织下的镜像仓库。

        :param DeleteRepoRequest request
        :return: DeleteRepoResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_repo_domains_async(self, request):
        """删除共享账号

        删除共享账号

        :param DeleteRepoDomainsRequest request
        :return: DeleteRepoDomainsResponse
        """
        return self.delete_repo_domains_with_http_info(request)

    def delete_repo_domains_with_http_info(self, request):
        """删除共享账号

        删除共享账号

        :param DeleteRepoDomainsRequest request
        :return: DeleteRepoDomainsResponse
        """

        all_params = ['namespace', 'repository', 'access_domain']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains/{access_domain}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_repo_tag_async(self, request):
        """删除指定tag的镜像

        删除镜像仓库中指定tag的镜像

        :param DeleteRepoTagRequest request
        :return: DeleteRepoTagResponse
        """
        return self.delete_repo_tag_with_http_info(request)

    def delete_repo_tag_with_http_info(self, request):
        """删除指定tag的镜像

        删除镜像仓库中指定tag的镜像

        :param DeleteRepoTagRequest request
        :return: DeleteRepoTagResponse
        """

        all_params = ['namespace', 'repository', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/tags/{tag}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRepoTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_retention_async(self, request):
        """删除镜像老化规则

        删除镜像老化规则

        :param DeleteRetentionRequest request
        :return: DeleteRetentionResponse
        """
        return self.delete_retention_with_http_info(request)

    def delete_retention_with_http_info(self, request):
        """删除镜像老化规则

        删除镜像老化规则

        :param DeleteRetentionRequest request
        :return: DeleteRetentionResponse
        """

        all_params = ['namespace', 'repository', 'retention_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/{retention_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_trigger_async(self, request):
        """删除触发器

        删除触发器

        :param DeleteTriggerRequest request
        :return: DeleteTriggerResponse
        """
        return self.delete_trigger_with_http_info(request)

    def delete_trigger_with_http_info(self, request):
        """删除触发器

        删除触发器

        :param DeleteTriggerRequest request
        :return: DeleteTriggerResponse
        """

        all_params = ['namespace', 'repository', 'trigger']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/triggers/{trigger}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_user_repository_auth_async(self, request):
        """删除镜像权限

        删除镜像权限

        :param DeleteUserRepositoryAuthRequest request
        :return: DeleteUserRepositoryAuthResponse
        """
        return self.delete_user_repository_auth_with_http_info(request)

    def delete_user_repository_auth_with_http_info(self, request):
        """删除镜像权限

        删除镜像权限

        :param DeleteUserRepositoryAuthRequest request
        :return: DeleteUserRepositoryAuthResponse
        """

        all_params = ['namespace', 'repository', 'delete_user_repository_auth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/access',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_image_auto_sync_repos_details_async(self, request):
        """获取镜像自动同步任务列表

        获取镜像自动同步任务列表

        :param ListImageAutoSyncReposDetailsRequest request
        :return: ListImageAutoSyncReposDetailsResponse
        """
        return self.list_image_auto_sync_repos_details_with_http_info(request)

    def list_image_auto_sync_repos_details_with_http_info(self, request):
        """获取镜像自动同步任务列表

        获取镜像自动同步任务列表

        :param ListImageAutoSyncReposDetailsRequest request
        :return: ListImageAutoSyncReposDetailsResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/sync_repo',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListImageAutoSyncReposDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_namespaces_async(self, request):
        """查询组织列表

        查询组织列表

        :param ListNamespacesRequest request
        :return: ListNamespacesResponse
        """
        return self.list_namespaces_with_http_info(request)

    def list_namespaces_with_http_info(self, request):
        """查询组织列表

        查询组织列表

        :param ListNamespacesRequest request
        :return: ListNamespacesResponse
        """

        all_params = ['namespace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNamespacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_repo_domains_async(self, request):
        """获取共享账号列表

        获取共享账号列表

        :param ListRepoDomainsRequest request
        :return: ListRepoDomainsResponse
        """
        return self.list_repo_domains_with_http_info(request)

    def list_repo_domains_with_http_info(self, request):
        """获取共享账号列表

        获取共享账号列表

        :param ListRepoDomainsRequest request
        :return: ListRepoDomainsResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_repository_tags_async(self, request):
        """查询镜像tag列表

        查询镜像tag列表

        :param ListRepositoryTagsRequest request
        :return: ListRepositoryTagsResponse
        """
        return self.list_repository_tags_with_http_info(request)

    def list_repository_tags_with_http_info(self, request):
        """查询镜像tag列表

        查询镜像tag列表

        :param ListRepositoryTagsRequest request
        :return: ListRepositoryTagsResponse
        """

        all_params = ['namespace', 'repository', 'offset', 'limit', 'order_column', 'order_type', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_column' in local_var_params:
            query_params.append(('order_column', local_var_params['order_column']))
        if 'order_type' in local_var_params:
            query_params.append(('order_type', local_var_params['order_type']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRepositoryTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_retention_histories_async(self, request):
        """获取镜像老化记录

        获取镜像老化记录

        :param ListRetentionHistoriesRequest request
        :return: ListRetentionHistoriesResponse
        """
        return self.list_retention_histories_with_http_info(request)

    def list_retention_histories_with_http_info(self, request):
        """获取镜像老化记录

        获取镜像老化记录

        :param ListRetentionHistoriesRequest request
        :return: ListRetentionHistoriesResponse
        """

        all_params = ['namespace', 'repository', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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

        response_headers = ["Content-Range"]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRetentionHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_retentions_async(self, request):
        """获取镜像老化规则列表

        获取镜像老化规则列表

        :param ListRetentionsRequest request
        :return: ListRetentionsResponse
        """
        return self.list_retentions_with_http_info(request)

    def list_retentions_with_http_info(self, request):
        """获取镜像老化规则列表

        获取镜像老化规则列表

        :param ListRetentionsRequest request
        :return: ListRetentionsResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/retentions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRetentionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_triggers_details_async(self, request):
        """获取镜像仓库下的触发器列表

        获取镜像仓库下的触发器列表

        :param ListTriggersDetailsRequest request
        :return: ListTriggersDetailsResponse
        """
        return self.list_triggers_details_with_http_info(request)

    def list_triggers_details_with_http_info(self, request):
        """获取镜像仓库下的触发器列表

        获取镜像仓库下的触发器列表

        :param ListTriggersDetailsRequest request
        :return: ListTriggersDetailsResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/triggers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTriggersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_access_domain_async(self, request):
        """判断共享账号是否存在

        判断共享租户是否存在

        :param ShowAccessDomainRequest request
        :return: ShowAccessDomainResponse
        """
        return self.show_access_domain_with_http_info(request)

    def show_access_domain_with_http_info(self, request):
        """判断共享账号是否存在

        判断共享租户是否存在

        :param ShowAccessDomainRequest request
        :return: ShowAccessDomainResponse
        """

        all_params = ['namespace', 'repository', 'access_domain']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains/{access_domain}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAccessDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_namespace_async(self, request):
        """获取组织详情

        获取组织详情

        :param ShowNamespaceRequest request
        :return: ShowNamespaceResponse
        """
        return self.show_namespace_with_http_info(request)

    def show_namespace_with_http_info(self, request):
        """获取组织详情

        获取组织详情

        :param ShowNamespaceRequest request
        :return: ShowNamespaceResponse
        """

        all_params = ['namespace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNamespaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_namespace_auth_async(self, request):
        """查询组织权限

        查询组织权限

        :param ShowNamespaceAuthRequest request
        :return: ShowNamespaceAuthResponse
        """
        return self.show_namespace_auth_with_http_info(request)

    def show_namespace_auth_with_http_info(self, request):
        """查询组织权限

        查询组织权限

        :param ShowNamespaceAuthRequest request
        :return: ShowNamespaceAuthResponse
        """

        all_params = ['namespace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/access',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_repository_async(self, request):
        """查询镜像概要信息

        查询镜像概要信息

        :param ShowRepositoryRequest request
        :return: ShowRepositoryResponse
        """
        return self.show_repository_with_http_info(request)

    def show_repository_with_http_info(self, request):
        """查询镜像概要信息

        查询镜像概要信息

        :param ShowRepositoryRequest request
        :return: ShowRepositoryResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_retention_async(self, request):
        """获取镜像老化规则记录

        获取镜像老化规则记录

        :param ShowRetentionRequest request
        :return: ShowRetentionResponse
        """
        return self.show_retention_with_http_info(request)

    def show_retention_with_http_info(self, request):
        """获取镜像老化规则记录

        获取镜像老化规则记录

        :param ShowRetentionRequest request
        :return: ShowRetentionResponse
        """

        all_params = ['namespace', 'repository', 'retention_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/{retention_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_trigger_async(self, request):
        """获取触发器详情

        获取触发器详情

        :param ShowTriggerRequest request
        :return: ShowTriggerResponse
        """
        return self.show_trigger_with_http_info(request)

    def show_trigger_with_http_info(self, request):
        """获取触发器详情

        获取触发器详情

        :param ShowTriggerRequest request
        :return: ShowTriggerResponse
        """

        all_params = ['namespace', 'repository', 'trigger']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/triggers/{trigger}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_user_repository_auth_async(self, request):
        """查询镜像权限

        查询镜像权限

        :param ShowUserRepositoryAuthRequest request
        :return: ShowUserRepositoryAuthResponse
        """
        return self.show_user_repository_auth_with_http_info(request)

    def show_user_repository_auth_with_http_info(self, request):
        """查询镜像权限

        查询镜像权限

        :param ShowUserRepositoryAuthRequest request
        :return: ShowUserRepositoryAuthResponse
        """

        all_params = ['namespace', 'repository']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/access',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_repo_domains_async(self, request):
        """更新共享账号

        更新共享账号

        :param UpdateRepoDomainsRequest request
        :return: UpdateRepoDomainsResponse
        """
        return self.update_repo_domains_with_http_info(request)

    def update_repo_domains_with_http_info(self, request):
        """更新共享账号

        更新共享账号

        :param UpdateRepoDomainsRequest request
        :return: UpdateRepoDomainsResponse
        """

        all_params = ['namespace', 'repository', 'access_domain', 'update_repo_domains_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/manage/namespaces/{namespace}/repositories/{repository}/access-domains/{access_domain}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_retention_async(self, request):
        """修改镜像老化规则

        修改镜像老化规则

        :param UpdateRetentionRequest request
        :return: UpdateRetentionResponse
        """
        return self.update_retention_with_http_info(request)

    def update_retention_with_http_info(self, request):
        """修改镜像老化规则

        修改镜像老化规则

        :param UpdateRetentionRequest request
        :return: UpdateRetentionResponse
        """

        all_params = ['namespace', 'repository', 'retention_id', 'update_retention_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/retentions/{retention_id}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_trigger_async(self, request):
        """更新触发器配置

        更新触发器配置

        :param UpdateTriggerRequest request
        :return: UpdateTriggerResponse
        """
        return self.update_trigger_with_http_info(request)

    def update_trigger_with_http_info(self, request):
        """更新触发器配置

        更新触发器配置

        :param UpdateTriggerRequest request
        :return: UpdateTriggerResponse
        """

        all_params = ['namespace', 'repository', 'trigger', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/triggers/{trigger}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_user_repository_auth_async(self, request):
        """更新镜像权限

        更新镜像权限

        :param UpdateUserRepositoryAuthRequest request
        :return: UpdateUserRepositoryAuthResponse
        """
        return self.update_user_repository_auth_with_http_info(request)

    def update_user_repository_auth_with_http_info(self, request):
        """更新镜像权限

        更新镜像权限

        :param UpdateUserRepositoryAuthRequest request
        :return: UpdateUserRepositoryAuthResponse
        """

        all_params = ['namespace', 'repository', 'update_repository_auth_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']
        if 'repository' in local_var_params:
            path_params['repository'] = local_var_params['repository']

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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/access',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_api_version_async(self, request):
        """查询指定API版本信息

        查询指定API版本信息

        :param ShowApiVersionRequest request
        :return: ShowApiVersionResponse
        """
        return self.show_api_version_with_http_info(request)

    def show_api_version_with_http_info(self, request):
        """查询指定API版本信息

        查询指定API版本信息

        :param ShowApiVersionRequest request
        :return: ShowApiVersionResponse
        """

        all_params = ['api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/{api_version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApiVersionResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)

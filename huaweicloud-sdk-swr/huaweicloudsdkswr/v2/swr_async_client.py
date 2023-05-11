# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class SwrAsyncClient(Client):
    def __init__(self):
        super(SwrAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkswr.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SwrClient":
            raise TypeError("client type error, support client type is SwrClient")

        return ClientBuilder(clazz)

    def create_image_sync_repo_async(self, request):
        """创建镜像自动同步任务

        创建镜像自动同步任务，帮助您把最新推送的镜像自动同步到其他区域镜像仓库内。 镜像自动同步帮助您把最新推送的镜像自动同步到其他区域镜像仓库内，后期镜像有更新时，目标仓库的镜像也会自动更新，但已有的镜像不会自动同步。已有镜像的同步需要手动操作，详情请参见手动同步镜像。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImageSyncRepo
        :type request: :class:`huaweicloudsdkswr.v2.CreateImageSyncRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateImageSyncRepoResponse`
        """
        return self._create_image_sync_repo_with_http_info(request)

    def _create_image_sync_repo_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateImageSyncRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_manual_image_sync_repo_async(self, request):
        """手动同步镜像

        对于镜像仓库已有的镜像，如果想在其他区域使用，需要手动触发镜像同步。 判断是否同步成功的方法如下：响应状态码为200，无报错信息，表示同步成功。通过SWR管理控制台或调用查询镜像仓库概要信息接口，在目标区域的目标组织下，若存在所同步的镜像版本表示同步成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateManualImageSyncRepo
        :type request: :class:`huaweicloudsdkswr.v2.CreateManualImageSyncRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateManualImageSyncRepoResponse`
        """
        return self._create_manual_image_sync_repo_with_http_info(request)

    def _create_manual_image_sync_repo_with_http_info(self, request):
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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/sync_images',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateManualImageSyncRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_namespace_async(self, request):
        """创建组织

        创建组织
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNamespace
        :type request: :class:`huaweicloudsdkswr.v2.CreateNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateNamespaceResponse`
        """
        return self._create_namespace_with_http_info(request)

    def _create_namespace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNamespaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_namespace_auth_async(self, request):
        """创建组织权限

        创建组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.CreateNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateNamespaceAuthResponse`
        """
        return self._create_namespace_auth_with_http_info(request)

    def _create_namespace_auth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='CreateNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_repo_async(self, request):
        """在组织下创建镜像仓库

        在组织下创建镜像仓库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRepo
        :type request: :class:`huaweicloudsdkswr.v2.CreateRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRepoResponse`
        """
        return self._create_repo_with_http_info(request)

    def _create_repo_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/manage/namespaces/{namespace}/repos',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_repo_domains_async(self, request):
        """创建共享帐号

        创建共享帐号。镜像上传后，您可以共享私有镜像给其他帐号，并授予下载该镜像的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.CreateRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRepoDomainsResponse`
        """
        return self._create_repo_domains_with_http_info(request)

    def _create_repo_domains_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_retention_async(self, request):
        """创建镜像老化规则

        创建镜像老化规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRetention
        :type request: :class:`huaweicloudsdkswr.v2.CreateRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateRetentionResponse`
        """
        return self._create_retention_with_http_info(request)

    def _create_retention_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_secret_async(self, request):
        """生成临时登录指令

        调用该接口，通过获取响应消息头的X-Swr-Dockerlogin的值及响应消息体的host值，可生成临时登录指令。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecret
        :type request: :class:`huaweicloudsdkswr.v2.CreateSecretRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateSecretResponse`
        """
        return self._create_secret_with_http_info(request)

    def _create_secret_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        response_headers = ["X-Swr-Dockerlogin", ]

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
            cname=cname,
            response_type='CreateSecretResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_trigger_async(self, request):
        """创建触发器

        创建触发器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrigger
        :type request: :class:`huaweicloudsdkswr.v2.CreateTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateTriggerResponse`
        """
        return self._create_trigger_with_http_info(request)

    def _create_trigger_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_user_repository_auth_async(self, request):
        """创建镜像权限

        创建镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.CreateUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.CreateUserRepositoryAuthResponse`
        """
        return self._create_user_repository_auth_with_http_info(request)

    def _create_user_repository_auth_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_image_sync_repo_async(self, request):
        """删除镜像自动同步任务

        根据目标区域、目标组织删除指定的镜像自动同步任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteImageSyncRepo
        :type request: :class:`huaweicloudsdkswr.v2.DeleteImageSyncRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteImageSyncRepoResponse`
        """
        return self._delete_image_sync_repo_with_http_info(request)

    def _delete_image_sync_repo_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteImageSyncRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_namespace_auth_async(self, request):
        """删除组织权限

        删除组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.DeleteNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteNamespaceAuthResponse`
        """
        return self._delete_namespace_auth_with_http_info(request)

    def _delete_namespace_auth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeleteNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_namespaces_async(self, request):
        """删除组织

        删除组织
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNamespaces
        :type request: :class:`huaweicloudsdkswr.v2.DeleteNamespacesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteNamespacesResponse`
        """
        return self._delete_namespaces_with_http_info(request)

    def _delete_namespaces_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='DeleteNamespacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_repo_async(self, request):
        """删除组织下的镜像仓库

        删除组织下的镜像仓库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRepo
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRepoResponse`
        """
        return self._delete_repo_with_http_info(request)

    def _delete_repo_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_repo_domains_async(self, request):
        """删除共享帐号

        删除共享帐号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRepoDomainsResponse`
        """
        return self._delete_repo_domains_with_http_info(request)

    def _delete_repo_domains_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_repo_tag_async(self, request):
        """删除指定tag的镜像

        删除镜像仓库中指定tag的镜像
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRepoTag
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRepoTagRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRepoTagResponse`
        """
        return self._delete_repo_tag_with_http_info(request)

    def _delete_repo_tag_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteRepoTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_retention_async(self, request):
        """删除镜像老化规则

        删除镜像老化规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRetention
        :type request: :class:`huaweicloudsdkswr.v2.DeleteRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteRetentionResponse`
        """
        return self._delete_retention_with_http_info(request)

    def _delete_retention_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_trigger_async(self, request):
        """删除触发器

        删除触发器
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTrigger
        :type request: :class:`huaweicloudsdkswr.v2.DeleteTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteTriggerResponse`
        """
        return self._delete_trigger_with_http_info(request)

    def _delete_trigger_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_user_repository_auth_async(self, request):
        """删除镜像权限

        删除镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.DeleteUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.DeleteUserRepositoryAuthResponse`
        """
        return self._delete_user_repository_auth_with_http_info(request)

    def _delete_user_repository_auth_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image_auto_sync_repos_details_async(self, request):
        """获取镜像自动同步任务列表

        获取为当前镜像仓库所创建的所有自动同步任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImageAutoSyncReposDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListImageAutoSyncReposDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListImageAutoSyncReposDetailsResponse`
        """
        return self._list_image_auto_sync_repos_details_with_http_info(request)

    def _list_image_auto_sync_repos_details_with_http_info(self, request):
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
            cname=cname,
            response_type='ListImageAutoSyncReposDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_namespaces_async(self, request):
        """查询组织列表

        查询组织列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNamespaces
        :type request: :class:`huaweicloudsdkswr.v2.ListNamespacesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListNamespacesResponse`
        """
        return self._list_namespaces_with_http_info(request)

    def _list_namespaces_with_http_info(self, request):
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
            cname=cname,
            response_type='ListNamespacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quotas_async(self, request):
        """获取配额信息

        获取配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkswr.v2.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListQuotasResponse`
        """
        return self._list_quotas_with_http_info(request)

    def _list_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/projects/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_repo_domains_async(self, request):
        """获取共享帐号列表

        获取共享帐号列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.ListRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRepoDomainsResponse`
        """
        return self._list_repo_domains_with_http_info(request)

    def _list_repo_domains_with_http_info(self, request):
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
            cname=cname,
            response_type='ListRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_repos_details_async(self, request):
        """查询镜像仓库列表

        查询镜像仓库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListReposDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListReposDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListReposDetailsResponse`
        """
        return self._list_repos_details_with_http_info(request)

    def _list_repos_details_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/repos',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListReposDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_repository_tags_async(self, request):
        """查询镜像tag列表

        查询镜像tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRepositoryTags
        :type request: :class:`huaweicloudsdkswr.v2.ListRepositoryTagsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRepositoryTagsResponse`
        """
        return self._list_repository_tags_with_http_info(request)

    def _list_repository_tags_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Range", ]

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
            cname=cname,
            response_type='ListRepositoryTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_retention_histories_async(self, request):
        """获取镜像老化记录

        获取镜像老化记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRetentionHistories
        :type request: :class:`huaweicloudsdkswr.v2.ListRetentionHistoriesRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRetentionHistoriesResponse`
        """
        return self._list_retention_histories_with_http_info(request)

    def _list_retention_histories_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Range", ]

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
            cname=cname,
            response_type='ListRetentionHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_retentions_async(self, request):
        """获取镜像老化规则列表

        获取镜像老化规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRetentions
        :type request: :class:`huaweicloudsdkswr.v2.ListRetentionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListRetentionsResponse`
        """
        return self._list_retentions_with_http_info(request)

    def _list_retentions_with_http_info(self, request):
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
            cname=cname,
            response_type='ListRetentionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_shared_repos_details_async(self, request):
        """查询共享镜像列表

        查询共享镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSharedReposDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListSharedReposDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListSharedReposDetailsResponse`
        """
        return self._list_shared_repos_details_with_http_info(request)

    def _list_shared_repos_details_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/shared-repositories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSharedReposDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_triggers_details_async(self, request):
        """获取镜像仓库下的触发器列表

        获取镜像仓库下的触发器列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTriggersDetails
        :type request: :class:`huaweicloudsdkswr.v2.ListTriggersDetailsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListTriggersDetailsResponse`
        """
        return self._list_triggers_details_with_http_info(request)

    def _list_triggers_details_with_http_info(self, request):
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
            cname=cname,
            response_type='ListTriggersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_access_domain_async(self, request):
        """判断共享帐号是否存在

        判断共享租户是否存在
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAccessDomain
        :type request: :class:`huaweicloudsdkswr.v2.ShowAccessDomainRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowAccessDomainResponse`
        """
        return self._show_access_domain_with_http_info(request)

    def _show_access_domain_with_http_info(self, request):
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
            cname=cname,
            response_type='ShowAccessDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_namespace_async(self, request):
        """获取组织详情

        获取组织详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNamespace
        :type request: :class:`huaweicloudsdkswr.v2.ShowNamespaceRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowNamespaceResponse`
        """
        return self._show_namespace_with_http_info(request)

    def _show_namespace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowNamespaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_namespace_auth_async(self, request):
        """查询组织权限

        查询组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.ShowNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowNamespaceAuthResponse`
        """
        return self._show_namespace_auth_with_http_info(request)

    def _show_namespace_auth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_repository_async(self, request):
        """查询镜像仓库概要信息

        查询镜像仓库概要信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRepository
        :type request: :class:`huaweicloudsdkswr.v2.ShowRepositoryRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowRepositoryResponse`
        """
        return self._show_repository_with_http_info(request)

    def _show_repository_with_http_info(self, request):
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
            cname=cname,
            response_type='ShowRepositoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_retention_async(self, request):
        """获取镜像老化规则记录

        获取镜像老化规则记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRetention
        :type request: :class:`huaweicloudsdkswr.v2.ShowRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowRetentionResponse`
        """
        return self._show_retention_with_http_info(request)

    def _show_retention_with_http_info(self, request):
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
            cname=cname,
            response_type='ShowRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sync_job_async(self, request):
        """获取镜像自动同步任务信息

        创建镜像自动同步任务后，可以通过此接口查询该任务的状态，以判断是否同步成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSyncJob
        :type request: :class:`huaweicloudsdkswr.v2.ShowSyncJobRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowSyncJobResponse`
        """
        return self._show_sync_job_with_http_info(request)

    def _show_sync_job_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["Content-Range", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}/sync_job',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSyncJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_trigger_async(self, request):
        """获取触发器详情

        获取触发器详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrigger
        :type request: :class:`huaweicloudsdkswr.v2.ShowTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowTriggerResponse`
        """
        return self._show_trigger_with_http_info(request)

    def _show_trigger_with_http_info(self, request):
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
            cname=cname,
            response_type='ShowTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_repository_auth_async(self, request):
        """查询镜像权限

        查询镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.ShowUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowUserRepositoryAuthResponse`
        """
        return self._show_user_repository_auth_with_http_info(request)

    def _show_user_repository_auth_with_http_info(self, request):
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
            cname=cname,
            response_type='ShowUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_namespace_auth_async(self, request):
        """更新组织权限

        更新组织权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNamespaceAuth
        :type request: :class:`huaweicloudsdkswr.v2.UpdateNamespaceAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateNamespaceAuthResponse`
        """
        return self._update_namespace_auth_with_http_info(request)

    def _update_namespace_auth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNamespaceAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_repo_async(self, request):
        """更新镜像仓库的概要信息

        更新租户组织下的镜像概要信息，包括镜像类型、是否公有、描述信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepo
        :type request: :class:`huaweicloudsdkswr.v2.UpdateRepoRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRepoResponse`
        """
        return self._update_repo_with_http_info(request)

    def _update_repo_with_http_info(self, request):
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
            resource_path='/v2/manage/namespaces/{namespace}/repos/{repository}',
            method='PATCH',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateRepoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_repo_domains_async(self, request):
        """更新共享帐号

        更新共享帐号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRepoDomains
        :type request: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRepoDomainsResponse`
        """
        return self._update_repo_domains_with_http_info(request)

    def _update_repo_domains_with_http_info(self, request):
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
            cname=cname,
            response_type='UpdateRepoDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_retention_async(self, request):
        """修改镜像老化规则

        修改镜像老化规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRetention
        :type request: :class:`huaweicloudsdkswr.v2.UpdateRetentionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateRetentionResponse`
        """
        return self._update_retention_with_http_info(request)

    def _update_retention_with_http_info(self, request):
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
            cname=cname,
            response_type='UpdateRetentionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_trigger_async(self, request):
        """更新触发器配置

        更新触发器配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTrigger
        :type request: :class:`huaweicloudsdkswr.v2.UpdateTriggerRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateTriggerResponse`
        """
        return self._update_trigger_with_http_info(request)

    def _update_trigger_with_http_info(self, request):
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
            cname=cname,
            response_type='UpdateTriggerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_repository_auth_async(self, request):
        """更新镜像权限

        更新镜像权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateUserRepositoryAuth
        :type request: :class:`huaweicloudsdkswr.v2.UpdateUserRepositoryAuthRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateUserRepositoryAuthResponse`
        """
        return self._update_user_repository_auth_with_http_info(request)

    def _update_user_repository_auth_with_http_info(self, request):
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
            cname=cname,
            response_type='UpdateUserRepositoryAuthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions_async(self, request):
        """查询所有API版本信息

        查询所有API版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkswr.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ListApiVersionsResponse`
        """
        return self._list_api_versions_with_http_info(request)

    def _list_api_versions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_version_async(self, request):
        """查询指定API版本信息

        查询指定API版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkswr.v2.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkswr.v2.ShowApiVersionResponse`
        """
        return self._show_api_version_with_http_info(request)

    def _show_api_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ShowApiVersionResponse',
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

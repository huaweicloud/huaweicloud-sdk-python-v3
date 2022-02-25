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


class CssClient(Client):
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
        super(CssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcss.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CssClient":
            raise TypeError("client type error, support client type is CssClient")

        return ClientBuilder(clazz)

    def create_auto_create_policy(self, request):
        """设置自动创建快照策略

        该接口用于设置自动创建快照，默认一天创建一个快照。

        :param CreateAutoCreatePolicyRequest request
        :return: CreateAutoCreatePolicyResponse
        """
        return self.create_auto_create_policy_with_http_info(request)

    def create_auto_create_policy_with_http_info(self, request):
        """设置自动创建快照策略

        该接口用于设置自动创建快照，默认一天创建一个快照。

        :param CreateAutoCreatePolicyRequest request
        :return: CreateAutoCreatePolicyResponse
        """

        all_params = ['cluster_id', 'set_rds_backup_cnf_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAutoCreatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_bind_public(self, request):
        """开启公网访问

        该接口用于开启公网访问。

        :param CreateBindPublicRequest request
        :return: CreateBindPublicResponse
        """
        return self.create_bind_public_with_http_info(request)

    def create_bind_public_with_http_info(self, request):
        """开启公网访问

        该接口用于开启公网访问。

        :param CreateBindPublicRequest request
        :return: CreateBindPublicResponse
        """

        all_params = ['cluster_id', 'bind_public_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/public/open',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBindPublicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cluster(self, request):
        """创建集群

        该接口用于创建集群。

        :param CreateClusterRequest request
        :return: CreateClusterResponse
        """
        return self.create_cluster_with_http_info(request)

    def create_cluster_with_http_info(self, request):
        """创建集群

        该接口用于创建集群。

        :param CreateClusterRequest request
        :return: CreateClusterResponse
        """

        all_params = ['create_cluster_req']
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
            resource_path='/v1.0/{project_id}/clusters',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_clusters_tags(self, request):
        """添加指定集群标签

        该接口用于给指定集群添加标签。

        :param CreateClustersTagsRequest request
        :return: CreateClustersTagsResponse
        """
        return self.create_clusters_tags_with_http_info(request)

    def create_clusters_tags_with_http_info(self, request):
        """添加指定集群标签

        该接口用于给指定集群添加标签。

        :param CreateClustersTagsRequest request
        :return: CreateClustersTagsResponse
        """

        all_params = ['cluster_id', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/css-cluster/{cluster_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateClustersTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_load_ik_thesaurus(self, request):
        """加载自定义词库

        该接口用于加载存放于OBS的自定义词库。

        :param CreateLoadIkThesaurusRequest request
        :return: CreateLoadIkThesaurusResponse
        """
        return self.create_load_ik_thesaurus_with_http_info(request)

    def create_load_ik_thesaurus_with_http_info(self, request):
        """加载自定义词库

        该接口用于加载存放于OBS的自定义词库。

        :param CreateLoadIkThesaurusRequest request
        :return: CreateLoadIkThesaurusResponse
        """

        all_params = ['cluster_id', 'load_custom_thesaurus_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/thesaurus',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLoadIkThesaurusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_log_backup(self, request):
        """备份日志

        该接口用于备份日志。

        :param CreateLogBackupRequest request
        :return: CreateLogBackupResponse
        """
        return self.create_log_backup_with_http_info(request)

    def create_log_backup_with_http_info(self, request):
        """备份日志

        该接口用于备份日志。

        :param CreateLogBackupRequest request
        :return: CreateLogBackupResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/collect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateLogBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_snapshot(self, request):
        """手动创建快照

        该接口用于手动创建一个快照。

        :param CreateSnapshotRequest request
        :return: CreateSnapshotResponse
        """
        return self.create_snapshot_with_http_info(request)

    def create_snapshot_with_http_info(self, request):
        """手动创建快照

        该接口用于手动创建一个快照。

        :param CreateSnapshotRequest request
        :return: CreateSnapshotResponse
        """

        all_params = ['cluster_id', 'create_snapshot_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_cluster(self, request):
        """删除集群

        此接口用于删除集群。集群删除将释放此集群的所有资源，包括客户数据。为了安全起见，请确保为这个集群创建快照。

        :param DeleteClusterRequest request
        :return: DeleteClusterResponse
        """
        return self.delete_cluster_with_http_info(request)

    def delete_cluster_with_http_info(self, request):
        """删除集群

        此接口用于删除集群。集群删除将释放此集群的所有资源，包括客户数据。为了安全起见，请确保为这个集群创建快照。

        :param DeleteClusterRequest request
        :return: DeleteClusterResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_clusters_tags(self, request):
        """删除集群标签

        此接口用于删除集群标签。

        :param DeleteClustersTagsRequest request
        :return: DeleteClustersTagsResponse
        """
        return self.delete_clusters_tags_with_http_info(request)

    def delete_clusters_tags_with_http_info(self, request):
        """删除集群标签

        此接口用于删除集群标签。

        :param DeleteClustersTagsRequest request
        :return: DeleteClustersTagsResponse
        """

        all_params = ['cluster_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v1.0/{project_id}/css-cluster/{cluster_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteClustersTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_ik_thesaurus(self, request):
        """删除自定义词库

        该接口用于删除自定义词库。

        :param DeleteIkThesaurusRequest request
        :return: DeleteIkThesaurusResponse
        """
        return self.delete_ik_thesaurus_with_http_info(request)

    def delete_ik_thesaurus_with_http_info(self, request):
        """删除自定义词库

        该接口用于删除自定义词库。

        :param DeleteIkThesaurusRequest request
        :return: DeleteIkThesaurusResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/thesaurus',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteIkThesaurusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_snapshot(self, request):
        """删除快照

        该接口用于删除快照。

        :param DeleteSnapshotRequest request
        :return: DeleteSnapshotResponse
        """
        return self.delete_snapshot_with_http_info(request)

    def delete_snapshot_with_http_info(self, request):
        """删除快照

        该接口用于删除快照。

        :param DeleteSnapshotRequest request
        :return: DeleteSnapshotResponse
        """

        all_params = ['cluster_id', 'snapshot_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_clusters_details(self, request):
        """查询集群列表

        该接口用于查询并显示集群列表以及集群的状态。

        :param ListClustersDetailsRequest request
        :return: ListClustersDetailsResponse
        """
        return self.list_clusters_details_with_http_info(request)

    def list_clusters_details_with_http_info(self, request):
        """查询集群列表

        该接口用于查询并显示集群列表以及集群的状态。

        :param ListClustersDetailsRequest request
        :return: ListClustersDetailsResponse
        """

        all_params = ['start', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in local_var_params:
            query_params.append(('start', local_var_params['start']))
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

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/clusters',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClustersDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_clusters_tags(self, request):
        """查询所有标签

        该接口用于查询指定region下的所有标签集合。

        :param ListClustersTagsRequest request
        :return: ListClustersTagsResponse
        """
        return self.list_clusters_tags_with_http_info(request)

    def list_clusters_tags_with_http_info(self, request):
        """查询所有标签

        该接口用于查询指定region下的所有标签集合。

        :param ListClustersTagsRequest request
        :return: ListClustersTagsResponse
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

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/css-cluster/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClustersTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors(self, request):
        """获取实例规格列表

        该接口用于查询并显示支持的实例规格对应的ID。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """获取实例规格列表

        该接口用于查询并显示支持的实例规格对应的ID。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
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

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/es-flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_logs_job(self, request):
        """查询作业列表

        该接口用于查询具体某个集群的日志任务记录列表。

        :param ListLogsJobRequest request
        :return: ListLogsJobResponse
        """
        return self.list_logs_job_with_http_info(request)

    def list_logs_job_with_http_info(self, request):
        """查询作业列表

        该接口用于查询具体某个集群的日志任务记录列表。

        :param ListLogsJobRequest request
        :return: ListLogsJobResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListLogsJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_snapshots(self, request):
        """查询快照列表

        该接口用于查询集群的所有快照。

        :param ListSnapshotsRequest request
        :return: ListSnapshotsResponse
        """
        return self.list_snapshots_with_http_info(request)

    def list_snapshots_with_http_info(self, request):
        """查询快照列表

        该接口用于查询集群的所有快照。

        :param ListSnapshotsRequest request
        :return: ListSnapshotsResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshots',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSnapshotsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ymls(self, request):
        """获取参数配置列表

        该接口用于获取参数配置列表。

        :param ListYmlsRequest request
        :return: ListYmlsResponse
        """
        return self.list_ymls_with_http_info(request)

    def list_ymls_with_http_info(self, request):
        """获取参数配置列表

        该接口用于获取参数配置列表。

        :param ListYmlsRequest request
        :return: ListYmlsResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ymls/template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListYmlsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ymls_job(self, request):
        """获取参数配置任务列表

        该接口用于获取参数配置任务列表。

        :param ListYmlsJobRequest request
        :return: ListYmlsJobResponse
        """
        return self.list_ymls_job_with_http_info(request)

    def list_ymls_job_with_http_info(self, request):
        """获取参数配置任务列表

        该接口用于获取参数配置任务列表。

        :param ListYmlsJobRequest request
        :return: ListYmlsJobResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ymls/joblists',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListYmlsJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def reset_password(self, request):
        """修改密码

        该接口用于修改集群密码。

        :param ResetPasswordRequest request
        :return: ResetPasswordResponse
        """
        return self.reset_password_with_http_info(request)

    def reset_password_with_http_info(self, request):
        """修改密码

        该接口用于修改集群密码。

        :param ResetPasswordRequest request
        :return: ResetPasswordResponse
        """

        all_params = ['cluster_id', 'reset_password_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/password/reset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restart_cluster(self, request):
        """重启集群

        此接口用于重启集群，重启集群将导致业务中断。

        :param RestartClusterRequest request
        :return: RestartClusterResponse
        """
        return self.restart_cluster_with_http_info(request)

    def restart_cluster_with_http_info(self, request):
        """重启集群

        此接口用于重启集群，重启集群将导致业务中断。

        :param RestartClusterRequest request
        :return: RestartClusterResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestartClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restore_snapshot(self, request):
        """恢复快照

        该接口用于手动恢复一个快照。

        :param RestoreSnapshotRequest request
        :return: RestoreSnapshotResponse
        """
        return self.restore_snapshot_with_http_info(request)

    def restore_snapshot_with_http_info(self, request):
        """恢复快照

        该接口用于手动恢复一个快照。

        :param RestoreSnapshotRequest request
        :return: RestoreSnapshotResponse
        """

        all_params = ['cluster_id', 'snapshot_id', 'restore_snapshot_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'snapshot_id' in local_var_params:
            path_params['snapshot_id'] = local_var_params['snapshot_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestoreSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_auto_create_policy(self, request):
        """查询集群的自动创建快照策略

        该接口用于查询自动创建快照策略。

        :param ShowAutoCreatePolicyRequest request
        :return: ShowAutoCreatePolicyResponse
        """
        return self.show_auto_create_policy_with_http_info(request)

    def show_auto_create_policy_with_http_info(self, request):
        """查询集群的自动创建快照策略

        该接口用于查询自动创建快照策略。

        :param ShowAutoCreatePolicyRequest request
        :return: ShowAutoCreatePolicyResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAutoCreatePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cluster_detail(self, request):
        """查询集群详情

        该接口用于查询并显示单个集群详情。

        :param ShowClusterDetailRequest request
        :return: ShowClusterDetailResponse
        """
        return self.show_cluster_detail_with_http_info(request)

    def show_cluster_detail_with_http_info(self, request):
        """查询集群详情

        该接口用于查询并显示单个集群详情。

        :param ShowClusterDetailRequest request
        :return: ShowClusterDetailResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClusterDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_cluster_tag(self, request):
        """查询指定集群的标签

        该接口用于查询指定集群的标签信息。

        :param ShowClusterTagRequest request
        :return: ShowClusterTagResponse
        """
        return self.show_cluster_tag_with_http_info(request)

    def show_cluster_tag_with_http_info(self, request):
        """查询指定集群的标签

        该接口用于查询指定集群的标签信息。

        :param ShowClusterTagRequest request
        :return: ShowClusterTagResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/css-cluster/{cluster_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowClusterTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_get_log_setting(self, request):
        """查询日志基础配置

        该接口用于日志基础配置查询。

        :param ShowGetLogSettingRequest request
        :return: ShowGetLogSettingResponse
        """
        return self.show_get_log_setting_with_http_info(request)

    def show_get_log_setting_with_http_info(self, request):
        """查询日志基础配置

        该接口用于日志基础配置查询。

        :param ShowGetLogSettingRequest request
        :return: ShowGetLogSettingResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/settings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGetLogSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ik_thesaurus(self, request):
        """查询自定义词库状态

        该接口用于查询自定义词库的加载状态。

        :param ShowIkThesaurusRequest request
        :return: ShowIkThesaurusResponse
        """
        return self.show_ik_thesaurus_with_http_info(request)

    def show_ik_thesaurus_with_http_info(self, request):
        """查询自定义词库状态

        该接口用于查询自定义词库的加载状态。

        :param ShowIkThesaurusRequest request
        :return: ShowIkThesaurusResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/thesaurus',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowIkThesaurusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_log_backup(self, request):
        """查询日志

        该接口用于查询日志信息。

        :param ShowLogBackupRequest request
        :return: ShowLogBackupResponse
        """
        return self.show_log_backup_with_http_info(request)

    def show_log_backup_with_http_info(self, request):
        """查询日志

        该接口用于查询日志信息。

        :param ShowLogBackupRequest request
        :return: ShowLogBackupResponse
        """

        all_params = ['cluster_id', 'get_log_backup_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLogBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vpcep_connection(self, request):
        """获取终端节点连接

        该接口用于获取终端节点连接。

        :param ShowVpcepConnectionRequest request
        :return: ShowVpcepConnectionResponse
        """
        return self.show_vpcep_connection_with_http_info(request)

    def show_vpcep_connection_with_http_info(self, request):
        """获取终端节点连接

        该接口用于获取终端节点连接。

        :param ShowVpcepConnectionRequest request
        :return: ShowVpcepConnectionResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcepConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_auto_setting(self, request):
        """自动设置集群快照的基础配置（不推荐使用）

        说明：自动设置集群快照接口将会自动创建快照OBS桶和委托。如果有多个集群，每个集群使用这个接口都会创建一个不一样的OBS桶，可能会导致OBS的配额不够，较多的OBS桶也难以维护。建议可以直接使用[修改集群快照的基础配置](https://support.huaweicloud.com/api-css/css_03_0030.html)。  该接口用于自动设置集群快照的基础配置，包括配置OBS桶和IAM委托。  - “OBS桶”：快照存储的OBS桶位置。 - “备份路径”：快照在OBS桶中的存放路径。 - “IAM委托”：由于需要将快照保存在OBS中，所以需要在IAM中设置对应的委托获取对OBS服务的授权。

        :param StartAutoSettingRequest request
        :return: StartAutoSettingResponse
        """
        return self.start_auto_setting_with_http_info(request)

    def start_auto_setting_with_http_info(self, request):
        """自动设置集群快照的基础配置（不推荐使用）

        说明：自动设置集群快照接口将会自动创建快照OBS桶和委托。如果有多个集群，每个集群使用这个接口都会创建一个不一样的OBS桶，可能会导致OBS的配额不够，较多的OBS桶也难以维护。建议可以直接使用[修改集群快照的基础配置](https://support.huaweicloud.com/api-css/css_03_0030.html)。  该接口用于自动设置集群快照的基础配置，包括配置OBS桶和IAM委托。  - “OBS桶”：快照存储的OBS桶位置。 - “备份路径”：快照在OBS桶中的存放路径。 - “IAM委托”：由于需要将快照保存在OBS中，所以需要在IAM中设置对应的委托获取对OBS服务的授权。

        :param StartAutoSettingRequest request
        :return: StartAutoSettingResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/auto_setting',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartAutoSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_log_auto_backup_policy(self, request):
        """开启日志自动备份策略

        该接口用于日志自动备份策略开启。

        :param StartLogAutoBackupPolicyRequest request
        :return: StartLogAutoBackupPolicyResponse
        """
        return self.start_log_auto_backup_policy_with_http_info(request)

    def start_log_auto_backup_policy_with_http_info(self, request):
        """开启日志自动备份策略

        该接口用于日志自动备份策略开启。

        :param StartLogAutoBackupPolicyRequest request
        :return: StartLogAutoBackupPolicyResponse
        """

        all_params = ['cluster_id', 'start_log_auto_backup_policy_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/policy/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartLogAutoBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_logs(self, request):
        """开启日志功能

        该接口用于开启日志功能。

        :param StartLogsRequest request
        :return: StartLogsResponse
        """
        return self.start_logs_with_http_info(request)

    def start_logs_with_http_info(self, request):
        """开启日志功能

        该接口用于开启日志功能。

        :param StartLogsRequest request
        :return: StartLogsResponse
        """

        all_params = ['cluster_id', 'start_logs_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/open',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_public_whitelist(self, request):
        """开启公网访问控制白名单

        该接口用于开启公网访问控制白名单。

        :param StartPublicWhitelistRequest request
        :return: StartPublicWhitelistResponse
        """
        return self.start_public_whitelist_with_http_info(request)

    def start_public_whitelist_with_http_info(self, request):
        """开启公网访问控制白名单

        该接口用于开启公网访问控制白名单。

        :param StartPublicWhitelistRequest request
        :return: StartPublicWhitelistResponse
        """

        all_params = ['cluster_id', 'start_public_whitelist_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartPublicWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_vpecp(self, request):
        """开启终端节点服务

        该接口用于开启终端节点服务。

        :param StartVpecpRequest request
        :return: StartVpecpResponse
        """
        return self.start_vpecp_with_http_info(request)

    def start_vpecp_with_http_info(self, request):
        """开启终端节点服务

        该接口用于开启终端节点服务。

        :param StartVpecpRequest request
        :return: StartVpecpResponse
        """

        all_params = ['cluster_id', 'start_vpecp_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/open',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartVpecpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_log_auto_backup_policy(self, request):
        """关闭日志自动备份策略

        该接口用于日志自动备份策略关闭。

        :param StopLogAutoBackupPolicyRequest request
        :return: StopLogAutoBackupPolicyResponse
        """
        return self.stop_log_auto_backup_policy_with_http_info(request)

    def stop_log_auto_backup_policy_with_http_info(self, request):
        """关闭日志自动备份策略

        该接口用于日志自动备份策略关闭。

        :param StopLogAutoBackupPolicyRequest request
        :return: StopLogAutoBackupPolicyResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/policy/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopLogAutoBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_logs(self, request):
        """关闭日志功能

        该接口用于关闭日志功能。

        :param StopLogsRequest request
        :return: StopLogsResponse
        """
        return self.stop_logs_with_http_info(request)

    def stop_logs_with_http_info(self, request):
        """关闭日志功能

        该接口用于关闭日志功能。

        :param StopLogsRequest request
        :return: StopLogsResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_public_whitelist(self, request):
        """关闭公网访问控制白名单

        该接口用于关闭公网访问控制白名单。

        :param StopPublicWhitelistRequest request
        :return: StopPublicWhitelistResponse
        """
        return self.stop_public_whitelist_with_http_info(request)

    def stop_public_whitelist_with_http_info(self, request):
        """关闭公网访问控制白名单

        该接口用于关闭公网访问控制白名单。

        :param StopPublicWhitelistRequest request
        :return: StopPublicWhitelistResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopPublicWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_snapshot(self, request):
        """停用快照功能

        该接口用于停用快照功能。

        :param StopSnapshotRequest request
        :return: StopSnapshotResponse
        """
        return self.stop_snapshot_with_http_info(request)

    def stop_snapshot_with_http_info(self, request):
        """停用快照功能

        该接口用于停用快照功能。

        :param StopSnapshotRequest request
        :return: StopSnapshotResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshots',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopSnapshotResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_vpecp(self, request):
        """关闭终端节点服务

        该接口用于关闭终端节点服务。

        :param StopVpecpRequest request
        :return: StopVpecpResponse
        """
        return self.stop_vpecp_with_http_info(request)

    def stop_vpecp_with_http_info(self, request):
        """关闭终端节点服务

        该接口用于关闭终端节点服务。

        :param StopVpecpRequest request
        :return: StopVpecpResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopVpecpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_batch_clusters_tags(self, request):
        """批量添加或删除集群标签

        该接口用于批量添加或删除集群标签。

        :param UpdateBatchClustersTagsRequest request
        :return: UpdateBatchClustersTagsResponse
        """
        return self.update_batch_clusters_tags_with_http_info(request)

    def update_batch_clusters_tags_with_http_info(self, request):
        """批量添加或删除集群标签

        该接口用于批量添加或删除集群标签。

        :param UpdateBatchClustersTagsRequest request
        :return: UpdateBatchClustersTagsResponse
        """

        all_params = ['cluster_id', 'batch_add_or_delete_tag_on_cluster_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/css-cluster/{cluster_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBatchClustersTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cluster_name(self, request):
        """修改集群名称

        该接口用于修改集群名称。

        :param UpdateClusterNameRequest request
        :return: UpdateClusterNameResponse
        """
        return self.update_cluster_name_with_http_info(request)

    def update_cluster_name_with_http_info(self, request):
        """修改集群名称

        该接口用于修改集群名称。

        :param UpdateClusterNameRequest request
        :return: UpdateClusterNameResponse
        """

        all_params = ['cluster_id', 'update_cluster_name_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/changename',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateClusterNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_extend_cluster(self, request):
        """扩容集群

        该接口用于集群扩容实例（仅支持扩容elasticsearch实例）。只扩容普通节点，且只针对要扩容的集群实例不存在特殊节点（Master、Client、冷数据节点）的情况。 说明：推荐使用[扩容实例的数量和存储容量](https://support.huaweicloud.com/api-css/css_03_0038.html)进行扩容。

        :param UpdateExtendClusterRequest request
        :return: UpdateExtendClusterResponse
        """
        return self.update_extend_cluster_with_http_info(request)

    def update_extend_cluster_with_http_info(self, request):
        """扩容集群

        该接口用于集群扩容实例（仅支持扩容elasticsearch实例）。只扩容普通节点，且只针对要扩容的集群实例不存在特殊节点（Master、Client、冷数据节点）的情况。 说明：推荐使用[扩容实例的数量和存储容量](https://support.huaweicloud.com/api-css/css_03_0038.html)进行扩容。

        :param UpdateExtendClusterRequest request
        :return: UpdateExtendClusterResponse
        """

        all_params = ['cluster_id', 'extend_cluster_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateExtendClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_extend_instance_storage(self, request):
        """扩容实例的数量和存储容量

        该接口用于集群扩容不同类型实例的个数以及存储容量。已经存在独立Master、Client、冷数据节点的集群使用该接口扩容。（支持扩容elasticsearch和logstash实例）。

        :param UpdateExtendInstanceStorageRequest request
        :return: UpdateExtendInstanceStorageResponse
        """
        return self.update_extend_instance_storage_with_http_info(request)

    def update_extend_instance_storage_with_http_info(self, request):
        """扩容实例的数量和存储容量

        该接口用于集群扩容不同类型实例的个数以及存储容量。已经存在独立Master、Client、冷数据节点的集群使用该接口扩容。（支持扩容elasticsearch和logstash实例）。

        :param UpdateExtendInstanceStorageRequest request
        :return: UpdateExtendInstanceStorageResponse
        """

        all_params = ['cluster_id', 'role_extend_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/role_extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateExtendInstanceStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_flavor(self, request):
        """变更规格

        该接口用于变更集群规格。只支持变更ess节点类型。

        :param UpdateFlavorRequest request
        :return: UpdateFlavorResponse
        """
        return self.update_flavor_with_http_info(request)

    def update_flavor_with_http_info(self, request):
        """变更规格

        该接口用于变更集群规格。只支持变更ess节点类型。

        :param UpdateFlavorRequest request
        :return: UpdateFlavorResponse
        """

        all_params = ['cluster_id', 'update_flavor_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/flavor',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFlavorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_flavor_by_type(self, request):
        """全规格集群变更

        修改集群规格。支持修改ess， ess-cold， ess-client， ess-master节点类型。

        :param UpdateFlavorByTypeRequest request
        :return: UpdateFlavorByTypeResponse
        """
        return self.update_flavor_by_type_with_http_info(request)

    def update_flavor_by_type_with_http_info(self, request):
        """全规格集群变更

        修改集群规格。支持修改ess， ess-cold， ess-client， ess-master节点类型。

        :param UpdateFlavorByTypeRequest request
        :return: UpdateFlavorByTypeResponse
        """

        all_params = ['cluster_id', 'types', 'update_flavor_by_type_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'types' in local_var_params:
            path_params['types'] = local_var_params['types']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/{types}/flavor',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFlavorByTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_log_setting(self, request):
        """修改日志基础配置

        该接口用于修改日志基础配置。

        :param UpdateLogSettingRequest request
        :return: UpdateLogSettingResponse
        """
        return self.update_log_setting_with_http_info(request)

    def update_log_setting_with_http_info(self, request):
        """修改日志基础配置

        该接口用于修改日志基础配置。

        :param UpdateLogSettingRequest request
        :return: UpdateLogSettingResponse
        """

        all_params = ['cluster_id', 'update_log_setting_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/logs/settings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateLogSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_ondemand_cluster_to_period(self, request):
        """按需集群转包周期

        该接口用于按需集群转包周期集群。

        :param UpdateOndemandClusterToPeriodRequest request
        :return: UpdateOndemandClusterToPeriodResponse
        """
        return self.update_ondemand_cluster_to_period_with_http_info(request)

    def update_ondemand_cluster_to_period_with_http_info(self, request):
        """按需集群转包周期

        该接口用于按需集群转包周期集群。

        :param UpdateOndemandClusterToPeriodRequest request
        :return: UpdateOndemandClusterToPeriodResponse
        """

        all_params = ['cluster_id', 'period_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/cluster/{cluster_id}/period',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateOndemandClusterToPeriodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_public_band_width(self, request):
        """修改公网访问带宽

        该接口用于修改公网访问带宽。

        :param UpdatePublicBandWidthRequest request
        :return: UpdatePublicBandWidthResponse
        """
        return self.update_public_band_width_with_http_info(request)

    def update_public_band_width_with_http_info(self, request):
        """修改公网访问带宽

        该接口用于修改公网访问带宽。

        :param UpdatePublicBandWidthRequest request
        :return: UpdatePublicBandWidthResponse
        """

        all_params = ['cluster_id', 'bind_public_req_eip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/public/bandwidth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicBandWidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_shrink_cluster(self, request):
        """缩容集群

        该接口用于集群缩容不同类型实例的个数以及存储容量。

        :param UpdateShrinkClusterRequest request
        :return: UpdateShrinkClusterResponse
        """
        return self.update_shrink_cluster_with_http_info(request)

    def update_shrink_cluster_with_http_info(self, request):
        """缩容集群

        该接口用于集群缩容不同类型实例的个数以及存储容量。

        :param UpdateShrinkClusterRequest request
        :return: UpdateShrinkClusterResponse
        """

        all_params = ['cluster_id', 'shrink_cluster_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/extend/{project_id}/clusters/{cluster_id}/role/shrink',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateShrinkClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_shrink_nodes(self, request):
        """指定角色下线

        该接口用于下线集群指定角色。

        :param UpdateShrinkNodesRequest request
        :return: UpdateShrinkNodesResponse
        """
        return self.update_shrink_nodes_with_http_info(request)

    def update_shrink_nodes_with_http_info(self, request):
        """指定角色下线

        该接口用于下线集群指定角色。

        :param UpdateShrinkNodesRequest request
        :return: UpdateShrinkNodesResponse
        """

        all_params = ['cluster_id', 'shrink_nodes_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/node/offline',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateShrinkNodesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_snapshot_setting(self, request):
        """修改集群快照的基础配置

        该接口用于修改集群快照的基础配置，可修改OBS桶和IAM委托。 说明：如果未开启快照功能，使用该接口后，将会开启快照。

        :param UpdateSnapshotSettingRequest request
        :return: UpdateSnapshotSettingResponse
        """
        return self.update_snapshot_setting_with_http_info(request)

    def update_snapshot_setting_with_http_info(self, request):
        """修改集群快照的基础配置

        该接口用于修改集群快照的基础配置，可修改OBS桶和IAM委托。 说明：如果未开启快照功能，使用该接口后，将会开启快照。

        :param UpdateSnapshotSettingRequest request
        :return: UpdateSnapshotSettingResponse
        """

        all_params = ['cluster_id', 'update_snapshot_setting_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/setting',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSnapshotSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_unbind_public(self, request):
        """关闭公网访问

        该接口用于关闭公网访问。

        :param UpdateUnbindPublicRequest request
        :return: UpdateUnbindPublicResponse
        """
        return self.update_unbind_public_with_http_info(request)

    def update_unbind_public_with_http_info(self, request):
        """关闭公网访问

        该接口用于关闭公网访问。

        :param UpdateUnbindPublicRequest request
        :return: UpdateUnbindPublicResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/public/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateUnbindPublicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_vpcep_connection(self, request):
        """更新终端节点连接

        该接口用于更新终端节点连接。

        :param UpdateVpcepConnectionRequest request
        :return: UpdateVpcepConnectionResponse
        """
        return self.update_vpcep_connection_with_http_info(request)

    def update_vpcep_connection_with_http_info(self, request):
        """更新终端节点连接

        该接口用于更新终端节点连接。

        :param UpdateVpcepConnectionRequest request
        :return: UpdateVpcepConnectionResponse
        """

        all_params = ['cluster_id', 'update_vpcep_connection_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcepConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_vpcep_whitelist(self, request):
        """修改终端节点服务白名单

        该接口用于修改终端节点服务白名单。

        :param UpdateVpcepWhitelistRequest request
        :return: UpdateVpcepWhitelistResponse
        """
        return self.update_vpcep_whitelist_with_http_info(request)

    def update_vpcep_whitelist_with_http_info(self, request):
        """修改终端节点服务白名单

        该接口用于修改终端节点服务白名单。

        :param UpdateVpcepWhitelistRequest request
        :return: UpdateVpcepWhitelistResponse
        """

        all_params = ['cluster_id', 'update_vpcep_whitelist_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/permissions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcepWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_ymls(self, request):
        """修改参数配置

        该接口用于修改参数配口。

        :param UpdateYmlsRequest request
        :return: UpdateYmlsResponse
        """
        return self.update_ymls_with_http_info(request)

    def update_ymls_with_http_info(self, request):
        """修改参数配置

        该接口用于修改参数配口。

        :param UpdateYmlsRequest request
        :return: UpdateYmlsResponse
        """

        all_params = ['cluster_id', 'update_ymls_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/ymls/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateYmlsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_kibana_public(self, request):
        """开启Kibana公网访问

        该接口用于开启Kibana公网访问。

        :param StartKibanaPublicRequest request
        :return: StartKibanaPublicResponse
        """
        return self.start_kibana_public_with_http_info(request)

    def start_kibana_public_with_http_info(self, request):
        """开启Kibana公网访问

        该接口用于开启Kibana公网访问。

        :param StartKibanaPublicRequest request
        :return: StartKibanaPublicResponse
        """

        all_params = ['cluster_id', 'start_kibana_public_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/publickibana/open',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartKibanaPublicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_public_kibana_whitelist(self, request):
        """关闭访问控制

        该接口用于关闭Kibana公网访问控制。

        :param StopPublicKibanaWhitelistRequest request
        :return: StopPublicKibanaWhitelistResponse
        """
        return self.stop_public_kibana_whitelist_with_http_info(request)

    def stop_public_kibana_whitelist_with_http_info(self, request):
        """关闭访问控制

        该接口用于关闭Kibana公网访问控制。

        :param StopPublicKibanaWhitelistRequest request
        :return: StopPublicKibanaWhitelistResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/publickibana/whitelist/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopPublicKibanaWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_alter_kibana(self, request):
        """修改Kibana公网带宽

        该接口用于修改Kibana公网带宽。

        :param UpdateAlterKibanaRequest request
        :return: UpdateAlterKibanaResponse
        """
        return self.update_alter_kibana_with_http_info(request)

    def update_alter_kibana_with_http_info(self, request):
        """修改Kibana公网带宽

        该接口用于修改Kibana公网带宽。

        :param UpdateAlterKibanaRequest request
        :return: UpdateAlterKibanaResponse
        """

        all_params = ['cluster_id', 'update_public_kibana_bandwidth_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/publickibana/bandwidth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAlterKibanaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_close_kibana(self, request):
        """关闭Kibana公网访问

        该接口用于关闭Kibana公网访问。

        :param UpdateCloseKibanaRequest request
        :return: UpdateCloseKibanaResponse
        """
        return self.update_close_kibana_with_http_info(request)

    def update_close_kibana_with_http_info(self, request):
        """关闭Kibana公网访问

        该接口用于关闭Kibana公网访问。

        :param UpdateCloseKibanaRequest request
        :return: UpdateCloseKibanaResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/publickibana/close',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCloseKibanaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_public_kibana_whitelist(self, request):
        """修改访问控制

        该接口通过修改kibana白名单，修改kibana的访问权限。

        :param UpdatePublicKibanaWhitelistRequest request
        :return: UpdatePublicKibanaWhitelistResponse
        """
        return self.update_public_kibana_whitelist_with_http_info(request)

    def update_public_kibana_whitelist_with_http_info(self, request):
        """修改访问控制

        该接口通过修改kibana白名单，修改kibana的访问权限。

        :param UpdatePublicKibanaWhitelistRequest request
        :return: UpdatePublicKibanaWhitelistResponse
        """

        all_params = ['cluster_id', 'update_public_kibana_whitelist_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/publickibana/whitelist/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicKibanaWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_favorite(self, request):
        """添加到自定义模板

        该接口用于添加到自定义模板。

        :param AddFavoriteRequest request
        :return: AddFavoriteResponse
        """
        return self.add_favorite_with_http_info(request)

    def add_favorite_with_http_info(self, request):
        """添加到自定义模板

        该接口用于添加到自定义模板。

        :param AddFavoriteRequest request
        :return: AddFavoriteResponse
        """

        all_params = ['cluster_id', 'add_favorite_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/favorite',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddFavoriteResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cnf(self, request):
        """创建配置文件

        该接口用于创建配置文件。

        :param CreateCnfRequest request
        :return: CreateCnfResponse
        """
        return self.create_cnf_with_http_info(request)

    def create_cnf_with_http_info(self, request):
        """创建配置文件

        该接口用于创建配置文件。

        :param CreateCnfRequest request
        :return: CreateCnfResponse
        """

        all_params = ['cluster_id', 'create_cnf_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/submit',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCnfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_conf(self, request):
        """删除配置文件

        删除配置文件。

        :param DeleteConfRequest request
        :return: DeleteConfResponse
        """
        return self.delete_conf_with_http_info(request)

    def delete_conf_with_http_info(self, request):
        """删除配置文件

        删除配置文件。

        :param DeleteConfRequest request
        :return: DeleteConfResponse
        """

        all_params = ['cluster_id', 'delete_conf_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteConfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_template(self, request):
        """删除自定义模板

        该接口用于删除自定义模板。

        :param DeleteTemplateRequest request
        :return: DeleteTemplateResponse
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        """删除自定义模板

        该接口用于删除自定义模板。

        :param DeleteTemplateRequest request
        :return: DeleteTemplateResponse
        """

        all_params = ['cluster_id', 'delete_template_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/lgsconf/deletetemplate',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_actions(self, request):
        """查询操作记录

        该接口用于查询操作记录。

        :param ListActionsRequest request
        :return: ListActionsResponse
        """
        return self.list_actions_with_http_info(request)

    def list_actions_with_http_info(self, request):
        """查询操作记录

        该接口用于查询操作记录。

        :param ListActionsRequest request
        :return: ListActionsResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/listactions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_confs(self, request):
        """查询配置文件列表

        该接口用于查询配置文件列表。

        :param ListConfsRequest request
        :return: ListConfsResponse
        """
        return self.list_confs_with_http_info(request)

    def list_confs_with_http_info(self, request):
        """查询配置文件列表

        该接口用于查询配置文件列表。

        :param ListConfsRequest request
        :return: ListConfsResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/listconfs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListConfsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_pipelines(self, request):
        """查询pipeline列表

        该接口用于查询pipeline列表。

        :param ListPipelinesRequest request
        :return: ListPipelinesResponse
        """
        return self.list_pipelines_with_http_info(request)

    def list_pipelines_with_http_info(self, request):
        """查询pipeline列表

        该接口用于查询pipeline列表。

        :param ListPipelinesRequest request
        :return: ListPipelinesResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/listpipelines',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPipelinesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_templates(self, request):
        """查询模板列表

        该接口用于查询模板列表。

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        """查询模板列表

        该接口用于查询模板列表。

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """

        all_params = ['type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1.0/{project_id}/lgsconf/template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_get_conf_detail(self, request):
        """查询配置文件内容

        该接口用于查询配置文件内容。

        :param ShowGetConfDetailRequest request
        :return: ShowGetConfDetailResponse
        """
        return self.show_get_conf_detail_with_http_info(request)

    def show_get_conf_detail_with_http_info(self, request):
        """查询配置文件内容

        该接口用于查询配置文件内容。

        :param ShowGetConfDetailRequest request
        :return: ShowGetConfDetailResponse
        """

        all_params = ['cluster_id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/confdetail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowGetConfDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_connectivity_test(self, request):
        """连通性测试

        该接口用于连通性测试。

        :param StartConnectivityTestRequest request
        :return: StartConnectivityTestResponse
        """
        return self.start_connectivity_test_with_http_info(request)

    def start_connectivity_test_with_http_info(self, request):
        """连通性测试

        该接口用于连通性测试。

        :param StartConnectivityTestRequest request
        :return: StartConnectivityTestResponse
        """

        all_params = ['cluster_id', 'start_connectivity_test_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/checkconnection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartConnectivityTestResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_pipeline(self, request):
        """启动pipeline迁移数据

        该接口用于启动pipeline迁移数据。

        :param StartPipelineRequest request
        :return: StartPipelineResponse
        """
        return self.start_pipeline_with_http_info(request)

    def start_pipeline_with_http_info(self, request):
        """启动pipeline迁移数据

        该接口用于启动pipeline迁移数据。

        :param StartPipelineRequest request
        :return: StartPipelineResponse
        """

        all_params = ['cluster_id', 'start_pipeline_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_pipeline(self, request):
        """停止pipeline迁移数据

        该接口用于停止pipeline迁移数据。

        :param StopPipelineRequest request
        :return: StopPipelineResponse
        """
        return self.stop_pipeline_with_http_info(request)

    def stop_pipeline_with_http_info(self, request):
        """停止pipeline迁移数据

        该接口用于停止pipeline迁移数据。

        :param StopPipelineRequest request
        :return: StopPipelineResponse
        """

        all_params = ['cluster_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_cnf(self, request):
        """更新配置文件

        该接口用于更新配置文件。

        :param UpdateCnfRequest request
        :return: UpdateCnfResponse
        """
        return self.update_cnf_with_http_info(request)

    def update_cnf_with_http_info(self, request):
        """更新配置文件

        该接口用于更新配置文件。

        :param UpdateCnfRequest request
        :return: UpdateCnfResponse
        """

        all_params = ['cluster_id', 'update_cnf_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']

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
            resource_path='/v1.0/{project_id}/clusters/{cluster_id}/lgsconf/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateCnfResponse',
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

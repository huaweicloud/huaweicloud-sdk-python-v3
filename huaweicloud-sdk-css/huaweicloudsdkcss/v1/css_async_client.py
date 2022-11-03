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


class CssAsyncClient(Client):
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
        super(CssAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcss.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CssClient":
            raise TypeError("client type error, support client type is CssClient")

        return ClientBuilder(clazz)

    def create_auto_create_policy_async(self, request):
        """设置自动创建快照策略

        该接口用于设置自动创建快照，默认一天创建一个快照。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateAutoCreatePolicy
        :type request: :class:`huaweicloudsdkcss.v1.CreateAutoCreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateAutoCreatePolicyResponse`
        """
        return self.create_auto_create_policy_with_http_info(request)

    def create_auto_create_policy_with_http_info(self, request):
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

    def create_bind_public_async(self, request):
        """开启公网访问

        该接口用于开启公网访问。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateBindPublic
        :type request: :class:`huaweicloudsdkcss.v1.CreateBindPublicRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateBindPublicResponse`
        """
        return self.create_bind_public_with_http_info(request)

    def create_bind_public_with_http_info(self, request):
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

    def create_cluster_async(self, request):
        """创建集群

        该接口用于创建集群。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCluster
        :type request: :class:`huaweicloudsdkcss.v1.CreateClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClusterResponse`
        """
        return self.create_cluster_with_http_info(request)

    def create_cluster_with_http_info(self, request):
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

    def create_clusters_tags_async(self, request):
        """添加指定集群标签

        该接口用于给指定集群添加标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.CreateClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateClustersTagsResponse`
        """
        return self.create_clusters_tags_with_http_info(request)

    def create_clusters_tags_with_http_info(self, request):
        all_params = ['cluster_id', 'resource_type', 'tag']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1.0/{project_id}/{resource_type}/{cluster_id}/tags',
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

    def create_load_ik_thesaurus_async(self, request):
        """加载自定义词库

        该接口用于加载存放于OBS的自定义词库。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateLoadIkThesaurus
        :type request: :class:`huaweicloudsdkcss.v1.CreateLoadIkThesaurusRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateLoadIkThesaurusResponse`
        """
        return self.create_load_ik_thesaurus_with_http_info(request)

    def create_load_ik_thesaurus_with_http_info(self, request):
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

    def create_log_backup_async(self, request):
        """备份日志

        该接口用于备份日志。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateLogBackup
        :type request: :class:`huaweicloudsdkcss.v1.CreateLogBackupRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateLogBackupResponse`
        """
        return self.create_log_backup_with_http_info(request)

    def create_log_backup_with_http_info(self, request):
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

    def create_snapshot_async(self, request):
        """手动创建快照

        该接口用于手动创建一个快照。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.CreateSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateSnapshotResponse`
        """
        return self.create_snapshot_with_http_info(request)

    def create_snapshot_with_http_info(self, request):
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

    def delete_cluster_async(self, request):
        """删除集群

        此接口用于删除集群。集群删除将释放此集群的所有资源，包括客户数据。如果需要保留客户集群数据，建议在删除集群前先创建快照。
        
        &gt;此接口亦可用于包年/包月集群退订。公安冻结的集群不能删除。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteCluster
        :type request: :class:`huaweicloudsdkcss.v1.DeleteClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteClusterResponse`
        """
        return self.delete_cluster_with_http_info(request)

    def delete_cluster_with_http_info(self, request):
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

    def delete_clusters_tags_async(self, request):
        """删除集群标签

        此接口用于删除集群标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.DeleteClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteClustersTagsResponse`
        """
        return self.delete_clusters_tags_with_http_info(request)

    def delete_clusters_tags_with_http_info(self, request):
        all_params = ['cluster_id', 'resource_type', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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
            resource_path='/v1.0/{project_id}/{resource_type}/{cluster_id}/tags/{key}',
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

    def delete_ik_thesaurus_async(self, request):
        """删除自定义词库

        该接口用于删除自定义词库。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteIkThesaurus
        :type request: :class:`huaweicloudsdkcss.v1.DeleteIkThesaurusRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteIkThesaurusResponse`
        """
        return self.delete_ik_thesaurus_with_http_info(request)

    def delete_ik_thesaurus_with_http_info(self, request):
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

    def delete_snapshot_async(self, request):
        """删除快照

        该接口用于删除快照。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.DeleteSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteSnapshotResponse`
        """
        return self.delete_snapshot_with_http_info(request)

    def delete_snapshot_with_http_info(self, request):
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

    def download_cert_async(self, request):
        """下载安全证书

        该接口用于下载安全证书。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DownloadCert
        :type request: :class:`huaweicloudsdkcss.v1.DownloadCertRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DownloadCertResponse`
        """
        return self.download_cert_with_http_info(request)

    def download_cert_with_http_info(self, request):
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
            resource_path='/v1.0/{project_id}/cer/download',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DownloadCertResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_clusters_details_async(self, request):
        """查询集群列表

        该接口用于查询并显示集群列表以及集群的状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListClustersDetails
        :type request: :class:`huaweicloudsdkcss.v1.ListClustersDetailsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListClustersDetailsResponse`
        """
        return self.list_clusters_details_with_http_info(request)

    def list_clusters_details_with_http_info(self, request):
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

    def list_clusters_tags_async(self, request):
        """查询所有标签

        该接口用于查询指定region下的所有标签集合。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.ListClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListClustersTagsResponse`
        """
        return self.list_clusters_tags_with_http_info(request)

    def list_clusters_tags_with_http_info(self, request):
        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1.0/{project_id}/{resource_type}/tags',
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

    def list_flavors_async(self, request):
        """获取实例规格列表

        该接口用于查询并显示支持的实例规格对应的ID。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkcss.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
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

    def list_logs_job_async(self, request):
        """查询作业列表

        该接口用于查询具体某个集群的日志任务记录列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListLogsJob
        :type request: :class:`huaweicloudsdkcss.v1.ListLogsJobRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListLogsJobResponse`
        """
        return self.list_logs_job_with_http_info(request)

    def list_logs_job_with_http_info(self, request):
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

    def list_snapshots_async(self, request):
        """查询快照列表

        该接口用于查询集群的所有快照。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSnapshots
        :type request: :class:`huaweicloudsdkcss.v1.ListSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListSnapshotsResponse`
        """
        return self.list_snapshots_with_http_info(request)

    def list_snapshots_with_http_info(self, request):
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

    def list_ymls_async(self, request):
        """获取参数配置列表

        该接口用于获取当前集群现有的参数配置列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListYmls
        :type request: :class:`huaweicloudsdkcss.v1.ListYmlsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListYmlsResponse`
        """
        return self.list_ymls_with_http_info(request)

    def list_ymls_with_http_info(self, request):
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

    def list_ymls_job_async(self, request):
        """获取参数配置任务列表

        该接口可获取参数配置的任务操作列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListYmlsJob
        :type request: :class:`huaweicloudsdkcss.v1.ListYmlsJobRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListYmlsJobResponse`
        """
        return self.list_ymls_job_with_http_info(request)

    def list_ymls_job_with_http_info(self, request):
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

    def reset_password_async(self, request):
        """修改密码

        该接口用于修改集群密码。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkcss.v1.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ResetPasswordResponse`
        """
        return self.reset_password_with_http_info(request)

    def reset_password_with_http_info(self, request):
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

    def restart_cluster_async(self, request):
        """重启集群

        此接口用于重启集群，重启集群将导致业务中断。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RestartCluster
        :type request: :class:`huaweicloudsdkcss.v1.RestartClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.RestartClusterResponse`
        """
        return self.restart_cluster_with_http_info(request)

    def restart_cluster_with_http_info(self, request):
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

    def restore_snapshot_async(self, request):
        """恢复快照

        该接口用于手动恢复一个快照。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RestoreSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.RestoreSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.RestoreSnapshotResponse`
        """
        return self.restore_snapshot_with_http_info(request)

    def restore_snapshot_with_http_info(self, request):
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

    def show_auto_create_policy_async(self, request):
        """查询自动创建快照的策略

        该接口用于查询自动创建快照策略。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowAutoCreatePolicy
        :type request: :class:`huaweicloudsdkcss.v1.ShowAutoCreatePolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowAutoCreatePolicyResponse`
        """
        return self.show_auto_create_policy_with_http_info(request)

    def show_auto_create_policy_with_http_info(self, request):
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

    def show_cluster_detail_async(self, request):
        """查询集群详情

        该接口用于查询并显示单个集群详情。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowClusterDetail
        :type request: :class:`huaweicloudsdkcss.v1.ShowClusterDetailRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowClusterDetailResponse`
        """
        return self.show_cluster_detail_with_http_info(request)

    def show_cluster_detail_with_http_info(self, request):
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

    def show_cluster_tag_async(self, request):
        """查询指定集群的标签

        该接口用于查询指定集群的标签信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowClusterTag
        :type request: :class:`huaweicloudsdkcss.v1.ShowClusterTagRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowClusterTagResponse`
        """
        return self.show_cluster_tag_with_http_info(request)

    def show_cluster_tag_with_http_info(self, request):
        all_params = ['cluster_id', 'resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1.0/{project_id}/{resource_type}/{cluster_id}/tags',
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

    def show_get_log_setting_async(self, request):
        """查询日志基础配置

        该接口用于日志基础配置查询。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowGetLogSetting
        :type request: :class:`huaweicloudsdkcss.v1.ShowGetLogSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowGetLogSettingResponse`
        """
        return self.show_get_log_setting_with_http_info(request)

    def show_get_log_setting_with_http_info(self, request):
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

    def show_ik_thesaurus_async(self, request):
        """查询自定义词库状态

        该接口用于查询自定义词库的加载状态。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowIkThesaurus
        :type request: :class:`huaweicloudsdkcss.v1.ShowIkThesaurusRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowIkThesaurusResponse`
        """
        return self.show_ik_thesaurus_with_http_info(request)

    def show_ik_thesaurus_with_http_info(self, request):
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

    def show_log_backup_async(self, request):
        """查询日志

        该接口用于查询日志信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowLogBackup
        :type request: :class:`huaweicloudsdkcss.v1.ShowLogBackupRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowLogBackupResponse`
        """
        return self.show_log_backup_with_http_info(request)

    def show_log_backup_with_http_info(self, request):
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

    def show_vpcep_connection_async(self, request):
        """获取终端节点连接

        该接口用于获取终端节点连接。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowVpcepConnection
        :type request: :class:`huaweicloudsdkcss.v1.ShowVpcepConnectionRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowVpcepConnectionResponse`
        """
        return self.show_vpcep_connection_with_http_info(request)

    def show_vpcep_connection_with_http_info(self, request):
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

    def start_auto_setting_async(self, request):
        """自动设置集群快照的基础配置（不推荐使用）

        &gt;自动设置集群快照接口将会自动创建快照OBS桶和委托。如果有多个集群，每个集群使用这个接口都会创建一个不一样的OBS桶，可能会导致OBS的配额不够，较多的OBS桶也难以维护。建议可以直接使用[修改集群快照的基础配置](UpdateSnapshotSetting.xml)。
        
        该接口用于自动设置集群快照的基础配置，包括配置OBS桶和IAM委托。
        
        - “OBS桶”：快照存储的OBS桶位置。
        - “备份路径”：快照在OBS桶中的存放路径。
        - “IAM委托”：由于需要将快照保存在OBS中，所以需要在IAM中设置对应的委托获取对OBS服务的授权。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartAutoSetting
        :type request: :class:`huaweicloudsdkcss.v1.StartAutoSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartAutoSettingResponse`
        """
        return self.start_auto_setting_with_http_info(request)

    def start_auto_setting_with_http_info(self, request):
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

    def start_log_auto_backup_policy_async(self, request):
        """开启日志自动备份策略

        该接口用于日志自动备份策略开启。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartLogAutoBackupPolicy
        :type request: :class:`huaweicloudsdkcss.v1.StartLogAutoBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartLogAutoBackupPolicyResponse`
        """
        return self.start_log_auto_backup_policy_with_http_info(request)

    def start_log_auto_backup_policy_with_http_info(self, request):
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

    def start_logs_async(self, request):
        """开启日志功能

        该接口用于开启日志功能。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartLogs
        :type request: :class:`huaweicloudsdkcss.v1.StartLogsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartLogsResponse`
        """
        return self.start_logs_with_http_info(request)

    def start_logs_with_http_info(self, request):
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

    def start_public_whitelist_async(self, request):
        """开启公网访问控制白名单

        该接口用于开启公网访问控制白名单。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartPublicWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.StartPublicWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartPublicWhitelistResponse`
        """
        return self.start_public_whitelist_with_http_info(request)

    def start_public_whitelist_with_http_info(self, request):
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

    def start_vpecp_async(self, request):
        """开启终端节点服务

        该接口用于开启终端节点服务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartVpecp
        :type request: :class:`huaweicloudsdkcss.v1.StartVpecpRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartVpecpResponse`
        """
        return self.start_vpecp_with_http_info(request)

    def start_vpecp_with_http_info(self, request):
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

    def stop_log_auto_backup_policy_async(self, request):
        """关闭日志自动备份策略

        该接口用于日志自动备份策略关闭。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopLogAutoBackupPolicy
        :type request: :class:`huaweicloudsdkcss.v1.StopLogAutoBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopLogAutoBackupPolicyResponse`
        """
        return self.stop_log_auto_backup_policy_with_http_info(request)

    def stop_log_auto_backup_policy_with_http_info(self, request):
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

    def stop_logs_async(self, request):
        """关闭日志功能

        该接口用于关闭日志功能。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopLogs
        :type request: :class:`huaweicloudsdkcss.v1.StopLogsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopLogsResponse`
        """
        return self.stop_logs_with_http_info(request)

    def stop_logs_with_http_info(self, request):
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

    def stop_public_whitelist_async(self, request):
        """关闭公网访问控制白名单

        该接口用于关闭公网访问控制白名单。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopPublicWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.StopPublicWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopPublicWhitelistResponse`
        """
        return self.stop_public_whitelist_with_http_info(request)

    def stop_public_whitelist_with_http_info(self, request):
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

    def stop_snapshot_async(self, request):
        """停用快照功能

        该接口用于停用快照功能。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopSnapshot
        :type request: :class:`huaweicloudsdkcss.v1.StopSnapshotRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopSnapshotResponse`
        """
        return self.stop_snapshot_with_http_info(request)

    def stop_snapshot_with_http_info(self, request):
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

    def stop_vpecp_async(self, request):
        """关闭终端节点服务

        该接口用于关闭终端节点服务。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopVpecp
        :type request: :class:`huaweicloudsdkcss.v1.StopVpecpRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopVpecpResponse`
        """
        return self.stop_vpecp_with_http_info(request)

    def stop_vpecp_with_http_info(self, request):
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

    def update_batch_clusters_tags_async(self, request):
        """批量添加或删除集群标签

        该接口用于对集群批量添加或删除标签。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateBatchClustersTags
        :type request: :class:`huaweicloudsdkcss.v1.UpdateBatchClustersTagsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateBatchClustersTagsResponse`
        """
        return self.update_batch_clusters_tags_with_http_info(request)

    def update_batch_clusters_tags_with_http_info(self, request):
        all_params = ['cluster_id', 'resource_type', 'batch_add_or_delete_tag_on_cluster_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in local_var_params:
            path_params['cluster_id'] = local_var_params['cluster_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1.0/{project_id}/{resource_type}/{cluster_id}/tags/action',
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

    def update_cluster_name_async(self, request):
        """修改集群名称

        该接口用于修改集群名称。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateClusterName
        :type request: :class:`huaweicloudsdkcss.v1.UpdateClusterNameRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateClusterNameResponse`
        """
        return self.update_cluster_name_with_http_info(request)

    def update_cluster_name_with_http_info(self, request):
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

    def update_extend_cluster_async(self, request):
        """扩容集群

        该接口用于集群扩容实例（仅支持扩容elasticsearch实例）。只扩容普通节点，且只针对要扩容的集群实例不存在特殊节点（Master、Client、冷数据节点）的情况。
        
        集群扩容实例的数量和存储容量，请参考[扩容实例的数量和存储容量](UpdateExtendInstanceStorage.xml)。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateExtendCluster
        :type request: :class:`huaweicloudsdkcss.v1.UpdateExtendClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateExtendClusterResponse`
        """
        return self.update_extend_cluster_with_http_info(request)

    def update_extend_cluster_with_http_info(self, request):
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

    def update_extend_instance_storage_async(self, request):
        """扩容实例的数量和存储容量

        该接口用于集群扩容不同类型实例的个数以及存储容量。已经存在独立Master、Client、冷数据节点的集群使用该接口扩容。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateExtendInstanceStorage
        :type request: :class:`huaweicloudsdkcss.v1.UpdateExtendInstanceStorageRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateExtendInstanceStorageResponse`
        """
        return self.update_extend_instance_storage_with_http_info(request)

    def update_extend_instance_storage_with_http_info(self, request):
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

    def update_flavor_async(self, request):
        """变更规格

        该接口用于变更集群规格。只支持变更ess节点类型。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateFlavor
        :type request: :class:`huaweicloudsdkcss.v1.UpdateFlavorRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateFlavorResponse`
        """
        return self.update_flavor_with_http_info(request)

    def update_flavor_with_http_info(self, request):
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

    def update_flavor_by_type_async(self, request):
        """指定节点类型规格变更

        修改集群规格。支持修改:
        - ess： 数据节点。
        - ess-cold: 冷数据节点。
        - ess-client: Client节点。
        - ess-master: Master节点。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateFlavorByType
        :type request: :class:`huaweicloudsdkcss.v1.UpdateFlavorByTypeRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateFlavorByTypeResponse`
        """
        return self.update_flavor_by_type_with_http_info(request)

    def update_flavor_by_type_with_http_info(self, request):
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

    def update_log_setting_async(self, request):
        """修改日志基础配置

        该接口用于修改日志基础配置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateLogSetting
        :type request: :class:`huaweicloudsdkcss.v1.UpdateLogSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateLogSettingResponse`
        """
        return self.update_log_setting_with_http_info(request)

    def update_log_setting_with_http_info(self, request):
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

    def update_ondemand_cluster_to_period_async(self, request):
        """按需集群转包周期

        该接口用于按需集群转包周期集群。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateOndemandClusterToPeriod
        :type request: :class:`huaweicloudsdkcss.v1.UpdateOndemandClusterToPeriodRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateOndemandClusterToPeriodResponse`
        """
        return self.update_ondemand_cluster_to_period_with_http_info(request)

    def update_ondemand_cluster_to_period_with_http_info(self, request):
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

    def update_public_band_width_async(self, request):
        """修改公网访问带宽

        该接口用于修改公网访问带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePublicBandWidth
        :type request: :class:`huaweicloudsdkcss.v1.UpdatePublicBandWidthRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdatePublicBandWidthResponse`
        """
        return self.update_public_band_width_with_http_info(request)

    def update_public_band_width_with_http_info(self, request):
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

    def update_shrink_cluster_async(self, request):
        """指定节点类型缩容

        该接口用于集群对不同类型实例的个数以及存储容量进行缩容。包周期集群不支持API操作。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateShrinkCluster
        :type request: :class:`huaweicloudsdkcss.v1.UpdateShrinkClusterRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateShrinkClusterResponse`
        """
        return self.update_shrink_cluster_with_http_info(request)

    def update_shrink_cluster_with_http_info(self, request):
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

    def update_shrink_nodes_async(self, request):
        """指定节点缩容

        该接口可以对集群现有节点中指定节点进行缩容。包周期集群不支持API操作。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateShrinkNodes
        :type request: :class:`huaweicloudsdkcss.v1.UpdateShrinkNodesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateShrinkNodesResponse`
        """
        return self.update_shrink_nodes_with_http_info(request)

    def update_shrink_nodes_with_http_info(self, request):
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

    def update_snapshot_setting_async(self, request):
        """修改集群快照的基础配置

        该接口用于修改集群快照的基础配置，可修改OBS桶和IAM委托。
        
        可以使用该接口开启快照功能。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateSnapshotSetting
        :type request: :class:`huaweicloudsdkcss.v1.UpdateSnapshotSettingRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateSnapshotSettingResponse`
        """
        return self.update_snapshot_setting_with_http_info(request)

    def update_snapshot_setting_with_http_info(self, request):
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

    def update_unbind_public_async(self, request):
        """关闭公网访问

        该接口用于关闭公网访问。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateUnbindPublic
        :type request: :class:`huaweicloudsdkcss.v1.UpdateUnbindPublicRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateUnbindPublicResponse`
        """
        return self.update_unbind_public_with_http_info(request)

    def update_unbind_public_with_http_info(self, request):
        all_params = ['cluster_id', 'un_bind_public_req']
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

    def update_vpcep_connection_async(self, request):
        """更新终端节点连接

        该接口用于更新终端节点连接。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateVpcepConnection
        :type request: :class:`huaweicloudsdkcss.v1.UpdateVpcepConnectionRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateVpcepConnectionResponse`
        """
        return self.update_vpcep_connection_with_http_info(request)

    def update_vpcep_connection_with_http_info(self, request):
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

    def update_vpcep_whitelist_async(self, request):
        """修改终端节点服务白名单

        该接口用于修改终端节点服务白名单。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateVpcepWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.UpdateVpcepWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateVpcepWhitelistResponse`
        """
        return self.update_vpcep_whitelist_with_http_info(request)

    def update_vpcep_whitelist_with_http_info(self, request):
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

    def update_ymls_async(self, request):
        """修改参数配置

        该接口用于修改参数配置。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateYmls
        :type request: :class:`huaweicloudsdkcss.v1.UpdateYmlsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateYmlsResponse`
        """
        return self.update_ymls_with_http_info(request)

    def update_ymls_with_http_info(self, request):
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

    def start_kibana_public_async(self, request):
        """开启Kibana公网访问

        该接口用于开启Kibana公网访问。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartKibanaPublic
        :type request: :class:`huaweicloudsdkcss.v1.StartKibanaPublicRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartKibanaPublicResponse`
        """
        return self.start_kibana_public_with_http_info(request)

    def start_kibana_public_with_http_info(self, request):
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

    def stop_public_kibana_whitelist_async(self, request):
        """关闭Kibana公网访问控制

        该接口用于关闭Kibana公网访问控制。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopPublicKibanaWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.StopPublicKibanaWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopPublicKibanaWhitelistResponse`
        """
        return self.stop_public_kibana_whitelist_with_http_info(request)

    def stop_public_kibana_whitelist_with_http_info(self, request):
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

    def update_alter_kibana_async(self, request):
        """修改Kibana公网带宽

        该接口用于修改Kibana公网带宽。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateAlterKibana
        :type request: :class:`huaweicloudsdkcss.v1.UpdateAlterKibanaRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateAlterKibanaResponse`
        """
        return self.update_alter_kibana_with_http_info(request)

    def update_alter_kibana_with_http_info(self, request):
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

    def update_close_kibana_async(self, request):
        """关闭Kibana公网访问

        该接口用于关闭Kibana公网访问。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCloseKibana
        :type request: :class:`huaweicloudsdkcss.v1.UpdateCloseKibanaRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateCloseKibanaResponse`
        """
        return self.update_close_kibana_with_http_info(request)

    def update_close_kibana_with_http_info(self, request):
        all_params = ['cluster_id', 'close_kibana_public_req']
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

    def update_public_kibana_whitelist_async(self, request):
        """修改Kibana公网访问控制

        该接口通过修改kibana白名单，修改kibana的访问权限。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdatePublicKibanaWhitelist
        :type request: :class:`huaweicloudsdkcss.v1.UpdatePublicKibanaWhitelistRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdatePublicKibanaWhitelistResponse`
        """
        return self.update_public_kibana_whitelist_with_http_info(request)

    def update_public_kibana_whitelist_with_http_info(self, request):
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

    def add_favorite_async(self, request):
        """添加到自定义模板

        该接口用于添加到自定义模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for AddFavorite
        :type request: :class:`huaweicloudsdkcss.v1.AddFavoriteRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.AddFavoriteResponse`
        """
        return self.add_favorite_with_http_info(request)

    def add_favorite_with_http_info(self, request):
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

    def create_cnf_async(self, request):
        """创建配置文件

        该接口用于创建配置文件。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateCnf
        :type request: :class:`huaweicloudsdkcss.v1.CreateCnfRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.CreateCnfResponse`
        """
        return self.create_cnf_with_http_info(request)

    def create_cnf_with_http_info(self, request):
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

    def delete_conf_async(self, request):
        """删除配置文件

        删除配置文件。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteConf
        :type request: :class:`huaweicloudsdkcss.v1.DeleteConfRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteConfResponse`
        """
        return self.delete_conf_with_http_info(request)

    def delete_conf_with_http_info(self, request):
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

    def delete_template_async(self, request):
        """删除自定义模板

        该接口用于删除自定义模板。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkcss.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.DeleteTemplateResponse`
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        all_params = ['delete_template_req']
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

    def list_actions_async(self, request):
        """查询操作记录

        该接口用于查询操作记录。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListActions
        :type request: :class:`huaweicloudsdkcss.v1.ListActionsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListActionsResponse`
        """
        return self.list_actions_with_http_info(request)

    def list_actions_with_http_info(self, request):
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

    def list_confs_async(self, request):
        """查询配置文件列表

        该接口用于查询配置文件列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListConfs
        :type request: :class:`huaweicloudsdkcss.v1.ListConfsRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListConfsResponse`
        """
        return self.list_confs_with_http_info(request)

    def list_confs_with_http_info(self, request):
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

    def list_pipelines_async(self, request):
        """查询pipeline列表

        该接口用于查询pipeline列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListPipelines
        :type request: :class:`huaweicloudsdkcss.v1.ListPipelinesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListPipelinesResponse`
        """
        return self.list_pipelines_with_http_info(request)

    def list_pipelines_with_http_info(self, request):
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

    def list_templates_async(self, request):
        """查询模板列表

        该接口用于查询模板列表。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcss.v1.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ListTemplatesResponse`
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
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

    def show_get_conf_detail_async(self, request):
        """查询配置文件内容

        该接口用于查询配置文件内容。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowGetConfDetail
        :type request: :class:`huaweicloudsdkcss.v1.ShowGetConfDetailRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.ShowGetConfDetailResponse`
        """
        return self.show_get_conf_detail_with_http_info(request)

    def show_get_conf_detail_with_http_info(self, request):
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

    def start_connectivity_test_async(self, request):
        """连通性测试

        该接口用于连通性测试。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartConnectivityTest
        :type request: :class:`huaweicloudsdkcss.v1.StartConnectivityTestRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartConnectivityTestResponse`
        """
        return self.start_connectivity_test_with_http_info(request)

    def start_connectivity_test_with_http_info(self, request):
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

    def start_pipeline_async(self, request):
        """启动pipeline迁移数据

        该接口用于启动pipeline迁移数据。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StartPipeline
        :type request: :class:`huaweicloudsdkcss.v1.StartPipelineRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StartPipelineResponse`
        """
        return self.start_pipeline_with_http_info(request)

    def start_pipeline_with_http_info(self, request):
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

    def stop_pipeline_async(self, request):
        """停止pipeline迁移数据

        该接口用于停止pipeline迁移数据。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for StopPipeline
        :type request: :class:`huaweicloudsdkcss.v1.StopPipelineRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.StopPipelineResponse`
        """
        return self.stop_pipeline_with_http_info(request)

    def stop_pipeline_with_http_info(self, request):
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

    def update_cnf_async(self, request):
        """更新配置文件

        该接口用于更新配置文件。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateCnf
        :type request: :class:`huaweicloudsdkcss.v1.UpdateCnfRequest`
        :rtype: :class:`huaweicloudsdkcss.v1.UpdateCnfResponse`
        """
        return self.update_cnf_with_http_info(request)

    def update_cnf_with_http_info(self, request):
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

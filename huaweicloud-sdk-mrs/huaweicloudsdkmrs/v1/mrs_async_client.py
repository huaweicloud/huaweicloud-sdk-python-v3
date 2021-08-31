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


class MrsAsyncClient(Client):
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
        super(MrsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmrs.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "MrsClient":
            raise TypeError("client type error, support client type is MrsClient")

        return ClientBuilder(clazz)

    def batch_create_cluster_tags_async(self, request):
        """批量添加集群标签

        为指定集群批量添加标签。  一个集群上最多有10个标签。  此接口为幂等接口：  - 创建时，同一个集群不允许重复key，如果数据库存在就覆盖。

        :param BatchCreateClusterTagsRequest request
        :return: BatchCreateClusterTagsResponse
        """
        return self.batch_create_cluster_tags_with_http_info(request)

    def batch_create_cluster_tags_with_http_info(self, request):
        """批量添加集群标签

        为指定集群批量添加标签。  一个集群上最多有10个标签。  此接口为幂等接口：  - 创建时，同一个集群不允许重复key，如果数据库存在就覆盖。

        :param BatchCreateClusterTagsRequest request
        :return: BatchCreateClusterTagsResponse
        """

        all_params = ['cluster_id', 'batch_create_cluster_tags_request']
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
            resource_path='/v1.1/{project_id}/clusters/{cluster_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateClusterTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_cluster_tags_async(self, request):
        """批量删除集群标签

        为指定集群批量删除标签。  一个集群上最多有10个标签。  此接口为幂等接口：   - 删除时，如果删除的标签不存在，默认处理成功，删除时不对标签字符集范围做校验。Key长度36个unicode字符，value为43个unicode字符。删除时tags结构体不能缺失，key不能为空，或者空字符串。

        :param BatchDeleteClusterTagsRequest request
        :return: BatchDeleteClusterTagsResponse
        """
        return self.batch_delete_cluster_tags_with_http_info(request)

    def batch_delete_cluster_tags_with_http_info(self, request):
        """批量删除集群标签

        为指定集群批量删除标签。  一个集群上最多有10个标签。  此接口为幂等接口：   - 删除时，如果删除的标签不存在，默认处理成功，删除时不对标签字符集范围做校验。Key长度36个unicode字符，value为43个unicode字符。删除时tags结构体不能缺失，key不能为空，或者空字符串。

        :param BatchDeleteClusterTagsRequest request
        :return: BatchDeleteClusterTagsResponse
        """

        all_params = ['cluster_id', 'batch_delete_cluster_tags_request']
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
            resource_path='/v1.1/{project_id}/clusters/{cluster_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteClusterTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_cluster_async(self, request):
        """创建集群并执行作业

        创建一个MRS集群，并在集群中提交一个作业。该接口不兼容Sahara。 支持同一时间并发创建10个集群。 使用接口前，您需要先获取下的资源信息。 - 通过VPC创建或查询VPC、子网 - 通过ECS创建或查询密钥对 - 通过[终端节点](mrs_02_0003.xml)获取区域信息 - 参考[MRS组件版本一览表](https://support.huaweicloud.com/productdesc-mrs/mrs_08_0005.html)获取MRS版本及对应版本支持的组件信息  

        :param CreateClusterRequest request
        :return: CreateClusterResponse
        """
        return self.create_cluster_with_http_info(request)

    def create_cluster_with_http_info(self, request):
        """创建集群并执行作业

        创建一个MRS集群，并在集群中提交一个作业。该接口不兼容Sahara。 支持同一时间并发创建10个集群。 使用接口前，您需要先获取下的资源信息。 - 通过VPC创建或查询VPC、子网 - 通过ECS创建或查询密钥对 - 通过[终端节点](mrs_02_0003.xml)获取区域信息 - 参考[MRS组件版本一览表](https://support.huaweicloud.com/productdesc-mrs/mrs_08_0005.html)获取MRS版本及对应版本支持的组件信息  

        :param CreateClusterRequest request
        :return: CreateClusterResponse
        """

        all_params = ['cluster_req']
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
            resource_path='/v1.1/{project_id}/run-job-flow',
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


    def create_cluster_tag_async(self, request):
        """给指定集群添加标签

        为特定的集群添加一个tag。 一个集群上最多有10个标签，此接口为幂等接口。添加标签时，如果创建的标签已经存在（key相同），则覆盖。

        :param CreateClusterTagRequest request
        :return: CreateClusterTagResponse
        """
        return self.create_cluster_tag_with_http_info(request)

    def create_cluster_tag_with_http_info(self, request):
        """给指定集群添加标签

        为特定的集群添加一个tag。 一个集群上最多有10个标签，此接口为幂等接口。添加标签时，如果创建的标签已经存在（key相同），则覆盖。

        :param CreateClusterTagRequest request
        :return: CreateClusterTagResponse
        """

        all_params = ['cluster_id', 'create_tag_request']
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
            resource_path='/v1.1/{project_id}/clusters/{cluster_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateClusterTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_cluster_async(self, request):
        """删除集群

        数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。  处于如下状态的集群不允许删除： - scaling-out：扩容中 - scaling-in：缩容中 - starting：启动中 - terminating：删除中 - terminated：已删除 - failed：失败

        :param DeleteClusterRequest request
        :return: DeleteClusterResponse
        """
        return self.delete_cluster_with_http_info(request)

    def delete_cluster_with_http_info(self, request):
        """删除集群

        数据完成处理分析后或者集群运行异常无法提供服务时可删除集群服务。该接口兼容Sahara。  处于如下状态的集群不允许删除： - scaling-out：扩容中 - scaling-in：缩容中 - starting：启动中 - terminating：删除中 - terminated：已删除 - failed：失败

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
            resource_path='/v1.1/{project_id}/clusters/{cluster_id}',
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


    def delete_cluster_tag_async(self, request):
        """删除指定集群的标签

        删除特定集群的标签。

        :param DeleteClusterTagRequest request
        :return: DeleteClusterTagResponse
        """
        return self.delete_cluster_tag_with_http_info(request)

    def delete_cluster_tag_with_http_info(self, request):
        """删除指定集群的标签

        删除特定集群的标签。

        :param DeleteClusterTagRequest request
        :return: DeleteClusterTagResponse
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
            resource_path='/v1.1/{project_id}/clusters/{cluster_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteClusterTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_all_tags_async(self, request):
        """查询所有标签

        查询租户在指定Region下的所有标签集合 。

        :param ListAllTagsRequest request
        :return: ListAllTagsResponse
        """
        return self.list_all_tags_with_http_info(request)

    def list_all_tags_with_http_info(self, request):
        """查询所有标签

        查询租户在指定Region下的所有标签集合 。

        :param ListAllTagsRequest request
        :return: ListAllTagsResponse
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
            resource_path='/v1.1/{project_id}/clusters/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAllTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_cluster_tags_async(self, request):
        """查询指定集群的标签

        查询指定集群的标签信息。

        :param ListClusterTagsRequest request
        :return: ListClusterTagsResponse
        """
        return self.list_cluster_tags_with_http_info(request)

    def list_cluster_tags_with_http_info(self, request):
        """查询指定集群的标签

        查询指定集群的标签信息。

        :param ListClusterTagsRequest request
        :return: ListClusterTagsResponse
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
            resource_path='/v1.1/{project_id}/clusters/{cluster_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClusterTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_clusters_async(self, request):
        """查询集群列表

        查看用户创建的集群列表信息。该接口不兼容Sahara。

        :param ListClustersRequest request
        :return: ListClustersResponse
        """
        return self.list_clusters_with_http_info(request)

    def list_clusters_with_http_info(self, request):
        """查询集群列表

        查看用户创建的集群列表信息。该接口不兼容Sahara。

        :param ListClustersRequest request
        :return: ListClustersResponse
        """

        all_params = ['tags', 'page_size', 'current_page', 'cluster_name', 'cluster_state', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))
        if 'current_page' in local_var_params:
            query_params.append(('currentPage', local_var_params['current_page']))
        if 'cluster_name' in local_var_params:
            query_params.append(('clusterName', local_var_params['cluster_name']))
        if 'cluster_state' in local_var_params:
            query_params.append(('clusterState', local_var_params['cluster_state']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterpriseProjectId', local_var_params['enterprise_project_id']))

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
            resource_path='/v1.1/{project_id}/cluster_infos',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClustersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_clusters_by_tags_async(self, request):
        """查询特定标签的集群列表

        使用标签过滤集群。  集群默认按照创建时间倒序，集群tag也按照创建时间倒序。

        :param ListClustersByTagsRequest request
        :return: ListClustersByTagsResponse
        """
        return self.list_clusters_by_tags_with_http_info(request)

    def list_clusters_by_tags_with_http_info(self, request):
        """查询特定标签的集群列表

        使用标签过滤集群。  集群默认按照创建时间倒序，集群tag也按照创建时间倒序。

        :param ListClustersByTagsRequest request
        :return: ListClustersByTagsResponse
        """

        all_params = ['list_resource_request']
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
            resource_path='/v1.1/{project_id}/clusters/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListClustersByTagsResponse',
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

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


class ResAsyncClient(Client):
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
        super(ResAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkres.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ResClient":
            raise TypeError("client type error, support client type is ResClient")

        return ClientBuilder(clazz)

    def create_res_datasource_async(self, request):
        """创建数据源

        在指定的工作空间下面创建一个新的数据源。

        :param CreateResDatasourceRequest request
        :return: CreateResDatasourceResponse
        """
        return self.create_res_datasource_with_http_info(request)

    def create_res_datasource_with_http_info(self, request):
        """创建数据源

        在指定的工作空间下面创建一个新的数据源。

        :param CreateResDatasourceRequest request
        :return: CreateResDatasourceResponse
        """

        all_params = ['content_type', 'workspace_id', 'rest_resource_create_ds_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResDatasourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_res_job_async(self, request):
        """新建训练作业

        新建训练作业元数据，新建成功之后可手动执行此任务。

        :param CreateResJobRequest request
        :return: CreateResJobResponse
        """
        return self.create_res_job_with_http_info(request)

    def create_res_job_with_http_info(self, request):
        """新建训练作业

        新建训练作业元数据，新建成功之后可手动执行此任务。

        :param CreateResJobRequest request
        :return: CreateResJobResponse
        """

        all_params = ['content_type', 'resource_id', 'workspace_id', 'rest_training_new_instance_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_res_jobs_async(self, request):
        """新建多个训练作业

        批量新建作业。

        :param CreateResJobsRequest request
        :return: CreateResJobsResponse
        """
        return self.create_res_jobs_with_http_info(request)

    def create_res_jobs_with_http_info(self, request):
        """新建多个训练作业

        批量新建作业。

        :param CreateResJobsRequest request
        :return: CreateResJobsResponse
        """

        all_params = ['resource_id', 'workspace_id', 'rest_training_new_instances_req', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_res_online_instance_async(self, request):
        """新建在线服务

        新建在线服务元数据，新建成功之后可手动发布此服务。

        :param CreateResOnlineInstanceRequest request
        :return: CreateResOnlineInstanceResponse
        """
        return self.create_res_online_instance_with_http_info(request)

    def create_res_online_instance_with_http_info(self, request):
        """新建在线服务

        新建在线服务元数据，新建成功之后可手动发布此服务。

        :param CreateResOnlineInstanceRequest request
        :return: CreateResOnlineInstanceResponse
        """

        all_params = ['content_type', 'resource_id', 'workspace_id', 'rest_online_new_instance_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResOnlineInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_res_scene_async(self, request):
        """创建自定义场景

        在指定工作空间下面创建自定义场景。

        :param CreateResSceneRequest request
        :return: CreateResSceneResponse
        """
        return self.create_res_scene_with_http_info(request)

    def create_res_scene_with_http_info(self, request):
        """创建自定义场景

        在指定工作空间下面创建自定义场景。

        :param CreateResSceneRequest request
        :return: CreateResSceneResponse
        """

        all_params = ['content_type', 'workspace_id', 'rest_resource_create_scene_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/scenes',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResSceneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_res_workspace_async(self, request):
        """创建工作空间

        用于在推荐系统下面创建独立的工作空间，用于资源的隔离，用户可以在工作空间下面继续创建数据源、场景以及推荐任务等。是否有工作空间的操作权限取决于用户是否属于当前工作空间绑定的企业项目。

        :param CreateResWorkspaceRequest request
        :return: CreateResWorkspaceResponse
        """
        return self.create_res_workspace_with_http_info(request)

    def create_res_workspace_with_http_info(self, request):
        """创建工作空间

        用于在推荐系统下面创建独立的工作空间，用于资源的隔离，用户可以在工作空间下面继续创建数据源、场景以及推荐任务等。是否有工作空间的操作权限取决于用户是否属于当前工作空间绑定的企业项目。

        :param CreateResWorkspaceRequest request
        :return: CreateResWorkspaceResponse
        """

        all_params = ['content_type', 'create_res_workspace_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateResWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_res_datasource_async(self, request):
        """删除数据源

        删除数据源。

        :param DeleteResDatasourceRequest request
        :return: DeleteResDatasourceResponse
        """
        return self.delete_res_datasource_with_http_info(request)

    def delete_res_datasource_with_http_info(self, request):
        """删除数据源

        删除数据源。

        :param DeleteResDatasourceRequest request
        :return: DeleteResDatasourceResponse
        """

        all_params = ['content_type', 'workspace_id', 'datasource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResDatasourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_res_job_async(self, request):
        """删除训练作业

        删除指定作业。

        :param DeleteResJobRequest request
        :return: DeleteResJobResponse
        """
        return self.delete_res_job_with_http_info(request)

    def delete_res_job_with_http_info(self, request):
        """删除训练作业

        删除指定作业。

        :param DeleteResJobRequest request
        :return: DeleteResJobResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_res_online_instance_async(self, request):
        """删除在线服务

        删除在线服务实例。

        :param DeleteResOnlineInstanceRequest request
        :return: DeleteResOnlineInstanceResponse
        """
        return self.delete_res_online_instance_with_http_info(request)

    def delete_res_online_instance_with_http_info(self, request):
        """删除在线服务

        删除在线服务实例。

        :param DeleteResOnlineInstanceRequest request
        :return: DeleteResOnlineInstanceResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResOnlineInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_res_scene_async(self, request):
        """删除场景

        该接口用于删除场景，删除之后不能恢复，请您谨慎操作。

        :param DeleteResSceneRequest request
        :return: DeleteResSceneResponse
        """
        return self.delete_res_scene_with_http_info(request)

    def delete_res_scene_with_http_info(self, request):
        """删除场景

        该接口用于删除场景，删除之后不能恢复，请您谨慎操作。

        :param DeleteResSceneRequest request
        :return: DeleteResSceneResponse
        """

        all_params = ['content_type', 'workspace_id', 'scene_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/scenes/{scene_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResSceneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_res_workspace_async(self, request):
        """删除工作空间

        删除指定工作空间。

        :param DeleteResWorkspaceRequest request
        :return: DeleteResWorkspaceResponse
        """
        return self.delete_res_workspace_with_http_info(request)

    def delete_res_workspace_with_http_info(self, request):
        """删除工作空间

        删除指定工作空间。

        :param DeleteResWorkspaceRequest request
        :return: DeleteResWorkspaceResponse
        """

        all_params = ['content_type', 'workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteResWorkspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_res_datasources_async(self, request):
        """查询数据源列表

        查询当前工作空间下的数据源列表。

        :param ListResDatasourcesRequest request
        :return: ListResDatasourcesResponse
        """
        return self.list_res_datasources_with_http_info(request)

    def list_res_datasources_with_http_info(self, request):
        """查询数据源列表

        查询当前工作空间下的数据源列表。

        :param ListResDatasourcesRequest request
        :return: ListResDatasourcesResponse
        """

        all_params = ['content_type', 'workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResDatasourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_res_enterprises_async(self, request):
        """查询企业项目列表

        查询用户在当前项目id下的企业项目列表。在创建工作空间时需要提供企业项目id。

        :param ListResEnterprisesRequest request
        :return: ListResEnterprisesResponse
        """
        return self.list_res_enterprises_with_http_info(request)

    def list_res_enterprises_with_http_info(self, request):
        """查询企业项目列表

        查询用户在当前项目id下的企业项目列表。在创建工作空间时需要提供企业项目id。

        :param ListResEnterprisesRequest request
        :return: ListResEnterprisesResponse
        """

        all_params = ['content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/enterprise-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResEnterprisesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_res_online_service_details_async(self, request):
        """查询在线服务详情

        根据给定的workspace_id和resource_id及category查询在线服务。

        :param ListResOnlineServiceDetailsRequest request
        :return: ListResOnlineServiceDetailsResponse
        """
        return self.list_res_online_service_details_with_http_info(request)

    def list_res_online_service_details_with_http_info(self, request):
        """查询在线服务详情

        根据给定的workspace_id和resource_id及category查询在线服务。

        :param ListResOnlineServiceDetailsRequest request
        :return: ListResOnlineServiceDetailsResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'category']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResOnlineServiceDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_res_resource_spec_async(self, request):
        """查询训练规格

        查询当前推荐系统所提供的离线计算规格，实时计算规格和排序模型训练规格。在创建数据源和场景时，需要提供此信息。

        :param ListResResourceSpecRequest request
        :return: ListResResourceSpecResponse
        """
        return self.list_res_resource_spec_with_http_info(request)

    def list_res_resource_spec_with_http_info(self, request):
        """查询训练规格

        查询当前推荐系统所提供的离线计算规格，实时计算规格和排序模型训练规格。在创建数据源和场景时，需要提供此信息。

        :param ListResResourceSpecRequest request
        :return: ListResResourceSpecResponse
        """

        all_params = ['content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/resource-specs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResResourceSpecResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_res_scenes_async(self, request):
        """查询场景列表

        查询当前工作空间下的场景列表。

        :param ListResScenesRequest request
        :return: ListResScenesResponse
        """
        return self.list_res_scenes_with_http_info(request)

    def list_res_scenes_with_http_info(self, request):
        """查询场景列表

        查询当前工作空间下的场景列表。

        :param ListResScenesRequest request
        :return: ListResScenesResponse
        """

        all_params = ['content_type', 'workspace_id', 'category']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/scenes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResScenesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_res_workspaces_async(self, request):
        """查询工作空间列表

        用于查询当前用户具有操作权限的工作空间列表。

        :param ListResWorkspacesRequest request
        :return: ListResWorkspacesResponse
        """
        return self.list_res_workspaces_with_http_info(request)

    def list_res_workspaces_with_http_info(self, request):
        """查询工作空间列表

        用于查询当前用户具有操作权限的工作空间列表。

        :param ListResWorkspacesRequest request
        :return: ListResWorkspacesResponse
        """

        all_params = ['content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListResWorkspacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_res_datasource_async(self, request):
        """查询数据源详情

        查询指定数据源的详情信息。

        :param ShowResDatasourceRequest request
        :return: ShowResDatasourceResponse
        """
        return self.show_res_datasource_with_http_info(request)

    def show_res_datasource_with_http_info(self, request):
        """查询数据源详情

        查询指定数据源的详情信息。

        :param ShowResDatasourceRequest request
        :return: ShowResDatasourceResponse
        """

        all_params = ['content_type', 'workspace_id', 'datasource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResDatasourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_res_datasource_work_detail_async(self, request):
        """查询数据源任务结果

        查询指定数据源下离线任务的结果。其中包括数据格式，数据检测、数据探索及效果评估的内容。

        :param ShowResDatasourceWorkDetailRequest request
        :return: ShowResDatasourceWorkDetailResponse
        """
        return self.show_res_datasource_work_detail_with_http_info(request)

    def show_res_datasource_work_detail_with_http_info(self, request):
        """查询数据源任务结果

        查询指定数据源下离线任务的结果。其中包括数据格式，数据检测、数据探索及效果评估的内容。

        :param ShowResDatasourceWorkDetailRequest request
        :return: ShowResDatasourceWorkDetailResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{resource_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResDatasourceWorkDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_res_job_async(self, request):
        """查询训练作业

        查询resource_id（数据源id或场景id）下的指定类型的作业。

        :param ShowResJobRequest request
        :return: ShowResJobResponse
        """
        return self.show_res_job_with_http_info(request)

    def show_res_job_with_http_info(self, request):
        """查询训练作业

        查询resource_id（数据源id或场景id）下的指定类型的作业。

        :param ShowResJobRequest request
        :return: ShowResJobResponse
        """

        all_params = ['workspace_id', 'resource_id', 'category', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_res_recall_set_async(self, request):
        """查询训练作业候选集

        查询给定workspaces_id和指定resource_id下的候选集。

        :param ShowResRecallSetRequest request
        :return: ShowResRecallSetResponse
        """
        return self.show_res_recall_set_with_http_info(request)

    def show_res_recall_set_with_http_info(self, request):
        """查询训练作业候选集

        查询给定workspaces_id和指定resource_id下的候选集。

        :param ShowResRecallSetRequest request
        :return: ShowResRecallSetResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'use_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'use_type' in local_var_params:
            query_params.append(('use_type', local_var_params['use_type']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/result-set',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResRecallSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_res_scene_async(self, request):
        """查询场景详情

        查询指定场景的详情。

        :param ShowResSceneRequest request
        :return: ShowResSceneResponse
        """
        return self.show_res_scene_with_http_info(request)

    def show_res_scene_with_http_info(self, request):
        """查询场景详情

        查询指定场景的详情。

        :param ShowResSceneRequest request
        :return: ShowResSceneResponse
        """

        all_params = ['content_type', 'workspace_id', 'scene_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/scenes/{scene_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResSceneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_res_wrokspace_async(self, request):
        """查询工作空间详情

        查询指定工作空间的具体信息。

        :param ShowResWrokspaceRequest request
        :return: ShowResWrokspaceResponse
        """
        return self.show_res_wrokspace_with_http_info(request)

    def show_res_wrokspace_with_http_info(self, request):
        """查询工作空间详情

        查询指定工作空间的具体信息。

        :param ShowResWrokspaceRequest request
        :return: ShowResWrokspaceResponse
        """

        all_params = ['content_type', 'workspace_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowResWrokspaceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_res_job_async(self, request):
        """执行作业

        执行独立的作业。

        :param StartResJobRequest request
        :return: StartResJobResponse
        """
        return self.start_res_job_with_http_info(request)

    def start_res_job_with_http_info(self, request):
        """执行作业

        执行独立的作业。

        :param StartResJobRequest request
        :return: StartResJobResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'job_id', 'action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/jobs/{job_id}/schedule-job',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartResJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_res_scene_jobs_async(self, request):
        """执行场景

        执行场景下面的所有作业和服务。

        :param StartResSceneJobsRequest request
        :return: StartResSceneJobsResponse
        """
        return self.start_res_scene_jobs_with_http_info(request)

    def start_res_scene_jobs_with_http_info(self, request):
        """执行场景

        执行场景下面的所有作业和服务。

        :param StartResSceneJobsRequest request
        :return: StartResSceneJobsResponse
        """

        all_params = ['content_type', 'workspace_id', 'resource_id', 'action']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/schedule-scene',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartResSceneJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_res_datasource_async(self, request):
        """修改数据源内容

        修改指定数据源的配置内容。

        :param UpdateResDatasourceRequest request
        :return: UpdateResDatasourceResponse
        """
        return self.update_res_datasource_with_http_info(request)

    def update_res_datasource_with_http_info(self, request):
        """修改数据源内容

        修改指定数据源的配置内容。

        :param UpdateResDatasourceRequest request
        :return: UpdateResDatasourceResponse
        """

        all_params = ['content_type', 'datasource_id', 'workspace_id', 'rest_resource_put_ds_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResDatasourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_res_datastruct_async(self, request):
        """修改数据源特征

        修改数据源中的特征。

        :param UpdateResDatastructRequest request
        :return: UpdateResDatastructResponse
        """
        return self.update_res_datastruct_with_http_info(request)

    def update_res_datastruct_with_http_info(self, request):
        """修改数据源特征

        修改数据源中的特征。

        :param UpdateResDatastructRequest request
        :return: UpdateResDatastructResponse
        """

        all_params = ['content_type', 'datasource_id', 'workspace_id', 'rest_resource_put_ds_data_sturct_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/data-sources/{datasource_id}/data-struct',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResDatastructResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_res_job_async(self, request):
        """修改训练作业参数

        修改指定作业的元数据信息。

        :param UpdateResJobRequest request
        :return: UpdateResJobResponse
        """
        return self.update_res_job_with_http_info(request)

    def update_res_job_with_http_info(self, request):
        """修改训练作业参数

        修改指定作业的元数据信息。

        :param UpdateResJobRequest request
        :return: UpdateResJobResponse
        """

        all_params = ['job_id', 'resource_id', 'workspace_id', 'rest_training_put_instance_req', 'content_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/job-instance/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_res_online_instance_async(self, request):
        """修改在线服务参数

        修改指定在线服务的元数据内容。

        :param UpdateResOnlineInstanceRequest request
        :return: UpdateResOnlineInstanceResponse
        """
        return self.update_res_online_instance_with_http_info(request)

    def update_res_online_instance_with_http_info(self, request):
        """修改在线服务参数

        修改指定在线服务的元数据内容。

        :param UpdateResOnlineInstanceRequest request
        :return: UpdateResOnlineInstanceResponse
        """

        all_params = ['content_type', 'job_id', 'resource_id', 'workspace_id', 'rest_onilne_put_instance_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'content_type' in local_var_params:
            query_params.append(('Content-Type', local_var_params['content_type']))

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/resources/{resource_id}/service-instance/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResOnlineInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_res_scene_async(self, request):
        """更新自定义场景内容

        更新自定义场景的内容信息。

        :param UpdateResSceneRequest request
        :return: UpdateResSceneResponse
        """
        return self.update_res_scene_with_http_info(request)

    def update_res_scene_with_http_info(self, request):
        """更新自定义场景内容

        更新自定义场景的内容信息。

        :param UpdateResSceneRequest request
        :return: UpdateResSceneResponse
        """

        all_params = ['content_type', 'scene_id', 'workspace_id', 'rest_resource_put_scene_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'scene_id' in local_var_params:
            path_params['scene_id'] = local_var_params['scene_id']
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}/scenes/{scene_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResSceneResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_res_workspace_async(self, request):
        """更新工作空间

        更新工作空间信息, 只允许更新描述信息。

        :param UpdateResWorkspaceRequest request
        :return: UpdateResWorkspaceResponse
        """
        return self.update_res_workspace_with_http_info(request)

    def update_res_workspace_with_http_info(self, request):
        """更新工作空间

        更新工作空间信息, 只允许更新描述信息。

        :param UpdateResWorkspaceRequest request
        :return: UpdateResWorkspaceResponse
        """

        all_params = ['content_type', 'workspace_id', 'update_res_workspace_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'content_type' in local_var_params:
            header_params['Content-Type'] = local_var_params['content_type']

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
            resource_path='/v2.0/{project_id}/workspaces/{workspace_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateResWorkspaceResponse',
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

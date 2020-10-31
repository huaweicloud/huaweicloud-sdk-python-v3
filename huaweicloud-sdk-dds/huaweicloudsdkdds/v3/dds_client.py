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


class DdsClient(Client):
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
        super(DdsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdds.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def add_sharding_node(self, request):
        """扩容指定集群实例的节点数量

        扩容指定集群实例的节点数量。

        :param AddShardingNodeRequest request
        :return: AddShardingNodeResponse
        """
        return self.add_sharding_node_with_http_info(request)

    def add_sharding_node_with_http_info(self, request):
        """扩容指定集群实例的节点数量

        扩容指定集群实例的节点数量。

        :param AddShardingNodeRequest request
        :return: AddShardingNodeResponse
        """

        all_params = ['instance_id', 'add_sharding_node_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddShardingNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_create_instance_tags(self, request):
        """批量添加指定实例的标签

        批量添加指定实例的标签。

        :param BatchCreateInstanceTagsRequest request
        :return: BatchCreateInstanceTagsResponse
        """
        return self.batch_create_instance_tags_with_http_info(request)

    def batch_create_instance_tags_with_http_info(self, request):
        """批量添加指定实例的标签

        批量添加指定实例的标签。

        :param BatchCreateInstanceTagsRequest request
        :return: BatchCreateInstanceTagsResponse
        """

        all_params = ['instance_id', 'batch_create_instance_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_instance_tags(self, request):
        """批量删除指定实例的标签

        批量删除指定实例的标签。

        :param BatchDeleteInstanceTagsRequest request
        :return: BatchDeleteInstanceTagsResponse
        """
        return self.batch_delete_instance_tags_with_http_info(request)

    def batch_delete_instance_tags_with_http_info(self, request):
        """批量删除指定实例的标签

        批量删除指定实例的标签。

        :param BatchDeleteInstanceTagsRequest request
        :return: BatchDeleteInstanceTagsResponse
        """

        all_params = ['instance_id', 'batch_delete_instance_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_instance(self, request):
        """创建文档数据库实例，包括集群实例、副本集实例、以及单节点实例。

        创建文档数据库实例，包括集群实例、副本集实例、以及单节点实例。

        :param CreateInstanceRequest request
        :return: CreateInstanceResponse
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        """创建文档数据库实例，包括集群实例、副本集实例、以及单节点实例。

        创建文档数据库实例，包括集群实例、副本集实例、以及单节点实例。

        :param CreateInstanceRequest request
        :return: CreateInstanceResponse
        """

        all_params = ['create_instance_request_body']
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
            resource_path='/v3/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_manual_backup(self, request):
        """创建数据库实例的手动备份

        创建数据库实例的手动备份。

        :param CreateManualBackupRequest request
        :return: CreateManualBackupResponse
        """
        return self.create_manual_backup_with_http_info(request)

    def create_manual_backup_with_http_info(self, request):
        """创建数据库实例的手动备份

        创建数据库实例的手动备份。

        :param CreateManualBackupRequest request
        :return: CreateManualBackupResponse
        """

        all_params = ['create_manual_backup_request_body']
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
            resource_path='/v3/{project_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateManualBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_instance(self, request):
        """删除数据库实例

        删除数据库实例。

        :param DeleteInstanceRequest request
        :return: DeleteInstanceResponse
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        """删除数据库实例

        删除数据库实例。

        :param DeleteInstanceRequest request
        :return: DeleteInstanceResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_manual_backup(self, request):
        """删除数据库实例的手动备份

        删除数据库实例的手动备份。

        :param DeleteManualBackupRequest request
        :return: DeleteManualBackupResponse
        """
        return self.delete_manual_backup_with_http_info(request)

    def delete_manual_backup_with_http_info(self, request):
        """删除数据库实例的手动备份

        删除数据库实例的手动备份。

        :param DeleteManualBackupRequest request
        :return: DeleteManualBackupResponse
        """

        all_params = ['backup_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteManualBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_backups(self, request):
        """根据指定条件查询备份列表

        根据指定条件查询备份列表。

        :param ListBackupsRequest request
        :return: ListBackupsResponse
        """
        return self.list_backups_with_http_info(request)

    def list_backups_with_http_info(self, request):
        """根据指定条件查询备份列表

        根据指定条件查询备份列表。

        :param ListBackupsRequest request
        :return: ListBackupsResponse
        """

        all_params = ['instance_id', 'backup_id', 'backup_type', 'offset', 'limit', 'begin_time', 'end_time', 'mode']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'backup_id' in local_var_params:
            query_params.append(('backup_id', local_var_params['backup_id']))
        if 'backup_type' in local_var_params:
            query_params.append(('backup_type', local_var_params['backup_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_datastore_versions(self, request):
        """查询数据库版本信息

        查询指定实例类型的数据库版本信息。

        :param ListDatastoreVersionsRequest request
        :return: ListDatastoreVersionsResponse
        """
        return self.list_datastore_versions_with_http_info(request)

    def list_datastore_versions_with_http_info(self, request):
        """查询数据库版本信息

        查询指定实例类型的数据库版本信息。

        :param ListDatastoreVersionsRequest request
        :return: ListDatastoreVersionsResponse
        """

        all_params = ['datastore_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datastore_name' in local_var_params:
            path_params['datastore_name'] = local_var_params['datastore_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/datastores/{datastore_name}/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDatastoreVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors(self, request):
        """查询指定条件下的所有实例规格信息

        查询指定条件下的所有实例规格信息。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """查询指定条件下的所有实例规格信息

        查询指定条件下的所有实例规格信息。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """

        all_params = ['region', 'engine_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'engine_name' in local_var_params:
            query_params.append(('engine_name', local_var_params['engine_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/flavors',
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


    def list_instance_tags(self, request):
        """查询指定实例的标签信息

        查询指定实例的标签信息。

        :param ListInstanceTagsRequest request
        :return: ListInstanceTagsResponse
        """
        return self.list_instance_tags_with_http_info(request)

    def list_instance_tags_with_http_info(self, request):
        """查询指定实例的标签信息

        查询指定实例的标签信息。

        :param ListInstanceTagsRequest request
        :return: ListInstanceTagsResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instances(self, request):
        """根据指定条件查询实例列表

        根据指定条件查询实例列表。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        """根据指定条件查询实例列表

        根据指定条件查询实例列表。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """

        all_params = ['id', 'name', 'mode', 'datastore_type', 'vpc_id', 'subnet_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instances_by_tags(self, request):
        """根据标签查询指定的数据库实例

        根据标签查询指定的数据库实例。

        :param ListInstancesByTagsRequest request
        :return: ListInstancesByTagsResponse
        """
        return self.list_instances_by_tags_with_http_info(request)

    def list_instances_by_tags_with_http_info(self, request):
        """根据标签查询指定的数据库实例

        根据标签查询指定的数据库实例。

        :param ListInstancesByTagsRequest request
        :return: ListInstancesByTagsResponse
        """

        all_params = ['list_instances_by_tags_request_body']
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
            resource_path='/v3/{project_id}/instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_project_tags(self, request):
        """查询指定project ID下实例的所有标签集合

        查询指定project ID下实例的所有标签集合。

        :param ListProjectTagsRequest request
        :return: ListProjectTagsResponse
        """
        return self.list_project_tags_with_http_info(request)

    def list_project_tags_with_http_info(self, request):
        """查询指定project ID下实例的所有标签集合

        查询指定project ID下实例的所有标签集合。

        :param ListProjectTagsRequest request
        :return: ListProjectTagsResponse
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


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def resize_instance(self, request):
        """变更实例的规格

        变更实例的规格。

        :param ResizeInstanceRequest request
        :return: ResizeInstanceResponse
        """
        return self.resize_instance_with_http_info(request)

    def resize_instance_with_http_info(self, request):
        """变更实例的规格

        变更实例的规格。

        :param ResizeInstanceRequest request
        :return: ResizeInstanceResponse
        """

        all_params = ['instance_id', 'resize_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def resize_instance_volume(self, request):
        """扩容实例相关的存储容量大小

        扩容实例相关的存储容量大小。

        :param ResizeInstanceVolumeRequest request
        :return: ResizeInstanceVolumeResponse
        """
        return self.resize_instance_volume_with_http_info(request)

    def resize_instance_volume_with_http_info(self, request):
        """扩容实例相关的存储容量大小

        扩容实例相关的存储容量大小。

        :param ResizeInstanceVolumeRequest request
        :return: ResizeInstanceVolumeResponse
        """

        all_params = ['instance_id', 'resize_instance_volume_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/enlarge-volume',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ResizeInstanceVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restart_instance(self, request):
        """重启实例的数据库服务

        重启实例的数据库服务。

        :param RestartInstanceRequest request
        :return: RestartInstanceResponse
        """
        return self.restart_instance_with_http_info(request)

    def restart_instance_with_http_info(self, request):
        """重启实例的数据库服务

        重启实例的数据库服务。

        :param RestartInstanceRequest request
        :return: RestartInstanceResponse
        """

        all_params = ['instance_id', 'restart_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestartInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def set_backup_policy(self, request):
        """设置自动备份策略

        设置自动备份策略。 x-constraint: |- - 该接口支持DDS社区版和增强版。

        :param SetBackupPolicyRequest request
        :return: SetBackupPolicyResponse
        """
        return self.set_backup_policy_with_http_info(request)

    def set_backup_policy_with_http_info(self, request):
        """设置自动备份策略

        设置自动备份策略。 x-constraint: |- - 该接口支持DDS社区版和增强版。

        :param SetBackupPolicyRequest request
        :return: SetBackupPolicyResponse
        """

        all_params = ['instance_id', 'set_backup_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SetBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_backup_policy(self, request):
        """查询自动备份策略

        查询自动备份策略。

        :param ShowBackupPolicyRequest request
        :return: ShowBackupPolicyResponse
        """
        return self.show_backup_policy_with_http_info(request)

    def show_backup_policy_with_http_info(self, request):
        """查询自动备份策略

        查询自动备份策略。

        :param ShowBackupPolicyRequest request
        :return: ShowBackupPolicyResponse
        """

        all_params = ['instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBackupPolicyResponse',
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

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


class DcsAsyncClient(Client):
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
        super(DcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdcs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def batch_create_or_delete_tags_async(self, request):
        """批量添加或删除标签

        为指定实例批量添加标签，或批量删除标签。

        :param BatchCreateOrDeleteTagsRequest request
        :return: BatchCreateOrDeleteTagsResponse
        """
        return self.batch_create_or_delete_tags_with_http_info(request)

    def batch_create_or_delete_tags_with_http_info(self, request):
        """批量添加或删除标签

        为指定实例批量添加标签，或批量删除标签。

        :param BatchCreateOrDeleteTagsRequest request
        :return: BatchCreateOrDeleteTagsResponse
        """

        all_params = ['instance_id', 'batch_create_or_delete_tags_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/dcs/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateOrDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_instances_async(self, request):
        """批量删除实例

        批量删除多个缓存实例。

        :param BatchDeleteInstancesRequest request
        :return: BatchDeleteInstancesResponse
        """
        return self.batch_delete_instances_with_http_info(request)

    def batch_delete_instances_with_http_info(self, request):
        """批量删除实例

        批量删除多个缓存实例。

        :param BatchDeleteInstancesRequest request
        :return: BatchDeleteInstancesResponse
        """

        all_params = ['all_failure', 'batch_delete_instances_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'all_failure' in local_var_params:
            query_params.append(('all_failure', local_var_params['all_failure']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_master_standby_async(self, request):
        """主备切换

        切换实例主备节点，只有主备实例支持该操作。

        :param ChangeMasterStandbyRequest request
        :return: ChangeMasterStandbyResponse
        """
        return self.change_master_standby_with_http_info(request)

    def change_master_standby_with_http_info(self, request):
        """主备切换

        切换实例主备节点，只有主备实例支持该操作。

        :param ChangeMasterStandbyRequest request
        :return: ChangeMasterStandbyResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/swap',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeMasterStandbyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def copy_instance_async(self, request):
        """备份指定实例

        备份指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param CopyInstanceRequest request
        :return: CopyInstanceResponse
        """
        return self.copy_instance_with_http_info(request)

    def copy_instance_with_http_info(self, request):
        """备份指定实例

        备份指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param CopyInstanceRequest request
        :return: CopyInstanceResponse
        """

        all_params = ['instance_id', 'copy_instance_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CopyInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_bigkey_scan_task_async(self, request):
        """创建大key分析任务

        为Redis实例创建大key分析任务。

        :param CreateBigkeyScanTaskRequest request
        :return: CreateBigkeyScanTaskResponse
        """
        return self.create_bigkey_scan_task_with_http_info(request)

    def create_bigkey_scan_task_with_http_info(self, request):
        """创建大key分析任务

        为Redis实例创建大key分析任务。

        :param CreateBigkeyScanTaskRequest request
        :return: CreateBigkeyScanTaskResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBigkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_hotkey_scan_task_async(self, request):
        """创建热key分析任务

        创建热key分析任务，Redis 3.0 不支持热key分析。  热key分析需要将缓存实例配置参数maxmemory-policy设置为allkeys-lfu或volatile-lfu。 

        :param CreateHotkeyScanTaskRequest request
        :return: CreateHotkeyScanTaskResponse
        """
        return self.create_hotkey_scan_task_with_http_info(request)

    def create_hotkey_scan_task_with_http_info(self, request):
        """创建热key分析任务

        创建热key分析任务，Redis 3.0 不支持热key分析。  热key分析需要将缓存实例配置参数maxmemory-policy设置为allkeys-lfu或volatile-lfu。 

        :param CreateHotkeyScanTaskRequest request
        :return: CreateHotkeyScanTaskResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateHotkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_instance_async(self, request):
        """创建缓存实例

        创建缓存实例，该接口创建的缓存实例支持按需计费和包周期两种方式。

        :param CreateInstanceRequest request
        :return: CreateInstanceResponse
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        """创建缓存实例

        创建缓存实例，该接口创建的缓存实例支持按需计费和包周期两种方式。

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
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


    def create_migration_task_async(self, request):
        """创建数据迁移任务

        创建数据迁移任务。

        :param CreateMigrationTaskRequest request
        :return: CreateMigrationTaskResponse
        """
        return self.create_migration_task_with_http_info(request)

    def create_migration_task_with_http_info(self, request):
        """创建数据迁移任务

        创建数据迁移任务。

        :param CreateMigrationTaskRequest request
        :return: CreateMigrationTaskResponse
        """

        all_params = ['create_migration_task_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_replication_async(self, request):
        """添加副本

        为Cluster集群实例的分片添加副本。

        :param CreateReplicationRequest request
        :return: CreateReplicationResponse
        """
        return self.create_replication_with_http_info(request)

    def create_replication_with_http_info(self, request):
        """添加副本

        为Cluster集群实例的分片添加副本。

        :param CreateReplicationRequest request
        :return: CreateReplicationResponse
        """

        all_params = ['instance_id', 'group_id', 'create_replication_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instance/{instance_id}/groups/{group_id}/replications',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_background_task_async(self, request):
        """删除后台任务

        删除后台任务

        :param DeleteBackgroundTaskRequest request
        :return: DeleteBackgroundTaskResponse
        """
        return self.delete_background_task_with_http_info(request)

    def delete_background_task_with_http_info(self, request):
        """删除后台任务

        删除后台任务

        :param DeleteBackgroundTaskRequest request
        :return: DeleteBackgroundTaskResponse
        """

        all_params = ['instance_id', 'task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_backup_file_async(self, request):
        """删除备份文件

        删除缓存实例已备份的文件。

        :param DeleteBackupFileRequest request
        :return: DeleteBackupFileResponse
        """
        return self.delete_backup_file_with_http_info(request)

    def delete_backup_file_with_http_info(self, request):
        """删除备份文件

        删除缓存实例已备份的文件。

        :param DeleteBackupFileRequest request
        :return: DeleteBackupFileResponse
        """

        all_params = ['backup_id', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
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
            resource_path='/v2/{project_id}/instances/{instance_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBackupFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_bigkey_scan_task_async(self, request):
        """删除大key分析记录

        删除大key分析记录。

        :param DeleteBigkeyScanTaskRequest request
        :return: DeleteBigkeyScanTaskResponse
        """
        return self.delete_bigkey_scan_task_with_http_info(request)

    def delete_bigkey_scan_task_with_http_info(self, request):
        """删除大key分析记录

        删除大key分析记录。

        :param DeleteBigkeyScanTaskRequest request
        :return: DeleteBigkeyScanTaskResponse
        """

        all_params = ['instance_id', 'bigkey_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'bigkey_id' in local_var_params:
            path_params['bigkey_id'] = local_var_params['bigkey_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-task/{bigkey_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBigkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_hotkey_scan_task_async(self, request):
        """删除热key分析任务

        删除热key分析任务。

        :param DeleteHotkeyScanTaskRequest request
        :return: DeleteHotkeyScanTaskResponse
        """
        return self.delete_hotkey_scan_task_with_http_info(request)

    def delete_hotkey_scan_task_with_http_info(self, request):
        """删除热key分析任务

        删除热key分析任务。

        :param DeleteHotkeyScanTaskRequest request
        :return: DeleteHotkeyScanTaskResponse
        """

        all_params = ['instance_id', 'hotkey_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'hotkey_id' in local_var_params:
            path_params['hotkey_id'] = local_var_params['hotkey_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-task/{hotkey_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteHotkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_ip_from_domain_name_async(self, request):
        """域名摘除IP

        将只读副本的IP从域名中摘除，摘除成功后，只读域名不会再解析到该副本IP。

        :param DeleteIpFromDomainNameRequest request
        :return: DeleteIpFromDomainNameResponse
        """
        return self.delete_ip_from_domain_name_with_http_info(request)

    def delete_ip_from_domain_name_with_http_info(self, request):
        """域名摘除IP

        将只读副本的IP从域名中摘除，摘除成功后，只读域名不会再解析到该副本IP。

        :param DeleteIpFromDomainNameRequest request
        :return: DeleteIpFromDomainNameResponse
        """

        all_params = ['instance_id', 'group_id', 'node_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/remove-ip',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteIpFromDomainNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_migration_task_async(self, request):
        """删除数据迁移任务

        删除数据迁移任务。

        :param DeleteMigrationTaskRequest request
        :return: DeleteMigrationTaskResponse
        """
        return self.delete_migration_task_with_http_info(request)

    def delete_migration_task_with_http_info(self, request):
        """删除数据迁移任务

        删除数据迁移任务。

        :param DeleteMigrationTaskRequest request
        :return: DeleteMigrationTaskResponse
        """

        all_params = ['delete_migration_task_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-tasks/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_replication_async(self, request):
        """删除副本

        为Cluster集群删除指定副本

        :param DeleteReplicationRequest request
        :return: DeleteReplicationResponse
        """
        return self.delete_replication_with_http_info(request)

    def delete_replication_with_http_info(self, request):
        """删除副本

        为Cluster集群删除指定副本

        :param DeleteReplicationRequest request
        :return: DeleteReplicationResponse
        """

        all_params = ['instance_id', 'group_id', 'node_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_single_instance_async(self, request):
        """删除实例

        删除指定的缓存实例，释放该实例的所有资源。  > 如果是删除按需资源，请按照本章节执行；如果是删除包周期资源，即退订，请参考[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html#section2)。 

        :param DeleteSingleInstanceRequest request
        :return: DeleteSingleInstanceResponse
        """
        return self.delete_single_instance_with_http_info(request)

    def delete_single_instance_with_http_info(self, request):
        """删除实例

        删除指定的缓存实例，释放该实例的所有资源。  > 如果是删除按需资源，请按照本章节执行；如果是删除包周期资源，即退订，请参考[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html#section2)。 

        :param DeleteSingleInstanceRequest request
        :return: DeleteSingleInstanceResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSingleInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_available_zones_async(self, request):
        """查询可用区信息

        查询所在局点的可用区信息

        :param ListAvailableZonesRequest request
        :return: ListAvailableZonesResponse
        """
        return self.list_available_zones_with_http_info(request)

    def list_available_zones_with_http_info(self, request):
        """查询可用区信息

        查询所在局点的可用区信息

        :param ListAvailableZonesRequest request
        :return: ListAvailableZonesResponse
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
            resource_path='/v2/available-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAvailableZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_background_task_async(self, request):
        """查询后台任务列表

        查询后台任务列表

        :param ListBackgroundTaskRequest request
        :return: ListBackgroundTaskResponse
        """
        return self.list_background_task_with_http_info(request)

    def list_background_task_with_http_info(self, request):
        """查询后台任务列表

        查询后台任务列表

        :param ListBackgroundTaskRequest request
        :return: ListBackgroundTaskResponse
        """

        all_params = ['instance_id', 'offset', 'limit', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_backup_file_links_async(self, request):
        """获取备份文件下载链接

        获取指定实例的备份文件下载链接，下载备份文件。

        :param ListBackupFileLinksRequest request
        :return: ListBackupFileLinksResponse
        """
        return self.list_backup_file_links_with_http_info(request)

    def list_backup_file_links_with_http_info(self, request):
        """获取备份文件下载链接

        获取指定实例的备份文件下载链接，下载备份文件。

        :param ListBackupFileLinksRequest request
        :return: ListBackupFileLinksResponse
        """

        all_params = ['instance_id', 'backup_id', 'list_backup_file_links_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/backups/{backup_id}/links',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupFileLinksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_backup_records_async(self, request):
        """查询实例备份信息

        查询指定缓存实例的备份信息列表。

        :param ListBackupRecordsRequest request
        :return: ListBackupRecordsResponse
        """
        return self.list_backup_records_with_http_info(request)

    def list_backup_records_with_http_info(self, request):
        """查询实例备份信息

        查询指定缓存实例的备份信息列表。

        :param ListBackupRecordsRequest request
        :return: ListBackupRecordsResponse
        """

        all_params = ['instance_id', 'begin_time', 'end_time', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBackupRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_bigkey_scan_tasks_async(self, request):
        """查询大key分析任务列表

        查询大key分析任务列表。

        :param ListBigkeyScanTasksRequest request
        :return: ListBigkeyScanTasksResponse
        """
        return self.list_bigkey_scan_tasks_with_http_info(request)

    def list_bigkey_scan_tasks_with_http_info(self, request):
        """查询大key分析任务列表

        查询大key分析任务列表。

        :param ListBigkeyScanTasksRequest request
        :return: ListBigkeyScanTasksResponse
        """

        all_params = ['instance_id', 'offset', 'limit', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBigkeyScanTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ces_monitored_objects_async(self, request):
        """查询主维度信息列表

        查询主维度对象列表，主维度ID当前支持dcs_instance_id，dcs_memcached_instance_id。 > 该接口当前仅在中国华南区开放。 

        :param ListCESMonitoredObjectsRequest request
        :return: ListCESMonitoredObjectsResponse
        """
        return self.list_ces_monitored_objects_with_http_info(request)

    def list_ces_monitored_objects_with_http_info(self, request):
        """查询主维度信息列表

        查询主维度对象列表，主维度ID当前支持dcs_instance_id，dcs_memcached_instance_id。 > 该接口当前仅在中国华南区开放。 

        :param ListCESMonitoredObjectsRequest request
        :return: ListCESMonitoredObjectsResponse
        """

        all_params = ['dim_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))
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
            resource_path='/v2/{project_id}/dims/monitored-objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCESMonitoredObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_configurations_async(self, request):
        """查询实例配置参数

        查询指定实例的配置参数信息。

        :param ListConfigurationsRequest request
        :return: ListConfigurationsResponse
        """
        return self.list_configurations_with_http_info(request)

    def list_configurations_with_http_info(self, request):
        """查询实例配置参数

        查询指定实例的配置参数信息。

        :param ListConfigurationsRequest request
        :return: ListConfigurationsResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors_async(self, request):
        """查询产品规格

        在创建缓存实例时，需要配置订购的产品规格编码（spec_code），可通过该接口查询产品规格，查询条件不选时默认查询全部。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """查询产品规格

        在创建缓存实例时，需要配置订购的产品规格编码（spec_code），可通过该接口查询产品规格，查询条件不选时默认查询全部。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """

        all_params = ['spec_code', 'cache_mode', 'engine', 'engine_version', 'cpu_type', 'capacity']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'cache_mode' in local_var_params:
            query_params.append(('cache_mode', local_var_params['cache_mode']))
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'engine_version' in local_var_params:
            query_params.append(('engine_version', local_var_params['engine_version']))
        if 'cpu_type' in local_var_params:
            query_params.append(('cpu_type', local_var_params['cpu_type']))
        if 'capacity' in local_var_params:
            query_params.append(('capacity', local_var_params['capacity']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/flavors',
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


    def list_group_replication_info_async(self, request):
        """查询分片信息

        查询读写分离实例和集群实例的分片和副本信息，其中，读写分离实例仅Redis4.0和Redis5.0的主备实例支持。

        :param ListGroupReplicationInfoRequest request
        :return: ListGroupReplicationInfoResponse
        """
        return self.list_group_replication_info_with_http_info(request)

    def list_group_replication_info_with_http_info(self, request):
        """查询分片信息

        查询读写分离实例和集群实例的分片和副本信息，其中，读写分离实例仅Redis4.0和Redis5.0的主备实例支持。

        :param ListGroupReplicationInfoRequest request
        :return: ListGroupReplicationInfoResponse
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
            resource_path='/v2/{project_id}/instance/{instance_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGroupReplicationInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_hot_key_scan_tasks_async(self, request):
        """查询热key分析任务列表

        查询热key分析历史记录。

        :param ListHotKeyScanTasksRequest request
        :return: ListHotKeyScanTasksResponse
        """
        return self.list_hot_key_scan_tasks_with_http_info(request)

    def list_hot_key_scan_tasks_with_http_info(self, request):
        """查询热key分析任务列表

        查询热key分析历史记录。

        :param ListHotKeyScanTasksRequest request
        :return: ListHotKeyScanTasksResponse
        """

        all_params = ['instance_id', 'offset', 'limit', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHotKeyScanTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instances_async(self, request):
        """查询所有实例列表

        查询租户的缓存实例列表，支持按照条件查询。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        """查询所有实例列表

        查询租户的缓存实例列表，支持按照条件查询。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """

        all_params = ['id', 'include_failure', 'name', 'offset', 'limit', 'status', 'name_equal', 'tags', 'ip']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name_equal' in local_var_params:
            query_params.append(('name_equal', local_var_params['name_equal']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
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


    def list_maintenance_windows_async(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。

        :param ListMaintenanceWindowsRequest request
        :return: ListMaintenanceWindowsResponse
        """
        return self.list_maintenance_windows_with_http_info(request)

    def list_maintenance_windows_with_http_info(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。

        :param ListMaintenanceWindowsRequest request
        :return: ListMaintenanceWindowsResponse
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
            resource_path='/v2/instances/maintain-windows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMaintenanceWindowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_migration_task_async(self, request):
        """查询迁移任务列表

        查询迁移任务列表。

        :param ListMigrationTaskRequest request
        :return: ListMigrationTaskResponse
        """
        return self.list_migration_task_with_http_info(request)

    def list_migration_task_with_http_info(self, request):
        """查询迁移任务列表

        查询迁移任务列表。

        :param ListMigrationTaskRequest request
        :return: ListMigrationTaskResponse
        """

        all_params = ['offset', 'limit', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_monitored_objects_of_instance_async(self, request):
        """查询单个主维度下子维度监控对象列表

        查询主维度下子维度监控对象列表，当前支持子维度的主维度ID的有 dcs_instance_id > 该接口当前仅在中国华南区开放。 

        :param ListMonitoredObjectsOfInstanceRequest request
        :return: ListMonitoredObjectsOfInstanceResponse
        """
        return self.list_monitored_objects_of_instance_with_http_info(request)

    def list_monitored_objects_of_instance_with_http_info(self, request):
        """查询单个主维度下子维度监控对象列表

        查询主维度下子维度监控对象列表，当前支持子维度的主维度ID的有 dcs_instance_id > 该接口当前仅在中国华南区开放。 

        :param ListMonitoredObjectsOfInstanceRequest request
        :return: ListMonitoredObjectsOfInstanceResponse
        """

        all_params = ['instance_id', 'dim_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dim_name' in local_var_params:
            query_params.append(('dim_name', local_var_params['dim_name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/dims/monitored-objects/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMonitoredObjectsOfInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_number_of_instances_in_different_status_async(self, request):
        """查询实例状态

        查询该租户在当前区域下不同状态的实例数。

        :param ListNumberOfInstancesInDifferentStatusRequest request
        :return: ListNumberOfInstancesInDifferentStatusResponse
        """
        return self.list_number_of_instances_in_different_status_with_http_info(request)

    def list_number_of_instances_in_different_status_with_http_info(self, request):
        """查询实例状态

        查询该租户在当前区域下不同状态的实例数。

        :param ListNumberOfInstancesInDifferentStatusRequest request
        :return: ListNumberOfInstancesInDifferentStatusResponse
        """

        all_params = ['include_failure']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNumberOfInstancesInDifferentStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_restore_records_async(self, request):
        """查询实例恢复记录

        查询指定缓存实例的恢复记录列表。

        :param ListRestoreRecordsRequest request
        :return: ListRestoreRecordsResponse
        """
        return self.list_restore_records_with_http_info(request)

    def list_restore_records_with_http_info(self, request):
        """查询实例恢复记录

        查询指定缓存实例的恢复记录列表。

        :param ListRestoreRecordsRequest request
        :return: ListRestoreRecordsResponse
        """

        all_params = ['instance_id', 'begin_time', 'end_time', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/restores',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRestoreRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_slowlog_async(self, request):
        """查询慢日志

        查询慢日志。

        :param ListSlowlogRequest request
        :return: ListSlowlogResponse
        """
        return self.list_slowlog_with_http_info(request)

    def list_slowlog_with_http_info(self, request):
        """查询慢日志

        查询慢日志。

        :param ListSlowlogRequest request
        :return: ListSlowlogResponse
        """

        all_params = ['instance_id', 'start_time', 'end_time', 'offset', 'limit', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/slowlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSlowlogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_statistics_of_running_instances_async(self, request):
        """查询运行中实例的统计信息

        查询当前租户下处于“运行中”状态的缓存实例的统计信息。

        :param ListStatisticsOfRunningInstancesRequest request
        :return: ListStatisticsOfRunningInstancesResponse
        """
        return self.list_statistics_of_running_instances_with_http_info(request)

    def list_statistics_of_running_instances_with_http_info(self, request):
        """查询运行中实例的统计信息

        查询当前租户下处于“运行中”状态的缓存实例的统计信息。

        :param ListStatisticsOfRunningInstancesRequest request
        :return: ListStatisticsOfRunningInstancesResponse
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
            resource_path='/v2/{project_id}/instances/statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStatisticsOfRunningInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tags_of_tenant_async(self, request):
        """查询租户所有标签

        查询租户在指定Project中实例类型的所有资源标签集合。

        :param ListTagsOfTenantRequest request
        :return: ListTagsOfTenantResponse
        """
        return self.list_tags_of_tenant_with_http_info(request)

    def list_tags_of_tenant_with_http_info(self, request):
        """查询租户所有标签

        查询租户在指定Project中实例类型的所有资源标签集合。

        :param ListTagsOfTenantRequest request
        :return: ListTagsOfTenantResponse
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
            resource_path='/v2/{project_id}/dcs/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagsOfTenantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restart_or_flush_instances_async(self, request):
        """重启实例或清空数据

        重启运行中的DCS缓存实例。  清空Redis4.0/Redis5.0的实例数据，数据清空后，无法撤销，且无法恢复，请谨慎操作。 

        :param RestartOrFlushInstancesRequest request
        :return: RestartOrFlushInstancesResponse
        """
        return self.restart_or_flush_instances_with_http_info(request)

    def restart_or_flush_instances_with_http_info(self, request):
        """重启实例或清空数据

        重启运行中的DCS缓存实例。  清空Redis4.0/Redis5.0的实例数据，数据清空后，无法撤销，且无法恢复，请谨慎操作。 

        :param RestartOrFlushInstancesRequest request
        :return: RestartOrFlushInstancesResponse
        """

        all_params = ['restart_or_flush_instances_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestartOrFlushInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def restore_instance_async(self, request):
        """恢复指定实例

        恢复指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param RestoreInstanceRequest request
        :return: RestoreInstanceResponse
        """
        return self.restore_instance_with_http_info(request)

    def restore_instance_with_http_info(self, request):
        """恢复指定实例

        恢复指定的缓存实例。 > 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。 

        :param RestoreInstanceRequest request
        :return: RestoreInstanceResponse
        """

        all_params = ['instance_id', 'restore_instance_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/restores',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RestoreInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_bigkey_autoscan_config_async(self, request):
        """查询大key自动分析配置

        查询大key自动分析配置。

        :param ShowBigkeyAutoscanConfigRequest request
        :return: ShowBigkeyAutoscanConfigResponse
        """
        return self.show_bigkey_autoscan_config_with_http_info(request)

    def show_bigkey_autoscan_config_with_http_info(self, request):
        """查询大key自动分析配置

        查询大key自动分析配置。

        :param ShowBigkeyAutoscanConfigRequest request
        :return: ShowBigkeyAutoscanConfigResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey/autoscan',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBigkeyAutoscanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_bigkey_scan_task_details_async(self, request):
        """查询大key分析详情

        查询大key分析详情。

        :param ShowBigkeyScanTaskDetailsRequest request
        :return: ShowBigkeyScanTaskDetailsResponse
        """
        return self.show_bigkey_scan_task_details_with_http_info(request)

    def show_bigkey_scan_task_details_with_http_info(self, request):
        """查询大key分析详情

        查询大key分析详情。

        :param ShowBigkeyScanTaskDetailsRequest request
        :return: ShowBigkeyScanTaskDetailsResponse
        """

        all_params = ['instance_id', 'bigkey_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'bigkey_id' in local_var_params:
            path_params['bigkey_id'] = local_var_params['bigkey_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-task/{bigkey_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBigkeyScanTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_hotkey_autoscan_config_async(self, request):
        """查询热key自动分析配置

        查询热key自动分析配置。

        :param ShowHotkeyAutoscanConfigRequest request
        :return: ShowHotkeyAutoscanConfigResponse
        """
        return self.show_hotkey_autoscan_config_with_http_info(request)

    def show_hotkey_autoscan_config_with_http_info(self, request):
        """查询热key自动分析配置

        查询热key自动分析配置。

        :param ShowHotkeyAutoscanConfigRequest request
        :return: ShowHotkeyAutoscanConfigResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey/autoscan',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHotkeyAutoscanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_hotkey_task_details_async(self, request):
        """查询热key分析详情

        查询热key分析详情。

        :param ShowHotkeyTaskDetailsRequest request
        :return: ShowHotkeyTaskDetailsResponse
        """
        return self.show_hotkey_task_details_with_http_info(request)

    def show_hotkey_task_details_with_http_info(self, request):
        """查询热key分析详情

        查询热key分析详情。

        :param ShowHotkeyTaskDetailsRequest request
        :return: ShowHotkeyTaskDetailsResponse
        """

        all_params = ['instance_id', 'hotkey_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'hotkey_id' in local_var_params:
            path_params['hotkey_id'] = local_var_params['hotkey_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-task/{hotkey_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowHotkeyTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_async(self, request):
        """查询指定实例

        通过实例ID查询实例的详细信息。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        """查询指定实例

        通过实例ID查询实例的详细信息。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_migration_task_async(self, request):
        """查询迁移任务详情

        查询迁移任务详情。

        :param ShowMigrationTaskRequest request
        :return: ShowMigrationTaskResponse
        """
        return self.show_migration_task_with_http_info(request)

    def show_migration_task_with_http_info(self, request):
        """查询迁移任务详情

        查询迁移任务详情。

        :param ShowMigrationTaskRequest request
        :return: ShowMigrationTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_migration_task_stats_async(self, request):
        """查询在线迁移进度明细

        查询在线迁移进度明细。

        :param ShowMigrationTaskStatsRequest request
        :return: ShowMigrationTaskStatsResponse
        """
        return self.show_migration_task_stats_with_http_info(request)

    def show_migration_task_stats_with_http_info(self, request):
        """查询在线迁移进度明细

        查询在线迁移进度明细。

        :param ShowMigrationTaskStatsRequest request
        :return: ShowMigrationTaskStatsResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}/stats',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMigrationTaskStatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quota_of_tenant_async(self, request):
        """查询租户配额

        查询租户默认可以创建的实例数和总内存的配额限制，以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。

        :param ShowQuotaOfTenantRequest request
        :return: ShowQuotaOfTenantResponse
        """
        return self.show_quota_of_tenant_with_http_info(request)

    def show_quota_of_tenant_with_http_info(self, request):
        """查询租户配额

        查询租户默认可以创建的实例数和总内存的配额限制，以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。

        :param ShowQuotaOfTenantRequest request
        :return: ShowQuotaOfTenantResponse
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
            resource_path='/v2/{project_id}/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowQuotaOfTenantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_tags_async(self, request):
        """查询单个实例标签

        通过实例ID查询标签。

        :param ShowTagsRequest request
        :return: ShowTagsResponse
        """
        return self.show_tags_with_http_info(request)

    def show_tags_with_http_info(self, request):
        """查询单个实例标签

        通过实例ID查询标签。

        :param ShowTagsRequest request
        :return: ShowTagsResponse
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
            resource_path='/v2/{project_id}/instances/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_migration_task_async(self, request):
        """停止数据迁移任务

        停止数据迁移任务。

        :param StopMigrationTaskRequest request
        :return: StopMigrationTaskResponse
        """
        return self.stop_migration_task_with_http_info(request)

    def stop_migration_task_with_http_info(self, request):
        """停止数据迁移任务

        停止数据迁移任务。

        :param StopMigrationTaskRequest request
        :return: StopMigrationTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_bigkey_autoscan_config_async(self, request):
        """设置大key自动分析配置

        设置大key自动分析配置。

        :param UpdateBigkeyAutoscanConfigRequest request
        :return: UpdateBigkeyAutoscanConfigResponse
        """
        return self.update_bigkey_autoscan_config_with_http_info(request)

    def update_bigkey_autoscan_config_with_http_info(self, request):
        """设置大key自动分析配置

        设置大key自动分析配置。

        :param UpdateBigkeyAutoscanConfigRequest request
        :return: UpdateBigkeyAutoscanConfigResponse
        """

        all_params = ['instance_id', 'update_bigkey_autoscan_config_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey/autoscan',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBigkeyAutoscanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_configurations_async(self, request):
        """修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。

        :param UpdateConfigurationsRequest request
        :return: UpdateConfigurationsResponse
        """
        return self.update_configurations_with_http_info(request)

    def update_configurations_with_http_info(self, request):
        """修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。

        :param UpdateConfigurationsRequest request
        :return: UpdateConfigurationsResponse
        """

        all_params = ['instance_id', 'update_configurations_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/configs',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_hotkey_auto_scan_config_async(self, request):
        """设置热key自动分析配置

        设置热key自动分析配置。

        :param UpdateHotkeyAutoScanConfigRequest request
        :return: UpdateHotkeyAutoScanConfigResponse
        """
        return self.update_hotkey_auto_scan_config_with_http_info(request)

    def update_hotkey_auto_scan_config_with_http_info(self, request):
        """设置热key自动分析配置

        设置热key自动分析配置。

        :param UpdateHotkeyAutoScanConfigRequest request
        :return: UpdateHotkeyAutoScanConfigResponse
        """

        all_params = ['instance_id', 'update_hotkey_autoscan_config_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey/autoscan',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateHotkeyAutoScanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_async(self, request):
        """修改实例信息

        修改缓存实例的信息，可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """
        return self.update_instance_with_http_info(request)

    def update_instance_with_http_info(self, request):
        """修改实例信息

        修改缓存实例的信息，可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """

        all_params = ['instance_id', 'update_instance_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_password_async(self, request):
        """修改密码

        修改缓存实例的密码。

        :param UpdatePasswordRequest request
        :return: UpdatePasswordResponse
        """
        return self.update_password_with_http_info(request)

    def update_password_with_http_info(self, request):
        """修改密码

        修改缓存实例的密码。

        :param UpdatePasswordRequest request
        :return: UpdatePasswordResponse
        """

        all_params = ['instance_id', 'update_password_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_slave_priority_async(self, request):
        """设置备节点优先级

        设置副本优先级，主节点故障时，权重越小的备节点切换为主节点的优先级越高。

        :param UpdateSlavePriorityRequest request
        :return: UpdateSlavePriorityResponse
        """
        return self.update_slave_priority_with_http_info(request)

    def update_slave_priority_with_http_info(self, request):
        """设置备节点优先级

        设置副本优先级，主节点故障时，权重越小的备节点切换为主节点的优先级越高。

        :param UpdateSlavePriorityRequest request
        :return: UpdateSlavePriorityResponse
        """

        all_params = ['instance_id', 'group_id', 'node_id', 'update_slave_priority_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/slave-priority',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSlavePriorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_ip_whitelist_async(self, request):
        """查询指定实例的IP白名单

        查询指定实例的IP白名单。

        :param ShowIpWhitelistRequest request
        :return: ShowIpWhitelistResponse
        """
        return self.show_ip_whitelist_with_http_info(request)

    def show_ip_whitelist_with_http_info(self, request):
        """查询指定实例的IP白名单

        查询指定实例的IP白名单。

        :param ShowIpWhitelistRequest request
        :return: ShowIpWhitelistResponse
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
            resource_path='/v2/{project_id}/instance/{instance_id}/whitelist',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowIpWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_ip_whitelist_async(self, request):
        """设置IP白名单分组

        为指定实例设置IP白名单分组，包含创建、停用、编辑、删除白名单四个功能

        :param UpdateIpWhitelistRequest request
        :return: UpdateIpWhitelistResponse
        """
        return self.update_ip_whitelist_with_http_info(request)

    def update_ip_whitelist_with_http_info(self, request):
        """设置IP白名单分组

        为指定实例设置IP白名单分组，包含创建、停用、编辑、删除白名单四个功能

        :param UpdateIpWhitelistRequest request
        :return: UpdateIpWhitelistResponse
        """

        all_params = ['instance_id', 'update_ip_whitelist_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instance/{instance_id}/whitelist',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateIpWhitelistResponse',
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

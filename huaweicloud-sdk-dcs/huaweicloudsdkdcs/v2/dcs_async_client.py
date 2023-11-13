# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DcsAsyncClient(Client):
    def __init__(self):
        super(DcsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdcs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DcsAsyncClient":
                raise TypeError("client type error, support client type is DcsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_tags_async(self, request):
        """批量添加或删除标签

        为指定实例批量添加标签，或批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteTags
        :type request: :class:`huaweicloudsdkdcs.v2.BatchCreateOrDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchCreateOrDeleteTagsResponse`
        """
        return self._batch_create_or_delete_tags_with_http_info(request)

    def _batch_create_or_delete_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='BatchCreateOrDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_instances_async(self, request):
        """批量删除实例

        批量删除多个缓存实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteInstances
        :type request: :class:`huaweicloudsdkdcs.v2.BatchDeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchDeleteInstancesResponse`
        """
        return self._batch_delete_instances_with_http_info(request)

    def _batch_delete_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='BatchDeleteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_nodes_information_async(self, request):
        """批量查询实例节点信息

        批量查询指定项目所有实例的节点信息、有效实例个数及节点个数。
        创建中实例不返回节点信息。
        仅支持Redis4.0和Redis5.0实例查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchShowNodesInformation
        :type request: :class:`huaweicloudsdkdcs.v2.BatchShowNodesInformationRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchShowNodesInformationResponse`
        """
        return self._batch_show_nodes_information_with_http_info(request)

    def _batch_show_nodes_information_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances-logical-nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowNodesInformationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_stop_migration_tasks_async(self, request):
        """批量停止数据迁移任务

        批量停止数据迁移任务，接口响应成功，仅表示下发任务成功。查询到迁移任务状态为TERMINATED时，即停止成功。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopMigrationTasks
        :type request: :class:`huaweicloudsdkdcs.v2.BatchStopMigrationTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchStopMigrationTasksResponse`
        """
        return self._batch_stop_migration_tasks_with_http_info(request)

    def _batch_stop_migration_tasks_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/batch-stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStopMigrationTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_master_standby_async(self, request):
        """主备切换

        切换实例主备节点，只有主备实例支持该操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeMasterStandby
        :type request: :class:`huaweicloudsdkdcs.v2.ChangeMasterStandbyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ChangeMasterStandbyResponse`
        """
        return self._change_master_standby_with_http_info(request)

    def _change_master_standby_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/swap',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeMasterStandbyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_instance_async(self, request):
        """备份指定实例

        备份指定的缓存实例。
        &gt; 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyInstance
        :type request: :class:`huaweicloudsdkdcs.v2.CopyInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CopyInstanceResponse`
        """
        return self._copy_instance_with_http_info(request)

    def _copy_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='CopyInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_acl_account_async(self, request):
        """创建ACL账号

        \&quot;为redis4.0/5.0实例（Cluster集群实例除外）创建权限访问账号，包含读写和只读权限。
        如果实例默认账号已开启免密访问，您创建的普通账号不能使用，如需使用普通账号请先关闭默认账号的免密访问。
        单机、主备实例默认账号的密码不能带有冒号(:)，否则无法创建普通账号。\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAclAccount
        :type request: :class:`huaweicloudsdkdcs.v2.CreateAclAccountRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateAclAccountResponse`
        """
        return self._create_acl_account_with_http_info(request)

    def _create_acl_account_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAclAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_auto_expire_scan_task_async(self, request):
        """创建过期key扫描任务

        创建过期key扫描任务（Redis 3.0 不支持过期key扫描）。
        过期key扫描会对键空间进行Redis的scan扫描，释放内存中已过期但是由于惰性删除机制而没有释放的内存空间。
        过期key扫描在主节点上执行，会对实例性能有一定的影响，建议不要在业务高峰期进行。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAutoExpireScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateAutoExpireScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateAutoExpireScanTaskResponse`
        """
        return self._create_auto_expire_scan_task_with_http_info(request)

    def _create_auto_expire_scan_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/scan-expire-keys-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAutoExpireScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_bigkey_scan_task_async(self, request):
        """创建大key分析任务

        为Redis实例创建大key分析任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBigkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateBigkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateBigkeyScanTaskResponse`
        """
        return self._create_bigkey_scan_task_with_http_info(request)

    def _create_bigkey_scan_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBigkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_custom_template_async(self, request):
        """创建自定义模板

        创建自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCustomTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.CreateCustomTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateCustomTemplateResponse`
        """
        return self._create_custom_template_with_http_info(request)

    def _create_custom_template_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/config-templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCustomTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_diagnosis_task_async(self, request):
        """创建实例诊断任务

        诊断指定的缓存实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDiagnosisTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateDiagnosisTaskResponse`
        """
        return self._create_diagnosis_task_with_http_info(request)

    def _create_diagnosis_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/diagnosis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDiagnosisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_hotkey_scan_task_async(self, request):
        """创建热key分析任务

        创建热key分析任务，Redis 3.0 不支持热key分析。
        
        热key分析需要将缓存实例配置参数maxmemory-policy设置为allkeys-lfu或volatile-lfu。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateHotkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateHotkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateHotkeyScanTaskResponse`
        """
        return self._create_hotkey_scan_task_with_http_info(request)

    def _create_hotkey_scan_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHotkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_async(self, request):
        """创建缓存实例

        创建缓存实例，该接口创建的缓存实例支持按需计费和包周期两种方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkdcs.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateInstanceResponse`
        """
        return self._create_instance_with_http_info(request)

    def _create_instance_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_migration_task_async(self, request):
        """创建数据迁移任务

        创建数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateMigrationTaskResponse`
        """
        return self._create_migration_task_with_http_info(request)

    def _create_migration_task_with_http_info(self, request):
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
            cname=cname,
            response_type='CreateMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_online_migration_task_async(self, request):
        """创建在线数据迁移任务

        创建在线数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOnlineMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateOnlineMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateOnlineMigrationTaskResponse`
        """
        return self._create_online_migration_task_with_http_info(request)

    def _create_online_migration_task_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration/instance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOnlineMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_redislog_async(self, request):
        """采集Redis运行日志

        采集Redis运行日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRedislog
        :type request: :class:`huaweicloudsdkdcs.v2.CreateRedislogRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateRedislogResponse`
        """
        return self._create_redislog_with_http_info(request)

    def _create_redislog_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'query_time' in local_var_params:
            query_params.append(('query_time', local_var_params['query_time']))
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))
        if 'replication_id' in local_var_params:
            query_params.append(('replication_id', local_var_params['replication_id']))

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
            resource_path='/v2/{project_id}/instances/{instance_id}/redislog',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRedislogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_redislog_download_link_async(self, request):
        """获取日志下载链接

        获取日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRedislogDownloadLink
        :type request: :class:`huaweicloudsdkdcs.v2.CreateRedislogDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateRedislogDownloadLinkResponse`
        """
        return self._create_redislog_download_link_with_http_info(request)

    def _create_redislog_download_link_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/redislog/{id}/links',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateRedislogDownloadLinkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resize_order_async(self, request):
        """包周期实例变更规格

        包周期实例变更规格
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResizeOrder
        :type request: :class:`huaweicloudsdkdcs.v2.CreateResizeOrderRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateResizeOrderResponse`
        """
        return self._create_resize_order_with_http_info(request)

    def _create_resize_order_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/orders/instances/{instance_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResizeOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_acl_account_async(self, request):
        """删除ACL账号

        删除所创建的ACL普通账号
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAclAccount
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteAclAccountRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteAclAccountResponse`
        """
        return self._delete_acl_account_with_http_info(request)

    def _delete_acl_account_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts/{account_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAclAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_background_task_async(self, request):
        """删除后台任务

        删除后台任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackgroundTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteBackgroundTaskResponse`
        """
        return self._delete_background_task_with_http_info(request)

    def _delete_background_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_backup_file_async(self, request):
        """删除备份文件

        删除缓存实例已备份的文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackupFile
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteBackupFileRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteBackupFileResponse`
        """
        return self._delete_backup_file_with_http_info(request)

    def _delete_backup_file_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBackupFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_bigkey_scan_task_async(self, request):
        """删除大key分析记录

        删除大key分析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBigkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteBigkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteBigkeyScanTaskResponse`
        """
        return self._delete_bigkey_scan_task_with_http_info(request)

    def _delete_bigkey_scan_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-task/{bigkey_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBigkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_center_task_async(self, request):
        """删除任务中心任务

        删除任务中心任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCenterTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteCenterTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteCenterTaskResponse`
        """
        return self._delete_center_task_with_http_info(request)

    def _delete_center_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v2/{project_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCenterTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_config_template_async(self, request):
        """删除自定义模板

        删除自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfigTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteConfigTemplateResponse`
        """
        return self._delete_config_template_with_http_info(request)

    def _delete_config_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v2/{project_id}/config-templates/{template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConfigTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_diagnosis_task_async(self, request):
        """删除诊断记录

        删除诊断记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDiagnosisTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteDiagnosisTaskResponse`
        """
        return self._delete_diagnosis_task_with_http_info(request)

    def _delete_diagnosis_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/diagnosis',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDiagnosisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_hotkey_scan_task_async(self, request):
        """删除热key分析任务

        删除热key分析任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteHotkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteHotkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteHotkeyScanTaskResponse`
        """
        return self._delete_hotkey_scan_task_with_http_info(request)

    def _delete_hotkey_scan_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-task/{hotkey_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHotkeyScanTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_ip_from_domain_name_async(self, request):
        """域名摘除IP

        将只读副本的IP从域名中摘除，摘除成功后，只读域名不会再解析到该副本IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteIpFromDomainName
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteIpFromDomainNameRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteIpFromDomainNameResponse`
        """
        return self._delete_ip_from_domain_name_with_http_info(request)

    def _delete_ip_from_domain_name_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/remove-ip',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteIpFromDomainNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_migration_task_async(self, request):
        """删除数据迁移任务

        删除数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteMigrationTaskResponse`
        """
        return self._delete_migration_task_with_http_info(request)

    def _delete_migration_task_with_http_info(self, request):
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
            cname=cname,
            response_type='DeleteMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_single_instance_async(self, request):
        """删除实例

        删除指定的缓存实例，释放该实例的所有资源。
        
        &gt; 如果是删除按需资源，请按照本章节执行；如果是删除包周期资源，即退订，请参考[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html#section2)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSingleInstance
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteSingleInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteSingleInstanceResponse`
        """
        return self._delete_single_instance_with_http_info(request)

    def _delete_single_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSingleInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def exchange_instance_ip_async(self, request):
        """进行IP交换

        进行IP交换
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExchangeInstanceIp
        :type request: :class:`huaweicloudsdkdcs.v2.ExchangeInstanceIpRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExchangeInstanceIpResponse`
        """
        return self._exchange_instance_ip_with_http_info(request)

    def _exchange_instance_ip_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v2/{project_id}/migration-task/{task_id}/exchange-ip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExchangeInstanceIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_cluster_switchover_async(self, request):
        """集群分片倒换

        集群分片倒换，适用于proxy和cluster实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteClusterSwitchover
        :type request: :class:`huaweicloudsdkdcs.v2.ExecuteClusterSwitchoverRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExecuteClusterSwitchoverResponse`
        """
        return self._execute_cluster_switchover_with_http_info(request)

    def _execute_cluster_switchover_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instance/{instance_id}/groups/{group_id}/replications/{node_id}/async-switchover',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteClusterSwitchoverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_command_mobilization_async(self, request):
        """执行web-cli命令V2接口

        登入web-cli，执行redis命令
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteCommandMobilization
        :type request: :class:`huaweicloudsdkdcs.v2.ExecuteCommandMobilizationRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExecuteCommandMobilizationResponse`
        """
        return self._execute_command_mobilization_with_http_info(request)

    def _execute_command_mobilization_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/webcli/command',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteCommandMobilizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_excel_job_async(self, request):
        """查询实例列表导出任务详情

        查询实例列表导出任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportExcelJob
        :type request: :class:`huaweicloudsdkdcs.v2.ExportExcelJobRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExportExcelJobResponse`
        """
        return self._export_excel_job_with_http_info(request)

    def _export_excel_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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
            resource_path='/v2/{project_id}/instances/export-job',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportExcelJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_instances_task_async(self, request):
        """异步导出实例资源

        异步导出实例资源
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportInstancesTask
        :type request: :class:`huaweicloudsdkdcs.v2.ExportInstancesTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExportInstancesTaskResponse`
        """
        return self._export_instances_task_with_http_info(request)

    def _export_instances_task_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportInstancesTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_acl_accounts_async(self, request):
        """查询ACL账户列表

        查询ACL账户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAclAccounts
        :type request: :class:`huaweicloudsdkdcs.v2.ListAclAccountsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListAclAccountsResponse`
        """
        return self._list_acl_accounts_with_http_info(request)

    def _list_acl_accounts_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAclAccountsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_zones_async(self, request):
        """查询可用区信息

        查询所在局点的可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkdcs.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListAvailableZonesResponse`
        """
        return self._list_available_zones_with_http_info(request)

    def _list_available_zones_with_http_info(self, request):
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
            resource_path='/v2/available-zones',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailableZonesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_background_task_async(self, request):
        """查询后台任务列表

        查询后台任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackgroundTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBackgroundTaskResponse`
        """
        return self._list_background_task_with_http_info(request)

    def _list_background_task_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackgroundTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backup_file_links_async(self, request):
        """获取备份文件下载链接

        获取指定实例的备份文件下载链接，下载备份文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackupFileLinks
        :type request: :class:`huaweicloudsdkdcs.v2.ListBackupFileLinksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBackupFileLinksResponse`
        """
        return self._list_backup_file_links_with_http_info(request)

    def _list_backup_file_links_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='ListBackupFileLinksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backup_records_async(self, request):
        """查询实例备份信息

        查询指定缓存实例的备份信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackupRecords
        :type request: :class:`huaweicloudsdkdcs.v2.ListBackupRecordsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBackupRecordsResponse`
        """
        return self._list_backup_records_with_http_info(request)

    def _list_backup_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackupRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bigkey_scan_tasks_async(self, request):
        """查询大key分析任务列表

        查询大key分析任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBigkeyScanTasks
        :type request: :class:`huaweicloudsdkdcs.v2.ListBigkeyScanTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBigkeyScanTasksResponse`
        """
        return self._list_bigkey_scan_tasks_with_http_info(request)

    def _list_bigkey_scan_tasks_with_http_info(self, request):
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBigkeyScanTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_center_task_async(self, request):
        """查询任务中心任务列表

        查询任务中心任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCenterTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListCenterTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListCenterTaskResponse`
        """
        return self._list_center_task_with_http_info(request)

    def _list_center_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCenterTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_config_histories_async(self, request):
        """查询实例参数修改记录列表

        查询实例的参数修改记录列表，支持按照关键字查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigHistories
        :type request: :class:`huaweicloudsdkdcs.v2.ListConfigHistoriesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListConfigHistoriesResponse`
        """
        return self._list_config_histories_with_http_info(request)

    def _list_config_histories_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/config-histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_config_templates_async(self, request):
        """查询参数模板列表

        查询租户的参数模板列表，支持按照条件查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigTemplates
        :type request: :class:`huaweicloudsdkdcs.v2.ListConfigTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListConfigTemplatesResponse`
        """
        return self._list_config_templates_with_http_info(request)

    def _list_config_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'engine_version' in local_var_params:
            query_params.append(('engine_version', local_var_params['engine_version']))
        if 'cache_mode' in local_var_params:
            query_params.append(('cache_mode', local_var_params['cache_mode']))
        if 'description' in local_var_params:
            query_params.append(('description', local_var_params['description']))
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/config-templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configurations_async(self, request):
        """查询实例配置参数

        查询指定实例的配置参数信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkdcs.v2.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListConfigurationsResponse`
        """
        return self._list_configurations_with_http_info(request)

    def _list_configurations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_diagnosis_tasks_async(self, request):
        """查询实例诊断任务列表

        查询指定缓存实例诊断任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDiagnosisTasks
        :type request: :class:`huaweicloudsdkdcs.v2.ListDiagnosisTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListDiagnosisTasksResponse`
        """
        return self._list_diagnosis_tasks_with_http_info(request)

    def _list_diagnosis_tasks_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/diagnosis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDiagnosisTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询产品规格

        在创建缓存实例时，需要配置订购的产品规格编码（spec_code），可通过该接口查询产品规格，查询条件不选时默认查询全部。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkdcs.v2.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListFlavorsResponse`
        """
        return self._list_flavors_with_http_info(request)

    def _list_flavors_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_group_replication_info_async(self, request):
        """查询分片信息

        查询读写分离实例和集群实例的分片和副本信息，其中，读写分离实例仅Redis4.0和Redis5.0的主备实例支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGroupReplicationInfo
        :type request: :class:`huaweicloudsdkdcs.v2.ListGroupReplicationInfoRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListGroupReplicationInfoResponse`
        """
        return self._list_group_replication_info_with_http_info(request)

    def _list_group_replication_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instance/{instance_id}/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGroupReplicationInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_hot_key_scan_tasks_async(self, request):
        """查询热key分析任务列表

        查询热key分析历史记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHotKeyScanTasks
        :type request: :class:`huaweicloudsdkdcs.v2.ListHotKeyScanTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListHotKeyScanTasksResponse`
        """
        return self._list_hot_key_scan_tasks_with_http_info(request)

    def _list_hot_key_scan_tasks_with_http_info(self, request):
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHotKeyScanTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_operations_async(self, request):
        """查询实例是否可以扩容

        查询实例是否可以扩容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceOperations
        :type request: :class:`huaweicloudsdkdcs.v2.ListInstanceOperationsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListInstanceOperationsResponse`
        """
        return self._list_instance_operations_with_http_info(request)

    def _list_instance_operations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'operation' in local_var_params:
            query_params.append(('operation', local_var_params['operation']))

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
            resource_path='/v2/{project_id}/instances/{instance_id}/operations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceOperationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_async(self, request):
        """查询所有实例列表

        查询租户的缓存实例列表，支持按照条件查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkdcs.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListInstancesResponse`
        """
        return self._list_instances_with_http_info(request)

    def _list_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))
        if 'include_delete' in local_var_params:
            query_params.append(('include_delete', local_var_params['include_delete']))
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_maintenance_windows_async(self, request):
        """查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMaintenanceWindows
        :type request: :class:`huaweicloudsdkdcs.v2.ListMaintenanceWindowsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMaintenanceWindowsResponse`
        """
        return self._list_maintenance_windows_with_http_info(request)

    def _list_maintenance_windows_with_http_info(self, request):
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
            resource_path='/v2/instances/maintain-windows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMaintenanceWindowsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_migration_task_async(self, request):
        """查询迁移任务列表

        查询迁移任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskResponse`
        """
        return self._list_migration_task_with_http_info(request)

    def _list_migration_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_migration_task_logs_async(self, request):
        """查询迁移日志列表

        查询迁移日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMigrationTaskLogs
        :type request: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskLogsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskLogsResponse`
        """
        return self._list_migration_task_logs_with_http_info(request)

    def _list_migration_task_logs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'log_level' in local_var_params:
            query_params.append(('log_level', local_var_params['log_level']))

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
            resource_path='/v2/{project_id}/migration-task/{task_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMigrationTaskLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_monitored_objects_async(self, request):
        """查询主维度信息列表

        查询主维度对象列表，主维度ID当前支持dcs_instance_id，dcs_memcached_instance_id。
        &gt; 该接口当前仅在中国华南区开放。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMonitoredObjects
        :type request: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsResponse`
        """
        return self._list_monitored_objects_with_http_info(request)

    def _list_monitored_objects_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/dims/monitored-objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMonitoredObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_monitored_objects_of_instance_async(self, request):
        """查询单个主维度下子维度监控对象列表

        查询主维度下子维度监控对象列表，当前支持子维度的主维度ID的有 dcs_instance_id
        &gt; 该接口当前仅在中国华南区开放。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMonitoredObjectsOfInstance
        :type request: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsOfInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsOfInstanceResponse`
        """
        return self._list_monitored_objects_of_instance_with_http_info(request)

    def _list_monitored_objects_of_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/dims/monitored-objects/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMonitoredObjectsOfInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_number_of_instances_in_different_status_async(self, request):
        """查询实例状态

        查询该租户在当前区域下不同状态的实例数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNumberOfInstancesInDifferentStatus
        :type request: :class:`huaweicloudsdkdcs.v2.ListNumberOfInstancesInDifferentStatusRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListNumberOfInstancesInDifferentStatusResponse`
        """
        return self._list_number_of_instances_in_different_status_with_http_info(request)

    def _list_number_of_instances_in_different_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNumberOfInstancesInDifferentStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_redislog_async(self, request):
        """查询Redis运行日志列表

        查询Redis运行日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRedislog
        :type request: :class:`huaweicloudsdkdcs.v2.ListRedislogRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListRedislogResponse`
        """
        return self._list_redislog_with_http_info(request)

    def _list_redislog_with_http_info(self, request):
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
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))

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
            resource_path='/v2/{project_id}/instances/{instance_id}/redislog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRedislogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_restore_records_async(self, request):
        """查询实例恢复记录

        查询指定缓存实例的恢复记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRestoreRecords
        :type request: :class:`huaweicloudsdkdcs.v2.ListRestoreRecordsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListRestoreRecordsResponse`
        """
        return self._list_restore_records_with_http_info(request)

    def _list_restore_records_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/restores',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRestoreRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slowlog_async(self, request):
        """查询慢日志

        查询慢日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowlog
        :type request: :class:`huaweicloudsdkdcs.v2.ListSlowlogRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListSlowlogResponse`
        """
        return self._list_slowlog_with_http_info(request)

    def _list_slowlog_with_http_info(self, request):
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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/slowlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSlowlogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_statistics_of_running_instances_async(self, request):
        """查询运行中实例的统计信息

        查询当前租户下处于“运行中”状态的缓存实例的统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStatisticsOfRunningInstances
        :type request: :class:`huaweicloudsdkdcs.v2.ListStatisticsOfRunningInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListStatisticsOfRunningInstancesResponse`
        """
        return self._list_statistics_of_running_instances_with_http_info(request)

    def _list_statistics_of_running_instances_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/instances/statistic',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStatisticsOfRunningInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_tags_of_tenant_async(self, request):
        """查询租户所有标签

        查询租户在指定Project中实例类型的所有资源标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTagsOfTenant
        :type request: :class:`huaweicloudsdkdcs.v2.ListTagsOfTenantRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListTagsOfTenantResponse`
        """
        return self._list_tags_of_tenant_with_http_info(request)

    def _list_tags_of_tenant_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/dcs/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTagsOfTenantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def login_web_cli_async(self, request):
        """登录webCli

        登录webCli
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LoginWebCli
        :type request: :class:`huaweicloudsdkdcs.v2.LoginWebCliRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.LoginWebCliResponse`
        """
        return self._login_web_cli_with_http_info(request)

    def _login_web_cli_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/webcli/auth',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='LoginWebCliResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_acl_account_pass_word_async(self, request):
        """重置ACL账号密码

        重置ACL账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetAclAccountPassWord
        :type request: :class:`huaweicloudsdkdcs.v2.ResetAclAccountPassWordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ResetAclAccountPassWordResponse`
        """
        return self._reset_acl_account_pass_word_with_http_info(request)

    def _reset_acl_account_pass_word_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts/{account_id}/password/reset',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetAclAccountPassWordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_password_async(self, request):
        """重置密码

        重置缓存实例的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkdcs.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ResetPasswordResponse`
        """
        return self._reset_password_with_http_info(request)

    def _reset_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/password/reset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_instance_async(self, request):
        """变更实例规格

        用户可以为状态为“运行中”的DCS缓存实例进行规格变更，当前仅能支持按需实例的同副本或分片数量的实例规格变更。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkdcs.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ResizeInstanceResponse`
        """
        return self._resize_instance_with_http_info(request)

    def _resize_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_or_flush_instances_async(self, request):
        """重启实例或清空数据

        重启运行中的DCS缓存实例。
        
        清空Redis4.0/Redis5.0的实例数据，数据清空后，无法撤销，且无法恢复，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartOrFlushInstances
        :type request: :class:`huaweicloudsdkdcs.v2.RestartOrFlushInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.RestartOrFlushInstancesResponse`
        """
        return self._restart_or_flush_instances_with_http_info(request)

    def _restart_or_flush_instances_with_http_info(self, request):
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
            cname=cname,
            response_type='RestartOrFlushInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_instance_async(self, request):
        """恢复指定实例

        恢复指定的缓存实例。
        &gt; 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreInstance
        :type request: :class:`huaweicloudsdkdcs.v2.RestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.RestoreInstanceResponse`
        """
        return self._restore_instance_with_http_info(request)

    def _restore_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='RestoreInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def scan_expire_key_async(self, request):
        """立刻扫描过期Key

        立刻扫描过期Key
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ScanExpireKey
        :type request: :class:`huaweicloudsdkdcs.v2.ScanExpireKeyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ScanExpireKeyResponse`
        """
        return self._scan_expire_key_with_http_info(request)

    def _scan_expire_key_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/auto-expire/scan',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ScanExpireKeyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_online_migration_task_async(self, request):
        """配置在线数据迁移任务

        配置在线数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetOnlineMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.SetOnlineMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.SetOnlineMigrationTaskResponse`
        """
        return self._set_online_migration_task_with_http_info(request)

    def _set_online_migration_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v2/{project_id}/migration/{task_id}/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetOnlineMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_background_task_progress_async(self, request):
        """查询后台任务详细信息

        查询后台任务详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackgroundTaskProgress
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBackgroundTaskProgressRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBackgroundTaskProgressResponse`
        """
        return self._show_background_task_progress_with_http_info(request)

    def _show_background_task_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tasks/{task_id}/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBackgroundTaskProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bigkey_autoscan_config_async(self, request):
        """查询大key自动分析配置

        查询大key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBigkeyAutoscanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBigkeyAutoscanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBigkeyAutoscanConfigResponse`
        """
        return self._show_bigkey_autoscan_config_with_http_info(request)

    def _show_bigkey_autoscan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey/autoscan',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBigkeyAutoscanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bigkey_scan_task_details_async(self, request):
        """查询大key分析详情

        查询大key分析详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBigkeyScanTaskDetails
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBigkeyScanTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBigkeyScanTaskDetailsResponse`
        """
        return self._show_bigkey_scan_task_details_with_http_info(request)

    def _show_bigkey_scan_task_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bigkey-task/{bigkey_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBigkeyScanTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_config_history_detail_async(self, request):
        """查询实例参数修改记录详情

        查询实例参数修改记录详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigHistoryDetail
        :type request: :class:`huaweicloudsdkdcs.v2.ShowConfigHistoryDetailRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowConfigHistoryDetailResponse`
        """
        return self._show_config_history_detail_with_http_info(request)

    def _show_config_history_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'history_id' in local_var_params:
            path_params['history_id'] = local_var_params['history_id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/config-histories/{history_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConfigHistoryDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_config_template_async(self, request):
        """查询参数模板详情

        查询参数模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.ShowConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowConfigTemplateResponse`
        """
        return self._show_config_template_with_http_info(request)

    def _show_config_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v2/{project_id}/config-templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConfigTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_diagnosis_task_details_async(self, request):
        """查询指定诊断报告

        通过报告ID查询诊断报告的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDiagnosisTaskDetails
        :type request: :class:`huaweicloudsdkdcs.v2.ShowDiagnosisTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowDiagnosisTaskDetailsResponse`
        """
        return self._show_diagnosis_task_details_with_http_info(request)

    def _show_diagnosis_task_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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
            resource_path='/v2/{project_id}/diagnosis/{report_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDiagnosisTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_expire_auto_scan_config_async(self, request):
        """查询自动扫描配置

        查询自动扫描配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExpireAutoScanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.ShowExpireAutoScanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowExpireAutoScanConfigResponse`
        """
        return self._show_expire_auto_scan_config_with_http_info(request)

    def _show_expire_auto_scan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/scan-expire-keys/autoscan-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowExpireAutoScanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_expire_key_scan_info_async(self, request):
        """查询过期Key扫描记录

        查询过期Key扫描记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowExpireKeyScanInfo
        :type request: :class:`huaweicloudsdkdcs.v2.ShowExpireKeyScanInfoRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowExpireKeyScanInfoResponse`
        """
        return self._show_expire_key_scan_info_with_http_info(request)

    def _show_expire_key_scan_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/auto-expire/histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowExpireKeyScanInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_hotkey_autoscan_config_async(self, request):
        """查询热key自动分析配置

        查询热key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHotkeyAutoscanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.ShowHotkeyAutoscanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowHotkeyAutoscanConfigResponse`
        """
        return self._show_hotkey_autoscan_config_with_http_info(request)

    def _show_hotkey_autoscan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey/autoscan',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHotkeyAutoscanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_hotkey_task_details_async(self, request):
        """查询热key分析详情

        查询热key分析详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHotkeyTaskDetails
        :type request: :class:`huaweicloudsdkdcs.v2.ShowHotkeyTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowHotkeyTaskDetailsResponse`
        """
        return self._show_hotkey_task_details_with_http_info(request)

    def _show_hotkey_task_details_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/hotkey-task/{hotkey_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHotkeyTaskDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_async(self, request):
        """查询指定实例

        通过实例ID查询实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkdcs.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowInstanceResponse`
        """
        return self._show_instance_with_http_info(request)

    def _show_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_info_async(self, request):
        """查询租户Job执行结果

        查询租户Job执行结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobInfo
        :type request: :class:`huaweicloudsdkdcs.v2.ShowJobInfoRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowJobInfoResponse`
        """
        return self._show_job_info_with_http_info(request)

    def _show_job_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v2/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_migration_task_async(self, request):
        """查询迁移任务详情

        查询迁移任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskResponse`
        """
        return self._show_migration_task_with_http_info(request)

    def _show_migration_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_migration_task_stats_async(self, request):
        """查询在线迁移进度明细

        查询在线迁移进度明细。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMigrationTaskStats
        :type request: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskStatsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskStatsResponse`
        """
        return self._show_migration_task_stats_with_http_info(request)

    def _show_migration_task_stats_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}/stats',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMigrationTaskStatsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nodes_information_async(self, request):
        """查询实例节点信息

        查询指定实例的节点信息。
        仅支持Redis4.0和Redis5.0实例查询。
        创建中实例不返回节点信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNodesInformation
        :type request: :class:`huaweicloudsdkdcs.v2.ShowNodesInformationRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowNodesInformationResponse`
        """
        return self._show_nodes_information_with_http_info(request)

    def _show_nodes_information_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/logical-nodes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNodesInformationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_of_tenant_async(self, request):
        """查询租户配额

        查询租户默认可以创建的实例数和总内存的配额限制，以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotaOfTenant
        :type request: :class:`huaweicloudsdkdcs.v2.ShowQuotaOfTenantRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowQuotaOfTenantResponse`
        """
        return self._show_quota_of_tenant_with_http_info(request)

    def _show_quota_of_tenant_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotaOfTenantResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_replication_states_async(self, request):
        """获取副本状态

        获取副本状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReplicationStates
        :type request: :class:`huaweicloudsdkdcs.v2.ShowReplicationStatesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowReplicationStatesResponse`
        """
        return self._show_replication_states_with_http_info(request)

    def _show_replication_states_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instance/{instance_id}/groups/{group_id}/group-nodes-state',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowReplicationStatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_tags_async(self, request):
        """查询单个实例标签

        通过实例ID查询标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTags
        :type request: :class:`huaweicloudsdkdcs.v2.ShowTagsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowTagsResponse`
        """
        return self._show_tags_with_http_info(request)

    def _show_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_instance_resize_check_job_async(self, request):
        """提交前置检查任务

        提交前置检查任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInstanceResizeCheckJob
        :type request: :class:`huaweicloudsdkdcs.v2.StartInstanceResizeCheckJobRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.StartInstanceResizeCheckJobResponse`
        """
        return self._start_instance_resize_check_job_with_http_info(request)

    def _start_instance_resize_check_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/resize/check-job',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartInstanceResizeCheckJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_migration_task_async(self, request):
        """停止数据迁移任务

        停止数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskResponse`
        """
        return self._stop_migration_task_with_http_info(request)

    def _stop_migration_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_migration_task_sync_async(self, request):
        """同步停止数据迁移任务

        同步停止数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopMigrationTaskSync
        :type request: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskSyncRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskSyncResponse`
        """
        return self._stop_migration_task_sync_with_http_info(request)

    def _stop_migration_task_sync_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/migration-task/{task_id}/sync-stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopMigrationTaskSyncResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_account_async(self, request):
        """修改ACL角色

        修改用户的类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAclAccount
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountResponse`
        """
        return self._update_acl_account_with_http_info(request)

    def _update_acl_account_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts/{account_id}/role',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAclAccountResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_account_pass_word_async(self, request):
        """修改ACL账号密码

        修改ACL账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAclAccountPassWord
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountPassWordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountPassWordResponse`
        """
        return self._update_acl_account_pass_word_with_http_info(request)

    def _update_acl_account_pass_word_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts/{account_id}/password/modify',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAclAccountPassWordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_acl_account_remark_async(self, request):
        """ACL账号修改备注

        ACL账号修改备注
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAclAccountRemark
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountRemarkRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountRemarkResponse`
        """
        return self._update_acl_account_remark_with_http_info(request)

    def _update_acl_account_remark_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'account_id' in local_var_params:
            path_params['account_id'] = local_var_params['account_id']

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
            resource_path='/v2/{project_id}/instances/{instance_id}/accounts/{account_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAclAccountRemarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_bigkey_autoscan_config_async(self, request):
        """设置大key自动分析配置

        设置大key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBigkeyAutoscanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateBigkeyAutoscanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateBigkeyAutoscanConfigResponse`
        """
        return self._update_bigkey_autoscan_config_with_http_info(request)

    def _update_bigkey_autoscan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateBigkeyAutoscanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_client_ip_transparent_transmission_async(self, request):
        """开启或关闭客户端ip透传

        开启或关闭客户端ip透传
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClientIpTransparentTransmission
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateClientIpTransparentTransmissionRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateClientIpTransparentTransmissionResponse`
        """
        return self._update_client_ip_transparent_transmission_with_http_info(request)

    def _update_client_ip_transparent_transmission_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/{instance_id}/client-ip-transparent-transmission',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateClientIpTransparentTransmissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_config_template_async(self, request):
        """修改自定义模板

        修改自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfigTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateConfigTemplateResponse`
        """
        return self._update_config_template_with_http_info(request)

    def _update_config_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v2/{project_id}/config-templates/{template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateConfigTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_configurations_async(self, request):
        """修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfigurations
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateConfigurationsResponse`
        """
        return self._update_configurations_with_http_info(request)

    def _update_configurations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_expire_auto_scan_config_async(self, request):
        """修改自动扫描配置

        修改自动扫描配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateExpireAutoScanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateExpireAutoScanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateExpireAutoScanConfigResponse`
        """
        return self._update_expire_auto_scan_config_with_http_info(request)

    def _update_expire_auto_scan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/scan-expire-keys/autoscan-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateExpireAutoScanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_hotkey_auto_scan_config_async(self, request):
        """设置热key自动分析配置

        设置热key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateHotkeyAutoScanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateHotkeyAutoScanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateHotkeyAutoScanConfigResponse`
        """
        return self._update_hotkey_auto_scan_config_with_http_info(request)

    def _update_hotkey_auto_scan_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateHotkeyAutoScanConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_async(self, request):
        """修改实例信息

        修改缓存实例的信息，可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceResponse`
        """
        return self._update_instance_with_http_info(request)

    def _update_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_bandwidth_async(self, request):
        """变更指定实例的带宽

        变更指定实例的带宽
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceBandwidth
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceBandwidthRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceBandwidthResponse`
        """
        return self._update_instance_bandwidth_with_http_info(request)

    def _update_instance_bandwidth_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instances/{instance_id}/bandwidth',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_config_async(self, request):
        """异步修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceConfigResponse`
        """
        return self._update_instance_config_with_http_info(request)

    def _update_instance_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            resource_path='/v2/{project_id}/instances/{instance_id}/async-configs',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_migration_task_async(self, request):
        """设置迁移任务自动重连

        设置迁移任务自动重连
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateMigrationTaskResponse`
        """
        return self._update_migration_task_with_http_info(request)

    def _update_migration_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v2/{project_id}/migration-task/{task_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMigrationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_password_async(self, request):
        """修改密码

        修改缓存实例的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePassword
        :type request: :class:`huaweicloudsdkdcs.v2.UpdatePasswordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdatePasswordResponse`
        """
        return self._update_password_with_http_info(request)

    def _update_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdatePasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_slave_priority_async(self, request):
        """设置备节点优先级

        设置副本优先级，主节点故障时，权重越小的备节点切换为主节点的优先级越高。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSlavePriority
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateSlavePriorityRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateSlavePriorityResponse`
        """
        return self._update_slave_priority_with_http_info(request)

    def _update_slave_priority_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateSlavePriorityResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ip_whitelist_async(self, request):
        """查询指定实例的IP白名单

        查询指定实例的IP白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIpWhitelist
        :type request: :class:`huaweicloudsdkdcs.v2.ShowIpWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowIpWhitelistResponse`
        """
        return self._show_ip_whitelist_with_http_info(request)

    def _show_ip_whitelist_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/instance/{instance_id}/whitelist',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIpWhitelistResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_ip_whitelist_async(self, request):
        """设置IP白名单分组

        为指定实例设置IP白名单分组，包含创建、停用、编辑、删除白名单四个功能
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateIpWhitelist
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateIpWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateIpWhitelistResponse`
        """
        return self._update_ip_whitelist_with_http_info(request)

    def _update_ip_whitelist_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
            cname=cname,
            response_type='UpdateIpWhitelistResponse',
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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdcs'")


class DcsClient(Client):
    def __init__(self):
        super(DcsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdcs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DcsClient":
                raise TypeError("client type error, support client type is DcsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_or_delete_tags(self, request):
        r"""批量添加或删除标签

        为指定实例批量添加标签，或批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateOrDeleteTags
        :type request: :class:`huaweicloudsdkdcs.v2.BatchCreateOrDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchCreateOrDeleteTagsResponse`
        """
        http_info = self._batch_create_or_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_tags_invoker(self, request):
        http_info = self._batch_create_or_delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_or_delete_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dcs/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteTagsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def batch_delete_instances(self, request):
        r"""批量删除实例

        批量删除多个缓存实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteInstances
        :type request: :class:`huaweicloudsdkdcs.v2.BatchDeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchDeleteInstancesResponse`
        """
        http_info = self._batch_delete_instances_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_instances_invoker(self, request):
        http_info = self._batch_delete_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_instances_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'all_failure' in local_var_params:
            query_params.append(('all_failure', local_var_params['all_failure']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def batch_restart_online_migration_tasks(self, request):
        r"""批量重启在线迁移任务

        批量重启在线迁移任务，接口响应成功，返回重启在线迁移任务下发结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRestartOnlineMigrationTasks
        :type request: :class:`huaweicloudsdkdcs.v2.BatchRestartOnlineMigrationTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchRestartOnlineMigrationTasksResponse`
        """
        http_info = self._batch_restart_online_migration_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_restart_online_migration_tasks_invoker(self, request):
        http_info = self._batch_restart_online_migration_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_restart_online_migration_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-tasks/batch-restart",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestartOnlineMigrationTasksResponse"
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
            ['application/json;charset=UTF-8'])

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

    def batch_show_nodes_information(self, request):
        r"""批量查询实例节点信息

        批量查询指定项目所有实例的节点信息、有效实例个数及节点个数。
        创建中实例不返回节点信息。
        仅支持Redis4.0和Redis5.0实例查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowNodesInformation
        :type request: :class:`huaweicloudsdkdcs.v2.BatchShowNodesInformationRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchShowNodesInformationResponse`
        """
        http_info = self._batch_show_nodes_information_http_info(request)
        return self._call_api(**http_info)

    def batch_show_nodes_information_invoker(self, request):
        http_info = self._batch_show_nodes_information_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_show_nodes_information_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances-logical-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowNodesInformationResponse"
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

    def batch_stop_migration_tasks(self, request):
        r"""批量停止数据迁移任务

        批量停止数据迁移任务，接口响应成功，仅表示下发任务成功。查询到迁移任务状态为TERMINATED时，即停止成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchStopMigrationTasks
        :type request: :class:`huaweicloudsdkdcs.v2.BatchStopMigrationTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.BatchStopMigrationTasksResponse`
        """
        http_info = self._batch_stop_migration_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_migration_tasks_invoker(self, request):
        http_info = self._batch_stop_migration_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_stop_migration_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-task/batch-stop",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopMigrationTasksResponse"
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
            ['application/json;charset=UTF-8'])

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

    def change_master_standby(self, request):
        r"""主备切换

        切换实例主备节点，只有主备实例支持该操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeMasterStandby
        :type request: :class:`huaweicloudsdkdcs.v2.ChangeMasterStandbyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ChangeMasterStandbyResponse`
        """
        http_info = self._change_master_standby_http_info(request)
        return self._call_api(**http_info)

    def change_master_standby_invoker(self, request):
        http_info = self._change_master_standby_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_master_standby_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/swap",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeMasterStandbyResponse"
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

    def change_master_standby_async(self, request):
        r"""异步交换实例主备节点

        异步交换实例主备节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeMasterStandbyAsync
        :type request: :class:`huaweicloudsdkdcs.v2.ChangeMasterStandbyAsyncRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ChangeMasterStandbyAsyncResponse`
        """
        http_info = self._change_master_standby_async_http_info(request)
        return self._call_api(**http_info)

    def change_master_standby_async_invoker(self, request):
        http_info = self._change_master_standby_async_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_master_standby_async_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/async-swap",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeMasterStandbyAsyncResponse"
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

    def change_nodes_start_stop_status(self, request):
        r"""指定实例节点启停开关

        实例节点启停。执行节点关机操作前的24小时内，需要对实例（单机实例除外）进行数据备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeNodesStartStopStatus
        :type request: :class:`huaweicloudsdkdcs.v2.ChangeNodesStartStopStatusRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ChangeNodesStartStopStatusResponse`
        """
        http_info = self._change_nodes_start_stop_status_http_info(request)
        return self._call_api(**http_info)

    def change_nodes_start_stop_status_invoker(self, request):
        http_info = self._change_nodes_start_stop_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_nodes_start_stop_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/nodes/status",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeNodesStartStopStatusResponse"
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
            ['application/json;charset=UTF-8'])

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

    def copy_instance(self, request):
        r"""备份指定实例

        备份指定的缓存实例。
        &gt; 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyInstance
        :type request: :class:`huaweicloudsdkdcs.v2.CopyInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CopyInstanceResponse`
        """
        http_info = self._copy_instance_http_info(request)
        return self._call_api(**http_info)

    def copy_instance_invoker(self, request):
        http_info = self._copy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "CopyInstanceResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_acl_account(self, request):
        r"""创建ACL账号

        \&quot;为redis4.0/5.0实例（Cluster集群实例除外）创建权限访问账号，包含读写和只读权限。
        如果实例默认账号已开启免密访问，您创建的普通账号不能使用，如需使用普通账号请先关闭默认账号的免密访问。
        单机、主备实例默认账号的密码不能带有冒号(:)，否则无法创建普通账号。\&quot;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAclAccount
        :type request: :class:`huaweicloudsdkdcs.v2.CreateAclAccountRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateAclAccountResponse`
        """
        http_info = self._create_acl_account_http_info(request)
        return self._call_api(**http_info)

    def create_acl_account_invoker(self, request):
        http_info = self._create_acl_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_acl_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAclAccountResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_auto_expire_scan_task(self, request):
        r"""创建过期key扫描任务

        创建过期key扫描任务（Redis 3.0 不支持过期key扫描）。
        过期key扫描会对键空间进行Redis的scan扫描，释放内存中已过期但是由于惰性删除机制而没有释放的内存空间。
        过期key扫描在主节点上执行，会对实例性能有一定的影响，建议不要在业务高峰期进行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutoExpireScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateAutoExpireScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateAutoExpireScanTaskResponse`
        """
        http_info = self._create_auto_expire_scan_task_http_info(request)
        return self._call_api(**http_info)

    def create_auto_expire_scan_task_invoker(self, request):
        http_info = self._create_auto_expire_scan_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_auto_expire_scan_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/scan-expire-keys-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAutoExpireScanTaskResponse"
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

    def create_bigkey_scan_task(self, request):
        r"""创建大key分析任务

        为Redis实例创建大key分析任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBigkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateBigkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateBigkeyScanTaskResponse`
        """
        http_info = self._create_bigkey_scan_task_http_info(request)
        return self._call_api(**http_info)

    def create_bigkey_scan_task_invoker(self, request):
        http_info = self._create_bigkey_scan_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_bigkey_scan_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bigkey-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBigkeyScanTaskResponse"
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

    def create_custom_template(self, request):
        r"""创建自定义模板

        创建自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.CreateCustomTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateCustomTemplateResponse`
        """
        http_info = self._create_custom_template_http_info(request)
        return self._call_api(**http_info)

    def create_custom_template_invoker(self, request):
        http_info = self._create_custom_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_custom_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/config-templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCustomTemplateResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_diagnosis_task(self, request):
        r"""创建实例诊断任务

        诊断指定的缓存实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDiagnosisTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateDiagnosisTaskResponse`
        """
        http_info = self._create_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def create_diagnosis_task_invoker(self, request):
        http_info = self._create_diagnosis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_diagnosis_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDiagnosisTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_hotkey_scan_task(self, request):
        r"""创建热key分析任务

        创建热key分析任务，Redis 3.0 不支持热key分析。
        
        热key分析需要将缓存实例配置参数maxmemory-policy设置为allkeys-lfu或volatile-lfu。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHotkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateHotkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateHotkeyScanTaskResponse`
        """
        http_info = self._create_hotkey_scan_task_http_info(request)
        return self._call_api(**http_info)

    def create_hotkey_scan_task_invoker(self, request):
        http_info = self._create_hotkey_scan_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_hotkey_scan_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHotkeyScanTaskResponse"
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

    def create_instance(self, request):
        r"""创建缓存实例

        创建缓存实例，该接口创建的缓存实例支持按需计费和包周期两种方式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkdcs.v2.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateInstanceResponse`
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
            ['application/json;charset=UTF-8'])

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

    def create_migration_task(self, request):
        r"""创建数据迁移任务

        创建数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateMigrationTaskResponse`
        """
        http_info = self._create_migration_task_http_info(request)
        return self._call_api(**http_info)

    def create_migration_task_invoker(self, request):
        http_info = self._create_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_migration_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMigrationTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_online_migration_task(self, request):
        r"""创建在线数据迁移任务

        创建在线数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOnlineMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.CreateOnlineMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateOnlineMigrationTaskResponse`
        """
        http_info = self._create_online_migration_task_http_info(request)
        return self._call_api(**http_info)

    def create_online_migration_task_invoker(self, request):
        http_info = self._create_online_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_online_migration_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration/instance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOnlineMigrationTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_redislog(self, request):
        r"""采集Redis运行日志

        采集Redis运行日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRedislog
        :type request: :class:`huaweicloudsdkdcs.v2.CreateRedislogRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateRedislogResponse`
        """
        http_info = self._create_redislog_http_info(request)
        return self._call_api(**http_info)

    def create_redislog_invoker(self, request):
        http_info = self._create_redislog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_redislog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/redislog",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRedislogResponse"
            }

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

    def create_redislog_download_link(self, request):
        r"""获取日志下载链接

        获取日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRedislogDownloadLink
        :type request: :class:`huaweicloudsdkdcs.v2.CreateRedislogDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateRedislogDownloadLinkResponse`
        """
        http_info = self._create_redislog_download_link_http_info(request)
        return self._call_api(**http_info)

    def create_redislog_download_link_invoker(self, request):
        http_info = self._create_redislog_download_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_redislog_download_link_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/redislog/{id}/links",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRedislogDownloadLinkResponse"
            }

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

    def create_resize_order(self, request):
        r"""包周期实例变更规格

        包周期实例变更规格
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResizeOrder
        :type request: :class:`huaweicloudsdkdcs.v2.CreateResizeOrderRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateResizeOrderResponse`
        """
        http_info = self._create_resize_order_http_info(request)
        return self._call_api(**http_info)

    def create_resize_order_invoker(self, request):
        http_info = self._create_resize_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resize_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/orders/instances/{instance_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResizeOrderResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_acl_account(self, request):
        r"""删除ACL账号

        删除所创建的ACL普通账号
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAclAccount
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteAclAccountRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteAclAccountResponse`
        """
        http_info = self._delete_acl_account_http_info(request)
        return self._call_api(**http_info)

    def delete_acl_account_invoker(self, request):
        http_info = self._delete_acl_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_acl_account_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts/{account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAclAccountResponse"
            }

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

    def delete_background_task(self, request):
        r"""删除后台任务

        删除后台任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackgroundTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteBackgroundTaskResponse`
        """
        http_info = self._delete_background_task_http_info(request)
        return self._call_api(**http_info)

    def delete_background_task_invoker(self, request):
        http_info = self._delete_background_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_background_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackgroundTaskResponse"
            }

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

    def delete_backup_file(self, request):
        r"""删除备份文件

        删除缓存实例已备份的文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackupFile
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteBackupFileRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteBackupFileResponse`
        """
        http_info = self._delete_backup_file_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_file_invoker(self, request):
        http_info = self._delete_backup_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_backup_file_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupFileResponse"
            }

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

    def delete_bigkey_scan_task(self, request):
        r"""删除大key分析记录

        删除大key分析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBigkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteBigkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteBigkeyScanTaskResponse`
        """
        http_info = self._delete_bigkey_scan_task_http_info(request)
        return self._call_api(**http_info)

    def delete_bigkey_scan_task_invoker(self, request):
        http_info = self._delete_bigkey_scan_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bigkey_scan_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bigkey-task/{bigkey_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBigkeyScanTaskResponse"
            }

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

    def delete_center_task(self, request):
        r"""删除任务中心任务

        删除任务中心任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCenterTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteCenterTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteCenterTaskResponse`
        """
        http_info = self._delete_center_task_http_info(request)
        return self._call_api(**http_info)

    def delete_center_task_invoker(self, request):
        http_info = self._delete_center_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_center_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCenterTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

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

    def delete_config_template(self, request):
        r"""删除自定义模板

        删除自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfigTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteConfigTemplateResponse`
        """
        http_info = self._delete_config_template_http_info(request)
        return self._call_api(**http_info)

    def delete_config_template_invoker(self, request):
        http_info = self._delete_config_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_config_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/config-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def delete_diagnosis_task(self, request):
        r"""删除诊断记录

        删除诊断记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDiagnosisTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteDiagnosisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteDiagnosisTaskResponse`
        """
        http_info = self._delete_diagnosis_task_http_info(request)
        return self._call_api(**http_info)

    def delete_diagnosis_task_invoker(self, request):
        http_info = self._delete_diagnosis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_diagnosis_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDiagnosisTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_hotkey_scan_task(self, request):
        r"""删除热key分析任务

        删除热key分析任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHotkeyScanTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteHotkeyScanTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteHotkeyScanTaskResponse`
        """
        http_info = self._delete_hotkey_scan_task_http_info(request)
        return self._call_api(**http_info)

    def delete_hotkey_scan_task_invoker(self, request):
        http_info = self._delete_hotkey_scan_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_hotkey_scan_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey-task/{hotkey_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHotkeyScanTaskResponse"
            }

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

    def delete_instance_bandwidth_auto_scaling_policy(self, request):
        r"""删除实例带宽弹性伸缩策略

        删除实例带宽弹性伸缩策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceBandwidthAutoScalingPolicy
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteInstanceBandwidthAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteInstanceBandwidthAutoScalingPolicyResponse`
        """
        http_info = self._delete_instance_bandwidth_auto_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_bandwidth_auto_scaling_policy_invoker(self, request):
        http_info = self._delete_instance_bandwidth_auto_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_bandwidth_auto_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/autoscaling-policy/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceBandwidthAutoScalingPolicyResponse"
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

    def delete_ip_from_domain_name(self, request):
        r"""域名摘除IP

        将只读副本的IP从域名中摘除，摘除成功后，只读域名不会再解析到该副本IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIpFromDomainName
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteIpFromDomainNameRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteIpFromDomainNameResponse`
        """
        http_info = self._delete_ip_from_domain_name_http_info(request)
        return self._call_api(**http_info)

    def delete_ip_from_domain_name_invoker(self, request):
        http_info = self._delete_ip_from_domain_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_ip_from_domain_name_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/remove-ip",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIpFromDomainNameResponse"
            }

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

    def delete_migration_task(self, request):
        r"""删除数据迁移任务

        删除数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteMigrationTaskResponse`
        """
        http_info = self._delete_migration_task_http_info(request)
        return self._call_api(**http_info)

    def delete_migration_task_invoker(self, request):
        http_info = self._delete_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_migration_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/migration-tasks/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMigrationTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_public_ip(self, request):
        r"""关闭实例公网访问

        关闭实例公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePublicIp
        :type request: :class:`huaweicloudsdkdcs.v2.DeletePublicIpRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeletePublicIpResponse`
        """
        http_info = self._delete_public_ip_http_info(request)
        return self._call_api(**http_info)

    def delete_public_ip_invoker(self, request):
        http_info = self._delete_public_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_public_ip_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/public-ip",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePublicIpResponse"
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

    def delete_single_instance(self, request):
        r"""删除实例

        删除指定的缓存实例，释放该实例的所有资源。
        
        &gt; 如果是删除按需资源，请按照本章节执行；如果是删除包周期资源，即退订，请参考[退订包周期资源](https://support.huaweicloud.com/api-oce/zh-cn_topic_0082522030.html#section2)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSingleInstance
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteSingleInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteSingleInstanceResponse`
        """
        http_info = self._delete_single_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_single_instance_invoker(self, request):
        http_info = self._delete_single_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_single_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSingleInstanceResponse"
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

    def download_hot_key(self, request):
        r"""下载热key

        下载热key。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadHotKey
        :type request: :class:`huaweicloudsdkdcs.v2.DownloadHotKeyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DownloadHotKeyResponse`
        """
        http_info = self._download_hot_key_http_info(request)
        return self._call_api(**http_info)

    def download_hot_key_invoker(self, request):
        http_info = self._download_hot_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_hot_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey/{task_id}/export",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadHotKeyResponse"
            }

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

    def download_ssl_cert(self, request):
        r"""下载实例SSL证书

        下载实例SSL证书。该接口目前仅针对Redis 6.0[基础版](tag:hws,hws_hk)版本实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadSslCert
        :type request: :class:`huaweicloudsdkdcs.v2.DownloadSslCertRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DownloadSslCertResponse`
        """
        http_info = self._download_ssl_cert_http_info(request)
        return self._call_api(**http_info)

    def download_ssl_cert_invoker(self, request):
        http_info = self._download_ssl_cert_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_ssl_cert_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/ssl-certs/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadSslCertResponse"
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

    def exchange_instance_ip(self, request):
        r"""进行IP交换

        进行IP交换
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExchangeInstanceIp
        :type request: :class:`huaweicloudsdkdcs.v2.ExchangeInstanceIpRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExchangeInstanceIpResponse`
        """
        http_info = self._exchange_instance_ip_http_info(request)
        return self._call_api(**http_info)

    def exchange_instance_ip_invoker(self, request):
        http_info = self._exchange_instance_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _exchange_instance_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}/exchange-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ExchangeInstanceIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

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

    def execute_cluster_switchover(self, request):
        r"""集群分片倒换

        集群分片倒换，适用于proxy和cluster实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteClusterSwitchover
        :type request: :class:`huaweicloudsdkdcs.v2.ExecuteClusterSwitchoverRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExecuteClusterSwitchoverResponse`
        """
        http_info = self._execute_cluster_switchover_http_info(request)
        return self._call_api(**http_info)

    def execute_cluster_switchover_invoker(self, request):
        http_info = self._execute_cluster_switchover_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_cluster_switchover_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instance/{instance_id}/groups/{group_id}/replications/{node_id}/async-switchover",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteClusterSwitchoverResponse"
            }

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

    def execute_command_mobilization(self, request):
        r"""执行web-cli命令V2接口

        登入web-cli，执行redis命令
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteCommandMobilization
        :type request: :class:`huaweicloudsdkdcs.v2.ExecuteCommandMobilizationRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExecuteCommandMobilizationResponse`
        """
        http_info = self._execute_command_mobilization_http_info(request)
        return self._call_api(**http_info)

    def execute_command_mobilization_invoker(self, request):
        http_info = self._execute_command_mobilization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_command_mobilization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/webcli/command",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteCommandMobilizationResponse"
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
            ['application/json;charset=UTF-8'])

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

    def export_excel_job(self, request):
        r"""查询实例列表导出任务详情

        查询实例列表导出任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportExcelJob
        :type request: :class:`huaweicloudsdkdcs.v2.ExportExcelJobRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExportExcelJobResponse`
        """
        http_info = self._export_excel_job_http_info(request)
        return self._call_api(**http_info)

    def export_excel_job_invoker(self, request):
        http_info = self._export_excel_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_excel_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/export-job",
            "request_type": request.__class__.__name__,
            "response_type": "ExportExcelJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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

    def export_instances_task(self, request):
        r"""异步导出实例资源

        异步导出实例资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportInstancesTask
        :type request: :class:`huaweicloudsdkdcs.v2.ExportInstancesTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ExportInstancesTaskResponse`
        """
        http_info = self._export_instances_task_http_info(request)
        return self._call_api(**http_info)

    def export_instances_task_invoker(self, request):
        http_info = self._export_instances_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_instances_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportInstancesTaskResponse"
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
            ['application/json;charset=UTF-8'])

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

    def hang_up_clients(self, request):
        r"""kill指定的会话

        kill指定的会话
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HangUpClients
        :type request: :class:`huaweicloudsdkdcs.v2.HangUpClientsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.HangUpClientsResponse`
        """
        http_info = self._hang_up_clients_http_info(request)
        return self._call_api(**http_info)

    def hang_up_clients_invoker(self, request):
        http_info = self._hang_up_clients_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _hang_up_clients_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/clients/kill",
            "request_type": request.__class__.__name__,
            "response_type": "HangUpClientsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def hang_up_kill_all_clients(self, request):
        r"""下发kill指定节点或实例的全部会话任务

        下发kill指定节点或实例的全部会话任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HangUpKillAllClients
        :type request: :class:`huaweicloudsdkdcs.v2.HangUpKillAllClientsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.HangUpKillAllClientsResponse`
        """
        http_info = self._hang_up_kill_all_clients_http_info(request)
        return self._call_api(**http_info)

    def hang_up_kill_all_clients_invoker(self, request):
        http_info = self._hang_up_kill_all_clients_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _hang_up_kill_all_clients_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/clients/kill-all",
            "request_type": request.__class__.__name__,
            "response_type": "HangUpKillAllClientsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def list_acl_accounts(self, request):
        r"""查询ACL账户列表

        查询ACL账户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAclAccounts
        :type request: :class:`huaweicloudsdkdcs.v2.ListAclAccountsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListAclAccountsResponse`
        """
        http_info = self._list_acl_accounts_http_info(request)
        return self._call_api(**http_info)

    def list_acl_accounts_invoker(self, request):
        http_info = self._list_acl_accounts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_acl_accounts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts",
            "request_type": request.__class__.__name__,
            "response_type": "ListAclAccountsResponse"
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

    def list_available_zones(self, request):
        r"""查询可用区信息

        查询所在局点的可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableZones
        :type request: :class:`huaweicloudsdkdcs.v2.ListAvailableZonesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListAvailableZonesResponse`
        """
        http_info = self._list_available_zones_http_info(request)
        return self._call_api(**http_info)

    def list_available_zones_invoker(self, request):
        http_info = self._list_available_zones_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_zones_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/available-zones",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZonesResponse"
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

    def list_background_task(self, request):
        r"""查询后台任务列表

        查询后台任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackgroundTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListBackgroundTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBackgroundTaskResponse`
        """
        http_info = self._list_background_task_http_info(request)
        return self._call_api(**http_info)

    def list_background_task_invoker(self, request):
        http_info = self._list_background_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_background_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackgroundTaskResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def list_backup_file_links(self, request):
        r"""获取备份文件下载链接

        获取指定实例的备份文件下载链接，下载备份文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackupFileLinks
        :type request: :class:`huaweicloudsdkdcs.v2.ListBackupFileLinksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBackupFileLinksResponse`
        """
        http_info = self._list_backup_file_links_http_info(request)
        return self._call_api(**http_info)

    def list_backup_file_links_invoker(self, request):
        http_info = self._list_backup_file_links_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_backup_file_links_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/backups/{backup_id}/links",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupFileLinksResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def list_backup_records(self, request):
        r"""查询实例备份信息

        查询指定缓存实例的备份信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackupRecords
        :type request: :class:`huaweicloudsdkdcs.v2.ListBackupRecordsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBackupRecordsResponse`
        """
        http_info = self._list_backup_records_http_info(request)
        return self._call_api(**http_info)

    def list_backup_records_invoker(self, request):
        http_info = self._list_backup_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_backup_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupRecordsResponse"
            }

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

    def list_bigkey_scan_tasks(self, request):
        r"""查询大key分析任务列表

        查询大key分析任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBigkeyScanTasks
        :type request: :class:`huaweicloudsdkdcs.v2.ListBigkeyScanTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListBigkeyScanTasksResponse`
        """
        http_info = self._list_bigkey_scan_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_bigkey_scan_tasks_invoker(self, request):
        http_info = self._list_bigkey_scan_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bigkey_scan_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bigkey-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListBigkeyScanTasksResponse"
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

    def list_center_task(self, request):
        r"""查询任务中心任务列表

        查询任务中心任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCenterTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListCenterTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListCenterTaskResponse`
        """
        http_info = self._list_center_task_http_info(request)
        return self._call_api(**http_info)

    def list_center_task_invoker(self, request):
        http_info = self._list_center_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_center_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListCenterTaskResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def list_clients(self, request):
        r"""获取会话列表

        获取会话列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClients
        :type request: :class:`huaweicloudsdkdcs.v2.ListClientsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListClientsResponse`
        """
        http_info = self._list_clients_http_info(request)
        return self._call_api(**http_info)

    def list_clients_invoker(self, request):
        http_info = self._list_clients_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_clients_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/clients",
            "request_type": request.__class__.__name__,
            "response_type": "ListClientsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'addr' in local_var_params:
            query_params.append(('addr', local_var_params['addr']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_config_histories(self, request):
        r"""查询实例参数修改记录列表

        查询实例的参数修改记录列表，支持按照关键字查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigHistories
        :type request: :class:`huaweicloudsdkdcs.v2.ListConfigHistoriesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListConfigHistoriesResponse`
        """
        http_info = self._list_config_histories_http_info(request)
        return self._call_api(**http_info)

    def list_config_histories_invoker(self, request):
        http_info = self._list_config_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_config_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/config-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigHistoriesResponse"
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

    def list_config_templates(self, request):
        r"""查询参数模板列表

        查询租户的参数模板列表，支持按照条件查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigTemplates
        :type request: :class:`huaweicloudsdkdcs.v2.ListConfigTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListConfigTemplatesResponse`
        """
        http_info = self._list_config_templates_http_info(request)
        return self._call_api(**http_info)

    def list_config_templates_invoker(self, request):
        http_info = self._list_config_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_config_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/config-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigTemplatesResponse"
            }

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

    def list_configurations(self, request):
        r"""查询实例配置参数

        查询指定实例的配置参数信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkdcs.v2.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListConfigurationsResponse`
        """
        http_info = self._list_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_configurations_invoker(self, request):
        http_info = self._list_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationsResponse"
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

    def list_diagnosis_tasks(self, request):
        r"""查询实例诊断任务列表

        查询指定缓存实例诊断任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDiagnosisTasks
        :type request: :class:`huaweicloudsdkdcs.v2.ListDiagnosisTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListDiagnosisTasksResponse`
        """
        http_info = self._list_diagnosis_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_diagnosis_tasks_invoker(self, request):
        http_info = self._list_diagnosis_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_diagnosis_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "ListDiagnosisTasksResponse"
            }

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

    def list_flavors(self, request):
        r"""查询产品规格

        在创建缓存实例时，需要配置订购的产品规格编码（spec_code），可通过该接口查询产品规格，查询条件不选时默认查询全部。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkdcs.v2.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

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

    def list_group_replication_info(self, request):
        r"""查询分片信息

        查询读写分离实例和集群实例的分片和副本信息，其中，读写分离实例仅Redis4.0和Redis5.0的主备实例支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroupReplicationInfo
        :type request: :class:`huaweicloudsdkdcs.v2.ListGroupReplicationInfoRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListGroupReplicationInfoResponse`
        """
        http_info = self._list_group_replication_info_http_info(request)
        return self._call_api(**http_info)

    def list_group_replication_info_invoker(self, request):
        http_info = self._list_group_replication_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_group_replication_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instance/{instance_id}/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupReplicationInfoResponse"
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

    def list_hot_key_scan_tasks(self, request):
        r"""查询热key分析任务列表

        查询热key分析历史记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHotKeyScanTasks
        :type request: :class:`huaweicloudsdkdcs.v2.ListHotKeyScanTasksRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListHotKeyScanTasksResponse`
        """
        http_info = self._list_hot_key_scan_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_hot_key_scan_tasks_invoker(self, request):
        http_info = self._list_hot_key_scan_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_hot_key_scan_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListHotKeyScanTasksResponse"
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

    def list_instance_operations(self, request):
        r"""查询实例是否可以扩容

        查询实例是否可以扩容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceOperations
        :type request: :class:`huaweicloudsdkdcs.v2.ListInstanceOperationsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListInstanceOperationsResponse`
        """
        http_info = self._list_instance_operations_http_info(request)
        return self._call_api(**http_info)

    def list_instance_operations_invoker(self, request):
        http_info = self._list_instance_operations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_operations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/operations",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceOperationsResponse"
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

    def list_instances(self, request):
        r"""查询所有实例列表

        查询租户的缓存实例列表，支持按照条件查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkdcs.v2.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

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

    def list_maintenance_windows(self, request):
        r"""查询维护时间窗时间段

        查询维护时间窗开始时间和结束时间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMaintenanceWindows
        :type request: :class:`huaweicloudsdkdcs.v2.ListMaintenanceWindowsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMaintenanceWindowsResponse`
        """
        http_info = self._list_maintenance_windows_http_info(request)
        return self._call_api(**http_info)

    def list_maintenance_windows_invoker(self, request):
        http_info = self._list_maintenance_windows_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_maintenance_windows_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/instances/maintain-windows",
            "request_type": request.__class__.__name__,
            "response_type": "ListMaintenanceWindowsResponse"
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

    def list_migration_task(self, request):
        r"""查询迁移任务列表

        查询迁移任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskResponse`
        """
        http_info = self._list_migration_task_http_info(request)
        return self._call_api(**http_info)

    def list_migration_task_invoker(self, request):
        http_info = self._list_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_migration_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/migration-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListMigrationTaskResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_migration_task_logs(self, request):
        r"""查询迁移日志列表

        查询迁移日志列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMigrationTaskLogs
        :type request: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskLogsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMigrationTaskLogsResponse`
        """
        http_info = self._list_migration_task_logs_http_info(request)
        return self._call_api(**http_info)

    def list_migration_task_logs_invoker(self, request):
        http_info = self._list_migration_task_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_migration_task_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListMigrationTaskLogsResponse"
            }

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

    def list_monitored_objects(self, request):
        r"""查询主维度信息列表

        查询主维度对象列表，主维度ID当前支持dcs_instance_id，dcs_memcached_instance_id。
        &gt; 该接口当前仅在中国华南区开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMonitoredObjects
        :type request: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsResponse`
        """
        http_info = self._list_monitored_objects_http_info(request)
        return self._call_api(**http_info)

    def list_monitored_objects_invoker(self, request):
        http_info = self._list_monitored_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_monitored_objects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dims/monitored-objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonitoredObjectsResponse"
            }

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

    def list_monitored_objects_of_instance(self, request):
        r"""查询单个主维度下子维度监控对象列表

        查询主维度下子维度监控对象列表，当前支持子维度的主维度ID的有 dcs_instance_id
        &gt; 该接口当前仅在中国华南区开放。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMonitoredObjectsOfInstance
        :type request: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsOfInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListMonitoredObjectsOfInstanceResponse`
        """
        http_info = self._list_monitored_objects_of_instance_http_info(request)
        return self._call_api(**http_info)

    def list_monitored_objects_of_instance_invoker(self, request):
        http_info = self._list_monitored_objects_of_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_monitored_objects_of_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dims/monitored-objects/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListMonitoredObjectsOfInstanceResponse"
            }

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

    def list_number_of_instances_in_different_status(self, request):
        r"""查询实例状态

        查询该租户在当前区域下不同状态的实例数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNumberOfInstancesInDifferentStatus
        :type request: :class:`huaweicloudsdkdcs.v2.ListNumberOfInstancesInDifferentStatusRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListNumberOfInstancesInDifferentStatusResponse`
        """
        http_info = self._list_number_of_instances_in_different_status_http_info(request)
        return self._call_api(**http_info)

    def list_number_of_instances_in_different_status_invoker(self, request):
        http_info = self._list_number_of_instances_in_different_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_number_of_instances_in_different_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/status",
            "request_type": request.__class__.__name__,
            "response_type": "ListNumberOfInstancesInDifferentStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_failure' in local_var_params:
            query_params.append(('include_failure', local_var_params['include_failure']))

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

    def list_redislog(self, request):
        r"""查询Redis运行日志列表

        查询Redis运行日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRedislog
        :type request: :class:`huaweicloudsdkdcs.v2.ListRedislogRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListRedislogResponse`
        """
        http_info = self._list_redislog_http_info(request)
        return self._call_api(**http_info)

    def list_redislog_invoker(self, request):
        http_info = self._list_redislog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_redislog_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/redislog",
            "request_type": request.__class__.__name__,
            "response_type": "ListRedislogResponse"
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
        if 'log_type' in local_var_params:
            query_params.append(('log_type', local_var_params['log_type']))

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

    def list_restore_records(self, request):
        r"""查询实例恢复记录

        查询指定缓存实例的恢复记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreRecords
        :type request: :class:`huaweicloudsdkdcs.v2.ListRestoreRecordsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListRestoreRecordsResponse`
        """
        http_info = self._list_restore_records_http_info(request)
        return self._call_api(**http_info)

    def list_restore_records_invoker(self, request):
        http_info = self._list_restore_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restore_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/restores",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestoreRecordsResponse"
            }

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

    def list_slowlog(self, request):
        r"""查询慢日志

        查询慢日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowlog
        :type request: :class:`huaweicloudsdkdcs.v2.ListSlowlogRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListSlowlogResponse`
        """
        http_info = self._list_slowlog_http_info(request)
        return self._call_api(**http_info)

    def list_slowlog_invoker(self, request):
        http_info = self._list_slowlog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slowlog_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/slowlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowlogResponse"
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
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'role' in local_var_params:
            query_params.append(('role', local_var_params['role']))

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

    def list_statistics_of_running_instances(self, request):
        r"""查询运行中实例的统计信息

        查询当前租户下处于“运行中”状态的缓存实例的统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStatisticsOfRunningInstances
        :type request: :class:`huaweicloudsdkdcs.v2.ListStatisticsOfRunningInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListStatisticsOfRunningInstancesResponse`
        """
        http_info = self._list_statistics_of_running_instances_http_info(request)
        return self._call_api(**http_info)

    def list_statistics_of_running_instances_invoker(self, request):
        http_info = self._list_statistics_of_running_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_statistics_of_running_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/statistic",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatisticsOfRunningInstancesResponse"
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

    def list_tags_of_tenant(self, request):
        r"""查询租户所有标签

        查询租户在指定Project中实例类型的所有资源标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagsOfTenant
        :type request: :class:`huaweicloudsdkdcs.v2.ListTagsOfTenantRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListTagsOfTenantResponse`
        """
        http_info = self._list_tags_of_tenant_http_info(request)
        return self._call_api(**http_info)

    def list_tags_of_tenant_invoker(self, request):
        http_info = self._list_tags_of_tenant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tags_of_tenant_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dcs/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsOfTenantResponse"
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

    def login_web_cli(self, request):
        r"""登录webCli

        登录webCli
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LoginWebCli
        :type request: :class:`huaweicloudsdkdcs.v2.LoginWebCliRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.LoginWebCliResponse`
        """
        http_info = self._login_web_cli_http_info(request)
        return self._call_api(**http_info)

    def login_web_cli_invoker(self, request):
        http_info = self._login_web_cli_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _login_web_cli_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/webcli/auth",
            "request_type": request.__class__.__name__,
            "response_type": "LoginWebCliResponse"
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
            ['application/json;charset=UTF-8'])

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

    def logoff_web_cli(self, request):
        r"""登出webCli

        登出webCli
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LogoffWebCli
        :type request: :class:`huaweicloudsdkdcs.v2.LogoffWebCliRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.LogoffWebCliResponse`
        """
        http_info = self._logoff_web_cli_http_info(request)
        return self._call_api(**http_info)

    def logoff_web_cli_invoker(self, request):
        http_info = self._logoff_web_cli_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _logoff_web_cli_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/webcli/logout",
            "request_type": request.__class__.__name__,
            "response_type": "LogoffWebCliResponse"
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
            ['application/json;charset=UTF-8'])

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

    def migrate_az(self, request):
        r"""变更可用区

        迁移缓存实例可用区，完成单可用区实例跨可用区改造。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateAz
        :type request: :class:`huaweicloudsdkdcs.v2.MigrateAzRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.MigrateAzResponse`
        """
        http_info = self._migrate_az_http_info(request)
        return self._call_api(**http_info)

    def migrate_az_invoker(self, request):
        http_info = self._migrate_az_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_az_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/available-zones",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateAzResponse"
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
            ['application/json;charset=UTF-8'])

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

    def reset_acl_account_pass_word(self, request):
        r"""重置ACL账号密码

        重置ACL账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetAclAccountPassWord
        :type request: :class:`huaweicloudsdkdcs.v2.ResetAclAccountPassWordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ResetAclAccountPassWordResponse`
        """
        http_info = self._reset_acl_account_pass_word_http_info(request)
        return self._call_api(**http_info)

    def reset_acl_account_pass_word_invoker(self, request):
        http_info = self._reset_acl_account_pass_word_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_acl_account_pass_word_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts/{account_id}/password/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetAclAccountPassWordResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def reset_password(self, request):
        r"""重置密码

        重置缓存实例的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkdcs.v2.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/password/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPasswordResponse"
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
            ['application/json;charset=UTF-8'])

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

    def resize_instance(self, request):
        r"""变更实例规格

        用户可以为状态为“运行中”的DCS缓存实例进行规格变更，当前仅能支持按需实例的同副本或分片数量的实例规格变更。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkdcs.v2.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ResizeInstanceResponse`
        """
        http_info = self._resize_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_invoker(self, request):
        http_info = self._resize_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceResponse"
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
            ['application/json;charset=UTF-8'])

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

    def restart_or_flush_instances(self, request):
        r"""重启实例或清空数据

        重启运行中的DCS缓存实例。
        
        清空Redis4.0/Redis5.0的实例数据，数据清空后，无法撤销，且无法恢复，请谨慎操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartOrFlushInstances
        :type request: :class:`huaweicloudsdkdcs.v2.RestartOrFlushInstancesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.RestartOrFlushInstancesResponse`
        """
        http_info = self._restart_or_flush_instances_http_info(request)
        return self._call_api(**http_info)

    def restart_or_flush_instances_invoker(self, request):
        http_info = self._restart_or_flush_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_or_flush_instances_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/status",
            "request_type": request.__class__.__name__,
            "response_type": "RestartOrFlushInstancesResponse"
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
            ['application/json;charset=UTF-8'])

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

    def restore_instance(self, request):
        r"""恢复指定实例

        恢复指定的缓存实例。
        &gt; 只有主备和集群类型的缓存实例支持备份恢复操作，单机实例不支持备份恢复操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreInstance
        :type request: :class:`huaweicloudsdkdcs.v2.RestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.RestoreInstanceResponse`
        """
        http_info = self._restore_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_instance_invoker(self, request):
        http_info = self._restore_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/restores",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreInstanceResponse"
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
            ['application/json;charset=UTF-8'])

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

    def rollback_exchange_instance_ip(self, request):
        r"""IP交换回滚

        IP交换回滚。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RollbackExchangeInstanceIp
        :type request: :class:`huaweicloudsdkdcs.v2.RollbackExchangeInstanceIpRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.RollbackExchangeInstanceIpResponse`
        """
        http_info = self._rollback_exchange_instance_ip_http_info(request)
        return self._call_api(**http_info)

    def rollback_exchange_instance_ip_invoker(self, request):
        http_info = self._rollback_exchange_instance_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rollback_exchange_instance_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}/rollback-ip",
            "request_type": request.__class__.__name__,
            "response_type": "RollbackExchangeInstanceIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def scan_clients(self, request):
        r"""下发查询会话列表任务

        下发查询会话列表任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ScanClients
        :type request: :class:`huaweicloudsdkdcs.v2.ScanClientsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ScanClientsResponse`
        """
        http_info = self._scan_clients_http_info(request)
        return self._call_api(**http_info)

    def scan_clients_invoker(self, request):
        http_info = self._scan_clients_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _scan_clients_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/clients",
            "request_type": request.__class__.__name__,
            "response_type": "ScanClientsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def scan_expire_key(self, request):
        r"""立刻扫描过期Key

        立刻扫描过期Key
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ScanExpireKey
        :type request: :class:`huaweicloudsdkdcs.v2.ScanExpireKeyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ScanExpireKeyResponse`
        """
        http_info = self._scan_expire_key_http_info(request)
        return self._call_api(**http_info)

    def scan_expire_key_invoker(self, request):
        http_info = self._scan_expire_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _scan_expire_key_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/auto-expire/scan",
            "request_type": request.__class__.__name__,
            "response_type": "ScanExpireKeyResponse"
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

    def set_online_migration_task(self, request):
        r"""配置在线数据迁移任务

        配置在线数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetOnlineMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.SetOnlineMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.SetOnlineMigrationTaskResponse`
        """
        http_info = self._set_online_migration_task_http_info(request)
        return self._call_api(**http_info)

    def set_online_migration_task_invoker(self, request):
        http_info = self._set_online_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_online_migration_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration/{task_id}/task",
            "request_type": request.__class__.__name__,
            "response_type": "SetOnlineMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

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

    def show_background_task_progress(self, request):
        r"""查询后台任务详细信息

        查询后台任务详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackgroundTaskProgress
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBackgroundTaskProgressRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBackgroundTaskProgressResponse`
        """
        http_info = self._show_background_task_progress_http_info(request)
        return self._call_api(**http_info)

    def show_background_task_progress_invoker(self, request):
        http_info = self._show_background_task_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_background_task_progress_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tasks/{task_id}/progress",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackgroundTaskProgressResponse"
            }

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

    def show_bandwidths(self, request):
        r"""获取实例分片带宽

        获取实例各个分片带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBandwidths
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBandwidthsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBandwidthsResponse`
        """
        http_info = self._show_bandwidths_http_info(request)
        return self._call_api(**http_info)

    def show_bandwidths_invoker(self, request):
        http_info = self._show_bandwidths_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bandwidths_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBandwidthsResponse"
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

    def show_bigkey_autoscan_config(self, request):
        r"""查询大key自动分析配置

        查询大key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBigkeyAutoscanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBigkeyAutoscanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBigkeyAutoscanConfigResponse`
        """
        http_info = self._show_bigkey_autoscan_config_http_info(request)
        return self._call_api(**http_info)

    def show_bigkey_autoscan_config_invoker(self, request):
        http_info = self._show_bigkey_autoscan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bigkey_autoscan_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bigkey/autoscan",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBigkeyAutoscanConfigResponse"
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

    def show_bigkey_scan_task_details(self, request):
        r"""查询大key分析详情

        查询大key分析详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBigkeyScanTaskDetails
        :type request: :class:`huaweicloudsdkdcs.v2.ShowBigkeyScanTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowBigkeyScanTaskDetailsResponse`
        """
        http_info = self._show_bigkey_scan_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_bigkey_scan_task_details_invoker(self, request):
        http_info = self._show_bigkey_scan_task_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_bigkey_scan_task_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bigkey-task/{bigkey_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBigkeyScanTaskDetailsResponse"
            }

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

    def show_config_history_detail(self, request):
        r"""查询实例参数修改记录详情

        查询实例参数修改记录详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigHistoryDetail
        :type request: :class:`huaweicloudsdkdcs.v2.ShowConfigHistoryDetailRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowConfigHistoryDetailResponse`
        """
        http_info = self._show_config_history_detail_http_info(request)
        return self._call_api(**http_info)

    def show_config_history_detail_invoker(self, request):
        http_info = self._show_config_history_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_config_history_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/config-histories/{history_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigHistoryDetailResponse"
            }

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

    def show_config_template(self, request):
        r"""查询参数模板详情

        查询参数模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.ShowConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowConfigTemplateResponse`
        """
        http_info = self._show_config_template_http_info(request)
        return self._call_api(**http_info)

    def show_config_template_invoker(self, request):
        http_info = self._show_config_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_config_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/config-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigTemplateResponse"
            }

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

    def show_diagnosis_task_details(self, request):
        r"""查询指定诊断报告

        通过报告ID查询诊断报告的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiagnosisTaskDetails
        :type request: :class:`huaweicloudsdkdcs.v2.ShowDiagnosisTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowDiagnosisTaskDetailsResponse`
        """
        http_info = self._show_diagnosis_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_diagnosis_task_details_invoker(self, request):
        http_info = self._show_diagnosis_task_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_diagnosis_task_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/diagnosis/{report_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiagnosisTaskDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'report_id' in local_var_params:
            path_params['report_id'] = local_var_params['report_id']

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

    def show_expire_auto_scan_config(self, request):
        r"""查询自动扫描配置

        查询自动扫描配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExpireAutoScanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.ShowExpireAutoScanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowExpireAutoScanConfigResponse`
        """
        http_info = self._show_expire_auto_scan_config_http_info(request)
        return self._call_api(**http_info)

    def show_expire_auto_scan_config_invoker(self, request):
        http_info = self._show_expire_auto_scan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_expire_auto_scan_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/scan-expire-keys/autoscan-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExpireAutoScanConfigResponse"
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

    def show_expire_key_scan_info(self, request):
        r"""查询过期Key扫描记录

        查询过期Key扫描记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExpireKeyScanInfo
        :type request: :class:`huaweicloudsdkdcs.v2.ShowExpireKeyScanInfoRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowExpireKeyScanInfoResponse`
        """
        http_info = self._show_expire_key_scan_info_http_info(request)
        return self._call_api(**http_info)

    def show_expire_key_scan_info_invoker(self, request):
        http_info = self._show_expire_key_scan_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_expire_key_scan_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/auto-expire/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExpireKeyScanInfoResponse"
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

    def show_hotkey_autoscan_config(self, request):
        r"""查询热key自动分析配置

        查询热key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHotkeyAutoscanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.ShowHotkeyAutoscanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowHotkeyAutoscanConfigResponse`
        """
        http_info = self._show_hotkey_autoscan_config_http_info(request)
        return self._call_api(**http_info)

    def show_hotkey_autoscan_config_invoker(self, request):
        http_info = self._show_hotkey_autoscan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_hotkey_autoscan_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey/autoscan",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHotkeyAutoscanConfigResponse"
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

    def show_hotkey_task_details(self, request):
        r"""查询热key分析详情

        查询热key分析详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHotkeyTaskDetails
        :type request: :class:`huaweicloudsdkdcs.v2.ShowHotkeyTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowHotkeyTaskDetailsResponse`
        """
        http_info = self._show_hotkey_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_hotkey_task_details_invoker(self, request):
        http_info = self._show_hotkey_task_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_hotkey_task_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey-task/{hotkey_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHotkeyTaskDetailsResponse"
            }

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
        r"""查询指定实例

        通过实例ID查询实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkdcs.v2.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowInstanceResponse`
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

    def show_instance_bandwidth_auto_scaling_policy(self, request):
        r"""查询实例带宽弹性伸缩策略

        查询实例带宽弹性伸缩策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceBandwidthAutoScalingPolicy
        :type request: :class:`huaweicloudsdkdcs.v2.ShowInstanceBandwidthAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowInstanceBandwidthAutoScalingPolicyResponse`
        """
        http_info = self._show_instance_bandwidth_auto_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def show_instance_bandwidth_auto_scaling_policy_invoker(self, request):
        http_info = self._show_instance_bandwidth_auto_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_bandwidth_auto_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/autoscaling-policy/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceBandwidthAutoScalingPolicyResponse"
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

    def show_instance_ssl_detail(self, request):
        r"""查询实例SSL信息

        查询实例SSL信息。该接口目前仅针对Redis 6.0[基础版](tag:hws,hws_hk)版本实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceSslDetail
        :type request: :class:`huaweicloudsdkdcs.v2.ShowInstanceSslDetailRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowInstanceSslDetailResponse`
        """
        http_info = self._show_instance_ssl_detail_http_info(request)
        return self._call_api(**http_info)

    def show_instance_ssl_detail_invoker(self, request):
        http_info = self._show_instance_ssl_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_ssl_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/ssl",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceSslDetailResponse"
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

    def show_instance_topology(self, request):
        r"""查询集群实例拓扑关系图

        查询集群实例拓扑关系图。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceTopology
        :type request: :class:`huaweicloudsdkdcs.v2.ShowInstanceTopologyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowInstanceTopologyResponse`
        """
        http_info = self._show_instance_topology_http_info(request)
        return self._call_api(**http_info)

    def show_instance_topology_invoker(self, request):
        http_info = self._show_instance_topology_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_topology_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceTopologyResponse"
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

    def show_instance_version(self, request):
        r"""根据实例ID获取实例内核版本信息

        获取对应实例内核版本号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceVersion
        :type request: :class:`huaweicloudsdkdcs.v2.ShowInstanceVersionRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowInstanceVersionResponse`
        """
        http_info = self._show_instance_version_http_info(request)
        return self._call_api(**http_info)

    def show_instance_version_invoker(self, request):
        http_info = self._show_instance_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceVersionResponse"
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

    def show_job_info(self, request):
        r"""查询租户Job执行结果

        查询租户Job执行结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobInfo
        :type request: :class:`huaweicloudsdkdcs.v2.ShowJobInfoRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowJobInfoResponse`
        """
        http_info = self._show_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_job_info_invoker(self, request):
        http_info = self._show_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInfoResponse"
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

    def show_migration_task(self, request):
        r"""查询迁移任务详情

        查询迁移任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskResponse`
        """
        http_info = self._show_migration_task_http_info(request)
        return self._call_api(**http_info)

    def show_migration_task_invoker(self, request):
        http_info = self._show_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_migration_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_migration_task_stats(self, request):
        r"""查询在线迁移进度明细

        查询在线迁移进度明细。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMigrationTaskStats
        :type request: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskStatsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowMigrationTaskStatsResponse`
        """
        http_info = self._show_migration_task_stats_http_info(request)
        return self._call_api(**http_info)

    def show_migration_task_stats_invoker(self, request):
        http_info = self._show_migration_task_stats_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_migration_task_stats_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}/stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMigrationTaskStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_nodes_information(self, request):
        r"""查询实例节点信息

        查询指定实例的节点信息。
        仅支持Redis4.0和Redis5.0实例查询。
        创建中实例不返回节点信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodesInformation
        :type request: :class:`huaweicloudsdkdcs.v2.ShowNodesInformationRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowNodesInformationResponse`
        """
        http_info = self._show_nodes_information_http_info(request)
        return self._call_api(**http_info)

    def show_nodes_information_invoker(self, request):
        http_info = self._show_nodes_information_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_nodes_information_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/logical-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodesInformationResponse"
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

    def show_quota_of_tenant(self, request):
        r"""查询租户配额

        查询租户默认可以创建的实例数和总内存的配额限制，以及可以申请配额的最大值和最小值。不同的租户在不同的区域配额可能不同。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotaOfTenant
        :type request: :class:`huaweicloudsdkdcs.v2.ShowQuotaOfTenantRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowQuotaOfTenantResponse`
        """
        http_info = self._show_quota_of_tenant_http_info(request)
        return self._call_api(**http_info)

    def show_quota_of_tenant_invoker(self, request):
        http_info = self._show_quota_of_tenant_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quota_of_tenant_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotaOfTenantResponse"
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

    def show_replication_states(self, request):
        r"""获取副本状态

        获取副本状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReplicationStates
        :type request: :class:`huaweicloudsdkdcs.v2.ShowReplicationStatesRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowReplicationStatesResponse`
        """
        http_info = self._show_replication_states_http_info(request)
        return self._call_api(**http_info)

    def show_replication_states_invoker(self, request):
        http_info = self._show_replication_states_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_replication_states_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instance/{instance_id}/groups/{group_id}/group-nodes-state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReplicationStatesResponse"
            }

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

    def show_tags(self, request):
        r"""查询单个实例标签

        通过实例ID查询标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTags
        :type request: :class:`huaweicloudsdkdcs.v2.ShowTagsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowTagsResponse`
        """
        http_info = self._show_tags_http_info(request)
        return self._call_api(**http_info)

    def show_tags_invoker(self, request):
        http_info = self._show_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTagsResponse"
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

    def start_instance_resize_check_job(self, request):
        r"""提交前置检查任务

        提交前置检查任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartInstanceResizeCheckJob
        :type request: :class:`huaweicloudsdkdcs.v2.StartInstanceResizeCheckJobRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.StartInstanceResizeCheckJobResponse`
        """
        http_info = self._start_instance_resize_check_job_http_info(request)
        return self._call_api(**http_info)

    def start_instance_resize_check_job_invoker(self, request):
        http_info = self._start_instance_resize_check_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_instance_resize_check_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/resize/check-job",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceResizeCheckJobResponse"
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
            ['application/json;charset=UTF-8'])

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

    def stop_migration_task(self, request):
        r"""停止数据迁移任务

        停止数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskResponse`
        """
        http_info = self._stop_migration_task_http_info(request)
        return self._call_api(**http_info)

    def stop_migration_task_invoker(self, request):
        http_info = self._stop_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_migration_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def stop_migration_task_sync(self, request):
        r"""同步停止数据迁移任务

        同步停止数据迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopMigrationTaskSync
        :type request: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskSyncRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.StopMigrationTaskSyncResponse`
        """
        http_info = self._stop_migration_task_sync_http_info(request)
        return self._call_api(**http_info)

    def stop_migration_task_sync_invoker(self, request):
        http_info = self._stop_migration_task_sync_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_migration_task_sync_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}/sync-stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopMigrationTaskSyncResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def update_acl_account(self, request):
        r"""修改ACL角色

        修改用户的类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclAccount
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountResponse`
        """
        http_info = self._update_acl_account_http_info(request)
        return self._call_api(**http_info)

    def update_acl_account_invoker(self, request):
        http_info = self._update_acl_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_acl_account_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts/{account_id}/role",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAclAccountResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def update_acl_account_pass_word(self, request):
        r"""修改ACL账号密码

        修改ACL账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclAccountPassWord
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountPassWordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountPassWordResponse`
        """
        http_info = self._update_acl_account_pass_word_http_info(request)
        return self._call_api(**http_info)

    def update_acl_account_pass_word_invoker(self, request):
        http_info = self._update_acl_account_pass_word_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_acl_account_pass_word_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts/{account_id}/password/modify",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAclAccountPassWordResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def update_acl_account_remark(self, request):
        r"""ACL账号修改备注

        ACL账号修改备注
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAclAccountRemark
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountRemarkRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateAclAccountRemarkResponse`
        """
        http_info = self._update_acl_account_remark_http_info(request)
        return self._call_api(**http_info)

    def update_acl_account_remark_invoker(self, request):
        http_info = self._update_acl_account_remark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_acl_account_remark_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/accounts/{account_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAclAccountRemarkResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def update_bandwidth(self, request):
        r"""修改实例分片带宽

        修改实例分片带宽。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidth
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateBandwidthRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateBandwidthResponse`
        """
        http_info = self._update_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_bandwidth_invoker(self, request):
        http_info = self._update_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_bandwidth_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bandwidths",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBandwidthResponse"
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

    def update_bigkey_autoscan_config(self, request):
        r"""设置大key自动分析配置

        设置大key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBigkeyAutoscanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateBigkeyAutoscanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateBigkeyAutoscanConfigResponse`
        """
        http_info = self._update_bigkey_autoscan_config_http_info(request)
        return self._call_api(**http_info)

    def update_bigkey_autoscan_config_invoker(self, request):
        http_info = self._update_bigkey_autoscan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_bigkey_autoscan_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bigkey/autoscan",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBigkeyAutoscanConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_client_ip_transparent_transmission(self, request):
        r"""开启或关闭客户端ip透传

        开启或关闭客户端ip透传
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClientIpTransparentTransmission
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateClientIpTransparentTransmissionRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateClientIpTransparentTransmissionResponse`
        """
        http_info = self._update_client_ip_transparent_transmission_http_info(request)
        return self._call_api(**http_info)

    def update_client_ip_transparent_transmission_invoker(self, request):
        http_info = self._update_client_ip_transparent_transmission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_client_ip_transparent_transmission_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/{instance_id}/client-ip-transparent-transmission",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClientIpTransparentTransmissionResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_config_template(self, request):
        r"""修改自定义模板

        修改自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigTemplate
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateConfigTemplateRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateConfigTemplateResponse`
        """
        http_info = self._update_config_template_http_info(request)
        return self._call_api(**http_info)

    def update_config_template_invoker(self, request):
        http_info = self._update_config_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_config_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/config-templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_configurations(self, request):
        r"""修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigurations
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateConfigurationsResponse`
        """
        http_info = self._update_configurations_http_info(request)
        return self._call_api(**http_info)

    def update_configurations_invoker(self, request):
        http_info = self._update_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_configurations_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigurationsResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_expire_auto_scan_config(self, request):
        r"""修改自动扫描配置

        修改自动扫描配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateExpireAutoScanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateExpireAutoScanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateExpireAutoScanConfigResponse`
        """
        http_info = self._update_expire_auto_scan_config_http_info(request)
        return self._call_api(**http_info)

    def update_expire_auto_scan_config_invoker(self, request):
        http_info = self._update_expire_auto_scan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_expire_auto_scan_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/scan-expire-keys/autoscan-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateExpireAutoScanConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_hotkey_auto_scan_config(self, request):
        r"""设置热key自动分析配置

        设置热key自动分析配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHotkeyAutoScanConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateHotkeyAutoScanConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateHotkeyAutoScanConfigResponse`
        """
        http_info = self._update_hotkey_auto_scan_config_http_info(request)
        return self._call_api(**http_info)

    def update_hotkey_auto_scan_config_invoker(self, request):
        http_info = self._update_hotkey_auto_scan_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_hotkey_auto_scan_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/hotkey/autoscan",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHotkeyAutoScanConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_instance(self, request):
        r"""修改实例信息

        修改缓存实例的信息，可修改信息包括实例名称、描述、备份策略、维护时间窗开始和结束时间以及安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstance
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceResponse`
        """
        http_info = self._update_instance_http_info(request)
        return self._call_api(**http_info)

    def update_instance_invoker(self, request):
        http_info = self._update_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_instance_bandwidth(self, request):
        r"""变更指定实例的带宽

        变更指定实例的带宽
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceBandwidth
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceBandwidthRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceBandwidthResponse`
        """
        http_info = self._update_instance_bandwidth_http_info(request)
        return self._call_api(**http_info)

    def update_instance_bandwidth_invoker(self, request):
        http_info = self._update_instance_bandwidth_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_bandwidth_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceBandwidthResponse"
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

    def update_instance_bandwidth_auto_scaling_policy(self, request):
        r"""更新实例带宽弹性伸缩策略

        更新实例带宽弹性伸缩策略。暂不支持实例带宽自动回缩。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceBandwidthAutoScalingPolicy
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceBandwidthAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceBandwidthAutoScalingPolicyResponse`
        """
        http_info = self._update_instance_bandwidth_auto_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def update_instance_bandwidth_auto_scaling_policy_invoker(self, request):
        http_info = self._update_instance_bandwidth_auto_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_bandwidth_auto_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/autoscaling-policy/bandwidth",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceBandwidthAutoScalingPolicyResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_instance_config(self, request):
        r"""异步修改实例配置参数

        为了确保分布式缓存服务发挥出最优性能，您可以根据自己的业务情况对DCS缓存实例的运行参数进行调整。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfig
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateInstanceConfigRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateInstanceConfigResponse`
        """
        http_info = self._update_instance_config_http_info(request)
        return self._call_api(**http_info)

    def update_instance_config_invoker(self, request):
        http_info = self._update_instance_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/async-configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceConfigResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_ip_whitelist_async(self, request):
        r"""设置IP白名单分组异步接口

        为指定实例设置IP白名单分组，包含创建、停用、编辑、删除白名单四个功能。返回异步任务jobId，设置白名单分组信息会覆盖掉已有的白名单信息，因此在新增IP白名单分组时，需保留已有的白名单信息后再编辑新的白名单分组信息。
        [仅Redis 4.0及以上版本的实例支持设置IP白名单分组，Redis 3.0实例不支持该功能。](tag:dt)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIpWhitelistAsync
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateIpWhitelistAsyncRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateIpWhitelistAsyncResponse`
        """
        http_info = self._update_ip_whitelist_async_http_info(request)
        return self._call_api(**http_info)

    def update_ip_whitelist_async_invoker(self, request):
        http_info = self._update_ip_whitelist_async_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ip_whitelist_async_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instance/{instance_id}/whitelist-async",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpWhitelistAsyncResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_migration_task(self, request):
        r"""设置迁移任务自动重连

        设置迁移任务自动重连
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMigrationTask
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateMigrationTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateMigrationTaskResponse`
        """
        http_info = self._update_migration_task_http_info(request)
        return self._call_api(**http_info)

    def update_migration_task_invoker(self, request):
        http_info = self._update_migration_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_migration_task_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/migration-task/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMigrationTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            ['application/json;charset=UTF-8'])

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

    def update_password(self, request):
        r"""修改密码

        修改缓存实例的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePassword
        :type request: :class:`huaweicloudsdkdcs.v2.UpdatePasswordRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdatePasswordResponse`
        """
        http_info = self._update_password_http_info(request)
        return self._call_api(**http_info)

    def update_password_invoker(self, request):
        http_info = self._update_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePasswordResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_public_ip(self, request):
        r"""开启/修改实例公网访问

        开启/修改实例公网访问。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePublicIp
        :type request: :class:`huaweicloudsdkdcs.v2.UpdatePublicIpRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdatePublicIpResponse`
        """
        http_info = self._update_public_ip_http_info(request)
        return self._call_api(**http_info)

    def update_public_ip_invoker(self, request):
        http_info = self._update_public_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_public_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/public-ip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePublicIpResponse"
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
            ['application/json;charset=UTF-8'])

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

    def update_slave_priority(self, request):
        r"""设置备节点优先级

        设置副本优先级，主节点故障时，权重越小的备节点切换为主节点的优先级越高。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSlavePriority
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateSlavePriorityRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateSlavePriorityResponse`
        """
        http_info = self._update_slave_priority_http_info(request)
        return self._call_api(**http_info)

    def update_slave_priority_invoker(self, request):
        http_info = self._update_slave_priority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_slave_priority_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/groups/{group_id}/replications/{node_id}/slave-priority",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSlavePriorityResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def update_ssl_switch(self, request):
        r"""开启/关闭SSL

        开启/关闭SSL。该接口目前仅针对Redis 6.0[基础版](tag:hws,hws_hk)版本实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSslSwitch
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateSslSwitchRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateSslSwitchResponse`
        """
        http_info = self._update_ssl_switch_http_info(request)
        return self._call_api(**http_info)

    def update_ssl_switch_invoker(self, request):
        http_info = self._update_ssl_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ssl_switch_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/ssl",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSslSwitchResponse"
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
            ['application/json;charset=UTF-8'])

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

    def upgrade_instance_minor_version(self, request):
        r"""升级实例小版本

        升级实例小版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeInstanceMinorVersion
        :type request: :class:`huaweicloudsdkdcs.v2.UpgradeInstanceMinorVersionRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpgradeInstanceMinorVersionResponse`
        """
        http_info = self._upgrade_instance_minor_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_instance_minor_version_invoker(self, request):
        http_info = self._upgrade_instance_minor_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_instance_minor_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/minor-version/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeInstanceMinorVersionResponse"
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
            ['application/json;charset=UTF-8'])

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

    def validate_deletable_replica(self, request):
        r"""校验集群副本是否支持删除

        校验集群副本是否支持删除
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateDeletableReplica
        :type request: :class:`huaweicloudsdkdcs.v2.ValidateDeletableReplicaRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ValidateDeletableReplicaResponse`
        """
        http_info = self._validate_deletable_replica_http_info(request)
        return self._call_api(**http_info)

    def validate_deletable_replica_invoker(self, request):
        http_info = self._validate_deletable_replica_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_deletable_replica_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/deletable-replication",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateDeletableReplicaResponse"
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

    def show_ip_whitelist(self, request):
        r"""查询指定实例的IP白名单

        查询指定实例的IP白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpWhitelist
        :type request: :class:`huaweicloudsdkdcs.v2.ShowIpWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowIpWhitelistResponse`
        """
        http_info = self._show_ip_whitelist_http_info(request)
        return self._call_api(**http_info)

    def show_ip_whitelist_invoker(self, request):
        http_info = self._show_ip_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ip_whitelist_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instance/{instance_id}/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpWhitelistResponse"
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

    def update_ip_whitelist(self, request):
        r"""设置IP白名单分组

        为指定实例设置IP白名单分组，包含创建、停用、编辑、删除白名单四个功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateIpWhitelist
        :type request: :class:`huaweicloudsdkdcs.v2.UpdateIpWhitelistRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.UpdateIpWhitelistResponse`
        """
        http_info = self._update_ip_whitelist_http_info(request)
        return self._call_api(**http_info)

    def update_ip_whitelist_invoker(self, request):
        http_info = self._update_ip_whitelist_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_ip_whitelist_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/instance/{instance_id}/whitelist",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateIpWhitelistResponse"
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
            ['application/json;charset=UTF-8'])

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

    def create_offline_key_analysis(self, request):
        r"""创建离线全量key分析任务

        创建离线全量key分析任务。离线全量key分析用于分析实例指定节点备份文件中的TOP100大key，每种数据类型前缀数量TOP50的key和每种数据类型key的内存占用和数量的分布情况。仅Redis 4.0、5.0、6.0版本及Redis企业版实例支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOfflineKeyAnalysis
        :type request: :class:`huaweicloudsdkdcs.v2.CreateOfflineKeyAnalysisRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.CreateOfflineKeyAnalysisResponse`
        """
        http_info = self._create_offline_key_analysis_http_info(request)
        return self._call_api(**http_info)

    def create_offline_key_analysis_invoker(self, request):
        http_info = self._create_offline_key_analysis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_offline_key_analysis_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/offline/key-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOfflineKeyAnalysisResponse"
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
            ['application/json;charset=UTF-8'])

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

    def delete_offline_key_analysis_task(self, request):
        r"""删除离线全量key分析记录

        删除离线全量key分析记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteOfflineKeyAnalysisTask
        :type request: :class:`huaweicloudsdkdcs.v2.DeleteOfflineKeyAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.DeleteOfflineKeyAnalysisTaskResponse`
        """
        http_info = self._delete_offline_key_analysis_task_http_info(request)
        return self._call_api(**http_info)

    def delete_offline_key_analysis_task_invoker(self, request):
        http_info = self._delete_offline_key_analysis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_offline_key_analysis_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/offline/key-analysis/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteOfflineKeyAnalysisTaskResponse"
            }

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

    def list_offline_key_analysis_task(self, request):
        r"""查询离线全量key分析任务列表

        查询离线全量key分析任务列表，支持Redis4.0、5.0、6.0版本及Redis企业版。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOfflineKeyAnalysisTask
        :type request: :class:`huaweicloudsdkdcs.v2.ListOfflineKeyAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ListOfflineKeyAnalysisTaskResponse`
        """
        http_info = self._list_offline_key_analysis_task_http_info(request)
        return self._call_api(**http_info)

    def list_offline_key_analysis_task_invoker(self, request):
        http_info = self._list_offline_key_analysis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_offline_key_analysis_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/offline/key-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "ListOfflineKeyAnalysisTaskResponse"
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

    def show_offline_key_analysis_task(self, request):
        r"""查询离线全量key分析详情

        查询离线全量key分析详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOfflineKeyAnalysisTask
        :type request: :class:`huaweicloudsdkdcs.v2.ShowOfflineKeyAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkdcs.v2.ShowOfflineKeyAnalysisTaskResponse`
        """
        http_info = self._show_offline_key_analysis_task_http_info(request)
        return self._call_api(**http_info)

    def show_offline_key_analysis_task_invoker(self, request):
        http_info = self._show_offline_key_analysis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_offline_key_analysis_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/instances/{instance_id}/offline/key-analysis/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOfflineKeyAnalysisTaskResponse"
            }

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

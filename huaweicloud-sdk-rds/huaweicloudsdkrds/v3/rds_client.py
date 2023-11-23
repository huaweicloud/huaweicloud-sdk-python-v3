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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkrds'")


class RdsClient(Client):
    def __init__(self):
        super(RdsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrds.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "RdsClient":
                raise TypeError("client type error, support client type is RdsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_postgresql_hba_conf(self, request):
        """在pg_hba.conf文件最后新增单个或多个配置

        以传入配置全量覆盖当前pg_hba.conf文件内容，入参为空时用默认配置覆盖当前文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddPostgresqlHbaConf
        :type request: :class:`huaweicloudsdkrds.v3.AddPostgresqlHbaConfRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AddPostgresqlHbaConfResponse`
        """
        http_info = self._add_postgresql_hba_conf_http_info(request)
        return self._call_api(**http_info)

    def add_postgresql_hba_conf_invoker(self, request):
        http_info = self._add_postgresql_hba_conf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_postgresql_hba_conf_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/hba-info",
            "request_type": request.__class__.__name__,
            "response_type": "AddPostgresqlHbaConfResponse"
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

    def apply_configuration_async(self, request):
        """应用参数模板

        应用参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyConfigurationAsync
        :type request: :class:`huaweicloudsdkrds.v3.ApplyConfigurationAsyncRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ApplyConfigurationAsyncResponse`
        """
        http_info = self._apply_configuration_async_http_info(request)
        return self._call_api(**http_info)

    def apply_configuration_async_invoker(self, request):
        http_info = self._apply_configuration_async_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_configuration_async_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/configurations/{config_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyConfigurationAsyncResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def attach_eip(self, request):
        """绑定和解绑弹性公网IP

        绑定和解绑弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachEip
        :type request: :class:`huaweicloudsdkrds.v3.AttachEipRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AttachEipResponse`
        """
        http_info = self._attach_eip_http_info(request)
        return self._call_api(**http_info)

    def attach_eip_invoker(self, request):
        http_info = self._attach_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/public-ip",
            "request_type": request.__class__.__name__,
            "response_type": "AttachEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def batch_delete_manual_backup(self, request):
        """批量删除手动备份

        批量删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteManualBackup
        :type request: :class:`huaweicloudsdkrds.v3.BatchDeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchDeleteManualBackupResponse`
        """
        http_info = self._batch_delete_manual_backup_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_manual_backup_invoker(self, request):
        http_info = self._batch_delete_manual_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_manual_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteManualBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def batch_restore_database(self, request):
        """库级时间点恢复

        库级时间点恢复
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRestoreDatabase
        :type request: :class:`huaweicloudsdkrds.v3.BatchRestoreDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchRestoreDatabaseResponse`
        """
        http_info = self._batch_restore_database_http_info(request)
        return self._call_api(**http_info)

    def batch_restore_database_invoker(self, request):
        http_info = self._batch_restore_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_restore_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/batch/restore/databases",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestoreDatabaseResponse"
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

    def batch_restore_postgre_sql_tables(self, request):
        """表级时间点恢复（PostgreSQL）

        表级时间点恢复（PostgreSQL）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRestorePostgreSqlTables
        :type request: :class:`huaweicloudsdkrds.v3.BatchRestorePostgreSqlTablesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchRestorePostgreSqlTablesResponse`
        """
        http_info = self._batch_restore_postgre_sql_tables_http_info(request)
        return self._call_api(**http_info)

    def batch_restore_postgre_sql_tables_invoker(self, request):
        http_info = self._batch_restore_postgre_sql_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_restore_postgre_sql_tables_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/batch/restore/tables",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestorePostgreSqlTablesResponse"
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

    def batch_tag_add_action(self, request):
        """批量添加标签

        批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagAddAction
        :type request: :class:`huaweicloudsdkrds.v3.BatchTagAddActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchTagAddActionResponse`
        """
        http_info = self._batch_tag_add_action_http_info(request)
        return self._call_api(**http_info)

    def batch_tag_add_action_invoker(self, request):
        http_info = self._batch_tag_add_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_tag_add_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchTagAddActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def batch_tag_del_action(self, request):
        """批量删除标签

        批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagDelAction
        :type request: :class:`huaweicloudsdkrds.v3.BatchTagDelActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchTagDelActionResponse`
        """
        http_info = self._batch_tag_del_action_http_info(request)
        return self._call_api(**http_info)

    def batch_tag_del_action_invoker(self, request):
        http_info = self._batch_tag_del_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_tag_del_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchTagDelActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def change_failover_mode(self, request):
        """更改主备实例的数据同步方式

        更改主备实例的数据同步方式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeFailoverMode
        :type request: :class:`huaweicloudsdkrds.v3.ChangeFailoverModeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeFailoverModeResponse`
        """
        http_info = self._change_failover_mode_http_info(request)
        return self._call_api(**http_info)

    def change_failover_mode_invoker(self, request):
        http_info = self._change_failover_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_failover_mode_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/failover/mode",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeFailoverModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def change_failover_strategy(self, request):
        """切换主备实例的倒换策略

        切换主备实例的倒换策略.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeFailoverStrategy
        :type request: :class:`huaweicloudsdkrds.v3.ChangeFailoverStrategyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeFailoverStrategyResponse`
        """
        http_info = self._change_failover_strategy_http_info(request)
        return self._call_api(**http_info)

    def change_failover_strategy_invoker(self, request):
        http_info = self._change_failover_strategy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_failover_strategy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/failover/strategy",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeFailoverStrategyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def change_ops_window(self, request):
        """设置可维护时间段

        设置可维护时间段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeOpsWindow
        :type request: :class:`huaweicloudsdkrds.v3.ChangeOpsWindowRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeOpsWindowResponse`
        """
        http_info = self._change_ops_window_http_info(request)
        return self._call_api(**http_info)

    def change_ops_window_invoker(self, request):
        http_info = self._change_ops_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_ops_window_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ops-window",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeOpsWindowResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def copy_configuration(self, request):
        """复制参数模板

        复制参数模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.CopyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CopyConfigurationResponse`
        """
        http_info = self._copy_configuration_http_info(request)
        return self._call_api(**http_info)

    def copy_configuration_invoker(self, request):
        http_info = self._copy_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def create_configuration(self, request):
        """创建参数模板

        创建参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.CreateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateConfigurationResponse`
        """
        http_info = self._create_configuration_http_info(request)
        return self._call_api(**http_info)

    def create_configuration_invoker(self, request):
        http_info = self._create_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_dns_name(self, request):
        """申请域名

        申请域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDnsName
        :type request: :class:`huaweicloudsdkrds.v3.CreateDnsNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateDnsNameResponse`
        """
        http_info = self._create_dns_name_http_info(request)
        return self._call_api(**http_info)

    def create_dns_name_invoker(self, request):
        http_info = self._create_dns_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dns_name_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/create-dns",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDnsNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_instance(self, request):
        """创建数据库实例

        创建数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkrds.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateInstanceResponse`
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
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def create_manual_backup(self, request):
        """创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateManualBackup
        :type request: :class:`huaweicloudsdkrds.v3.CreateManualBackupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateManualBackupResponse`
        """
        http_info = self._create_manual_backup_http_info(request)
        return self._call_api(**http_info)

    def create_manual_backup_invoker(self, request):
        http_info = self._create_manual_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_manual_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateManualBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_restore_instance(self, request):
        """恢复到新实例

        恢复到新实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRestoreInstance
        :type request: :class:`huaweicloudsdkrds.v3.CreateRestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateRestoreInstanceResponse`
        """
        http_info = self._create_restore_instance_http_info(request)
        return self._call_api(**http_info)

    def create_restore_instance_invoker(self, request):
        http_info = self._create_restore_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_restore_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRestoreInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_xel_log_download(self, request):
        """获取扩展日志下载信息

        获取扩展日志下载信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateXelLogDownload
        :type request: :class:`huaweicloudsdkrds.v3.CreateXelLogDownloadRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateXelLogDownloadResponse`
        """
        http_info = self._create_xel_log_download_http_info(request)
        return self._call_api(**http_info)

    def create_xel_log_download_invoker(self, request):
        http_info = self._create_xel_log_download_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_xel_log_download_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/xellog-download",
            "request_type": request.__class__.__name__,
            "response_type": "CreateXelLogDownloadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_configuration(self, request):
        """删除参数模板

        删除参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteConfigurationResponse`
        """
        http_info = self._delete_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_configuration_invoker(self, request):
        http_info = self._delete_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_configuration_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_instance(self, request):
        """删除数据库实例

        删除数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkrds.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_job(self, request):
        """删除即时任务

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkrds.v3.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def delete_manual_backup(self, request):
        """删除手动备份

        删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteManualBackup
        :type request: :class:`huaweicloudsdkrds.v3.DeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteManualBackupResponse`
        """
        http_info = self._delete_manual_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_manual_backup_invoker(self, request):
        http_info = self._delete_manual_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_manual_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteManualBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_postgresql_hba_conf(self, request):
        """删除pg_hba.conf文件的单个或多个配置

        删除pg_hba.conf文件的单个或多个配置，以priority做唯一标识
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePostgresqlHbaConf
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlHbaConfRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlHbaConfResponse`
        """
        http_info = self._delete_postgresql_hba_conf_http_info(request)
        return self._call_api(**http_info)

    def delete_postgresql_hba_conf_invoker(self, request):
        http_info = self._delete_postgresql_hba_conf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_postgresql_hba_conf_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/hba-info",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePostgresqlHbaConfResponse"
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

    def download_slowlog(self, request):
        """获取慢日志下载链接

        获取慢日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadSlowlog
        :type request: :class:`huaweicloudsdkrds.v3.DownloadSlowlogRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DownloadSlowlogResponse`
        """
        http_info = self._download_slowlog_http_info(request)
        return self._call_api(**http_info)

    def download_slowlog_invoker(self, request):
        http_info = self._download_slowlog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_slowlog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadSlowlogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def enable_configuration(self, request):
        """应用参数模板

        应用参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.EnableConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.EnableConfigurationResponse`
        """
        http_info = self._enable_configuration_http_info(request)
        return self._call_api(**http_info)

    def enable_configuration_invoker(self, request):
        http_info = self._enable_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "EnableConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_auditlogs(self, request):
        """获取审计日志列表

        获取审计日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditlogs
        :type request: :class:`huaweicloudsdkrds.v3.ListAuditlogsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuditlogsResponse`
        """
        http_info = self._list_auditlogs_http_info(request)
        return self._call_api(**http_info)

    def list_auditlogs_invoker(self, request):
        http_info = self._list_auditlogs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_auditlogs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auditlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditlogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_backups(self, request):
        """获取备份列表

        获取备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkrds.v3.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListBackupsResponse`
        """
        http_info = self._list_backups_http_info(request)
        return self._call_api(**http_info)

    def list_backups_invoker(self, request):
        http_info = self._list_backups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_backups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_collations(self, request):
        """查询SQLServer可用字符集

        查询SQLServer可用字符集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollations
        :type request: :class:`huaweicloudsdkrds.v3.ListCollationsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListCollationsResponse`
        """
        http_info = self._list_collations_http_info(request)
        return self._call_api(**http_info)

    def list_collations_invoker(self, request):
        http_info = self._list_collations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/collations",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
        """获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkrds.v3.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListConfigurationsResponse`
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
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_datastores(self, request):
        """查询数据库引擎的版本

        查询数据库引擎的版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatastores
        :type request: :class:`huaweicloudsdkrds.v3.ListDatastoresRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDatastoresResponse`
        """
        http_info = self._list_datastores_http_info(request)
        return self._call_api(**http_info)

    def list_datastores_invoker(self, request):
        http_info = self._list_datastores_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_datastores_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/datastores/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatastoresResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_dr_relations(self, request):
        """list_dr_relations

        批量查询容灾实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDrRelations
        :type request: :class:`huaweicloudsdkrds.v3.ListDrRelationsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDrRelationsResponse`
        """
        http_info = self._list_dr_relations_http_info(request)
        return self._call_api(**http_info)

    def list_dr_relations_invoker(self, request):
        http_info = self._list_dr_relations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dr_relations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/disaster-recovery-relation",
            "request_type": request.__class__.__name__,
            "response_type": "ListDrRelationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_engine_flavors(self, request):
        """查询实例可变更规格

        查询实例可变更规格
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEngineFlavors
        :type request: :class:`huaweicloudsdkrds.v3.ListEngineFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListEngineFlavorsResponse`
        """
        http_info = self._list_engine_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_engine_flavors_invoker(self, request):
        http_info = self._list_engine_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_engine_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/available-flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListEngineFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'availability_zone_ids' in local_var_params:
            query_params.append(('availability_zone_ids', local_var_params['availability_zone_ids']))
        if 'ha_mode' in local_var_params:
            query_params.append(('ha_mode', local_var_params['ha_mode']))
        if 'spec_code_like' in local_var_params:
            query_params.append(('spec_code_like', local_var_params['spec_code_like']))
        if 'flavor_category_type' in local_var_params:
            query_params.append(('flavor_category_type', local_var_params['flavor_category_type']))
        if 'is_rha_flavor' in local_var_params:
            query_params.append(('is_rha_flavor', local_var_params['is_rha_flavor']))
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

    def list_error_logs(self, request):
        """查询数据库错误日志

        查询数据库错误日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListErrorLogs
        :type request: :class:`huaweicloudsdkrds.v3.ListErrorLogsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListErrorLogsResponse`
        """
        http_info = self._list_error_logs_http_info(request)
        return self._call_api(**http_info)

    def list_error_logs_invoker(self, request):
        http_info = self._list_error_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_error_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/errorlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListErrorLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_error_logs_new(self, request):
        """查询数据库错误日志

        查询数据库错误日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListErrorLogsNew
        :type request: :class:`huaweicloudsdkrds.v3.ListErrorLogsNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListErrorLogsNewResponse`
        """
        http_info = self._list_error_logs_new_http_info(request)
        return self._call_api(**http_info)

    def list_error_logs_new_invoker(self, request):
        http_info = self._list_error_logs_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_error_logs_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/errorlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListErrorLogsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'level' in local_var_params:
            query_params.append(('level', local_var_params['level']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_errorlog_for_lts(self, request):
        """list_errorlog_for_lts

        查询实例的错误日志数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListErrorlogForLts
        :type request: :class:`huaweicloudsdkrds.v3.ListErrorlogForLtsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListErrorlogForLtsResponse`
        """
        http_info = self._list_errorlog_for_lts_http_info(request)
        return self._call_api(**http_info)

    def list_errorlog_for_lts_invoker(self, request):
        http_info = self._list_errorlog_for_lts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_errorlog_for_lts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/error-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListErrorlogForLtsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_flavors(self, request):
        """查询数据库规格

        查询数据库规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkrds.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListFlavorsResponse`
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
            "resource_path": "/v3/{project_id}/flavors/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'version_name' in local_var_params:
            query_params.append(('version_name', local_var_params['version_name']))
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_history_database(self, request):
        """查询指定时间点可恢复的库

        查询指定时间点可恢复的库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryDatabase
        :type request: :class:`huaweicloudsdkrds.v3.ListHistoryDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListHistoryDatabaseResponse`
        """
        http_info = self._list_history_database_http_info(request)
        return self._call_api(**http_info)

    def list_history_database_invoker(self, request):
        http_info = self._list_history_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/{database_name}/instances/history/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_inspection_histories(self, request):
        """list_inspection_histories

        查询实例大版本升级检查历史。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInspectionHistories
        :type request: :class:`huaweicloudsdkrds.v3.ListInspectionHistoriesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInspectionHistoriesResponse`
        """
        http_info = self._list_inspection_histories_http_info(request)
        return self._call_api(**http_info)

    def list_inspection_histories_invoker(self, request):
        http_info = self._list_inspection_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_inspection_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/major-version/inspection-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListInspectionHistoriesResponse"
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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'target_version' in local_var_params:
            query_params.append(('target_version', local_var_params['target_version']))
        if 'is_available' in local_var_params:
            query_params.append(('is_available', local_var_params['is_available']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_instance_diagnosis(self, request):
        """获取诊断后的实例数量

        获取诊断后的实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceDiagnosis
        :type request: :class:`huaweicloudsdkrds.v3.ListInstanceDiagnosisRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstanceDiagnosisResponse`
        """
        http_info = self._list_instance_diagnosis_http_info(request)
        return self._call_api(**http_info)

    def list_instance_diagnosis_invoker(self, request):
        http_info = self._list_instance_diagnosis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_diagnosis_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/diagnosis",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceDiagnosisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

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

    def list_instance_param_histories(self, request):
        """查询实例参数修改历史

        实例参数修改历史。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceParamHistories
        :type request: :class:`huaweicloudsdkrds.v3.ListInstanceParamHistoriesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstanceParamHistoriesResponse`
        """
        http_info = self._list_instance_param_histories_http_info(request)
        return self._call_api(**http_info)

    def list_instance_param_histories_invoker(self, request):
        http_info = self._list_instance_param_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_param_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configuration-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceParamHistoriesResponse"
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
        if 'param_name' in local_var_params:
            query_params.append(('param_name', local_var_params['param_name']))

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

    def list_instance_tags(self, request):
        """查询实例标签

        查询实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkrds.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstanceTagsResponse`
        """
        http_info = self._list_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_tags_invoker(self, request):
        http_info = self._list_instance_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
        """查询数据库实例列表

        查询数据库实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesResponse`
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
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_instances_info_diagnosis(self, request):
        """获取指定诊断项的诊断结果

        获取指定诊断项的诊断结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesInfoDiagnosis
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesInfoDiagnosisRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesInfoDiagnosisResponse`
        """
        http_info = self._list_instances_info_diagnosis_http_info(request)
        return self._call_api(**http_info)

    def list_instances_info_diagnosis_invoker(self, request):
        http_info = self._list_instances_info_diagnosis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_info_diagnosis_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/diagnosis/info",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesInfoDiagnosisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'diagnosis' in local_var_params:
            query_params.append(('diagnosis', local_var_params['diagnosis']))
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

    def list_instances_support_fast_restore(self, request):
        """获取实例是否能使用极速恢复

        批量获取实例是否能在库表恢复时使用极速恢复。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesSupportFastRestore
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesSupportFastRestoreRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesSupportFastRestoreResponse`
        """
        http_info = self._list_instances_support_fast_restore_http_info(request)
        return self._call_api(**http_info)

    def list_instances_support_fast_restore_invoker(self, request):
        http_info = self._list_instances_support_fast_restore_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_support_fast_restore_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/fast-restore",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesSupportFastRestoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_job_info(self, request):
        """获取指定ID的任务信息

        获取指定ID的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobInfo
        :type request: :class:`huaweicloudsdkrds.v3.ListJobInfoRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListJobInfoResponse`
        """
        http_info = self._list_job_info_http_info(request)
        return self._call_api(**http_info)

    def list_job_info_invoker(self, request):
        http_info = self._list_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_job_info_detail(self, request):
        """获取指定实例和时间范围的任务信息（SQL Server）

        获取指定实例和时间范围的任务信息（SQL Server）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobInfoDetail
        :type request: :class:`huaweicloudsdkrds.v3.ListJobInfoDetailRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListJobInfoDetailResponse`
        """
        http_info = self._list_job_info_detail_http_info(request)
        return self._call_api(**http_info)

    def list_job_info_detail_invoker(self, request):
        http_info = self._list_job_info_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_job_info_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tasklist/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobInfoDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_off_site_backups(self, request):
        """查询跨区域备份列表

        查询跨区域备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOffSiteBackups
        :type request: :class:`huaweicloudsdkrds.v3.ListOffSiteBackupsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListOffSiteBackupsResponse`
        """
        http_info = self._list_off_site_backups_http_info(request)
        return self._call_api(**http_info)

    def list_off_site_backups_invoker(self, request):
        http_info = self._list_off_site_backups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_off_site_backups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/offsite-backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListOffSiteBackupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_off_site_instances(self, request):
        """查询跨区域备份实例列表

        查询跨区域备份实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOffSiteInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListOffSiteInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListOffSiteInstancesResponse`
        """
        http_info = self._list_off_site_instances_http_info(request)
        return self._call_api(**http_info)

    def list_off_site_instances_invoker(self, request):
        http_info = self._list_off_site_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_off_site_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/backups/offsite-backup-instance",
            "request_type": request.__class__.__name__,
            "response_type": "ListOffSiteInstancesResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_off_site_restore_times(self, request):
        """查询跨区域备份可恢复时间段

        查询跨区域备份可恢复时间段。
        如果您备份策略中的保存天数设置较长，建议您传入查询日期“date”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOffSiteRestoreTimes
        :type request: :class:`huaweicloudsdkrds.v3.ListOffSiteRestoreTimesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListOffSiteRestoreTimesResponse`
        """
        http_info = self._list_off_site_restore_times_http_info(request)
        return self._call_api(**http_info)

    def list_off_site_restore_times_invoker(self, request):
        http_info = self._list_off_site_restore_times_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_off_site_restore_times_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/offsite-restore-time",
            "request_type": request.__class__.__name__,
            "response_type": "ListOffSiteRestoreTimesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_postgresql_hba_info(self, request):
        """查询实例的pg_hba.conf文件配置

        查询实例的pg_hba.conf文件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlHbaInfo
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoResponse`
        """
        http_info = self._list_postgresql_hba_info_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_hba_info_invoker(self, request):
        http_info = self._list_postgresql_hba_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_hba_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/hba-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlHbaInfoResponse"
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

    def list_postgresql_hba_info_history(self, request):
        """查询实例的pg_hba.conf文件修改历史

        查询实例的pg_hba.conf文件修改历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlHbaInfoHistory
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoHistoryRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoHistoryResponse`
        """
        http_info = self._list_postgresql_hba_info_history_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_hba_info_history_invoker(self, request):
        http_info = self._list_postgresql_hba_info_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_hba_info_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/hba-info/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlHbaInfoHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
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

    def list_postgresql_list_history_tables(self, request):
        """查询指定时间点可恢复的表(PostgreSQL)

        查询指定时间点可恢复的表(PostgreSQL)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlListHistoryTables
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlListHistoryTablesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlListHistoryTablesResponse`
        """
        http_info = self._list_postgresql_list_history_tables_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_list_history_tables_invoker(self, request):
        http_info = self._list_postgresql_list_history_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_list_history_tables_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/{database_name}/instances/history/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlListHistoryTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_predefined_tag(self, request):
        """list_predefined_tag

        查询预定义标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPredefinedTag
        :type request: :class:`huaweicloudsdkrds.v3.ListPredefinedTagRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPredefinedTagResponse`
        """
        http_info = self._list_predefined_tag_http_info(request)
        return self._call_api(**http_info)

    def list_predefined_tag_invoker(self, request):
        http_info = self._list_predefined_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_predefined_tag_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tags/predefined-tag",
            "request_type": request.__class__.__name__,
            "response_type": "ListPredefinedTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_project_tags(self, request):
        """查询项目标签

        查询项目标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkrds.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_recycle_instances(self, request):
        """查询回收站

        查询回收站实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListRecycleInstancesResponse`
        """
        http_info = self._list_recycle_instances_http_info(request)
        return self._call_api(**http_info)

    def list_recycle_instances_invoker(self, request):
        http_info = self._list_recycle_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_recycle_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/recycle-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecycleInstancesResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_restore_times(self, request):
        """查询可恢复时间段

        查询可恢复时间段。
        如果您备份策略中的保存天数设置较长，建议您传入查询日期“date”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreTimes
        :type request: :class:`huaweicloudsdkrds.v3.ListRestoreTimesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListRestoreTimesResponse`
        """
        http_info = self._list_restore_times_http_info(request)
        return self._call_api(**http_info)

    def list_restore_times_invoker(self, request):
        http_info = self._list_restore_times_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restore_times_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restore-time",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestoreTimesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_simplified_instances(self, request):
        """list_simplified_instances

        获取指定实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSimplifiedInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListSimplifiedInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSimplifiedInstancesResponse`
        """
        http_info = self._list_simplified_instances_http_info(request)
        return self._call_api(**http_info)

    def list_simplified_instances_invoker(self, request):
        http_info = self._list_simplified_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_simplified_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/simplified-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListSimplifiedInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_slow_log_file(self, request):
        """查询慢日志文件列表

        查询慢日志文件列表。
        调用该接口取到慢日志文件名后，可以调用接口/v3/{project_id}/instances/{instance_id}/slowlog-download 获取慢日志文件下载链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogFile
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogFileRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogFileResponse`
        """
        http_info = self._list_slow_log_file_http_info(request)
        return self._call_api(**http_info)

    def list_slow_log_file_invoker(self, request):
        http_info = self._list_slow_log_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_log_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogFileResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_slow_log_statistics_for_lts(self, request):
        """list_slow_log_statistics_for_lts

        查询实例慢日志的统计数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogStatisticsForLts
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogStatisticsForLtsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogStatisticsForLtsResponse`
        """
        http_info = self._list_slow_log_statistics_for_lts_http_info(request)
        return self._call_api(**http_info)

    def list_slow_log_statistics_for_lts_invoker(self, request):
        http_info = self._list_slow_log_statistics_for_lts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_log_statistics_for_lts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/slow-logs/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogStatisticsForLtsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_slow_logs(self, request):
        """查询数据库慢日志

        查询数据库慢日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogs
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogsResponse`
        """
        http_info = self._list_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_slow_logs_invoker(self, request):
        http_info = self._list_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_slow_logs_new(self, request):
        """查询数据库慢日志

        查询数据库慢日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogsNew
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogsNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogsNewResponse`
        """
        http_info = self._list_slow_logs_new_http_info(request)
        return self._call_api(**http_info)

    def list_slow_logs_new_invoker(self, request):
        http_info = self._list_slow_logs_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_logs_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/slowlog",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_slowlog_for_lts(self, request):
        """list_slowlog_for_lts

        查询实例的慢日志数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowlogForLts
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowlogForLtsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowlogForLtsResponse`
        """
        http_info = self._list_slowlog_for_lts_http_info(request)
        return self._call_api(**http_info)

    def list_slowlog_for_lts_invoker(self, request):
        http_info = self._list_slowlog_for_lts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slowlog_for_lts_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowlogForLtsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_slowlog_statistics(self, request):
        """获取慢日志统计信息

        获取慢日志统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowlogStatistics
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowlogStatisticsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowlogStatisticsResponse`
        """
        http_info = self._list_slowlog_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_slowlog_statistics_invoker(self, request):
        http_info = self._list_slowlog_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slowlog_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowlogStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_ssl_cert_download_link(self, request):
        """获取SSL证书下载地址

        获取SSL证书下载地址
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSslCertDownloadLink
        :type request: :class:`huaweicloudsdkrds.v3.ListSslCertDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSslCertDownloadLinkResponse`
        """
        http_info = self._list_ssl_cert_download_link_http_info(request)
        return self._call_api(**http_info)

    def list_ssl_cert_download_link_invoker(self, request):
        http_info = self._list_ssl_cert_download_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ssl_cert_download_link_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ssl-cert/download-link",
            "request_type": request.__class__.__name__,
            "response_type": "ListSslCertDownloadLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_storage_types(self, request):
        """查询数据库磁盘类型

        查询数据库磁盘类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStorageTypes
        :type request: :class:`huaweicloudsdkrds.v3.ListStorageTypesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListStorageTypesResponse`
        """
        http_info = self._list_storage_types_http_info(request)
        return self._call_api(**http_info)

    def list_storage_types_invoker(self, request):
        http_info = self._list_storage_types_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_storage_types_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/storage-type/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database_name' in local_var_params:
            path_params['database_name'] = local_var_params['database_name']

        query_params = []
        if 'version_name' in local_var_params:
            query_params.append(('version_name', local_var_params['version_name']))
        if 'ha_mode' in local_var_params:
            query_params.append(('ha_mode', local_var_params['ha_mode']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_upgrade_histories(self, request):
        """list_upgrade_histories

        查询实例大版本升级历史信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUpgradeHistories
        :type request: :class:`huaweicloudsdkrds.v3.ListUpgradeHistoriesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListUpgradeHistoriesResponse`
        """
        http_info = self._list_upgrade_histories_http_info(request)
        return self._call_api(**http_info)

    def list_upgrade_histories_invoker(self, request):
        http_info = self._list_upgrade_histories_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_upgrade_histories_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/major-version/upgrade-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListUpgradeHistoriesResponse"
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
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_xellog_files(self, request):
        """查询扩展日志文件列表

        查询扩展日志文件列表。
        查询扩展日志文件列表，可以调用接口/v3/{project_id}/instances/{instance_id}/xellog-download 获取扩展日志下载链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListXellogFiles
        :type request: :class:`huaweicloudsdkrds.v3.ListXellogFilesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListXellogFilesResponse`
        """
        http_info = self._list_xellog_files_http_info(request)
        return self._call_api(**http_info)

    def list_xellog_files_invoker(self, request):
        http_info = self._list_xellog_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_xellog_files_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/xellog-files",
            "request_type": request.__class__.__name__,
            "response_type": "ListXellogFilesResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def migrate_follower(self, request):
        """迁移主备实例的备机

        迁移主备实例的备机
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateFollower
        :type request: :class:`huaweicloudsdkrds.v3.MigrateFollowerRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.MigrateFollowerResponse`
        """
        http_info = self._migrate_follower_http_info(request)
        return self._call_api(**http_info)

    def migrate_follower_invoker(self, request):
        http_info = self._migrate_follower_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_follower_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/migrateslave",
            "request_type": request.__class__.__name__,
            "response_type": "MigrateFollowerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def modify_postgresql_hba_conf(self, request):
        """修改pg_hba.conf文件的单个或多个配置

        修改/新增pg_hba.conf文件的单个或多个配置，以priority做唯一标识，priority不存在的新增，存在的修改
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyPostgresqlHbaConf
        :type request: :class:`huaweicloudsdkrds.v3.ModifyPostgresqlHbaConfRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ModifyPostgresqlHbaConfResponse`
        """
        http_info = self._modify_postgresql_hba_conf_http_info(request)
        return self._call_api(**http_info)

    def modify_postgresql_hba_conf_invoker(self, request):
        http_info = self._modify_postgresql_hba_conf_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_postgresql_hba_conf_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/hba-info",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyPostgresqlHbaConfResponse"
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

    def restore_exist_instance(self, request):
        """恢复到已有实例

        恢复到已有实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreExistInstance
        :type request: :class:`huaweicloudsdkrds.v3.RestoreExistInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreExistInstanceResponse`
        """
        http_info = self._restore_exist_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_exist_instance_invoker(self, request):
        http_info = self._restore_exist_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_exist_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreExistInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def restore_tables(self, request):
        """表级时间点恢复(MySQL)

        表级时间点恢复(MySQL)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreTables
        :type request: :class:`huaweicloudsdkrds.v3.RestoreTablesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreTablesResponse`
        """
        http_info = self._restore_tables_http_info(request)
        return self._call_api(**http_info)

    def restore_tables_invoker(self, request):
        http_info = self._restore_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_tables_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restore/tables",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def restore_tables_new(self, request):
        """表级时间点恢复(MySQL)

        表级时间点恢复(MySQL)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreTablesNew
        :type request: :class:`huaweicloudsdkrds.v3.RestoreTablesNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreTablesNewResponse`
        """
        http_info = self._restore_tables_new_http_info(request)
        return self._call_api(**http_info)

    def restore_tables_new_invoker(self, request):
        http_info = self._restore_tables_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_tables_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/restore/tables",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreTablesNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def restore_to_existing_instance(self, request):
        """恢复到已有实例

        恢复到已有实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreToExistingInstance
        :type request: :class:`huaweicloudsdkrds.v3.RestoreToExistingInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreToExistingInstanceResponse`
        """
        http_info = self._restore_to_existing_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_to_existing_instance_invoker(self, request):
        http_info = self._restore_to_existing_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_to_existing_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreToExistingInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_auditlog_policy(self, request):
        """设置审计日志策略

        设置审计日志策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditlogPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetAuditlogPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetAuditlogPolicyResponse`
        """
        http_info = self._set_auditlog_policy_http_info(request)
        return self._call_api(**http_info)

    def set_auditlog_policy_invoker(self, request):
        http_info = self._set_auditlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_auditlog_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auditlog-policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetAuditlogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_auto_enlarge_policy(self, request):
        """设置自动扩容策略

        设置实例存储空间自动扩容策略，按扩容量扣除存储费用。
        可用存储空间小于设置值或者10GB时，自动扩容当前存储空间的15%（非10倍数向上取整，账户余额不足，会导致自动扩容失败）。
        设置只读实例自动扩容与主实例自动扩容互不影响，对只读实例设置自动扩容时，可选择大于或等于主实例的存储空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetAutoEnlargePolicyResponse`
        """
        http_info = self._set_auto_enlarge_policy_http_info(request)
        return self._call_api(**http_info)

    def set_auto_enlarge_policy_invoker(self, request):
        http_info = self._set_auto_enlarge_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_auto_enlarge_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disk-auto-expansion",
            "request_type": request.__class__.__name__,
            "response_type": "SetAutoEnlargePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_backup_policy(self, request):
        """设置自动备份策略

        设置自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetBackupPolicyResponse`
        """
        http_info = self._set_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def set_backup_policy_invoker(self, request):
        http_info = self._set_backup_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_backup_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetBackupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_binlog_clear_policy(self, request):
        """设置binlog本地保留时长

        修改指定实例的binlog本地保留时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBinlogClearPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetBinlogClearPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetBinlogClearPolicyResponse`
        """
        http_info = self._set_binlog_clear_policy_http_info(request)
        return self._call_api(**http_info)

    def set_binlog_clear_policy_invoker(self, request):
        http_info = self._set_binlog_clear_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_binlog_clear_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/binlog/clear-policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetBinlogClearPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_off_site_backup_policy(self, request):
        """设置跨区域备份策略

        设置跨区域备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetOffSiteBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetOffSiteBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetOffSiteBackupPolicyResponse`
        """
        http_info = self._set_off_site_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def set_off_site_backup_policy_invoker(self, request):
        http_info = self._set_off_site_backup_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_off_site_backup_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/offsite-policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetOffSiteBackupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_second_level_monitor(self, request):
        """设置秒级监控策略

        设置实例秒级监控策略，约五分钟后生效，对于1秒监控和5秒监控，计费方式为按需付费（每小时扣费一次）。
        设置只读实例秒级监控与主实例互不影响。
        规格变更到4U以下的实例，秒级监控功能会自动关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSecondLevelMonitor
        :type request: :class:`huaweicloudsdkrds.v3.SetSecondLevelMonitorRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetSecondLevelMonitorResponse`
        """
        http_info = self._set_second_level_monitor_http_info(request)
        return self._call_api(**http_info)

    def set_second_level_monitor_invoker(self, request):
        http_info = self._set_second_level_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_second_level_monitor_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/second-level-monitor",
            "request_type": request.__class__.__name__,
            "response_type": "SetSecondLevelMonitorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_security_group(self, request):
        """修改安全组

        修改安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSecurityGroup
        :type request: :class:`huaweicloudsdkrds.v3.SetSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetSecurityGroupResponse`
        """
        http_info = self._set_security_group_http_info(request)
        return self._call_api(**http_info)

    def set_security_group_invoker(self, request):
        http_info = self._set_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "SetSecurityGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_sensitive_slow_log(self, request):
        """慢日志敏感信息的开关

        V3慢日志敏感信息的开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSensitiveSlowLog
        :type request: :class:`huaweicloudsdkrds.v3.SetSensitiveSlowLogRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetSensitiveSlowLogResponse`
        """
        http_info = self._set_sensitive_slow_log_http_info(request)
        return self._call_api(**http_info)

    def set_sensitive_slow_log_invoker(self, request):
        http_info = self._set_sensitive_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sensitive_slow_log_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-sensitization/{status}",
            "request_type": request.__class__.__name__,
            "response_type": "SetSensitiveSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'status' in local_var_params:
            path_params['status'] = local_var_params['status']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_auditlog_download_link(self, request):
        """生成审计日志下载链接

        生成审计日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditlogDownloadLink
        :type request: :class:`huaweicloudsdkrds.v3.ShowAuditlogDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAuditlogDownloadLinkResponse`
        """
        http_info = self._show_auditlog_download_link_http_info(request)
        return self._call_api(**http_info)

    def show_auditlog_download_link_invoker(self, request):
        http_info = self._show_auditlog_download_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auditlog_download_link_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auditlog-links",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditlogDownloadLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_auditlog_policy(self, request):
        """查询审计日志策略

        查询审计日志策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditlogPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowAuditlogPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAuditlogPolicyResponse`
        """
        http_info = self._show_auditlog_policy_http_info(request)
        return self._call_api(**http_info)

    def show_auditlog_policy_invoker(self, request):
        http_info = self._show_auditlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auditlog_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auditlog-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditlogPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_auto_enlarge_policy(self, request):
        """查询自动扩容策略

        查询实例存储空间自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAutoEnlargePolicyResponse`
        """
        http_info = self._show_auto_enlarge_policy_http_info(request)
        return self._call_api(**http_info)

    def show_auto_enlarge_policy_invoker(self, request):
        http_info = self._show_auto_enlarge_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_enlarge_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disk-auto-expansion",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoEnlargePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_available_version(self, request):
        """show_available_version

        查询实例可升级的目标版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAvailableVersion
        :type request: :class:`huaweicloudsdkrds.v3.ShowAvailableVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAvailableVersionResponse`
        """
        http_info = self._show_available_version_http_info(request)
        return self._call_api(**http_info)

    def show_available_version_invoker(self, request):
        http_info = self._show_available_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_available_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/major-version/available-version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAvailableVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_backup_download_link(self, request):
        """获取备份下载链接

        获取备份下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupDownloadLink
        :type request: :class:`huaweicloudsdkrds.v3.ShowBackupDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowBackupDownloadLinkResponse`
        """
        http_info = self._show_backup_download_link_http_info(request)
        return self._call_api(**http_info)

    def show_backup_download_link_invoker(self, request):
        http_info = self._show_backup_download_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_download_link_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backup-files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupDownloadLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'backup_id' in local_var_params:
            query_params.append(('backup_id', local_var_params['backup_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_backup_policy(self, request):
        """查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowBackupPolicyResponse`
        """
        http_info = self._show_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def show_backup_policy_invoker(self, request):
        http_info = self._show_backup_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_binlog_clear_policy(self, request):
        """获取binlog本地保留时长

        查寻指定实例的binlog本地保留时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBinlogClearPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowBinlogClearPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowBinlogClearPolicyResponse`
        """
        http_info = self._show_binlog_clear_policy_http_info(request)
        return self._call_api(**http_info)

    def show_binlog_clear_policy_invoker(self, request):
        http_info = self._show_binlog_clear_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_binlog_clear_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/binlog/clear-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBinlogClearPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_configuration(self, request):
        """获取指定参数模板的参数

        获取指定参数模板的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.ShowConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowConfigurationResponse`
        """
        http_info = self._show_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_invoker(self, request):
        http_info = self._show_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_dns_name(self, request):
        """查询实例ipv6域名。

        查询实例ipv6域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDnsName
        :type request: :class:`huaweicloudsdkrds.v3.ShowDnsNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowDnsNameResponse`
        """
        http_info = self._show_dns_name_http_info(request)
        return self._call_api(**http_info)

    def show_dns_name_invoker(self, request):
        http_info = self._show_dns_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dns_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dns-ipv6",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDnsNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dns_type' in local_var_params:
            query_params.append(('dns_type', local_var_params['dns_type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_domain_name(self, request):
        """show_domain_name

        查询实例ipv4域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDomainName
        :type request: :class:`huaweicloudsdkrds.v3.ShowDomainNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowDomainNameResponse`
        """
        http_info = self._show_domain_name_http_info(request)
        return self._call_api(**http_info)

    def show_domain_name_invoker(self, request):
        http_info = self._show_domain_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_domain_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDomainNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dns_type' in local_var_params:
            query_params.append(('dns_type', local_var_params['dns_type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_dr_replica_status(self, request):
        """查询跨云容灾复制状态

        建立跨云容灾关系后，查询主实例和灾备实例间的复制状态及延迟。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDrReplicaStatus
        :type request: :class:`huaweicloudsdkrds.v3.ShowDrReplicaStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowDrReplicaStatusResponse`
        """
        http_info = self._show_dr_replica_status_http_info(request)
        return self._call_api(**http_info)

    def show_dr_replica_status_invoker(self, request):
        http_info = self._show_dr_replica_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dr_replica_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDrReplicaStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_instance_configuration(self, request):
        """获取指定实例的参数模板

        获取指定实例的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.ShowInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowInstanceConfigurationResponse`
        """
        http_info = self._show_instance_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_instance_configuration_invoker(self, request):
        http_info = self._show_instance_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_off_site_backup_policy(self, request):
        """查询跨区域备份策略

        查询跨区域备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOffSiteBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowOffSiteBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowOffSiteBackupPolicyResponse`
        """
        http_info = self._show_off_site_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def show_off_site_backup_policy_invoker(self, request):
        http_info = self._show_off_site_backup_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_off_site_backup_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/offsite-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOffSiteBackupPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_quotas(self, request):
        """查询配额

        查询当前项目下资源配额情况。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkrds.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_recycle_policy(self, request):
        """查询回收站的回收策略。

        查询回收站的回收策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowRecyclePolicyResponse`
        """
        http_info = self._show_recycle_policy_http_info(request)
        return self._call_api(**http_info)

    def show_recycle_policy_invoker(self, request):
        http_info = self._show_recycle_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_recycle_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/recycle-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRecyclePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_replication_status(self, request):
        """获取实例的复制状态。

        获取实例的复制状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReplicationStatus
        :type request: :class:`huaweicloudsdkrds.v3.ShowReplicationStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowReplicationStatusResponse`
        """
        http_info = self._show_replication_status_http_info(request)
        return self._call_api(**http_info)

    def show_replication_status_invoker(self, request):
        http_info = self._show_replication_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_replication_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/replication/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReplicationStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_second_level_monitoring(self, request):
        """查询秒级监控策略

        查询实例秒级监控策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecondLevelMonitoring
        :type request: :class:`huaweicloudsdkrds.v3.ShowSecondLevelMonitoringRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowSecondLevelMonitoringResponse`
        """
        http_info = self._show_second_level_monitoring_http_info(request)
        return self._call_api(**http_info)

    def show_second_level_monitoring_invoker(self, request):
        http_info = self._show_second_level_monitoring_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_second_level_monitoring_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/second-level-monitor",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecondLevelMonitoringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_tde_status(self, request):
        """根据实例id查询sqlserver TDE状态

        根据实例id查询sqlserver TDE状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTdeStatus
        :type request: :class:`huaweicloudsdkrds.v3.ShowTdeStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowTdeStatusResponse`
        """
        http_info = self._show_tde_status_http_info(request)
        return self._call_api(**http_info)

    def show_tde_status_invoker(self, request):
        http_info = self._show_tde_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tde_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tde-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTdeStatusResponse"
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

    def show_upgrade_db_major_version_status(self, request):
        """show_upgrade_db_major_version_status

        查询大版本检查状态或升级状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpgradeDbMajorVersionStatus
        :type request: :class:`huaweicloudsdkrds.v3.ShowUpgradeDbMajorVersionStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowUpgradeDbMajorVersionStatusResponse`
        """
        http_info = self._show_upgrade_db_major_version_status_http_info(request)
        return self._call_api(**http_info)

    def show_upgrade_db_major_version_status_invoker(self, request):
        http_info = self._show_upgrade_db_major_version_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_upgrade_db_major_version_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/major-version/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpgradeDbMajorVersionStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'action' in local_var_params:
            query_params.append(('action', local_var_params['action']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_failover(self, request):
        """手动倒换主备

        手动倒换主备.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartFailover
        :type request: :class:`huaweicloudsdkrds.v3.StartFailoverRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartFailoverResponse`
        """
        http_info = self._start_failover_http_info(request)
        return self._call_api(**http_info)

    def start_failover_invoker(self, request):
        http_info = self._start_failover_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_failover_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/failover",
            "request_type": request.__class__.__name__,
            "response_type": "StartFailoverResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_instance_enlarge_volume_action(self, request):
        """扩容数据库实例的磁盘空间

        扩容数据库实例的磁盘空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartInstanceEnlargeVolumeAction
        :type request: :class:`huaweicloudsdkrds.v3.StartInstanceEnlargeVolumeActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartInstanceEnlargeVolumeActionResponse`
        """
        http_info = self._start_instance_enlarge_volume_action_http_info(request)
        return self._call_api(**http_info)

    def start_instance_enlarge_volume_action_invoker(self, request):
        http_info = self._start_instance_enlarge_volume_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_instance_enlarge_volume_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceEnlargeVolumeActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_instance_restart_action(self, request):
        """重启数据库实例

        重启数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartInstanceRestartAction
        :type request: :class:`huaweicloudsdkrds.v3.StartInstanceRestartActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartInstanceRestartActionResponse`
        """
        http_info = self._start_instance_restart_action_http_info(request)
        return self._call_api(**http_info)

    def start_instance_restart_action_invoker(self, request):
        http_info = self._start_instance_restart_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_instance_restart_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceRestartActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_instance_single_to_ha_action(self, request):
        """单机转主备实例

        单机转主备实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartInstanceSingleToHaAction
        :type request: :class:`huaweicloudsdkrds.v3.StartInstanceSingleToHaActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartInstanceSingleToHaActionResponse`
        """
        http_info = self._start_instance_single_to_ha_action_http_info(request)
        return self._call_api(**http_info)

    def start_instance_single_to_ha_action_invoker(self, request):
        http_info = self._start_instance_single_to_ha_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_instance_single_to_ha_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceSingleToHaActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_recycle_policy(self, request):
        """设置回收站策略

        设置回收站策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartRecyclePolicy
        :type request: :class:`huaweicloudsdkrds.v3.StartRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartRecyclePolicyResponse`
        """
        http_info = self._start_recycle_policy_http_info(request)
        return self._call_api(**http_info)

    def start_recycle_policy_invoker(self, request):
        http_info = self._start_recycle_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_recycle_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/recycle-policy",
            "request_type": request.__class__.__name__,
            "response_type": "StartRecyclePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_resize_flavor_action(self, request):
        """变更数据库实例的规格

        变更数据库实例的规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartResizeFlavorAction
        :type request: :class:`huaweicloudsdkrds.v3.StartResizeFlavorActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartResizeFlavorActionResponse`
        """
        http_info = self._start_resize_flavor_action_http_info(request)
        return self._call_api(**http_info)

    def start_resize_flavor_action_invoker(self, request):
        http_info = self._start_resize_flavor_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_resize_flavor_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StartResizeFlavorActionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def startup_instance(self, request):
        """开启实例

        停止实例以节省费用，在停止数据库实例后，支持手动重新开启实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartupInstance
        :type request: :class:`huaweicloudsdkrds.v3.StartupInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartupInstanceResponse`
        """
        http_info = self._startup_instance_http_info(request)
        return self._call_api(**http_info)

    def startup_instance_invoker(self, request):
        http_info = self._startup_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _startup_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action/startup",
            "request_type": request.__class__.__name__,
            "response_type": "StartupInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def stop_instance(self, request):
        """停止实例

        实例进行关机，通过暂时停止按需实例以节省费用，实例默认停止七天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopInstance
        :type request: :class:`huaweicloudsdkrds.v3.StopInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StopInstanceResponse`
        """
        http_info = self._stop_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_instance_invoker(self, request):
        http_info = self._stop_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action/shutdown",
            "request_type": request.__class__.__name__,
            "response_type": "StopInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def switch_ssl(self, request):
        """设置SSL数据加密

        设置SSL数据加密。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSsl
        :type request: :class:`huaweicloudsdkrds.v3.SwitchSslRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SwitchSslResponse`
        """
        http_info = self._switch_ssl_http_info(request)
        return self._call_api(**http_info)

    def switch_ssl_invoker(self, request):
        http_info = self._switch_ssl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_ssl_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ssl",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchSslResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_configuration(self, request):
        """修改参数模板参数

        修改参数模板参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.UpdateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateConfigurationResponse`
        """
        http_info = self._update_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_configuration_invoker(self, request):
        http_info = self._update_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_data_ip(self, request):
        """修改内网地址

        修改内网地址
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataIp
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDataIpRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDataIpResponse`
        """
        http_info = self._update_data_ip_http_info(request)
        return self._call_api(**http_info)

    def update_data_ip_invoker(self, request):
        http_info = self._update_data_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_data_ip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataIpResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_dns_name(self, request):
        """修改域名

        修改域名
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDnsName
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDnsNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDnsNameResponse`
        """
        http_info = self._update_dns_name_http_info(request)
        return self._call_api(**http_info)

    def update_dns_name_invoker(self, request):
        http_info = self._update_dns_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_dns_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/modify-dns",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDnsNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_instance_configuration(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationResponse`
        """
        http_info = self._update_instance_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_instance_configuration_invoker(self, request):
        http_info = self._update_instance_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_instance_configuration_async(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfigurationAsync
        :type request: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationAsyncRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationAsyncResponse`
        """
        http_info = self._update_instance_configuration_async_http_info(request)
        return self._call_api(**http_info)

    def update_instance_configuration_async_invoker(self, request):
        http_info = self._update_instance_configuration_async_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_configuration_async_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceConfigurationAsyncResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_instance_name(self, request):
        """修改实例名称

        修改实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkrds.v3.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateInstanceNameResponse`
        """
        http_info = self._update_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_instance_name_invoker(self, request):
        http_info = self._update_instance_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_port(self, request):
        """修改数据库端口

        修改数据库端口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePort
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePortRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePortResponse`
        """
        http_info = self._update_port_http_info(request)
        return self._call_api(**http_info)

    def update_port_invoker(self, request):
        http_info = self._update_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/port",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_postgresql_instance_alias(self, request):
        """修改实例备注信息

        修改指定数据库实例的备注信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePostgresqlInstanceAlias
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlInstanceAliasRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlInstanceAliasResponse`
        """
        http_info = self._update_postgresql_instance_alias_http_info(request)
        return self._call_api(**http_info)

    def update_postgresql_instance_alias_invoker(self, request):
        http_info = self._update_postgresql_instance_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_postgresql_instance_alias_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/alias",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePostgresqlInstanceAliasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_tde_status(self, request):
        """sqlserverTDE开关

        sqlserverTDE开关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTdeStatus
        :type request: :class:`huaweicloudsdkrds.v3.UpdateTdeStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateTdeStatusResponse`
        """
        http_info = self._update_tde_status_http_info(request)
        return self._call_api(**http_info)

    def update_tde_status_invoker(self, request):
        http_info = self._update_tde_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_tde_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tde",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTdeStatusResponse"
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

    def upgrade_db_major_version(self, request):
        """upgrade_db_major_version

        PostgreSQL数据库升级大版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeDbMajorVersion
        :type request: :class:`huaweicloudsdkrds.v3.UpgradeDbMajorVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpgradeDbMajorVersionResponse`
        """
        http_info = self._upgrade_db_major_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_db_major_version_invoker(self, request):
        http_info = self._upgrade_db_major_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_db_major_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/major-version/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeDbMajorVersionResponse"
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

    def upgrade_db_major_version_pre_check(self, request):
        """upgrade_db_major_version_pre_check

        大版本升级前进行升级检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeDbMajorVersionPreCheck
        :type request: :class:`huaweicloudsdkrds.v3.UpgradeDbMajorVersionPreCheckRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpgradeDbMajorVersionPreCheckResponse`
        """
        http_info = self._upgrade_db_major_version_pre_check_http_info(request)
        return self._call_api(**http_info)

    def upgrade_db_major_version_pre_check_invoker(self, request):
        http_info = self._upgrade_db_major_version_pre_check_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_db_major_version_pre_check_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/major-version/inspection",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeDbMajorVersionPreCheckResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def upgrade_db_version(self, request):
        """升级内核小版本

        对实例进行小版本升级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeDbVersion
        :type request: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionResponse`
        """
        http_info = self._upgrade_db_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_db_version_invoker(self, request):
        http_info = self._upgrade_db_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_db_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeDbVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def upgrade_db_version_new(self, request):
        """升级内核小版本

        对实例进行小版本升级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeDbVersionNew
        :type request: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionNewResponse`
        """
        http_info = self._upgrade_db_version_new_http_info(request)
        return self._call_api(**http_info)

    def upgrade_db_version_new_invoker(self, request):
        http_info = self._upgrade_db_version_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_db_version_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeDbVersionNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_api_version(self, request):
        """查询API版本列表

        查询API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdkrds.v3.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListApiVersionResponse`
        """
        http_info = self._list_api_version_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_invoker(self, request):
        http_info = self._list_api_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/rds",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionResponse"
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

    def list_api_version_new(self, request):
        """查询API版本列表

        查询API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersionNew
        :type request: :class:`huaweicloudsdkrds.v3.ListApiVersionNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListApiVersionNewResponse`
        """
        http_info = self._list_api_version_new_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_new_invoker(self, request):
        http_info = self._list_api_version_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_version_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionNewResponse"
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

    def show_api_version(self, request):
        """查询指定的API版本信息

        查询指定的API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkrds.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowApiVersionResponse`
        """
        http_info = self._show_api_version_http_info(request)
        return self._call_api(**http_info)

    def show_api_version_invoker(self, request):
        http_info = self._show_api_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/rds/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def revoke_postgresql_db_privilege(self, request):
        """解除数据库帐号权限

        解除数据库帐号权限
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokePostgresqlDbPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.RevokePostgresqlDbPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RevokePostgresqlDbPrivilegeResponse`
        """
        http_info = self._revoke_postgresql_db_privilege_http_info(request)
        return self._call_api(**http_info)

    def revoke_postgresql_db_privilege_invoker(self, request):
        http_info = self._revoke_postgresql_db_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _revoke_postgresql_db_privilege_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_privilege",
            "request_type": request.__class__.__name__,
            "response_type": "RevokePostgresqlDbPrivilegeResponse"
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

    def allow_db_user_privilege(self, request):
        """授权数据库帐号

        授权数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.AllowDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AllowDbUserPrivilegeResponse`
        """
        http_info = self._allow_db_user_privilege_http_info(request)
        return self._call_api(**http_info)

    def allow_db_user_privilege_invoker(self, request):
        http_info = self._allow_db_user_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_db_user_privilege_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_privilege",
            "request_type": request.__class__.__name__,
            "response_type": "AllowDbUserPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_database(self, request):
        """创建数据库

        创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkrds.v3.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateDatabaseResponse`
        """
        http_info = self._create_database_http_info(request)
        return self._call_api(**http_info)

    def create_database_invoker(self, request):
        http_info = self._create_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_db_user(self, request):
        """创建数据库用户

        在指定实例中创建数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbUser
        :type request: :class:`huaweicloudsdkrds.v3.CreateDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateDbUserResponse`
        """
        http_info = self._create_db_user_http_info(request)
        return self._call_api(**http_info)

    def create_db_user_invoker(self, request):
        http_info = self._create_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_db_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_database(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkrds.v3.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteDatabaseResponse`
        """
        http_info = self._delete_database_http_info(request)
        return self._call_api(**http_info)

    def delete_database_invoker(self, request):
        http_info = self._delete_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/{db_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_db_user(self, request):
        """删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbUser
        :type request: :class:`huaweicloudsdkrds.v3.DeleteDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteDbUserResponse`
        """
        http_info = self._delete_db_user_http_info(request)
        return self._call_api(**http_info)

    def delete_db_user_invoker(self, request):
        http_info = self._delete_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_db_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_authorized_databases(self, request):
        """查询指定用户的已授权数据库

        查询指定用户的已授权数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorizedDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListAuthorizedDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuthorizedDatabasesResponse`
        """
        http_info = self._list_authorized_databases_http_info(request)
        return self._call_api(**http_info)

    def list_authorized_databases_invoker(self, request):
        http_info = self._list_authorized_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_authorized_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/database",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizedDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user-name', local_var_params['user_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_authorized_db_users(self, request):
        """查询指定数据库的已授权用户

        查询指定数据库的已授权用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorizedDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListAuthorizedDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuthorizedDbUsersResponse`
        """
        http_info = self._list_authorized_db_users_http_info(request)
        return self._call_api(**http_info)

    def list_authorized_db_users_invoker(self, request):
        http_info = self._list_authorized_db_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_authorized_db_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/db_user",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizedDbUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_name' in local_var_params:
            query_params.append(('db-name', local_var_params['db_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_databases(self, request):
        """查询数据库列表

        查询数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDatabasesResponse`
        """
        http_info = self._list_databases_http_info(request)
        return self._call_api(**http_info)

    def list_databases_invoker(self, request):
        http_info = self._list_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_db_users(self, request):
        """查询数据库用户列表

        查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDbUsersResponse`
        """
        http_info = self._list_db_users_http_info(request)
        return self._call_api(**http_info)

    def list_db_users_invoker(self, request):
        http_info = self._list_db_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_db_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def reset_pwd(self, request):
        """重置数据库密码

        重置数据库密码.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPwd
        :type request: :class:`huaweicloudsdkrds.v3.ResetPwdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ResetPwdResponse`
        """
        http_info = self._reset_pwd_http_info(request)
        return self._call_api(**http_info)

    def reset_pwd_invoker(self, request):
        http_info = self._reset_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_pwd_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetPwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def revoke(self, request):
        """解除数据库帐号权限

        解除数据库帐号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Revoke
        :type request: :class:`huaweicloudsdkrds.v3.RevokeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RevokeResponse`
        """
        http_info = self._revoke_http_info(request)
        return self._call_api(**http_info)

    def revoke_invoker(self, request):
        http_info = self._revoke_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _revoke_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_privilege",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_db_user_pwd(self, request):
        """设置数据库账号密码

        设置数据库账号密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetDbUserPwd
        :type request: :class:`huaweicloudsdkrds.v3.SetDbUserPwdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetDbUserPwdResponse`
        """
        http_info = self._set_db_user_pwd_http_info(request)
        return self._call_api(**http_info)

    def set_db_user_pwd_invoker(self, request):
        http_info = self._set_db_user_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_db_user_pwd_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/resetpwd",
            "request_type": request.__class__.__name__,
            "response_type": "SetDbUserPwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_read_only_switch(self, request):
        """设置数据库用户只读参数

        根据业务需求，设置数据库用户只读
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetReadOnlySwitch
        :type request: :class:`huaweicloudsdkrds.v3.SetReadOnlySwitchRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetReadOnlySwitchResponse`
        """
        http_info = self._set_read_only_switch_http_info(request)
        return self._call_api(**http_info)

    def set_read_only_switch_invoker(self, request):
        http_info = self._set_read_only_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_read_only_switch_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/readonly-status",
            "request_type": request.__class__.__name__,
            "response_type": "SetReadOnlySwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_database(self, request):
        """修改指定实例的数据库备注

        修改指定实例中的数据库备注。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabase
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDatabaseResponse`
        """
        http_info = self._update_database_http_info(request)
        return self._call_api(**http_info)

    def update_database_invoker(self, request):
        http_info = self._update_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_db_user_comment(self, request):
        """修改数据库用户名备注

        修改数据库用户名备注
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbUserComment
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDbUserCommentRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDbUserCommentResponse`
        """
        http_info = self._update_db_user_comment_http_info(request)
        return self._call_api(**http_info)

    def update_db_user_comment_invoker(self, request):
        http_info = self._update_db_user_comment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_user_comment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{user_name}/comment",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbUserCommentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

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

    def allow_db_privilege(self, request):
        """授权数据库帐号

        在指定实例的数据库中, 设置帐号的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowDbPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.AllowDbPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AllowDbPrivilegeResponse`
        """
        http_info = self._allow_db_privilege_http_info(request)
        return self._call_api(**http_info)

    def allow_db_privilege_invoker(self, request):
        http_info = self._allow_db_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_db_privilege_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_privilege",
            "request_type": request.__class__.__name__,
            "response_type": "AllowDbPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def change_proxy_scale(self, request):
        """数据库代理规格变更

        数据库代理实例进行规格变更。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeProxyScale
        :type request: :class:`huaweicloudsdkrds.v3.ChangeProxyScaleRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeProxyScaleResponse`
        """
        http_info = self._change_proxy_scale_http_info(request)
        return self._call_api(**http_info)

    def change_proxy_scale_invoker(self, request):
        http_info = self._change_proxy_scale_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_proxy_scale_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/scale",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeProxyScaleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def change_the_delay_threshold(self, request):
        """修改读写分离阈值

        修改指定实例的读写分离延时阈值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeTheDelayThreshold
        :type request: :class:`huaweicloudsdkrds.v3.ChangeTheDelayThresholdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeTheDelayThresholdResponse`
        """
        http_info = self._change_the_delay_threshold_http_info(request)
        return self._call_api(**http_info)

    def change_the_delay_threshold_invoker(self, request):
        http_info = self._change_the_delay_threshold_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_the_delay_threshold_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/delay-threshold",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeTheDelayThresholdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_postgresql_database(self, request):
        """创建数据库

        在指定实例中创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePostgresqlDatabase
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseResponse`
        """
        http_info = self._create_postgresql_database_http_info(request)
        return self._call_api(**http_info)

    def create_postgresql_database_invoker(self, request):
        http_info = self._create_postgresql_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_postgresql_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostgresqlDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_postgresql_database_schema(self, request):
        """创建数据库SCHEMA

        在指定实例的数据库中, 创建数据库schema。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePostgresqlDatabaseSchema
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseSchemaRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseSchemaResponse`
        """
        http_info = self._create_postgresql_database_schema_http_info(request)
        return self._call_api(**http_info)

    def create_postgresql_database_schema_invoker(self, request):
        http_info = self._create_postgresql_database_schema_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_postgresql_database_schema_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/schema",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostgresqlDatabaseSchemaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_postgresql_db_user(self, request):
        """创建数据库用户

        在指定实例中创建数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePostgresqlDbUser
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDbUserResponse`
        """
        http_info = self._create_postgresql_db_user_http_info(request)
        return self._call_api(**http_info)

    def create_postgresql_db_user_invoker(self, request):
        http_info = self._create_postgresql_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_postgresql_db_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostgresqlDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_postgresql_extension(self, request):
        """创建插件

        在指定数据库上创建插件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePostgresqlExtension
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlExtensionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlExtensionResponse`
        """
        http_info = self._create_postgresql_extension_http_info(request)
        return self._call_api(**http_info)

    def create_postgresql_extension_invoker(self, request):
        http_info = self._create_postgresql_extension_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_postgresql_extension_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/extensions",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePostgresqlExtensionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_postgresql_database(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePostgresqlDatabase
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDatabaseResponse`
        """
        http_info = self._delete_postgresql_database_http_info(request)
        return self._call_api(**http_info)

    def delete_postgresql_database_invoker(self, request):
        http_info = self._delete_postgresql_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_postgresql_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/{db_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePostgresqlDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_postgresql_db_user(self, request):
        """删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePostgresqlDbUser
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDbUserResponse`
        """
        http_info = self._delete_postgresql_db_user_http_info(request)
        return self._call_api(**http_info)

    def delete_postgresql_db_user_invoker(self, request):
        http_info = self._delete_postgresql_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_postgresql_db_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePostgresqlDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_postgresql_extension(self, request):
        """删除插件

        在指定数据库上删除插件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePostgresqlExtension
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlExtensionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlExtensionResponse`
        """
        http_info = self._delete_postgresql_extension_http_info(request)
        return self._call_api(**http_info)

    def delete_postgresql_extension_invoker(self, request):
        http_info = self._delete_postgresql_extension_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_postgresql_extension_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/extensions",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePostgresqlExtensionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_postgresql_database_schemas(self, request):
        """查询数据库SCHEMA列表

        查询指定实例的数据库SCHEMA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlDatabaseSchemas
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabaseSchemasRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabaseSchemasResponse`
        """
        http_info = self._list_postgresql_database_schemas_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_database_schemas_invoker(self, request):
        http_info = self._list_postgresql_database_schemas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_database_schemas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/schema/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlDatabaseSchemasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_postgresql_databases(self, request):
        """查询数据库列表

        查询指定实例中的数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabasesResponse`
        """
        http_info = self._list_postgresql_databases_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_databases_invoker(self, request):
        http_info = self._list_postgresql_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_postgresql_db_user_paginated(self, request):
        """查询数据库用户列表

        在指定实例中查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlDbUserPaginated
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlDbUserPaginatedRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlDbUserPaginatedResponse`
        """
        http_info = self._list_postgresql_db_user_paginated_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_db_user_paginated_invoker(self, request):
        http_info = self._list_postgresql_db_user_paginated_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_db_user_paginated_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlDbUserPaginatedResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_postgresql_extension(self, request):
        """查询插件

        获取指定数据库的插件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresqlExtension
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlExtensionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlExtensionResponse`
        """
        http_info = self._list_postgresql_extension_http_info(request)
        return self._call_api(**http_info)

    def list_postgresql_extension_invoker(self, request):
        http_info = self._list_postgresql_extension_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgresql_extension_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/extensions",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresqlExtensionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def search_query_scale_compute_flavors(self, request):
        """查询数据库代理可变更的规格

        查询数据库代理可变更的规格信息。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQueryScaleComputeFlavors
        :type request: :class:`huaweicloudsdkrds.v3.SearchQueryScaleComputeFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SearchQueryScaleComputeFlavorsResponse`
        """
        http_info = self._search_query_scale_compute_flavors_http_info(request)
        return self._call_api(**http_info)

    def search_query_scale_compute_flavors_invoker(self, request):
        http_info = self._search_query_scale_compute_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_query_scale_compute_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/proxy/scale/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQueryScaleComputeFlavorsResponse"
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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def search_query_scale_flavors(self, request):
        """查询数据库代理可变更的规格

        查询数据库代理可变更的规格信息。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchQueryScaleFlavors
        :type request: :class:`huaweicloudsdkrds.v3.SearchQueryScaleFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SearchQueryScaleFlavorsResponse`
        """
        http_info = self._search_query_scale_flavors_http_info(request)
        return self._call_api(**http_info)

    def search_query_scale_flavors_invoker(self, request):
        http_info = self._search_query_scale_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_query_scale_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/scale/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "SearchQueryScaleFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_database_user_privilege(self, request):
        """设置数据库用户权限

        设置数据库用户权限：只读或可读写。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetDatabaseUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.SetDatabaseUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetDatabaseUserPrivilegeResponse`
        """
        http_info = self._set_database_user_privilege_http_info(request)
        return self._call_api(**http_info)

    def set_database_user_privilege_invoker(self, request):
        http_info = self._set_database_user_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_database_user_privilege_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/user-privilege",
            "request_type": request.__class__.__name__,
            "response_type": "SetDatabaseUserPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def set_postgresql_db_user_pwd(self, request):
        """重置数据库帐号密码

        重置指定数据库帐号的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetPostgresqlDbUserPwd
        :type request: :class:`huaweicloudsdkrds.v3.SetPostgresqlDbUserPwdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetPostgresqlDbUserPwdResponse`
        """
        http_info = self._set_postgresql_db_user_pwd_http_info(request)
        return self._call_api(**http_info)

    def set_postgresql_db_user_pwd_invoker(self, request):
        http_info = self._set_postgresql_db_user_pwd_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_postgresql_db_user_pwd_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/resetpwd",
            "request_type": request.__class__.__name__,
            "response_type": "SetPostgresqlDbUserPwdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_information_about_database_proxy(self, request):
        """查询数据库代理信息

        查询指定实例的数据库代理详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInformationAboutDatabaseProxy
        :type request: :class:`huaweicloudsdkrds.v3.ShowInformationAboutDatabaseProxyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowInformationAboutDatabaseProxyResponse`
        """
        http_info = self._show_information_about_database_proxy_http_info(request)
        return self._call_api(**http_info)

    def show_information_about_database_proxy_invoker(self, request):
        http_info = self._show_information_about_database_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_information_about_database_proxy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInformationAboutDatabaseProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_postgresql_param_value(self, request):
        """获取实例指定参数的值

        获取实例指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPostgresqlParamValue
        :type request: :class:`huaweicloudsdkrds.v3.ShowPostgresqlParamValueRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowPostgresqlParamValueResponse`
        """
        http_info = self._show_postgresql_param_value_http_info(request)
        return self._call_api(**http_info)

    def show_postgresql_param_value_invoker(self, request):
        http_info = self._show_postgresql_param_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_postgresql_param_value_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/parameter/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPostgresqlParamValueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_database_proxy(self, request):
        """开启数据库代理

        为指定实例开启数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDatabaseProxy
        :type request: :class:`huaweicloudsdkrds.v3.StartDatabaseProxyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartDatabaseProxyResponse`
        """
        http_info = self._start_database_proxy_http_info(request)
        return self._call_api(**http_info)

    def start_database_proxy_invoker(self, request):
        http_info = self._start_database_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_database_proxy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "StartDatabaseProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def stop_database_proxy(self, request):
        """关闭数据库代理

        为指定实例关闭数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopDatabaseProxy
        :type request: :class:`huaweicloudsdkrds.v3.StopDatabaseProxyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StopDatabaseProxyResponse`
        """
        http_info = self._stop_database_proxy_http_info(request)
        return self._call_api(**http_info)

    def stop_database_proxy_invoker(self, request):
        http_info = self._stop_database_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_database_proxy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "StopDatabaseProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_db_user_privilege(self, request):
        """update_db_user_privilege

        数据库帐号授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDbUserPrivilegeResponse`
        """
        http_info = self._update_db_user_privilege_http_info(request)
        return self._call_api(**http_info)

    def update_db_user_privilege_invoker(self, request):
        http_info = self._update_db_user_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_user_privilege_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-user-privilege",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbUserPrivilegeResponse"
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

    def update_postgresql_database(self, request):
        """修改指定实例的数据库备注

        修改指定实例中的数据库备注。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePostgresqlDatabase
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDatabaseResponse`
        """
        http_info = self._update_postgresql_database_http_info(request)
        return self._call_api(**http_info)

    def update_postgresql_database_invoker(self, request):
        http_info = self._update_postgresql_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_postgresql_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePostgresqlDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_postgresql_db_user_comment(self, request):
        """修改数据库用户名备注

        修改数据库用户名备注
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePostgresqlDbUserComment
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDbUserCommentRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDbUserCommentResponse`
        """
        http_info = self._update_postgresql_db_user_comment_http_info(request)
        return self._call_api(**http_info)

    def update_postgresql_db_user_comment_invoker(self, request):
        http_info = self._update_postgresql_db_user_comment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_postgresql_db_user_comment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{user_name}/comment",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePostgresqlDbUserCommentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

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

    def update_postgresql_parameter_value(self, request):
        """修改实例指定参数的值

        修改实例指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePostgresqlParameterValue
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlParameterValueRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlParameterValueResponse`
        """
        http_info = self._update_postgresql_parameter_value_http_info(request)
        return self._call_api(**http_info)

    def update_postgresql_parameter_value_invoker(self, request):
        http_info = self._update_postgresql_parameter_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_postgresql_parameter_value_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/parameter/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePostgresqlParameterValueResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def update_read_weight(self, request):
        """修改读写分离权重

        修改指定实例的读写分离权重。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateReadWeight
        :type request: :class:`huaweicloudsdkrds.v3.UpdateReadWeightRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateReadWeightResponse`
        """
        http_info = self._update_read_weight_http_info(request)
        return self._call_api(**http_info)

    def update_read_weight_invoker(self, request):
        http_info = self._update_read_weight_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_read_weight_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/weight",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReadWeightResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def allow_sqlserver_db_user_privilege(self, request):
        """授权数据库帐号

        授权数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AllowSqlserverDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.AllowSqlserverDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AllowSqlserverDbUserPrivilegeResponse`
        """
        http_info = self._allow_sqlserver_db_user_privilege_http_info(request)
        return self._call_api(**http_info)

    def allow_sqlserver_db_user_privilege_invoker(self, request):
        http_info = self._allow_sqlserver_db_user_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _allow_sqlserver_db_user_privilege_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_privilege",
            "request_type": request.__class__.__name__,
            "response_type": "AllowSqlserverDbUserPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def batch_add_msdtcs(self, request):
        """添加MSDTC

        添加MSDTC相关主机host地址
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddMsdtcs
        :type request: :class:`huaweicloudsdkrds.v3.BatchAddMsdtcsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchAddMsdtcsResponse`
        """
        http_info = self._batch_add_msdtcs_http_info(request)
        return self._call_api(**http_info)

    def batch_add_msdtcs_invoker(self, request):
        http_info = self._batch_add_msdtcs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_msdtcs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/msdtc/host",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddMsdtcsResponse"
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

    def create_sqlserver_database(self, request):
        """创建数据库

        创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlserverDatabase
        :type request: :class:`huaweicloudsdkrds.v3.CreateSqlserverDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSqlserverDatabaseResponse`
        """
        http_info = self._create_sqlserver_database_http_info(request)
        return self._call_api(**http_info)

    def create_sqlserver_database_invoker(self, request):
        http_info = self._create_sqlserver_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sqlserver_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlserverDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def create_sqlserver_db_user(self, request):
        """创建数据库用户

        创建数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlserverDbUser
        :type request: :class:`huaweicloudsdkrds.v3.CreateSqlserverDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSqlserverDbUserResponse`
        """
        http_info = self._create_sqlserver_db_user_http_info(request)
        return self._call_api(**http_info)

    def create_sqlserver_db_user_invoker(self, request):
        http_info = self._create_sqlserver_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sqlserver_db_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlserverDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_sqlserver_database(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlserverDatabase
        :type request: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseResponse`
        """
        http_info = self._delete_sqlserver_database_http_info(request)
        return self._call_api(**http_info)

    def delete_sqlserver_database_invoker(self, request):
        http_info = self._delete_sqlserver_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sqlserver_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/{db_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlserverDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_sqlserver_database_ex(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlserverDatabaseEx
        :type request: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseExRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseExResponse`
        """
        http_info = self._delete_sqlserver_database_ex_http_info(request)
        return self._call_api(**http_info)

    def delete_sqlserver_database_ex_invoker(self, request):
        http_info = self._delete_sqlserver_database_ex_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sqlserver_database_ex_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/database/{db_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlserverDatabaseExResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_name' in local_var_params:
            path_params['db_name'] = local_var_params['db_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_sqlserver_db_user(self, request):
        """删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlserverDbUser
        :type request: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDbUserResponse`
        """
        http_info = self._delete_sqlserver_db_user_http_info(request)
        return self._call_api(**http_info)

    def delete_sqlserver_db_user_invoker(self, request):
        http_info = self._delete_sqlserver_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sqlserver_db_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlserverDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'user_name' in local_var_params:
            path_params['user_name'] = local_var_params['user_name']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_authorized_sqlserver_db_users(self, request):
        """查询指定数据库的已授权用户

        查询指定数据库的已授权用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuthorizedSqlserverDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListAuthorizedSqlserverDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuthorizedSqlserverDbUsersResponse`
        """
        http_info = self._list_authorized_sqlserver_db_users_http_info(request)
        return self._call_api(**http_info)

    def list_authorized_sqlserver_db_users_invoker(self, request):
        http_info = self._list_authorized_sqlserver_db_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_authorized_sqlserver_db_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/db_user",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuthorizedSqlserverDbUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_name' in local_var_params:
            query_params.append(('db-name', local_var_params['db_name']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_msdtc_hosts(self, request):
        """查询MSDTC的hosts信息

        查询MSDTC的hosts信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMsdtcHosts
        :type request: :class:`huaweicloudsdkrds.v3.ListMsdtcHostsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListMsdtcHostsResponse`
        """
        http_info = self._list_msdtc_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_msdtc_hosts_invoker(self, request):
        http_info = self._list_msdtc_hosts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_msdtc_hosts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/msdtc/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListMsdtcHostsResponse"
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

    def list_sqlserver_databases(self, request):
        """查询数据库列表

        查询数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlserverDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListSqlserverDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSqlserverDatabasesResponse`
        """
        http_info = self._list_sqlserver_databases_http_info(request)
        return self._call_api(**http_info)

    def list_sqlserver_databases_invoker(self, request):
        http_info = self._list_sqlserver_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sqlserver_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlserverDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'db_name' in local_var_params:
            query_params.append(('db-name', local_var_params['db_name']))
        if 'recover_model' in local_var_params:
            query_params.append(('recover_model', local_var_params['recover_model']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_sqlserver_db_users(self, request):
        """查询数据库用户列表

        查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlserverDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListSqlserverDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSqlserverDbUsersResponse`
        """
        http_info = self._list_sqlserver_db_users_http_info(request)
        return self._call_api(**http_info)

    def list_sqlserver_db_users_invoker(self, request):
        http_info = self._list_sqlserver_db_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sqlserver_db_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_user/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlserverDbUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def modify_collation(self, request):
        """修改实例字符集

        修改实例字符集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyCollation
        :type request: :class:`huaweicloudsdkrds.v3.ModifyCollationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ModifyCollationResponse`
        """
        http_info = self._modify_collation_http_info(request)
        return self._call_api(**http_info)

    def modify_collation_invoker(self, request):
        http_info = self._modify_collation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_collation_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/collations",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyCollationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def revoke_sqlserver_db_user_privilege(self, request):
        """解除数据库帐号权限

        解除数据库帐号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RevokeSqlserverDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.RevokeSqlserverDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RevokeSqlserverDbUserPrivilegeResponse`
        """
        http_info = self._revoke_sqlserver_db_user_privilege_http_info(request)
        return self._call_api(**http_info)

    def revoke_sqlserver_db_user_privilege_invoker(self, request):
        http_info = self._revoke_sqlserver_db_user_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _revoke_sqlserver_db_user_privilege_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db_privilege",
            "request_type": request.__class__.__name__,
            "response_type": "RevokeSqlserverDbUserPrivilegeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

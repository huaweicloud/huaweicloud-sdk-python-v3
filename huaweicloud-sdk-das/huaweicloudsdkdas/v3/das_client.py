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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdas'")


class DasClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdas.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DasClient":
                raise TypeError("client type error, support client type is DasClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def cancel_share_connections(self, request):
        r"""删除共享链接

        删除共享链接，
        用于用户删除共享链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelShareConnections
        :type request: :class:`huaweicloudsdkdas.v3.CancelShareConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CancelShareConnectionsResponse`
        """
        http_info = self._cancel_share_connections_http_info(request)
        return self._call_api(**http_info)

    def cancel_share_connections_invoker(self, request):
        http_info = self._cancel_share_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_share_connections_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/connections/share",
            "request_type": request.__class__.__name__,
            "response_type": "CancelShareConnectionsResponse"
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

    def create_instance_connection(self, request):
        r"""创建实例连接

        创建实例连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceConnection
        :type request: :class:`huaweicloudsdkdas.v3.CreateInstanceConnectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateInstanceConnectionResponse`
        """
        http_info = self._create_instance_connection_http_info(request)
        return self._call_api(**http_info)

    def create_instance_connection_invoker(self, request):
        http_info = self._create_instance_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/create-connection",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceConnectionResponse"
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

    def create_share_connections(self, request):
        r"""设置共享链接

        设置共享链接，
        用于用户添加共享链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateShareConnections
        :type request: :class:`huaweicloudsdkdas.v3.CreateShareConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateShareConnectionsResponse`
        """
        http_info = self._create_share_connections_http_info(request)
        return self._call_api(**http_info)

    def create_share_connections_invoker(self, request):
        http_info = self._create_share_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_share_connections_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/share",
            "request_type": request.__class__.__name__,
            "response_type": "CreateShareConnectionsResponse"
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

    def execute_export_task(self, request):
        r"""立即执行导出任务

        立即执行导出任务，
        用于用户立即执行导出任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteExportTask
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteExportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteExportTaskResponse`
        """
        http_info = self._execute_export_task_http_info(request)
        return self._call_api(**http_info)

    def execute_export_task_invoker(self, request):
        http_info = self._execute_export_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_export_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/export-tasks/{job_id}/execute",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteExportTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def execute_import_task(self, request):
        r"""立即执行导入任务

        立即执行导入任务，
        用于用户立即执行导入任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteImportTask
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteImportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteImportTaskResponse`
        """
        http_info = self._execute_import_task_http_info(request)
        return self._call_api(**http_info)

    def execute_import_task_invoker(self, request):
        http_info = self._execute_import_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_import_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/import-tasks/{job_id}/execute",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteImportTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def list_connections(self, request):
        r"""查询实例连接列表

        查询实例连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnections
        :type request: :class:`huaweicloudsdkdas.v3.ListConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListConnectionsResponse`
        """
        http_info = self._list_connections_http_info(request)
        return self._call_api(**http_info)

    def list_connections_invoker(self, request):
        http_info = self._list_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/list-connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'condition' in local_var_params:
            query_params.append(('condition', local_var_params['condition']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'connection_type' in local_var_params:
            query_params.append(('connection_type', local_var_params['connection_type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_api_versions(self, request):
        r"""查询API版本列表

        查询API版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdas.v3.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/das",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
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
        r"""查询指定的API版本信息

        查询指定的API版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkdas.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowApiVersionResponse`
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
            "resource_path": "/das/{version}",
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

    def add(self, request):
        r"""创建全量SQL明细解析任务

        Add
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Add
        :type request: :class:`huaweicloudsdkdas.v3.AddRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddResponse`
        """
        http_info = self._add_http_info(request)
        return self._call_api(**http_info)

    def add_invoker(self, request):
        http_info = self._add_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/task/add",
            "request_type": request.__class__.__name__,
            "response_type": "AddResponse"
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

    def add_tasks_new(self, request):
        r"""创建全量SQL明细解析任务

        创建全量SQL明细解析任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddTasksNew
        :type request: :class:`huaweicloudsdkdas.v3.AddTasksNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddTasksNewResponse`
        """
        http_info = self._add_tasks_new_http_info(request)
        return self._call_api(**http_info)

    def add_tasks_new_invoker(self, request):
        http_info = self._add_tasks_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_tasks_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/task/add-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "AddTasksNewResponse"
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

    def batch_add_full_sql_tasks(self, request):
        r"""批量创建全量SQL明细解析任务

        批量创建全量SQL明细解析任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddFullSqlTasks
        :type request: :class:`huaweicloudsdkdas.v3.BatchAddFullSqlTasksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.BatchAddFullSqlTasksResponse`
        """
        http_info = self._batch_add_full_sql_tasks_http_info(request)
        return self._call_api(**http_info)

    def batch_add_full_sql_tasks_invoker(self, request):
        http_info = self._batch_add_full_sql_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_full_sql_tasks_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/task/batch-add",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddFullSqlTasksResponse"
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

    def batch_set_sql_limiting_switch(self, request):
        r"""批量设置SQL限流开关

        Sql Limitbatch Set Switch New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetSqlLimitingSwitch
        :type request: :class:`huaweicloudsdkdas.v3.BatchSetSqlLimitingSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.BatchSetSqlLimitingSwitchResponse`
        """
        http_info = self._batch_set_sql_limiting_switch_http_info(request)
        return self._call_api(**http_info)

    def batch_set_sql_limiting_switch_invoker(self, request):
        http_info = self._batch_set_sql_limiting_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_set_sql_limiting_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/sql-limiting/batch-set-switch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetSqlLimitingSwitchResponse"
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

    def batch_set_sql_switch_new(self, request):
        r"""批量设置SQL开关

        批量设置SQL开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSetSqlSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.BatchSetSqlSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.BatchSetSqlSwitchNewResponse`
        """
        http_info = self._batch_set_sql_switch_new_http_info(request)
        return self._call_api(**http_info)

    def batch_set_sql_switch_new_invoker(self, request):
        http_info = self._batch_set_sql_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_set_sql_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/batch-set-sql-switch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetSqlSwitchNewResponse"
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

    def cancel_connection_process(self, request):
        r"""Kill进程

        Kill进程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelConnectionProcess
        :type request: :class:`huaweicloudsdkdas.v3.CancelConnectionProcessRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CancelConnectionProcessResponse`
        """
        http_info = self._cancel_connection_process_http_info(request)
        return self._call_api(**http_info)

    def cancel_connection_process_invoker(self, request):
        http_info = self._cancel_connection_process_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_connection_process_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/kill-process",
            "request_type": request.__class__.__name__,
            "response_type": "CancelConnectionProcessResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def cancel_instance_process(self, request):
        r"""删除会话

        删除会话
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelInstanceProcess
        :type request: :class:`huaweicloudsdkdas.v3.CancelInstanceProcessRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CancelInstanceProcessResponse`
        """
        http_info = self._cancel_instance_process_http_info(request)
        return self._call_api(**http_info)

    def cancel_instance_process_invoker(self, request):
        http_info = self._cancel_instance_process_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_instance_process_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/kill-process",
            "request_type": request.__class__.__name__,
            "response_type": "CancelInstanceProcessResponse"
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

    def change_kill_task_switch(self, request):
        r"""设置自治限流开关

        Change Kill Task Switch
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeKillTaskSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ChangeKillTaskSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeKillTaskSwitchResponse`
        """
        http_info = self._change_kill_task_switch_http_info(request)
        return self._call_api(**http_info)

    def change_kill_task_switch_invoker(self, request):
        http_info = self._change_kill_task_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_kill_task_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/set-kill-process-task-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeKillTaskSwitchResponse"
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

    def change_quota_new(self, request):
        r"""修改配额

        修改配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeQuotaNew
        :type request: :class:`huaweicloudsdkdas.v3.ChangeQuotaNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeQuotaNewResponse`
        """
        http_info = self._change_quota_new_http_info(request)
        return self._call_api(**http_info)

    def change_quota_new_invoker(self, request):
        http_info = self._change_quota_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_quota_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clouddba/change-quota",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeQuotaNewResponse"
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

    def check_health_report_task(self, request):
        r"""检查是否有健康报告任务

        检查是否有健康报告任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckHealthReportTask
        :type request: :class:`huaweicloudsdkdas.v3.CheckHealthReportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CheckHealthReportTaskResponse`
        """
        http_info = self._check_health_report_task_http_info(request)
        return self._call_api(**http_info)

    def check_health_report_task_invoker(self, request):
        http_info = self._check_health_report_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_health_report_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/has-health-report-task",
            "request_type": request.__class__.__name__,
            "response_type": "CheckHealthReportTaskResponse"
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

    def compare_slow_log_templates(self, request):
        r"""对比慢日志模板列表

        对比慢日志模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareSlowLogTemplates
        :type request: :class:`huaweicloudsdkdas.v3.CompareSlowLogTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CompareSlowLogTemplatesResponse`
        """
        http_info = self._compare_slow_log_templates_http_info(request)
        return self._call_api(**http_info)

    def compare_slow_log_templates_invoker(self, request):
        http_info = self._compare_slow_log_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _compare_slow_log_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/contrast-slow-log-tpl-list",
            "request_type": request.__class__.__name__,
            "response_type": "CompareSlowLogTemplatesResponse"
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

    def create_binlog_task(self, request):
        r"""创建binlog解析任务

        创建binlog解析任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBinlogTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateBinlogTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateBinlogTaskResponse`
        """
        http_info = self._create_binlog_task_http_info(request)
        return self._call_api(**http_info)

    def create_binlog_task_invoker(self, request):
        http_info = self._create_binlog_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_binlog_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/create-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBinlogTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def create_connection(self, request):
        r"""创建实例连接

        创建实例连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnection
        :type request: :class:`huaweicloudsdkdas.v3.CreateConnectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateConnectionResponse`
        """
        http_info = self._create_connection_http_info(request)
        return self._call_api(**http_info)

    def create_connection_invoker(self, request):
        http_info = self._create_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionResponse"
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

    def create_dbs_connection(self, request):
        r"""DBS连接

        DBS连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbsConnection
        :type request: :class:`huaweicloudsdkdas.v3.CreateDbsConnectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateDbsConnectionResponse`
        """
        http_info = self._create_dbs_connection_http_info(request)
        return self._call_api(**http_info)

    def create_dbs_connection_invoker(self, request):
        http_info = self._create_dbs_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_dbs_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dbs-connection",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbsConnectionResponse"
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

    def create_full_sql_bucket(self, request):
        r"""创建全量SQL桶

        创建全量SQL桶
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFullSqlBucket
        :type request: :class:`huaweicloudsdkdas.v3.CreateFullSqlBucketRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateFullSqlBucketResponse`
        """
        http_info = self._create_full_sql_bucket_http_info(request)
        return self._call_api(**http_info)

    def create_full_sql_bucket_invoker(self, request):
        http_info = self._create_full_sql_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_full_sql_bucket_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/create-bucket",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFullSqlBucketResponse"
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

    def create_index_usage_export_task_new(self, request):
        r"""创建索引使用导出任务

        创建索引使用导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndexUsageExportTaskNew
        :type request: :class:`huaweicloudsdkdas.v3.CreateIndexUsageExportTaskNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateIndexUsageExportTaskNewResponse`
        """
        http_info = self._create_index_usage_export_task_new_http_info(request)
        return self._call_api(**http_info)

    def create_index_usage_export_task_new_invoker(self, request):
        http_info = self._create_index_usage_export_task_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_index_usage_export_task_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/create-index-usage-export-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIndexUsageExportTaskNewResponse"
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

    def create_instance_health_report_task_new(self, request):
        r"""创建实例健康报告任务

        创建实例健康报告任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstanceHealthReportTaskNew
        :type request: :class:`huaweicloudsdkdas.v3.CreateInstanceHealthReportTaskNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateInstanceHealthReportTaskNewResponse`
        """
        http_info = self._create_instance_health_report_task_new_http_info(request)
        return self._call_api(**http_info)

    def create_instance_health_report_task_new_invoker(self, request):
        http_info = self._create_instance_health_report_task_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instance_health_report_task_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/create-instance-health-report-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstanceHealthReportTaskNewResponse"
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

    def create_kill_task(self, request):
        r"""添加自动kill会话任务

        Create Kill Task
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateKillTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateKillTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateKillTaskResponse`
        """
        http_info = self._create_kill_task_http_info(request)
        return self._call_api(**http_info)

    def create_kill_task_invoker(self, request):
        http_info = self._create_kill_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_kill_task_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/add-kill-process-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKillTaskResponse"
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

    def create_missing_index_export_task_new(self, request):
        r"""创建缺失索引导出任务

        创建缺失索引导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMissingIndexExportTaskNew
        :type request: :class:`huaweicloudsdkdas.v3.CreateMissingIndexExportTaskNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateMissingIndexExportTaskNewResponse`
        """
        http_info = self._create_missing_index_export_task_new_http_info(request)
        return self._call_api(**http_info)

    def create_missing_index_export_task_new_invoker(self, request):
        http_info = self._create_missing_index_export_task_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_missing_index_export_task_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/create-missing-index-export-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMissingIndexExportTaskNewResponse"
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

    def create_obs_bucket(self, request):
        r"""创建OBS桶

        Create Obs Bucket
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateObsBucket
        :type request: :class:`huaweicloudsdkdas.v3.CreateObsBucketRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateObsBucketResponse`
        """
        http_info = self._create_obs_bucket_http_info(request)
        return self._call_api(**http_info)

    def create_obs_bucket_invoker(self, request):
        http_info = self._create_obs_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_obs_bucket_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/obs/bucket",
            "request_type": request.__class__.__name__,
            "response_type": "CreateObsBucketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def create_shared_connection(self, request):
        r"""创建共享链接

        创建共享链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSharedConnection
        :type request: :class:`huaweicloudsdkdas.v3.CreateSharedConnectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSharedConnectionResponse`
        """
        http_info = self._create_shared_connection_http_info(request)
        return self._call_api(**http_info)

    def create_shared_connection_invoker(self, request):
        http_info = self._create_shared_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_shared_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/connections/share",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSharedConnectionResponse"
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

    def create_slow_log_export_task_new(self, request):
        r"""创建慢日志导出任务

        创建慢日志导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSlowLogExportTaskNew
        :type request: :class:`huaweicloudsdkdas.v3.CreateSlowLogExportTaskNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSlowLogExportTaskNewResponse`
        """
        http_info = self._create_slow_log_export_task_new_http_info(request)
        return self._call_api(**http_info)

    def create_slow_log_export_task_new_invoker(self, request):
        http_info = self._create_slow_log_export_task_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_slow_log_export_task_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/create-slow-log-export-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSlowLogExportTaskNewResponse"
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

    def create_wdr_report(self, request):
        r"""触发WDR

        触发WDR
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWdrReport
        :type request: :class:`huaweicloudsdkdas.v3.CreateWdrReportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateWdrReportResponse`
        """
        http_info = self._create_wdr_report_http_info(request)
        return self._call_api(**http_info)

    def create_wdr_report_invoker(self, request):
        http_info = self._create_wdr_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_wdr_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/wdr/trigger-wdr",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWdrReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_all_sessions(self, request):
        r"""一键kill所有会话

        Delete All Sessions
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAllSessions
        :type request: :class:`huaweicloudsdkdas.v3.DeleteAllSessionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteAllSessionsResponse`
        """
        http_info = self._delete_all_sessions_http_info(request)
        return self._call_api(**http_info)

    def delete_all_sessions_invoker(self, request):
        http_info = self._delete_all_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_all_sessions_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/kill-all-session",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAllSessionsResponse"
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

    def delete_binlog_task(self, request):
        r"""删除binlog任务

        删除binlog任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBinlogTask
        :type request: :class:`huaweicloudsdkdas.v3.DeleteBinlogTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteBinlogTaskResponse`
        """
        http_info = self._delete_binlog_task_http_info(request)
        return self._call_api(**http_info)

    def delete_binlog_task_invoker(self, request):
        http_info = self._delete_binlog_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_binlog_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/delete-task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBinlogTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def delete_db_obj_new(self, request):
        r"""删除数据库对象

        删除数据库对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbObjNew
        :type request: :class:`huaweicloudsdkdas.v3.DeleteDbObjNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteDbObjNewResponse`
        """
        http_info = self._delete_db_obj_new_http_info(request)
        return self._call_api(**http_info)

    def delete_db_obj_new_invoker(self, request):
        http_info = self._delete_db_obj_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_db_obj_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/delete-db-obj",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbObjNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'schema_name' in local_var_params:
            query_params.append(('schema_name', local_var_params['schema_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'obj_name' in local_var_params:
            query_params.append(('obj_name', local_var_params['obj_name']))
        if 'obj_id' in local_var_params:
            query_params.append(('obj_id', local_var_params['obj_id']))
        if 'object_sub_type' in local_var_params:
            query_params.append(('object_sub_type', local_var_params['object_sub_type']))
        if 'obj_type' in local_var_params:
            query_params.append(('obj_type', local_var_params['obj_type']))

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

    def delete_export_task_new(self, request):
        r"""删除binlog导出任务

        删除binlog导出任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExportTaskNew
        :type request: :class:`huaweicloudsdkdas.v3.DeleteExportTaskNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteExportTaskNewResponse`
        """
        http_info = self._delete_export_task_new_http_info(request)
        return self._call_api(**http_info)

    def delete_export_task_new_invoker(self, request):
        http_info = self._delete_export_task_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_export_task_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/delete-export-task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExportTaskNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_export_task_obs_file_new(self, request):
        r"""删除导出任务OBS文件

        删除导出任务OBS文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExportTaskObsFileNew
        :type request: :class:`huaweicloudsdkdas.v3.DeleteExportTaskObsFileNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteExportTaskObsFileNewResponse`
        """
        http_info = self._delete_export_task_obs_file_new_http_info(request)
        return self._call_api(**http_info)

    def delete_export_task_obs_file_new_invoker(self, request):
        http_info = self._delete_export_task_obs_file_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_export_task_obs_file_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/delete-export-task-obs-file",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExportTaskObsFileNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

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

    def delete_full_sql_export_task_obs_file(self, request):
        r"""删除全量SQL导出任务OBS文件

        删除全量SQL导出任务OBS文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFullSqlExportTaskObsFile
        :type request: :class:`huaweicloudsdkdas.v3.DeleteFullSqlExportTaskObsFileRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteFullSqlExportTaskObsFileResponse`
        """
        http_info = self._delete_full_sql_export_task_obs_file_http_info(request)
        return self._call_api(**http_info)

    def delete_full_sql_export_task_obs_file_invoker(self, request):
        http_info = self._delete_full_sql_export_task_obs_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_full_sql_export_task_obs_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/delete-export-task-obs-file",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFullSqlExportTaskObsFileResponse"
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

    def delete_sql_limiting_record(self, request):
        r"""删除SQL限流记录

        删除SQL限流记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlLimitingRecord
        :type request: :class:`huaweicloudsdkdas.v3.DeleteSqlLimitingRecordRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteSqlLimitingRecordResponse`
        """
        http_info = self._delete_sql_limiting_record_http_info(request)
        return self._call_api(**http_info)

    def delete_sql_limiting_record_invoker(self, request):
        http_info = self._delete_sql_limiting_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sql_limiting_record_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/del-sql-limiting-record",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlLimitingRecordResponse"
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

    def enable_quota(self, request):
        r"""开通配额

        开通配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for EnableQuota
        :type request: :class:`huaweicloudsdkdas.v3.EnableQuotaRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.EnableQuotaResponse`
        """
        http_info = self._enable_quota_http_info(request)
        return self._call_api(**http_info)

    def enable_quota_invoker(self, request):
        http_info = self._enable_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _enable_quota_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clouddba/open-quota",
            "request_type": request.__class__.__name__,
            "response_type": "EnableQuotaResponse"
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

    def execute_format_sql(self, request):
        r"""格式化SQL

        格式化SQL
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteFormatSql
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteFormatSqlRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteFormatSqlResponse`
        """
        http_info = self._execute_format_sql_http_info(request)
        return self._call_api(**http_info)

    def execute_format_sql_invoker(self, request):
        http_info = self._execute_format_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_format_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/format-sql",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteFormatSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def execute_login_connection_new(self, request):
        r"""登录操作

        登录操作
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteLoginConnectionNew
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteLoginConnectionNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteLoginConnectionNewResponse`
        """
        http_info = self._execute_login_connection_new_http_info(request)
        return self._call_api(**http_info)

    def execute_login_connection_new_invoker(self, request):
        http_info = self._execute_login_connection_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_login_connection_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/login-actions",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteLoginConnectionNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def execute_split_sql(self, request):
        r"""拆分SQL

        拆分SQL
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteSplitSql
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteSplitSqlRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteSplitSqlResponse`
        """
        http_info = self._execute_split_sql_http_info(request)
        return self._call_api(**http_info)

    def execute_split_sql_invoker(self, request):
        http_info = self._execute_split_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_split_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/split-sql",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteSplitSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def execute_test_connection_new(self, request):
        r"""测试数据库实例连接

        测试数据库实例连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteTestConnectionNew
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteTestConnectionNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteTestConnectionNewResponse`
        """
        http_info = self._execute_test_connection_new_http_info(request)
        return self._call_api(**http_info)

    def execute_test_connection_new_invoker(self, request):
        http_info = self._execute_test_connection_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_test_connection_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/test-connection",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteTestConnectionNewResponse"
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

    def execute_tuning(self, request):
        r"""执行调优

        执行调优
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteTuning
        :type request: :class:`huaweicloudsdkdas.v3.ExecuteTuningRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExecuteTuningResponse`
        """
        http_info = self._execute_tuning_http_info(request)
        return self._call_api(**http_info)

    def execute_tuning_invoker(self, request):
        http_info = self._execute_tuning_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_tuning_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/tuning/exe-tuning",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteTuningResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def export_binlog(self, request):
        r"""导出binlog解析结果

        导出binlog解析结果到OBS桶
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportBinlog
        :type request: :class:`huaweicloudsdkdas.v3.ExportBinlogRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportBinlogResponse`
        """
        http_info = self._export_binlog_http_info(request)
        return self._call_api(**http_info)

    def export_binlog_invoker(self, request):
        http_info = self._export_binlog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_binlog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportBinlogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def export_full_sql(self, request):
        r"""创建导出全量SQL任务

        Console Full Sql Export
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportFullSql
        :type request: :class:`huaweicloudsdkdas.v3.ExportFullSqlRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportFullSqlResponse`
        """
        http_info = self._export_full_sql_http_info(request)
        return self._call_api(**http_info)

    def export_full_sql_invoker(self, request):
        http_info = self._export_full_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_full_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportFullSqlResponse"
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

    def export_instance_list_new(self, request):
        r"""导出实例列表

        导出实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportInstanceListNew
        :type request: :class:`huaweicloudsdkdas.v3.ExportInstanceListNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportInstanceListNewResponse`
        """
        http_info = self._export_instance_list_new_http_info(request)
        return self._call_api(**http_info)

    def export_instance_list_new_invoker(self, request):
        http_info = self._export_instance_list_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_instance_list_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/export-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "ExportInstanceListNewResponse"
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

    def import_export_obs_objects(self, request):
        r"""获取OBS对象列表

        获取OBS对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportExportObsObjects
        :type request: :class:`huaweicloudsdkdas.v3.ImportExportObsObjectsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ImportExportObsObjectsResponse`
        """
        http_info = self._import_export_obs_objects_http_info(request)
        return self._call_api(**http_info)

    def import_export_obs_objects_invoker(self, request):
        http_info = self._import_export_obs_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_export_obs_objects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/obs/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ImportExportObsObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'bucket_name' in local_var_params:
            query_params.append(('bucket_name', local_var_params['bucket_name']))
        if 'max_keys' in local_var_params:
            query_params.append(('max_keys', local_var_params['max_keys']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))

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

    def invoke_slow_log_archive(self, request):
        r"""触发慢日志归档

        触发慢日志归档
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InvokeSlowLogArchive
        :type request: :class:`huaweicloudsdkdas.v3.InvokeSlowLogArchiveRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.InvokeSlowLogArchiveResponse`
        """
        http_info = self._invoke_slow_log_archive_http_info(request)
        return self._call_api(**http_info)

    def invoke_slow_log_archive_invoker(self, request):
        http_info = self._invoke_slow_log_archive_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invoke_slow_log_archive_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/trigger-slow-log-archive",
            "request_type": request.__class__.__name__,
            "response_type": "InvokeSlowLogArchiveResponse"
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

    def invoke_wdr_report(self, request):
        r"""获取WDR数据

        获取WDR数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InvokeWdrReport
        :type request: :class:`huaweicloudsdkdas.v3.InvokeWdrReportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.InvokeWdrReportResponse`
        """
        http_info = self._invoke_wdr_report_http_info(request)
        return self._call_api(**http_info)

    def invoke_wdr_report_invoker(self, request):
        http_info = self._invoke_wdr_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invoke_wdr_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/wdr/fetch-wdr",
            "request_type": request.__class__.__name__,
            "response_type": "InvokeWdrReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def list_all_type_instances(self, request):
        r"""查询所有类型实例列表

        查询所有类型实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllTypeInstances
        :type request: :class:`huaweicloudsdkdas.v3.ListAllTypeInstancesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListAllTypeInstancesResponse`
        """
        http_info = self._list_all_type_instances_http_info(request)
        return self._call_api(**http_info)

    def list_all_type_instances_invoker(self, request):
        http_info = self._list_all_type_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_type_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/all-type-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllTypeInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
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

    def list_binlog_exports(self, request):
        r"""导出binlog任务列表

        导出binlog任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBinlogExports
        :type request: :class:`huaweicloudsdkdas.v3.ListBinlogExportsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListBinlogExportsResponse`
        """
        http_info = self._list_binlog_exports_http_info(request)
        return self._call_api(**http_info)

    def list_binlog_exports_invoker(self, request):
        http_info = self._list_binlog_exports_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_binlog_exports_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/export-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBinlogExportsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_binlog_files(self, request):
        r"""查询binlog文件列表

        查询binlog文件列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBinlogFiles
        :type request: :class:`huaweicloudsdkdas.v3.ListBinlogFilesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListBinlogFilesResponse`
        """
        http_info = self._list_binlog_files_http_info(request)
        return self._call_api(**http_info)

    def list_binlog_files_invoker(self, request):
        http_info = self._list_binlog_files_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_binlog_files_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/list-file",
            "request_type": request.__class__.__name__,
            "response_type": "ListBinlogFilesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def list_bucket_name(self, request):
        r"""获取OBS桶列表

        获取全量SQL导出使用的OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBucketName
        :type request: :class:`huaweicloudsdkdas.v3.ListBucketNameRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListBucketNameResponse`
        """
        http_info = self._list_bucket_name_http_info(request)
        return self._call_api(**http_info)

    def list_bucket_name_invoker(self, request):
        http_info = self._list_bucket_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_bucket_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/get-bucket-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListBucketNameResponse"
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

    def list_connection(self, request):
        r"""查询实例连接列表

        查询实例连接列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnection
        :type request: :class:`huaweicloudsdkdas.v3.ListConnectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListConnectionResponse`
        """
        http_info = self._list_connection_http_info(request)
        return self._call_api(**http_info)

    def list_connection_invoker(self, request):
        http_info = self._list_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'condition' in local_var_params:
            query_params.append(('condition', local_var_params['condition']))
        if 'perpage' in local_var_params:
            query_params.append(('perpage', local_var_params['perpage']))
        if 'curpage' in local_var_params:
            query_params.append(('curpage', local_var_params['curpage']))
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'connection_type' in local_var_params:
            query_params.append(('connection_type', local_var_params['connection_type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_connection_processes(self, request):
        r"""查询实例会话

        查询实例会话
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnectionProcesses
        :type request: :class:`huaweicloudsdkdas.v3.ListConnectionProcessesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListConnectionProcessesResponse`
        """
        http_info = self._list_connection_processes_http_info(request)
        return self._call_api(**http_info)

    def list_connection_processes_invoker(self, request):
        http_info = self._list_connection_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_connection_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/query-process-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'host' in local_var_params:
            query_params.append(('host', local_var_params['host']))
        if 'db' in local_var_params:
            query_params.append(('db', local_var_params['db']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'command' in local_var_params:
            query_params.append(('command', local_var_params['command']))
        if 'keywords' in local_var_params:
            query_params.append(('keywords', local_var_params['keywords']))
        if 'show_all' in local_var_params:
            query_params.append(('show_all', local_var_params['show_all']))
        if 'show_no_pid' in local_var_params:
            query_params.append(('show_no_pid', local_var_params['show_no_pid']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_role' in local_var_params:
            query_params.append(('node_role', local_var_params['node_role']))
        if 'hide_sys' in local_var_params:
            query_params.append(('hide_sys', local_var_params['hide_sys']))

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

    def list_database_objects(self, request):
        r"""查询数据库对象列表

        查询数据库对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseObjects
        :type request: :class:`huaweicloudsdkdas.v3.ListDatabaseObjectsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDatabaseObjectsResponse`
        """
        http_info = self._list_database_objects_http_info(request)
        return self._call_api(**http_info)

    def list_database_objects_invoker(self, request):
        http_info = self._list_database_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_database_objects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/get-db-obj-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))
        if 'schema_name' in local_var_params:
            query_params.append(('schema_name', local_var_params['schema_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'table_id' in local_var_params:
            query_params.append(('table_id', local_var_params['table_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'extra_order_by' in local_var_params:
            query_params.append(('extra_order_by', local_var_params['extra_order_by']))
        if 'extra_order' in local_var_params:
            query_params.append(('extra_order', local_var_params['extra_order']))
        if 'obj_type' in local_var_params:
            query_params.append(('obj_type', local_var_params['obj_type']))
        if 'ret_type' in local_var_params:
            query_params.append(('ret_type', local_var_params['ret_type']))
        if 'is_sys' in local_var_params:
            query_params.append(('is_sys', local_var_params['is_sys']))
        if 'obj_sub_type' in local_var_params:
            query_params.append(('obj_sub_type', local_var_params['obj_sub_type']))
        if 'node_type' in local_var_params:
            query_params.append(('node_type', local_var_params['node_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'obj_name' in local_var_params:
            query_params.append(('obj_name', local_var_params['obj_name']))
        if 'keywords' in local_var_params:
            query_params.append(('keywords', local_var_params['keywords']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_dead_lock_databases(self, request):
        r"""获取死锁数据库列表

        获取死锁数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeadLockDatabases
        :type request: :class:`huaweicloudsdkdas.v3.ListDeadLockDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDeadLockDatabasesResponse`
        """
        http_info = self._list_dead_lock_databases_http_info(request)
        return self._call_api(**http_info)

    def list_dead_lock_databases_invoker(self, request):
        http_info = self._list_dead_lock_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dead_lock_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock/get-dead-lock-db-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeadLockDatabasesResponse"
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

    def list_dead_lock_detail(self, request):
        r"""获取死锁详情列表

        获取死锁详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeadLockDetail
        :type request: :class:`huaweicloudsdkdas.v3.ListDeadLockDetailRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDeadLockDetailResponse`
        """
        http_info = self._list_dead_lock_detail_http_info(request)
        return self._call_api(**http_info)

    def list_dead_lock_detail_invoker(self, request):
        http_info = self._list_dead_lock_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dead_lock_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock/get-dead-lock-detail-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeadLockDetailResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_emergency_logs(self, request):
        r"""查询紧急日志

        查询紧急日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEmergencyLogs
        :type request: :class:`huaweicloudsdkdas.v3.ListEmergencyLogsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListEmergencyLogsResponse`
        """
        http_info = self._list_emergency_logs_http_info(request)
        return self._call_api(**http_info)

    def list_emergency_logs_invoker(self, request):
        http_info = self._list_emergency_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_emergency_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/query-emergency-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListEmergencyLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_enterprise_projects(self, request):
        r"""获取企业项目列表

        获取企业项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseProjects
        :type request: :class:`huaweicloudsdkdas.v3.ListEnterpriseProjectsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListEnterpriseProjectsResponse`
        """
        http_info = self._list_enterprise_projects_http_info(request)
        return self._call_api(**http_info)

    def list_enterprise_projects_invoker(self, request):
        http_info = self._list_enterprise_projects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_enterprise_projects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/user-info/eps/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseProjectsResponse"
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

    def list_exception_metrics(self, request):
        r"""查询异常检测指标数据

        Exception Analyze Query Metrics New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExceptionMetrics
        :type request: :class:`huaweicloudsdkdas.v3.ListExceptionMetricsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListExceptionMetricsResponse`
        """
        http_info = self._list_exception_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_exception_metrics_invoker(self, request):
        http_info = self._list_exception_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_exception_metrics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/metrics/{instance_id}/exception-analyze/query-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListExceptionMetricsResponse"
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

    def list_full_dead_locks(self, request):
        r"""获取完整死锁列表

        获取完整死锁列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFullDeadLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListFullDeadLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListFullDeadLocksResponse`
        """
        http_info = self._list_full_dead_locks_http_info(request)
        return self._call_api(**http_info)

    def list_full_dead_locks_invoker(self, request):
        http_info = self._list_full_dead_locks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_full_dead_locks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/get-full-dead-lock-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListFullDeadLocksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def list_full_sql_export_tasks(self, request):
        r"""获取全量SQL导出任务列表

        获取全量SQL导出任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFullSqlExportTasks
        :type request: :class:`huaweicloudsdkdas.v3.ListFullSqlExportTasksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListFullSqlExportTasksResponse`
        """
        http_info = self._list_full_sql_export_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_full_sql_export_tasks_invoker(self, request):
        http_info = self._list_full_sql_export_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_full_sql_export_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/get-export-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListFullSqlExportTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))

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

    def list_full_sql_tasks_api(self, request):
        r"""查询全量SQL明细解析任务

        Fullsql Tasks
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFullSqlTasksApi
        :type request: :class:`huaweicloudsdkdas.v3.ListFullSqlTasksApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListFullSqlTasksApiResponse`
        """
        http_info = self._list_full_sql_tasks_api_http_info(request)
        return self._call_api(**http_info)

    def list_full_sql_tasks_api_invoker(self, request):
        http_info = self._list_full_sql_tasks_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_full_sql_tasks_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListFullSqlTasksApiResponse"
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

    def list_gauss_db_instance_configurations(self, request):
        r"""查询GaussDB实例参数

        查询GaussDB实例参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussDbInstanceConfigurations
        :type request: :class:`huaweicloudsdkdas.v3.ListGaussDbInstanceConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListGaussDbInstanceConfigurationsResponse`
        """
        http_info = self._list_gauss_db_instance_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_db_instance_configurations_invoker(self, request):
        http_info = self._list_gauss_db_instance_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_db_instance_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/get-gauss-db-instance-configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussDbInstanceConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_history_transactions(self, request):
        r"""获取历史事务列表

        获取历史事务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryTransactions
        :type request: :class:`huaweicloudsdkdas.v3.ListHistoryTransactionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListHistoryTransactionsResponse`
        """
        http_info = self._list_history_transactions_http_info(request)
        return self._call_api(**http_info)

    def list_history_transactions_invoker(self, request):
        http_info = self._list_history_transactions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_transactions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/get-history-transaction-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryTransactionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'last_sec_min' in local_var_params:
            query_params.append(('last_sec_min', local_var_params['last_sec_min']))
        if 'last_sec_max' in local_var_params:
            query_params.append(('last_sec_max', local_var_params['last_sec_max']))

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

    def list_index_usage_details(self, request):
        r"""获取索引使用详情列表

        获取索引使用详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndexUsageDetails
        :type request: :class:`huaweicloudsdkdas.v3.ListIndexUsageDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListIndexUsageDetailsResponse`
        """
        http_info = self._list_index_usage_details_http_info(request)
        return self._call_api(**http_info)

    def list_index_usage_details_invoker(self, request):
        http_info = self._list_index_usage_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_index_usage_details_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/get-index-usage-detail-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListIndexUsageDetailsResponse"
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

    def list_index_usage_export_tasks(self, request):
        r"""获取索引使用导出任务列表

        获取索引使用导出任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIndexUsageExportTasks
        :type request: :class:`huaweicloudsdkdas.v3.ListIndexUsageExportTasksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListIndexUsageExportTasksResponse`
        """
        http_info = self._list_index_usage_export_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_index_usage_export_tasks_invoker(self, request):
        http_info = self._list_index_usage_export_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_index_usage_export_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/get-index-usage-export-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListIndexUsageExportTasksResponse"
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

    def list_instance_emergency_logs(self, request):
        r"""查询实例紧急日志

        查询实例紧急日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceEmergencyLogs
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceEmergencyLogsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceEmergencyLogsResponse`
        """
        http_info = self._list_instance_emergency_logs_http_info(request)
        return self._call_api(**http_info)

    def list_instance_emergency_logs_invoker(self, request):
        http_info = self._list_instance_emergency_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_emergency_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/query-emergency-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceEmergencyLogsResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_instance_health_report_tasks(self, request):
        r"""获取实例健康报告任务列表

        获取实例健康报告任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceHealthReportTasks
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceHealthReportTasksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceHealthReportTasksResponse`
        """
        http_info = self._list_instance_health_report_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_instance_health_report_tasks_invoker(self, request):
        http_info = self._list_instance_health_report_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_health_report_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/get-instance-health-report-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceHealthReportTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def list_instance_processes(self, request):
        r"""查询进程列表

        查询进程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceProcesses
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceProcessesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceProcessesResponse`
        """
        http_info = self._list_instance_processes_http_info(request)
        return self._call_api(**http_info)

    def list_instance_processes_invoker(self, request):
        http_info = self._list_instance_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/query-process-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'host' in local_var_params:
            query_params.append(('host', local_var_params['host']))
        if 'db' in local_var_params:
            query_params.append(('db', local_var_params['db']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'command' in local_var_params:
            query_params.append(('command', local_var_params['command']))
        if 'keywords' in local_var_params:
            query_params.append(('keywords', local_var_params['keywords']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'network_type' in local_var_params:
            query_params.append(('network_type', local_var_params['network_type']))

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

    def list_instance_subscription(self, request):
        r"""获取实例订阅列表

        获取实例健康报告订阅列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceSubscription
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceSubscriptionResponse`
        """
        http_info = self._list_instance_subscription_http_info(request)
        return self._call_api(**http_info)

    def list_instance_subscription_invoker(self, request):
        http_info = self._list_instance_subscription_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_subscription_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/get-instance-subscription-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSubscriptionResponse"
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

    def list_instances_api(self, request):
        r"""获取实例列表

        获取实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesApi
        :type request: :class:`huaweicloudsdkdas.v3.ListInstancesApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstancesApiResponse`
        """
        http_info = self._list_instances_api_http_info(request)
        return self._call_api(**http_info)

    def list_instances_api_invoker(self, request):
        http_info = self._list_instances_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_api_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/get-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesApiResponse"
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

    def list_kill_process_history(self, request):
        r"""查询Kill进程历史

        查询Kill进程历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListKillProcessHistory
        :type request: :class:`huaweicloudsdkdas.v3.ListKillProcessHistoryRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListKillProcessHistoryResponse`
        """
        http_info = self._list_kill_process_history_http_info(request)
        return self._call_api(**http_info)

    def list_kill_process_history_invoker(self, request):
        http_info = self._list_kill_process_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_kill_process_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/query-kill-process-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListKillProcessHistoryResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def list_missing_index_details(self, request):
        r"""获取缺失索引详情列表

        获取缺失索引详情列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMissingIndexDetails
        :type request: :class:`huaweicloudsdkdas.v3.ListMissingIndexDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListMissingIndexDetailsResponse`
        """
        http_info = self._list_missing_index_details_http_info(request)
        return self._call_api(**http_info)

    def list_missing_index_details_invoker(self, request):
        http_info = self._list_missing_index_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_missing_index_details_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/get-missing-index-detail-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListMissingIndexDetailsResponse"
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

    def list_missing_index_export_tasks(self, request):
        r"""获取缺失索引导出任务列表

        获取缺失索引导出任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMissingIndexExportTasks
        :type request: :class:`huaweicloudsdkdas.v3.ListMissingIndexExportTasksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListMissingIndexExportTasksResponse`
        """
        http_info = self._list_missing_index_export_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_missing_index_export_tasks_invoker(self, request):
        http_info = self._list_missing_index_export_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_missing_index_export_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/get-missing-index-export-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListMissingIndexExportTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'export_type' in local_var_params:
            query_params.append(('export_type', local_var_params['export_type']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_not_set_charge_mode_instance(self, request):
        r"""获取未设置付费的实例列表

        获取未设置付费的实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotSetChargeModeInstance
        :type request: :class:`huaweicloudsdkdas.v3.ListNotSetChargeModeInstanceRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListNotSetChargeModeInstanceResponse`
        """
        http_info = self._list_not_set_charge_mode_instance_http_info(request)
        return self._call_api(**http_info)

    def list_not_set_charge_mode_instance_invoker(self, request):
        http_info = self._list_not_set_charge_mode_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_not_set_charge_mode_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clouddba/get-not-set-charge-mode-instance",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotSetChargeModeInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def list_obs_buckets(self, request):
        r"""获取OBS桶列表

        New Das Get Obs Buckets List
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBuckets
        :type request: :class:`huaweicloudsdkdas.v3.ListObsBucketsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListObsBucketsResponse`
        """
        http_info = self._list_obs_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_obs_buckets_invoker(self, request):
        http_info = self._list_obs_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_obs_buckets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/obs/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsBucketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def list_obs_objects(self, request):
        r"""查询OBS对象列表

        查询OBS对象列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsObjects
        :type request: :class:`huaweicloudsdkdas.v3.ListObsObjectsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListObsObjectsResponse`
        """
        http_info = self._list_obs_objects_http_info(request)
        return self._call_api(**http_info)

    def list_obs_objects_invoker(self, request):
        http_info = self._list_obs_objects_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_obs_objects_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/obs/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsObjectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'bucket_name' in local_var_params:
            query_params.append(('bucket_name', local_var_params['bucket_name']))
        if 'max_keys' in local_var_params:
            query_params.append(('max_keys', local_var_params['max_keys']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))

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

    def list_postgres_processes(self, request):
        r"""PostgreSQL查询进程列表

        PostgreSQL查询进程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPostgresProcesses
        :type request: :class:`huaweicloudsdkdas.v3.ListPostgresProcessesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListPostgresProcessesResponse`
        """
        http_info = self._list_postgres_processes_http_info(request)
        return self._call_api(**http_info)

    def list_postgres_processes_invoker(self, request):
        http_info = self._list_postgres_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_postgres_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/pg/query-process-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListPostgresProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'host' in local_var_params:
            query_params.append(('host', local_var_params['host']))
        if 'db' in local_var_params:
            query_params.append(('db', local_var_params['db']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'command' in local_var_params:
            query_params.append(('command', local_var_params['command']))
        if 'keywords' in local_var_params:
            query_params.append(('keywords', local_var_params['keywords']))
        if 'show_all' in local_var_params:
            query_params.append(('show_all', local_var_params['show_all']))
        if 'show_no_pid' in local_var_params:
            query_params.append(('show_no_pid', local_var_params['show_no_pid']))
        if 'time' in local_var_params:
            query_params.append(('time', local_var_params['time']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'node_role' in local_var_params:
            query_params.append(('node_role', local_var_params['node_role']))
        if 'hide_sys' in local_var_params:
            query_params.append(('hide_sys', local_var_params['hide_sys']))

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

    def list_rapid_growth_tables(self, request):
        r"""获取快速增长表

        获取快速增长表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRapidGrowthTables
        :type request: :class:`huaweicloudsdkdas.v3.ListRapidGrowthTablesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListRapidGrowthTablesResponse`
        """
        http_info = self._list_rapid_growth_tables_http_info(request)
        return self._call_api(**http_info)

    def list_rapid_growth_tables_invoker(self, request):
        http_info = self._list_rapid_growth_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rapid_growth_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space/get-rapid-growth-tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListRapidGrowthTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))

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

    def list_rds_instance_configurations_new(self, request):
        r"""查询RDS实例参数

        查询RDS实例参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRdsInstanceConfigurationsNew
        :type request: :class:`huaweicloudsdkdas.v3.ListRdsInstanceConfigurationsNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListRdsInstanceConfigurationsNewResponse`
        """
        http_info = self._list_rds_instance_configurations_new_http_info(request)
        return self._call_api(**http_info)

    def list_rds_instance_configurations_new_invoker(self, request):
        http_info = self._list_rds_instance_configurations_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rds_instance_configurations_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/get-rds-instance-configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListRdsInstanceConfigurationsNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_risk_items_api(self, request):
        r"""获取风险项

        获取风险项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRiskItemsApi
        :type request: :class:`huaweicloudsdkdas.v3.ListRiskItemsApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListRiskItemsApiResponse`
        """
        http_info = self._list_risk_items_api_http_info(request)
        return self._call_api(**http_info)

    def list_risk_items_api_invoker(self, request):
        http_info = self._list_risk_items_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_risk_items_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/get-risk-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListRiskItemsApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def list_risks(self, request):
        r"""查询风险列表

        查询风险列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRisks
        :type request: :class:`huaweicloudsdkdas.v3.ListRisksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListRisksResponse`
        """
        http_info = self._list_risks_http_info(request)
        return self._call_api(**http_info)

    def list_risks_invoker(self, request):
        http_info = self._list_risks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_risks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/query-risk-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListRisksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'num' in local_var_params:
            query_params.append(('num', local_var_params['num']))
        if 'metric_code' in local_var_params:
            query_params.append(('metric_code', local_var_params['metric_code']))

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

    def list_schema_names(self, request):
        r"""获取schema名称列表

        获取schema名称列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSchemaNames
        :type request: :class:`huaweicloudsdkdas.v3.ListSchemaNamesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSchemaNamesResponse`
        """
        http_info = self._list_schema_names_http_info(request)
        return self._call_api(**http_info)

    def list_schema_names_invoker(self, request):
        http_info = self._list_schema_names_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_schema_names_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/schema/clouddba-get-schema-name-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSchemaNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'obj_type' in local_var_params:
            query_params.append(('obj_type', local_var_params['obj_type']))
        if 'is_with_all_user' in local_var_params:
            query_params.append(('is_with_all_user', local_var_params['is_with_all_user']))
        if 'node_type' in local_var_params:
            query_params.append(('node_type', local_var_params['node_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def list_shared_connections(self, request):
        r"""查询共享列表

        查询共享列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSharedConnections
        :type request: :class:`huaweicloudsdkdas.v3.ListSharedConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSharedConnectionsResponse`
        """
        http_info = self._list_shared_connections_http_info(request)
        return self._call_api(**http_info)

    def list_shared_connections_invoker(self, request):
        http_info = self._list_shared_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_shared_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/get-shared-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSharedConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'keywords' in local_var_params:
            query_params.append(('keywords', local_var_params['keywords']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_slow_log_archives(self, request):
        r"""获取慢日志归档列表

        获取慢日志归档列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogArchives
        :type request: :class:`huaweicloudsdkdas.v3.ListSlowLogArchivesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSlowLogArchivesResponse`
        """
        http_info = self._list_slow_log_archives_http_info(request)
        return self._call_api(**http_info)

    def list_slow_log_archives_invoker(self, request):
        http_info = self._list_slow_log_archives_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_log_archives_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-archive-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogArchivesResponse"
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

    def list_slow_log_export_task(self, request):
        r"""获取慢日志导出任务列表

        获取慢日志导出任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogExportTask
        :type request: :class:`huaweicloudsdkdas.v3.ListSlowLogExportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSlowLogExportTaskResponse`
        """
        http_info = self._list_slow_log_export_task_http_info(request)
        return self._call_api(**http_info)

    def list_slow_log_export_task_invoker(self, request):
        http_info = self._list_slow_log_export_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_slow_log_export_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-export-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSlowLogExportTaskResponse"
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
        if 'export_type' in local_var_params:
            query_params.append(('export_type', local_var_params['export_type']))

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

    def list_smn_topics(self, request):
        r"""获取SMN主题列表

        获取SMN主题列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSmnTopics
        :type request: :class:`huaweicloudsdkdas.v3.ListSmnTopicsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSmnTopicsResponse`
        """
        http_info = self._list_smn_topics_http_info(request)
        return self._call_api(**http_info)

    def list_smn_topics_invoker(self, request):
        http_info = self._list_smn_topics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_smn_topics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/health-report/get-smn-topic-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmnTopicsResponse"
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

    def list_snapshots4_api(self, request):
        r"""查询快照

        查询快照
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshots4Api
        :type request: :class:`huaweicloudsdkdas.v3.ListSnapshots4ApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSnapshots4ApiResponse`
        """
        http_info = self._list_snapshots4_api_http_info(request)
        return self._call_api(**http_info)

    def list_snapshots4_api_invoker(self, request):
        http_info = self._list_snapshots4_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_snapshots4_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/query-snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshots4ApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'module' in local_var_params:
            query_params.append(('module', local_var_params['module']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))

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

    def list_sql_limit_user_instance(self, request):
        r"""获取用户实例

        获取用户实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlLimitUserInstance
        :type request: :class:`huaweicloudsdkdas.v3.ListSqlLimitUserInstanceRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSqlLimitUserInstanceResponse`
        """
        http_info = self._list_sql_limit_user_instance_http_info(request)
        return self._call_api(**http_info)

    def list_sql_limit_user_instance_invoker(self, request):
        http_info = self._list_sql_limit_user_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_limit_user_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/sql-limiting/get-user-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlLimitUserInstanceResponse"
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

    def list_sql_template_comparisons(self, request):
        r"""查询SQL模板对比列表

        查询SQL模板对比列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlTemplateComparisons
        :type request: :class:`huaweicloudsdkdas.v3.ListSqlTemplateComparisonsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSqlTemplateComparisonsResponse`
        """
        http_info = self._list_sql_template_comparisons_http_info(request)
        return self._call_api(**http_info)

    def list_sql_template_comparisons_invoker(self, request):
        http_info = self._list_sql_template_comparisons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_template_comparisons_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/query-sql-tpl-cmp-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlTemplateComparisonsResponse"
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

    def list_sql_template_databases(self, request):
        r"""查询SQL模板数据库列表

        查询SQL模板数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlTemplateDatabases
        :type request: :class:`huaweicloudsdkdas.v3.ListSqlTemplateDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSqlTemplateDatabasesResponse`
        """
        http_info = self._list_sql_template_databases_http_info(request)
        return self._call_api(**http_info)

    def list_sql_template_databases_invoker(self, request):
        http_info = self._list_sql_template_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_template_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/query-sql-tpl-db-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlTemplateDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'operation' in local_var_params:
            query_params.append(('operation', local_var_params['operation']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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

    def list_sql_templates(self, request):
        r"""查询SQL模板列表

        查询SQL模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlTemplates
        :type request: :class:`huaweicloudsdkdas.v3.ListSqlTemplatesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSqlTemplatesResponse`
        """
        http_info = self._list_sql_templates_http_info(request)
        return self._call_api(**http_info)

    def list_sql_templates_invoker(self, request):
        http_info = self._list_sql_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_templates_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/query-sql-tpl-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlTemplatesResponse"
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

    def list_sub_users(self, request):
        r"""获取子用户

        获取子用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSubUsers
        :type request: :class:`huaweicloudsdkdas.v3.ListSubUsersRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSubUsersResponse`
        """
        http_info = self._list_sub_users_http_info(request)
        return self._call_api(**http_info)

    def list_sub_users_invoker(self, request):
        http_info = self._list_sub_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sub_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/user-info/iam/sub-users",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in local_var_params:
            query_params.append(('keywords', local_var_params['keywords']))
        if 'connection_id' in local_var_params:
            query_params.append(('connection_id', local_var_params['connection_id']))

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

    def list_supported_metric_names(self, request):
        r"""多节点单指标支持指标信息

        Metric Names Support New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportedMetricNames
        :type request: :class:`huaweicloudsdkdas.v3.ListSupportedMetricNamesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSupportedMetricNamesResponse`
        """
        http_info = self._list_supported_metric_names_http_info(request)
        return self._call_api(**http_info)

    def list_supported_metric_names_invoker(self, request):
        http_info = self._list_supported_metric_names_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_supported_metric_names_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/metric-names/support",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportedMetricNamesResponse"
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

    def list_supported_metrics(self, request):
        r"""查询支持异常检测的指标名

        Exception Analyze Supported Metrics New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupportedMetrics
        :type request: :class:`huaweicloudsdkdas.v3.ListSupportedMetricsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSupportedMetricsResponse`
        """
        http_info = self._list_supported_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_supported_metrics_invoker(self, request):
        http_info = self._list_supported_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_supported_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/metrics/exception-analyze/supported-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupportedMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'instance_mode' in local_var_params:
            query_params.append(('instance_mode', local_var_params['instance_mode']))

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

    def list_tasks_by_batch_id(self, request):
        r"""按批次ID查询全量SQL任务

        按批次ID查询全量SQL任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasksByBatchId
        :type request: :class:`huaweicloudsdkdas.v3.ListTasksByBatchIdRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListTasksByBatchIdResponse`
        """
        http_info = self._list_tasks_by_batch_id_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_by_batch_id_invoker(self, request):
        http_info = self._list_tasks_by_batch_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tasks_by_batch_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/task/query-by-batch-id",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksByBatchIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'batch_id' in local_var_params:
            query_params.append(('batch_id', local_var_params['batch_id']))

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

    def list_tasks_by_sql_template_id(self, request):
        r"""按SQL模板ID查询全量SQL任务

        按SQL模板ID查询全量SQL任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasksBySqlTemplateId
        :type request: :class:`huaweicloudsdkdas.v3.ListTasksBySqlTemplateIdRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListTasksBySqlTemplateIdResponse`
        """
        http_info = self._list_tasks_by_sql_template_id_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_by_sql_template_id_invoker(self, request):
        http_info = self._list_tasks_by_sql_template_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tasks_by_sql_template_id_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/tasks/query-by-sql-template-id",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksBySqlTemplateIdResponse"
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

    def list_tasks_by_task_id(self, request):
        r"""按任务ID查询全量SQL任务

        按任务ID查询全量SQL任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasksByTaskId
        :type request: :class:`huaweicloudsdkdas.v3.ListTasksByTaskIdRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListTasksByTaskIdResponse`
        """
        http_info = self._list_tasks_by_task_id_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_by_task_id_invoker(self, request):
        http_info = self._list_tasks_by_task_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tasks_by_task_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/task/query-by-task-id",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksByTaskIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def list_template_database_comparisons(self, request):
        r"""查询模板数据库对比列表

        查询模板数据库对比列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateDatabaseComparisons
        :type request: :class:`huaweicloudsdkdas.v3.ListTemplateDatabaseComparisonsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListTemplateDatabaseComparisonsResponse`
        """
        http_info = self._list_template_database_comparisons_http_info(request)
        return self._call_api(**http_info)

    def list_template_database_comparisons_invoker(self, request):
        http_info = self._list_template_database_comparisons_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_database_comparisons_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/query-tpl-db-cmp-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateDatabaseComparisonsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'start_at1' in local_var_params:
            query_params.append(('start_at1', local_var_params['start_at1']))
        if 'end_at1' in local_var_params:
            query_params.append(('end_at1', local_var_params['end_at1']))
        if 'start_at2' in local_var_params:
            query_params.append(('start_at2', local_var_params['start_at2']))
        if 'end_at2' in local_var_params:
            query_params.append(('end_at2', local_var_params['end_at2']))
        if 'operation' in local_var_params:
            query_params.append(('operation', local_var_params['operation']))
        if 'db_name_list' in local_var_params:
            query_params.append(('db_name_list', local_var_params['db_name_list']))
            collection_formats['db_name_list'] = 'csv'
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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

    def list_user_instance_list(self, request):
        r"""获取用户实例列表

        获取用户实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUserInstanceList
        :type request: :class:`huaweicloudsdkdas.v3.ListUserInstanceListRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListUserInstanceListResponse`
        """
        http_info = self._list_user_instance_list_http_info(request)
        return self._call_api(**http_info)

    def list_user_instance_list_invoker(self, request):
        http_info = self._list_user_instance_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_user_instance_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/get-user-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserInstanceListResponse"
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

    def login(self, request):
        r"""实例级登录

        Login
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Login
        :type request: :class:`huaweicloudsdkdas.v3.LoginRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.LoginResponse`
        """
        http_info = self._login_http_info(request)
        return self._call_api(**http_info)

    def login_invoker(self, request):
        http_info = self._login_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _login_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/login",
            "request_type": request.__class__.__name__,
            "response_type": "LoginResponse"
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

    def modify_connection(self, request):
        r"""修改实例连接

        修改实例连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyConnection
        :type request: :class:`huaweicloudsdkdas.v3.ModifyConnectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ModifyConnectionResponse`
        """
        http_info = self._modify_connection_http_info(request)
        return self._call_api(**http_info)

    def modify_connection_invoker(self, request):
        http_info = self._modify_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def parse_sql_limit_rule_new(self, request):
        r"""解析SQL限流规则

        解析SQL限流规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseSqlLimitRuleNew
        :type request: :class:`huaweicloudsdkdas.v3.ParseSqlLimitRuleNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ParseSqlLimitRuleNewResponse`
        """
        http_info = self._parse_sql_limit_rule_new_http_info(request)
        return self._call_api(**http_info)

    def parse_sql_limit_rule_new_invoker(self, request):
        http_info = self._parse_sql_limit_rule_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_sql_limit_rule_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/sql-limiting/parse-sql-limit-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ParseSqlLimitRuleNewResponse"
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

    def preview_session_for_kill_process_task_new(self, request):
        r"""预览Kill进程任务的会话

        预览Kill进程任务的会话
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PreviewSessionForKillProcessTaskNew
        :type request: :class:`huaweicloudsdkdas.v3.PreviewSessionForKillProcessTaskNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.PreviewSessionForKillProcessTaskNewResponse`
        """
        http_info = self._preview_session_for_kill_process_task_new_http_info(request)
        return self._call_api(**http_info)

    def preview_session_for_kill_process_task_new_invoker(self, request):
        http_info = self._preview_session_for_kill_process_task_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _preview_session_for_kill_process_task_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/preview-session-for-kill-process-task",
            "request_type": request.__class__.__name__,
            "response_type": "PreviewSessionForKillProcessTaskNewResponse"
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

    def put_global_privacy_new(self, request):
        r"""设置全局隐私

        设置全局隐私
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutGlobalPrivacyNew
        :type request: :class:`huaweicloudsdkdas.v3.PutGlobalPrivacyNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.PutGlobalPrivacyNewResponse`
        """
        http_info = self._put_global_privacy_new_http_info(request)
        return self._call_api(**http_info)

    def put_global_privacy_new_invoker(self, request):
        http_info = self._put_global_privacy_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_global_privacy_new_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/policy/{agree_status}/put-global-privacy",
            "request_type": request.__class__.__name__,
            "response_type": "PutGlobalPrivacyNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agree_status' in local_var_params:
            path_params['agree_status'] = local_var_params['agree_status']

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

    def recollect_index_usage_new(self, request):
        r"""重新收集索引使用

        重新收集索引使用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecollectIndexUsageNew
        :type request: :class:`huaweicloudsdkdas.v3.RecollectIndexUsageNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RecollectIndexUsageNewResponse`
        """
        http_info = self._recollect_index_usage_new_http_info(request)
        return self._call_api(**http_info)

    def recollect_index_usage_new_invoker(self, request):
        http_info = self._recollect_index_usage_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recollect_index_usage_new_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/recollect-index-usage",
            "request_type": request.__class__.__name__,
            "response_type": "RecollectIndexUsageNewResponse"
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

    def recollect_missing_index_new(self, request):
        r"""重新收集缺失索引

        重新收集缺失索引
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecollectMissingIndexNew
        :type request: :class:`huaweicloudsdkdas.v3.RecollectMissingIndexNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RecollectMissingIndexNewResponse`
        """
        http_info = self._recollect_missing_index_new_http_info(request)
        return self._call_api(**http_info)

    def recollect_missing_index_new_invoker(self, request):
        http_info = self._recollect_missing_index_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recollect_missing_index_new_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/recollect-missing-index",
            "request_type": request.__class__.__name__,
            "response_type": "RecollectMissingIndexNewResponse"
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

    def retry_binlog_part(self, request):
        r"""重试binlog解析任务部分

        重试binlog解析任务部分
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryBinlogPart
        :type request: :class:`huaweicloudsdkdas.v3.RetryBinlogPartRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RetryBinlogPartResponse`
        """
        http_info = self._retry_binlog_part_http_info(request)
        return self._call_api(**http_info)

    def retry_binlog_part_invoker(self, request):
        http_info = self._retry_binlog_part_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_binlog_part_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/retry-part",
            "request_type": request.__class__.__name__,
            "response_type": "RetryBinlogPartResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def retry_binlog_task(self, request):
        r"""重试binlog解析任务

        重试binlog解析任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryBinlogTask
        :type request: :class:`huaweicloudsdkdas.v3.RetryBinlogTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RetryBinlogTaskResponse`
        """
        http_info = self._retry_binlog_task_http_info(request)
        return self._call_api(**http_info)

    def retry_binlog_task_invoker(self, request):
        http_info = self._retry_binlog_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_binlog_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/retry-task",
            "request_type": request.__class__.__name__,
            "response_type": "RetryBinlogTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def search_binlog_parse(self, request):
        r"""查看binlog解析详情

        查看binlog解析详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchBinlogParse
        :type request: :class:`huaweicloudsdkdas.v3.SearchBinlogParseRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SearchBinlogParseResponse`
        """
        http_info = self._search_binlog_parse_http_info(request)
        return self._call_api(**http_info)

    def search_binlog_parse_invoker(self, request):
        http_info = self._search_binlog_parse_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_binlog_parse_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchBinlogParseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def search_error_info4_api(self, request):
        r"""查看binlog解析错误信息

        查看binlog解析错误信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchErrorInfo4Api
        :type request: :class:`huaweicloudsdkdas.v3.SearchErrorInfo4ApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SearchErrorInfo4ApiResponse`
        """
        http_info = self._search_error_info4_api_http_info(request)
        return self._call_api(**http_info)

    def search_error_info4_api_invoker(self, request):
        http_info = self._search_error_info4_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_error_info4_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/search-error-info",
            "request_type": request.__class__.__name__,
            "response_type": "SearchErrorInfo4ApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))

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

    def search_error_info_source4_api(self, request):
        r"""查看binlog解析错误信息条件

        查看binlog解析错误信息条件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchErrorInfoSource4Api
        :type request: :class:`huaweicloudsdkdas.v3.SearchErrorInfoSource4ApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SearchErrorInfoSource4ApiResponse`
        """
        http_info = self._search_error_info_source4_api_http_info(request)
        return self._call_api(**http_info)

    def search_error_info_source4_api_invoker(self, request):
        http_info = self._search_error_info_source4_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_error_info_source4_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/search-error-info-source",
            "request_type": request.__class__.__name__,
            "response_type": "SearchErrorInfoSource4ApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))

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

    def search_new(self, request):
        r"""全量SQL搜索

        全量SQL搜索
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchNew
        :type request: :class:`huaweicloudsdkdas.v3.SearchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SearchNewResponse`
        """
        http_info = self._search_new_http_info(request)
        return self._call_api(**http_info)

    def search_new_invoker(self, request):
        http_info = self._search_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
        if 'task_ids' in local_var_params:
            query_params.append(('task_ids', local_var_params['task_ids']))
            collection_formats['task_ids'] = 'csv'
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'fuzzy' in local_var_params:
            query_params.append(('fuzzy', local_var_params['fuzzy']))
        if 'user_list' in local_var_params:
            query_params.append(('user_list', local_var_params['user_list']))
        if 'db_list' in local_var_params:
            query_params.append(('db_list', local_var_params['db_list']))
        if 'operation_list' in local_var_params:
            query_params.append(('operation_list', local_var_params['operation_list']))
        if 'client_ip_list' in local_var_params:
            query_params.append(('client_ip_list', local_var_params['client_ip_list']))
        if 'thread_id_list' in local_var_params:
            query_params.append(('thread_id_list', local_var_params['thread_id_list']))
        if 'trx_id_list' in local_var_params:
            query_params.append(('trx_id_list', local_var_params['trx_id_list']))
        if 'session_id_list' in local_var_params:
            query_params.append(('session_id_list', local_var_params['session_id_list']))
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
        if 'sql_template_ids' in local_var_params:
            query_params.append(('sql_template_ids', local_var_params['sql_template_ids']))
        if 'cost_min' in local_var_params:
            query_params.append(('cost_min', local_var_params['cost_min']))
        if 'cost_max' in local_var_params:
            query_params.append(('cost_max', local_var_params['cost_max']))
        if 'scan_min' in local_var_params:
            query_params.append(('scan_min', local_var_params['scan_min']))
        if 'scan_max' in local_var_params:
            query_params.append(('scan_max', local_var_params['scan_max']))
        if 'affect_min' in local_var_params:
            query_params.append(('affect_min', local_var_params['affect_min']))
        if 'affect_max' in local_var_params:
            query_params.append(('affect_max', local_var_params['affect_max']))
        if 'return_min' in local_var_params:
            query_params.append(('return_min', local_var_params['return_min']))
        if 'return_max' in local_var_params:
            query_params.append(('return_max', local_var_params['return_max']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
        if 'page_no' in local_var_params:
            query_params.append(('page_no', local_var_params['page_no']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def set_full_dead_lock_switch_new(self, request):
        r"""设置完整死锁开关

        设置完整死锁开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetFullDeadLockSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetFullDeadLockSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetFullDeadLockSwitchNewResponse`
        """
        http_info = self._set_full_dead_lock_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_full_dead_lock_switch_new_invoker(self, request):
        http_info = self._set_full_dead_lock_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_full_dead_lock_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/set-full-dead-lock-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetFullDeadLockSwitchNewResponse"
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

    def set_history_transaction_switch_new(self, request):
        r"""设置历史事务开关

        设置历史事务开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetHistoryTransactionSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetHistoryTransactionSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetHistoryTransactionSwitchNewResponse`
        """
        http_info = self._set_history_transaction_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_history_transaction_switch_new_invoker(self, request):
        http_info = self._set_history_transaction_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_history_transaction_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/set-history-transaction-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetHistoryTransactionSwitchNewResponse"
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

    def set_index_usage_switch_new(self, request):
        r"""设置索引使用开关

        设置索引使用开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetIndexUsageSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetIndexUsageSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetIndexUsageSwitchNewResponse`
        """
        http_info = self._set_index_usage_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_index_usage_switch_new_invoker(self, request):
        http_info = self._set_index_usage_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_index_usage_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/set-index-usage-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetIndexUsageSwitchNewResponse"
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

    def set_long_history_transaction_switch_new(self, request):
        r"""设置长历史事务开关

        设置长历史事务开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetLongHistoryTransactionSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetLongHistoryTransactionSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetLongHistoryTransactionSwitchNewResponse`
        """
        http_info = self._set_long_history_transaction_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_long_history_transaction_switch_new_invoker(self, request):
        http_info = self._set_long_history_transaction_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_long_history_transaction_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/set-long-history-transaction-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetLongHistoryTransactionSwitchNewResponse"
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

    def set_metric_threshold_new(self, request):
        r"""设置指标阈值

        设置指标阈值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetMetricThresholdNew
        :type request: :class:`huaweicloudsdkdas.v3.SetMetricThresholdNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetMetricThresholdNewResponse`
        """
        http_info = self._set_metric_threshold_new_http_info(request)
        return self._call_api(**http_info)

    def set_metric_threshold_new_invoker(self, request):
        http_info = self._set_metric_threshold_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_metric_threshold_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/tenant-panel/set-metric-threshold",
            "request_type": request.__class__.__name__,
            "response_type": "SetMetricThresholdNewResponse"
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

    def set_missing_index_switch_new(self, request):
        r"""设置缺失索引开关

        设置缺失索引开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetMissingIndexSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetMissingIndexSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetMissingIndexSwitchNewResponse`
        """
        http_info = self._set_missing_index_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_missing_index_switch_new_invoker(self, request):
        http_info = self._set_missing_index_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_missing_index_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/set-missing-index-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetMissingIndexSwitchNewResponse"
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

    def set_rapid_growth_threshold_new(self, request):
        r"""设置快速增长阈值

        设置快速增长阈值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRapidGrowthThresholdNew
        :type request: :class:`huaweicloudsdkdas.v3.SetRapidGrowthThresholdNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetRapidGrowthThresholdNewResponse`
        """
        http_info = self._set_rapid_growth_threshold_new_http_info(request)
        return self._call_api(**http_info)

    def set_rapid_growth_threshold_new_invoker(self, request):
        http_info = self._set_rapid_growth_threshold_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_rapid_growth_threshold_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space/set-rapid-growth-threshold",
            "request_type": request.__class__.__name__,
            "response_type": "SetRapidGrowthThresholdNewResponse"
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

    def set_slow_log_switch_new(self, request):
        r"""设置慢日志开关

        设置慢日志开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSlowLogSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetSlowLogSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetSlowLogSwitchNewResponse`
        """
        http_info = self._set_slow_log_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_slow_log_switch_new_invoker(self, request):
        http_info = self._set_slow_log_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_slow_log_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/set-slow-log-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetSlowLogSwitchNewResponse"
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

    def set_sql_limiting_switch_new(self, request):
        r"""设置SQL限流开关

        设置SQL限流开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSqlLimitingSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetSqlLimitingSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetSqlLimitingSwitchNewResponse`
        """
        http_info = self._set_sql_limiting_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_sql_limiting_switch_new_invoker(self, request):
        http_info = self._set_sql_limiting_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sql_limiting_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/set-sql-limiting-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetSqlLimitingSwitchNewResponse"
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

    def set_sql_switch_new(self, request):
        r"""设置SQL开关

        设置SQL开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSqlSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.SetSqlSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetSqlSwitchNewResponse`
        """
        http_info = self._set_sql_switch_new_http_info(request)
        return self._call_api(**http_info)

    def set_sql_switch_new_invoker(self, request):
        http_info = self._set_sql_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sql_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/set-sql-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetSqlSwitchNewResponse"
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

    def show_binlog_export_task_info(self, request):
        r"""查询binlog导出任务信息

        查询binlog导出任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBinlogExportTaskInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowBinlogExportTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowBinlogExportTaskInfoResponse`
        """
        http_info = self._show_binlog_export_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_binlog_export_task_info_invoker(self, request):
        http_info = self._show_binlog_export_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_binlog_export_task_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/get-export-task-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBinlogExportTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'export_task_id' in local_var_params:
            query_params.append(('export_task_id', local_var_params['export_task_id']))

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

    def show_binlog_parse(self, request):
        r"""查看binlog概览

        查看binlog概览
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBinlogParse
        :type request: :class:`huaweicloudsdkdas.v3.ShowBinlogParseRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowBinlogParseResponse`
        """
        http_info = self._show_binlog_parse_http_info(request)
        return self._call_api(**http_info)

    def show_binlog_parse_invoker(self, request):
        http_info = self._show_binlog_parse_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_binlog_parse_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/show",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBinlogParseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_binlog_task_info(self, request):
        r"""查看binlog解析任务详情

        查看binlog解析任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBinlogTaskInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowBinlogTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowBinlogTaskInfoResponse`
        """
        http_info = self._show_binlog_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_binlog_task_info_invoker(self, request):
        http_info = self._show_binlog_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_binlog_task_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/get-task-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBinlogTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def show_connection_detail(self, request):
        r"""查询实例连接详情

        查询实例连接详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectionDetail
        :type request: :class:`huaweicloudsdkdas.v3.ShowConnectionDetailRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowConnectionDetailResponse`
        """
        http_info = self._show_connection_detail_http_info(request)
        return self._call_api(**http_info)

    def show_connection_detail_invoker(self, request):
        http_info = self._show_connection_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connection_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectionDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_dds_connection_stat(self, request):
        r"""DDS连接统计

        DDS连接统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDdsConnectionStat
        :type request: :class:`huaweicloudsdkdas.v3.ShowDdsConnectionStatRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDdsConnectionStatResponse`
        """
        http_info = self._show_dds_connection_stat_http_info(request)
        return self._call_api(**http_info)

    def show_dds_connection_stat_invoker(self, request):
        http_info = self._show_dds_connection_stat_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dds_connection_stat_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dds-connection-stat",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdsConnectionStatResponse"
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
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def show_dds_slow_log_trend(self, request):
        r"""获取DDS慢日志趋势

        获取DDS慢日志趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDdsSlowLogTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowDdsSlowLogTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDdsSlowLogTrendResponse`
        """
        http_info = self._show_dds_slow_log_trend_http_info(request)
        return self._call_api(**http_info)

    def show_dds_slow_log_trend_invoker(self, request):
        http_info = self._show_dds_slow_log_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dds_slow_log_trend_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-trend-dds",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDdsSlowLogTrendResponse"
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

    def show_dead_lock_origin_data(self, request):
        r"""获取死锁原始数据

        获取死锁原始数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockOriginData
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockOriginDataRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockOriginDataResponse`
        """
        http_info = self._show_dead_lock_origin_data_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_origin_data_invoker(self, request):
        http_info = self._show_dead_lock_origin_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_origin_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock/get-dead-lock-origin-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockOriginDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dead_lock_id' in local_var_params:
            query_params.append(('dead_lock_id', local_var_params['dead_lock_id']))
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

    def show_dead_lock_relationship(self, request):
        r"""获取死锁关系

        获取死锁关系
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockRelationship
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockRelationshipRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockRelationshipResponse`
        """
        http_info = self._show_dead_lock_relationship_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_relationship_invoker(self, request):
        http_info = self._show_dead_lock_relationship_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_relationship_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock/get-dead-lock-relationship",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockRelationshipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dead_lock_id' in local_var_params:
            query_params.append(('dead_lock_id', local_var_params['dead_lock_id']))
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

    def show_dead_lock_statistics(self, request):
        r"""获取死锁统计

        获取死锁统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockStatistics
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockStatisticsResponse`
        """
        http_info = self._show_dead_lock_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_statistics_invoker(self, request):
        http_info = self._show_dead_lock_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock/get-dead-lock-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'current_time' in local_var_params:
            query_params.append(('current_time', local_var_params['current_time']))
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

    def show_dead_lock_trend(self, request):
        r"""获取死锁趋势

        获取死锁趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockTrendResponse`
        """
        http_info = self._show_dead_lock_trend_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_trend_invoker(self, request):
        http_info = self._show_dead_lock_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock/get-dead-lock-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockTrendResponse"
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

    def show_execute_result_without_key(self, request):
        r"""查询SQL执行结果

        查询SQL执行结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExecuteResultWithoutKey
        :type request: :class:`huaweicloudsdkdas.v3.ShowExecuteResultWithoutKeyRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowExecuteResultWithoutKeyResponse`
        """
        http_info = self._show_execute_result_without_key_http_info(request)
        return self._call_api(**http_info)

    def show_execute_result_without_key_invoker(self, request):
        http_info = self._show_execute_result_without_key_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_execute_result_without_key_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/get-execute-result-without-key",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExecuteResultWithoutKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'execute_id' in local_var_params:
            query_params.append(('execute_id', local_var_params['execute_id']))

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

    def show_execute_result_without_key_no_retry(self, request):
        r"""查询SQL执行结果（POST）

        查询SQL执行结果（POST）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExecuteResultWithoutKeyNoRetry
        :type request: :class:`huaweicloudsdkdas.v3.ShowExecuteResultWithoutKeyNoRetryRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowExecuteResultWithoutKeyNoRetryResponse`
        """
        http_info = self._show_execute_result_without_key_no_retry_http_info(request)
        return self._call_api(**http_info)

    def show_execute_result_without_key_no_retry_invoker(self, request):
        http_info = self._show_execute_result_without_key_no_retry_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_execute_result_without_key_no_retry_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/get-execute-result-without-key",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExecuteResultWithoutKeyNoRetryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_execution_plan(self, request):
        r"""获取执行计划

        获取执行计划
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExecutionPlan
        :type request: :class:`huaweicloudsdkdas.v3.ShowExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowExecutionPlanResponse`
        """
        http_info = self._show_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def show_execution_plan_invoker(self, request):
        http_info = self._show_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_execution_plan_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/get-plan",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_execution_time_template_trend(self, request):
        r"""查询执行时间模板趋势

        查询执行时间模板趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExecutionTimeTemplateTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowExecutionTimeTemplateTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowExecutionTimeTemplateTrendResponse`
        """
        http_info = self._show_execution_time_template_trend_http_info(request)
        return self._call_api(**http_info)

    def show_execution_time_template_trend_invoker(self, request):
        http_info = self._show_execution_time_template_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_execution_time_template_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/query-ex-time-tpl-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExecutionTimeTemplateTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'interval_millis' in local_var_params:
            query_params.append(('interval_millis', local_var_params['interval_millis']))

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

    def show_fragment_switch(self, request):
        r"""是否展示fragment任务

        是否展示fragment任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFragmentSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ShowFragmentSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowFragmentSwitchResponse`
        """
        http_info = self._show_fragment_switch_http_info(request)
        return self._call_api(**http_info)

    def show_fragment_switch_invoker(self, request):
        http_info = self._show_fragment_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_fragment_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/fragment-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFragmentSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_full_sql_sample(self, request):
        r"""获取全量SQL样本

        Full Sql Sample
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFullSqlSample
        :type request: :class:`huaweicloudsdkdas.v3.ShowFullSqlSampleRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowFullSqlSampleResponse`
        """
        http_info = self._show_full_sql_sample_http_info(request)
        return self._call_api(**http_info)

    def show_full_sql_sample_invoker(self, request):
        http_info = self._show_full_sql_sample_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_full_sql_sample_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/full-sql-sample",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFullSqlSampleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'sql_template_id' in local_var_params:
            query_params.append(('sql_template_id', local_var_params['sql_template_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))

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

    def show_iam_user(self, request):
        r"""获取IAM用户信息

        Query Iam User New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIamUser
        :type request: :class:`huaweicloudsdkdas.v3.ShowIamUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowIamUserResponse`
        """
        http_info = self._show_iam_user_http_info(request)
        return self._call_api(**http_info)

    def show_iam_user_invoker(self, request):
        http_info = self._show_iam_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_iam_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/user-info/iam/user",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIamUserResponse"
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

    def show_index_usage_statistics(self, request):
        r"""获取索引使用统计

        获取索引使用统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndexUsageStatistics
        :type request: :class:`huaweicloudsdkdas.v3.ShowIndexUsageStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowIndexUsageStatisticsResponse`
        """
        http_info = self._show_index_usage_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_index_usage_statistics_invoker(self, request):
        http_info = self._show_index_usage_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_index_usage_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/get-index-usage-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIndexUsageStatisticsResponse"
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

    def show_index_usage_trend(self, request):
        r"""获取索引使用趋势

        获取索引使用趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndexUsageTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowIndexUsageTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowIndexUsageTrendResponse`
        """
        http_info = self._show_index_usage_trend_http_info(request)
        return self._call_api(**http_info)

    def show_index_usage_trend_invoker(self, request):
        http_info = self._show_index_usage_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_index_usage_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/get-index-usage-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIndexUsageTrendResponse"
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

    def show_instance_distribution(self, request):
        r"""获取实例分布

        获取实例分布
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceDistribution
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceDistributionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceDistributionResponse`
        """
        http_info = self._show_instance_distribution_http_info(request)
        return self._call_api(**http_info)

    def show_instance_distribution_invoker(self, request):
        http_info = self._show_instance_distribution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_distribution_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/get-instance-distr",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceDistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_instance_health_report4_api(self, request):
        r"""获取实例健康报告

        获取实例健康报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceHealthReport4Api
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceHealthReport4ApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceHealthReport4ApiResponse`
        """
        http_info = self._show_instance_health_report4_api_http_info(request)
        return self._call_api(**http_info)

    def show_instance_health_report4_api_invoker(self, request):
        http_info = self._show_instance_health_report4_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_health_report4_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/get-instance-health-report",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceHealthReport4ApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def show_instance_info(self, request):
        r"""获取实例信息

        获取实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceInfoResponse`
        """
        http_info = self._show_instance_info_http_info(request)
        return self._call_api(**http_info)

    def show_instance_info_invoker(self, request):
        http_info = self._show_instance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instance/get-instance-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_instance_log_usage(self, request):
        r"""查看实例日志存储使用量

        查看实例日志存储使用量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceLogUsage
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceLogUsageRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceLogUsageResponse`
        """
        http_info = self._show_instance_log_usage_http_info(request)
        return self._call_api(**http_info)

    def show_instance_log_usage_invoker(self, request):
        http_info = self._show_instance_log_usage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_log_usage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clouddba/get-instance-log-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceLogUsageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def show_instance_metric(self, request):
        r"""查询实例指标

        查询实例指标
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceMetric
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceMetricRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceMetricResponse`
        """
        http_info = self._show_instance_metric_http_info(request)
        return self._call_api(**http_info)

    def show_instance_metric_invoker(self, request):
        http_info = self._show_instance_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/query-instance-metric",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceMetricResponse"
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

    def show_instance_nodes_info(self, request):
        r"""获取实例节点信息

        获取实例节点信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceNodesInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceNodesInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceNodesInfoResponse`
        """
        http_info = self._show_instance_nodes_info_http_info(request)
        return self._call_api(**http_info)

    def show_instance_nodes_info_invoker(self, request):
        http_info = self._show_instance_nodes_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_nodes_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instance/get-instance-nodes-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceNodesInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'all_nodes' in local_var_params:
            query_params.append(('all_nodes', local_var_params['all_nodes']))
        if 'show_hidden_nodes' in local_var_params:
            query_params.append(('show_hidden_nodes', local_var_params['show_hidden_nodes']))

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

    def show_instance_top_slow_log(self, request):
        r"""TOP慢SQL列表

        Ins Get Top Slow Log New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceTopSlowLog
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceTopSlowLogRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceTopSlowLogResponse`
        """
        http_info = self._show_instance_top_slow_log_http_info(request)
        return self._call_api(**http_info)

    def show_instance_top_slow_log_invoker(self, request):
        http_info = self._show_instance_top_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_top_slow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/{instance_id}/get-top-slow-log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceTopSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'num' in local_var_params:
            query_params.append(('num', local_var_params['num']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))

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

    def show_is_admin_user_new(self, request):
        r"""是否为IAM主账号

        是否为IAM主账号
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIsAdminUserNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowIsAdminUserNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowIsAdminUserNewResponse`
        """
        http_info = self._show_is_admin_user_new_http_info(request)
        return self._call_api(**http_info)

    def show_is_admin_user_new_invoker(self, request):
        http_info = self._show_is_admin_user_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_is_admin_user_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/is-admin-user",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIsAdminUserNewResponse"
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

    def show_is_signed_protocol(self, request):
        r"""是否签署数据安全协议

        是否签署数据安全协议
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIsSignedProtocol
        :type request: :class:`huaweicloudsdkdas.v3.ShowIsSignedProtocolRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowIsSignedProtocolResponse`
        """
        http_info = self._show_is_signed_protocol_http_info(request)
        return self._call_api(**http_info)

    def show_is_signed_protocol_invoker(self, request):
        http_info = self._show_is_signed_protocol_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_is_signed_protocol_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/binlog-parse/is-signed-protocol",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIsSignedProtocolResponse"
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

    def show_kill_process_task(self, request):
        r"""查询Kill进程任务

        查询Kill进程任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowKillProcessTask
        :type request: :class:`huaweicloudsdkdas.v3.ShowKillProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowKillProcessTaskResponse`
        """
        http_info = self._show_kill_process_task_http_info(request)
        return self._call_api(**http_info)

    def show_kill_process_task_invoker(self, request):
        http_info = self._show_kill_process_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_kill_process_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/query-kill-process-task",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKillProcessTaskResponse"
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

    def show_latest_dead_lock_snapshot4_api(self, request):
        r"""查询最新死锁快照

        查询最新死锁快照
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLatestDeadLockSnapshot4Api
        :type request: :class:`huaweicloudsdkdas.v3.ShowLatestDeadLockSnapshot4ApiRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLatestDeadLockSnapshot4ApiResponse`
        """
        http_info = self._show_latest_dead_lock_snapshot4_api_http_info(request)
        return self._call_api(**http_info)

    def show_latest_dead_lock_snapshot4_api_invoker(self, request):
        http_info = self._show_latest_dead_lock_snapshot4_api_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_latest_dead_lock_snapshot4_api_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/query-latest-dead-lock-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestDeadLockSnapshot4ApiResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_latest_space(self, request):
        r"""获取最新空间

        获取最新空间
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLatestSpace
        :type request: :class:`huaweicloudsdkdas.v3.ShowLatestSpaceRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLatestSpaceResponse`
        """
        http_info = self._show_latest_space_http_info(request)
        return self._call_api(**http_info)

    def show_latest_space_invoker(self, request):
        http_info = self._show_latest_space_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_latest_space_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space/get-latest-space",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestSpaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def show_meta_lock(self, request):
        r"""查询元数据锁

        查询元数据锁
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetaLock
        :type request: :class:`huaweicloudsdkdas.v3.ShowMetaLockRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMetaLockResponse`
        """
        http_info = self._show_meta_lock_http_info(request)
        return self._call_api(**http_info)

    def show_meta_lock_invoker(self, request):
        http_info = self._show_meta_lock_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_meta_lock_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/query-meta-lock",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetaLockResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'thread_id' in local_var_params:
            query_params.append(('thread_id', local_var_params['thread_id']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'lock_status' in local_var_params:
            query_params.append(('lock_status', local_var_params['lock_status']))
        if 'lock_type' in local_var_params:
            query_params.append(('lock_type', local_var_params['lock_type']))

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

    def show_meta_lock_snapshot(self, request):
        r"""查询元数据锁快照

        查询元数据锁快照
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetaLockSnapshot
        :type request: :class:`huaweicloudsdkdas.v3.ShowMetaLockSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMetaLockSnapshotResponse`
        """
        http_info = self._show_meta_lock_snapshot_http_info(request)
        return self._call_api(**http_info)

    def show_meta_lock_snapshot_invoker(self, request):
        http_info = self._show_meta_lock_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_meta_lock_snapshot_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/query-meta-lock-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetaLockSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'thread_id' in local_var_params:
            query_params.append(('thread_id', local_var_params['thread_id']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'lock_status' in local_var_params:
            query_params.append(('lock_status', local_var_params['lock_status']))
        if 'lock_type' in local_var_params:
            query_params.append(('lock_type', local_var_params['lock_type']))

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

    def show_metric_threshold(self, request):
        r"""获取指标阈值

        获取指标阈值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricThreshold
        :type request: :class:`huaweicloudsdkdas.v3.ShowMetricThresholdRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMetricThresholdResponse`
        """
        http_info = self._show_metric_threshold_http_info(request)
        return self._call_api(**http_info)

    def show_metric_threshold_invoker(self, request):
        http_info = self._show_metric_threshold_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_threshold_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/tenant-panel/get-metric-threshold",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricThresholdResponse"
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

    def show_missing_index_script(self, request):
        r"""获取缺失索引脚本

        获取缺失索引脚本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMissingIndexScript
        :type request: :class:`huaweicloudsdkdas.v3.ShowMissingIndexScriptRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMissingIndexScriptResponse`
        """
        http_info = self._show_missing_index_script_http_info(request)
        return self._call_api(**http_info)

    def show_missing_index_script_invoker(self, request):
        http_info = self._show_missing_index_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_missing_index_script_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/get-missing-index-script",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMissingIndexScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))
        if 'equality_columns' in local_var_params:
            query_params.append(('equality_columns', local_var_params['equality_columns']))
        if 'inequality_columns' in local_var_params:
            query_params.append(('inequality_columns', local_var_params['inequality_columns']))
        if 'included_columns' in local_var_params:
            query_params.append(('included_columns', local_var_params['included_columns']))
        if 'object_id' in local_var_params:
            query_params.append(('object_id', local_var_params['object_id']))

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

    def show_missing_index_statistics(self, request):
        r"""获取缺失索引统计

        获取缺失索引统计
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMissingIndexStatistics
        :type request: :class:`huaweicloudsdkdas.v3.ShowMissingIndexStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMissingIndexStatisticsResponse`
        """
        http_info = self._show_missing_index_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_missing_index_statistics_invoker(self, request):
        http_info = self._show_missing_index_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_missing_index_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/get-missing-index-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMissingIndexStatisticsResponse"
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

    def show_missing_index_switch(self, request):
        r"""获取缺失索引开关

        获取缺失索引开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMissingIndexSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ShowMissingIndexSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMissingIndexSwitchResponse`
        """
        http_info = self._show_missing_index_switch_http_info(request)
        return self._call_api(**http_info)

    def show_missing_index_switch_invoker(self, request):
        http_info = self._show_missing_index_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_missing_index_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/get-missing-index-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMissingIndexSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_missing_index_trend(self, request):
        r"""获取缺失索引趋势

        获取缺失索引趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMissingIndexTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowMissingIndexTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMissingIndexTrendResponse`
        """
        http_info = self._show_missing_index_trend_http_info(request)
        return self._call_api(**http_info)

    def show_missing_index_trend_invoker(self, request):
        http_info = self._show_missing_index_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_missing_index_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/missing-index/get-missing-index-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMissingIndexTrendResponse"
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

    def show_node_metrics(self, request):
        r"""查询性能指标

        Query
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNodeMetrics
        :type request: :class:`huaweicloudsdkdas.v3.ShowNodeMetricsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowNodeMetricsResponse`
        """
        http_info = self._show_node_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_node_metrics_invoker(self, request):
        http_info = self._show_node_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_node_metrics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/metrics/{node_id}/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNodeMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_obs_bucket_acl(self, request):
        r"""查询OBS桶ACL

        查询OBS桶ACL
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowObsBucketAcl
        :type request: :class:`huaweicloudsdkdas.v3.ShowObsBucketAclRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowObsBucketAclResponse`
        """
        http_info = self._show_obs_bucket_acl_http_info(request)
        return self._call_api(**http_info)

    def show_obs_bucket_acl_invoker(self, request):
        http_info = self._show_obs_bucket_acl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_obs_bucket_acl_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/obs/bucket/acl",
            "request_type": request.__class__.__name__,
            "response_type": "ShowObsBucketAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'bucket_name' in local_var_params:
            query_params.append(('bucket_name', local_var_params['bucket_name']))

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

    def show_opening_info(self, request):
        r"""获取开通信息

        获取开通信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOpeningInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowOpeningInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowOpeningInfoResponse`
        """
        http_info = self._show_opening_info_http_info(request)
        return self._call_api(**http_info)

    def show_opening_info_invoker(self, request):
        http_info = self._show_opening_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_opening_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clouddba/get-opening-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpeningInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def show_risk_trend(self, request):
        r"""查询风险趋势

        查询风险趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRiskTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowRiskTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowRiskTrendResponse`
        """
        http_info = self._show_risk_trend_http_info(request)
        return self._call_api(**http_info)

    def show_risk_trend_invoker(self, request):
        http_info = self._show_risk_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_risk_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/query-risk-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRiskTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'metric_code' in local_var_params:
            query_params.append(('metric_code', local_var_params['metric_code']))

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

    def show_sensitive_operation_switch_new(self, request):
        r"""查询敏感操作开关

        查询敏感操作开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSensitiveOperationSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowSensitiveOperationSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSensitiveOperationSwitchNewResponse`
        """
        http_info = self._show_sensitive_operation_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_sensitive_operation_switch_new_invoker(self, request):
        http_info = self._show_sensitive_operation_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sensitive_operation_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/sensitive-operation-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSensitiveOperationSwitchNewResponse"
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

    def show_single_metric(self, request):
        r"""获取多节点单指标数据

        Query Single Metric New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleMetric
        :type request: :class:`huaweicloudsdkdas.v3.ShowSingleMetricRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSingleMetricResponse`
        """
        http_info = self._show_single_metric_http_info(request)
        return self._call_api(**http_info)

    def show_single_metric_invoker(self, request):
        http_info = self._show_single_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_single_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/tenant-panel/multi-nodes/single-metric",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSingleMetricResponse"
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

    def show_single_template_trend(self, request):
        r"""查询单个模板趋势

        查询单个模板趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSingleTemplateTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowSingleTemplateTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSingleTemplateTrendResponse`
        """
        http_info = self._show_single_template_trend_http_info(request)
        return self._call_api(**http_info)

    def show_single_template_trend_invoker(self, request):
        http_info = self._show_single_template_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_single_template_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/query-single-tpl-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSingleTemplateTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'interval_millis' in local_var_params:
            query_params.append(('interval_millis', local_var_params['interval_millis']))

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

    def show_slow_log_archive_link(self, request):
        r"""获取慢日志归档链接

        获取慢日志归档链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogArchiveLink
        :type request: :class:`huaweicloudsdkdas.v3.ShowSlowLogArchiveLinkRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSlowLogArchiveLinkResponse`
        """
        http_info = self._show_slow_log_archive_link_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_archive_link_invoker(self, request):
        http_info = self._show_slow_log_archive_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_archive_link_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-archive-link",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogArchiveLinkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'archive_id' in local_var_params:
            query_params.append(('archive_id', local_var_params['archive_id']))

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

    def show_slow_log_detail_sample(self, request):
        r"""获取慢日志明细样例

        获取指定SQL模板的慢日志明细样例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogDetailSample
        :type request: :class:`huaweicloudsdkdas.v3.ShowSlowLogDetailSampleRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSlowLogDetailSampleResponse`
        """
        http_info = self._show_slow_log_detail_sample_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_detail_sample_invoker(self, request):
        http_info = self._show_slow_log_detail_sample_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_detail_sample_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-detail-sample",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogDetailSampleResponse"
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
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'sql_template_id' in local_var_params:
            query_params.append(('sql_template_id', local_var_params['sql_template_id']))
        if 'with_db' in local_var_params:
            query_params.append(('with_db', local_var_params['with_db']))

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

    def show_slow_log_statistics_new(self, request):
        r"""获取慢日志统计

        获取慢日志统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogStatisticsNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowSlowLogStatisticsNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSlowLogStatisticsNewResponse`
        """
        http_info = self._show_slow_log_statistics_new_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_statistics_new_invoker(self, request):
        http_info = self._show_slow_log_statistics_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_statistics_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogStatisticsNewResponse"
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

    def show_slow_log_top_info_new(self, request):
        r"""获取慢日志Top信息

        获取慢日志Top用户、Top IP、Top数据库信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogTopInfoNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowSlowLogTopInfoNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSlowLogTopInfoNewResponse`
        """
        http_info = self._show_slow_log_top_info_new_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_top_info_new_invoker(self, request):
        http_info = self._show_slow_log_top_info_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_top_info_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-top-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogTopInfoNewResponse"
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

    def show_slow_log_trend_new(self, request):
        r"""获取慢日志趋势

        获取慢日志趋势数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogTrendNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowSlowLogTrendNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSlowLogTrendNewResponse`
        """
        http_info = self._show_slow_log_trend_new_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_trend_new_invoker(self, request):
        http_info = self._show_slow_log_trend_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_trend_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogTrendNewResponse"
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

    def show_space_trend(self, request):
        r"""获取空间趋势

        获取空间趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSpaceTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowSpaceTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSpaceTrendResponse`
        """
        http_info = self._show_space_trend_http_info(request)
        return self._call_api(**http_info)

    def show_space_trend_invoker(self, request):
        http_info = self._show_space_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_space_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space/get-space-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSpaceTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def show_sql_limiting_info(self, request):
        r"""使用SQL限流信息

        使用SQL限流信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitingInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingInfoResponse`
        """
        http_info = self._show_sql_limiting_info_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limiting_info_invoker(self, request):
        http_info = self._show_sql_limiting_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limiting_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/use-sql-limiting-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitingInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_sql_limiting_job_info(self, request):
        r"""获取SQL限流任务信息

        获取SQL限流任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitingJobInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingJobInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingJobInfoResponse`
        """
        http_info = self._show_sql_limiting_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limiting_job_info_invoker(self, request):
        http_info = self._show_sql_limiting_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limiting_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/get-sql-limiting-job-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitingJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
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

    def show_sql_limiting_record(self, request):
        r"""获取SQL限流记录

        获取SQL限流记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitingRecord
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingRecordRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingRecordResponse`
        """
        http_info = self._show_sql_limiting_record_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limiting_record_invoker(self, request):
        http_info = self._show_sql_limiting_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limiting_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/get-sql-limiting-record",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitingRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'sql_type' in local_var_params:
            query_params.append(('sql_type', local_var_params['sql_type']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'query_id' in local_var_params:
            query_params.append(('query_id', local_var_params['query_id']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))

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

    def show_sql_template_trend(self, request):
        r"""查询SQL模板趋势

        查询SQL模板趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlTemplateTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlTemplateTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlTemplateTrendResponse`
        """
        http_info = self._show_sql_template_trend_http_info(request)
        return self._call_api(**http_info)

    def show_sql_template_trend_invoker(self, request):
        http_info = self._show_sql_template_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_template_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/query-sql-tpl-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlTemplateTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'interval_millis' in local_var_params:
            query_params.append(('interval_millis', local_var_params['interval_millis']))

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

    def show_support_key_string(self, request):
        r"""支持的关键字

        支持的关键字
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSupportKeyString
        :type request: :class:`huaweicloudsdkdas.v3.ShowSupportKeyStringRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSupportKeyStringResponse`
        """
        http_info = self._show_support_key_string_http_info(request)
        return self._call_api(**http_info)

    def show_support_key_string_invoker(self, request):
        http_info = self._show_support_key_string_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_support_key_string_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-sql-limiting/support-key-string",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSupportKeyStringResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_top_data(self, request):
        r"""获取Top数据

        获取Top数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopData
        :type request: :class:`huaweicloudsdkdas.v3.ShowTopDataRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTopDataResponse`
        """
        http_info = self._show_top_data_http_info(request)
        return self._call_api(**http_info)

    def show_top_data_invoker(self, request):
        http_info = self._show_top_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_top_data_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space/get-top-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def show_top_slow_log(self, request):
        r"""获取Top慢日志

        获取Top慢日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopSlowLog
        :type request: :class:`huaweicloudsdkdas.v3.ShowTopSlowLogRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTopSlowLogResponse`
        """
        http_info = self._show_top_slow_log_http_info(request)
        return self._call_api(**http_info)

    def show_top_slow_log_invoker(self, request):
        http_info = self._show_top_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_top_slow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tenant-panel/get-top-slow-log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num' in local_var_params:
            query_params.append(('num', local_var_params['num']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))

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

    def show_top_trend(self, request):
        r"""查询Top库表趋势

        Console Get Top Trend New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowTopTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTopTrendResponse`
        """
        http_info = self._show_top_trend_http_info(request)
        return self._call_api(**http_info)

    def show_top_trend_invoker(self, request):
        http_info = self._show_top_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_top_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space/get-top-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'object_name' in local_var_params:
            query_params.append(('object_name', local_var_params['object_name']))
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def show_tuning_result(self, request):
        r"""获取调优结果

        获取调优结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTuningResult
        :type request: :class:`huaweicloudsdkdas.v3.ShowTuningResultRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTuningResultResponse`
        """
        http_info = self._show_tuning_result_http_info(request)
        return self._call_api(**http_info)

    def show_tuning_result_invoker(self, request):
        http_info = self._show_tuning_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tuning_result_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/tuning/get-tuning-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTuningResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_waiting_locks_snapshot(self, request):
        r"""查询InnoDB锁等待快照

        查询InnoDB锁等待快照
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWaitingLocksSnapshot
        :type request: :class:`huaweicloudsdkdas.v3.ShowWaitingLocksSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowWaitingLocksSnapshotResponse`
        """
        http_info = self._show_waiting_locks_snapshot_http_info(request)
        return self._call_api(**http_info)

    def show_waiting_locks_snapshot_invoker(self, request):
        http_info = self._show_waiting_locks_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_waiting_locks_snapshot_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/query-waiting-locks-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWaitingLocksSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_wdr_snapshot(self, request):
        r"""获取WDR快照列表

        获取WDR快照列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWdrSnapshot
        :type request: :class:`huaweicloudsdkdas.v3.ShowWdrSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowWdrSnapshotResponse`
        """
        http_info = self._show_wdr_snapshot_http_info(request)
        return self._call_api(**http_info)

    def show_wdr_snapshot_invoker(self, request):
        http_info = self._show_wdr_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_wdr_snapshot_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/wdr/get-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWdrSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def sign_protocol_new(self, request):
        r"""签署数据安全协议

        签署数据安全协议
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SignProtocolNew
        :type request: :class:`huaweicloudsdkdas.v3.SignProtocolNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SignProtocolNewResponse`
        """
        http_info = self._sign_protocol_new_http_info(request)
        return self._call_api(**http_info)

    def sign_protocol_new_invoker(self, request):
        http_info = self._sign_protocol_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sign_protocol_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/binlog-parse/sign-protocol",
            "request_type": request.__class__.__name__,
            "response_type": "SignProtocolNewResponse"
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

    def stop_binlog_task(self, request):
        r"""停止binlog解析任务

        停止binlog解析任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopBinlogTask
        :type request: :class:`huaweicloudsdkdas.v3.StopBinlogTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.StopBinlogTaskResponse`
        """
        http_info = self._stop_binlog_task_http_info(request)
        return self._call_api(**http_info)

    def stop_binlog_task_invoker(self, request):
        http_info = self._stop_binlog_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_binlog_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/binlog-parse/stop-task",
            "request_type": request.__class__.__name__,
            "response_type": "StopBinlogTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def stop_kill_task(self, request):
        r"""终止自动kill会话任务

        Stop Kill Task
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopKillTask
        :type request: :class:`huaweicloudsdkdas.v3.StopKillTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.StopKillTaskResponse`
        """
        http_info = self._stop_kill_task_http_info(request)
        return self._call_api(**http_info)

    def stop_kill_task_invoker(self, request):
        http_info = self._stop_kill_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_kill_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/terminate-kill-process-task",
            "request_type": request.__class__.__name__,
            "response_type": "StopKillTaskResponse"
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

    def subscribe_instance_report_new(self, request):
        r"""订阅实例报告

        订阅实例报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeInstanceReportNew
        :type request: :class:`huaweicloudsdkdas.v3.SubscribeInstanceReportNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SubscribeInstanceReportNewResponse`
        """
        http_info = self._subscribe_instance_report_new_http_info(request)
        return self._call_api(**http_info)

    def subscribe_instance_report_new_invoker(self, request):
        http_info = self._subscribe_instance_report_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _subscribe_instance_report_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/subscribe-instance-report",
            "request_type": request.__class__.__name__,
            "response_type": "SubscribeInstanceReportNewResponse"
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

    def switch_sql_limiting_rule_new(self, request):
        r"""切换SQL限流规则

        切换SQL限流规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSqlLimitingRuleNew
        :type request: :class:`huaweicloudsdkdas.v3.SwitchSqlLimitingRuleNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SwitchSqlLimitingRuleNewResponse`
        """
        http_info = self._switch_sql_limiting_rule_new_http_info(request)
        return self._call_api(**http_info)

    def switch_sql_limiting_rule_new_invoker(self, request):
        http_info = self._switch_sql_limiting_rule_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_sql_limiting_rule_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/switch-sql-limiting-rule",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchSqlLimitingRuleNewResponse"
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

    def sync_connections_new(self, request):
        r"""同步连接

        同步连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncConnectionsNew
        :type request: :class:`huaweicloudsdkdas.v3.SyncConnectionsNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SyncConnectionsNewResponse`
        """
        http_info = self._sync_connections_new_http_info(request)
        return self._call_api(**http_info)

    def sync_connections_new_invoker(self, request):
        http_info = self._sync_connections_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sync_connections_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/sync-connections",
            "request_type": request.__class__.__name__,
            "response_type": "SyncConnectionsNewResponse"
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

    def synchronize_instance_list_new(self, request):
        r"""同步实例列表

        同步实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SynchronizeInstanceListNew
        :type request: :class:`huaweicloudsdkdas.v3.SynchronizeInstanceListNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SynchronizeInstanceListNewResponse`
        """
        http_info = self._synchronize_instance_list_new_http_info(request)
        return self._call_api(**http_info)

    def synchronize_instance_list_new_invoker(self, request):
        http_info = self._synchronize_instance_list_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _synchronize_instance_list_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/synchronize-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "SynchronizeInstanceListNewResponse"
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

    def unsubscribe_instance_report_new(self, request):
        r"""取消订阅实例报告

        取消订阅实例报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnsubscribeInstanceReportNew
        :type request: :class:`huaweicloudsdkdas.v3.UnsubscribeInstanceReportNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UnsubscribeInstanceReportNewResponse`
        """
        http_info = self._unsubscribe_instance_report_new_http_info(request)
        return self._call_api(**http_info)

    def unsubscribe_instance_report_new_invoker(self, request):
        http_info = self._unsubscribe_instance_report_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unsubscribe_instance_report_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/unsubscribe-instance-report",
            "request_type": request.__class__.__name__,
            "response_type": "UnsubscribeInstanceReportNewResponse"
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

    def update_instance_config(self, request):
        r"""设置实例配置

        Space Set Config New
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfig
        :type request: :class:`huaweicloudsdkdas.v3.UpdateInstanceConfigRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateInstanceConfigResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/config/set-config",
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_search_path_flag(self, request):
        r"""设置searchpath开关

        设置searchpath开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSearchPathFlag
        :type request: :class:`huaweicloudsdkdas.v3.UpdateSearchPathFlagRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateSearchPathFlagResponse`
        """
        http_info = self._update_search_path_flag_http_info(request)
        return self._call_api(**http_info)

    def update_search_path_flag_invoker(self, request):
        http_info = self._update_search_path_flag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_search_path_flag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/clouddba-edit-search-path-flag",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSearchPathFlagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def update_sensitive_operation_switch(self, request):
        r"""敏感操作开关

        敏感操作开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSensitiveOperationSwitch
        :type request: :class:`huaweicloudsdkdas.v3.UpdateSensitiveOperationSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateSensitiveOperationSwitchResponse`
        """
        http_info = self._update_sensitive_operation_switch_http_info(request)
        return self._call_api(**http_info)

    def update_sensitive_operation_switch_invoker(self, request):
        http_info = self._update_sensitive_operation_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sensitive_operation_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/sensitive-operation-switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSensitiveOperationSwitchResponse"
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

    def update_shared_info_new(self, request):
        r"""更新共享信息

        更新共享信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSharedInfoNew
        :type request: :class:`huaweicloudsdkdas.v3.UpdateSharedInfoNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateSharedInfoNewResponse`
        """
        http_info = self._update_shared_info_new_http_info(request)
        return self._call_api(**http_info)

    def update_shared_info_new_invoker(self, request):
        http_info = self._update_shared_info_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_shared_info_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/update-shared-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSharedInfoNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def update_sql_limiting_record_new(self, request):
        r"""更新SQL限流记录

        更新SQL限流记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlLimitingRecordNew
        :type request: :class:`huaweicloudsdkdas.v3.UpdateSqlLimitingRecordNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateSqlLimitingRecordNewResponse`
        """
        http_info = self._update_sql_limiting_record_new_http_info(request)
        return self._call_api(**http_info)

    def update_sql_limiting_record_new_invoker(self, request):
        http_info = self._update_sql_limiting_record_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sql_limiting_record_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/update-sql-limiting-record",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSqlLimitingRecordNewResponse"
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

    def verify_connection_new(self, request):
        r"""验证数据库实例连接

        验证数据库实例连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for VerifyConnectionNew
        :type request: :class:`huaweicloudsdkdas.v3.VerifyConnectionNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.VerifyConnectionNewResponse`
        """
        http_info = self._verify_connection_new_http_info(request)
        return self._call_api(**http_info)

    def verify_connection_new_invoker(self, request):
        http_info = self._verify_connection_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _verify_connection_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/verify-connection",
            "request_type": request.__class__.__name__,
            "response_type": "VerifyConnectionNewResponse"
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

    def add_email_template(self, request):
        r"""新增邮件模板

        新增邮件模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddEmailTemplate
        :type request: :class:`huaweicloudsdkdas.v3.AddEmailTemplateRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddEmailTemplateResponse`
        """
        http_info = self._add_email_template_http_info(request)
        return self._call_api(**http_info)

    def add_email_template_invoker(self, request):
        http_info = self._add_email_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_email_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/email-template",
            "request_type": request.__class__.__name__,
            "response_type": "AddEmailTemplateResponse"
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

    def add_full_sql_task(self, request):
        r"""创建全量SQL明细解析任务

        创建全量SQL明细解析任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddFullSqlTask
        :type request: :class:`huaweicloudsdkdas.v3.AddFullSqlTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddFullSqlTaskResponse`
        """
        http_info = self._add_full_sql_task_http_info(request)
        return self._call_api(**http_info)

    def add_full_sql_task_invoker(self, request):
        http_info = self._add_full_sql_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_full_sql_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/full-sql/add-task",
            "request_type": request.__class__.__name__,
            "response_type": "AddFullSqlTaskResponse"
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

    def add_instance_group(self, request):
        r"""新增实例组

        新增实例组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddInstanceGroup
        :type request: :class:`huaweicloudsdkdas.v3.AddInstanceGroupRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddInstanceGroupResponse`
        """
        http_info = self._add_instance_group_http_info(request)
        return self._call_api(**http_info)

    def add_instance_group_invoker(self, request):
        http_info = self._add_instance_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_instance_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/instance-group",
            "request_type": request.__class__.__name__,
            "response_type": "AddInstanceGroupResponse"
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

    def add_instance_to_group(self, request):
        r"""将实例添加到实例组

        将实例添加到实例组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddInstanceToGroup
        :type request: :class:`huaweicloudsdkdas.v3.AddInstanceToGroupRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddInstanceToGroupResponse`
        """
        http_info = self._add_instance_to_group_http_info(request)
        return self._call_api(**http_info)

    def add_instance_to_group_invoker(self, request):
        http_info = self._add_instance_to_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_instance_to_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/add-instance-to-group",
            "request_type": request.__class__.__name__,
            "response_type": "AddInstanceToGroupResponse"
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

    def add_sql_limiting_record_new(self, request):
        r"""新增SQL限流规则

        新增SQL限流规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddSqlLimitingRecordNew
        :type request: :class:`huaweicloudsdkdas.v3.AddSqlLimitingRecordNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.AddSqlLimitingRecordNewResponse`
        """
        http_info = self._add_sql_limiting_record_new_http_info(request)
        return self._call_api(**http_info)

    def add_sql_limiting_record_new_invoker(self, request):
        http_info = self._add_sql_limiting_record_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_sql_limiting_record_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/add-sql-limiting-record",
            "request_type": request.__class__.__name__,
            "response_type": "AddSqlLimitingRecordNewResponse"
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

    def batch_delete_connection_new(self, request):
        r"""批量删除连接

        批量删除连接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteConnectionNew
        :type request: :class:`huaweicloudsdkdas.v3.BatchDeleteConnectionNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.BatchDeleteConnectionNewResponse`
        """
        http_info = self._batch_delete_connection_new_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_connection_new_invoker(self, request):
        http_info = self._batch_delete_connection_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_connection_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/batch-delete-connections",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteConnectionNewResponse"
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

    def batch_send_email(self, request):
        r"""批量发送邮件

        批量发送邮件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSendEmail
        :type request: :class:`huaweicloudsdkdas.v3.BatchSendEmailRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.BatchSendEmailResponse`
        """
        http_info = self._batch_send_email_http_info(request)
        return self._call_api(**http_info)

    def batch_send_email_invoker(self, request):
        http_info = self._batch_send_email_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_send_email_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/batch-send-email",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSendEmailResponse"
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

    def batch_subscribe_report(self, request):
        r"""批量订阅/取消订阅

        批量订阅/取消订阅
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchSubscribeReport
        :type request: :class:`huaweicloudsdkdas.v3.BatchSubscribeReportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.BatchSubscribeReportResponse`
        """
        http_info = self._batch_subscribe_report_http_info(request)
        return self._call_api(**http_info)

    def batch_subscribe_report_invoker(self, request):
        http_info = self._batch_subscribe_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_subscribe_report_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/batch-subscribe",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSubscribeReportResponse"
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

    def cancel_share_new(self, request):
        r"""取消共享链接

        取消共享链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelShareNew
        :type request: :class:`huaweicloudsdkdas.v3.CancelShareNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CancelShareNewResponse`
        """
        http_info = self._cancel_share_new_http_info(request)
        return self._call_api(**http_info)

    def cancel_share_new_invoker(self, request):
        http_info = self._cancel_share_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_share_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/connections/cancel-share",
            "request_type": request.__class__.__name__,
            "response_type": "CancelShareNewResponse"
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

    def change_charge_mode(self, request):
        r"""设置实例付费/免费模式

        设置实例付费/免费模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeChargeMode
        :type request: :class:`huaweicloudsdkdas.v3.ChangeChargeModeRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeChargeModeResponse`
        """
        http_info = self._change_charge_mode_http_info(request)
        return self._call_api(**http_info)

    def change_charge_mode_invoker(self, request):
        http_info = self._change_charge_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_charge_mode_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/cloud-dba/change-payment-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeChargeModeResponse"
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

    def change_dead_lock_switch_new(self, request):
        r"""修改死锁开关

        修改死锁开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDeadLockSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ChangeDeadLockSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeDeadLockSwitchNewResponse`
        """
        http_info = self._change_dead_lock_switch_new_http_info(request)
        return self._call_api(**http_info)

    def change_dead_lock_switch_new_invoker(self, request):
        http_info = self._change_dead_lock_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_dead_lock_switch_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dead-lock/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDeadLockSwitchNewResponse"
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

    def change_full_dead_lock_switch(self, request):
        r"""设置全量死锁开关

        设置全量死锁开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeFullDeadLockSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ChangeFullDeadLockSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeFullDeadLockSwitchResponse`
        """
        http_info = self._change_full_dead_lock_switch_http_info(request)
        return self._call_api(**http_info)

    def change_full_dead_lock_switch_invoker(self, request):
        http_info = self._change_full_dead_lock_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_full_dead_lock_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/set-fulldeadlock-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeFullDeadLockSwitchResponse"
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

    def change_payment_mode_new(self, request):
        r"""设置实例付费/免费模式

        设置实例付费/免费模式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePaymentModeNew
        :type request: :class:`huaweicloudsdkdas.v3.ChangePaymentModeNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangePaymentModeNewResponse`
        """
        http_info = self._change_payment_mode_new_http_info(request)
        return self._call_api(**http_info)

    def change_payment_mode_new_invoker(self, request):
        http_info = self._change_payment_mode_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_payment_mode_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clouddba/change-payment-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ChangePaymentModeNewResponse"
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

    def change_sql_limit_switch_status(self, request):
        r"""设置SQL限流开关状态

        设置SQL限流开关状态。目前仅支持MySQL数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSqlLimitSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ChangeSqlLimitSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeSqlLimitSwitchStatusResponse`
        """
        http_info = self._change_sql_limit_switch_status_http_info(request)
        return self._call_api(**http_info)

    def change_sql_limit_switch_status_invoker(self, request):
        http_info = self._change_sql_limit_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_sql_limit_switch_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSqlLimitSwitchStatusResponse"
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

    def change_sql_switch(self, request):
        r"""开启/关闭全量SQL、慢SQL开关

        打开或者关闭DAS收集全量SQL开关，开启后，实例的性能损耗在5%以内。开启全量SQL后，本服务会对SQL的文本内容进行存储，以便进行分析。用户可自行设置全量SQL的保存时间范围，到期后会自动删除；如果未设置，数据默认保留7天。
        打开或者关闭DAS收集慢SQL开关。开启慢SQL后，本服务会对慢SQL的文本内容进行存储，以便进行分析。用户可自行设置慢SQL的保存时间范围，到期后会自动删除；如果未设置，数据默认保留7天。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSqlSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ChangeSqlSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeSqlSwitchResponse`
        """
        http_info = self._change_sql_switch_http_info(request)
        return self._call_api(**http_info)

    def change_sql_switch_invoker(self, request):
        http_info = self._change_sql_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_sql_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSqlSwitchResponse"
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

    def change_transaction_switch_status(self, request):
        r"""开启/关闭历史事务开关

        开启/关闭历史事务开关，仅支持MySQL引擎，并且依赖开启全量SQL或者慢SQL功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeTransactionSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ChangeTransactionSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeTransactionSwitchStatusResponse`
        """
        http_info = self._change_transaction_switch_status_http_info(request)
        return self._call_api(**http_info)

    def change_transaction_switch_status_invoker(self, request):
        http_info = self._change_transaction_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_transaction_switch_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/transaction/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeTransactionSwitchStatusResponse"
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

    def check_credential(self, request):
        r"""测试AK/SK

        测试AK/SK，测试用户AK/SK能否正常访问OBS桶。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckCredential
        :type request: :class:`huaweicloudsdkdas.v3.CheckCredentialRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CheckCredentialResponse`
        """
        http_info = self._check_credential_http_info(request)
        return self._call_api(**http_info)

    def check_credential_invoker(self, request):
        http_info = self._check_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_credential_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/health-report/check-credential",
            "request_type": request.__class__.__name__,
            "response_type": "CheckCredentialResponse"
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

    def check_credential_for_batch_inspection(self, request):
        r"""测试AK/SK

        测试AK/SK，测试用户AK/SK能否正常访问OBS桶。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckCredentialForBatchInspection
        :type request: :class:`huaweicloudsdkdas.v3.CheckCredentialForBatchInspectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CheckCredentialForBatchInspectionResponse`
        """
        http_info = self._check_credential_for_batch_inspection_http_info(request)
        return self._call_api(**http_info)

    def check_credential_for_batch_inspection_invoker(self, request):
        http_info = self._check_credential_for_batch_inspection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_credential_for_batch_inspection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/check-credential",
            "request_type": request.__class__.__name__,
            "response_type": "CheckCredentialForBatchInspectionResponse"
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

    def create_health_report_task(self, request):
        r"""创建实例健康诊断任务

        创建实例健康诊断任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHealthReportTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateHealthReportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateHealthReportTaskResponse`
        """
        http_info = self._create_health_report_task_http_info(request)
        return self._call_api(**http_info)

    def create_health_report_task_invoker(self, request):
        http_info = self._create_health_report_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_health_report_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/create-instance-health-report-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHealthReportTaskResponse"
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

    def create_history_transaction_export_task(self, request):
        r"""创建导出历史事务任务

        DAS收集历史事务开关打开后，支持创建一次性导出指定时间范围内的历史事务数据任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHistoryTransactionExportTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateHistoryTransactionExportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateHistoryTransactionExportTaskResponse`
        """
        http_info = self._create_history_transaction_export_task_http_info(request)
        return self._call_api(**http_info)

    def create_history_transaction_export_task_invoker(self, request):
        http_info = self._create_history_transaction_export_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_history_transaction_export_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/create-export-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHistoryTransactionExportTaskResponse"
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

    def create_snapshots(self, request):
        r"""创建快照

        创建快照
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSnapshots
        :type request: :class:`huaweicloudsdkdas.v3.CreateSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSnapshotsResponse`
        """
        http_info = self._create_snapshots_http_info(request)
        return self._call_api(**http_info)

    def create_snapshots_invoker(self, request):
        http_info = self._create_snapshots_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_snapshots_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/create-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSnapshotsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def create_space_analysis_task(self, request):
        r"""创建空间分析任务

        创建空间分析任务，如触发重新分析，支持MySQL和GaussDB(for MySQL)引擎
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSpaceAnalysisTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateSpaceAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSpaceAnalysisTaskResponse`
        """
        http_info = self._create_space_analysis_task_http_info(request)
        return self._call_api(**http_info)

    def create_space_analysis_task_invoker(self, request):
        http_info = self._create_space_analysis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_space_analysis_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSpaceAnalysisTaskResponse"
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

    def create_sql_limit_rules(self, request):
        r"""创建SQL限流规则

        添加SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。
        MySQL使用限制如下：
        1.规则举例详细说明：例如关键字是\&quot;select~a\&quot;, 含义为：select以及a为该并发控制所包含的两个关键字，~为关键字间隔符，即若执行SQL命令包含select与a两个关键字视为命中此条并发控制规则。
        2.当SQL语句匹配多条限流规则时，优先生效最新添加的规则，之前的规则不再生效。
        3.限流规则关键字有顺序要求，只会按顺序匹配。如：a~and~b 只会匹配 xxx a&gt;1 and b&gt;2，而不会匹配 xxx b&gt;2 and a&gt;1。
        4.关键字可能大小写敏感，请执行 \&quot;show variables like &#39;rds_sqlfilter_case_sensitive&#39;或者到实例参数设置页面进行确认。
        5.部分版本只读实例不允许设置限流规则，如果要设置限流规则，请到主实例上进行添加。
        6.系统表不限制、不涉及数据查询的不限制、root账号在特定版本下不限制。
        PostgreSQL使用限制如下：
        1.无法添加相同QUERY_ID或SQL语句的规则。
        2.使用SQL语句添加规则时，需要确保存在数据库表，如：select * from test，需要确保数据库中有test表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.CreateSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSqlLimitRulesResponse`
        """
        http_info = self._create_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def create_sql_limit_rules_invoker(self, request):
        http_info = self._create_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlLimitRulesResponse"
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

    def create_tuning(self, request):
        r"""执行SQL诊断

        执行SQL诊断，
        用于用户执行SQL诊断。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTuning
        :type request: :class:`huaweicloudsdkdas.v3.CreateTuningRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateTuningResponse`
        """
        http_info = self._create_tuning_http_info(request)
        return self._call_api(**http_info)

    def create_tuning_invoker(self, request):
        http_info = self._create_tuning_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tuning_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/tuning/create-tuning",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTuningResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_db_user(self, request):
        r"""删除数据库用户

        删除注册在DAS里的数据库用户。此接口只是将注册的数据库用户在DAS系统里删除，不会真正删除数据库用户对象。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbUser
        :type request: :class:`huaweicloudsdkdas.v3.DeleteDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteDbUserResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_user_id' in local_var_params:
            path_params['db_user_id'] = local_var_params['db_user_id']

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

    def delete_email_template(self, request):
        r"""删除邮件模板

        删除邮件模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEmailTemplate
        :type request: :class:`huaweicloudsdkdas.v3.DeleteEmailTemplateRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteEmailTemplateResponse`
        """
        http_info = self._delete_email_template_http_info(request)
        return self._call_api(**http_info)

    def delete_email_template_invoker(self, request):
        http_info = self._delete_email_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_email_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/batch-inspection/email-template",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEmailTemplateResponse"
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

    def delete_history_transaction_export_task(self, request):
        r"""删除导出历史事务任务

        DAS收集历史事务开关打开后，删除历史事务导出任务记录对应的OBS文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHistoryTransactionExportTask
        :type request: :class:`huaweicloudsdkdas.v3.DeleteHistoryTransactionExportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteHistoryTransactionExportTaskResponse`
        """
        http_info = self._delete_history_transaction_export_task_http_info(request)
        return self._call_api(**http_info)

    def delete_history_transaction_export_task_invoker(self, request):
        http_info = self._delete_history_transaction_export_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_history_transaction_export_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/delete-export-task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHistoryTransactionExportTaskResponse"
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

    def delete_instance_group(self, request):
        r"""删除实例组

        删除实例组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstanceGroup
        :type request: :class:`huaweicloudsdkdas.v3.DeleteInstanceGroupRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteInstanceGroupResponse`
        """
        http_info = self._delete_instance_group_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_group_invoker(self, request):
        http_info = self._delete_instance_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instance_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/batch-inspection/instance-group",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceGroupResponse"
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

    def delete_process(self, request):
        r"""查杀会话

        查杀会话。支持按照用户、数据库、会话列表查杀会话，三个条件至少指定一个。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProcess
        :type request: :class:`huaweicloudsdkdas.v3.DeleteProcessRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteProcessResponse`
        """
        http_info = self._delete_process_http_info(request)
        return self._call_api(**http_info)

    def delete_process_invoker(self, request):
        http_info = self._delete_process_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_process_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/process",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProcessResponse"
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

    def delete_sql_limit_rules(self, request):
        r"""删除SQL限流规则

        删除SQL限流规则。目前仅支持MySQL和PostgreSQL数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.DeleteSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteSqlLimitRulesResponse`
        """
        http_info = self._delete_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def delete_sql_limit_rules_invoker(self, request):
        http_info = self._delete_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlLimitRulesResponse"
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

    def export_full_sql_details(self, request):
        r"""导出全量SQL明细

        全量SQL开关打开后，创建SQL洞察任务，支持按节点、用户名、数据库、操作类型等导出全量SQL明细数据。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportFullSqlDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportFullSqlDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportFullSqlDetailsResponse`
        """
        http_info = self._export_full_sql_details_http_info(request)
        return self._call_api(**http_info)

    def export_full_sql_details_invoker(self, request):
        http_info = self._export_full_sql_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_full_sql_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/full-sql-search",
            "request_type": request.__class__.__name__,
            "response_type": "ExportFullSqlDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'task_ids' in local_var_params:
            query_params.append(('task_ids', local_var_params['task_ids']))
            collection_formats['task_ids'] = 'csv'
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'fuzzy' in local_var_params:
            query_params.append(('fuzzy', local_var_params['fuzzy']))
        if 'user_list' in local_var_params:
            query_params.append(('user_list', local_var_params['user_list']))
        if 'db_list' in local_var_params:
            query_params.append(('db_list', local_var_params['db_list']))
        if 'operation_list' in local_var_params:
            query_params.append(('operation_list', local_var_params['operation_list']))
        if 'client_ip_list' in local_var_params:
            query_params.append(('client_ip_list', local_var_params['client_ip_list']))
        if 'thread_id_list' in local_var_params:
            query_params.append(('thread_id_list', local_var_params['thread_id_list']))
        if 'trx_id_list' in local_var_params:
            query_params.append(('trx_id_list', local_var_params['trx_id_list']))
        if 'session_id_list' in local_var_params:
            query_params.append(('session_id_list', local_var_params['session_id_list']))
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
        if 'sql_template_ids' in local_var_params:
            query_params.append(('sql_template_ids', local_var_params['sql_template_ids']))
        if 'cost_min' in local_var_params:
            query_params.append(('cost_min', local_var_params['cost_min']))
        if 'cost_max' in local_var_params:
            query_params.append(('cost_max', local_var_params['cost_max']))
        if 'scan_min' in local_var_params:
            query_params.append(('scan_min', local_var_params['scan_min']))
        if 'scan_max' in local_var_params:
            query_params.append(('scan_max', local_var_params['scan_max']))
        if 'affect_min' in local_var_params:
            query_params.append(('affect_min', local_var_params['affect_min']))
        if 'affect_max' in local_var_params:
            query_params.append(('affect_max', local_var_params['affect_max']))
        if 'return_min' in local_var_params:
            query_params.append(('return_min', local_var_params['return_min']))
        if 'return_max' in local_var_params:
            query_params.append(('return_max', local_var_params['return_max']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
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

    def export_slow_query_logs(self, request):
        r"""导出慢SQL数据

        DAS收集慢SQL开关打开后，一次性导出指定时间范围内的慢SQL数据，支持分页滚动获取。免费实例仅支持查看最近一小时数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowQueryLogs
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowQueryLogsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowQueryLogsResponse`
        """
        http_info = self._export_slow_query_logs_http_info(request)
        return self._call_api(**http_info)

    def export_slow_query_logs_invoker(self, request):
        http_info = self._export_slow_query_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_query_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-query-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowQueryLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def export_slow_sql_statistics(self, request):
        r"""导出慢SQL统计数据

        慢SQL开关打开后，导出慢SQL统计数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowSqlStatistics
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowSqlStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowSqlStatisticsResponse`
        """
        http_info = self._export_slow_sql_statistics_http_info(request)
        return self._call_api(**http_info)

    def export_slow_sql_statistics_invoker(self, request):
        http_info = self._export_slow_sql_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_sql_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-sql-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowSqlStatisticsResponse"
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

    def export_slow_sql_templates_details(self, request):
        r"""导出慢SQL模板列表

        慢SQL开关打开后，导出慢SQL模板列表。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowSqlTemplatesDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTemplatesDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTemplatesDetailsResponse`
        """
        http_info = self._export_slow_sql_templates_details_http_info(request)
        return self._call_api(**http_info)

    def export_slow_sql_templates_details_invoker(self, request):
        http_info = self._export_slow_sql_templates_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_sql_templates_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-sql-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowSqlTemplatesDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
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

    def export_slow_sql_trend_details(self, request):
        r"""导出慢SQL数量趋势

        慢SQL开关打开后，导出慢SQL数量趋势。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowSqlTrendDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTrendDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTrendDetailsResponse`
        """
        http_info = self._export_slow_sql_trend_details_http_info(request)
        return self._call_api(**http_info)

    def export_slow_sql_trend_details_invoker(self, request):
        http_info = self._export_slow_sql_trend_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_sql_trend_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-sql-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowSqlTrendDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
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

    def export_sql_statements(self, request):
        r"""导出全量SQL

        全量SQL开关打开后，一次性导出指定时间范围内的全量SQL数据，支持分页滚动获取。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSqlStatements
        :type request: :class:`huaweicloudsdkdas.v3.ExportSqlStatementsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSqlStatementsResponse`
        """
        http_info = self._export_sql_statements_http_info(request)
        return self._call_api(**http_info)

    def export_sql_statements_invoker(self, request):
        http_info = self._export_sql_statements_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_sql_statements_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-statements",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSqlStatementsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def export_top_risk_instances(self, request):
        r"""导出TOP风险实例列表

        导出TOP风险实例列表，支持查看最近24小时数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTopRiskInstances
        :type request: :class:`huaweicloudsdkdas.v3.ExportTopRiskInstancesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportTopRiskInstancesResponse`
        """
        http_info = self._export_top_risk_instances_http_info(request)
        return self._call_api(**http_info)

    def export_top_risk_instances_invoker(self, request):
        http_info = self._export_top_risk_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_top_risk_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/top-risk",
            "request_type": request.__class__.__name__,
            "response_type": "ExportTopRiskInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'num' in local_var_params:
            query_params.append(('num', local_var_params['num']))
        if 'metric_code' in local_var_params:
            query_params.append(('metric_code', local_var_params['metric_code']))

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

    def export_top_sql_templates_details(self, request):
        r"""导出TopSQL模板列表

        TopSQL开关打开后，导出TopSQL模板列表。该功能仅支持付费实例。查询时间间隔最长一小时。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTopSqlTemplatesDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportTopSqlTemplatesDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportTopSqlTemplatesDetailsResponse`
        """
        http_info = self._export_top_sql_templates_details_http_info(request)
        return self._call_api(**http_info)

    def export_top_sql_templates_details_invoker(self, request):
        http_info = self._export_top_sql_templates_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_top_sql_templates_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/top-sql-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ExportTopSqlTemplatesDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
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

    def export_top_sql_trend_details(self, request):
        r"""导出SQL执行耗时区间数据

        TopSQL开关打开后，导出SQL执行耗时区间数据。该功能仅支持付费实例。查询时间间隔最长六小时。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTopSqlTrendDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportTopSqlTrendDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportTopSqlTrendDetailsResponse`
        """
        http_info = self._export_top_sql_trend_details_http_info(request)
        return self._call_api(**http_info)

    def export_top_sql_trend_details_invoker(self, request):
        http_info = self._export_top_sql_trend_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_top_sql_trend_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/top-sql-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ExportTopSqlTrendDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def list_analysis_result(self, request):
        r"""获取分析结果

        获取分析结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAnalysisResult
        :type request: :class:`huaweicloudsdkdas.v3.ListAnalysisResultRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListAnalysisResultResponse`
        """
        http_info = self._list_analysis_result_http_info(request)
        return self._call_api(**http_info)

    def list_analysis_result_invoker(self, request):
        http_info = self._list_analysis_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_analysis_result_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/query-analysis-result",
            "request_type": request.__class__.__name__,
            "response_type": "ListAnalysisResultResponse"
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

    def list_auto_increment_usage(self, request):
        r"""查询自增配额

        查询自增配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutoIncrementUsage
        :type request: :class:`huaweicloudsdkdas.v3.ListAutoIncrementUsageRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListAutoIncrementUsageResponse`
        """
        http_info = self._list_auto_increment_usage_http_info(request)
        return self._call_api(**http_info)

    def list_auto_increment_usage_invoker(self, request):
        http_info = self._list_auto_increment_usage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_auto_increment_usage_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/list-auto-increment-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ListAutoIncrementUsageResponse"
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

    def list_cloud_dba_instances(self, request):
        r"""获取DAS云DBA实例列表

        获取DAS云DBA实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCloudDbaInstances
        :type request: :class:`huaweicloudsdkdas.v3.ListCloudDbaInstancesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListCloudDbaInstancesResponse`
        """
        http_info = self._list_cloud_dba_instances_http_info(request)
        return self._call_api(**http_info)

    def list_cloud_dba_instances_invoker(self, request):
        http_info = self._list_cloud_dba_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cloud_dba_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListCloudDbaInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
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

    def list_database_infos(self, request):
        r"""获取数据库相关的cpu和内存信息

        获取数据库相关的cpu和内存信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseInfos
        :type request: :class:`huaweicloudsdkdas.v3.ListDatabaseInfosRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDatabaseInfosResponse`
        """
        http_info = self._list_database_infos_http_info(request)
        return self._call_api(**http_info)

    def list_database_infos_invoker(self, request):
        http_info = self._list_database_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_database_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/list-database-infos",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseInfosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def list_db_names(self, request):
        r"""获取库名列表

        获取库名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbNames
        :type request: :class:`huaweicloudsdkdas.v3.ListDbNamesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDbNamesResponse`
        """
        http_info = self._list_db_names_http_info(request)
        return self._call_api(**http_info)

    def list_db_names_invoker(self, request):
        http_info = self._list_db_names_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_db_names_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/get-name-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbNamesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def list_db_users(self, request):
        r"""查询数据库用户列表

        查询注册在DAS里的数据库用户列表，后续调用其他接口时(如查询实例会话列表接口)需要用到此接口返回的db_user_id。此接口不会返回数据库实例上的数据库用户对象。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkdas.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDbUsersResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users",
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'db_username' in local_var_params:
            query_params.append(('db_username', local_var_params['db_username']))

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

    def list_email_record(self, request):
        r"""查询邮件推送记录

        查询邮件推送记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEmailRecord
        :type request: :class:`huaweicloudsdkdas.v3.ListEmailRecordRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListEmailRecordResponse`
        """
        http_info = self._list_email_record_http_info(request)
        return self._call_api(**http_info)

    def list_email_record_invoker(self, request):
        http_info = self._list_email_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_email_record_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/batch-inspection/email-record",
            "request_type": request.__class__.__name__,
            "response_type": "ListEmailRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'send_status' in local_var_params:
            query_params.append(('send_status', local_var_params['send_status']))
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

    def list_email_template(self, request):
        r"""查询邮件模板列表

        查询邮件模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEmailTemplate
        :type request: :class:`huaweicloudsdkdas.v3.ListEmailTemplateRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListEmailTemplateResponse`
        """
        http_info = self._list_email_template_http_info(request)
        return self._call_api(**http_info)

    def list_email_template_invoker(self, request):
        http_info = self._list_email_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_email_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/batch-inspection/email-template",
            "request_type": request.__class__.__name__,
            "response_type": "ListEmailTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
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

    def list_full_sql_tasks(self, request):
        r"""查询SQL洞察任务列表

        全量SQL开关打开后，查询SQL洞察任务列表。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFullSqlTasks
        :type request: :class:`huaweicloudsdkdas.v3.ListFullSqlTasksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListFullSqlTasksResponse`
        """
        http_info = self._list_full_sql_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_full_sql_tasks_invoker(self, request):
        http_info = self._list_full_sql_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_full_sql_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/full-sql-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListFullSqlTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'range_left' in local_var_params:
            query_params.append(('range_left', local_var_params['range_left']))
        if 'range_right' in local_var_params:
            query_params.append(('range_right', local_var_params['range_right']))
        if 'create_at_left' in local_var_params:
            query_params.append(('create_at_left', local_var_params['create_at_left']))
        if 'create_at_right' in local_var_params:
            query_params.append(('create_at_right', local_var_params['create_at_right']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
        if 'operation' in local_var_params:
            query_params.append(('operation', local_var_params['operation']))
        if 'thread_id' in local_var_params:
            query_params.append(('thread_id', local_var_params['thread_id']))
        if 'trx_id' in local_var_params:
            query_params.append(('trx_id', local_var_params['trx_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'sql_template_id' in local_var_params:
            query_params.append(('sql_template_id', local_var_params['sql_template_id']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
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

    def list_health_report_task(self, request):
        r"""查询实例健康诊断报告列表

        查询实例健康诊断报告列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHealthReportTask
        :type request: :class:`huaweicloudsdkdas.v3.ListHealthReportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListHealthReportTaskResponse`
        """
        http_info = self._list_health_report_task_http_info(request)
        return self._call_api(**http_info)

    def list_health_report_task_invoker(self, request):
        http_info = self._list_health_report_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_health_report_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/get-instance-health-report-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListHealthReportTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
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

    def list_history_transaction_export_task(self, request):
        r"""查询历史事务导出任务列表

        DAS收集历史事务开关打开后，查询历史事务导出任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistoryTransactionExportTask
        :type request: :class:`huaweicloudsdkdas.v3.ListHistoryTransactionExportTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListHistoryTransactionExportTaskResponse`
        """
        http_info = self._list_history_transaction_export_task_http_info(request)
        return self._call_api(**http_info)

    def list_history_transaction_export_task_invoker(self, request):
        http_info = self._list_history_transaction_export_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_transaction_export_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/get-export-task-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryTransactionExportTaskResponse"
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

    def list_innodb_locks(self, request):
        r"""查询InnoDB锁等待列表

        查询InnoDB锁等待列表。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInnodbLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListInnodbLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInnodbLocksResponse`
        """
        http_info = self._list_innodb_locks_http_info(request)
        return self._call_api(**http_info)

    def list_innodb_locks_invoker(self, request):
        http_info = self._list_innodb_locks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_innodb_locks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/innodb-locks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInnodbLocksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))

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

    def list_inspection_report(self, request):
        r"""查询巡检报告列表

        查询巡检报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInspectionReport
        :type request: :class:`huaweicloudsdkdas.v3.ListInspectionReportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInspectionReportResponse`
        """
        http_info = self._list_inspection_report_http_info(request)
        return self._call_api(**http_info)

    def list_inspection_report_invoker(self, request):
        http_info = self._list_inspection_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_inspection_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/batch-inspection/health-report-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListInspectionReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'health_rank' in local_var_params:
            query_params.append(('health_rank', local_var_params['health_rank']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
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

    def list_instance_distribution(self, request):
        r"""查询实例分布情况

        查询实例分布情况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceDistribution
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceDistributionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceDistributionResponse`
        """
        http_info = self._list_instance_distribution_http_info(request)
        return self._call_api(**http_info)

    def list_instance_distribution_invoker(self, request):
        http_info = self._list_instance_distribution_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_distribution_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/distribution",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceDistributionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def list_instance_group(self, request):
        r"""查询实例组列表

        查询实例组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceGroup
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceGroupRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceGroupResponse`
        """
        http_info = self._list_instance_group_http_info(request)
        return self._call_api(**http_info)

    def list_instance_group_invoker(self, request):
        http_info = self._list_instance_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/batch-inspection/instance-group",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
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

    def list_instance_multi_nodes_single_metric(self, request):
        r"""获取多节点单指标数据

        获取多节点单指标数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceMultiNodesSingleMetric
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceMultiNodesSingleMetricRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceMultiNodesSingleMetricResponse`
        """
        http_info = self._list_instance_multi_nodes_single_metric_http_info(request)
        return self._call_api(**http_info)

    def list_instance_multi_nodes_single_metric_invoker(self, request):
        http_info = self._list_instance_multi_nodes_single_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_multi_nodes_single_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/multi-nodes/single-metric",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceMultiNodesSingleMetricResponse"
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

    def list_instance_nodes_info(self, request):
        r"""获取单个实例节点信息

        获取单个实例节点信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceNodesInfo
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceNodesInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceNodesInfoResponse`
        """
        http_info = self._list_instance_nodes_info_http_info(request)
        return self._call_api(**http_info)

    def list_instance_nodes_info_invoker(self, request):
        http_info = self._list_instance_nodes_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_nodes_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instance/nodes-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceNodesInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def list_instance_top_slow_log(self, request):
        r"""查询实例的TOP慢SQL列表

        查询实例的TOP慢SQL列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTopSlowLog
        :type request: :class:`huaweicloudsdkdas.v3.ListInstanceTopSlowLogRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInstanceTopSlowLogResponse`
        """
        http_info = self._list_instance_top_slow_log_http_info(request)
        return self._call_api(**http_info)

    def list_instance_top_slow_log_invoker(self, request):
        http_info = self._list_instance_top_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_top_slow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/top-slow-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceTopSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'num' in local_var_params:
            query_params.append(('num', local_var_params['num']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))

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

    def list_lock_blocking_db(self, request):
        r"""查询锁阻塞数据库名列表

        查询锁阻塞数据库名列表。
        仅支持SQLServer实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLockBlockingDb
        :type request: :class:`huaweicloudsdkdas.v3.ListLockBlockingDbRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListLockBlockingDbResponse`
        """
        http_info = self._list_lock_blocking_db_http_info(request)
        return self._call_api(**http_info)

    def list_lock_blocking_db_invoker(self, request):
        http_info = self._list_lock_blocking_db_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lock_blocking_db_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lock-blocking/get-lock-blocking-db-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListLockBlockingDbResponse"
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

    def list_lock_blocking_detail(self, request):
        r"""查询锁阻塞明细列表

        查询锁阻塞明细列表。
        仅支持SQLServer实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLockBlockingDetail
        :type request: :class:`huaweicloudsdkdas.v3.ListLockBlockingDetailRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListLockBlockingDetailResponse`
        """
        http_info = self._list_lock_blocking_detail_http_info(request)
        return self._call_api(**http_info)

    def list_lock_blocking_detail_invoker(self, request):
        http_info = self._list_lock_blocking_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lock_blocking_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lock-blocking/get-lock-blocking-detail-list",
            "request_type": request.__class__.__name__,
            "response_type": "ListLockBlockingDetailResponse"
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
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))

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

    def list_lock_blocking_relationship(self, request):
        r"""查询锁阻塞关系

        查询锁阻塞关系。
        仅支持SQLServer实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLockBlockingRelationship
        :type request: :class:`huaweicloudsdkdas.v3.ListLockBlockingRelationshipRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListLockBlockingRelationshipResponse`
        """
        http_info = self._list_lock_blocking_relationship_http_info(request)
        return self._call_api(**http_info)

    def list_lock_blocking_relationship_invoker(self, request):
        http_info = self._list_lock_blocking_relationship_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lock_blocking_relationship_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lock-blocking/get-lock-blocking-relationship",
            "request_type": request.__class__.__name__,
            "response_type": "ListLockBlockingRelationshipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'unique_id' in local_var_params:
            query_params.append(('unique_id', local_var_params['unique_id']))
        if 'spid' in local_var_params:
            query_params.append(('spid', local_var_params['spid']))

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

    def list_metadata_locks(self, request):
        r"""查询元数据锁列表

        查询元数据锁列表。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetadataLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListMetadataLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListMetadataLocksResponse`
        """
        http_info = self._list_metadata_locks_http_info(request)
        return self._call_api(**http_info)

    def list_metadata_locks_invoker(self, request):
        http_info = self._list_metadata_locks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metadata_locks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/metadata-locks",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetadataLocksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'thread_id' in local_var_params:
            query_params.append(('thread_id', local_var_params['thread_id']))
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'table' in local_var_params:
            query_params.append(('table', local_var_params['table']))

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

    def list_processes(self, request):
        r"""查询实例会话列表

        支持根据数据库、用户查询实例会话列表。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProcesses
        :type request: :class:`huaweicloudsdkdas.v3.ListProcessesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListProcessesResponse`
        """
        http_info = self._list_processes_http_info(request)
        return self._call_api(**http_info)

    def list_processes_invoker(self, request):
        http_info = self._list_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/processes",
            "request_type": request.__class__.__name__,
            "response_type": "ListProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
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

    def list_risk_items(self, request):
        r"""查询资源风险实例风险项

        查询资源风险实例风险项
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRiskItems
        :type request: :class:`huaweicloudsdkdas.v3.ListRiskItemsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListRiskItemsResponse`
        """
        http_info = self._list_risk_items_http_info(request)
        return self._call_api(**http_info)

    def list_risk_items_invoker(self, request):
        http_info = self._list_risk_items_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_risk_items_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/get-risk-items",
            "request_type": request.__class__.__name__,
            "response_type": "ListRiskItemsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_risk_trend(self, request):
        r"""查询资源风险实例风险趋势

        查询资源风险实例风险趋势
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRiskTrend
        :type request: :class:`huaweicloudsdkdas.v3.ListRiskTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListRiskTrendResponse`
        """
        http_info = self._list_risk_trend_http_info(request)
        return self._call_api(**http_info)

    def list_risk_trend_invoker(self, request):
        http_info = self._list_risk_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_risk_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/risk-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ListRiskTrendResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'metric_code' in local_var_params:
            query_params.append(('metric_code', local_var_params['metric_code']))

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

    def list_snapshots(self, request):
        r"""查询快照列表

        查询快照列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSnapshots
        :type request: :class:`huaweicloudsdkdas.v3.ListSnapshotsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSnapshotsResponse`
        """
        http_info = self._list_snapshots_http_info(request)
        return self._call_api(**http_info)

    def list_snapshots_invoker(self, request):
        http_info = self._list_snapshots_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_snapshots_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/list-snapshots",
            "request_type": request.__class__.__name__,
            "response_type": "ListSnapshotsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'module' in local_var_params:
            query_params.append(('module', local_var_params['module']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'per_page' in local_var_params:
            query_params.append(('per_page', local_var_params['per_page']))
        if 'cur_page' in local_var_params:
            query_params.append(('cur_page', local_var_params['cur_page']))

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

    def list_space_analysis(self, request):
        r"""获取空间分析数据列表

        获取空间分析数据列表。实例级别数据来源于文件系统，库级别和表级别数据来源于information_schema.tables表。空间&amp;元数据分析最多分析10000张表，若缺少库表空间数据，可能是因为数据库实例表个数过多或者账号未保存密码。如果为保存密码，请使用用户管理接口或页面录入数据库账号。 支持MySQL、GaussDB(for MySQL)和SQLServer引擎。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpaceAnalysis
        :type request: :class:`huaweicloudsdkdas.v3.ListSpaceAnalysisRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSpaceAnalysisResponse`
        """
        http_info = self._list_space_analysis_http_info(request)
        return self._call_api(**http_info)

    def list_space_analysis_invoker(self, request):
        http_info = self._list_space_analysis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_space_analysis_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpaceAnalysisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'database_id' in local_var_params:
            query_params.append(('database_id', local_var_params['database_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'show_instance_info' in local_var_params:
            query_params.append(('show_instance_info', local_var_params['show_instance_info']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def list_sql_limit_rules(self, request):
        r"""查询SQL限流规则列表

        查询SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.ListSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSqlLimitRulesResponse`
        """
        http_info = self._list_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def list_sql_limit_rules_invoker(self, request):
        http_info = self._list_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlLimitRulesResponse"
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
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))

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

    def list_top_slow_log(self, request):
        r"""查询TOP慢SQL列表

        查询TOP慢SQL列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTopSlowLog
        :type request: :class:`huaweicloudsdkdas.v3.ListTopSlowLogRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListTopSlowLogResponse`
        """
        http_info = self._list_top_slow_log_http_info(request)
        return self._call_api(**http_info)

    def list_top_slow_log_invoker(self, request):
        http_info = self._list_top_slow_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_top_slow_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/top-slow-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopSlowLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'num' in local_var_params:
            query_params.append(('num', local_var_params['num']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))

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

    def list_transactions(self, request):
        r"""查询历史事务列表

        查询历史事务列表。
        目前仅支持MySQL实例，仅支持查看最近7天的历史事务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTransactions
        :type request: :class:`huaweicloudsdkdas.v3.ListTransactionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListTransactionsResponse`
        """
        http_info = self._list_transactions_http_info(request)
        return self._call_api(**http_info)

    def list_transactions_invoker(self, request):
        http_info = self._list_transactions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_transactions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/transaction",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransactionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'last_sec_min' in local_var_params:
            query_params.append(('last_sec_min', local_var_params['last_sec_min']))
        if 'last_sec_max' in local_var_params:
            query_params.append(('last_sec_max', local_var_params['last_sec_max']))

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

    def login_built_in_account(self, request):
        r"""内置账号登录

        内置账号登录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LoginBuiltInAccount
        :type request: :class:`huaweicloudsdkdas.v3.LoginBuiltInAccountRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.LoginBuiltInAccountResponse`
        """
        http_info = self._login_built_in_account_http_info(request)
        return self._call_api(**http_info)

    def login_built_in_account_invoker(self, request):
        http_info = self._login_built_in_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _login_built_in_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/login-built-in-account",
            "request_type": request.__class__.__name__,
            "response_type": "LoginBuiltInAccountResponse"
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

    def logoff_built_in_account(self, request):
        r"""内置账号登出

        内置账号登出
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LogoffBuiltInAccount
        :type request: :class:`huaweicloudsdkdas.v3.LogoffBuiltInAccountRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.LogoffBuiltInAccountResponse`
        """
        http_info = self._logoff_built_in_account_http_info(request)
        return self._call_api(**http_info)

    def logoff_built_in_account_invoker(self, request):
        http_info = self._logoff_built_in_account_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _logoff_built_in_account_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/logoff-built-in-account",
            "request_type": request.__class__.__name__,
            "response_type": "LogoffBuiltInAccountResponse"
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

    def parse_dead_lock(self, request):
        r"""一键分析死锁日志

        一键分析死锁日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseDeadLock
        :type request: :class:`huaweicloudsdkdas.v3.ParseDeadLockRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ParseDeadLockResponse`
        """
        http_info = self._parse_dead_lock_http_info(request)
        return self._call_api(**http_info)

    def parse_dead_lock_invoker(self, request):
        http_info = self._parse_dead_lock_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_dead_lock_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "ParseDeadLockResponse"
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

    def parse_sql_limit_rules(self, request):
        r"""根据原始SQL生成SQL限流关键字

        根据原始SQL生成SQL限流关键字，目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.ParseSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ParseSqlLimitRulesResponse`
        """
        http_info = self._parse_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def parse_sql_limit_rules_invoker(self, request):
        http_info = self._parse_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/parse",
            "request_type": request.__class__.__name__,
            "response_type": "ParseSqlLimitRulesResponse"
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

    def register_db_user(self, request):
        r"""注册数据库用户

        此接口是将数据库用户和密码注册进DAS系统，同时会返回一个数据库用户ID ，后续调用其他接口时（如查询实例会话列表接口）需要用到此数据库用户ID。密码为加密存储，且仅用于DAS API相关功能。此接口不会在数据库实例上创建数据库用户对象。请确保输入的用户名和密码是已经存在并且是正确的。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDbUser
        :type request: :class:`huaweicloudsdkdas.v3.RegisterDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RegisterDbUserResponse`
        """
        http_info = self._register_db_user_http_info(request)
        return self._call_api(**http_info)

    def register_db_user_invoker(self, request):
        http_info = self._register_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_db_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterDbUserResponse"
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

    def save_credential(self, request):
        r"""保存AK/SK

        保存AK/SK，用于后台任务访问OBS上传实例诊断报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveCredential
        :type request: :class:`huaweicloudsdkdas.v3.SaveCredentialRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SaveCredentialResponse`
        """
        http_info = self._save_credential_http_info(request)
        return self._call_api(**http_info)

    def save_credential_invoker(self, request):
        http_info = self._save_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_credential_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/health-report/save-credential",
            "request_type": request.__class__.__name__,
            "response_type": "SaveCredentialResponse"
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

    def save_credential_for_batch_inspection(self, request):
        r"""保存AK/SK

        保存AK/SK，用于后台任务访问OBS上传实例诊断报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveCredentialForBatchInspection
        :type request: :class:`huaweicloudsdkdas.v3.SaveCredentialForBatchInspectionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SaveCredentialForBatchInspectionResponse`
        """
        http_info = self._save_credential_for_batch_inspection_http_info(request)
        return self._call_api(**http_info)

    def save_credential_for_batch_inspection_invoker(self, request):
        http_info = self._save_credential_for_batch_inspection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_credential_for_batch_inspection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/batch-inspection/save-credential",
            "request_type": request.__class__.__name__,
            "response_type": "SaveCredentialForBatchInspectionResponse"
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

    def set_lock_blocking_switch(self, request):
        r"""设置锁阻塞开关和保存时长

        设置锁阻塞开关和保存时长，仅支持SQLServer引擎
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetLockBlockingSwitch
        :type request: :class:`huaweicloudsdkdas.v3.SetLockBlockingSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetLockBlockingSwitchResponse`
        """
        http_info = self._set_lock_blocking_switch_http_info(request)
        return self._call_api(**http_info)

    def set_lock_blocking_switch_invoker(self, request):
        http_info = self._set_lock_blocking_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_lock_blocking_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/lock-blocking/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SetLockBlockingSwitchResponse"
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

    def set_threshold_for_metric(self, request):
        r"""设置指标阈值

        设置指标阈值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetThresholdForMetric
        :type request: :class:`huaweicloudsdkdas.v3.SetThresholdForMetricRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SetThresholdForMetricResponse`
        """
        http_info = self._set_threshold_for_metric_http_info(request)
        return self._call_api(**http_info)

    def set_threshold_for_metric_invoker(self, request):
        http_info = self._set_threshold_for_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_threshold_for_metric_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/set-metric-threshold",
            "request_type": request.__class__.__name__,
            "response_type": "SetThresholdForMetricResponse"
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

    def show_analysis_session_result(self, request):
        r"""查询会话分析结果

        查询会话分析结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAnalysisSessionResult
        :type request: :class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowAnalysisSessionResultResponse`
        """
        http_info = self._show_analysis_session_result_http_info(request)
        return self._call_api(**http_info)

    def show_analysis_session_result_invoker(self, request):
        http_info = self._show_analysis_session_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_analysis_session_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/session-analysis-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAnalysisSessionResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def show_analysis_session_status(self, request):
        r"""查询会话分析状态

        查询会话分析状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAnalysisSessionStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowAnalysisSessionStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowAnalysisSessionStatusResponse`
        """
        http_info = self._show_analysis_session_status_http_info(request)
        return self._call_api(**http_info)

    def show_analysis_session_status_invoker(self, request):
        http_info = self._show_analysis_session_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_analysis_session_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/session-analysis-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAnalysisSessionStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

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

    def show_clouddba_get_search_path_flag_new(self, request):
        r"""查询searchpath开关状态

        查询searchpath开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClouddbaGetSearchPathFlagNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowClouddbaGetSearchPathFlagNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowClouddbaGetSearchPathFlagNewResponse`
        """
        http_info = self._show_clouddba_get_search_path_flag_new_http_info(request)
        return self._call_api(**http_info)

    def show_clouddba_get_search_path_flag_new_invoker(self, request):
        http_info = self._show_clouddba_get_search_path_flag_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_clouddba_get_search_path_flag_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/clouddba-get-search-path-flag",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClouddbaGetSearchPathFlagNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_credential(self, request):
        r"""查询AK/SK

        查询AK/SK。用于判断是否已保存AK/SK
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCredential
        :type request: :class:`huaweicloudsdkdas.v3.ShowCredentialRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowCredentialResponse`
        """
        http_info = self._show_credential_http_info(request)
        return self._call_api(**http_info)

    def show_credential_invoker(self, request):
        http_info = self._show_credential_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_credential_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/batch-inspection/get-credential",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCredentialResponse"
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

    def show_das_cloud_dba_price(self, request):
        r"""开通配额询价

        开通配额询价
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDasCloudDbaPrice
        :type request: :class:`huaweicloudsdkdas.v3.ShowDasCloudDbaPriceRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDasCloudDbaPriceResponse`
        """
        http_info = self._show_das_cloud_dba_price_http_info(request)
        return self._call_api(**http_info)

    def show_das_cloud_dba_price_invoker(self, request):
        http_info = self._show_das_cloud_dba_price_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_das_cloud_dba_price_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clouddba/inquiry-price",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDasCloudDbaPriceResponse"
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

    def show_das_recommend_sql_limit_rule(self, request):
        r"""自动推荐SQL限流规则

        根据条件（包括模板所代表的sql平均时长，条数，最大执行时长，前三者混合）自动推荐SQL限流规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDasRecommendSqlLimitRule
        :type request: :class:`huaweicloudsdkdas.v3.ShowDasRecommendSqlLimitRuleRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDasRecommendSqlLimitRuleResponse`
        """
        http_info = self._show_das_recommend_sql_limit_rule_http_info(request)
        return self._call_api(**http_info)

    def show_das_recommend_sql_limit_rule_invoker(self, request):
        http_info = self._show_das_recommend_sql_limit_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_das_recommend_sql_limit_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/das-recommend-sql-limit-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDasRecommendSqlLimitRuleResponse"
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

    def show_db_user(self, request):
        r"""查询数据库用户信息

        查询注册在DAS里的数据库用户信息。此接口不能查询数据库实例上的数据库用户对象。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDbUser
        :type request: :class:`huaweicloudsdkdas.v3.ShowDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDbUserResponse`
        """
        http_info = self._show_db_user_http_info(request)
        return self._call_api(**http_info)

    def show_db_user_invoker(self, request):
        http_info = self._show_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_db_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_user_id' in local_var_params:
            path_params['db_user_id'] = local_var_params['db_user_id']

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

    def show_dead_lock_analysis_result(self, request):
        r"""查询死锁日志分析结果

        查询死锁日志分析结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockAnalysisResult
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockAnalysisResultRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockAnalysisResultResponse`
        """
        http_info = self._show_dead_lock_analysis_result_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_analysis_result_invoker(self, request):
        http_info = self._show_dead_lock_analysis_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_analysis_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dead-lock-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockAnalysisResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'dead_lock_id' in local_var_params:
            query_params.append(('dead_lock_id', local_var_params['dead_lock_id']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'transaction_id' in local_var_params:
            query_params.append(('transaction_id', local_var_params['transaction_id']))
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

    def show_dead_lock_topology(self, request):
        r"""获取死锁拓扑图数据

        获取死锁拓扑图数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockTopology
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockTopologyResponse`
        """
        http_info = self._show_dead_lock_topology_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_topology_invoker(self, request):
        http_info = self._show_dead_lock_topology_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_topology_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/dead-lock-topology",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockTopologyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'dead_lock_id' in local_var_params:
            query_params.append(('dead_lock_id', local_var_params['dead_lock_id']))

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

    def show_export_task_info(self, request):
        r"""查看全量SQL导出任务详情

        查看全量SQL导出任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExportTaskInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowExportTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowExportTaskInfoResponse`
        """
        http_info = self._show_export_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_export_task_info_invoker(self, request):
        http_info = self._show_export_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_export_task_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/get-export-task-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExportTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def show_full_dead_lock_list(self, request):
        r"""获取全量死锁信息

        获取全量死锁信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFullDeadLockList
        :type request: :class:`huaweicloudsdkdas.v3.ShowFullDeadLockListRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowFullDeadLockListResponse`
        """
        http_info = self._show_full_dead_lock_list_http_info(request)
        return self._call_api(**http_info)

    def show_full_dead_lock_list_invoker(self, request):
        http_info = self._show_full_dead_lock_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_full_dead_lock_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/show-fulldeadlock-list",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFullDeadLockListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))

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

    def show_full_dead_lock_switch(self, request):
        r"""获取全量死锁开关

        获取全量死锁开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFullDeadLockSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ShowFullDeadLockSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowFullDeadLockSwitchResponse`
        """
        http_info = self._show_full_dead_lock_switch_http_info(request)
        return self._call_api(**http_info)

    def show_full_dead_lock_switch_invoker(self, request):
        http_info = self._show_full_dead_lock_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_full_dead_lock_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/show-fulldeadlock-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFullDeadLockSwitchResponse"
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

    def show_full_dead_lock_switch_new(self, request):
        r"""获取全量死锁开关

        获取全量死锁开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFullDeadLockSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowFullDeadLockSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowFullDeadLockSwitchNewResponse`
        """
        http_info = self._show_full_dead_lock_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_full_dead_lock_switch_new_invoker(self, request):
        http_info = self._show_full_dead_lock_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_full_dead_lock_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/get-full-dead-lock-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFullDeadLockSwitchNewResponse"
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

    def show_global_privacy_new(self, request):
        r"""获取产品级别的安全协议

        获取产品级别的安全协议
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGlobalPrivacyNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowGlobalPrivacyNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowGlobalPrivacyNewResponse`
        """
        http_info = self._show_global_privacy_new_http_info(request)
        return self._call_api(**http_info)

    def show_global_privacy_new_invoker(self, request):
        http_info = self._show_global_privacy_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_global_privacy_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/policy/get-global-privacy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGlobalPrivacyNewResponse"
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

    def show_health_report_settings(self, request):
        r"""查看实例诊断报告设置

        查看实例诊断报告设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHealthReportSettings
        :type request: :class:`huaweicloudsdkdas.v3.ShowHealthReportSettingsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowHealthReportSettingsResponse`
        """
        http_info = self._show_health_report_settings_http_info(request)
        return self._call_api(**http_info)

    def show_health_report_settings_invoker(self, request):
        http_info = self._show_health_report_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_health_report_settings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/health-report/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthReportSettingsResponse"
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

    def show_history_transaction_export_task_info(self, request):
        r"""查询历史事务导出任务详情

        DAS收集历史事务开关打开后，查询历史事务导出任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTransactionExportTaskInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowHistoryTransactionExportTaskInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowHistoryTransactionExportTaskInfoResponse`
        """
        http_info = self._show_history_transaction_export_task_info_http_info(request)
        return self._call_api(**http_info)

    def show_history_transaction_export_task_info_invoker(self, request):
        http_info = self._show_history_transaction_export_task_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_history_transaction_export_task_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/get-export-task-info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTransactionExportTaskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def show_history_transaction_switch_new(self, request):
        r"""查询历史事务开关

        查询历史事务开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryTransactionSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowHistoryTransactionSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowHistoryTransactionSwitchNewResponse`
        """
        http_info = self._show_history_transaction_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_history_transaction_switch_new_invoker(self, request):
        http_info = self._show_history_transaction_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_history_transaction_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/get-history-transaction-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryTransactionSwitchNewResponse"
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

    def show_index_usage_switch_new(self, request):
        r"""查询索引使用开关

        查询索引使用开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIndexUsageSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowIndexUsageSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowIndexUsageSwitchNewResponse`
        """
        http_info = self._show_index_usage_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_index_usage_switch_new_invoker(self, request):
        http_info = self._show_index_usage_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_index_usage_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/index-usage/get-index-usage-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIndexUsageSwitchNewResponse"
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

    def show_instance_health_report(self, request):
        r"""获取实例健康诊断报告内容

        获取实例健康诊断报告内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceHealthReport
        :type request: :class:`huaweicloudsdkdas.v3.ShowInstanceHealthReportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowInstanceHealthReportResponse`
        """
        http_info = self._show_instance_health_report_http_info(request)
        return self._call_api(**http_info)

    def show_instance_health_report_invoker(self, request):
        http_info = self._show_instance_health_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_health_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/get-instance-health-report",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceHealthReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def show_kill_process_task_switch(self, request):
        r"""查询自治限流开关

        查询自治限流开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowKillProcessTaskSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ShowKillProcessTaskSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowKillProcessTaskSwitchResponse`
        """
        http_info = self._show_kill_process_task_switch_http_info(request)
        return self._call_api(**http_info)

    def show_kill_process_task_switch_invoker(self, request):
        http_info = self._show_kill_process_task_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_kill_process_task_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-flow/get-kill-process-task-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKillProcessTaskSwitchResponse"
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

    def show_latest_dead_lock_snapshot(self, request):
        r"""获取死锁的快照信息

        获取死锁的快照信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLatestDeadLockSnapshot
        :type request: :class:`huaweicloudsdkdas.v3.ShowLatestDeadLockSnapshotRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLatestDeadLockSnapshotResponse`
        """
        http_info = self._show_latest_dead_lock_snapshot_http_info(request)
        return self._call_api(**http_info)

    def show_latest_dead_lock_snapshot_invoker(self, request):
        http_info = self._show_latest_dead_lock_snapshot_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_latest_dead_lock_snapshot_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/instance/show-latestdeadlock-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestDeadLockSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_latest_instance_health_report(self, request):
        r"""获取最新的数据库健康日报内容

        获取最新的数据库健康日报内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLatestInstanceHealthReport
        :type request: :class:`huaweicloudsdkdas.v3.ShowLatestInstanceHealthReportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLatestInstanceHealthReportResponse`
        """
        http_info = self._show_latest_instance_health_report_http_info(request)
        return self._call_api(**http_info)

    def show_latest_instance_health_report_invoker(self, request):
        http_info = self._show_latest_instance_health_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_latest_instance_health_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/health-report/{instance_id}/get-latest-instance-health-report",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLatestInstanceHealthReportResponse"
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

    def show_lock_blocking_statistics(self, request):
        r"""查询锁阻塞数量统计

        查询锁阻塞数量统计。
        仅支持SQLServer实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLockBlockingStatistics
        :type request: :class:`huaweicloudsdkdas.v3.ShowLockBlockingStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLockBlockingStatisticsResponse`
        """
        http_info = self._show_lock_blocking_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_lock_blocking_statistics_invoker(self, request):
        http_info = self._show_lock_blocking_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_lock_blocking_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lock-blocking/get-lock-blocking-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLockBlockingStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'current_time' in local_var_params:
            query_params.append(('current_time', local_var_params['current_time']))

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

    def show_lock_blocking_switch(self, request):
        r"""查询锁阻塞开关和保存时长

        查询锁阻塞开关和保存时长。
        仅支持SQLServer实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLockBlockingSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ShowLockBlockingSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLockBlockingSwitchResponse`
        """
        http_info = self._show_lock_blocking_switch_http_info(request)
        return self._call_api(**http_info)

    def show_lock_blocking_switch_invoker(self, request):
        http_info = self._show_lock_blocking_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_lock_blocking_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/lock-blocking/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLockBlockingSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_lock_blocking_trend(self, request):
        r"""查询锁阻塞趋势列表

        查询锁阻塞趋势列表。
        仅支持SQLServer实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLockBlockingTrend
        :type request: :class:`huaweicloudsdkdas.v3.ShowLockBlockingTrendRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLockBlockingTrendResponse`
        """
        http_info = self._show_lock_blocking_trend_http_info(request)
        return self._call_api(**http_info)

    def show_lock_blocking_trend_invoker(self, request):
        http_info = self._show_lock_blocking_trend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_lock_blocking_trend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lock-blocking/get-lock-blocking-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLockBlockingTrendResponse"
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

    def show_long_history_transaction_switch_new(self, request):
        r"""查询长事务开关

        查询长事务开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLongHistoryTransactionSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowLongHistoryTransactionSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowLongHistoryTransactionSwitchNewResponse`
        """
        http_info = self._show_long_history_transaction_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_long_history_transaction_switch_new_invoker(self, request):
        http_info = self._show_long_history_transaction_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_long_history_transaction_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/transaction/{instance_id}/get-long-history-transaction-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLongHistoryTransactionSwitchNewResponse"
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

    def show_metric_names_support(self, request):
        r"""多节点单指标支持指标信息

        多节点单指标支持指标信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricNamesSupport
        :type request: :class:`huaweicloudsdkdas.v3.ShowMetricNamesSupportRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowMetricNamesSupportResponse`
        """
        http_info = self._show_metric_names_support_http_info(request)
        return self._call_api(**http_info)

    def show_metric_names_support_invoker(self, request):
        http_info = self._show_metric_names_support_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_names_support_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/metric-names/support",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricNamesSupportResponse"
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

    def show_name_list(self, request):
        r"""查看库名列表

        查看库名列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNameList
        :type request: :class:`huaweicloudsdkdas.v3.ShowNameListRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowNameListResponse`
        """
        http_info = self._show_name_list_http_info(request)
        return self._call_api(**http_info)

    def show_name_list_invoker(self, request):
        http_info = self._show_name_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_name_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/databases/get-name-list",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNameListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []
        if 'node_type' in local_var_params:
            query_params.append(('node_type', local_var_params['node_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def show_quotas(self, request):
        r"""查询云DBA配额

        查询云DBA配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkdas.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowQuotasResponse`
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

    def show_slow_log_switch_new(self, request):
        r"""查询慢日志开关

        查询慢日志开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowSlowLogSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSlowLogSwitchNewResponse`
        """
        http_info = self._show_slow_log_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_switch_new_invoker(self, request):
        http_info = self._show_slow_log_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/get-slow-log-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogSwitchNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_sql_execution_plan(self, request):
        r"""查询SQL执行计划

        查询SQL执行计划。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlExecutionPlan
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlExecutionPlanResponse`
        """
        http_info = self._show_sql_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def show_sql_execution_plan_invoker(self, request):
        http_info = self._show_sql_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_execution_plan_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/explain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'sql' in local_var_params:
            query_params.append(('sql', local_var_params['sql']))

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

    def show_sql_explain(self, request):
        r"""查询SQL执行计划

        查询SQL执行计划。
        目前仅支持MySQL实例。
        补充GET请求，处理超长SQL
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlExplain
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlExplainRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlExplainResponse`
        """
        http_info = self._show_sql_explain_http_info(request)
        return self._call_api(**http_info)

    def show_sql_explain_invoker(self, request):
        http_info = self._show_sql_explain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_explain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/explain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlExplainResponse"
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

    def show_sql_limit_job_info(self, request):
        r"""查询SQL限流任务

        查询指定ID的SQL限流任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitJobInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitJobInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitJobInfoResponse`
        """
        http_info = self._show_sql_limit_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limit_job_info_invoker(self, request):
        http_info = self._show_sql_limit_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limit_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/job",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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

    def show_sql_limit_switch_status(self, request):
        r"""查看SQL限流开关状态

        查询SQL限流的开关状态。目前仅支持MySQL实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitSwitchStatusResponse`
        """
        http_info = self._show_sql_limit_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limit_switch_status_invoker(self, request):
        http_info = self._show_sql_limit_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limit_switch_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitSwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def show_sql_limiting_switch_new(self, request):
        r"""查询SQL限流开关

        查询SQL限流开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitingSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitingSwitchNewResponse`
        """
        http_info = self._show_sql_limiting_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limiting_switch_new_invoker(self, request):
        http_info = self._show_sql_limiting_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limiting_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limiting/get-sql-limiting-switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitingSwitchNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def show_sql_switch_status(self, request):
        r"""查询全量SQL和慢SQL的开关状态

        查询DAS收集全量SQL和慢SQL的开关状态。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlSwitchStatusResponse`
        """
        http_info = self._show_sql_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_sql_switch_status_invoker(self, request):
        http_info = self._show_sql_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_switch_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlSwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def show_supported_engines(self, request):
        r"""查看支持的引擎类型

        查看支持的引擎类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSupportedEngines
        :type request: :class:`huaweicloudsdkdas.v3.ShowSupportedEnginesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSupportedEnginesResponse`
        """
        http_info = self._show_supported_engines_http_info(request)
        return self._call_api(**http_info)

    def show_supported_engines_invoker(self, request):
        http_info = self._show_supported_engines_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_supported_engines_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/engine/supported",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSupportedEnginesResponse"
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

    def show_transaction_switch_status(self, request):
        r"""查询历史事务开关

        查询历史事务开关。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTransactionSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowTransactionSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTransactionSwitchStatusResponse`
        """
        http_info = self._show_transaction_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_transaction_switch_status_invoker(self, request):
        http_info = self._show_transaction_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_transaction_switch_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/transaction/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTransactionSwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def show_tuning(self, request):
        r"""获取诊断结果

        获取诊断结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTuning
        :type request: :class:`huaweicloudsdkdas.v3.ShowTuningRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTuningResponse`
        """
        http_info = self._show_tuning_http_info(request)
        return self._call_api(**http_info)

    def show_tuning_invoker(self, request):
        http_info = self._show_tuning_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tuning_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/tuning/{message_id}/show-tuning-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTuningResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_whether_use_cloud_dba(self, request):
        r"""判断该实例能否使用云DBA功能

        判断该实例能否使用云DBA功能
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWhetherUseCloudDba
        :type request: :class:`huaweicloudsdkdas.v3.ShowWhetherUseCloudDbaRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowWhetherUseCloudDbaResponse`
        """
        http_info = self._show_whether_use_cloud_dba_http_info(request)
        return self._call_api(**http_info)

    def show_whether_use_cloud_dba_invoker(self, request):
        http_info = self._show_whether_use_cloud_dba_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_whether_use_cloud_dba_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/can-use-cloud-dba",
            "request_type": request.__class__.__name__,
            "response_type": "ShowWhetherUseCloudDbaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))

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

    def start_analysis_session(self, request):
        r"""开始会话分析

        开始会话分析
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAnalysisSession
        :type request: :class:`huaweicloudsdkdas.v3.StartAnalysisSessionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.StartAnalysisSessionResponse`
        """
        http_info = self._start_analysis_session_http_info(request)
        return self._call_api(**http_info)

    def start_analysis_session_invoker(self, request):
        http_info = self._start_analysis_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_analysis_session_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/session-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "StartAnalysisSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def synchronize_instances(self, request):
        r"""同步实例列表

        同步实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SynchronizeInstances
        :type request: :class:`huaweicloudsdkdas.v3.SynchronizeInstancesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SynchronizeInstancesResponse`
        """
        http_info = self._synchronize_instances_http_info(request)
        return self._call_api(**http_info)

    def synchronize_instances_invoker(self, request):
        http_info = self._synchronize_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _synchronize_instances_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/synchronize-instance-list",
            "request_type": request.__class__.__name__,
            "response_type": "SynchronizeInstancesResponse"
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

    def update_db_user(self, request):
        r"""修改数据库用户

        修改注册在DAS里的数据库用户名和密码。此接口不会修改数据库实例上的数据库用户对象的用户名和密码。请确保输入的用户名和密码是已经存在并且是正确的。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbUser
        :type request: :class:`huaweicloudsdkdas.v3.UpdateDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateDbUserResponse`
        """
        http_info = self._update_db_user_http_info(request)
        return self._call_api(**http_info)

    def update_db_user_invoker(self, request):
        http_info = self._update_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_user_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_user_id' in local_var_params:
            path_params['db_user_id'] = local_var_params['db_user_id']

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

    def update_email_template(self, request):
        r"""修改邮件模板

        修改邮件模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEmailTemplate
        :type request: :class:`huaweicloudsdkdas.v3.UpdateEmailTemplateRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateEmailTemplateResponse`
        """
        http_info = self._update_email_template_http_info(request)
        return self._call_api(**http_info)

    def update_email_template_invoker(self, request):
        http_info = self._update_email_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_email_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/batch-inspection/email-template",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEmailTemplateResponse"
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

    def update_full_sql_switch(self, request):
        r"""全量SQL开关

        全量SQL开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFullSqlSwitch
        :type request: :class:`huaweicloudsdkdas.v3.UpdateFullSqlSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateFullSqlSwitchResponse`
        """
        http_info = self._update_full_sql_switch_http_info(request)
        return self._call_api(**http_info)

    def update_full_sql_switch_invoker(self, request):
        http_info = self._update_full_sql_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_full_sql_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/fullsql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFullSqlSwitchResponse"
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

    def update_health_report_settings(self, request):
        r"""更新实例诊断报告设置

        更新实例诊断报告设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHealthReportSettings
        :type request: :class:`huaweicloudsdkdas.v3.UpdateHealthReportSettingsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateHealthReportSettingsResponse`
        """
        http_info = self._update_health_report_settings_http_info(request)
        return self._call_api(**http_info)

    def update_health_report_settings_invoker(self, request):
        http_info = self._update_health_report_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_health_report_settings_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/health-report/settings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHealthReportSettingsResponse"
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

    def update_instance_group(self, request):
        r"""修改实例组

        修改实例组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceGroup
        :type request: :class:`huaweicloudsdkdas.v3.UpdateInstanceGroupRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateInstanceGroupResponse`
        """
        http_info = self._update_instance_group_http_info(request)
        return self._call_api(**http_info)

    def update_instance_group_invoker(self, request):
        http_info = self._update_instance_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/batch-inspection/instance-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceGroupResponse"
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

    def update_sql_limit_rules(self, request):
        r"""修改SQL限流规则

        修改SQL限流规则。目前仅支持PostgreSQL数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.UpdateSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateSqlLimitRulesResponse`
        """
        http_info = self._update_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def update_sql_limit_rules_invoker(self, request):
        http_info = self._update_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSqlLimitRulesResponse"
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

    def show_dead_lock_switch_new(self, request):
        r"""查询死锁开关状态

        查询死锁开关状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeadLockSwitchNew
        :type request: :class:`huaweicloudsdkdas.v3.ShowDeadLockSwitchNewRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDeadLockSwitchNewResponse`
        """
        http_info = self._show_dead_lock_switch_new_http_info(request)
        return self._call_api(**http_info)

    def show_dead_lock_switch_new_invoker(self, request):
        http_info = self._show_dead_lock_switch_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dead_lock_switch_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dead-lock/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeadLockSwitchNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def switch_fullsql_switch(self, request):
        r"""开启/关闭全量SQL开关

        开启/关闭全量SQL开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchFullsqlSwitch
        :type request: :class:`huaweicloudsdkdas.v3.SwitchFullsqlSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.SwitchFullsqlSwitchResponse`
        """
        http_info = self._switch_fullsql_switch_http_info(request)
        return self._call_api(**http_info)

    def switch_fullsql_switch_invoker(self, request):
        http_info = self._switch_fullsql_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_fullsql_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/fullsql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchFullsqlSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkoms'")


class OmsClient(Client):
    def __init__(self):
        super(OmsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkoms.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "OmsClient":
                raise TypeError("client type error, support client type is OmsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_sync_events(self, request):
        """创建同步事件

        源端有对象需要进行同步时，调用该接口创建一个同步事件，系统将根据同步事件中包含的对象名称进行同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSyncEvents
        :type request: :class:`huaweicloudsdkoms.v2.CreateSyncEventsRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.CreateSyncEventsResponse`
        """
        http_info = self._create_sync_events_http_info(request)
        return self._call_api(**http_info)

    def create_sync_events_invoker(self, request):
        http_info = self._create_sync_events_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sync_events_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/sync-tasks/{sync_task_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSyncEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'sync_task_id' in local_var_params:
            path_params['sync_task_id'] = local_var_params['sync_task_id']

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

    def create_task(self, request):
        """创建迁移任务

        创建迁移任务，创建成功后，任务会被自动启动，不需要额外调用启动任务命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkoms.v2.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.CreateTaskResponse`
        """
        http_info = self._create_task_http_info(request)
        return self._call_api(**http_info)

    def create_task_invoker(self, request):
        http_info = self._create_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTaskResponse"
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

    def delete_task(self, request):
        """删除迁移任务

        调用该接口删除迁移任务。
        正在运行的任务不允许删除，如果删除会返回失败；若要删除，请先行暂停任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkoms.v2.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.DeleteTaskResponse`
        """
        http_info = self._delete_task_http_info(request)
        return self._call_api(**http_info)

    def delete_task_invoker(self, request):
        http_info = self._delete_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskResponse"
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

    def list_tasks(self, request):
        """查询迁移任务列表

        查询用户账户下的所有任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkoms.v2.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def show_task(self, request):
        """查询指定ID的任务详情

        查询指定ID的任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkoms.v2.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResponse"
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

    def start_task(self, request):
        """启动迁移任务

        迁移任务暂停或失败后，调用该接口以启动任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartTask
        :type request: :class:`huaweicloudsdkoms.v2.StartTaskRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.StartTaskResponse`
        """
        http_info = self._start_task_http_info(request)
        return self._call_api(**http_info)

    def start_task_invoker(self, request):
        http_info = self._start_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/tasks/{task_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartTaskResponse"
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

    def stop_task(self, request):
        """暂停迁移任务

        当迁移任务处于迁移中时，调用该接口停止任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopTask
        :type request: :class:`huaweicloudsdkoms.v2.StopTaskRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.StopTaskResponse`
        """
        http_info = self._stop_task_http_info(request)
        return self._call_api(**http_info)

    def stop_task_invoker(self, request):
        http_info = self._stop_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/tasks/{task_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopTaskResponse"
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

    def update_bandwidth_policy(self, request):
        """更新任务带宽策略

        当迁移任务未执行完成时，修改迁移任务的流量控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBandwidthPolicy
        :type request: :class:`huaweicloudsdkoms.v2.UpdateBandwidthPolicyRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.UpdateBandwidthPolicyResponse`
        """
        http_info = self._update_bandwidth_policy_http_info(request)
        return self._call_api(**http_info)

    def update_bandwidth_policy_invoker(self, request):
        http_info = self._update_bandwidth_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_bandwidth_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/tasks/{task_id}/bandwidth-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBandwidthPolicyResponse"
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

    def create_task_group(self, request):
        """创建迁移任务组

        创建迁移任务组，创建成功后，迁移任务组会自动创建迁移任务，不需要额外调用启动任务命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.CreateTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.CreateTaskGroupResponse`
        """
        http_info = self._create_task_group_http_info(request)
        return self._call_api(**http_info)

    def create_task_group_invoker(self, request):
        http_info = self._create_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_task_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/taskgroups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTaskGroupResponse"
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

    def delete_task_group(self, request):
        """删除指定ID的迁移任务组

        删除指定的迁移任务组.
        创建任务中、监控中、暂停中状态的任务不允许删除，如果删除会返回失败；若要删除，请先行暂停任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.DeleteTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.DeleteTaskGroupResponse`
        """
        http_info = self._delete_task_group_http_info(request)
        return self._call_api(**http_info)

    def delete_task_group_invoker(self, request):
        http_info = self._delete_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_task_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/taskgroups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_task_group(self, request):
        """查询迁移任务组列表

        查询用户账户下的任务组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.ListTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.ListTaskGroupResponse`
        """
        http_info = self._list_task_group_http_info(request)
        return self._call_api(**http_info)

    def list_task_group_invoker(self, request):
        http_info = self._list_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_task_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/taskgroups",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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

    def retry_task_group(self, request):
        """对已经失败的指定ID迁移任务组进行重启

        当迁移任务组处于迁移失败状态时，调用该接口重启指定ID的迁移任务组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.RetryTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.RetryTaskGroupResponse`
        """
        http_info = self._retry_task_group_http_info(request)
        return self._call_api(**http_info)

    def retry_task_group_invoker(self, request):
        http_info = self._retry_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _retry_task_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/taskgroups/{group_id}/retry",
            "request_type": request.__class__.__name__,
            "response_type": "RetryTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def show_task_group(self, request):
        """获取指定ID的taskgroup信息

        获取指定ID的taskgroup信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.ShowTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.ShowTaskGroupResponse`
        """
        http_info = self._show_task_group_http_info(request)
        return self._call_api(**http_info)

    def show_task_group_invoker(self, request):
        http_info = self._show_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/taskgroups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def start_task_group(self, request):
        """恢复指定ID的迁移任务组

        当迁移任务组处于暂停状态时，调用该接口启动指定ID的迁移任务组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.StartTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.StartTaskGroupResponse`
        """
        http_info = self._start_task_group_http_info(request)
        return self._call_api(**http_info)

    def start_task_group_invoker(self, request):
        http_info = self._start_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_task_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/taskgroups/{group_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def stop_task_group(self, request):
        """暂停指定ID的迁移任务组

        当迁移任务组处于创建任务中或监控中时，调用该接口暂停指定迁移任务组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.StopTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.StopTaskGroupResponse`
        """
        http_info = self._stop_task_group_http_info(request)
        return self._call_api(**http_info)

    def stop_task_group_invoker(self, request):
        http_info = self._stop_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_task_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/taskgroups/{group_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def update_task_group(self, request):
        """更新指定ID的迁移任务组的流控策略

        当迁移任务组未执行完成时，修改迁移任务组的流量控制策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskGroup
        :type request: :class:`huaweicloudsdkoms.v2.UpdateTaskGroupRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.UpdateTaskGroupResponse`
        """
        http_info = self._update_task_group_http_info(request)
        return self._call_api(**http_info)

    def update_task_group_invoker(self, request):
        http_info = self._update_task_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_task_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/taskgroups/{group_id}/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_api_versions(self, request):
        """查询API版本信息列表

        查询对象存储迁移服务的API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkoms.v2.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.ListApiVersionsResponse`
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
            "resource_path": "/",
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

    def show_api_info(self, request):
        """查询指定API版本信息

        查询对象存储迁移服务指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiInfo
        :type request: :class:`huaweicloudsdkoms.v2.ShowApiInfoRequest`
        :rtype: :class:`huaweicloudsdkoms.v2.ShowApiInfoResponse`
        """
        http_info = self._show_api_info_http_info(request)
        return self._call_api(**http_info)

    def show_api_info_invoker(self, request):
        http_info = self._show_api_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_api_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiInfoResponse"
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

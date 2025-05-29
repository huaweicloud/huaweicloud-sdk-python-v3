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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdds'")


class DdsClient(Client):
    def __init__(self):
        super(DdsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdds.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DdsClient":
                raise TypeError("client type error, support client type is DdsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_readonly_node(self, request):
        r"""实例新增只读节点

        DDS副本集实例新增只读节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddReadonlyNode
        :type request: :class:`huaweicloudsdkdds.v3.AddReadonlyNodeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.AddReadonlyNodeResponse`
        """
        http_info = self._add_readonly_node_http_info(request)
        return self._call_api(**http_info)

    def add_readonly_node_invoker(self, request):
        http_info = self._add_readonly_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_readonly_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/readonly-node",
            "request_type": request.__class__.__name__,
            "response_type": "AddReadonlyNodeResponse"
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

    def add_sharding_node(self, request):
        r"""扩容集群实例的节点数量

        扩容指定集群实例的节点数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddShardingNode
        :type request: :class:`huaweicloudsdkdds.v3.AddShardingNodeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.AddShardingNodeResponse`
        """
        http_info = self._add_sharding_node_http_info(request)
        return self._call_api(**http_info)

    def add_sharding_node_invoker(self, request):
        http_info = self._add_sharding_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_sharding_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/enlarge",
            "request_type": request.__class__.__name__,
            "response_type": "AddShardingNodeResponse"
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

    def attach_eip(self, request):
        r"""绑定弹性公网IP

        为实例下的节点绑定弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachEip
        :type request: :class:`huaweicloudsdkdds.v3.AttachEipRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.AttachEipResponse`
        """
        http_info = self._attach_eip_http_info(request)
        return self._call_api(**http_info)

    def attach_eip_invoker(self, request):
        http_info = self._attach_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/nodes/{node_id}/bind-eip",
            "request_type": request.__class__.__name__,
            "response_type": "AttachEipResponse"
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

    def attach_internal_ip(self, request):
        r"""修改实例内网地址

        修改实例的内网地址
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AttachInternalIp
        :type request: :class:`huaweicloudsdkdds.v3.AttachInternalIpRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.AttachInternalIpResponse`
        """
        http_info = self._attach_internal_ip_http_info(request)
        return self._call_api(**http_info)

    def attach_internal_ip_invoker(self, request):
        http_info = self._attach_internal_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _attach_internal_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/modify-internal-ip",
            "request_type": request.__class__.__name__,
            "response_type": "AttachInternalIpResponse"
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

    def batch_delete_backup(self, request):
        r"""批量删除手动备份

        批量删除数据库实例的手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteBackup
        :type request: :class:`huaweicloudsdkdds.v3.BatchDeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.BatchDeleteBackupResponse`
        """
        http_info = self._batch_delete_backup_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_backup_invoker(self, request):
        http_info = self._batch_delete_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/backups",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteBackupResponse"
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

    def batch_tag_action(self, request):
        r"""批量添加或删除资源标签

        批量添加或删除指定实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkdds.v3.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.BatchTagActionResponse`
        """
        http_info = self._batch_tag_action_http_info(request)
        return self._call_api(**http_info)

    def batch_tag_action_invoker(self, request):
        http_info = self._batch_tag_action_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_tag_action_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchTagActionResponse"
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

    def batch_upgrade_database_version(self, request):
        r"""批量数据库补丁升级

        批量升级数据库补丁版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpgradeDatabaseVersion
        :type request: :class:`huaweicloudsdkdds.v3.BatchUpgradeDatabaseVersionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.BatchUpgradeDatabaseVersionResponse`
        """
        http_info = self._batch_upgrade_database_version_http_info(request)
        return self._call_api(**http_info)

    def batch_upgrade_database_version_invoker(self, request):
        http_info = self._batch_upgrade_database_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_upgrade_database_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpgradeDatabaseVersionResponse"
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

    def cancel_eip(self, request):
        r"""解绑弹性公网IP

        解绑实例下节点已经绑定的弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelEip
        :type request: :class:`huaweicloudsdkdds.v3.CancelEipRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CancelEipResponse`
        """
        http_info = self._cancel_eip_http_info(request)
        return self._call_api(**http_info)

    def cancel_eip_invoker(self, request):
        http_info = self._cancel_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_eip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/nodes/{node_id}/unbind-eip",
            "request_type": request.__class__.__name__,
            "response_type": "CancelEipResponse"
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def cancel_scheduled_task(self, request):
        r"""取消定时任务

        根据任务ID取消定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelScheduledTask
        :type request: :class:`huaweicloudsdkdds.v3.CancelScheduledTaskRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CancelScheduledTaskResponse`
        """
        http_info = self._cancel_scheduled_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_scheduled_task_invoker(self, request):
        http_info = self._cancel_scheduled_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_scheduled_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/scheduled-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelScheduledTaskResponse"
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

    def change_ops_window(self, request):
        r"""设置可维护时间段

        修改用户允许启动某项对数据库实例运行有影响的任务的时间范围，例如操作系统升级和数据库软件版本升级的时间窗。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeOpsWindow
        :type request: :class:`huaweicloudsdkdds.v3.ChangeOpsWindowRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ChangeOpsWindowResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/maintenance-window",
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

    def check_password(self, request):
        r"""检查数据库密码

        检查数据库密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckPassword
        :type request: :class:`huaweicloudsdkdds.v3.CheckPasswordRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CheckPasswordResponse`
        """
        http_info = self._check_password_http_info(request)
        return self._call_api(**http_info)

    def check_password_invoker(self, request):
        http_info = self._check_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/check-password",
            "request_type": request.__class__.__name__,
            "response_type": "CheckPasswordResponse"
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

    def check_weak_password(self, request):
        r"""检查弱密码

        检查弱密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckWeakPassword
        :type request: :class:`huaweicloudsdkdds.v3.CheckWeakPasswordRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CheckWeakPasswordResponse`
        """
        http_info = self._check_weak_password_http_info(request)
        return self._call_api(**http_info)

    def check_weak_password_invoker(self, request):
        http_info = self._check_weak_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_weak_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/weak-password-verification",
            "request_type": request.__class__.__name__,
            "response_type": "CheckWeakPasswordResponse"
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

    def compare_configuration(self, request):
        r"""参数模板比较

        比较两个参数模板之间的差异。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.CompareConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CompareConfigurationResponse`
        """
        http_info = self._compare_configuration_http_info(request)
        return self._call_api(**http_info)

    def compare_configuration_invoker(self, request):
        http_info = self._compare_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _compare_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/comparison",
            "request_type": request.__class__.__name__,
            "response_type": "CompareConfigurationResponse"
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

    def copy_configuration(self, request):
        r"""复制参数模板

        复制参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.CopyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CopyConfigurationResponse`
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
        r"""创建参数模板

        创建参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.CreateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateConfigurationResponse`
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

    def create_database_role(self, request):
        r"""创建数据库角色

        创建数据库角色。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseRole
        :type request: :class:`huaweicloudsdkdds.v3.CreateDatabaseRoleRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateDatabaseRoleResponse`
        """
        http_info = self._create_database_role_http_info(request)
        return self._call_api(**http_info)

    def create_database_role_invoker(self, request):
        http_info = self._create_database_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_role_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-role",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseRoleResponse"
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

    def create_database_user(self, request):
        r"""创建数据库用户

        创建数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseUser
        :type request: :class:`huaweicloudsdkdds.v3.CreateDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateDatabaseUserResponse`
        """
        http_info = self._create_database_user_http_info(request)
        return self._call_api(**http_info)

    def create_database_user_invoker(self, request):
        http_info = self._create_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-user",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseUserResponse"
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

    def create_instance(self, request):
        r"""创建实例

        创建文档数据库实例，包括集群实例、副本集实例、以及单节点实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkdds.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateInstanceResponse`
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

    def create_ip(self, request):
        r"""创建集群的Shard/Config IP

        创建集群的Shard/Config IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIp
        :type request: :class:`huaweicloudsdkdds.v3.CreateIpRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateIpResponse`
        """
        http_info = self._create_ip_http_info(request)
        return self._call_api(**http_info)

    def create_ip_invoker(self, request):
        http_info = self._create_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/create-ip",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIpResponse"
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

    def create_kill_op_rule(self, request):
        r"""创建killOp规则

        创建killOp规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateKillOpRule
        :type request: :class:`huaweicloudsdkdds.v3.CreateKillOpRuleRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateKillOpRuleResponse`
        """
        http_info = self._create_kill_op_rule_http_info(request)
        return self._call_api(**http_info)

    def create_kill_op_rule_invoker(self, request):
        http_info = self._create_kill_op_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_kill_op_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/kill-op-rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKillOpRuleResponse"
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

    def create_manual_backup(self, request):
        r"""创建手动备份

        创建数据库实例的手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateManualBackup
        :type request: :class:`huaweicloudsdkdds.v3.CreateManualBackupRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.CreateManualBackupResponse`
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

    def delete_audit_log(self, request):
        r"""删除审计日志

        删除审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditLog
        :type request: :class:`huaweicloudsdkdds.v3.DeleteAuditLogRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteAuditLogResponse`
        """
        http_info = self._delete_audit_log_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_log_invoker(self, request):
        http_info = self._delete_audit_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_log_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auditlog",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditLogResponse"
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
        r"""删除参数模板

        删除参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteConfigurationResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_database_role(self, request):
        r"""删除数据库角色

        删除数据库角色。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabaseRole
        :type request: :class:`huaweicloudsdkdds.v3.DeleteDatabaseRoleRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteDatabaseRoleResponse`
        """
        http_info = self._delete_database_role_http_info(request)
        return self._call_api(**http_info)

    def delete_database_role_invoker(self, request):
        http_info = self._delete_database_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_role_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-role",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseRoleResponse"
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

    def delete_database_user(self, request):
        r"""删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabaseUser
        :type request: :class:`huaweicloudsdkdds.v3.DeleteDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteDatabaseUserResponse`
        """
        http_info = self._delete_database_user_http_info(request)
        return self._call_api(**http_info)

    def delete_database_user_invoker(self, request):
        http_info = self._delete_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-user",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseUserResponse"
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

    def delete_instance(self, request):
        r"""删除实例

        删除数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkdds.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteInstanceResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_kill_op_rule_list(self, request):
        r"""删除killOp规则

        删除killOp规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteKillOpRuleList
        :type request: :class:`huaweicloudsdkdds.v3.DeleteKillOpRuleListRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteKillOpRuleListResponse`
        """
        http_info = self._delete_kill_op_rule_list_http_info(request)
        return self._call_api(**http_info)

    def delete_kill_op_rule_list_invoker(self, request):
        http_info = self._delete_kill_op_rule_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_kill_op_rule_list_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/kill-op-rule",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKillOpRuleListResponse"
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

    def delete_lts_config(self, request):
        r"""解除关联LTS日志流

        将实例日志与LTS日志流解除关联，后台将取消上传实例日志到的LTS日志流里。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLtsConfig
        :type request: :class:`huaweicloudsdkdds.v3.DeleteLtsConfigRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteLtsConfigResponse`
        """
        http_info = self._delete_lts_config_http_info(request)
        return self._call_api(**http_info)

    def delete_lts_config_invoker(self, request):
        http_info = self._delete_lts_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_lts_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLtsConfigResponse"
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

    def delete_manual_backup(self, request):
        r"""删除手动备份

        删除数据库实例的手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteManualBackup
        :type request: :class:`huaweicloudsdkdds.v3.DeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteManualBackupResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_mongos_node(self, request):
        r"""删除mongos节点

        当集群实例需要缩减mongos节点时，需要调用此API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMongosNode
        :type request: :class:`huaweicloudsdkdds.v3.DeleteMongosNodeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteMongosNodeResponse`
        """
        http_info = self._delete_mongos_node_http_info(request)
        return self._call_api(**http_info)

    def delete_mongos_node_invoker(self, request):
        http_info = self._delete_mongos_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_mongos_node_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/mongos-node",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMongosNodeResponse"
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

    def delete_readonly_node(self, request):
        r"""删除只读节点

        当副本集添加了只读节点后，需要删除对应的只读节点需要调用此API。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteReadonlyNode
        :type request: :class:`huaweicloudsdkdds.v3.DeleteReadonlyNodeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteReadonlyNodeResponse`
        """
        http_info = self._delete_readonly_node_http_info(request)
        return self._call_api(**http_info)

    def delete_readonly_node_invoker(self, request):
        http_info = self._delete_readonly_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_readonly_node_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/readonly-node",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteReadonlyNodeResponse"
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

    def delete_session(self, request):
        r"""终结实例节点会话

        终结实例节点会话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSession
        :type request: :class:`huaweicloudsdkdds.v3.DeleteSessionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteSessionResponse`
        """
        http_info = self._delete_session_http_info(request)
        return self._call_api(**http_info)

    def delete_session_invoker(self, request):
        http_info = self._delete_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_session_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/nodes/{node_id}/session",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSessionResponse"
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

    def download_errorlog(self, request):
        r"""获取错误日志下载链接

        获取错误日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadErrorlog
        :type request: :class:`huaweicloudsdkdds.v3.DownloadErrorlogRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DownloadErrorlogResponse`
        """
        http_info = self._download_errorlog_http_info(request)
        return self._call_api(**http_info)

    def download_errorlog_invoker(self, request):
        http_info = self._download_errorlog_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_errorlog_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/errorlog-download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadErrorlogResponse"
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
        r"""获取慢日志下载链接

        获取慢日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadSlowlog
        :type request: :class:`huaweicloudsdkdds.v3.DownloadSlowlogRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.DownloadSlowlogResponse`
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

    def expand_replicaset_node(self, request):
        r"""扩容副本集实例的节点数量

        扩容指定副本集实例的节点数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandReplicasetNode
        :type request: :class:`huaweicloudsdkdds.v3.ExpandReplicasetNodeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ExpandReplicasetNodeResponse`
        """
        http_info = self._expand_replicaset_node_http_info(request)
        return self._call_api(**http_info)

    def expand_replicaset_node_invoker(self, request):
        http_info = self._expand_replicaset_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_replicaset_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/replicaset-node",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandReplicasetNodeResponse"
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

    def list_applied_instances(self, request):
        r"""查询可应用的实例

        查询指定参数模板可被应用的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAppliedInstances
        :type request: :class:`huaweicloudsdkdds.v3.ListAppliedInstancesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListAppliedInstancesResponse`
        """
        http_info = self._list_applied_instances_http_info(request)
        return self._call_api(**http_info)

    def list_applied_instances_invoker(self, request):
        http_info = self._list_applied_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_applied_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/applicable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppliedInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def list_auditlog_links(self, request):
        r"""获取审计日志下载链接

        获取审计日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditlogLinks
        :type request: :class:`huaweicloudsdkdds.v3.ListAuditlogLinksRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListAuditlogLinksResponse`
        """
        http_info = self._list_auditlog_links_http_info(request)
        return self._call_api(**http_info)

    def list_auditlog_links_invoker(self, request):
        http_info = self._list_auditlog_links_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_auditlog_links_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auditlog-links",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditlogLinksResponse"
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

    def list_auditlogs(self, request):
        r"""获取审计日志列表

        获取审计日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditlogs
        :type request: :class:`huaweicloudsdkdds.v3.ListAuditlogsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListAuditlogsResponse`
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
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
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

    def list_az2_migrate(self, request):
        r"""查询实例可迁移到的可用区

        查询实例可迁移到的可用区。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAz2Migrate
        :type request: :class:`huaweicloudsdkdds.v3.ListAz2MigrateRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListAz2MigrateResponse`
        """
        http_info = self._list_az2_migrate_http_info(request)
        return self._call_api(**http_info)

    def list_az2_migrate_invoker(self, request):
        http_info = self._list_az2_migrate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_az2_migrate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/migrate/az",
            "request_type": request.__class__.__name__,
            "response_type": "ListAz2MigrateResponse"
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

    def list_backups(self, request):
        r"""查询备份列表

        根据指定条件查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkdds.v3.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListBackupsResponse`
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
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))

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
        r"""获取参数模板列表

        获取参数模板列表，包括DDS数据库的所有默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkdds.v3.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListConfigurationsResponse`
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

    def list_database_roles(self, request):
        r"""查询数据库角色列表

        查询数据库角色列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseRoles
        :type request: :class:`huaweicloudsdkdds.v3.ListDatabaseRolesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListDatabaseRolesResponse`
        """
        http_info = self._list_database_roles_http_info(request)
        return self._call_api(**http_info)

    def list_database_roles_invoker(self, request):
        http_info = self._list_database_roles_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_database_roles_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-roles",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseRolesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'role_name' in local_var_params:
            query_params.append(('role_name', local_var_params['role_name']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
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

    def list_database_users(self, request):
        r"""查询数据库用户列表

        查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseUsers
        :type request: :class:`huaweicloudsdkdds.v3.ListDatabaseUsersRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListDatabaseUsersResponse`
        """
        http_info = self._list_database_users_http_info(request)
        return self._call_api(**http_info)

    def list_database_users_invoker(self, request):
        http_info = self._list_database_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_database_users_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-user/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseUsersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'db_name' in local_var_params:
            query_params.append(('db_name', local_var_params['db_name']))
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

    def list_databases(self, request):
        r"""查询数据库列表

        查询数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkdds.v3.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListDatabasesResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
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

    def list_datastore_versions(self, request):
        r"""查询数据库版本信息

        查询指定实例类型的数据库版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatastoreVersions
        :type request: :class:`huaweicloudsdkdds.v3.ListDatastoreVersionsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListDatastoreVersionsResponse`
        """
        http_info = self._list_datastore_versions_http_info(request)
        return self._call_api(**http_info)

    def list_datastore_versions_invoker(self, request):
        http_info = self._list_datastore_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_datastore_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/datastores/{datastore_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatastoreVersionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datastore_name' in local_var_params:
            path_params['datastore_name'] = local_var_params['datastore_name']

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

    def list_error_logs(self, request):
        r"""查询数据库错误日志

        查询数据库错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListErrorLogs
        :type request: :class:`huaweicloudsdkdds.v3.ListErrorLogsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListErrorLogsResponse`
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
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def list_flavor_infos(self, request):
        r"""查询数据库规格

        查询指定条件下的实例规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavorInfos
        :type request: :class:`huaweicloudsdkdds.v3.ListFlavorInfosRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListFlavorInfosResponse`
        """
        http_info = self._list_flavor_infos_http_info(request)
        return self._call_api(**http_info)

    def list_flavor_infos_invoker(self, request):
        http_info = self._list_flavor_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_flavor_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorInfosResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_name' in local_var_params:
            query_params.append(('engine_name', local_var_params['engine_name']))
        if 'engine_version' in local_var_params:
            query_params.append(('engine_version', local_var_params['engine_version']))
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

    def list_flavors(self, request):
        r"""查询所有实例规格信息

        查询指定条件下的所有实例规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkdds.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListFlavorsResponse`
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
            "resource_path": "/v3/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'engine_name' in local_var_params:
            query_params.append(('engine_name', local_var_params['engine_name']))

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
        r"""查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkdds.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListInstanceTagsResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""查询实例列表和详情

        根据指定条件查询实例列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkdds.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListInstancesResponse`
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
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

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

    def list_instances_by_tags(self, request):
        r"""查询资源实例

        根据标签查询指定的数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesByTags
        :type request: :class:`huaweicloudsdkdds.v3.ListInstancesByTagsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListInstancesByTagsResponse`
        """
        http_info = self._list_instances_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instances_by_tags_invoker(self, request):
        http_info = self._list_instances_by_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_by_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesByTagsResponse"
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

    def list_lts_configs(self, request):
        r"""查询LTS日志配置信息

        查询LTS日志配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLtsConfigs
        :type request: :class:`huaweicloudsdkdds.v3.ListLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListLtsConfigsResponse`
        """
        http_info = self._list_lts_configs_http_info(request)
        return self._call_api(**http_info)

    def list_lts_configs_invoker(self, request):
        http_info = self._list_lts_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lts_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLtsConfigsResponse"
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

    def list_lts_error_logs(self, request):
        r"""查询数据库错误日志

        查询数据库错误日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLtsErrorLogs
        :type request: :class:`huaweicloudsdkdds.v3.ListLtsErrorLogsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListLtsErrorLogsResponse`
        """
        http_info = self._list_lts_error_logs_http_info(request)
        return self._call_api(**http_info)

    def list_lts_error_logs_invoker(self, request):
        http_info = self._list_lts_error_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lts_error_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/error-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLtsErrorLogsResponse"
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

    def list_lts_slow_logs(self, request):
        r"""查询数据库慢日志

        查询数据库慢日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLtsSlowLogs
        :type request: :class:`huaweicloudsdkdds.v3.ListLtsSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListLtsSlowLogsResponse`
        """
        http_info = self._list_lts_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_lts_slow_logs_invoker(self, request):
        http_info = self._list_lts_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lts_slow_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLtsSlowLogsResponse"
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

    def list_project_tags(self, request):
        r"""查询项目标签

        查询指定project ID下实例的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkdds.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListProjectTagsResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""查询回收站实例列表

        查询回收站实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkdds.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListRecycleInstancesResponse`
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

    def list_restore_collections(self, request):
        r"""获取可恢复的数据库集合列表

        获取可恢复的数据库集合列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreCollections
        :type request: :class:`huaweicloudsdkdds.v3.ListRestoreCollectionsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListRestoreCollectionsResponse`
        """
        http_info = self._list_restore_collections_http_info(request)
        return self._call_api(**http_info)

    def list_restore_collections_invoker(self, request):
        http_info = self._list_restore_collections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restore_collections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restore-collection",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestoreCollectionsResponse"
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
        if 'restore_time' in local_var_params:
            query_params.append(('restore_time', local_var_params['restore_time']))
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

    def list_restore_databases(self, request):
        r"""获取可恢复的数据库列表

        获取可恢复的数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreDatabases
        :type request: :class:`huaweicloudsdkdds.v3.ListRestoreDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListRestoreDatabasesResponse`
        """
        http_info = self._list_restore_databases_http_info(request)
        return self._call_api(**http_info)

    def list_restore_databases_invoker(self, request):
        http_info = self._list_restore_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restore_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restore-database",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestoreDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'restore_time' in local_var_params:
            query_params.append(('restore_time', local_var_params['restore_time']))
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
        r"""查询可恢复的时间段

        查询实例的可恢复时间段。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreTimes
        :type request: :class:`huaweicloudsdkdds.v3.ListRestoreTimesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListRestoreTimesResponse`
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

    def list_scheduled_tasks(self, request):
        r"""查询定时任务

        根据指定条件查询定时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduledTasks
        :type request: :class:`huaweicloudsdkdds.v3.ListScheduledTasksRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListScheduledTasksResponse`
        """
        http_info = self._list_scheduled_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_scheduled_tasks_invoker(self, request):
        http_info = self._list_scheduled_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scheduled_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/scheduled-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduledTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'job_status' in local_var_params:
            query_params.append(('job_status', local_var_params['job_status']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
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

    def list_sessions(self, request):
        r"""查询实例节点会话

        查询实例节点会话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSessions
        :type request: :class:`huaweicloudsdkdds.v3.ListSessionsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListSessionsResponse`
        """
        http_info = self._list_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_sessions_invoker(self, request):
        http_info = self._list_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sessions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/nodes/{node_id}/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSessionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'node_id' in local_var_params:
            path_params['node_id'] = local_var_params['node_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'plan_summary' in local_var_params:
            query_params.append(('plan_summary', local_var_params['plan_summary']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'namespace' in local_var_params:
            query_params.append(('namespace', local_var_params['namespace']))
        if 'cost_time' in local_var_params:
            query_params.append(('cost_time', local_var_params['cost_time']))

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

    def list_slow_logs(self, request):
        r"""查询数据库慢日志

        查询数据库慢日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSlowLogs
        :type request: :class:`huaweicloudsdkdds.v3.ListSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListSlowLogsResponse`
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
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def list_ssl_cert_download_address(self, request):
        r"""获取SSL证书下载地址

        获取SSL证书下载地址
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSslCertDownloadAddress
        :type request: :class:`huaweicloudsdkdds.v3.ListSslCertDownloadAddressRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListSslCertDownloadAddressResponse`
        """
        http_info = self._list_ssl_cert_download_address_http_info(request)
        return self._call_api(**http_info)

    def list_ssl_cert_download_address_invoker(self, request):
        http_info = self._list_ssl_cert_download_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ssl_cert_download_address_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ssl-cert/download-link",
            "request_type": request.__class__.__name__,
            "response_type": "ListSslCertDownloadAddressResponse"
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

    def list_storage_type(self, request):
        r"""查询数据库磁盘类型

        查询当前区域下的数据库磁盘类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStorageType
        :type request: :class:`huaweicloudsdkdds.v3.ListStorageTypeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListStorageTypeResponse`
        """
        http_info = self._list_storage_type_http_info(request)
        return self._call_api(**http_info)

    def list_storage_type_invoker(self, request):
        http_info = self._list_storage_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_storage_type_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/storage-type",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_name' in local_var_params:
            query_params.append(('engine_name', local_var_params['engine_name']))

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
        r"""查询任务列表和详情

        根据指定条件查询任务中心中的任务列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkdds.v3.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListTasksResponse`
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
            "resource_path": "/v3.1/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def migrate_az(self, request):
        r"""实例可用区迁移

        实例可用区迁移。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for MigrateAz
        :type request: :class:`huaweicloudsdkdds.v3.MigrateAzRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.MigrateAzResponse`
        """
        http_info = self._migrate_az_http_info(request)
        return self._call_api(**http_info)

    def migrate_az_invoker(self, request):
        http_info = self._migrate_az_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _migrate_az_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/migrate",
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def reset_configuration(self, request):
        r"""重置参数模板

        重置参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.ResetConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ResetConfigurationResponse`
        """
        http_info = self._reset_configuration_http_info(request)
        return self._call_api(**http_info)

    def reset_configuration_invoker(self, request):
        http_info = self._reset_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetConfigurationResponse"
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""修改数据库用户密码

        修改数据库用户密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkdds.v3.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ResetPasswordResponse`
        """
        http_info = self._reset_password_http_info(request)
        return self._call_api(**http_info)

    def reset_password_invoker(self, request):
        http_info = self._reset_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/reset-password",
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
            ['application/json'])

        auth_settings = []

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

        变更实例的规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkdds.v3.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ResizeInstanceResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/resize",
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def resize_instance_volume(self, request):
        r"""扩容实例存储容量

        扩容实例相关的存储容量大小。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeInstanceVolume
        :type request: :class:`huaweicloudsdkdds.v3.ResizeInstanceVolumeRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ResizeInstanceVolumeResponse`
        """
        http_info = self._resize_instance_volume_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_volume_invoker(self, request):
        http_info = self._resize_instance_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_instance_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/enlarge-volume",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceVolumeResponse"
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

    def restart_instance(self, request):
        r"""重启实例

        重启实例的数据库服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartInstance
        :type request: :class:`huaweicloudsdkdds.v3.RestartInstanceRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.RestartInstanceResponse`
        """
        http_info = self._restart_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_instance_invoker(self, request):
        http_info = self._restart_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartInstanceResponse"
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

    def restore_instance(self, request):
        r"""恢复到当前实例

        恢复到当前实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreInstance
        :type request: :class:`huaweicloudsdkdds.v3.RestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.RestoreInstanceResponse`
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
            "resource_path": "/v3/{project_id}/instances/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreInstanceResponse"
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

    def restore_instance_from_collection(self, request):
        r"""库表级时间点恢复

        库表级时间点恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreInstanceFromCollection
        :type request: :class:`huaweicloudsdkdds.v3.RestoreInstanceFromCollectionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.RestoreInstanceFromCollectionResponse`
        """
        http_info = self._restore_instance_from_collection_http_info(request)
        return self._call_api(**http_info)

    def restore_instance_from_collection_invoker(self, request):
        http_info = self._restore_instance_from_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_instance_from_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restore/collections",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreInstanceFromCollectionResponse"
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

    def restore_new_instance(self, request):
        r"""恢复到新实例

        根据备份恢复新实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreNewInstance
        :type request: :class:`huaweicloudsdkdds.v3.RestoreNewInstanceRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.RestoreNewInstanceResponse`
        """
        http_info = self._restore_new_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_new_instance_invoker(self, request):
        http_info = self._restore_new_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_new_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreNewInstanceResponse"
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

    def set_auditlog_policy(self, request):
        r"""设置审计日志策略

        设置审计日志策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAuditlogPolicy
        :type request: :class:`huaweicloudsdkdds.v3.SetAuditlogPolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SetAuditlogPolicyResponse`
        """
        http_info = self._set_auditlog_policy_http_info(request)
        return self._call_api(**http_info)

    def set_auditlog_policy_invoker(self, request):
        http_info = self._set_auditlog_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_auditlog_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
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

    def set_auto_enlarge_policies(self, request):
        r"""设置磁盘自动扩容策略

        设置磁盘自动扩容策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAutoEnlargePolicies
        :type request: :class:`huaweicloudsdkdds.v3.SetAutoEnlargePoliciesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SetAutoEnlargePoliciesResponse`
        """
        http_info = self._set_auto_enlarge_policies_http_info(request)
        return self._call_api(**http_info)

    def set_auto_enlarge_policies_invoker(self, request):
        http_info = self._set_auto_enlarge_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_auto_enlarge_policies_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/auto-enlarge-volume-policies",
            "request_type": request.__class__.__name__,
            "response_type": "SetAutoEnlargePoliciesResponse"
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

    def set_backup_policy(self, request):
        r"""设置自动备份策略

        设置自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBackupPolicy
        :type request: :class:`huaweicloudsdkdds.v3.SetBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SetBackupPolicyResponse`
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

    def set_balancer_switch(self, request):
        r"""设置集群均衡开关

        设置集群均衡开关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBalancerSwitch
        :type request: :class:`huaweicloudsdkdds.v3.SetBalancerSwitchRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SetBalancerSwitchResponse`
        """
        http_info = self._set_balancer_switch_http_info(request)
        return self._call_api(**http_info)

    def set_balancer_switch_invoker(self, request):
        http_info = self._set_balancer_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_balancer_switch_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/balancer/{action}",
            "request_type": request.__class__.__name__,
            "response_type": "SetBalancerSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'action' in local_var_params:
            path_params['action'] = local_var_params['action']

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

    def set_balancer_window(self, request):
        r"""设置集群均衡活动时间窗

        设置集群均衡活动时间窗。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetBalancerWindow
        :type request: :class:`huaweicloudsdkdds.v3.SetBalancerWindowRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SetBalancerWindowResponse`
        """
        http_info = self._set_balancer_window_http_info(request)
        return self._call_api(**http_info)

    def set_balancer_window_invoker(self, request):
        http_info = self._set_balancer_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_balancer_window_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/balancer/active-window",
            "request_type": request.__class__.__name__,
            "response_type": "SetBalancerWindowResponse"
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

    def set_recycle_policy(self, request):
        r"""设置实例回收站策略

        设置实例回收站策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRecyclePolicy
        :type request: :class:`huaweicloudsdkdds.v3.SetRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SetRecyclePolicyResponse`
        """
        http_info = self._set_recycle_policy_http_info(request)
        return self._call_api(**http_info)

    def set_recycle_policy_invoker(self, request):
        http_info = self._set_recycle_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_recycle_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/recycle-policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetRecyclePolicyResponse"
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

    def show_auditlog_policy(self, request):
        r"""查询审计日志策略

        查询审计日志策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditlogPolicy
        :type request: :class:`huaweicloudsdkdds.v3.ShowAuditlogPolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowAuditlogPolicyResponse`
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
        r"""查询磁盘自动扩容策略

        查询磁盘自动扩容策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkdds.v3.ShowAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowAutoEnlargePolicyResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-enlarge-volume-policy",
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""获取备份下载链接

        获取备份下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupDownloadLink
        :type request: :class:`huaweicloudsdkdds.v3.ShowBackupDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowBackupDownloadLinkResponse`
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
            "resource_path": "/v3/{project_id}/backups/download-file",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupDownloadLinkResponse"
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
        r"""查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupPolicy
        :type request: :class:`huaweicloudsdkdds.v3.ShowBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowBackupPolicyResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_client_network(self, request):
        r"""查询副本集跨网段访问配置

        查询副本集跨网段访问配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClientNetwork
        :type request: :class:`huaweicloudsdkdds.v3.ShowClientNetworkRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowClientNetworkResponse`
        """
        http_info = self._show_client_network_http_info(request)
        return self._call_api(**http_info)

    def show_client_network_invoker(self, request):
        http_info = self._show_client_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_client_network_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/client-network",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClientNetworkResponse"
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

    def show_configuration_applied_history(self, request):
        r"""查询参数模板被应用历史

        查询参数模板应用历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigurationAppliedHistory
        :type request: :class:`huaweicloudsdkdds.v3.ShowConfigurationAppliedHistoryRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowConfigurationAppliedHistoryResponse`
        """
        http_info = self._show_configuration_applied_history_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_applied_history_invoker(self, request):
        http_info = self._show_configuration_applied_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_applied_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/applied-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationAppliedHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def show_configuration_modify_history(self, request):
        r"""查询参数模板修改历史

        查询参数模板修改历史。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigurationModifyHistory
        :type request: :class:`huaweicloudsdkdds.v3.ShowConfigurationModifyHistoryRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowConfigurationModifyHistoryResponse`
        """
        http_info = self._show_configuration_modify_history_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_modify_history_invoker(self, request):
        http_info = self._show_configuration_modify_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_modify_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationModifyHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def show_configuration_parameter(self, request):
        r"""获取参数模板的详情

        获取参数模板的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigurationParameter
        :type request: :class:`huaweicloudsdkdds.v3.ShowConfigurationParameterRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowConfigurationParameterResponse`
        """
        http_info = self._show_configuration_parameter_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_parameter_invoker(self, request):
        http_info = self._show_configuration_parameter_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_parameter_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationParameterResponse"
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_connection_statistics(self, request):
        r"""查询实例连接数统计信息

        查询客户端IP访问至DDS数据库实例的连接数统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnectionStatistics
        :type request: :class:`huaweicloudsdkdds.v3.ShowConnectionStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowConnectionStatisticsResponse`
        """
        http_info = self._show_connection_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_connection_statistics_invoker(self, request):
        http_info = self._show_connection_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connection_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/conn-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectionStatisticsResponse"
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

    def show_disk_usage(self, request):
        r"""查询实例磁盘信息

        查询实例磁盘信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDiskUsage
        :type request: :class:`huaweicloudsdkdds.v3.ShowDiskUsageRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowDiskUsageResponse`
        """
        http_info = self._show_disk_usage_http_info(request)
        return self._call_api(**http_info)

    def show_disk_usage_invoker(self, request):
        http_info = self._show_disk_usage_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_disk_usage_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disk-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDiskUsageResponse"
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

    def show_entity_configuration(self, request):
        r"""获取指定实例的参数信息

        获取指定实例的参数，可以是实例，组，节点的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEntityConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.ShowEntityConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowEntityConfigurationResponse`
        """
        http_info = self._show_entity_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_entity_configuration_invoker(self, request):
        http_info = self._show_entity_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_entity_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEntityConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'entity_id' in local_var_params:
            query_params.append(('entity_id', local_var_params['entity_id']))

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

    def show_instance_configuration_modify_history(self, request):
        r"""查询实例参数的修改历史

        查询实例参数的修改历史。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceConfigurationModifyHistory
        :type request: :class:`huaweicloudsdkdds.v3.ShowInstanceConfigurationModifyHistoryRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowInstanceConfigurationModifyHistoryResponse`
        """
        http_info = self._show_instance_configuration_modify_history_http_info(request)
        return self._call_api(**http_info)

    def show_instance_configuration_modify_history_invoker(self, request):
        http_info = self._show_instance_configuration_modify_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_configuration_modify_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configuration-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceConfigurationModifyHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'entity_id' in local_var_params:
            query_params.append(('entity_id', local_var_params['entity_id']))
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

    def show_job_detail(self, request):
        r"""获取DDS任务中心指定ID的任务信息。

        获取DDS任务中心指定ID的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkdds.v3.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobDetailResponse"
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

    def show_kill_op_rule_rule_list(self, request):
        r"""获取killOp规则列表

        获取killOp规则列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowKillOpRuleRuleList
        :type request: :class:`huaweicloudsdkdds.v3.ShowKillOpRuleRuleListRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowKillOpRuleRuleListResponse`
        """
        http_info = self._show_kill_op_rule_rule_list_http_info(request)
        return self._call_api(**http_info)

    def show_kill_op_rule_rule_list_invoker(self, request):
        http_info = self._show_kill_op_rule_rule_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_kill_op_rule_rule_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/kill-op-rule",
            "request_type": request.__class__.__name__,
            "response_type": "ShowKillOpRuleRuleListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'operation_types' in local_var_params:
            query_params.append(('operation_types', local_var_params['operation_types']))
        if 'namespaces' in local_var_params:
            query_params.append(('namespaces', local_var_params['namespaces']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'plan_summary' in local_var_params:
            query_params.append(('plan_summary', local_var_params['plan_summary']))
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

    def show_quotas(self, request):
        r"""查询配额

        查询单租户在DDS服务下的资源配额，包括单节点实例配额、副本集实例配额、集群实例配额等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkdds.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowQuotasResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""查询实例回收站策略

        查询实例回收站策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkdds.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowRecyclePolicyResponse`
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

    def show_repl_set_name(self, request):
        r"""查询数据库复制集名称

        查询数据库复制集名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReplSetName
        :type request: :class:`huaweicloudsdkdds.v3.ShowReplSetNameRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowReplSetNameResponse`
        """
        http_info = self._show_repl_set_name_http_info(request)
        return self._call_api(**http_info)

    def show_repl_set_name_invoker(self, request):
        http_info = self._show_repl_set_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_repl_set_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/replica-set/name",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReplSetNameResponse"
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

    def show_second_level_monitoring_status(self, request):
        r"""查询秒级监控配置

        查询秒级监控配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecondLevelMonitoringStatus
        :type request: :class:`huaweicloudsdkdds.v3.ShowSecondLevelMonitoringStatusRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowSecondLevelMonitoringStatusResponse`
        """
        http_info = self._show_second_level_monitoring_status_http_info(request)
        return self._call_api(**http_info)

    def show_second_level_monitoring_status_invoker(self, request):
        http_info = self._show_second_level_monitoring_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_second_level_monitoring_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/monitoring-by-seconds/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSecondLevelMonitoringStatusResponse"
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

    def show_sharding_balancer(self, request):
        r"""查询集群均衡设置

        查询集群均衡设置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowShardingBalancer
        :type request: :class:`huaweicloudsdkdds.v3.ShowShardingBalancerRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowShardingBalancerResponse`
        """
        http_info = self._show_sharding_balancer_http_info(request)
        return self._call_api(**http_info)

    def show_sharding_balancer_invoker(self, request):
        http_info = self._show_sharding_balancer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sharding_balancer_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/balancer",
            "request_type": request.__class__.__name__,
            "response_type": "ShowShardingBalancerResponse"
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

    def show_slowlog_desensitization_switch(self, request):
        r"""查询慢日志明文开关

        查询慢日志明文开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowlogDesensitizationSwitch
        :type request: :class:`huaweicloudsdkdds.v3.ShowSlowlogDesensitizationSwitchRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowSlowlogDesensitizationSwitchResponse`
        """
        http_info = self._show_slowlog_desensitization_switch_http_info(request)
        return self._call_api(**http_info)

    def show_slowlog_desensitization_switch_invoker(self, request):
        http_info = self._show_slowlog_desensitization_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slowlog_desensitization_switch_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-desensitization/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowlogDesensitizationSwitchResponse"
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

    def show_upgrade_duration(self, request):
        r"""查询数据库补丁升级预估时长

        查询数据库补丁升级预估时长
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpgradeDuration
        :type request: :class:`huaweicloudsdkdds.v3.ShowUpgradeDurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowUpgradeDurationResponse`
        """
        http_info = self._show_upgrade_duration_http_info(request)
        return self._call_api(**http_info)

    def show_upgrade_duration_invoker(self, request):
        http_info = self._show_upgrade_duration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_upgrade_duration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-upgrade-duration",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpgradeDurationResponse"
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

    def shrink_instance_nodes(self, request):
        r"""删除实例的节点

        删除实例的节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkInstanceNodes
        :type request: :class:`huaweicloudsdkdds.v3.ShrinkInstanceNodesRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShrinkInstanceNodesResponse`
        """
        http_info = self._shrink_instance_nodes_http_info(request)
        return self._call_api(**http_info)

    def shrink_instance_nodes_invoker(self, request):
        http_info = self._shrink_instance_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _shrink_instance_nodes_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ShrinkInstanceNodesResponse"
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

    def stop_backup(self, request):
        r"""停止备份

        支持紧急情况下停止备份功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopBackup
        :type request: :class:`huaweicloudsdkdds.v3.StopBackupRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.StopBackupResponse`
        """
        http_info = self._stop_backup_http_info(request)
        return self._call_api(**http_info)

    def stop_backup_invoker(self, request):
        http_info = self._stop_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_backup_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "StopBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def switch_configuration(self, request):
        r"""应用参数模板

        指定实例变更参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.SwitchConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SwitchConfigurationResponse`
        """
        http_info = self._switch_configuration_http_info(request)
        return self._call_api(**http_info)

    def switch_configuration_invoker(self, request):
        http_info = self._switch_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchConfigurationResponse"
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

    def switch_instance_primary(self, request):
        r"""强制备节点升主

        支持副本集、shard和config备节点强制升主。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchInstancePrimary
        :type request: :class:`huaweicloudsdkdds.v3.SwitchInstancePrimaryRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SwitchInstancePrimaryResponse`
        """
        http_info = self._switch_instance_primary_http_info(request)
        return self._call_api(**http_info)

    def switch_instance_primary_invoker(self, request):
        http_info = self._switch_instance_primary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_instance_primary_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/primary",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchInstancePrimaryResponse"
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def switch_second_level_monitoring(self, request):
        r"""开启/关闭秒级监控

        开启或关闭指定实例的秒级监控。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSecondLevelMonitoring
        :type request: :class:`huaweicloudsdkdds.v3.SwitchSecondLevelMonitoringRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SwitchSecondLevelMonitoringResponse`
        """
        http_info = self._switch_second_level_monitoring_http_info(request)
        return self._call_api(**http_info)

    def switch_second_level_monitoring_invoker(self, request):
        http_info = self._switch_second_level_monitoring_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_second_level_monitoring_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/monitoring-by-seconds/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchSecondLevelMonitoringResponse"
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

    def switch_slowlog_desensitization(self, request):
        r"""设置慢日志明文开关

        设置实例的慢日志明文开关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSlowlogDesensitization
        :type request: :class:`huaweicloudsdkdds.v3.SwitchSlowlogDesensitizationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SwitchSlowlogDesensitizationResponse`
        """
        http_info = self._switch_slowlog_desensitization_http_info(request)
        return self._call_api(**http_info)

    def switch_slowlog_desensitization_invoker(self, request):
        http_info = self._switch_slowlog_desensitization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_slowlog_desensitization_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-desensitization/{status}",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchSlowlogDesensitizationResponse"
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

    def switch_ssl(self, request):
        r"""切换SSL开关

        切换实例的SSL开关
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSsl
        :type request: :class:`huaweicloudsdkdds.v3.SwitchSslRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SwitchSslResponse`
        """
        http_info = self._switch_ssl_http_info(request)
        return self._call_api(**http_info)

    def switch_ssl_invoker(self, request):
        http_info = self._switch_ssl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_ssl_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switch-ssl",
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

    def switchover_replica_set(self, request):
        r"""切换副本集实例的主备节点

        切换副本集实例下的主备节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchoverReplicaSet
        :type request: :class:`huaweicloudsdkdds.v3.SwitchoverReplicaSetRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.SwitchoverReplicaSetResponse`
        """
        http_info = self._switchover_replica_set_http_info(request)
        return self._call_api(**http_info)

    def switchover_replica_set_invoker(self, request):
        http_info = self._switchover_replica_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switchover_replica_set_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switchover",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchoverReplicaSetResponse"
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

    def update_client_network(self, request):
        r"""副本集跨网段访问配置。

        副本集跨网段访问配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClientNetwork
        :type request: :class:`huaweicloudsdkdds.v3.UpdateClientNetworkRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateClientNetworkResponse`
        """
        http_info = self._update_client_network_http_info(request)
        return self._call_api(**http_info)

    def update_client_network_invoker(self, request):
        http_info = self._update_client_network_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_client_network_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/client-network",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClientNetworkResponse"
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

    def update_configuration_parameter(self, request):
        r"""修改参数模板

        修改指定参数模板的参数信息，包括名称、描述、指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfigurationParameter
        :type request: :class:`huaweicloudsdkdds.v3.UpdateConfigurationParameterRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateConfigurationParameterResponse`
        """
        http_info = self._update_configuration_parameter_http_info(request)
        return self._call_api(**http_info)

    def update_configuration_parameter_invoker(self, request):
        http_info = self._update_configuration_parameter_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_configuration_parameter_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConfigurationParameterResponse"
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

    def update_entity_configuration(self, request):
        r"""修改指定实例的参数

        修改指定实例的参数，可以是实例，组，节点的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateEntityConfiguration
        :type request: :class:`huaweicloudsdkdds.v3.UpdateEntityConfigurationRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateEntityConfigurationResponse`
        """
        http_info = self._update_entity_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_entity_configuration_invoker(self, request):
        http_info = self._update_entity_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_entity_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEntityConfigurationResponse"
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

    def update_instance_name(self, request):
        r"""修改实例名称

        修改实例名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkdds.v3.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateInstanceNameResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/modify-name",
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

    def update_instance_port(self, request):
        r"""修改数据库端口

        修改数据库实例的端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstancePort
        :type request: :class:`huaweicloudsdkdds.v3.UpdateInstancePortRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateInstancePortResponse`
        """
        http_info = self._update_instance_port_http_info(request)
        return self._call_api(**http_info)

    def update_instance_port_invoker(self, request):
        http_info = self._update_instance_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_port_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/modify-port",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstancePortResponse"
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

    def update_instance_remark(self, request):
        r"""修改实例备注

        修改实例备注。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceRemark
        :type request: :class:`huaweicloudsdkdds.v3.UpdateInstanceRemarkRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateInstanceRemarkResponse`
        """
        http_info = self._update_instance_remark_http_info(request)
        return self._call_api(**http_info)

    def update_instance_remark_invoker(self, request):
        http_info = self._update_instance_remark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_remark_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/remark",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceRemarkResponse"
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

    def update_kill_op_rule(self, request):
        r"""启用/禁用killOp规则

        启用/禁用killOp规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateKillOpRule
        :type request: :class:`huaweicloudsdkdds.v3.UpdateKillOpRuleRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateKillOpRuleResponse`
        """
        http_info = self._update_kill_op_rule_http_info(request)
        return self._call_api(**http_info)

    def update_kill_op_rule_invoker(self, request):
        http_info = self._update_kill_op_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_kill_op_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/kill-op-rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKillOpRuleResponse"
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

    def update_lts_config(self, request):
        r"""关联LTS日志流

        将实例日志与LTS日志流关联，后台将自动上传实例日志到关联的LTS日志流里。
        关联成功后，会产生一定费用，具体计费可参考云日志服务（LTS）的定价详情。
        系统会为当前选择的日志流创建对应日志类型的结构化配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateLtsConfig
        :type request: :class:`huaweicloudsdkdds.v3.UpdateLtsConfigRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateLtsConfigResponse`
        """
        http_info = self._update_lts_config_http_info(request)
        return self._call_api(**http_info)

    def update_lts_config_invoker(self, request):
        http_info = self._update_lts_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_lts_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLtsConfigResponse"
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

    def update_repl_set_name(self, request):
        r"""修改数据库复制集名称

        修改数据库复制集名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateReplSetName
        :type request: :class:`huaweicloudsdkdds.v3.UpdateReplSetNameRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateReplSetNameResponse`
        """
        http_info = self._update_repl_set_name_http_info(request)
        return self._call_api(**http_info)

    def update_repl_set_name_invoker(self, request):
        http_info = self._update_repl_set_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_repl_set_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/replica-set/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateReplSetNameResponse"
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

    def update_security_group(self, request):
        r"""变更实例安全组

        变更实例关联的安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSecurityGroup
        :type request: :class:`huaweicloudsdkdds.v3.UpdateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpdateSecurityGroupResponse`
        """
        http_info = self._update_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_security_group_invoker(self, request):
        http_info = self._update_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_security_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/modify-security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSecurityGroupResponse"
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

    def upgrade_database_version(self, request):
        r"""数据库补丁升级

        升级数据库补丁版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeDatabaseVersion
        :type request: :class:`huaweicloudsdkdds.v3.UpgradeDatabaseVersionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.UpgradeDatabaseVersionResponse`
        """
        http_info = self._upgrade_database_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_database_version_invoker(self, request):
        http_info = self._upgrade_database_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_database_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeDatabaseVersionResponse"
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

    def validate_configuration_name(self, request):
        r"""校验参数模板名称是否存在

        校验参数模板名称是否存在。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateConfigurationName
        :type request: :class:`huaweicloudsdkdds.v3.ValidateConfigurationNameRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ValidateConfigurationNameResponse`
        """
        http_info = self._validate_configuration_name_http_info(request)
        return self._call_api(**http_info)

    def validate_configuration_name_invoker(self, request):
        http_info = self._validate_configuration_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_configuration_name_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/name-validation",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateConfigurationNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def list_api_version(self, request):
        r"""查询当前支持的API版本信息列表

        查询当前支持的API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdkdds.v3.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ListApiVersionResponse`
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
            "resource_path": "/",
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

    def show_api_version(self, request):
        r"""查询指定API版本信息

        查询指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkdds.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkdds.v3.ShowApiVersionResponse`
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
            "resource_path": "/{version}",
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

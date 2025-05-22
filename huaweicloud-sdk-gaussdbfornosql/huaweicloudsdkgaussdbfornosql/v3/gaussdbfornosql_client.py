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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkgaussdbfornosql'")


class GaussDBforNoSQLClient(Client):
    def __init__(self):
        super(GaussDBforNoSQLClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgaussdbfornosql.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GaussDBforNoSQLClient":
                raise TypeError("client type error, support client type is GaussDBforNoSQLClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def apply_configuration(self, request):
        r"""应用参数模板

        将参数模板应用到实例，可以指定一个或多个实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ApplyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ApplyConfigurationResponse`
        """
        http_info = self._apply_configuration_http_info(request)
        return self._call_api(**http_info)

    def apply_configuration_invoker(self, request):
        http_info = self._apply_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyConfigurationResponse"
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

    def apply_configuration_to_instances(self, request):
        r"""应用参数模板

        将参数模板应用到实例，可以指定一个或多个实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ApplyConfigurationToInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ApplyConfigurationToInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ApplyConfigurationToInstancesResponse`
        """
        http_info = self._apply_configuration_to_instances_http_info(request)
        return self._call_api(**http_info)

    def apply_configuration_to_instances_invoker(self, request):
        http_info = self._apply_configuration_to_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _apply_configuration_to_instances_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/configurations/{config_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "ApplyConfigurationToInstancesResponse"
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

    def batch_delete_manual_backup(self, request):
        r"""批量删除手动备份

        批量删除数据库实例的手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteManualBackup
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchDeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchDeleteManualBackupResponse`
        """
        http_info = self._batch_delete_manual_backup_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_manual_backup_invoker(self, request):
        http_info = self._batch_delete_manual_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_manual_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/backups",
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

    def batch_tag_action(self, request):
        r"""批量添加或删除资源标签

        批量添加或删除指定数据库实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchTagActionResponse`
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchUpgradeDatabaseVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchUpgradeDatabaseVersionResponse`
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

    def cancel_instance_schedule_window(self, request):
        r"""取消定时任务

        取消定时任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelInstanceScheduleWindow
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CancelInstanceScheduleWindowRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CancelInstanceScheduleWindowResponse`
        """
        http_info = self._cancel_instance_schedule_window_http_info(request)
        return self._call_api(**http_info)

    def cancel_instance_schedule_window_invoker(self, request):
        http_info = self._cancel_instance_schedule_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_instance_schedule_window_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/scheduled-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelInstanceScheduleWindowResponse"
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

    def check_disaster_recovery_operation(self, request):
        r"""校验实例是否可以与指定实例建立/解除容灾关系

        校验实例是否可以与指定实例建立/解除容灾关系。若接口返回成功，表示可以与指定实例建立/解除容灾关系。
        该接口需要对建立/解除容灾关系的两个实例各调用一次，2次调用都响应成功才能进行容灾关系的搭建/解除。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDisasterRecoveryOperation
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckDisasterRecoveryOperationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckDisasterRecoveryOperationResponse`
        """
        http_info = self._check_disaster_recovery_operation_http_info(request)
        return self._call_api(**http_info)

    def check_disaster_recovery_operation_invoker(self, request):
        http_info = self._check_disaster_recovery_operation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_disaster_recovery_operation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery/precheck",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDisasterRecoveryOperationResponse"
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

    def check_week_password(self, request):
        r"""判断弱密码

        判断弱密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckWeekPassword
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckWeekPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckWeekPasswordResponse`
        """
        http_info = self._check_week_password_http_info(request)
        return self._call_api(**http_info)

    def check_week_password_invoker(self, request):
        http_info = self._check_week_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_week_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/weak-password-verification",
            "request_type": request.__class__.__name__,
            "response_type": "CheckWeekPasswordResponse"
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

    def clear_instance_sessions(self, request):
        r"""关闭实例所有节点会话

        关闭实例所有节点会话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ClearInstanceSessions
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ClearInstanceSessionsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ClearInstanceSessionsResponse`
        """
        http_info = self._clear_instance_sessions_http_info(request)
        return self._call_api(**http_info)

    def clear_instance_sessions_invoker(self, request):
        http_info = self._clear_instance_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _clear_instance_sessions_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ClearInstanceSessionsResponse"
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

    def compare_configuration(self, request):
        r"""参数模板比较

        比较两个参数模板之间的差异
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CompareConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CompareConfigurationResponse`
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

        复制参数模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CopyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CopyConfigurationResponse`
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

    def create_back(self, request):
        r"""创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBack
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateBackRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateBackResponse`
        """
        http_info = self._create_back_http_info(request)
        return self._call_api(**http_info)

    def create_back_invoker(self, request):
        http_info = self._create_back_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_back_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBackResponse"
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

    def create_cold_volume(self, request):
        r"""‘创建冷数据存储’

        ‘创建冷数据存储’
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateColdVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateColdVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateColdVolumeResponse`
        """
        http_info = self._create_cold_volume_http_info(request)
        return self._call_api(**http_info)

    def create_cold_volume_invoker(self, request):
        http_info = self._create_cold_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_cold_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/cold-volume",
            "request_type": request.__class__.__name__,
            "response_type": "CreateColdVolumeResponse"
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

    def create_configuration(self, request):
        r"""创建参数模板

        创建参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateConfigurationResponse`
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

    def create_db_cache_mapping(self, request):
        r"""创建内存加速映射

        创建内存加速映射。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbCacheMapping
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDbCacheMappingRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDbCacheMappingResponse`
        """
        http_info = self._create_db_cache_mapping_http_info(request)
        return self._call_api(**http_info)

    def create_db_cache_mapping_invoker(self, request):
        http_info = self._create_db_cache_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_db_cache_mapping_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dbcache/mapping",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbCacheMappingResponse"
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

    def create_db_cache_rule(self, request):
        r"""创建内存加速规则

        创建内存加速规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbCacheRule
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDbCacheRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDbCacheRuleResponse`
        """
        http_info = self._create_db_cache_rule_http_info(request)
        return self._call_api(**http_info)

    def create_db_cache_rule_invoker(self, request):
        http_info = self._create_db_cache_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_db_cache_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/dbcache/rule",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbCacheRuleResponse"
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

    def create_db_user(self, request):
        r"""创建Redis数据库账号

        在Redis实例中创建数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDbUser
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDbUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDbUserResponse`
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
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/db-users",
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

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_disaster_recovery(self, request):
        r"""搭建实例与特定实例的容灾关系

        搭建实例与特定实例的容灾关系。 该接口需要对搭建容灾关系的两个实例分别各调用一次，2次接口都调用成功才能成功搭建容灾关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDisasterRecovery
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDisasterRecoveryResponse`
        """
        http_info = self._create_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def create_disaster_recovery_invoker(self, request):
        http_info = self._create_disaster_recovery_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_disaster_recovery_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery/construction",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDisasterRecoveryResponse"
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

    def create_gemini_db_dual_active(self, request):
        r"""搭建双活

        为了实现跨区域实例数据同步，GeminiDB提供了异地双活功能，即创建异地双活实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGeminiDbDualActive
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateGeminiDbDualActiveRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateGeminiDbDualActiveResponse`
        """
        http_info = self._create_gemini_db_dual_active_http_info(request)
        return self._call_api(**http_info)

    def create_gemini_db_dual_active_invoker(self, request):
        http_info = self._create_gemini_db_dual_active_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gemini_db_dual_active_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dual-active-relationship",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGeminiDbDualActiveResponse"
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

        创建数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceResponse`
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

    def delete_backup(self, request):
        r"""删除手动备份

        删除手动备份
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteBackupResponse`
        """
        http_info = self._delete_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_invoker(self, request):
        http_info = self._delete_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupResponse"
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

    def delete_configuration(self, request):
        r"""删除参数模板

        删除指定参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteConfigurationResponse`
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

    def delete_db_cache_mapping(self, request):
        r"""解除内存加速映射

        解除指定内存加速映射。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbCacheMapping
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDbCacheMappingRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDbCacheMappingResponse`
        """
        http_info = self._delete_db_cache_mapping_http_info(request)
        return self._call_api(**http_info)

    def delete_db_cache_mapping_invoker(self, request):
        http_info = self._delete_db_cache_mapping_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_db_cache_mapping_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dbcache/mapping",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbCacheMappingResponse"
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

    def delete_db_cache_rule(self, request):
        r"""删除内存加速规则

        删除内存加速规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbCacheRule
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDbCacheRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDbCacheRuleResponse`
        """
        http_info = self._delete_db_cache_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_db_cache_rule_invoker(self, request):
        http_info = self._delete_db_cache_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_db_cache_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/dbcache/rule",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbCacheRuleResponse"
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

    def delete_db_user(self, request):
        r"""删除Redis数据库账号

        删除Redis实例的数据库账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbUser
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDbUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDbUserResponse`
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
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/db-users",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbUserResponse"
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

    def delete_disaster_recovery(self, request):
        r"""解除实例与特定实例的容灾关系

        解除实例与特定实例的容灾关系。 该接口需要对搭建容灾关系的两个实例分别各调用一次，2次接口都调用成功才能成功解除容灾关系。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDisasterRecovery
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDisasterRecoveryResponse`
        """
        http_info = self._delete_disaster_recovery_http_info(request)
        return self._call_api(**http_info)

    def delete_disaster_recovery_invoker(self, request):
        http_info = self._delete_disaster_recovery_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_disaster_recovery_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery/deconstruction",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDisasterRecoveryResponse"
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

    def delete_enlarge_fail_node(self, request):
        r"""删除扩容失败的节点

        删除扩容失败的节点
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnlargeFailNode
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteEnlargeFailNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteEnlargeFailNodeResponse`
        """
        http_info = self._delete_enlarge_fail_node_http_info(request)
        return self._call_api(**http_info)

    def delete_enlarge_fail_node_invoker(self, request):
        http_info = self._delete_enlarge_fail_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_enlarge_fail_node_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/enlarge-failed-nodes",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnlargeFailNodeResponse"
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

    def delete_gemini_db_dual_active(self, request):
        r"""解除双活

        解除跨区域双活。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGeminiDbDualActive
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteGeminiDbDualActiveRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteGeminiDbDualActiveResponse`
        """
        http_info = self._delete_gemini_db_dual_active_http_info(request)
        return self._call_api(**http_info)

    def delete_gemini_db_dual_active_invoker(self, request):
        http_info = self._delete_gemini_db_dual_active_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gemini_db_dual_active_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dual-active-relationship",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGeminiDbDualActiveResponse"
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

    def delete_instance(self, request):
        r"""删除实例

        删除数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteInstanceResponse`
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

    def delete_instances_session(self, request):
        r"""关闭实例节点会话

        关闭实例节点会话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstancesSession
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteInstancesSessionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteInstancesSessionResponse`
        """
        http_info = self._delete_instances_session_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_session_invoker(self, request):
        http_info = self._delete_instances_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instances_session_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/redis/nodes/{node_id}/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesSessionResponse"
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

    def delete_lts_configs(self, request):
        r"""解除关联LTS日志流

        将实例日志与LTS日志流解除关联，后台将取消上传实例日志到的LTS日志流里。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLtsConfigs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteLtsConfigsResponse`
        """
        http_info = self._delete_lts_configs_http_info(request)
        return self._call_api(**http_info)

    def delete_lts_configs_invoker(self, request):
        http_info = self._delete_lts_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_lts_configs_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLtsConfigsResponse"
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

    def delete_redis_disabled_commands(self, request):
        r"""删除Redis禁用命令

        删除Redis禁用命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRedisDisabledCommands
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteRedisDisabledCommandsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteRedisDisabledCommandsResponse`
        """
        http_info = self._delete_redis_disabled_commands_http_info(request)
        return self._call_api(**http_info)

    def delete_redis_disabled_commands_invoker(self, request):
        http_info = self._delete_redis_disabled_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_redis_disabled_commands_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/disabled-commands",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRedisDisabledCommandsResponse"
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

    def expand_instance_node(self, request):
        r"""扩容指定集群实例的节点数量

        扩容指定集群实例的节点数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandInstanceNode
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ExpandInstanceNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ExpandInstanceNodeResponse`
        """
        http_info = self._expand_instance_node_http_info(request)
        return self._call_api(**http_info)

    def expand_instance_node_invoker(self, request):
        http_info = self._expand_instance_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_instance_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/enlarge-node",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandInstanceNodeResponse"
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

    def list_available_flavor_infos(self, request):
        r"""查询实例可变更规格

        查询实例可变更规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailableFlavorInfos
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListAvailableFlavorInfosRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListAvailableFlavorInfosResponse`
        """
        http_info = self._list_available_flavor_infos_http_info(request)
        return self._call_api(**http_info)

    def list_available_flavor_infos_invoker(self, request):
        http_info = self._list_available_flavor_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_available_flavor_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/available-flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableFlavorInfosResponse"
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

    def list_cassandra_slow_logs(self, request):
        r"""查询GeminiDB(for Cassandra)数据库慢日志

        查询GeminiDB(for Cassandra)数据库慢日志信息，支持日志关键字搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCassandraSlowLogs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListCassandraSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListCassandraSlowLogsResponse`
        """
        http_info = self._list_cassandra_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_cassandra_slow_logs_invoker(self, request):
        http_info = self._list_cassandra_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_cassandra_slow_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/cassandra/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListCassandraSlowLogsResponse"
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

    def list_configuration_datastores(self, request):
        r"""查询支持参数模板的接口信息

        查询支持参数模板的接口信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationDatastores
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationDatastoresRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationDatastoresResponse`
        """
        http_info = self._list_configuration_datastores_http_info(request)
        return self._call_api(**http_info)

    def list_configuration_datastores_invoker(self, request):
        http_info = self._list_configuration_datastores_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configuration_datastores_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/datastores",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationDatastoresResponse"
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

    def list_configuration_templates(self, request):
        r"""获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationTemplates
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationTemplatesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationTemplatesResponse`
        """
        http_info = self._list_configuration_templates_http_info(request)
        return self._call_api(**http_info)

    def list_configuration_templates_invoker(self, request):
        http_info = self._list_configuration_templates_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configuration_templates_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationTemplatesResponse"
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
        if 'datastore_name' in local_var_params:
            query_params.append(('datastore_name', local_var_params['datastore_name']))
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

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationsResponse`
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
        if 'datastore_name' in local_var_params:
            query_params.append(('datastore_name', local_var_params['datastore_name']))
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

    def list_datastores(self, request):
        r"""查询指定实例类型的数据库版本信息

        查询指定实例类型的数据库版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatastores
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDatastoresRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDatastoresResponse`
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
            "resource_path": "/v3/{project_id}/datastores/{datastore_name}/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatastoresResponse"
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

    def list_db_cache_mappings(self, request):
        r"""查询内存加速映射列表和详情

        根据指定条件查询内存加速映射关系列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbCacheMappings
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDbCacheMappingsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDbCacheMappingsResponse`
        """
        http_info = self._list_db_cache_mappings_http_info(request)
        return self._call_api(**http_info)

    def list_db_cache_mappings_invoker(self, request):
        http_info = self._list_db_cache_mappings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_db_cache_mappings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dbcache/mappings",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbCacheMappingsResponse"
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
        if 'source_instance_id' in local_var_params:
            query_params.append(('source_instance_id', local_var_params['source_instance_id']))
        if 'source_instance_name' in local_var_params:
            query_params.append(('source_instance_name', local_var_params['source_instance_name']))
        if 'target_instance_id' in local_var_params:
            query_params.append(('target_instance_id', local_var_params['target_instance_id']))
        if 'target_instance_name' in local_var_params:
            query_params.append(('target_instance_name', local_var_params['target_instance_name']))
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

    def list_db_cache_rules(self, request):
        r"""查询内存加速规则列表和详情

        查询内存加速规则列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbCacheRules
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDbCacheRulesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDbCacheRulesResponse`
        """
        http_info = self._list_db_cache_rules_http_info(request)
        return self._call_api(**http_info)

    def list_db_cache_rules_invoker(self, request):
        http_info = self._list_db_cache_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_db_cache_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dbcache/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbCacheRulesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dbcache_mapping_id' in local_var_params:
            query_params.append(('dbcache_mapping_id', local_var_params['dbcache_mapping_id']))
        if 'rule_id' in local_var_params:
            query_params.append(('rule_id', local_var_params['rule_id']))
        if 'rule_name' in local_var_params:
            query_params.append(('rule_name', local_var_params['rule_name']))
        if 'source_db_schema' in local_var_params:
            query_params.append(('source_db_schema', local_var_params['source_db_schema']))
        if 'source_db_table' in local_var_params:
            query_params.append(('source_db_table', local_var_params['source_db_table']))
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

    def list_db_users(self, request):
        r"""获取Redis数据库账号列表和详情

        获取Redis数据库账号列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDbUsersResponse`
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
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/db-users",
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

    def list_dedicated_resources(self, request):
        r"""查询专属资源列表

        查询专属资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDedicatedResources
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDedicatedResourcesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDedicatedResourcesResponse`
        """
        http_info = self._list_dedicated_resources_http_info(request)
        return self._call_api(**http_info)

    def list_dedicated_resources_invoker(self, request):
        http_info = self._list_dedicated_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_dedicated_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dedicated-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListDedicatedResourcesResponse"
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

    def list_eps_quotas(self, request):
        r"""查询企业项目配额

        查询企业项目配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEpsQuotas
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListEpsQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListEpsQuotasResponse`
        """
        http_info = self._list_eps_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_eps_quotas_invoker(self, request):
        http_info = self._list_eps_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_eps_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/enterprise-projects/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListEpsQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_name' in local_var_params:
            query_params.append(('enterprise_project_name', local_var_params['enterprise_project_name']))
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorInfosRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorInfosResponse`
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
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
        if 'product_type' in local_var_params:
            query_params.append(('product_type', local_var_params['product_type']))
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
        r"""查询指定条件下的所有实例规格信息

        查询指定条件下的所有实例规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorsResponse`
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

    def list_influxdb_slow_logs(self, request):
        r"""查询GeminiDB(for influxdb)数据库慢日志

        查询GeminiDB(for influxdb)数据库慢日志信息，支持日志关键字搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInfluxdbSlowLogs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInfluxdbSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInfluxdbSlowLogsResponse`
        """
        http_info = self._list_influxdb_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_influxdb_slow_logs_invoker(self, request):
        http_info = self._list_influxdb_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_influxdb_slow_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/influxdb/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListInfluxdbSlowLogsResponse"
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

    def list_instance_databases(self, request):
        r"""获取Redis实例数据库列表

        获取Redis实例数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceDatabases
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceDatabasesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceDatabasesResponse`
        """
        http_info = self._list_instance_databases_http_info(request)
        return self._call_api(**http_info)

    def list_instance_databases_invoker(self, request):
        http_info = self._list_instance_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceDatabasesResponse"
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

    def list_instance_maintenance_window(self, request):
        r"""查询实例可维护时间段

        查询实例可维护时间段。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceMaintenanceWindow
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceMaintenanceWindowResponse`
        """
        http_info = self._list_instance_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def list_instance_maintenance_window_invoker(self, request):
        http_info = self._list_instance_maintenance_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_maintenance_window_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ops-window",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceMaintenanceWindowResponse"
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

    def list_instance_sessions(self, request):
        r"""获取实例的会话

        获取实例的会话。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceSessions
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceSessionsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceSessionsResponse`
        """
        http_info = self._list_instance_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_instance_sessions_invoker(self, request):
        http_info = self._list_instance_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_sessions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceSessionsResponse"
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

    def list_instance_tags(self, request):
        r"""查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceTagsResponse`
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

        根据指定条件查询数据库实例列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesResponse`
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
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instances_by_resource_tags(self, request):
        r"""查询资源实例

        根据标签查询指定的数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesByResourceTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByResourceTagsResponse`
        """
        http_info = self._list_instances_by_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instances_by_resource_tags_invoker(self, request):
        http_info = self._list_instances_by_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_by_resource_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/resource-instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesByResourceTagsResponse"
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

    def list_instances_by_tags(self, request):
        r"""查询资源实例

        根据标签查询指定的数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesByTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByTagsResponse`
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
            "resource_path": "/v3/{project_id}/instances/resource_instances/action",
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

    def list_instances_session(self, request):
        r"""获取节点会话列表

        获取节点会话列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesSession
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionResponse`
        """
        http_info = self._list_instances_session_http_info(request)
        return self._call_api(**http_info)

    def list_instances_session_invoker(self, request):
        http_info = self._list_instances_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_session_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/nodes/{node_id}/sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesSessionResponse"
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
        if 'addr_prefix' in local_var_params:
            query_params.append(('addr_prefix', local_var_params['addr_prefix']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_instances_session_statistics(self, request):
        r"""查询实例节点会话统计信息

        查询实例节点会话统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstancesSessionStatistics
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionStatisticsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionStatisticsResponse`
        """
        http_info = self._list_instances_session_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_instances_session_statistics_invoker(self, request):
        http_info = self._list_instances_session_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instances_session_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/nodes/{node_id}/session-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesSessionStatisticsResponse"
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

    def list_jobs(self, request):
        r"""查询任务列表和详情

        查询任务列表和详情，默认查询任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
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

    def list_lts_configs(self, request):
        r"""查询LTS日志配置信息

        分页查询实例关联的LTS日志配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLtsConfigs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListLtsConfigsResponse`
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
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def list_mongodb_error_logs(self, request):
        r"""查询GeminiDB(for Mongo)数据库错误日志

        查询GeminiDB(for Mongo)数据库错误日志信息，支持日志关键字搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMongodbErrorLogs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListMongodbErrorLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListMongodbErrorLogsResponse`
        """
        http_info = self._list_mongodb_error_logs_http_info(request)
        return self._call_api(**http_info)

    def list_mongodb_error_logs_invoker(self, request):
        http_info = self._list_mongodb_error_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_mongodb_error_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/mongodb/instances/{instance_id}/error-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListMongodbErrorLogsResponse"
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

    def list_mongodb_slow_logs(self, request):
        r"""查询GeminiDB(for Mongo)数据库慢日志

        查询GeminiDB(for Mongo)数据库慢日志信息，支持日志关键字搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMongodbSlowLogs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListMongodbSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListMongodbSlowLogsResponse`
        """
        http_info = self._list_mongodb_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_mongodb_slow_logs_invoker(self, request):
        http_info = self._list_mongodb_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_mongodb_slow_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/mongodb/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListMongodbSlowLogsResponse"
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

    def list_nosql_task_list(self, request):
        r"""查询定时任务列表

        根据指定条件查询定时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNosqlTaskList
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListNosqlTaskListRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListNosqlTaskListResponse`
        """
        http_info = self._list_nosql_task_list_http_info(request)
        return self._call_api(**http_info)

    def list_nosql_task_list_invoker(self, request):
        http_info = self._list_nosql_task_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_nosql_task_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/scheduled-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListNosqlTaskListResponse"
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

    def list_project_tags(self, request):
        r"""查询项目标签

        查询指定项目的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListProjectTagsResponse`
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

    def list_recycle_instances(self, request):
        r"""查询回收站实例列表

        查询回收站所有引擎的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRecycleInstancesResponse`
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

    def list_redis_pitr_restore_time(self, request):
        r"""查询Redis可恢复时间点

        查询Redis可恢复时间点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRedisPitrRestoreTime
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRedisPitrRestoreTimeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRedisPitrRestoreTimeResponse`
        """
        http_info = self._list_redis_pitr_restore_time_http_info(request)
        return self._call_api(**http_info)

    def list_redis_pitr_restore_time_invoker(self, request):
        http_info = self._list_redis_pitr_restore_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_redis_pitr_restore_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/pitr/restorable-time-periods",
            "request_type": request.__class__.__name__,
            "response_type": "ListRedisPitrRestoreTimeResponse"
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_redis_slow_logs(self, request):
        r"""查询GeminiDB(for Redis)数据库慢日志

        查询GeminiDB(for Redis)数据库慢日志信息，支持日志关键字搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRedisSlowLogs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRedisSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRedisSlowLogsResponse`
        """
        http_info = self._list_redis_slow_logs_http_info(request)
        return self._call_api(**http_info)

    def list_redis_slow_logs_invoker(self, request):
        http_info = self._list_redis_slow_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_redis_slow_logs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRedisSlowLogsResponse"
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

    def list_restore_databases(self, request):
        r"""获取GeminiDB(for Cassandra)实例表级恢复的数据库信息

        获取GeminiDB(for Cassandra)实例表级恢复的数据库信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreDatabases
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreDatabasesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreDatabasesResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
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

    def list_restore_tables(self, request):
        r"""获取GeminiDB(for Cassandra)实例表级恢复的表信息

        获取GeminiDB(for Cassandra)实例表级恢复的表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreTables
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreTablesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreTablesResponse`
        """
        http_info = self._list_restore_tables_http_info(request)
        return self._call_api(**http_info)

    def list_restore_tables_invoker(self, request):
        http_info = self._list_restore_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restore_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestoreTablesResponse"
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_restore_time(self, request):
        r"""查询实例可恢复的时间段

        查询实例可恢复的时间段
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRestoreTime
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreTimeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreTimeResponse`
        """
        http_info = self._list_restore_time_http_info(request)
        return self._call_api(**http_info)

    def list_restore_time_invoker(self, request):
        http_info = self._list_restore_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_restore_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/restorable-time-periods",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestoreTimeResponse"
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListSlowLogsResponse`
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

    def modify_db_user_privilege(self, request):
        r"""修改Redis数据库帐号权限

        修改Redis数据库帐号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyDbUserPrivilege
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyDbUserPrivilegeResponse`
        """
        http_info = self._modify_db_user_privilege_http_info(request)
        return self._call_api(**http_info)

    def modify_db_user_privilege_invoker(self, request):
        http_info = self._modify_db_user_privilege_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_db_user_privilege_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/db-users/privilege",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyDbUserPrivilegeResponse"
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

    def modify_eps_quotas(self, request):
        r"""修改企业项目配额

        修改企业项目配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyEpsQuotas
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyEpsQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyEpsQuotasResponse`
        """
        http_info = self._modify_eps_quotas_http_info(request)
        return self._call_api(**http_info)

    def modify_eps_quotas_invoker(self, request):
        http_info = self._modify_eps_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_eps_quotas_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/enterprise-projects/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyEpsQuotasResponse"
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

    def modify_instance_maintenance_window(self, request):
        r"""设置实例可维护时间段

        设置指定实例可维护时间段。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyInstanceMaintenanceWindow
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyInstanceMaintenanceWindowRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyInstanceMaintenanceWindowResponse`
        """
        http_info = self._modify_instance_maintenance_window_http_info(request)
        return self._call_api(**http_info)

    def modify_instance_maintenance_window_invoker(self, request):
        http_info = self._modify_instance_maintenance_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_instance_maintenance_window_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/maintenance-window",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyInstanceMaintenanceWindowResponse"
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

    def modify_port(self, request):
        r"""修改数据库端口

        修改数据库实例的端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyPort
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPortRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPortResponse`
        """
        http_info = self._modify_port_http_info(request)
        return self._call_api(**http_info)

    def modify_port_invoker(self, request):
        http_info = self._modify_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/port",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyPortResponse"
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

    def modify_public_ip(self, request):
        r"""绑定/解绑弹性公网IP

        实例下的节点绑定弹性公网IP/解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyPublicIp
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPublicIpRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPublicIpResponse`
        """
        http_info = self._modify_public_ip_http_info(request)
        return self._call_api(**http_info)

    def modify_public_ip_invoker(self, request):
        http_info = self._modify_public_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_public_ip_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/public-ip",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyPublicIpResponse"
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

    def modify_volume(self, request):
        r"""变更实例存储容量

        变更实例的存储容量大小
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyVolumeResponse`
        """
        http_info = self._modify_volume_http_info(request)
        return self._call_api(**http_info)

    def modify_volume_invoker(self, request):
        http_info = self._modify_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_volume_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/volume",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyVolumeResponse"
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

    def offline_nodes(self, request):
        r"""支持节点的开关机

        当底层故障导致节点无法正常工作时，可以对该节点执行关机操作，关机后会由其他节点接管业务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for OfflineNodes
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.OfflineNodesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.OfflineNodesResponse`
        """
        http_info = self._offline_nodes_http_info(request)
        return self._call_api(**http_info)

    def offline_nodes_invoker(self, request):
        http_info = self._offline_nodes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _offline_nodes_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "OfflineNodesResponse"
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

    def pause_resume_data_synchronization(self, request):
        r"""暂停/恢复具备容灾关系的实例数据同步

        该接口用于暂停/恢复具备容灾关系的实例数据同步。
        
        该接口需要对具备容灾关系的两个实例分别各调用一次，2次接口都调用成功才能成功暂停/恢复容灾实例数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PauseResumeDataSynchronization
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.PauseResumeDataSynchronizationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.PauseResumeDataSynchronizationResponse`
        """
        http_info = self._pause_resume_data_synchronization_http_info(request)
        return self._call_api(**http_info)

    def pause_resume_data_synchronization_invoker(self, request):
        http_info = self._pause_resume_data_synchronization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pause_resume_data_synchronization_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery/data-synchronization",
            "request_type": request.__class__.__name__,
            "response_type": "PauseResumeDataSynchronizationResponse"
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

    def reset_db_user_password(self, request):
        r"""重置Redis数据库账号密码

        重置Redis数据库账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetDbUserPassword
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetDbUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetDbUserPasswordResponse`
        """
        http_info = self._reset_db_user_password_http_info(request)
        return self._call_api(**http_info)

    def reset_db_user_password_invoker(self, request):
        http_info = self._reset_db_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_db_user_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/db-users/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetDbUserPasswordResponse"
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

    def reset_param_group_template(self, request):
        r"""重置自定义参数模板

        重置自定义参数模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetParamGroupTemplate
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetParamGroupTemplateRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetParamGroupTemplateResponse`
        """
        http_info = self._reset_param_group_template_http_info(request)
        return self._call_api(**http_info)

    def reset_param_group_template_invoker(self, request):
        http_info = self._reset_param_group_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_param_group_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/reset",
            "request_type": request.__class__.__name__,
            "response_type": "ResetParamGroupTemplateResponse"
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
        r"""修改实例的管理员密码

        修改实例的管理员密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetPasswordResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/password",
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

    def resize_cold_volume(self, request):
        r"""扩容冷数据存储

        扩容冷数据存储。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeColdVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeColdVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeColdVolumeResponse`
        """
        http_info = self._resize_cold_volume_http_info(request)
        return self._call_api(**http_info)

    def resize_cold_volume_invoker(self, request):
        http_info = self._resize_cold_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_cold_volume_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/cold-volume",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeColdVolumeResponse"
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceResponse`
        """
        http_info = self._resize_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_invoker(self, request):
        http_info = self._resize_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
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

        扩容实例的存储容量大小。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeInstanceVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceVolumeResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/extend-volume",
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
        r"""重启实例或节点

        重启实例或节点的数据库服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.RestartInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RestartInstanceResponse`
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

    def restore_existing_instance(self, request):
        r"""恢复到已有实例

        恢复到已有实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreExistingInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreExistingInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreExistingInstanceResponse`
        """
        http_info = self._restore_existing_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_existing_instance_invoker(self, request):
        http_info = self._restore_existing_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_existing_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/recovery",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreExistingInstanceResponse"
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

    def restore_redis_pitr(self, request):
        r"""恢复当前Redis实例到指定时间点

        恢复当前Redis实例到指定时间点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreRedisPitr
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreRedisPitrRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreRedisPitrResponse`
        """
        http_info = self._restore_redis_pitr_http_info(request)
        return self._call_api(**http_info)

    def restore_redis_pitr_invoker(self, request):
        http_info = self._restore_redis_pitr_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_redis_pitr_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/pitr",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreRedisPitrResponse"
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

    def save_lts_configs(self, request):
        r"""关联LTS日志流

        - 将实例日志与LTS日志流关联，后台将自动上传实例日志到关联的LTS日志流里。
        - 关联成功后，会产生一定费用，具体计费可参考云日志服务（LTS）的定价详情。
        - 系统会为当前选择的日志流创建对应日志类型的结构化配置，若该日志流已存在其他日志类型的结构化配置，系统会进行覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveLtsConfigs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SaveLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SaveLtsConfigsResponse`
        """
        http_info = self._save_lts_configs_http_info(request)
        return self._call_api(**http_info)

    def save_lts_configs_invoker(self, request):
        http_info = self._save_lts_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_lts_configs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "SaveLtsConfigsResponse"
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

    def save_redis_disabled_commands(self, request):
        r"""设置Redis禁用命令

        设置Redis禁用命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveRedisDisabledCommands
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SaveRedisDisabledCommandsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SaveRedisDisabledCommandsResponse`
        """
        http_info = self._save_redis_disabled_commands_http_info(request)
        return self._call_api(**http_info)

    def save_redis_disabled_commands_invoker(self, request):
        http_info = self._save_redis_disabled_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_redis_disabled_commands_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/disabled-commands",
            "request_type": request.__class__.__name__,
            "response_type": "SaveRedisDisabledCommandsResponse"
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

    def set_auto_enlarge_policy(self, request):
        r"""设置磁盘自动扩容策略

        设置磁盘自动扩容策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetAutoEnlargePolicyResponse`
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
            "resource_path": "/v3/{project_id}/instances/disk-auto-expansion",
            "request_type": request.__class__.__name__,
            "response_type": "SetAutoEnlargePolicyResponse"
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetBackupPolicyResponse`
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

    def set_disaster_recovery_settings(self, request):
        r"""设置实例容灾切换的故障节点比例

        设置实例容灾切换的故障节点比例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetDisasterRecoverySettings
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetDisasterRecoverySettingsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetDisasterRecoverySettingsResponse`
        """
        http_info = self._set_disaster_recovery_settings_http_info(request)
        return self._call_api(**http_info)

    def set_disaster_recovery_settings_invoker(self, request):
        http_info = self._set_disaster_recovery_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_disaster_recovery_settings_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/disaster-recovery/settings",
            "request_type": request.__class__.__name__,
            "response_type": "SetDisasterRecoverySettingsResponse"
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

    def set_instance_data_dump(self, request):
        r"""开启/关闭实例数据导出

        开启/关闭实例数据导出。
        当前支持将InfluxDB数据转为parquet格式文件然后上传到指定的OBS桶中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetInstanceDataDump
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetInstanceDataDumpRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetInstanceDataDumpResponse`
        """
        http_info = self._set_instance_data_dump_http_info(request)
        return self._call_api(**http_info)

    def set_instance_data_dump_invoker(self, request):
        http_info = self._set_instance_data_dump_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_instance_data_dump_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/data-dump",
            "request_type": request.__class__.__name__,
            "response_type": "SetInstanceDataDumpResponse"
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
        r"""设置回收策略

        设置已删除实例保留天数，修改保留天数后删除的实例按照新的天数保留，修改之前已在回收站的实例保留天数不变。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetRecyclePolicyResponse`
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

    def set_redis_pitr_policy(self, request):
        r"""设置Redis恢复到指定时间点策略

        设置Redis恢复到指定时间点策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRedisPitrPolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetRedisPitrPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetRedisPitrPolicyResponse`
        """
        http_info = self._set_redis_pitr_policy_http_info(request)
        return self._call_api(**http_info)

    def set_redis_pitr_policy_invoker(self, request):
        http_info = self._set_redis_pitr_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_redis_pitr_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/pitr/policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetRedisPitrPolicyResponse"
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

    def show_all_instances_backups(self, request):
        r"""查询备份列表

        根据指定条件查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllInstancesBackups
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAllInstancesBackupsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAllInstancesBackupsResponse`
        """
        http_info = self._show_all_instances_backups_http_info(request)
        return self._call_api(**http_info)

    def show_all_instances_backups_invoker(self, request):
        http_info = self._show_all_instances_backups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_instances_backups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllInstancesBackupsResponse"
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
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'backup_id' in local_var_params:
            query_params.append(('backup_id', local_var_params['backup_id']))
        if 'backup_type' in local_var_params:
            query_params.append(('backup_type', local_var_params['backup_type']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
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

    def show_all_instances_backups_new(self, request):
        r"""查询备份列表（推荐）

        根据指定条件查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllInstancesBackupsNew
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAllInstancesBackupsNewRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAllInstancesBackupsNewResponse`
        """
        http_info = self._show_all_instances_backups_new_http_info(request)
        return self._call_api(**http_info)

    def show_all_instances_backups_new_invoker(self, request):
        http_info = self._show_all_instances_backups_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_instances_backups_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllInstancesBackupsNewResponse"
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
        if 'backup_id' in local_var_params:
            query_params.append(('backup_id', local_var_params['backup_id']))
        if 'backup_type' in local_var_params:
            query_params.append(('backup_type', local_var_params['backup_type']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
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

    def show_applicable_instances(self, request):
        r"""查询参数模板可应用的实例列表

        查询参数模板可应用的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplicableInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplicableInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplicableInstancesResponse`
        """
        http_info = self._show_applicable_instances_http_info(request)
        return self._call_api(**http_info)

    def show_applicable_instances_invoker(self, request):
        http_info = self._show_applicable_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_applicable_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/applicable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplicableInstancesResponse"
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

    def show_apply_history(self, request):
        r"""查询参数模板应用历史

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApplyHistory
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplyHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplyHistoryResponse`
        """
        http_info = self._show_apply_history_http_info(request)
        return self._call_api(**http_info)

    def show_apply_history_invoker(self, request):
        http_info = self._show_apply_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_apply_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/applied-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApplyHistoryResponse"
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

    def show_auto_enlarge_policy(self, request):
        r"""查询磁盘自动扩容策略

        查询磁盘自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAutoEnlargePolicyResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_backup_policies(self, request):
        r"""查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupPolicies
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowBackupPoliciesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowBackupPoliciesResponse`
        """
        http_info = self._show_backup_policies_http_info(request)
        return self._call_api(**http_info)

    def show_backup_policies_invoker(self, request):
        http_info = self._show_backup_policies_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_policies_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/backups/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupPoliciesResponse"
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

    def show_backup_policy(self, request):
        r"""查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowBackupPolicyResponse`
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

    def show_configuration_detail(self, request):
        r"""获取指定参数模板的参数

        获取指定参数模板的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConfigurationDetail
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowConfigurationDetailRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowConfigurationDetailResponse`
        """
        http_info = self._show_configuration_detail_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_detail_invoker(self, request):
        http_info = self._show_configuration_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_configuration_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigurationDetailResponse"
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

    def show_disaster_recovery_settings(self, request):
        r"""查询实例容灾切换的故障节点比例

        查询实例容灾切换的故障节点比例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDisasterRecoverySettings
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowDisasterRecoverySettingsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowDisasterRecoverySettingsResponse`
        """
        http_info = self._show_disaster_recovery_settings_http_info(request)
        return self._call_api(**http_info)

    def show_disaster_recovery_settings_invoker(self, request):
        http_info = self._show_disaster_recovery_settings_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_disaster_recovery_settings_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/disaster-recovery/settings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDisasterRecoverySettingsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
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

    def show_elb_ip_group(self, request):
        r"""查询实例负载均衡的IP访问黑白名单

        查询实例负载均衡的IP访问黑白名单。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowElbIpGroup
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowElbIpGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowElbIpGroupResponse`
        """
        http_info = self._show_elb_ip_group_http_info(request)
        return self._call_api(**http_info)

    def show_elb_ip_group_invoker(self, request):
        http_info = self._show_elb_ip_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_elb_ip_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lb/access-control",
            "request_type": request.__class__.__name__,
            "response_type": "ShowElbIpGroupResponse"
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

    def show_error_log(self, request):
        r"""查询数据库错误日志信息

        查询数据库错误日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowErrorLog
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowErrorLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowErrorLogResponse`
        """
        http_info = self._show_error_log_http_info(request)
        return self._call_api(**http_info)

    def show_error_log_invoker(self, request):
        http_info = self._show_error_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_error_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/error-log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowErrorLogResponse"
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

    def show_high_risk_commands(self, request):
        r"""查询高危命令

        查询Redis的高危命令
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHighRiskCommands
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowHighRiskCommandsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowHighRiskCommandsResponse`
        """
        http_info = self._show_high_risk_commands_http_info(request)
        return self._call_api(**http_info)

    def show_high_risk_commands_invoker(self, request):
        http_info = self._show_high_risk_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_high_risk_commands_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/high-risk-commands",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHighRiskCommandsResponse"
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

    def show_instance_biactive_regions(self, request):
        r"""查询实例可搭建双活关系的Region

        查询实例可搭建双活关系的Region。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceBiactiveRegions
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceBiactiveRegionsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceBiactiveRegionsResponse`
        """
        http_info = self._show_instance_biactive_regions_http_info(request)
        return self._call_api(**http_info)

    def show_instance_biactive_regions_invoker(self, request):
        http_info = self._show_instance_biactive_regions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_biactive_regions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery/regions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceBiactiveRegionsResponse"
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

    def show_instance_configuration(self, request):
        r"""查询实例参数配置

        查询实例参数配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceConfigurationResponse`
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_instance_role(self, request):
        r"""获取容灾实例主/备角色信息

        该接口用于获取容灾实例主/备角色信息，以便后续容灾实例备升主和容灾实例主降备接口调用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceRole
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceRoleRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceRoleResponse`
        """
        http_info = self._show_instance_role_http_info(request)
        return self._call_api(**http_info)

    def show_instance_role_invoker(self, request):
        http_info = self._show_instance_role_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_role_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/instance-role",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceRoleResponse"
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

    def show_ip_num_requirement(self, request):
        r"""查询创建实例或扩容节点时需要的IP数量

        查询创建实例或扩容节点时需要的IP数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIpNumRequirement
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowIpNumRequirementRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowIpNumRequirementResponse`
        """
        http_info = self._show_ip_num_requirement_http_info(request)
        return self._call_api(**http_info)

    def show_ip_num_requirement_invoker(self, request):
        http_info = self._show_ip_num_requirement_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_ip_num_requirement_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/ip-num-requirement",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIpNumRequirementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'node_num' in local_var_params:
            query_params.append(('node_num', local_var_params['node_num']))
        if 'engine_name' in local_var_params:
            query_params.append(('engine_name', local_var_params['engine_name']))
        if 'instance_mode' in local_var_params:
            query_params.append(('instance_mode', local_var_params['instance_mode']))
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

    def show_modify_history(self, request):
        r"""查询实例参数的修改历史

        查询实例参数的修改历史
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowModifyHistory
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowModifyHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowModifyHistoryResponse`
        """
        http_info = self._show_modify_history_http_info(request)
        return self._call_api(**http_info)

    def show_modify_history_invoker(self, request):
        http_info = self._show_modify_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_modify_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configuration-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModifyHistoryResponse"
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

    def show_passwordless_config(self, request):
        r"""获取GeminiDB Redis的免密配置

        获取GeminiDB Redis的免密配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPasswordlessConfig
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowPasswordlessConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowPasswordlessConfigResponse`
        """
        http_info = self._show_passwordless_config_http_info(request)
        return self._call_api(**http_info)

    def show_passwordless_config_invoker(self, request):
        http_info = self._show_passwordless_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_passwordless_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/passwordless-config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPasswordlessConfigResponse"
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

    def show_pause_resume_stutus(self, request):
        r"""获取容灾实例数据同步状态

        获取容灾实例数据同步状态，主备实例id，数据同步指标值，以及倒换和切换场景下的RPO，RTO指标值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPauseResumeStutus
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowPauseResumeStutusRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowPauseResumeStutusResponse`
        """
        http_info = self._show_pause_resume_stutus_http_info(request)
        return self._call_api(**http_info)

    def show_pause_resume_stutus_invoker(self, request):
        http_info = self._show_pause_resume_stutus_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pause_resume_stutus_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/disaster-recovery/data-synchronization",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPauseResumeStutusResponse"
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

    def show_quotas(self, request):
        r"""查询配额

        查询单租户在GeminiDB服务下的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowQuotasResponse`
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
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))
        if 'product_type' in local_var_params:
            query_params.append(('product_type', local_var_params['product_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        r"""查询回收策略

        查询回收策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRecyclePolicyResponse`
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

    def show_redis_big_keys(self, request):
        r"""查询Redis实例的大key

        支持查询Redis实例的大key。value长度大于bigkeys-string-threshold参数的string类型的key或者元素数大于bigkeys-composite-threshold参数的hash/list/zset/set/stream类型key，会被判断为大key。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRedisBigKeys
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisBigKeysRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisBigKeysResponse`
        """
        http_info = self._show_redis_big_keys_http_info(request)
        return self._call_api(**http_info)

    def show_redis_big_keys_invoker(self, request):
        http_info = self._show_redis_big_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_redis_big_keys_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/big-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRedisBigKeysResponse"
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

    def show_redis_disabled_commands(self, request):
        r"""查询Redis禁用命令

        查询Redis禁用命令。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRedisDisabledCommands
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisDisabledCommandsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisDisabledCommandsResponse`
        """
        http_info = self._show_redis_disabled_commands_http_info(request)
        return self._call_api(**http_info)

    def show_redis_disabled_commands_invoker(self, request):
        http_info = self._show_redis_disabled_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_redis_disabled_commands_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/disabled-commands",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRedisDisabledCommandsResponse"
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

    def show_redis_hot_keys(self, request):
        r"""查询Redis实例的热key

        支持查询Redis实例的热key。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRedisHotKeys
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisHotKeysRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisHotKeysResponse`
        """
        http_info = self._show_redis_hot_keys_http_info(request)
        return self._call_api(**http_info)

    def show_redis_hot_keys_invoker(self, request):
        http_info = self._show_redis_hot_keys_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_redis_hot_keys_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/hot-keys",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRedisHotKeysResponse"
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

    def show_redis_pitr_info(self, request):
        r"""查询Redis实例指定时间点恢复所占用的存储空间

        查询Redis实例指定时间点恢复所占用的存储空间。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRedisPitrInfo
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisPitrInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisPitrInfoResponse`
        """
        http_info = self._show_redis_pitr_info_http_info(request)
        return self._call_api(**http_info)

    def show_redis_pitr_info_invoker(self, request):
        http_info = self._show_redis_pitr_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_redis_pitr_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/pitr",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRedisPitrInfoResponse"
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

    def show_redis_pitr_policy(self, request):
        r"""查询Redis恢复到指定时间点策略

        查询Redis恢复到指定时间点策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRedisPitrPolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisPitrPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRedisPitrPolicyResponse`
        """
        http_info = self._show_redis_pitr_policy_http_info(request)
        return self._call_api(**http_info)

    def show_redis_pitr_policy_invoker(self, request):
        http_info = self._show_redis_pitr_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_redis_pitr_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/redis/instances/{instance_id}/pitr/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRedisPitrPolicyResponse"
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

    def show_restorable_list(self, request):
        r"""查询可恢复的实例列表

        查询用户可恢复的实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRestorableList
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRestorableListRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRestorableListResponse`
        """
        http_info = self._show_restorable_list_http_info(request)
        return self._call_api(**http_info)

    def show_restorable_list_invoker(self, request):
        http_info = self._show_restorable_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_restorable_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups/{backup_id}/restorable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRestorableListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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

    def show_second_level_monitoring_status(self, request):
        r"""查询秒级监控配置

        查询秒级监控配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSecondLevelMonitoringStatus
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowSecondLevelMonitoringStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowSecondLevelMonitoringStatusResponse`
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

    def show_slow_log_desensitization(self, request):
        r"""查询慢日志脱敏状态

        查询慢日志脱敏状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowLogDesensitization
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowSlowLogDesensitizationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowSlowLogDesensitizationResponse`
        """
        http_info = self._show_slow_log_desensitization_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_desensitization_invoker(self, request):
        http_info = self._show_slow_log_desensitization_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slow_log_desensitization_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-desensitization",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogDesensitizationResponse"
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

    def shrink_instance_node(self, request):
        r"""缩容指定集群实例的节点数量

        缩容指定集群实例的节点数量。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkInstanceNode
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShrinkInstanceNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShrinkInstanceNodeResponse`
        """
        http_info = self._shrink_instance_node_http_info(request)
        return self._call_api(**http_info)

    def shrink_instance_node_invoker(self, request):
        http_info = self._shrink_instance_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _shrink_instance_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/reduce-node",
            "request_type": request.__class__.__name__,
            "response_type": "ShrinkInstanceNodeResponse"
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.StopBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.StopBackupResponse`
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

    def switch_ip_group(self, request):
        r"""设置实例负载均衡的IP访问黑白名单

        设置实例负载均衡的IP访问黑白名单，黑名单、白名单只能选一种，每次调用此接口覆盖之前的设置。关闭后不限制连接的源IP地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchIpGroup
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchIpGroupResponse`
        """
        http_info = self._switch_ip_group_http_info(request)
        return self._call_api(**http_info)

    def switch_ip_group_invoker(self, request):
        http_info = self._switch_ip_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_ip_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/lb/access-control",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchIpGroupResponse"
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

    def switch_over(self, request):
        r"""Redis主备切换

        切换实例的主备节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchOver
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchOverRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchOverResponse`
        """
        http_info = self._switch_over_http_info(request)
        return self._call_api(**http_info)

    def switch_over_invoker(self, request):
        http_info = self._switch_over_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_over_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instance/{instance_id}/switchover",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchOverResponse"
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

    def switch_second_level_monitoring(self, request):
        r"""开启/关闭秒级监控

        开启或关闭指定实例的5秒级监控。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSecondLevelMonitoring
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSecondLevelMonitoringRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSecondLevelMonitoringResponse`
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
        r"""设置慢日志脱敏状态

        设置慢日志脱敏状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSlowlogDesensitization
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSlowlogDesensitizationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSlowlogDesensitizationResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog-desensitization",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchSlowlogDesensitizationResponse"
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

    def switch_ssl(self, request):
        r"""切换实例SSL开关

        切换实例SSL开关。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchSsl
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSslRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSslResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ssl-option",
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

    def switch_to_master(self, request):
        r"""容灾实例备升主

        该接口用于对已经搭建容灾关系的实例，将备实例升级为主实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchToMaster
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToMasterRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToMasterResponse`
        """
        http_info = self._switch_to_master_http_info(request)
        return self._call_api(**http_info)

    def switch_to_master_invoker(self, request):
        http_info = self._switch_to_master_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_to_master_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switchover-master",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchToMasterResponse"
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

    def switch_to_slave(self, request):
        r"""容灾实例主降备

        该接口用于对已经搭建容灾关系的实例，将主实例降级为备实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchToSlave
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToSlaveRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToSlaveResponse`
        """
        http_info = self._switch_to_slave_http_info(request)
        return self._call_api(**http_info)

    def switch_to_slave_invoker(self, request):
        http_info = self._switch_to_slave_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_to_slave_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switchover-slave",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchToSlaveResponse"
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
        r"""修改副本集跨网段访问配置

        修改副本集跨网段访问配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClientNetwork
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateClientNetworkRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateClientNetworkResponse`
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

    def update_configuration(self, request):
        r"""修改参数模板参数

        修改参数模板参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateConfigurationResponse`
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

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_databases(self, request):
        r"""操作GeminDB实例数据库

        操作GeminDB实例数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabases
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateDatabasesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateDatabasesResponse`
        """
        http_info = self._update_databases_http_info(request)
        return self._call_api(**http_info)

    def update_databases_invoker(self, request):
        http_info = self._update_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_databases_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDatabasesResponse"
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

    def update_db_cache_rule(self, request):
        r"""修改内存加速规则

        修改指定内存加速规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbCacheRule
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateDbCacheRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateDbCacheRuleResponse`
        """
        http_info = self._update_db_cache_rule_http_info(request)
        return self._call_api(**http_info)

    def update_db_cache_rule_invoker(self, request):
        http_info = self._update_db_cache_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_cache_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/dbcache/rule",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbCacheRuleResponse"
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

    def update_high_risk_commands(self, request):
        r"""修改高危命令

        批量修改高危命令
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateHighRiskCommands
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateHighRiskCommandsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateHighRiskCommandsResponse`
        """
        http_info = self._update_high_risk_commands_http_info(request)
        return self._call_api(**http_info)

    def update_high_risk_commands_invoker(self, request):
        http_info = self._update_high_risk_commands_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_high_risk_commands_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/high-risk-commands",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateHighRiskCommandsResponse"
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

    def update_instance_configuration(self, request):
        r"""修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceConfigurationResponse`
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

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_instance_configurations(self, request):
        r"""修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfigurations
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceConfigurationsResponse`
        """
        http_info = self._update_instance_configurations_http_info(request)
        return self._call_api(**http_info)

    def update_instance_configurations_invoker(self, request):
        http_info = self._update_instance_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_configurations_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceConfigurationsResponse"
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceNameResponse`
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

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def update_passwordless_config(self, request):
        r"""支持修改GeminiDB Redis的免密配置

        支持修改GeminiDB Redis的免密配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePasswordlessConfig
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdatePasswordlessConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdatePasswordlessConfigResponse`
        """
        http_info = self._update_passwordless_config_http_info(request)
        return self._call_api(**http_info)

    def update_passwordless_config_invoker(self, request):
        http_info = self._update_passwordless_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_passwordless_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/passwordless-config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePasswordlessConfigResponse"
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateSecurityGroupResponse`
        """
        http_info = self._update_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_security_group_invoker(self, request):
        http_info = self._update_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/security-group",
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

    def upgrade_db_version(self, request):
        r"""数据库补丁升级

        升级数据库补丁版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeDbVersion
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpgradeDbVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpgradeDbVersionResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-upgrade",
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

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListApiVersionResponse`
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApiVersionResponse`
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

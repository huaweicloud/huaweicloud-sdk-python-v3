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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkgaussdb'")


class GaussDBClient(Client):
    def __init__(self):
        super(GaussDBClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgaussdb.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GaussDBClient":
                raise TypeError("client type error, support client type is GaussDBClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_database_permission(self, request):
        """授予数据库用户数据库权限

        授予云数据库 GaussDB(for MySQL)实例数据库用户数据库权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDatabasePermission
        :type request: :class:`huaweicloudsdkgaussdb.v3.AddDatabasePermissionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.AddDatabasePermissionResponse`
        """
        http_info = self._add_database_permission_http_info(request)
        return self._call_api(**http_info)

    def add_database_permission_invoker(self, request):
        http_info = self._add_database_permission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_database_permission_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/privilege",
            "request_type": request.__class__.__name__,
            "response_type": "AddDatabasePermissionResponse"
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

    def batch_tag_action(self, request):
        """批量添加或删除标签

        批量添加或删除指定实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkgaussdb.v3.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.BatchTagActionResponse`
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

    def cancel_gauss_my_sql_instance_eip(self, request):
        """解绑弹性公网IP

        实例解绑弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelGaussMySqlInstanceEip
        :type request: :class:`huaweicloudsdkgaussdb.v3.CancelGaussMySqlInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CancelGaussMySqlInstanceEipResponse`
        """
        http_info = self._cancel_gauss_my_sql_instance_eip_http_info(request)
        return self._call_api(**http_info)

    def cancel_gauss_my_sql_instance_eip_invoker(self, request):
        http_info = self._cancel_gauss_my_sql_instance_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_gauss_my_sql_instance_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/public-ips/unbind",
            "request_type": request.__class__.__name__,
            "response_type": "CancelGaussMySqlInstanceEipResponse"
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

    def cancel_schedule_task(self, request):
        """取消定时任务

        取消定时任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelScheduleTask
        :type request: :class:`huaweicloudsdkgaussdb.v3.CancelScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CancelScheduleTaskResponse`
        """
        http_info = self._cancel_schedule_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_schedule_task_invoker(self, request):
        http_info = self._cancel_schedule_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_schedule_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/scheduled-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CancelScheduleTaskResponse"
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

    def change_gauss_my_sql_instance_specification(self, request):
        """变更实例规格

        变更数据库实例的规格。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeGaussMySqlInstanceSpecification
        :type request: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlInstanceSpecificationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlInstanceSpecificationResponse`
        """
        http_info = self._change_gauss_my_sql_instance_specification_http_info(request)
        return self._call_api(**http_info)

    def change_gauss_my_sql_instance_specification_invoker(self, request):
        http_info = self._change_gauss_my_sql_instance_specification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_gauss_my_sql_instance_specification_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeGaussMySqlInstanceSpecificationResponse"
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

    def change_gauss_my_sql_proxy_specification(self, request):
        """数据库代理规格变更

        数据库代理规格变更。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeGaussMySqlProxySpecification
        :type request: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlProxySpecificationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlProxySpecificationResponse`
        """
        http_info = self._change_gauss_my_sql_proxy_specification_http_info(request)
        return self._call_api(**http_info)

    def change_gauss_my_sql_proxy_specification_invoker(self, request):
        http_info = self._change_gauss_my_sql_proxy_specification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_gauss_my_sql_proxy_specification_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/flavor",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeGaussMySqlProxySpecificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def check_resource(self, request):
        """资源预校验

        资源预校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckResource
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckResourceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckResourceResponse`
        """
        http_info = self._check_resource_http_info(request)
        return self._call_api(**http_info)

    def check_resource_invoker(self, request):
        http_info = self._check_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/resource-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckResourceResponse"
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

    def copy_configurations(self, request):
        """复制参数组

        复制参数组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.CopyConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CopyConfigurationsResponse`
        """
        http_info = self._copy_configurations_http_info(request)
        return self._call_api(**http_info)

    def copy_configurations_invoker(self, request):
        http_info = self._copy_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_configurations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def copy_instance_configurations(self, request):
        """复制实例参数组

        复制实例参数组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyInstanceConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.CopyInstanceConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CopyInstanceConfigurationsResponse`
        """
        http_info = self._copy_instance_configurations_http_info(request)
        return self._call_api(**http_info)

    def copy_instance_configurations_invoker(self, request):
        http_info = self._copy_instance_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _copy_instance_configurations_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations/{configuration_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyInstanceConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def create_access_control(self, request):
        """设置访问控制规则

        设置访问控制规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAccessControl
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateAccessControlRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateAccessControlResponse`
        """
        http_info = self._create_access_control_http_info(request)
        return self._call_api(**http_info)

    def create_access_control_invoker(self, request):
        http_info = self._create_access_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_access_control_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/access-control",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAccessControlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def create_gauss_my_sql_backup(self, request):
        """创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlBackup
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlBackupResponse`
        """
        http_info = self._create_gauss_my_sql_backup_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_backup_invoker(self, request):
        http_info = self._create_gauss_my_sql_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_backup_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/backups/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlBackupResponse"
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

    def create_gauss_my_sql_configuration(self, request):
        """创建参数模板

        创建参数模板信息，包含参数模板名称、描述、数据库版本信息、参数值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlConfigurationResponse`
        """
        http_info = self._create_gauss_my_sql_configuration_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_configuration_invoker(self, request):
        http_info = self._create_gauss_my_sql_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_configuration_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlConfigurationResponse"
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

    def create_gauss_my_sql_database(self, request):
        """创建数据库

        创建云数据库 GaussDB(for MySQL)实例数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseResponse`
        """
        http_info = self._create_gauss_my_sql_database_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_database_invoker(self, request):
        http_info = self._create_gauss_my_sql_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlDatabaseResponse"
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

    def create_gauss_my_sql_database_user(self, request):
        """创建数据库用户

        创建云数据库GaussDB(for MySQL)实例数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseUserResponse`
        """
        http_info = self._create_gauss_my_sql_database_user_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_database_user_invoker(self, request):
        http_info = self._create_gauss_my_sql_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_database_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlDatabaseUserResponse"
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

    def create_gauss_my_sql_instance(self, request):
        """创建数据库实例

        创建云数据库GaussDB(for MySQL)实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlInstanceResponse`
        """
        http_info = self._create_gauss_my_sql_instance_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_instance_invoker(self, request):
        http_info = self._create_gauss_my_sql_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlInstanceResponse"
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

    def create_gauss_my_sql_proxy(self, request):
        """开启数据库代理

        开启数据库代理，只支持ELB模式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlProxyResponse`
        """
        http_info = self._create_gauss_my_sql_proxy_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_proxy_invoker(self, request):
        http_info = self._create_gauss_my_sql_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_proxy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlProxyResponse"
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

    def create_gauss_my_sql_readonly_node(self, request):
        """创建只读节点

        创建只读节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMySqlReadonlyNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlReadonlyNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlReadonlyNodeResponse`
        """
        http_info = self._create_gauss_my_sql_readonly_node_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_my_sql_readonly_node_invoker(self, request):
        http_info = self._create_gauss_my_sql_readonly_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_my_sql_readonly_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/enlarge",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMySqlReadonlyNodeResponse"
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

    def create_gauss_mysql_dns(self, request):
        """申请内网域名

        申请内网域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGaussMysqlDns
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMysqlDnsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMysqlDnsResponse`
        """
        http_info = self._create_gauss_mysql_dns_http_info(request)
        return self._call_api(**http_info)

    def create_gauss_mysql_dns_invoker(self, request):
        http_info = self._create_gauss_mysql_dns_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_gauss_mysql_dns_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGaussMysqlDnsResponse"
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

    def create_lts_configs(self, request):
        """批量创建LTS日志配置

        批量创建LTS日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLtsConfigs
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateLtsConfigsResponse`
        """
        http_info = self._create_lts_configs_http_info(request)
        return self._call_api(**http_info)

    def create_lts_configs_invoker(self, request):
        http_info = self._create_lts_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_lts_configs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLtsConfigsResponse"
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

    def create_restore_tables(self, request):
        """表级时间点恢复

        表级时间点恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRestoreTables
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateRestoreTablesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateRestoreTablesResponse`
        """
        http_info = self._create_restore_tables_http_info(request)
        return self._call_api(**http_info)

    def create_restore_tables_invoker(self, request):
        http_info = self._create_restore_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_restore_tables_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/restore/tables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRestoreTablesResponse"
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

    def delete_database_permission(self, request):
        """删除数据库用户的数据库权限

        删除云数据库 GaussDB(for MySQL)实例数据库用户的数据库权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabasePermission
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteDatabasePermissionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteDatabasePermissionResponse`
        """
        http_info = self._delete_database_permission_http_info(request)
        return self._call_api(**http_info)

    def delete_database_permission_invoker(self, request):
        http_info = self._delete_database_permission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_database_permission_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/privilege",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabasePermissionResponse"
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

    def delete_gauss_my_sql_backup(self, request):
        """删除手动备份

        删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlBackup
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlBackupResponse`
        """
        http_info = self._delete_gauss_my_sql_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_backup_invoker(self, request):
        http_info = self._delete_gauss_my_sql_backup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_backup_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlBackupResponse"
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

    def delete_gauss_my_sql_configuration(self, request):
        """删除参数模板

        删除指定参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlConfigurationResponse`
        """
        http_info = self._delete_gauss_my_sql_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_configuration_invoker(self, request):
        http_info = self._delete_gauss_my_sql_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_configuration_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def delete_gauss_my_sql_database(self, request):
        """删除数据库

        删除云数据库 GaussDB(for MySQL)实例数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseResponse`
        """
        http_info = self._delete_gauss_my_sql_database_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_database_invoker(self, request):
        http_info = self._delete_gauss_my_sql_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlDatabaseResponse"
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

    def delete_gauss_my_sql_database_user(self, request):
        """删除数据库用户

        删除云数据库 GaussDB(for MySQL)实例数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseUserResponse`
        """
        http_info = self._delete_gauss_my_sql_database_user_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_database_user_invoker(self, request):
        http_info = self._delete_gauss_my_sql_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_database_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlDatabaseUserResponse"
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

    def delete_gauss_my_sql_instance(self, request):
        """删除/退订数据库实例

        删除/退订数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlInstanceResponse`
        """
        http_info = self._delete_gauss_my_sql_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_instance_invoker(self, request):
        http_info = self._delete_gauss_my_sql_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlInstanceResponse"
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

    def delete_gauss_my_sql_proxy(self, request):
        """关闭数据库代理

        关闭数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlProxyResponse`
        """
        http_info = self._delete_gauss_my_sql_proxy_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_proxy_invoker(self, request):
        http_info = self._delete_gauss_my_sql_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_proxy_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlProxyResponse"
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

    def delete_gauss_my_sql_readonly_node(self, request):
        """删除/退订只读节点

        删除/退订实例的只读节点。多可用区模式删除/退订只读节点时，要保证删除/退订后，剩余的只读节点和主节点在不同的可用区中，否则无法删除/退订该只读节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGaussMySqlReadonlyNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlReadonlyNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlReadonlyNodeResponse`
        """
        http_info = self._delete_gauss_my_sql_readonly_node_http_info(request)
        return self._call_api(**http_info)

    def delete_gauss_my_sql_readonly_node_invoker(self, request):
        http_info = self._delete_gauss_my_sql_readonly_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_gauss_my_sql_readonly_node_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGaussMySqlReadonlyNodeResponse"
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

    def delete_lts_configs(self, request):
        """批量删除LTS日志配置

        批量删除LTS日志配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLtsConfigs
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteLtsConfigsResponse`
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
            "resource_path": "/v3/{project_id}/logs/lts-configs",
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

    def delete_schedule_tas_k(self, request):
        """删除定时任务

        删除定时任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScheduleTasK
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteScheduleTasKRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteScheduleTasKResponse`
        """
        http_info = self._delete_schedule_tas_k_http_info(request)
        return self._call_api(**http_info)

    def delete_schedule_tas_k_invoker(self, request):
        http_info = self._delete_schedule_tas_k_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_schedule_tas_k_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instance/{instance_id}/scheduled-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScheduleTasKResponse"
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

    def delete_task_record(self, request):
        """删除指定任务记录

        删除指定任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTaskRecord
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteTaskRecordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteTaskRecordResponse`
        """
        http_info = self._delete_task_record_http_info(request)
        return self._call_api(**http_info)

    def delete_task_record_invoker(self, request):
        http_info = self._delete_task_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_task_record_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def describe_backup_encrypt_status(self, request):
        """查询实例是否开启备份加密功能

        查询实例是否开启备份加密功能。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeBackupEncryptStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.DescribeBackupEncryptStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DescribeBackupEncryptStatusResponse`
        """
        http_info = self._describe_backup_encrypt_status_http_info(request)
        return self._call_api(**http_info)

    def describe_backup_encrypt_status_invoker(self, request):
        http_info = self._describe_backup_encrypt_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_backup_encrypt_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/encryption",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeBackupEncryptStatusResponse"
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

    def expand_gauss_my_sql_instance_volume(self, request):
        """包周期存储扩容

        包周期存储扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandGaussMySqlInstanceVolume
        :type request: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlInstanceVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlInstanceVolumeResponse`
        """
        http_info = self._expand_gauss_my_sql_instance_volume_http_info(request)
        return self._call_api(**http_info)

    def expand_gauss_my_sql_instance_volume_invoker(self, request):
        http_info = self._expand_gauss_my_sql_instance_volume_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_gauss_my_sql_instance_volume_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/volume/extend",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandGaussMySqlInstanceVolumeResponse"
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

    def expand_gauss_my_sql_proxy(self, request):
        """扩容数据库代理节点的数量

        扩容数据库代理节点的数量。
        DeC专属云账号暂不支持数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExpandGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlProxyResponse`
        """
        http_info = self._expand_gauss_my_sql_proxy_http_info(request)
        return self._call_api(**http_info)

    def expand_gauss_my_sql_proxy_invoker(self, request):
        http_info = self._expand_gauss_my_sql_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _expand_gauss_my_sql_proxy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/enlarge",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandGaussMySqlProxyResponse"
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

    def invoke_gauss_my_sql_instance_switch_over(self, request):
        """手动主备倒换

        用户手动进行主备倒换。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InvokeGaussMySqlInstanceSwitchOver
        :type request: :class:`huaweicloudsdkgaussdb.v3.InvokeGaussMySqlInstanceSwitchOverRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.InvokeGaussMySqlInstanceSwitchOverResponse`
        """
        http_info = self._invoke_gauss_my_sql_instance_switch_over_http_info(request)
        return self._call_api(**http_info)

    def invoke_gauss_my_sql_instance_switch_over_invoker(self, request):
        http_info = self._invoke_gauss_my_sql_instance_switch_over_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _invoke_gauss_my_sql_instance_switch_over_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switchover",
            "request_type": request.__class__.__name__,
            "response_type": "InvokeGaussMySqlInstanceSwitchOverResponse"
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

    def list_audit_log_download_link(self, request):
        """获取全量SQL的临时下载链接

        获取全量SQL的临时下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditLogDownloadLink
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListAuditLogDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListAuditLogDownloadLinkResponse`
        """
        http_info = self._list_audit_log_download_link_http_info(request)
        return self._call_api(**http_info)

    def list_audit_log_download_link_invoker(self, request):
        http_info = self._list_audit_log_download_link_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_log_download_link_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instance/{instance_id}/auditlog/download-link",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditLogDownloadLinkResponse"
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
        if 'last_file_name' in local_var_params:
            query_params.append(('last_file_name', local_var_params['last_file_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_configurations_differences(self, request):
        """对比参数模板

        比较两个参数模板之间的差异。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationsDifferences
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListConfigurationsDifferencesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListConfigurationsDifferencesResponse`
        """
        http_info = self._list_configurations_differences_http_info(request)
        return self._call_api(**http_info)

    def list_configurations_differences_invoker(self, request):
        http_info = self._list_configurations_differences_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configurations_differences_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/comparison",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationsDifferencesResponse"
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

    def list_configurations_instances(self, request):
        """查询可应用的实例列表

        查询指定参数模板可被应用的实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConfigurationsInstances
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListConfigurationsInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListConfigurationsInstancesResponse`
        """
        http_info = self._list_configurations_instances_http_info(request)
        return self._call_api(**http_info)

    def list_configurations_instances_invoker(self, request):
        http_info = self._list_configurations_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_configurations_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}/applicable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationsInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def list_enterprise_projects(self, request):
        """查询企业项目

        查询企业项目。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnterpriseProjects
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListEnterpriseProjectsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListEnterpriseProjectsResponse`
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
            "resource_path": "/v3/{project_id}/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnterpriseProjectsResponse"
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

    def list_gauss_my_sql_configurations(self, request):
        """查询参数模板

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlConfigurationsResponse`
        """
        http_info = self._list_gauss_my_sql_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_configurations_invoker(self, request):
        http_info = self._list_gauss_my_sql_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlConfigurationsResponse"
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

    def list_gauss_my_sql_database(self, request):
        """查询数据库列表

        查询 GaussDB(for MySQL)实例数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseResponse`
        """
        http_info = self._list_gauss_my_sql_database_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_database_invoker(self, request):
        http_info = self._list_gauss_my_sql_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_database_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlDatabaseResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'charset' in local_var_params:
            query_params.append(('charset', local_var_params['charset']))

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

    def list_gauss_my_sql_database_charsets(self, request):
        """查询数据库可用字符集

        查询云数据库 GaussDB(for MySQL)实例数据库可用字符集。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlDatabaseCharsets
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseCharsetsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseCharsetsResponse`
        """
        http_info = self._list_gauss_my_sql_database_charsets_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_database_charsets_invoker(self, request):
        http_info = self._list_gauss_my_sql_database_charsets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_database_charsets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/charsets",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlDatabaseCharsetsResponse"
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

    def list_gauss_my_sql_database_user(self, request):
        """查询数据库用户

        查询云数据库 GaussDB(for MySQL)实例数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseUserResponse`
        """
        http_info = self._list_gauss_my_sql_database_user_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_database_user_invoker(self, request):
        http_info = self._list_gauss_my_sql_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_database_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlDatabaseUserResponse"
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

    def list_gauss_my_sql_dedicated_resources(self, request):
        """查询专属资源池列表

        获取专属资源池列表，包括用户开通的所有专属资源池信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlDedicatedResources
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDedicatedResourcesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDedicatedResourcesResponse`
        """
        http_info = self._list_gauss_my_sql_dedicated_resources_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_dedicated_resources_invoker(self, request):
        http_info = self._list_gauss_my_sql_dedicated_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_dedicated_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dedicated-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlDedicatedResourcesResponse"
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

    def list_gauss_my_sql_instance_detail_info(self, request):
        """批量查询实例详情

        批量查询实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlInstanceDetailInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstanceDetailInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstanceDetailInfoResponse`
        """
        http_info = self._list_gauss_my_sql_instance_detail_info_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_instance_detail_info_invoker(self, request):
        http_info = self._list_gauss_my_sql_instance_detail_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_instance_detail_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/details",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlInstanceDetailInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_ids' in local_var_params:
            query_params.append(('instance_ids', local_var_params['instance_ids']))

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

    def list_gauss_my_sql_instance_detail_info_unify_status(self, request):
        """批量查询实例详情

        批量查询实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlInstanceDetailInfoUnifyStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstanceDetailInfoUnifyStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstanceDetailInfoUnifyStatusResponse`
        """
        http_info = self._list_gauss_my_sql_instance_detail_info_unify_status_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_instance_detail_info_unify_status_invoker(self, request):
        http_info = self._list_gauss_my_sql_instance_detail_info_unify_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_instance_detail_info_unify_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/details",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlInstanceDetailInfoUnifyStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_ids' in local_var_params:
            query_params.append(('instance_ids', local_var_params['instance_ids']))

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

    def list_gauss_my_sql_instances(self, request):
        """查询实例列表

        根据指定条件查询实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlInstances
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstancesResponse`
        """
        http_info = self._list_gauss_my_sql_instances_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_instances_invoker(self, request):
        http_info = self._list_gauss_my_sql_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlInstancesResponse"
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
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'readonly_private_ip' in local_var_params:
            query_params.append(('readonly_private_ip', local_var_params['readonly_private_ip']))
        if 'proxy_ip' in local_var_params:
            query_params.append(('proxy_ip', local_var_params['proxy_ip']))
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

    def list_gauss_my_sql_instances_unify_status(self, request):
        """查询实例列表

        根据指定条件查询实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGaussMySqlInstancesUnifyStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstancesUnifyStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstancesUnifyStatusResponse`
        """
        http_info = self._list_gauss_my_sql_instances_unify_status_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_my_sql_instances_unify_status_invoker(self, request):
        http_info = self._list_gauss_my_sql_instances_unify_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_gauss_my_sql_instances_unify_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussMySqlInstancesUnifyStatusResponse"
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
        if 'private_ip' in local_var_params:
            query_params.append(('private_ip', local_var_params['private_ip']))
        if 'readonly_private_ip' in local_var_params:
            query_params.append(('readonly_private_ip', local_var_params['readonly_private_ip']))
        if 'proxy_ip' in local_var_params:
            query_params.append(('proxy_ip', local_var_params['proxy_ip']))
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

    def list_immediate_jobs(self, request):
        """获取即时任务列表

        获取即时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImmediateJobs
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListImmediateJobsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListImmediateJobsResponse`
        """
        http_info = self._list_immediate_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_immediate_jobs_invoker(self, request):
        http_info = self._list_immediate_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_immediate_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/immediate-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListImmediateJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_instance_configurations(self, request):
        """获取指定实例的参数信息

        获取指定实例的参数信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListInstanceConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListInstanceConfigurationsResponse`
        """
        http_info = self._list_instance_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_instance_configurations_invoker(self, request):
        http_info = self._list_instance_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_instance_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceConfigurationsResponse"
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

    def list_instance_tags(self, request):
        """查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListInstanceTagsResponse`
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

    def list_lts_error_log_details(self, request):
        """获取错误日志详情列表

        获取指定实例的错误日志详情列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLtsErrorLogDetails
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListLtsErrorLogDetailsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListLtsErrorLogDetailsResponse`
        """
        http_info = self._list_lts_error_log_details_http_info(request)
        return self._call_api(**http_info)

    def list_lts_error_log_details_invoker(self, request):
        http_info = self._list_lts_error_log_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lts_error_log_details_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/error-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLtsErrorLogDetailsResponse"
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

    def list_lts_slowlog_details(self, request):
        """获取慢日志详情列表

        获取指定实例的慢日志详情列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLtsSlowlogDetails
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListLtsSlowlogDetailsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListLtsSlowlogDetailsResponse`
        """
        http_info = self._list_lts_slowlog_details_http_info(request)
        return self._call_api(**http_info)

    def list_lts_slowlog_details_invoker(self, request):
        http_info = self._list_lts_slowlog_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_lts_slowlog_details_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListLtsSlowlogDetailsResponse"
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

    def list_modify_history(self, request):
        """查询参数修改历史

        查询参数修改历史。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListModifyHistory
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListModifyHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListModifyHistoryResponse`
        """
        http_info = self._list_modify_history_http_info(request)
        return self._call_api(**http_info)

    def list_modify_history_invoker(self, request):
        http_info = self._list_modify_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_modify_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}/modify-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListModifyHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def list_params_template_apply_history(self, request):
        """查询参数模板应用记录。

        查询参数模板应用记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListParamsTemplateApplyHistory
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListParamsTemplateApplyHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListParamsTemplateApplyHistoryResponse`
        """
        http_info = self._list_params_template_apply_history_http_info(request)
        return self._call_api(**http_info)

    def list_params_template_apply_history_invoker(self, request):
        http_info = self._list_params_template_apply_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_params_template_apply_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/apply-history",
            "request_type": request.__class__.__name__,
            "response_type": "ListParamsTemplateApplyHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def list_project_tags(self, request):
        """查询项目标签

        查询指定project ID下实例的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListProjectTagsResponse`
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
        """查询回收站实例信息

        查询回收站实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListRecycleInstancesResponse`
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
            "resource_path": "/v3/{project_id}/instances/recycle-info",
            "request_type": request.__class__.__name__,
            "response_type": "ListRecycleInstancesResponse"
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

    def list_schedule_jobs(self, request):
        """获取定时任务列表

        获取定时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScheduleJobs
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListScheduleJobsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListScheduleJobsResponse`
        """
        http_info = self._list_schedule_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_schedule_jobs_invoker(self, request):
        http_info = self._list_schedule_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_schedule_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/scheduled-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListScheduleJobsResponse"
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))

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

    def modify_backup_encrypt_status(self, request):
        """打开或关闭备份加密

        打开或关闭备份加密。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyBackupEncryptStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.ModifyBackupEncryptStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ModifyBackupEncryptStatusResponse`
        """
        http_info = self._modify_backup_encrypt_status_http_info(request)
        return self._call_api(**http_info)

    def modify_backup_encrypt_status_invoker(self, request):
        http_info = self._modify_backup_encrypt_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_backup_encrypt_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/encryption",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyBackupEncryptStatusResponse"
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

    def modify_gauss_my_sql_proxy_route_mode(self, request):
        """设置读写分离路由模式

        设置读写分离路由模式。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyGaussMySqlProxyRouteMode
        :type request: :class:`huaweicloudsdkgaussdb.v3.ModifyGaussMySqlProxyRouteModeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ModifyGaussMySqlProxyRouteModeResponse`
        """
        http_info = self._modify_gauss_my_sql_proxy_route_mode_http_info(request)
        return self._call_api(**http_info)

    def modify_gauss_my_sql_proxy_route_mode_invoker(self, request):
        http_info = self._modify_gauss_my_sql_proxy_route_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_gauss_my_sql_proxy_route_mode_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/route-mode",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyGaussMySqlProxyRouteModeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def modify_gauss_mysql_dns(self, request):
        """修改内网域名

        修改内网域名。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyGaussMysqlDns
        :type request: :class:`huaweicloudsdkgaussdb.v3.ModifyGaussMysqlDnsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ModifyGaussMysqlDnsResponse`
        """
        http_info = self._modify_gauss_mysql_dns_http_info(request)
        return self._call_api(**http_info)

    def modify_gauss_mysql_dns_invoker(self, request):
        http_info = self._modify_gauss_mysql_dns_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_gauss_mysql_dns_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/dns",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyGaussMysqlDnsResponse"
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

    def modify_node_priority(self, request):
        """修改节点故障倒换优先级。

        修改节点故障倒换优先级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifyNodePriority
        :type request: :class:`huaweicloudsdkgaussdb.v3.ModifyNodePriorityRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ModifyNodePriorityResponse`
        """
        http_info = self._modify_node_priority_http_info(request)
        return self._call_api(**http_info)

    def modify_node_priority_invoker(self, request):
        http_info = self._modify_node_priority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_node_priority_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/priority",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyNodePriorityResponse"
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

    def rename_instance_node(self, request):
        """批量修改节点名称.

        批量修改节点名称.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RenameInstanceNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.RenameInstanceNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RenameInstanceNodeResponse`
        """
        http_info = self._rename_instance_node_http_info(request)
        return self._call_api(**http_info)

    def rename_instance_node_invoker(self, request):
        http_info = self._rename_instance_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _rename_instance_node_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/name",
            "request_type": request.__class__.__name__,
            "response_type": "RenameInstanceNodeResponse"
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

    def reset_gauss_my_sql_database_password(self, request):
        """修改数据库用户密码

        修改云数据库 GaussDB(for MySQL)实例数据库用户密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetGaussMySqlDatabasePassword
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlDatabasePasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlDatabasePasswordResponse`
        """
        http_info = self._reset_gauss_my_sql_database_password_http_info(request)
        return self._call_api(**http_info)

    def reset_gauss_my_sql_database_password_invoker(self, request):
        http_info = self._reset_gauss_my_sql_database_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_gauss_my_sql_database_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetGaussMySqlDatabasePasswordResponse"
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

    def reset_gauss_my_sql_password(self, request):
        """重置数据库密码

        重置数据库密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResetGaussMySqlPassword
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlPasswordResponse`
        """
        http_info = self._reset_gauss_my_sql_password_http_info(request)
        return self._call_api(**http_info)

    def reset_gauss_my_sql_password_invoker(self, request):
        http_info = self._reset_gauss_my_sql_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reset_gauss_my_sql_password_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/password",
            "request_type": request.__class__.__name__,
            "response_type": "ResetGaussMySqlPasswordResponse"
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

    def restart_gauss_my_sql_instance(self, request):
        """重启数据库实例

        重启数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartGaussMySqlInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlInstanceResponse`
        """
        http_info = self._restart_gauss_my_sql_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_gauss_my_sql_instance_invoker(self, request):
        http_info = self._restart_gauss_my_sql_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_gauss_my_sql_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartGaussMySqlInstanceResponse"
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

    def restart_gauss_my_sql_node(self, request):
        """节点重启

        节点重启。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartGaussMySqlNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlNodeResponse`
        """
        http_info = self._restart_gauss_my_sql_node_http_info(request)
        return self._call_api(**http_info)

    def restart_gauss_my_sql_node_invoker(self, request):
        http_info = self._restart_gauss_my_sql_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_gauss_my_sql_node_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartGaussMySqlNodeResponse"
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

    def restart_proxy_instance(self, request):
        """重启数据库代理.

        重启数据库代理.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartProxyInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartProxyInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartProxyInstanceResponse`
        """
        http_info = self._restart_proxy_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_proxy_instance_invoker(self, request):
        http_info = self._restart_proxy_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_proxy_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartProxyInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def restore_old_instance(self, request):
        """备份恢复到当前实例或已有实例

        备份恢复到当前实例或已有实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreOldInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestoreOldInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestoreOldInstanceResponse`
        """
        http_info = self._restore_old_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_old_instance_invoker(self, request):
        http_info = self._restore_old_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_old_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreOldInstanceResponse"
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

    def set_gauss_my_sql_proxy_weight(self, request):
        """设置读写分离权重

        设置读写分离权重。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetGaussMySqlProxyWeight
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlProxyWeightRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlProxyWeightResponse`
        """
        http_info = self._set_gauss_my_sql_proxy_weight_http_info(request)
        return self._call_api(**http_info)

    def set_gauss_my_sql_proxy_weight_invoker(self, request):
        http_info = self._set_gauss_my_sql_proxy_weight_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_gauss_my_sql_proxy_weight_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/weight",
            "request_type": request.__class__.__name__,
            "response_type": "SetGaussMySqlProxyWeightResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def set_gauss_my_sql_quotas(self, request):
        """设置租户基于企业项目的资源配额

        设置指定企业项目的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetGaussMySqlQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlQuotasResponse`
        """
        http_info = self._set_gauss_my_sql_quotas_http_info(request)
        return self._call_api(**http_info)

    def set_gauss_my_sql_quotas_invoker(self, request):
        http_info = self._set_gauss_my_sql_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_gauss_my_sql_quotas_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "SetGaussMySqlQuotasResponse"
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

    def set_recycle_policy(self, request):
        """设置回收站策略

        设置回收站策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetRecyclePolicyResponse`
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

    def show_audit_log(self, request):
        """查询全量SQL开关状态

        查询全量SQL开关状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditLog
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowAuditLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowAuditLogResponse`
        """
        http_info = self._show_audit_log_http_info(request)
        return self._call_api(**http_info)

    def show_audit_log_invoker(self, request):
        http_info = self._show_audit_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instance/{instance_id}/audit-log/switch-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditLogResponse"
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

    def show_auto_scaling_history(self, request):
        """查询自动变配历史记录.

        查询自动变配历史记录.
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoScalingHistory
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowAutoScalingHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowAutoScalingHistoryResponse`
        """
        http_info = self._show_auto_scaling_history_http_info(request)
        return self._call_api(**http_info)

    def show_auto_scaling_history_invoker(self, request):
        http_info = self._show_auto_scaling_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_scaling_history_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-scaling/history",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoScalingHistoryResponse"
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

    def show_auto_scaling_policy(self, request):
        """查询自动变配

        查询自动变配。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoScalingPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowAutoScalingPolicyResponse`
        """
        http_info = self._show_auto_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def show_auto_scaling_policy_invoker(self, request):
        http_info = self._show_auto_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_auto_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-scaling/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAutoScalingPolicyResponse"
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

    def show_backup_restore_time(self, request):
        """查询可恢复时间段

        查询实例的可恢复时间段。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupRestoreTime
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowBackupRestoreTimeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowBackupRestoreTimeResponse`
        """
        http_info = self._show_backup_restore_time_http_info(request)
        return self._call_api(**http_info)

    def show_backup_restore_time_invoker(self, request):
        http_info = self._show_backup_restore_time_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_backup_restore_time_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/restore-time",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBackupRestoreTimeResponse"
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

    def show_dedicated_resource_info(self, request):
        """查询专属资源信息详情

        查询专属资源信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDedicatedResourceInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowDedicatedResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowDedicatedResourceInfoResponse`
        """
        http_info = self._show_dedicated_resource_info_http_info(request)
        return self._call_api(**http_info)

    def show_dedicated_resource_info_invoker(self, request):
        http_info = self._show_dedicated_resource_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dedicated_resource_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/dedicated-resource/{dedicated_resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDedicatedResourceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'dedicated_resource_id' in local_var_params:
            path_params['dedicated_resource_id'] = local_var_params['dedicated_resource_id']

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

    def show_gauss_my_sql_backup_list(self, request):
        """查询全量备份列表

        查询全量备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlBackupList
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupListRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupListResponse`
        """
        http_info = self._show_gauss_my_sql_backup_list_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_backup_list_invoker(self, request):
        http_info = self._show_gauss_my_sql_backup_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_backup_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlBackupListResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))

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

    def show_gauss_my_sql_backup_policy(self, request):
        """查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupPolicyResponse`
        """
        http_info = self._show_gauss_my_sql_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_backup_policy_invoker(self, request):
        http_info = self._show_gauss_my_sql_backup_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_backup_policy_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlBackupPolicyResponse"
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

    def show_gauss_my_sql_configuration(self, request):
        """获取参数模板详情

        获取指定参数模板的参数信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlConfigurationResponse`
        """
        http_info = self._show_gauss_my_sql_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_configuration_invoker(self, request):
        http_info = self._show_gauss_my_sql_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_configuration_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def show_gauss_my_sql_engine_version(self, request):
        """查询数据库引擎的版本

        获取指定数据库引擎对应的数据库版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlEngineVersion
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlEngineVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlEngineVersionResponse`
        """
        http_info = self._show_gauss_my_sql_engine_version_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_engine_version_invoker(self, request):
        http_info = self._show_gauss_my_sql_engine_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_engine_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/datastores/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlEngineVersionResponse"
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

    def show_gauss_my_sql_flavors(self, request):
        """查询数据库规格

        获取指定数据库引擎版本对应的规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlFlavors
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlFlavorsResponse`
        """
        http_info = self._show_gauss_my_sql_flavors_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_flavors_invoker(self, request):
        http_info = self._show_gauss_my_sql_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/flavors/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlFlavorsResponse"
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
        if 'availability_zone_mode' in local_var_params:
            query_params.append(('availability_zone_mode', local_var_params['availability_zone_mode']))
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

    def show_gauss_my_sql_incremental_backup_list(self, request):
        """查询增量备份列表

        查询增量备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlIncrementalBackupList
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlIncrementalBackupListRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlIncrementalBackupListResponse`
        """
        http_info = self._show_gauss_my_sql_incremental_backup_list_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_incremental_backup_list_invoker(self, request):
        http_info = self._show_gauss_my_sql_incremental_backup_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_incremental_backup_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/incremental-backups",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlIncrementalBackupListResponse"
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

    def show_gauss_my_sql_instance_info(self, request):
        """查询实例详情信息

        查询实例详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlInstanceInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlInstanceInfoResponse`
        """
        http_info = self._show_gauss_my_sql_instance_info_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_instance_info_invoker(self, request):
        http_info = self._show_gauss_my_sql_instance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_instance_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlInstanceInfoResponse"
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

    def show_gauss_my_sql_instance_info_unify_status(self, request):
        """查询实例详情信息

        查询实例详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlInstanceInfoUnifyStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlInstanceInfoUnifyStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlInstanceInfoUnifyStatusResponse`
        """
        http_info = self._show_gauss_my_sql_instance_info_unify_status_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_instance_info_unify_status_invoker(self, request):
        http_info = self._show_gauss_my_sql_instance_info_unify_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_instance_info_unify_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlInstanceInfoUnifyStatusResponse"
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

    def show_gauss_my_sql_job_info(self, request):
        """获取指定ID的任务信息

        获取GaussDB(for MySQL)任务中心指定ID的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlJobInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlJobInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlJobInfoResponse`
        """
        http_info = self._show_gauss_my_sql_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_job_info_invoker(self, request):
        http_info = self._show_gauss_my_sql_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlJobInfoResponse"
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

    def show_gauss_my_sql_project_quotas(self, request):
        """查询租户的实例配额

        获取指定租户的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlProjectQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProjectQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProjectQuotasResponse`
        """
        http_info = self._show_gauss_my_sql_project_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_project_quotas_invoker(self, request):
        http_info = self._show_gauss_my_sql_project_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_project_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/project-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlProjectQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def show_gauss_my_sql_proxy_flavors(self, request):
        """查询数据库代理规格信息

        查询数据库代理规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlProxyFlavors
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyFlavorsResponse`
        """
        http_info = self._show_gauss_my_sql_proxy_flavors_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_proxy_flavors_invoker(self, request):
        http_info = self._show_gauss_my_sql_proxy_flavors_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_proxy_flavors_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlProxyFlavorsResponse"
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

    def show_gauss_my_sql_proxy_list(self, request):
        """查询数据库代理信息列表

        查询数据库代理信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlProxyList
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyListRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyListResponse`
        """
        http_info = self._show_gauss_my_sql_proxy_list_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_proxy_list_invoker(self, request):
        http_info = self._show_gauss_my_sql_proxy_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_proxy_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlProxyListResponse"
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

    def show_gauss_my_sql_quotas(self, request):
        """查询租户基于企业项目的资源配额

        获取指定企业项目的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGaussMySqlQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlQuotasResponse`
        """
        http_info = self._show_gauss_my_sql_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_gauss_my_sql_quotas_invoker(self, request):
        http_info = self._show_gauss_my_sql_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_gauss_my_sql_quotas_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGaussMySqlQuotasResponse"
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
        if 'enterprise_project_name' in local_var_params:
            query_params.append(('enterprise_project_name', local_var_params['enterprise_project_name']))

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

    def show_instance_database_version(self, request):
        """查询内核版本信息

        查询内核版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceDatabaseVersion
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceDatabaseVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceDatabaseVersionResponse`
        """
        http_info = self._show_instance_database_version_http_info(request)
        return self._call_api(**http_info)

    def show_instance_database_version_invoker(self, request):
        http_info = self._show_instance_database_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_database_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database-version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceDatabaseVersionResponse"
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

    def show_instance_eip(self, request):
        """查询弹性公网IP。

        查询弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceEip
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceEipResponse`
        """
        http_info = self._show_instance_eip_http_info(request)
        return self._call_api(**http_info)

    def show_instance_eip_invoker(self, request):
        http_info = self._show_instance_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_eip_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/eip",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceEipResponse"
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

    def show_instance_monitor_extend(self, request):
        """查询实例秒级监控

        查询实例秒级监控信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceMonitorExtend
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceMonitorExtendRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceMonitorExtendResponse`
        """
        http_info = self._show_instance_monitor_extend_http_info(request)
        return self._call_api(**http_info)

    def show_instance_monitor_extend_invoker(self, request):
        http_info = self._show_instance_monitor_extend_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_instance_monitor_extend_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/monitor-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceMonitorExtendResponse"
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

    def show_intelligent_diagnosis_abnormal_count_of_instances(self, request):
        """获取各指标的异常实例数

        获取各指标的异常实例数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIntelligentDiagnosisAbnormalCountOfInstances
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowIntelligentDiagnosisAbnormalCountOfInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse`
        """
        http_info = self._show_intelligent_diagnosis_abnormal_count_of_instances_http_info(request)
        return self._call_api(**http_info)

    def show_intelligent_diagnosis_abnormal_count_of_instances_invoker(self, request):
        http_info = self._show_intelligent_diagnosis_abnormal_count_of_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_intelligent_diagnosis_abnormal_count_of_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/diagnosis-instance-count",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIntelligentDiagnosisAbnormalCountOfInstancesResponse"
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

    def show_intelligent_diagnosis_instance_infos_per_metric(self, request):
        """获取某个指标的异常实例信息

        获取某个指标的异常实例信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIntelligentDiagnosisInstanceInfosPerMetric
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowIntelligentDiagnosisInstanceInfosPerMetricRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowIntelligentDiagnosisInstanceInfosPerMetricResponse`
        """
        http_info = self._show_intelligent_diagnosis_instance_infos_per_metric_http_info(request)
        return self._call_api(**http_info)

    def show_intelligent_diagnosis_instance_infos_per_metric_invoker(self, request):
        http_info = self._show_intelligent_diagnosis_instance_infos_per_metric_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_intelligent_diagnosis_instance_infos_per_metric_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/diagnosis-instance-infos",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIntelligentDiagnosisInstanceInfosPerMetricResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
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

    def show_lts_configs(self, request):
        """查询实例LTS日志配置列表

        查询实例LTS日志配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLtsConfigs
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowLtsConfigsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowLtsConfigsResponse`
        """
        http_info = self._show_lts_configs_http_info(request)
        return self._call_api(**http_info)

    def show_lts_configs_invoker(self, request):
        http_info = self._show_lts_configs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_lts_configs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLtsConfigsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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

    def show_proxy_configurations(self, request):
        """查询数据库代理内核参数。

        查询数据库代理内核参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProxyConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowProxyConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowProxyConfigurationsResponse`
        """
        http_info = self._show_proxy_configurations_http_info(request)
        return self._call_api(**http_info)

    def show_proxy_configurations_invoker(self, request):
        http_info = self._show_proxy_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_proxy_configurations_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProxyConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def show_proxy_ipgroup(self, request):
        """查询代理实例访问控制

        查询代理实例访问控制
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProxyIpgroup
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowProxyIpgroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowProxyIpgroupResponse`
        """
        http_info = self._show_proxy_ipgroup_http_info(request)
        return self._call_api(**http_info)

    def show_proxy_ipgroup_invoker(self, request):
        http_info = self._show_proxy_ipgroup_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_proxy_ipgroup_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/ipgroup",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProxyIpgroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def show_proxy_version(self, request):
        """查询代理实例小版本

        查询代理实例小版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProxyVersion
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowProxyVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowProxyVersionResponse`
        """
        http_info = self._show_proxy_version_http_info(request)
        return self._call_api(**http_info)

    def show_proxy_version_invoker(self, request):
        http_info = self._show_proxy_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_proxy_version_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/{engine_name}/proxy-version",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProxyVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'engine_name' in local_var_params:
            path_params['engine_name'] = local_var_params['engine_name']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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
        """查询回收站策略

        查询回收站策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowRecyclePolicyResponse`
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

    def show_restore_tables(self, request):
        """查询表级时间点恢复可选表

        查询表级时间点恢复可选表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRestoreTables
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowRestoreTablesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowRestoreTablesResponse`
        """
        http_info = self._show_restore_tables_http_info(request)
        return self._call_api(**http_info)

    def show_restore_tables_invoker(self, request):
        http_info = self._show_restore_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_restore_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/restore/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRestoreTablesResponse"
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
        if 'last_table_info' in local_var_params:
            query_params.append(('last_table_info', local_var_params['last_table_info']))
        if 'database_name' in local_var_params:
            query_params.append(('database_name', local_var_params['database_name']))
        if 'table_name' in local_var_params:
            query_params.append(('table_name', local_var_params['table_name']))

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

    def show_slowlog_sensitive_status(self, request):
        """查询慢日志脱敏状态

        查询慢日志脱敏状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSlowlogSensitiveStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowSlowlogSensitiveStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowSlowlogSensitiveStatusResponse`
        """
        http_info = self._show_slowlog_sensitive_status_http_info(request)
        return self._call_api(**http_info)

    def show_slowlog_sensitive_status_invoker(self, request):
        http_info = self._show_slowlog_sensitive_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_slowlog_sensitive_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowlogSensitiveStatusResponse"
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

    def shrink_gauss_my_sql_proxy(self, request):
        """减少数据库代理节点的数量

        缩容数据库代理节点的数量。
        DeC专属云账号暂不支持数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShrinkGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShrinkGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShrinkGaussMySqlProxyResponse`
        """
        http_info = self._shrink_gauss_my_sql_proxy_http_info(request)
        return self._call_api(**http_info)

    def shrink_gauss_my_sql_proxy_invoker(self, request):
        http_info = self._shrink_gauss_my_sql_proxy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _shrink_gauss_my_sql_proxy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/reduce",
            "request_type": request.__class__.__name__,
            "response_type": "ShrinkGaussMySqlProxyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def switch_access_control(self, request):
        """开启或关闭访问控制

        开启或关闭访问控制。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAccessControl
        :type request: :class:`huaweicloudsdkgaussdb.v3.SwitchAccessControlRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchAccessControlResponse`
        """
        http_info = self._switch_access_control_http_info(request)
        return self._call_api(**http_info)

    def switch_access_control_invoker(self, request):
        http_info = self._switch_access_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_access_control_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/access-control-switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAccessControlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def switch_gauss_my_sql_configuration(self, request):
        """应用参数模板

        指定实例变更参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlConfigurationResponse`
        """
        http_info = self._switch_gauss_my_sql_configuration_http_info(request)
        return self._call_api(**http_info)

    def switch_gauss_my_sql_configuration_invoker(self, request):
        http_info = self._switch_gauss_my_sql_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_gauss_my_sql_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}/apply",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchGaussMySqlConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def switch_gauss_my_sql_instance_ssl(self, request):
        """开关SSL

        为实例设置SSL数据加密。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchGaussMySqlInstanceSsl
        :type request: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlInstanceSslRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlInstanceSslResponse`
        """
        http_info = self._switch_gauss_my_sql_instance_ssl_http_info(request)
        return self._call_api(**http_info)

    def switch_gauss_my_sql_instance_ssl_invoker(self, request):
        http_info = self._switch_gauss_my_sql_instance_ssl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_gauss_my_sql_instance_ssl_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ssl-option",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchGaussMySqlInstanceSslResponse"
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

    def switch_gauss_my_sql_proxy_ssl(self, request):
        """开关数据库代理SSL

        为数据库代理设置SSL数据加密。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchGaussMySqlProxySsl
        :type request: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxySslRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlProxySslResponse`
        """
        http_info = self._switch_gauss_my_sql_proxy_ssl_http_info(request)
        return self._call_api(**http_info)

    def switch_gauss_my_sql_proxy_ssl_invoker(self, request):
        http_info = self._switch_gauss_my_sql_proxy_ssl_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_gauss_my_sql_proxy_ssl_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/ssl",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchGaussMySqlProxySslResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_audit_log(self, request):
        """开启或者关闭全量SQL

        开启或者关闭全量SQL。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditLog
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateAuditLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateAuditLogResponse`
        """
        http_info = self._update_audit_log_http_info(request)
        return self._call_api(**http_info)

    def update_audit_log_invoker(self, request):
        http_info = self._update_audit_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_log_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instance/{instance_id}/audit-log/switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditLogResponse"
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

    def update_auto_scaling_policy(self, request):
        """设置自动变配

        设置自动变配。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutoScalingPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateAutoScalingPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateAutoScalingPolicyResponse`
        """
        http_info = self._update_auto_scaling_policy_http_info(request)
        return self._call_api(**http_info)

    def update_auto_scaling_policy_invoker(self, request):
        http_info = self._update_auto_scaling_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_auto_scaling_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-scaling/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAutoScalingPolicyResponse"
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

    def update_backup_offsite_policy(self, request):
        """设置跨区备份策略

        设置跨区备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBackupOffsitePolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateBackupOffsitePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateBackupOffsitePolicyResponse`
        """
        http_info = self._update_backup_offsite_policy_http_info(request)
        return self._call_api(**http_info)

    def update_backup_offsite_policy_invoker(self, request):
        http_info = self._update_backup_offsite_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_backup_offsite_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/offsite-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBackupOffsitePolicyResponse"
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

    def update_gauss_my_sql_backup_policy(self, request):
        """设置备份策略

        设置自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlBackupPolicyResponse`
        """
        http_info = self._update_gauss_my_sql_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_backup_policy_invoker(self, request):
        http_info = self._update_gauss_my_sql_backup_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_backup_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/policy/update",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlBackupPolicyResponse"
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

    def update_gauss_my_sql_configuration(self, request):
        """修改参数模板

        修改指定参数模板的参数信息，包括名称、描述、指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlConfigurationResponse`
        """
        http_info = self._update_gauss_my_sql_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_configuration_invoker(self, request):
        http_info = self._update_gauss_my_sql_configuration_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_configuration_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/configurations/{configuration_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlConfigurationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'configuration_id' in local_var_params:
            path_params['configuration_id'] = local_var_params['configuration_id']

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

    def update_gauss_my_sql_database_comment(self, request):
        """修改数据库备注

        修改云数据库 GaussDB(for MySQL)实例数据库备注。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlDatabaseComment
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlDatabaseCommentRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlDatabaseCommentResponse`
        """
        http_info = self._update_gauss_my_sql_database_comment_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_database_comment_invoker(self, request):
        http_info = self._update_gauss_my_sql_database_comment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_database_comment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/databases/comment",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlDatabaseCommentResponse"
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

    def update_gauss_my_sql_database_user_comment(self, request):
        """修改数据库用户备注

        修改云数据库 GaussDB(for MySQL)实例数据库用户备注。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlDatabaseUserComment
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlDatabaseUserCommentRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlDatabaseUserCommentResponse`
        """
        http_info = self._update_gauss_my_sql_database_user_comment_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_database_user_comment_invoker(self, request):
        http_info = self._update_gauss_my_sql_database_user_comment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_database_user_comment_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/comment",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlDatabaseUserCommentResponse"
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

    def update_gauss_my_sql_instance_alias(self, request):
        """修改实例备注

        修改实例备注。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstanceAlias
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceAliasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceAliasResponse`
        """
        http_info = self._update_gauss_my_sql_instance_alias_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_alias_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_alias_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_alias_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/alias",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstanceAliasResponse"
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

    def update_gauss_my_sql_instance_eip(self, request):
        """绑定弹性公网IP

        实例绑定弹性公网IP，供外网连接使用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstanceEip
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceEipResponse`
        """
        http_info = self._update_gauss_my_sql_instance_eip_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_eip_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_eip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_eip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/public-ips/bind",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstanceEipResponse"
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

    def update_gauss_my_sql_instance_internal_ip(self, request):
        """修改内网地址

        修改实例内网地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstanceInternalIp
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceInternalIpRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceInternalIpResponse`
        """
        http_info = self._update_gauss_my_sql_instance_internal_ip_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_internal_ip_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_internal_ip_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_internal_ip_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/internal-ip",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstanceInternalIpResponse"
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

    def update_gauss_my_sql_instance_name(self, request):
        """修改实例名称

        修改实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstanceName
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceNameResponse`
        """
        http_info = self._update_gauss_my_sql_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_name_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstanceNameResponse"
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

    def update_gauss_my_sql_instance_ops_window(self, request):
        """设置可维护时间段

        设置可维护时间段。建议将可维护时间段设置在业务低峰期，避免业务在维护过程中异常中断。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstanceOpsWindow
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceOpsWindowRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceOpsWindowResponse`
        """
        http_info = self._update_gauss_my_sql_instance_ops_window_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_ops_window_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_ops_window_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_ops_window_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ops-window",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstanceOpsWindowResponse"
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

    def update_gauss_my_sql_instance_port(self, request):
        """修改实例端口

        修改实例数据库端口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstancePort
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstancePortRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstancePortResponse`
        """
        http_info = self._update_gauss_my_sql_instance_port_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_port_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/port",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstancePortResponse"
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

    def update_gauss_my_sql_instance_security_group(self, request):
        """修改安全组

        修改指定实例安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlInstanceSecurityGroup
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceSecurityGroupResponse`
        """
        http_info = self._update_gauss_my_sql_instance_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_instance_security_group_invoker(self, request):
        http_info = self._update_gauss_my_sql_instance_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_instance_security_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlInstanceSecurityGroupResponse"
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

    def update_gauss_my_sql_quotas(self, request):
        """修改租户基于企业项目的资源配额

        修改指定企业项目的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGaussMySqlQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlQuotasResponse`
        """
        http_info = self._update_gauss_my_sql_quotas_http_info(request)
        return self._call_api(**http_info)

    def update_gauss_my_sql_quotas_invoker(self, request):
        http_info = self._update_gauss_my_sql_quotas_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_gauss_my_sql_quotas_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGaussMySqlQuotasResponse"
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

    def update_instance_configurations(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateInstanceConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateInstanceConfigurationsResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/configurations",
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

    def update_instance_monitor(self, request):
        """设置实例秒级监控

        设置实例秒级监控，包括1秒监控和5秒监控。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInstanceMonitor
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateInstanceMonitorRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateInstanceMonitorResponse`
        """
        http_info = self._update_instance_monitor_http_info(request)
        return self._call_api(**http_info)

    def update_instance_monitor_invoker(self, request):
        http_info = self._update_instance_monitor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_instance_monitor_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/monitor-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInstanceMonitorResponse"
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

    def update_new_node_auto_add_switch(self, request):
        """开启或关闭新增节点自动加入该Proxy

        开启或关闭新增节点自动加入该Proxy。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNewNodeAutoAddSwitch
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateNewNodeAutoAddSwitchRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateNewNodeAutoAddSwitchResponse`
        """
        http_info = self._update_new_node_auto_add_switch_http_info(request)
        return self._call_api(**http_info)

    def update_new_node_auto_add_switch_invoker(self, request):
        http_info = self._update_new_node_auto_add_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_new_node_auto_add_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/new-node-auto-add",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNewNodeAutoAddSwitchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_proxy_connection_pool_type(self, request):
        """更改数据库代理连接池类型

        更改数据库代理连接池类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProxyConnectionPoolType
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyConnectionPoolTypeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyConnectionPoolTypeResponse`
        """
        http_info = self._update_proxy_connection_pool_type_http_info(request)
        return self._call_api(**http_info)

    def update_proxy_connection_pool_type_invoker(self, request):
        http_info = self._update_proxy_connection_pool_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_proxy_connection_pool_type_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/connection-pool-type",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProxyConnectionPoolTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_proxy_name(self, request):
        """修改代理实例名称

        修改代理实例名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProxyName
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyNameResponse`
        """
        http_info = self._update_proxy_name_http_info(request)
        return self._call_api(**http_info)

    def update_proxy_name_invoker(self, request):
        http_info = self._update_proxy_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_proxy_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/rename",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProxyNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_proxy_new_configurations(self, request):
        """修改代理实例参数

        修改数据库代理参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProxyNewConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyNewConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyNewConfigurationsResponse`
        """
        http_info = self._update_proxy_new_configurations_http_info(request)
        return self._call_api(**http_info)

    def update_proxy_new_configurations_invoker(self, request):
        http_info = self._update_proxy_new_configurations_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_proxy_new_configurations_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProxyNewConfigurationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_proxy_port(self, request):
        """修改读写分离端口号

        修改读写分离端口号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProxyPort
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyPortRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateProxyPortResponse`
        """
        http_info = self._update_proxy_port_http_info(request)
        return self._call_api(**http_info)

    def update_proxy_port_invoker(self, request):
        http_info = self._update_proxy_port_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_proxy_port_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/port",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProxyPortResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_proxy_session_consistence(self, request):
        """修改代理会话一致性

        修改代理会话一致性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProxySessionConsistence
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateProxySessionConsistenceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateProxySessionConsistenceResponse`
        """
        http_info = self._update_proxy_session_consistence_http_info(request)
        return self._call_api(**http_info)

    def update_proxy_session_consistence_invoker(self, request):
        http_info = self._update_proxy_session_consistence_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_proxy_session_consistence_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/session-consistence",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProxySessionConsistenceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def update_serverless_policy(self, request):
        """设置Serverless配置策略

        设置Serverless配置策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateServerlessPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateServerlessPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateServerlessPolicyResponse`
        """
        http_info = self._update_serverless_policy_http_info(request)
        return self._call_api(**http_info)

    def update_serverless_policy_invoker(self, request):
        http_info = self._update_serverless_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_serverless_policy_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/serverless/policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerlessPolicyResponse"
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

    def update_slowlog_sensitive_switch(self, request):
        """开启或关闭慢日志脱敏状态

        开启或关闭慢日志脱敏状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSlowlogSensitiveSwitch
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateSlowlogSensitiveSwitchRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateSlowlogSensitiveSwitchResponse`
        """
        http_info = self._update_slowlog_sensitive_switch_http_info(request)
        return self._call_api(**http_info)

    def update_slowlog_sensitive_switch_invoker(self, request):
        http_info = self._update_slowlog_sensitive_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_slowlog_sensitive_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slowlog/modify",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSlowlogSensitiveSwitchResponse"
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

    def update_transaction_split_status(self, request):
        """设置proxy事务拆分

        设置proxy事务拆分。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTransactionSplitStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateTransactionSplitStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateTransactionSplitStatusResponse`
        """
        http_info = self._update_transaction_split_status_http_info(request)
        return self._call_api(**http_info)

    def update_transaction_split_status_invoker(self, request):
        http_info = self._update_transaction_split_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_transaction_split_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/transaction-split",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTransactionSplitStatusResponse"
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

    def upgrade_gauss_my_sql_instance_database(self, request):
        """内核版本升级

        内核版本升级。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeGaussMySqlInstanceDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpgradeGaussMySqlInstanceDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpgradeGaussMySqlInstanceDatabaseResponse`
        """
        http_info = self._upgrade_gauss_my_sql_instance_database_http_info(request)
        return self._call_api(**http_info)

    def upgrade_gauss_my_sql_instance_database_invoker(self, request):
        http_info = self._upgrade_gauss_my_sql_instance_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_gauss_my_sql_instance_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeGaussMySqlInstanceDatabaseResponse"
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

    def upgrade_proxy_version(self, request):
        """升级数据库代理实例内核版本

        升级数据库代理实例内核版本。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeProxyVersion
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpgradeProxyVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpgradeProxyVersionResponse`
        """
        http_info = self._upgrade_proxy_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_proxy_version_invoker(self, request):
        http_info = self._upgrade_proxy_version_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upgrade_proxy_version_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/upgrade-version",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeProxyVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'proxy_id' in local_var_params:
            path_params['proxy_id'] = local_var_params['proxy_id']

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

    def check_click_house_data_base_config(self, request):
        """数据同步库配置校验

        数据同步库配置校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckClickHouseDataBaseConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckClickHouseDataBaseConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckClickHouseDataBaseConfigResponse`
        """
        http_info = self._check_click_house_data_base_config_http_info(request)
        return self._call_api(**http_info)

    def check_click_house_data_base_config_invoker(self, request):
        http_info = self._check_click_house_data_base_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_click_house_data_base_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication/database-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckClickHouseDataBaseConfigResponse"
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

    def check_click_house_table_config(self, request):
        """数据同步表配置校验

        数据同步表配置校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckClickHouseTableConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckClickHouseTableConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckClickHouseTableConfigResponse`
        """
        http_info = self._check_click_house_table_config_http_info(request)
        return self._call_api(**http_info)

    def check_click_house_table_config_invoker(self, request):
        http_info = self._check_click_house_table_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_click_house_table_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication/table-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckClickHouseTableConfigResponse"
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

    def check_data_base_config(self, request):
        """HTAP数据同步库配置校验

        HTAP数据同步库配置校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDataBaseConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckDataBaseConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckDataBaseConfigResponse`
        """
        http_info = self._check_data_base_config_http_info(request)
        return self._call_api(**http_info)

    def check_data_base_config_invoker(self, request):
        http_info = self._check_data_base_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_data_base_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication/database-config-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDataBaseConfigResponse"
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

    def check_star_rocks_resource(self, request):
        """StarRocks资源检查

        StarRocks资源检查。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckStarRocksResource
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckStarRocksResourceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckStarRocksResourceResponse`
        """
        http_info = self._check_star_rocks_resource_http_info(request)
        return self._call_api(**http_info)

    def check_star_rocks_resource_invoker(self, request):
        http_info = self._check_star_rocks_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_star_rocks_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/starrocks/resource-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckStarRocksResourceResponse"
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

    def check_starrocks_params(self, request):
        """参数对比

        对比实例参数和默认模板的差异
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckStarrocksParams
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckStarrocksParamsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckStarrocksParamsResponse`
        """
        http_info = self._check_starrocks_params_http_info(request)
        return self._call_api(**http_info)

    def check_starrocks_params_invoker(self, request):
        http_info = self._check_starrocks_params_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_starrocks_params_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/starrocks/comparison",
            "request_type": request.__class__.__name__,
            "response_type": "CheckStarrocksParamsResponse"
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

    def check_table_config(self, request):
        """HTAP数据同步表配置校验

        HTAP数据同步表配置校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckTableConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.CheckTableConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckTableConfigResponse`
        """
        http_info = self._check_table_config_http_info(request)
        return self._call_api(**http_info)

    def check_table_config_invoker(self, request):
        http_info = self._check_table_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_table_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication/table-config-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckTableConfigResponse"
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

    def create_click_house_data_base_replication(self, request):
        """创建数据同步

        创建数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClickHouseDataBaseReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateClickHouseDataBaseReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateClickHouseDataBaseReplicationResponse`
        """
        http_info = self._create_click_house_data_base_replication_http_info(request)
        return self._call_api(**http_info)

    def create_click_house_data_base_replication_invoker(self, request):
        http_info = self._create_click_house_data_base_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_click_house_data_base_replication_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClickHouseDataBaseReplicationResponse"
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

    def create_click_house_database_user(self, request):
        """创建数据库账号

        创建数据库账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClickHouseDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateClickHouseDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateClickHouseDatabaseUserResponse`
        """
        http_info = self._create_click_house_database_user_http_info(request)
        return self._call_api(**http_info)

    def create_click_house_database_user_invoker(self, request):
        http_info = self._create_click_house_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_click_house_database_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClickHouseDatabaseUserResponse"
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

    def create_click_house_instance(self, request):
        """创建实例

        创建实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateClickHouseInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateClickHouseInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateClickHouseInstanceResponse`
        """
        http_info = self._create_click_house_instance_http_info(request)
        return self._call_api(**http_info)

    def create_click_house_instance_invoker(self, request):
        http_info = self._create_click_house_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_click_house_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse",
            "request_type": request.__class__.__name__,
            "response_type": "CreateClickHouseInstanceResponse"
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

    def create_star_rocks_data_replication(self, request):
        """创建StarRocks数据同步

        创建StarRocks数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStarRocksDataReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateStarRocksDataReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateStarRocksDataReplicationResponse`
        """
        http_info = self._create_star_rocks_data_replication_http_info(request)
        return self._call_api(**http_info)

    def create_star_rocks_data_replication_invoker(self, request):
        http_info = self._create_star_rocks_data_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_star_rocks_data_replication_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStarRocksDataReplicationResponse"
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

    def create_star_rocks_database_user(self, request):
        """创建数据库账号

        创建StarRocks数据库账号。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStarRocksDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateStarRocksDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateStarRocksDatabaseUserResponse`
        """
        http_info = self._create_star_rocks_database_user_http_info(request)
        return self._call_api(**http_info)

    def create_star_rocks_database_user_invoker(self, request):
        http_info = self._create_star_rocks_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_star_rocks_database_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/users",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStarRocksDatabaseUserResponse"
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

    def create_starrocks_instance(self, request):
        """创建StarRocks实例

        创建StarRocks实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStarrocksInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateStarrocksInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateStarrocksInstanceResponse`
        """
        http_info = self._create_starrocks_instance_http_info(request)
        return self._call_api(**http_info)

    def create_starrocks_instance_invoker(self, request):
        http_info = self._create_starrocks_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_starrocks_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStarrocksInstanceResponse"
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

    def delete_click_house_data_base_config(self, request):
        """停止修改数据同步

        停止修改数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClickHouseDataBaseConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseDataBaseConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseDataBaseConfigResponse`
        """
        http_info = self._delete_click_house_data_base_config_http_info(request)
        return self._call_api(**http_info)

    def delete_click_house_data_base_config_invoker(self, request):
        http_info = self._delete_click_house_data_base_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_click_house_data_base_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/databases/replication/config",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClickHouseDataBaseConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))

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

    def delete_click_house_data_base_replication(self, request):
        """删除数据同步

        删除数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClickHouseDataBaseReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseDataBaseReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseDataBaseReplicationResponse`
        """
        http_info = self._delete_click_house_data_base_replication_http_info(request)
        return self._call_api(**http_info)

    def delete_click_house_data_base_replication_invoker(self, request):
        http_info = self._delete_click_house_data_base_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_click_house_data_base_replication_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication/{database_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClickHouseDataBaseReplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
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

    def delete_click_house_database_user(self, request):
        """删除数据库账户

        删除数据库账户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClickHouseDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseDatabaseUserResponse`
        """
        http_info = self._delete_click_house_database_user_http_info(request)
        return self._call_api(**http_info)

    def delete_click_house_database_user_invoker(self, request):
        http_info = self._delete_click_house_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_click_house_database_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/users/{user_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClickHouseDatabaseUserResponse"
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

    def delete_click_house_instance(self, request):
        """删除实例

        删除实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClickHouseInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseInstanceResponse`
        """
        http_info = self._delete_click_house_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_click_house_instance_invoker(self, request):
        http_info = self._delete_click_house_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_click_house_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/{clickhouse_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClickHouseInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'clickhouse_instance_id' in local_var_params:
            path_params['clickhouse_instance_id'] = local_var_params['clickhouse_instance_id']

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

    def delete_click_house_lts_config(self, request):
        """批量解除LTS日志配置

        批量解除LTS日志配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteClickHouseLtsConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseLtsConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteClickHouseLtsConfigResponse`
        """
        http_info = self._delete_click_house_lts_config_http_info(request)
        return self._call_api(**http_info)

    def delete_click_house_lts_config_invoker(self, request):
        http_info = self._delete_click_house_lts_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_click_house_lts_config_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/clickhouse/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteClickHouseLtsConfigResponse"
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

    def delete_star_rocks_data_replication(self, request):
        """删除StarRocks数据同步

        删除StarRocks数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStarRocksDataReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteStarRocksDataReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteStarRocksDataReplicationResponse`
        """
        http_info = self._delete_star_rocks_data_replication_http_info(request)
        return self._call_api(**http_info)

    def delete_star_rocks_data_replication_invoker(self, request):
        http_info = self._delete_star_rocks_data_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_star_rocks_data_replication_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStarRocksDataReplicationResponse"
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

    def delete_star_rocks_database_user(self, request):
        """删除数据库账户

        删除StarRocks数据库账户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStarRocksDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteStarRocksDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteStarRocksDatabaseUserResponse`
        """
        http_info = self._delete_star_rocks_database_user_http_info(request)
        return self._call_api(**http_info)

    def delete_star_rocks_database_user_invoker(self, request):
        http_info = self._delete_star_rocks_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_star_rocks_database_user_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/users",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStarRocksDatabaseUserResponse"
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

    def delete_starrocks_instance(self, request):
        """删除StarRocks实例

        删除StarRocks实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStarrocksInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteStarrocksInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteStarrocksInstanceResponse`
        """
        http_info = self._delete_starrocks_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_starrocks_instance_invoker(self, request):
        http_info = self._delete_starrocks_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_starrocks_instance_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/{starrocks_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStarrocksInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'starrocks_instance_id' in local_var_params:
            path_params['starrocks_instance_id'] = local_var_params['starrocks_instance_id']

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

    def list_click_house_data_base(self, request):
        """查询数据库列表

        查询数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClickHouseDataBase
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseResponse`
        """
        http_info = self._list_click_house_data_base_http_info(request)
        return self._call_api(**http_info)

    def list_click_house_data_base_invoker(self, request):
        http_info = self._list_click_house_data_base_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_click_house_data_base_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListClickHouseDataBaseResponse"
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

    def list_click_house_data_base_parameter(self, request):
        """查询数据同步的库参数配置

        查询数据同步的库参数配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClickHouseDataBaseParameter
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseParameterRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseParameterResponse`
        """
        http_info = self._list_click_house_data_base_parameter_http_info(request)
        return self._call_api(**http_info)

    def list_click_house_data_base_parameter_invoker(self, request):
        http_info = self._list_click_house_data_base_parameter_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_click_house_data_base_parameter_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication/database-parameter",
            "request_type": request.__class__.__name__,
            "response_type": "ListClickHouseDataBaseParameterResponse"
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

    def list_click_house_data_base_replication(self, request):
        """查询数据同步信息

        查询数据同步信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClickHouseDataBaseReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseReplicationResponse`
        """
        http_info = self._list_click_house_data_base_replication_http_info(request)
        return self._call_api(**http_info)

    def list_click_house_data_base_replication_invoker(self, request):
        http_info = self._list_click_house_data_base_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_click_house_data_base_replication_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication",
            "request_type": request.__class__.__name__,
            "response_type": "ListClickHouseDataBaseReplicationResponse"
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

    def list_click_house_data_base_replication_config(self, request):
        """查看数据同步配置

        查看数据同步配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClickHouseDataBaseReplicationConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseReplicationConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseDataBaseReplicationConfigResponse`
        """
        http_info = self._list_click_house_data_base_replication_config_http_info(request)
        return self._call_api(**http_info)

    def list_click_house_data_base_replication_config_invoker(self, request):
        http_info = self._list_click_house_data_base_replication_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_click_house_data_base_replication_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/replication/config",
            "request_type": request.__class__.__name__,
            "response_type": "ListClickHouseDataBaseReplicationConfigResponse"
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

    def list_click_house_instance(self, request):
        """查询实例详情

        查询实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClickHouseInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseInstanceResponse`
        """
        http_info = self._list_click_house_instance_http_info(request)
        return self._call_api(**http_info)

    def list_click_house_instance_invoker(self, request):
        http_info = self._list_click_house_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_click_house_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/{clickhouse_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListClickHouseInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'clickhouse_instance_id' in local_var_params:
            path_params['clickhouse_instance_id'] = local_var_params['clickhouse_instance_id']

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

    def list_click_house_instance_node(self, request):
        """查询错误日志、慢日志节点信息

        查询错误日志、慢日志节点信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClickHouseInstanceNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseInstanceNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListClickHouseInstanceNodeResponse`
        """
        http_info = self._list_click_house_instance_node_http_info(request)
        return self._call_api(**http_info)

    def list_click_house_instance_node_invoker(self, request):
        http_info = self._list_click_house_instance_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_click_house_instance_node_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/nodes",
            "request_type": request.__class__.__name__,
            "response_type": "ListClickHouseInstanceNodeResponse"
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

    def list_htap_data_store(self, request):
        """HTAP引擎资源查询

        HTAP引擎资源查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHtapDataStore
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListHtapDataStoreRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListHtapDataStoreResponse`
        """
        http_info = self._list_htap_data_store_http_info(request)
        return self._call_api(**http_info)

    def list_htap_data_store_invoker(self, request):
        http_info = self._list_htap_data_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_htap_data_store_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/htap/datastores/{engine_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListHtapDataStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_name' in local_var_params:
            path_params['engine_name'] = local_var_params['engine_name']

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

    def list_htap_flavor(self, request):
        """HTAP查询规格信息

        HTAP查询规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHtapFlavor
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListHtapFlavorRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListHtapFlavorResponse`
        """
        http_info = self._list_htap_flavor_http_info(request)
        return self._call_api(**http_info)

    def list_htap_flavor_invoker(self, request):
        http_info = self._list_htap_flavor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_htap_flavor_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/htap/flavors/{engine_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListHtapFlavorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_name' in local_var_params:
            path_params['engine_name'] = local_var_params['engine_name']

        query_params = []
        if 'availability_zone_mode' in local_var_params:
            query_params.append(('availability_zone_mode', local_var_params['availability_zone_mode']))
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'version_name' in local_var_params:
            query_params.append(('version_name', local_var_params['version_name']))

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

    def list_htap_instance_info(self, request):
        """查询HTAP实例列表

        查询HTAP实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHtapInstanceInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListHtapInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListHtapInstanceInfoResponse`
        """
        http_info = self._list_htap_instance_info_http_info(request)
        return self._call_api(**http_info)

    def list_htap_instance_info_invoker(self, request):
        http_info = self._list_htap_instance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_htap_instance_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/htap",
            "request_type": request.__class__.__name__,
            "response_type": "ListHtapInstanceInfoResponse"
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

    def list_htap_storage_type(self, request):
        """获取HTAP实例存储类型

        获取HTAP实例存储类型。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHtapStorageType
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListHtapStorageTypeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListHtapStorageTypeResponse`
        """
        http_info = self._list_htap_storage_type_http_info(request)
        return self._call_api(**http_info)

    def list_htap_storage_type_invoker(self, request):
        http_info = self._list_htap_storage_type_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_htap_storage_type_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/htap/storage-type/{database}",
            "request_type": request.__class__.__name__,
            "response_type": "ListHtapStorageTypeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'database' in local_var_params:
            path_params['database'] = local_var_params['database']

        query_params = []
        if 'version_name' in local_var_params:
            query_params.append(('version_name', local_var_params['version_name']))

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

    def list_star_rocks_data_bases(self, request):
        """查询StarRocks数据库

        查询StarRocks数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStarRocksDataBases
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDataBasesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDataBasesResponse`
        """
        http_info = self._list_star_rocks_data_bases_http_info(request)
        return self._call_api(**http_info)

    def list_star_rocks_data_bases_invoker(self, request):
        http_info = self._list_star_rocks_data_bases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_star_rocks_data_bases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListStarRocksDataBasesResponse"
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

    def list_star_rocks_data_replication_config(self, request):
        """查询StarRocks数据同步配置信息

        查询StarRocks数据同步配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStarRocksDataReplicationConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDataReplicationConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDataReplicationConfigResponse`
        """
        http_info = self._list_star_rocks_data_replication_config_http_info(request)
        return self._call_api(**http_info)

    def list_star_rocks_data_replication_config_invoker(self, request):
        http_info = self._list_star_rocks_data_replication_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_star_rocks_data_replication_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication/configuration",
            "request_type": request.__class__.__name__,
            "response_type": "ListStarRocksDataReplicationConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))

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

    def list_star_rocks_data_replications(self, request):
        """查询StarRocks数据同步状态信息

        查询StarRocks数据同步状态信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStarRocksDataReplications
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDataReplicationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDataReplicationsResponse`
        """
        http_info = self._list_star_rocks_data_replications_http_info(request)
        return self._call_api(**http_info)

    def list_star_rocks_data_replications_invoker(self, request):
        http_info = self._list_star_rocks_data_replications_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_star_rocks_data_replications_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication",
            "request_type": request.__class__.__name__,
            "response_type": "ListStarRocksDataReplicationsResponse"
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

    def list_star_rocks_db_parameters(self, request):
        """查询StarRocks数据同步的库参数配置

        查询StarRocks数据同步的库参数配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStarRocksDbParameters
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDbParametersRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListStarRocksDbParametersResponse`
        """
        http_info = self._list_star_rocks_db_parameters_http_info(request)
        return self._call_api(**http_info)

    def list_star_rocks_db_parameters_invoker(self, request):
        http_info = self._list_star_rocks_db_parameters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_star_rocks_db_parameters_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication/database-parameters",
            "request_type": request.__class__.__name__,
            "response_type": "ListStarRocksDbParametersResponse"
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

    def list_starrocks_instance_info(self, request):
        """查询StarRocks实例

        查询StarRocks实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStarrocksInstanceInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListStarrocksInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListStarrocksInstanceInfoResponse`
        """
        http_info = self._list_starrocks_instance_info_http_info(request)
        return self._call_api(**http_info)

    def list_starrocks_instance_info_invoker(self, request):
        http_info = self._list_starrocks_instance_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_starrocks_instance_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/{starrocks_instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListStarrocksInstanceInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'starrocks_instance_id' in local_var_params:
            path_params['starrocks_instance_id'] = local_var_params['starrocks_instance_id']

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

    def pause_star_rocks_data_replication(self, request):
        """暂停StarRocks数据同步

        暂停StarRocks数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PauseStarRocksDataReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.PauseStarRocksDataReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.PauseStarRocksDataReplicationResponse`
        """
        http_info = self._pause_star_rocks_data_replication_http_info(request)
        return self._call_api(**http_info)

    def pause_star_rocks_data_replication_invoker(self, request):
        http_info = self._pause_star_rocks_data_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _pause_star_rocks_data_replication_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication/pause",
            "request_type": request.__class__.__name__,
            "response_type": "PauseStarRocksDataReplicationResponse"
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

    def reboot_click_house_instance(self, request):
        """重启实例

        重启实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootClickHouseInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.RebootClickHouseInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RebootClickHouseInstanceResponse`
        """
        http_info = self._reboot_click_house_instance_http_info(request)
        return self._call_api(**http_info)

    def reboot_click_house_instance_invoker(self, request):
        http_info = self._reboot_click_house_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_click_house_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RebootClickHouseInstanceResponse"
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

    def resize_click_house_flavor(self, request):
        """实例规格变更

        实例规格变更。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeClickHouseFlavor
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResizeClickHouseFlavorRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResizeClickHouseFlavorResponse`
        """
        http_info = self._resize_click_house_flavor_http_info(request)
        return self._call_api(**http_info)

    def resize_click_house_flavor_invoker(self, request):
        http_info = self._resize_click_house_flavor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_click_house_flavor_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/resize-flavor",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeClickHouseFlavorResponse"
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

    def resize_click_house_instance(self, request):
        """实例磁盘扩容

        实例磁盘扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeClickHouseInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResizeClickHouseInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResizeClickHouseInstanceResponse`
        """
        http_info = self._resize_click_house_instance_http_info(request)
        return self._call_api(**http_info)

    def resize_click_house_instance_invoker(self, request):
        http_info = self._resize_click_house_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_click_house_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeClickHouseInstanceResponse"
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

    def resize_star_rocks_flavor(self, request):
        """StarRocks实例规格变更

        StarRocks实例规格变更。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResizeStarRocksFlavor
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResizeStarRocksFlavorRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResizeStarRocksFlavorResponse`
        """
        http_info = self._resize_star_rocks_flavor_http_info(request)
        return self._call_api(**http_info)

    def resize_star_rocks_flavor_invoker(self, request):
        http_info = self._resize_star_rocks_flavor_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resize_star_rocks_flavor_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/resize-flavor",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeStarRocksFlavorResponse"
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

    def restart_starrocks_instance(self, request):
        """重启StarRocks实例

        重启StarRocks实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartStarrocksInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartStarrocksInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartStarrocksInstanceResponse`
        """
        http_info = self._restart_starrocks_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_starrocks_instance_invoker(self, request):
        http_info = self._restart_starrocks_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_starrocks_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{starrocks_instance_id}/starrocks/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartStarrocksInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'starrocks_instance_id' in local_var_params:
            path_params['starrocks_instance_id'] = local_var_params['starrocks_instance_id']

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

    def restart_starrocks_node(self, request):
        """重启StarRocks节点

        重启StarRocks节点。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartStarrocksNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartStarrocksNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartStarrocksNodeResponse`
        """
        http_info = self._restart_starrocks_node_http_info(request)
        return self._call_api(**http_info)

    def restart_starrocks_node_invoker(self, request):
        http_info = self._restart_starrocks_node_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_starrocks_node_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{starrocks_instance_id}/starrocks/{starrocks_node_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartStarrocksNodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'starrocks_node_id' in local_var_params:
            path_params['starrocks_node_id'] = local_var_params['starrocks_node_id']
        if 'starrocks_instance_id' in local_var_params:
            path_params['starrocks_instance_id'] = local_var_params['starrocks_instance_id']

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

    def resume_star_rocks_data_replication(self, request):
        """恢复StarRocks数据同步

        恢复StarRocks数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ResumeStarRocksDataReplication
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResumeStarRocksDataReplicationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResumeStarRocksDataReplicationResponse`
        """
        http_info = self._resume_star_rocks_data_replication_http_info(request)
        return self._call_api(**http_info)

    def resume_star_rocks_data_replication_invoker(self, request):
        http_info = self._resume_star_rocks_data_replication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _resume_star_rocks_data_replication_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/databases/replication/resume",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeStarRocksDataReplicationResponse"
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

    def show_click_house_database_user(self, request):
        """查询数据库账户

        查询数据库账户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClickHouseDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseDatabaseUserResponse`
        """
        http_info = self._show_click_house_database_user_http_info(request)
        return self._call_api(**http_info)

    def show_click_house_database_user_invoker(self, request):
        http_info = self._show_click_house_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_click_house_database_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/users",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClickHouseDatabaseUserResponse"
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
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))

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

    def show_click_house_lts_config(self, request):
        """查询实例LTS日志配置列表

        查询实例LTS日志配置列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClickHouseLtsConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseLtsConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseLtsConfigResponse`
        """
        http_info = self._show_click_house_lts_config_http_info(request)
        return self._call_api(**http_info)

    def show_click_house_lts_config_invoker(self, request):
        http_info = self._show_click_house_lts_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_click_house_lts_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/clickhouse/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClickHouseLtsConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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

    def show_click_house_slow_log_detail(self, request):
        """查询慢日志

        获取内核慢日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClickHouseSlowLogDetail
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseSlowLogDetailRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseSlowLogDetailResponse`
        """
        http_info = self._show_click_house_slow_log_detail_http_info(request)
        return self._call_api(**http_info)

    def show_click_house_slow_log_detail_invoker(self, request):
        http_info = self._show_click_house_slow_log_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_click_house_slow_log_detail_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/slow-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClickHouseSlowLogDetailResponse"
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

    def show_click_house_slow_log_sensitive_status(self, request):
        """查询慢日志脱敏状态

        查询慢日志脱敏状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowClickHouseSlowLogSensitiveStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseSlowLogSensitiveStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowClickHouseSlowLogSensitiveStatusResponse`
        """
        http_info = self._show_click_house_slow_log_sensitive_status_http_info(request)
        return self._call_api(**http_info)

    def show_click_house_slow_log_sensitive_status_invoker(self, request):
        http_info = self._show_click_house_slow_log_sensitive_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_click_house_slow_log_sensitive_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/slowlog-sensitive",
            "request_type": request.__class__.__name__,
            "response_type": "ShowClickHouseSlowLogSensitiveStatusResponse"
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

    def show_star_rocks_database_user(self, request):
        """查询数据库账户

        查询StarRocks数据库账户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStarRocksDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowStarRocksDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowStarRocksDatabaseUserResponse`
        """
        http_info = self._show_star_rocks_database_user_http_info(request)
        return self._call_api(**http_info)

    def show_star_rocks_database_user_invoker(self, request):
        http_info = self._show_star_rocks_database_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_star_rocks_database_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/users",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStarRocksDatabaseUserResponse"
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

    def show_starrocks_params(self, request):
        """查询参数

        按节点类型查询参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowStarrocksParams
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowStarrocksParamsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowStarrocksParamsResponse`
        """
        http_info = self._show_starrocks_params_http_info(request)
        return self._call_api(**http_info)

    def show_starrocks_params_invoker(self, request):
        http_info = self._show_starrocks_params_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_starrocks_params_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStarrocksParamsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'node_type' in local_var_params:
            query_params.append(('node_type', local_var_params['node_type']))
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

    def sync_star_rocks_users(self, request):
        """StarRocks实例开启行列分流

        StarRocks实例开启行列分流。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SyncStarRocksUsers
        :type request: :class:`huaweicloudsdkgaussdb.v3.SyncStarRocksUsersRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SyncStarRocksUsersResponse`
        """
        http_info = self._sync_star_rocks_users_http_info(request)
        return self._call_api(**http_info)

    def sync_star_rocks_users_invoker(self, request):
        http_info = self._sync_star_rocks_users_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _sync_star_rocks_users_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/users/sync",
            "request_type": request.__class__.__name__,
            "response_type": "SyncStarRocksUsersResponse"
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

    def update_click_house_data_base_config(self, request):
        """修改数据同步

        修改数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClickHouseDataBaseConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseDataBaseConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseDataBaseConfigResponse`
        """
        http_info = self._update_click_house_data_base_config_http_info(request)
        return self._call_api(**http_info)

    def update_click_house_data_base_config_invoker(self, request):
        http_info = self._update_click_house_data_base_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_click_house_data_base_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/databases/replication/config",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClickHouseDataBaseConfigResponse"
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

    def update_click_house_database_user_password(self, request):
        """修改数据库账号密码

        修改数据库账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClickHouseDatabaseUserPassword
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseDatabaseUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseDatabaseUserPasswordResponse`
        """
        http_info = self._update_click_house_database_user_password_http_info(request)
        return self._call_api(**http_info)

    def update_click_house_database_user_password_invoker(self, request):
        http_info = self._update_click_house_database_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_click_house_database_user_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/users/password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClickHouseDatabaseUserPasswordResponse"
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

    def update_click_house_database_user_permission(self, request):
        """修改数据库账号权限

        修改数据库账号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClickHouseDatabaseUserPermission
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseDatabaseUserPermissionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseDatabaseUserPermissionResponse`
        """
        http_info = self._update_click_house_database_user_permission_http_info(request)
        return self._call_api(**http_info)

    def update_click_house_database_user_permission_invoker(self, request):
        http_info = self._update_click_house_database_user_permission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_click_house_database_user_permission_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/users/permission",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClickHouseDatabaseUserPermissionResponse"
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

    def update_click_house_lts_config(self, request):
        """批量创建LTS日志配置

        批量创建LTS日志配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClickHouseLtsConfig
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseLtsConfigRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseLtsConfigResponse`
        """
        http_info = self._update_click_house_lts_config_http_info(request)
        return self._call_api(**http_info)

    def update_click_house_lts_config_invoker(self, request):
        http_info = self._update_click_house_lts_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_click_house_lts_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/clickhouse/instances/logs/lts-configs",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClickHouseLtsConfigResponse"
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

    def update_click_house_slow_log_sensitive_status(self, request):
        """修改慢日志脱敏状态

        修改慢日志脱敏状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateClickHouseSlowLogSensitiveStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseSlowLogSensitiveStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateClickHouseSlowLogSensitiveStatusResponse`
        """
        http_info = self._update_click_house_slow_log_sensitive_status_http_info(request)
        return self._call_api(**http_info)

    def update_click_house_slow_log_sensitive_status_invoker(self, request):
        http_info = self._update_click_house_slow_log_sensitive_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_click_house_slow_log_sensitive_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/clickhouse/slowlog-sensitive",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateClickHouseSlowLogSensitiveStatusResponse"
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

    def update_star_rocks_database_user_password(self, request):
        """修改数据库账号密码

        修改StarRocks数据库账号密码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStarRocksDatabaseUserPassword
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateStarRocksDatabaseUserPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateStarRocksDatabaseUserPasswordResponse`
        """
        http_info = self._update_star_rocks_database_user_password_http_info(request)
        return self._call_api(**http_info)

    def update_star_rocks_database_user_password_invoker(self, request):
        http_info = self._update_star_rocks_database_user_password_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_star_rocks_database_user_password_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/users/password",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStarRocksDatabaseUserPasswordResponse"
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

    def update_star_rocks_database_user_permission(self, request):
        """修改数据库账号权限

        修改StarRocks数据库账号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStarRocksDatabaseUserPermission
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateStarRocksDatabaseUserPermissionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateStarRocksDatabaseUserPermissionResponse`
        """
        http_info = self._update_star_rocks_database_user_permission_http_info(request)
        return self._call_api(**http_info)

    def update_star_rocks_database_user_permission_invoker(self, request):
        http_info = self._update_star_rocks_database_user_permission_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_star_rocks_database_user_permission_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/users/permission",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStarRocksDatabaseUserPermissionResponse"
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

    def update_starrocks_params(self, request):
        """修改参数

        按节点类型修改节点参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStarrocksParams
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateStarrocksParamsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateStarrocksParamsResponse`
        """
        http_info = self._update_starrocks_params_http_info(request)
        return self._call_api(**http_info)

    def update_starrocks_params_invoker(self, request):
        http_info = self._update_starrocks_params_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_starrocks_params_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/starrocks/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStarrocksParamsResponse"
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

    def delete_sql_filter_rule(self, request):
        """删除SQL限流规则

        删除SQL限流规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlFilterRule
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteSqlFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteSqlFilterRuleResponse`
        """
        http_info = self._delete_sql_filter_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_sql_filter_rule_invoker(self, request):
        http_info = self._delete_sql_filter_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sql_filter_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-filter/rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlFilterRuleResponse"
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

    def set_sql_filter_rule(self, request):
        """设置SQL限流规则

        设置SQL限流规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetSqlFilterRule
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetSqlFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetSqlFilterRuleResponse`
        """
        http_info = self._set_sql_filter_rule_http_info(request)
        return self._call_api(**http_info)

    def set_sql_filter_rule_invoker(self, request):
        http_info = self._set_sql_filter_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_sql_filter_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-filter/rules",
            "request_type": request.__class__.__name__,
            "response_type": "SetSqlFilterRuleResponse"
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

    def show_sql_filter_control(self, request):
        """查询SQL限流开关状态

        查询SQL限流开关状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlFilterControl
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterControlRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterControlResponse`
        """
        http_info = self._show_sql_filter_control_http_info(request)
        return self._call_api(**http_info)

    def show_sql_filter_control_invoker(self, request):
        http_info = self._show_sql_filter_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_filter_control_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-filter/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlFilterControlResponse"
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

    def show_sql_filter_rule(self, request):
        """查询SQL限流规则

        查询SQL限流规则。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlFilterRule
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterRuleResponse`
        """
        http_info = self._show_sql_filter_rule_http_info(request)
        return self._call_api(**http_info)

    def show_sql_filter_rule_invoker(self, request):
        http_info = self._show_sql_filter_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_filter_rule_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-filter/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlFilterRuleResponse"
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
        if 'sql_type' in local_var_params:
            query_params.append(('sql_type', local_var_params['sql_type']))

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

    def update_sql_filter_control(self, request):
        """开启或者关闭SQL限流

        开启或者关闭SQL限流。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlFilterControl
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateSqlFilterControlRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateSqlFilterControlResponse`
        """
        http_info = self._update_sql_filter_control_http_info(request)
        return self._call_api(**http_info)

    def update_sql_filter_control_invoker(self, request):
        http_info = self._update_sql_filter_control_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sql_filter_control_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-filter/switch",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSqlFilterControlResponse"
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

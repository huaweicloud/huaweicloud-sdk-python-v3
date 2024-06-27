# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkgaussdbforopengauss'")


class GaussDBforopenGaussAsyncClient(Client):
    def __init__(self):
        super(GaussDBforopenGaussAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgaussdbforopengauss.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GaussDBforopenGaussAsyncClient":
                raise TypeError("client type error, support client type is GaussDBforopenGaussAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_instance_tags_async(self, request):
        """添加实例标签。

        对指定实例添加用户标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddInstanceTags
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.AddInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.AddInstanceTagsResponse`
        """
        http_info = self._add_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def add_instance_tags_async_invoker(self, request):
        http_info = self._add_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_instance_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "AddInstanceTagsResponse"
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

    def allow_db_privileges_async(self, request):
        """授权数据库帐号

        在指定实例的数据库中, 设置帐号的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AllowDbPrivileges
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.AllowDbPrivilegesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.AllowDbPrivilegesResponse`
        """
        http_info = self._allow_db_privileges_http_info(request)
        return self._call_api(**http_info)

    def allow_db_privileges_async_invoker(self, request):
        http_info = self._allow_db_privileges_http_info(request)
        return AsyncInvoker(self, http_info)

    def _allow_db_privileges_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-privilege",
            "request_type": request.__class__.__name__,
            "response_type": "AllowDbPrivilegesResponse"
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

    def attach_eip_async(self, request):
        """绑定/解绑弹性公网IP

        实例下的节点绑定弹性公网IP/解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachEip
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.AttachEipRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.AttachEipResponse`
        """
        http_info = self._attach_eip_http_info(request)
        return self._call_api(**http_info)

    def attach_eip_async_invoker(self, request):
        http_info = self._attach_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/public-ip",
            "request_type": request.__class__.__name__,
            "response_type": "AttachEipResponse"
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

    def confirm_restored_data_async(self, request):
        """备份恢复到目标实例数据后执行数据确认

        确认备份恢复到目标实例的数据正常。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmRestoredData
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ConfirmRestoredDataRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ConfirmRestoredDataResponse`
        """
        http_info = self._confirm_restored_data_http_info(request)
        return self._call_api(**http_info)

    def confirm_restored_data_async_invoker(self, request):
        http_info = self._confirm_restored_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_restored_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/confirm-restore-data",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmRestoredDataResponse"
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

    def copy_configuration_async(self, request):
        """复制参数模板

        复制参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyConfiguration
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CopyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CopyConfigurationResponse`
        """
        http_info = self._copy_configuration_http_info(request)
        return self._call_api(**http_info)

    def copy_configuration_async_invoker(self, request):
        http_info = self._copy_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_configuration_http_info(self, request):
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

    def create_configuration_template_async(self, request):
        """创建参数模板

        创建参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfigurationTemplate
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateConfigurationTemplateRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateConfigurationTemplateResponse`
        """
        http_info = self._create_configuration_template_http_info(request)
        return self._call_api(**http_info)

    def create_configuration_template_async_invoker(self, request):
        http_info = self._create_configuration_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_configuration_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConfigurationTemplateResponse"
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

    def create_database_async(self, request):
        """创建数据库

        在指定实例中创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDatabaseResponse`
        """
        http_info = self._create_database_http_info(request)
        return self._call_api(**http_info)

    def create_database_async_invoker(self, request):
        http_info = self._create_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_database_http_info(self, request):
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

    def create_database_schemas_async(self, request):
        """创建数据库SCHEMA

        在指定实例的数据库中, 创建数据库schema。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatabaseSchemas
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDatabaseSchemasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDatabaseSchemasResponse`
        """
        http_info = self._create_database_schemas_http_info(request)
        return self._call_api(**http_info)

    def create_database_schemas_async_invoker(self, request):
        http_info = self._create_database_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_database_schemas_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/schema",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseSchemasResponse"
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

    def create_db_instance_async(self, request):
        """创建数据库实例

        创建数据库实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDbInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDbInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDbInstanceResponse`
        """
        http_info = self._create_db_instance_http_info(request)
        return self._call_api(**http_info)

    def create_db_instance_async_invoker(self, request):
        http_info = self._create_db_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_db_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3.1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDbInstanceResponse"
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

    def create_db_user_async(self, request):
        """创建数据库用户

        在指定实例中创建数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDbUser
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDbUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateDbUserResponse`
        """
        http_info = self._create_db_user_http_info(request)
        return self._call_api(**http_info)

    def create_db_user_async_invoker(self, request):
        http_info = self._create_db_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_db_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-user",
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

    def create_instance_async(self, request):
        """创建数据库实例

        创建数据库企业版和集中式实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateInstanceResponse`
        """
        http_info = self._create_instance_http_info(request)
        return self._call_api(**http_info)

    def create_instance_async_invoker(self, request):
        http_info = self._create_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instance_http_info(self, request):
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

    def create_manual_backup_async(self, request):
        """创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateManualBackup
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateManualBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateManualBackupResponse`
        """
        http_info = self._create_manual_backup_http_info(request)
        return self._call_api(**http_info)

    def create_manual_backup_async_invoker(self, request):
        http_info = self._create_manual_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_manual_backup_http_info(self, request):
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

    def create_restore_instance_async(self, request):
        """恢复到新实例

        根据备份恢复新实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRestoreInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateRestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateRestoreInstanceResponse`
        """
        http_info = self._create_restore_instance_http_info(request)
        return self._call_api(**http_info)

    def create_restore_instance_async_invoker(self, request):
        http_info = self._create_restore_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_restore_instance_http_info(self, request):
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

    def create_slow_log_download_async(self, request):
        """创建慢日志下载信息

        创建慢日志下载信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSlowLogDownload
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateSlowLogDownloadRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.CreateSlowLogDownloadResponse`
        """
        http_info = self._create_slow_log_download_http_info(request)
        return self._call_api(**http_info)

    def create_slow_log_download_async_invoker(self, request):
        http_info = self._create_slow_log_download_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_slow_log_download_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/download",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSlowLogDownloadResponse"
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

    def delete_configuration_async(self, request):
        """删除参数模板

        删除参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteConfigurationResponse`
        """
        http_info = self._delete_configuration_http_info(request)
        return self._call_api(**http_info)

    def delete_configuration_async_invoker(self, request):
        http_info = self._delete_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_configuration_http_info(self, request):
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

    def delete_database_async(self, request):
        """删除数据库

        删除指定实例的数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteDatabaseResponse`
        """
        http_info = self._delete_database_http_info(request)
        return self._call_api(**http_info)

    def delete_database_async_invoker(self, request):
        http_info = self._delete_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_database_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/database",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatabaseResponse"
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

    def delete_instance_async(self, request):
        """删除实例

        删除数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteInstanceResponse`
        """
        http_info = self._delete_instance_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_async_invoker(self, request):
        http_info = self._delete_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_http_info(self, request):
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

    def delete_instance_tag_async(self, request):
        """删除实例标签

        删除实例标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstanceTag
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteInstanceTagRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteInstanceTagResponse`
        """
        http_info = self._delete_instance_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_instance_tag_async_invoker(self, request):
        http_info = self._delete_instance_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_instance_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/tag",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstanceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))

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

    def delete_job_async(self, request):
        """删除任务记录

        删除任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_async_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobResponse"
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

    def delete_manual_backup_async(self, request):
        """删除手动备份

        删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteManualBackup
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DeleteManualBackupResponse`
        """
        http_info = self._delete_manual_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_manual_backup_async_invoker(self, request):
        http_info = self._delete_manual_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_manual_backup_http_info(self, request):
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

    def download_backup_async(self, request):
        """获取备份下载链接

        获取备份下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBackup
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.DownloadBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DownloadBackupResponse`
        """
        http_info = self._download_backup_http_info(request)
        return self._call_api(**http_info)

    def download_backup_async_invoker(self, request):
        http_info = self._download_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_backup_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/backup-files",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadBackupResponse"
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

    def list_applicable_instances_async(self, request):
        """查询可应用实例列表

        查询可应用当前参数组模板的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplicableInstances
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListApplicableInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListApplicableInstancesResponse`
        """
        http_info = self._list_applicable_instances_http_info(request)
        return self._call_api(**http_info)

    def list_applicable_instances_async_invoker(self, request):
        http_info = self._list_applicable_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applicable_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/applicable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicableInstancesResponse"
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

    def list_applied_histories_async(self, request):
        """查询参数模板的应用记录

        查询参数模板的应用记录，以实例级别为维度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAppliedHistories
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListAppliedHistoriesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListAppliedHistoriesResponse`
        """
        http_info = self._list_applied_histories_http_info(request)
        return self._call_api(**http_info)

    def list_applied_histories_async_invoker(self, request):
        http_info = self._list_applied_histories_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applied_histories_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/applied-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppliedHistoriesResponse"
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

    def list_available_flavors_async(self, request):
        """查询实例可变更规格

        查询实例可变更规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableFlavors
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListAvailableFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListAvailableFlavorsResponse`
        """
        http_info = self._list_available_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_available_flavors_async_invoker(self, request):
        http_info = self._list_available_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_available_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/available-flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableFlavorsResponse"
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

    def list_backups_async(self, request):
        """查询备份列表

        获取备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListBackupsResponse`
        """
        http_info = self._list_backups_http_info(request)
        return self._call_api(**http_info)

    def list_backups_async_invoker(self, request):
        http_info = self._list_backups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backups_http_info(self, request):
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

    def list_binded_eips_async(self, request):
        """查询实例已绑定EIP列表

        查询实例已绑定EIP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBindedEips
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListBindedEipsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListBindedEipsResponse`
        """
        http_info = self._list_binded_eips_http_info(request)
        return self._call_api(**http_info)

    def list_binded_eips_async_invoker(self, request):
        http_info = self._list_binded_eips_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_binded_eips_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/public-ips",
            "request_type": request.__class__.__name__,
            "response_type": "ListBindedEipsResponse"
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

    def list_cn_infos_before_reduce_async(self, request):
        """查询协调节点列表

        查询协调节点列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCnInfosBeforeReduce
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListCnInfosBeforeReduceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListCnInfosBeforeReduceResponse`
        """
        http_info = self._list_cn_infos_before_reduce_http_info(request)
        return self._call_api(**http_info)

    def list_cn_infos_before_reduce_async_invoker(self, request):
        http_info = self._list_cn_infos_before_reduce_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_cn_infos_before_reduce_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/coordinators",
            "request_type": request.__class__.__name__,
            "response_type": "ListCnInfosBeforeReduceResponse"
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

    def list_component_infos_async(self, request):
        """查询实例的组件列表

        查询实例的组件列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListComponentInfos
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListComponentInfosRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListComponentInfosResponse`
        """
        http_info = self._list_component_infos_http_info(request)
        return self._call_api(**http_info)

    def list_component_infos_async_invoker(self, request):
        http_info = self._list_component_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_component_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/components",
            "request_type": request.__class__.__name__,
            "response_type": "ListComponentInfosResponse"
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
        if 'component_type' in local_var_params:
            query_params.append(('component_type', local_var_params['component_type']))
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))

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

    def list_configurations_async(self, request):
        """获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListConfigurationsResponse`
        """
        http_info = self._list_configurations_http_info(request)
        return self._call_api(**http_info)

    def list_configurations_async_invoker(self, request):
        http_info = self._list_configurations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_configurations_http_info(self, request):
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

    def list_configurations_diff_async(self, request):
        """比较两个参数组模板之间的差异

        获取两个参数配置模板的差异列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurationsDiff
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListConfigurationsDiffRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListConfigurationsDiffResponse`
        """
        http_info = self._list_configurations_diff_http_info(request)
        return self._call_api(**http_info)

    def list_configurations_diff_async_invoker(self, request):
        http_info = self._list_configurations_diff_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_configurations_diff_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/configurations/comparison",
            "request_type": request.__class__.__name__,
            "response_type": "ListConfigurationsDiffResponse"
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

    def list_database_schemas_async(self, request):
        """查询数据库SCHEMA列表

        查询指定实例的数据库SCHEMA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabaseSchemas
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatabaseSchemasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatabaseSchemasResponse`
        """
        http_info = self._list_database_schemas_http_info(request)
        return self._call_api(**http_info)

    def list_database_schemas_async_invoker(self, request):
        http_info = self._list_database_schemas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_database_schemas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/schemas",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatabaseSchemasResponse"
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

    def list_databases_async(self, request):
        """查询数据库列表

        查询指定实例中的数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatabasesResponse`
        """
        http_info = self._list_databases_http_info(request)
        return self._call_api(**http_info)

    def list_databases_async_invoker(self, request):
        http_info = self._list_databases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_databases_http_info(self, request):
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

    def list_datastores_async(self, request):
        """查询数据库引擎的版本

        查询指定数据库引擎对应的版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatastores
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatastoresRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDatastoresResponse`
        """
        http_info = self._list_datastores_http_info(request)
        return self._call_api(**http_info)

    def list_datastores_async_invoker(self, request):
        http_info = self._list_datastores_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_datastores_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/datastore/versions",
            "request_type": request.__class__.__name__,
            "response_type": "ListDatastoresResponse"
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

    def list_db_backups_async(self, request):
        """查询备份列表

        获取备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbBackups
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDbBackupsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDbBackupsResponse`
        """
        http_info = self._list_db_backups_http_info(request)
        return self._call_api(**http_info)

    def list_db_backups_async_invoker(self, request):
        http_info = self._list_db_backups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_db_backups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbBackupsResponse"
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

    def list_db_flavors_async(self, request):
        """查询数据库规格

        查询数据库的规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbFlavors
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDbFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDbFlavorsResponse`
        """
        http_info = self._list_db_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_db_flavors_async_invoker(self, request):
        http_info = self._list_db_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_db_flavors_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/flavors",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbFlavorsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'ha_mode' in local_var_params:
            query_params.append(('ha_mode', local_var_params['ha_mode']))
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

    def list_db_users_async(self, request):
        """查询数据库用户列表

        在指定实例中查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListDbUsersResponse`
        """
        http_info = self._list_db_users_http_info(request)
        return self._call_api(**http_info)

    def list_db_users_async_invoker(self, request):
        http_info = self._list_db_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_db_users_http_info(self, request):
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

    def list_eps_quotas_async(self, request):
        """查询企业项目配额组

        查询企业项目配额组信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEpsQuotas
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListEpsQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListEpsQuotasResponse`
        """
        http_info = self._list_eps_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_eps_quotas_async_invoker(self, request):
        http_info = self._list_eps_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_eps_quotas_http_info(self, request):
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
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

    def list_flavors_async(self, request):
        """查询数据库规格

        查询数据库的规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListFlavorsResponse`
        """
        http_info = self._list_flavors_http_info(request)
        return self._call_api(**http_info)

    def list_flavors_async_invoker(self, request):
        http_info = self._list_flavors_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_flavors_http_info(self, request):
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
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
        if 'spec_code' in local_var_params:
            query_params.append(('spec_code', local_var_params['spec_code']))
        if 'ha_mode' in local_var_params:
            query_params.append(('ha_mode', local_var_params['ha_mode']))
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

    def list_gauss_db_datastores_async(self, request):
        """查询引擎列表

        查询引擎列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussDbDatastores
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListGaussDbDatastoresRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListGaussDbDatastoresResponse`
        """
        http_info = self._list_gauss_db_datastores_http_info(request)
        return self._call_api(**http_info)

    def list_gauss_db_datastores_async_invoker(self, request):
        http_info = self._list_gauss_db_datastores_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_gauss_db_datastores_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/datastores",
            "request_type": request.__class__.__name__,
            "response_type": "ListGaussDbDatastoresResponse"
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

    def list_history_operations_async(self, request):
        """查询参数模板的修改历史

        查询参数模板的修改历史记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListHistoryOperations
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListHistoryOperationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListHistoryOperationsResponse`
        """
        http_info = self._list_history_operations_http_info(request)
        return self._call_api(**http_info)

    def list_history_operations_async_invoker(self, request):
        http_info = self._list_history_operations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_history_operations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/{config_id}/histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryOperationsResponse"
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

    def list_instance_details_async(self, request):
        """查询数据库实例列表/查询实例详情

        查询数据库实例列表/查询实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceDetails
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstanceDetailsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstanceDetailsResponse`
        """
        http_info = self._list_instance_details_http_info(request)
        return self._call_api(**http_info)

    def list_instance_details_async_invoker(self, request):
        http_info = self._list_instance_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.2/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceDetailsResponse"
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
            collection_formats['tags'] = 'csv'
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))

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

    def list_instance_error_logs_async(self, request):
        """查询错误日志下载链接

        查询数据库错误日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceErrorLogs
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstanceErrorLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstanceErrorLogsResponse`
        """
        http_info = self._list_instance_error_logs_http_info(request)
        return self._call_api(**http_info)

    def list_instance_error_logs_async_invoker(self, request):
        http_info = self._list_instance_error_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_error_logs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/error-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceErrorLogsResponse"
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

    def list_instance_tags_async(self, request):
        """查询实例标签

        查询指定实例的用户标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstanceTagsResponse`
        """
        http_info = self._list_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_tags_async_invoker(self, request):
        http_info = self._list_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_tags_http_info(self, request):
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

    def list_instances_async(self, request):
        """查询数据库实例列表/查询实例详情

        查询数据库实例列表/查询实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstancesResponse`
        """
        http_info = self._list_instances_http_info(request)
        return self._call_api(**http_info)

    def list_instances_async_invoker(self, request):
        http_info = self._list_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_http_info(self, request):
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
            collection_formats['tags'] = 'csv'
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))

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

    def list_instances_details_async(self, request):
        """查询数据库实例列表/查询实例详情

        查询数据库实例列表/查询实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesDetails
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstancesDetailsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListInstancesDetailsResponse`
        """
        http_info = self._list_instances_details_http_info(request)
        return self._call_api(**http_info)

    def list_instances_details_async_invoker(self, request):
        http_info = self._list_instances_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instances_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstancesDetailsResponse"
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
            collection_formats['tags'] = 'csv'
        if 'charge_mode' in local_var_params:
            query_params.append(('charge_mode', local_var_params['charge_mode']))

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

    def list_param_group_templates_async(self, request):
        """获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListParamGroupTemplates
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListParamGroupTemplatesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListParamGroupTemplatesResponse`
        """
        http_info = self._list_param_group_templates_http_info(request)
        return self._call_api(**http_info)

    def list_param_group_templates_async_invoker(self, request):
        http_info = self._list_param_group_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_param_group_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListParamGroupTemplatesResponse"
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

    def list_predefined_tags_async(self, request):
        """查询预定义标签

        查询预预定义标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPredefinedTags
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListPredefinedTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListPredefinedTagsResponse`
        """
        http_info = self._list_predefined_tags_http_info(request)
        return self._call_api(**http_info)

    def list_predefined_tags_async_invoker(self, request):
        http_info = self._list_predefined_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_predefined_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/predefined-tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListPredefinedTagsResponse"
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

    def list_project_tags_async(self, request):
        """查询项目标签

        查询项目下所有用户标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
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

    def list_recycle_instances_async(self, request):
        """查询回收站所有引擎实例列表。

        查询回收站所有引擎实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListRecycleInstancesResponse`
        """
        http_info = self._list_recycle_instances_http_info(request)
        return self._call_api(**http_info)

    def list_recycle_instances_async_invoker(self, request):
        http_info = self._list_recycle_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_recycle_instances_http_info(self, request):
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
        if 'instance_name' in local_var_params:
            query_params.append(('instance_name', local_var_params['instance_name']))
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

    def list_restorable_instances_async(self, request):
        """查询可用于备份恢复的实例列表

        查询可用于备份恢复的实例列表，实例信息要符合备份条件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRestorableInstances
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListRestorableInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListRestorableInstancesResponse`
        """
        http_info = self._list_restorable_instances_http_info(request)
        return self._call_api(**http_info)

    def list_restorable_instances_async_invoker(self, request):
        http_info = self._list_restorable_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_restorable_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/restorable-instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListRestorableInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_instance_id' in local_var_params:
            query_params.append(('source_instance_id', local_var_params['source_instance_id']))
        if 'backup_id' in local_var_params:
            query_params.append(('backup_id', local_var_params['backup_id']))
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

    def list_restore_times_async(self, request):
        """查询可恢复时间段

        查询可恢复时间段。
        如果您备份策略中的保存天数设置较长，建议您传入查询日期“date”。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRestoreTimes
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListRestoreTimesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListRestoreTimesResponse`
        """
        http_info = self._list_restore_times_http_info(request)
        return self._call_api(**http_info)

    def list_restore_times_async_invoker(self, request):
        http_info = self._list_restore_times_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_restore_times_http_info(self, request):
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

    def list_storage_types_async(self, request):
        """查询数据库磁盘类型

        查询指定数据库引擎对应的磁盘类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStorageTypes
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListStorageTypesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListStorageTypesResponse`
        """
        http_info = self._list_storage_types_http_info(request)
        return self._call_api(**http_info)

    def list_storage_types_async_invoker(self, request):
        http_info = self._list_storage_types_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_storage_types_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/storage-type",
            "request_type": request.__class__.__name__,
            "response_type": "ListStorageTypesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))
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

    def list_tasks_async(self, request):
        """查询任务列表

        获取任务中心的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTasksRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_async_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def list_top_io_traffics_async(self, request):
        """查询Top IO列表

        查询实例数据库进程下的Top IO流量数据，返回与会话信息相关联后的结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopIoTraffics
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTopIoTrafficsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ListTopIoTrafficsResponse`
        """
        http_info = self._list_top_io_traffics_http_info(request)
        return self._call_api(**http_info)

    def list_top_io_traffics_async_invoker(self, request):
        http_info = self._list_top_io_traffics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_top_io_traffics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/top-io-traffics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopIoTrafficsResponse"
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
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))
        if 'top_io_num' in local_var_params:
            query_params.append(('top_io_num', local_var_params['top_io_num']))
        if 'sort_condition' in local_var_params:
            query_params.append(('sort_condition', local_var_params['sort_condition']))

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

    def modify_eps_quota_async(self, request):
        """修改企业项目配额

        修改企业项目配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyEpsQuota
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ModifyEpsQuotaRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ModifyEpsQuotaResponse`
        """
        http_info = self._modify_eps_quota_http_info(request)
        return self._call_api(**http_info)

    def modify_eps_quota_async_invoker(self, request):
        http_info = self._modify_eps_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _modify_eps_quota_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/enterprise-projects/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ModifyEpsQuotaResponse"
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

    def reset_configuration_async(self, request):
        """重置参数模板

        重置参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetConfiguration
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResetConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResetConfigurationResponse`
        """
        http_info = self._reset_configuration_http_info(request)
        return self._call_api(**http_info)

    def reset_configuration_async_invoker(self, request):
        http_info = self._reset_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_configuration_http_info(self, request):
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

    def reset_pwd_async(self, request):
        """重置数据库密码。

        重置数据库密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPwd
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResetPwdRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResetPwdResponse`
        """
        http_info = self._reset_pwd_http_info(request)
        return self._call_api(**http_info)

    def reset_pwd_async_invoker(self, request):
        http_info = self._reset_pwd_http_info(request)
        return AsyncInvoker(self, http_info)

    def _reset_pwd_http_info(self, request):
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

    def resize_instance_flavor_async(self, request):
        """GaussDB数据库实例规格变更

        GaussDB数据库实例规格变更
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstanceFlavor
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResizeInstanceFlavorRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ResizeInstanceFlavorResponse`
        """
        http_info = self._resize_instance_flavor_http_info(request)
        return self._call_api(**http_info)

    def resize_instance_flavor_async_invoker(self, request):
        http_info = self._resize_instance_flavor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_instance_flavor_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instance/{instance_id}/flavor",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeInstanceFlavorResponse"
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

    def restart_instance_async(self, request):
        """重启数据库实例

        重启数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestartInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestartInstanceResponse`
        """
        http_info = self._restart_instance_http_info(request)
        return self._call_api(**http_info)

    def restart_instance_async_invoker(self, request):
        http_info = self._restart_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_instance_http_info(self, request):
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

    def restore_instance_async(self, request):
        """备份恢复到当前实例

        备份恢复到当前实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RestoreInstanceResponse`
        """
        http_info = self._restore_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_instance_async_invoker(self, request):
        http_info = self._restore_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_instance_http_info(self, request):
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

    def run_instance_action_async(self, request):
        """CN横向扩容/DN分片扩容/磁盘扩容

        CN横向扩容/DN分片扩容/磁盘扩容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunInstanceAction
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.RunInstanceActionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RunInstanceActionResponse`
        """
        http_info = self._run_instance_action_http_info(request)
        return self._call_api(**http_info)

    def run_instance_action_async_invoker(self, request):
        http_info = self._run_instance_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_instance_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RunInstanceActionResponse"
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

    def search_auto_enlarge_policy_async(self, request):
        """查询磁盘自动扩容策略

        查询磁盘自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SearchAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SearchAutoEnlargePolicyResponse`
        """
        http_info = self._search_auto_enlarge_policy_http_info(request)
        return self._call_api(**http_info)

    def search_auto_enlarge_policy_async_invoker(self, request):
        http_info = self._search_auto_enlarge_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_auto_enlarge_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/auto-enlarge-policy",
            "request_type": request.__class__.__name__,
            "response_type": "SearchAutoEnlargePolicyResponse"
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

    def set_backup_policy_async(self, request):
        """设置自动备份策略。

        设置自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetBackupPolicyResponse`
        """
        http_info = self._set_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def set_backup_policy_async_invoker(self, request):
        http_info = self._set_backup_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_backup_policy_http_info(self, request):
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

    def set_db_user_pwd_async(self, request):
        """重置数据库帐号密码

        重置指定数据库帐号的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetDbUserPwd
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetDbUserPwdRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetDbUserPwdResponse`
        """
        http_info = self._set_db_user_pwd_http_info(request)
        return self._call_api(**http_info)

    def set_db_user_pwd_async_invoker(self, request):
        http_info = self._set_db_user_pwd_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_db_user_pwd_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-user/password",
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

    def set_new_backup_policy_async(self, request):
        """设置自动备份策略

        设置自动备份策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetNewBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetNewBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetNewBackupPolicyResponse`
        """
        http_info = self._set_new_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def set_new_backup_policy_async_invoker(self, request):
        http_info = self._set_new_backup_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_new_backup_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/backups/policy",
            "request_type": request.__class__.__name__,
            "response_type": "SetNewBackupPolicyResponse"
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

    def set_recycle_policy_async(self, request):
        """设置回收站策略

        设置回收站策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SetRecyclePolicyResponse`
        """
        http_info = self._set_recycle_policy_http_info(request)
        return self._call_api(**http_info)

    def set_recycle_policy_async_invoker(self, request):
        http_info = self._set_recycle_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _set_recycle_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/recycle-policy",
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

    def show_backup_policy_async(self, request):
        """查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowBackupPolicyResponse`
        """
        http_info = self._show_backup_policy_http_info(request)
        return self._call_api(**http_info)

    def show_backup_policy_async_invoker(self, request):
        http_info = self._show_backup_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_backup_policy_http_info(self, request):
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

    def show_balance_status_async(self, request):
        """查询实例主备平衡状态

        查询实例是否发生过主备切换而导致主机负载不均衡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBalanceStatus
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowBalanceStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowBalanceStatusResponse`
        """
        http_info = self._show_balance_status_http_info(request)
        return self._call_api(**http_info)

    def show_balance_status_async_invoker(self, request):
        http_info = self._show_balance_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_balance_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/balance",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBalanceStatusResponse"
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

    def show_batch_upgrade_candidate_versions_async(self, request):
        """查询批量实例可升级的版本和升级类型

        查询批量实例可升级的版本和升级类型
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBatchUpgradeCandidateVersions
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowBatchUpgradeCandidateVersionsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowBatchUpgradeCandidateVersionsResponse`
        """
        http_info = self._show_batch_upgrade_candidate_versions_http_info(request)
        return self._call_api(**http_info)

    def show_batch_upgrade_candidate_versions_async_invoker(self, request):
        http_info = self._show_batch_upgrade_candidate_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_batch_upgrade_candidate_versions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/db-upgrade/candidate-versions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchUpgradeCandidateVersionsResponse"
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

    def show_configuration_detail_async(self, request):
        """查询参数模板详情

        根据参数模板ID获取指定参数模板详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigurationDetail
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowConfigurationDetailRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowConfigurationDetailResponse`
        """
        http_info = self._show_configuration_detail_http_info(request)
        return self._call_api(**http_info)

    def show_configuration_detail_async_invoker(self, request):
        http_info = self._show_configuration_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_configuration_detail_http_info(self, request):
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

    def show_deployment_form_async(self, request):
        """查询解决方案模板配置

        根据解决方案模板名称或实例ID查询副本数、分片数、节点数
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDeploymentForm
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowDeploymentFormRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowDeploymentFormResponse`
        """
        http_info = self._show_deployment_form_http_info(request)
        return self._call_api(**http_info)

    def show_deployment_form_async_invoker(self, request):
        http_info = self._show_deployment_form_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_deployment_form_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/deployment-form",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeploymentFormResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'solution' in local_var_params:
            query_params.append(('solution', local_var_params['solution']))
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

    def show_error_log_switch_status_async(self, request):
        """查询错误日志采集开关状态

        查询数据库错误日志采集的开关状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowErrorLogSwitchStatus
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowErrorLogSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowErrorLogSwitchStatusResponse`
        """
        http_info = self._show_error_log_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_error_log_switch_status_async_invoker(self, request):
        http_info = self._show_error_log_switch_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_error_log_switch_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/error-log/switch/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowErrorLogSwitchStatusResponse"
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

    def show_instance_configuration_async(self, request):
        """获取指定实例的参数模板

        获取指定实例的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceConfiguration
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceConfigurationResponse`
        """
        http_info = self._show_instance_configuration_http_info(request)
        return self._call_api(**http_info)

    def show_instance_configuration_async_invoker(self, request):
        http_info = self._show_instance_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_configuration_http_info(self, request):
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

    def show_instance_disk_async(self, request):
        """查询实例存储空间使用信息

        查询指定实例的存储使用空间和最大空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceDisk
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceDiskRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceDiskResponse`
        """
        http_info = self._show_instance_disk_http_info(request)
        return self._call_api(**http_info)

    def show_instance_disk_async_invoker(self, request):
        http_info = self._show_instance_disk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_disk_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/volume-usage",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceDiskResponse"
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

    def show_instance_param_group_async(self, request):
        """获取指定实例的参数模板

        获取指定实例的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceParamGroup
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceParamGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceParamGroupResponse`
        """
        http_info = self._show_instance_param_group_http_info(request)
        return self._call_api(**http_info)

    def show_instance_param_group_async_invoker(self, request):
        http_info = self._show_instance_param_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_param_group_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceParamGroupResponse"
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

    def show_instance_snapshot_async(self, request):
        """根据时间点或者备份文件查询原实例信息

        根据时间点或者备份文件查询原实例信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceSnapshot
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceSnapshotRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowInstanceSnapshotResponse`
        """
        http_info = self._show_instance_snapshot_http_info(request)
        return self._call_api(**http_info)

    def show_instance_snapshot_async_invoker(self, request):
        http_info = self._show_instance_snapshot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_snapshot_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instance-snapshot",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceSnapshotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))
        if 'restore_time' in local_var_params:
            query_params.append(('restore_time', local_var_params['restore_time']))
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

    def show_job_detail_async(self, request):
        """获取指定ID的任务信息。

        获取指定ID的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_async_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_detail_http_info(self, request):
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

    def show_project_quotas_async(self, request):
        """查询租户的实例配额

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProjectQuotas
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowProjectQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowProjectQuotasResponse`
        """
        http_info = self._show_project_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_project_quotas_async_invoker(self, request):
        http_info = self._show_project_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_project_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/project-quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectQuotasResponse"
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

    def show_recycle_policy_async(self, request):
        """查看回收站策略

        查看回收站的回收策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowRecyclePolicyResponse`
        """
        http_info = self._show_recycle_policy_http_info(request)
        return self._call_api(**http_info)

    def show_recycle_policy_async_invoker(self, request):
        http_info = self._show_recycle_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_recycle_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/recycle-policy",
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

    def show_slow_log_download_async(self, request):
        """查询慢日志下载信息

        查询慢日志下载信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSlowLogDownload
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowSlowLogDownloadRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowSlowLogDownloadResponse`
        """
        http_info = self._show_slow_log_download_http_info(request)
        return self._call_api(**http_info)

    def show_slow_log_download_async_invoker(self, request):
        http_info = self._show_slow_log_download_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_slow_log_download_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-log/download",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSlowLogDownloadResponse"
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

    def show_ssl_cert_download_link_async(self, request):
        """查询实例SSL证书下载地址

        查询实例SSL证书下载地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSslCertDownloadLink
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowSslCertDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowSslCertDownloadLinkResponse`
        """
        http_info = self._show_ssl_cert_download_link_http_info(request)
        return self._call_api(**http_info)

    def show_ssl_cert_download_link_async_invoker(self, request):
        http_info = self._show_ssl_cert_download_link_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_ssl_cert_download_link_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/ssl-cert/download-link",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSslCertDownloadLinkResponse"
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

    def show_upgrade_candidate_versions_async(self, request):
        """查询实例可升级版本

        查询实例可升级版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUpgradeCandidateVersions
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowUpgradeCandidateVersionsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ShowUpgradeCandidateVersionsResponse`
        """
        http_info = self._show_upgrade_candidate_versions_http_info(request)
        return self._call_api(**http_info)

    def show_upgrade_candidate_versions_async_invoker(self, request):
        http_info = self._show_upgrade_candidate_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_upgrade_candidate_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-upgrade/candidate-versions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpgradeCandidateVersionsResponse"
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

    def start_instance_async(self, request):
        """启动数据库

        启动数据库，同时支持节点级别的启动操作
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInstance
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.StartInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.StartInstanceResponse`
        """
        http_info = self._start_instance_http_info(request)
        return self._call_api(**http_info)

    def start_instance_async_invoker(self, request):
        http_info = self._start_instance_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_instance_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-startup",
            "request_type": request.__class__.__name__,
            "response_type": "StartInstanceResponse"
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

    def stop_backup_async(self, request):
        """停止备份

        停止进行中的备份，包括全备和差备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopBackup
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.StopBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.StopBackupResponse`
        """
        http_info = self._stop_backup_http_info(request)
        return self._call_api(**http_info)

    def stop_backup_async_invoker(self, request):
        http_info = self._stop_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_backup_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/backups/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopBackupResponse"
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

    def switch_configuration_async(self, request):
        """应用参数模板

        指定实例变更参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchConfiguration
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SwitchConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SwitchConfigurationResponse`
        """
        http_info = self._switch_configuration_http_info(request)
        return self._call_api(**http_info)

    def switch_configuration_async_invoker(self, request):
        http_info = self._switch_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_configuration_http_info(self, request):
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

    def switch_shard_async(self, request):
        """分片节点主备切换。

        支持用户对单个或多个DN分片做主备切换，同一分组内只能指定一个新的备节点进行升主操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchShard
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.SwitchShardRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.SwitchShardResponse`
        """
        http_info = self._switch_shard_http_info(request)
        return self._call_api(**http_info)

    def switch_shard_async_invoker(self, request):
        http_info = self._switch_shard_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_shard_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/switch-shard",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchShardResponse"
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

    def update_instance_configuration_async(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConfiguration
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpdateInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpdateInstanceConfigurationResponse`
        """
        http_info = self._update_instance_configuration_http_info(request)
        return self._call_api(**http_info)

    def update_instance_configuration_async_invoker(self, request):
        http_info = self._update_instance_configuration_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_configuration_http_info(self, request):
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

    def update_instance_name_async(self, request):
        """修改实例名称

        修改实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpdateInstanceNameResponse`
        """
        http_info = self._update_instance_name_http_info(request)
        return self._call_api(**http_info)

    def update_instance_name_async_invoker(self, request):
        http_info = self._update_instance_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_instance_name_http_info(self, request):
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

    def upgrade_instance_version_async(self, request):
        """实例内核版本升级

        GaussDB(for openGauss)实例版本升级。包括灰度升级，就地升级，热补丁升级等三种升级方式。 
        就地升级：
        就地升级需要停止业务进行，会一次性升级集群中所有节点。就地升级需要暂停业务30分钟来升级。 
        灰度升级： 
        升级自动提交：所有节点进程一起升级，在升级过程中有大概10秒的业务中断，不阻塞其他业务操作。 
        升级待观察：升级待观察，将数据库升级过程细分为升级，提交两个阶段。升级阶段可以根据部署方式细分为按分片或者按az的滚动升级，提交阶段可以对升级完成后的实例进行业务测试，根据需要可以选择提交升级，或者升级回退。每个主dn或者cn组件升级就有一次10秒业务中断。升级过程均是先管理面，再数据面，由备到主的升级方式。 分布式实例：根据分片数滚动升级，每次滚动升级可以根据选择的分片数进行指定分片数量的节点进行升级。 主备版实例：根据AZ数进行滚动升级，每次滚动升级可以根据选择的AZ进行1个分区或者多个分区进行升级。 
        提交升级：提交升级。在升级完成，进入提交阶段时。业务测试正常后提交升级，完成本次升级流程。
        升级回退：升级回退，在升级完成，进入提交阶段时。可以根据需要回退本次升级，回退到升级前的版本。
        热补丁升级： 
        升级自动提交：热补丁自动升级并提交，中间无业务中断，仅修复产品bug。 
        升级回退：热补丁回退，无业务中断时间
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeInstanceVersion
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeInstanceVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeInstanceVersionResponse`
        """
        http_info = self._upgrade_instance_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_instance_version_async_invoker(self, request):
        http_info = self._upgrade_instance_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_instance_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3.1/{project_id}/instances/{instance_id}/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeInstanceVersionResponse"
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

    def upgrade_instances_version_async(self, request):
        """批量实例内核版本升级

        GaussDB批量实例版本升级。包括灰度升级，就地升级、热补丁升级三种升级方式。 
        就地升级：
        就地升级需要停止业务进行，会一次性升级集群中所有节点。就地升级需要暂停业务30分钟来升级。 
        灰度升级： 
        升级自动提交：所有节点进程一起升级，在升级过程中有大概10秒的业务中断，不阻塞其他业务操作。 
        升级待观察：升级待观察，将数据库升级过程细分为升级，提交两个阶段。升级阶段可以根据部署方式细分为按分片或者按az的滚动升级，提交阶段可以对升级完成后的实例进行业务测试，根据需要可以选择提交升级，或者升级回退。每个主dn或者cn组件升级就有一次10秒业务中断。升级过程均是先管理面，再数据面，由备到主的升级方式。 分布式实例：根据分片数滚动升级，每次滚动升级可以根据选择的分片数进行指定分片数量的节点进行升级。 主备版实例：根据AZ数进行滚动升级，每次滚动升级可以根据选择的AZ进行1个分区或者多个分区进行升级。 
        热补丁升级： 
        升级自动提交：热补丁自动升级并提交，中间无业务中断，仅修复产品bug。 
        提交升级：提交升级。在升级完成，进入提交阶段时。业务测试正常后提交升级，完成本次升级流程。
        升级回退：升级回退，在升级完成，进入提交阶段时。可以根据需要回退本次升级，回退到升级前的版本。
        批量实例可升级版本大于当前所有实例的引擎版本，且选择的所有实例，其升级方式和操作方式要保持一致。
        若批量实例升级方式是灰度升级，默认升级所有az和分片。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeInstancesVersion
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeInstancesVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeInstancesVersionResponse`
        """
        http_info = self._upgrade_instances_version_http_info(request)
        return self._call_api(**http_info)

    def upgrade_instances_version_async_invoker(self, request):
        http_info = self._upgrade_instances_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_instances_version_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/db-upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeInstancesVersionResponse"
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

    def validate_para_group_name_async(self, request):
        """校验参数组名称是否存在

        校验参数组名称是否存在。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateParaGroupName
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ValidateParaGroupNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ValidateParaGroupNameResponse`
        """
        http_info = self._validate_para_group_name_http_info(request)
        return self._call_api(**http_info)

    def validate_para_group_name_async_invoker(self, request):
        http_info = self._validate_para_group_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_para_group_name_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/configurations/name-validation",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateParaGroupNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
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

    def validate_weak_password_async(self, request):
        """弱密码校验

        校验数据库root用户密码的安全性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateWeakPassword
        :type request: :class:`huaweicloudsdkgaussdbforopengauss.v3.ValidateWeakPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.ValidateWeakPasswordResponse`
        """
        http_info = self._validate_weak_password_http_info(request)
        return self._call_api(**http_info)

    def validate_weak_password_async_invoker(self, request):
        http_info = self._validate_weak_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_weak_password_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/weak-password-verification",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateWeakPasswordResponse"
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

    def _call_api(self, **kwargs):
        try:
            kwargs["async_request"] = True
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

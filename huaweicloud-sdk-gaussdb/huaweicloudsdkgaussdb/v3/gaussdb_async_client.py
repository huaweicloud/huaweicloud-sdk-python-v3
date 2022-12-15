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


class GaussDBAsyncClient(Client):
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
        super(GaussDBAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgaussdb.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GaussDBClient":
            raise TypeError("client type error, support client type is GaussDBClient")

        return ClientBuilder(clazz)

    def add_database_permission_async(self, request):
        """授予数据库用户数据库权限

        授予云数据库 GaussDB(for MySQL)实例数据库用户数据库权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddDatabasePermission
        :type request: :class:`huaweicloudsdkgaussdb.v3.AddDatabasePermissionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.AddDatabasePermissionResponse`
        """
        return self.add_database_permission_with_http_info(request)

    def add_database_permission_with_http_info(self, request):
        all_params = ['instance_id', 'grant_database_permission_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/privilege',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddDatabasePermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_tag_action_async(self, request):
        """批量添加或删除标签

        批量添加或删除指定实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkgaussdb.v3.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.BatchTagActionResponse`
        """
        return self.batch_tag_action_with_http_info(request)

    def batch_tag_action_with_http_info(self, request):
        all_params = ['instance_id', 'batch_operate_instance_tag_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchTagActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_gauss_my_sql_instance_eip_async(self, request):
        """解绑弹性公网IP

        实例解绑弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelGaussMySqlInstanceEip
        :type request: :class:`huaweicloudsdkgaussdb.v3.CancelGaussMySqlInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CancelGaussMySqlInstanceEipResponse`
        """
        return self.cancel_gauss_my_sql_instance_eip_with_http_info(request)

    def cancel_gauss_my_sql_instance_eip_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/public-ips/unbind',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelGaussMySqlInstanceEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_schedule_task_async(self, request):
        """取消定时任务

        取消定时任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelScheduleTask
        :type request: :class:`huaweicloudsdkgaussdb.v3.CancelScheduleTaskRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CancelScheduleTaskResponse`
        """
        return self.cancel_schedule_task_with_http_info(request)

    def cancel_schedule_task_with_http_info(self, request):
        all_params = ['cancel_schedule_task', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/scheduled-jobs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelScheduleTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_gauss_my_sql_instance_specification_async(self, request):
        """变更实例规格

        变更数据库实例的规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeGaussMySqlInstanceSpecification
        :type request: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlInstanceSpecificationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlInstanceSpecificationResponse`
        """
        return self.change_gauss_my_sql_instance_specification_with_http_info(request)

    def change_gauss_my_sql_instance_specification_with_http_info(self, request):
        all_params = ['instance_id', 'mysql_change_specification_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeGaussMySqlInstanceSpecificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_gauss_my_sql_proxy_specification_async(self, request):
        """数据库代理规格变更

        数据库代理规格变更。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeGaussMySqlProxySpecification
        :type request: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlProxySpecificationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ChangeGaussMySqlProxySpecificationResponse`
        """
        return self.change_gauss_my_sql_proxy_specification_with_http_info(request)

    def change_gauss_my_sql_proxy_specification_with_http_info(self, request):
        all_params = ['instance_id', 'proxy_id', 'taurus_proxy_scale_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/flavor',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeGaussMySqlProxySpecificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_backup_async(self, request):
        """创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlBackup
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlBackupResponse`
        """
        return self.create_gauss_my_sql_backup_with_http_info(request)

    def create_gauss_my_sql_backup_with_http_info(self, request):
        all_params = ['mysql_create_backup_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/backups/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_configuration_async(self, request):
        """创建参数模板

        创建参数模板信息，包含参数模板名称、描述、数据库版本信息、参数值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlConfigurationResponse`
        """
        return self.create_gauss_my_sql_configuration_with_http_info(request)

    def create_gauss_my_sql_configuration_with_http_info(self, request):
        all_params = ['create_configuration_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/configurations',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_database_async(self, request):
        """创建数据库

        创建云数据库 GaussDB(for MySQL)实例数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseResponse`
        """
        return self.create_gauss_my_sql_database_with_http_info(request)

    def create_gauss_my_sql_database_with_http_info(self, request):
        all_params = ['instance_id', 'create_gauss_my_sql_database_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/databases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_database_user_async(self, request):
        """创建数据库用户

        创建云数据库GaussDB(for MySQL)实例数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlDatabaseUserResponse`
        """
        return self.create_gauss_my_sql_database_user_with_http_info(request)

    def create_gauss_my_sql_database_user_with_http_info(self, request):
        all_params = ['instance_id', 'create_database_user_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlDatabaseUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_instance_async(self, request):
        """创建数据库实例

        创建云数据库GaussDB(for MySQL)实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlInstanceResponse`
        """
        return self.create_gauss_my_sql_instance_with_http_info(request)

    def create_gauss_my_sql_instance_with_http_info(self, request):
        all_params = ['create_instance_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_proxy_async(self, request):
        """开启数据库代理

        开启数据库代理，只支持ELB模式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlProxyResponse`
        """
        return self.create_gauss_my_sql_proxy_with_http_info(request)

    def create_gauss_my_sql_proxy_with_http_info(self, request):
        all_params = ['instance_id', 'x_language', 'create_mysql_proxy_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_gauss_my_sql_readonly_node_async(self, request):
        """创建只读节点

        创建只读节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGaussMySqlReadonlyNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlReadonlyNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CreateGaussMySqlReadonlyNodeResponse`
        """
        return self.create_gauss_my_sql_readonly_node_with_http_info(request)

    def create_gauss_my_sql_readonly_node_with_http_info(self, request):
        all_params = ['instance_id', 'mysql_create_readonly_node_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/nodes/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGaussMySqlReadonlyNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database_permission_async(self, request):
        """删除数据库用户的数据库权限

        删除云数据库 GaussDB(for MySQL)实例数据库用户的数据库权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatabasePermission
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteDatabasePermissionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteDatabasePermissionResponse`
        """
        return self.delete_database_permission_with_http_info(request)

    def delete_database_permission_with_http_info(self, request):
        all_params = ['instance_id', 'grant_database_permission_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/privilege',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDatabasePermissionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_backup_async(self, request):
        """删除手动备份

        删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlBackup
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlBackupResponse`
        """
        return self.delete_gauss_my_sql_backup_with_http_info(request)

    def delete_gauss_my_sql_backup_with_http_info(self, request):
        all_params = ['backup_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_configuration_async(self, request):
        """删除参数模板

        删除指定参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlConfigurationResponse`
        """
        return self.delete_gauss_my_sql_configuration_with_http_info(request)

    def delete_gauss_my_sql_configuration_with_http_info(self, request):
        all_params = ['configuration_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{configuration_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_database_async(self, request):
        """删除数据库

        删除云数据库 GaussDB(for MySQL)实例数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseResponse`
        """
        return self.delete_gauss_my_sql_database_with_http_info(request)

    def delete_gauss_my_sql_database_with_http_info(self, request):
        all_params = ['instance_id', 'delete_gauss_my_sql_database_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/databases',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_database_user_async(self, request):
        """删除数据库用户

        删除云数据库 GaussDB(for MySQL)实例数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlDatabaseUserResponse`
        """
        return self.delete_gauss_my_sql_database_user_with_http_info(request)

    def delete_gauss_my_sql_database_user_with_http_info(self, request):
        all_params = ['instance_id', 'delete_database_user_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlDatabaseUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_instance_async(self, request):
        """删除实例

        删除数据库实例，不支持删除包周期实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlInstanceResponse`
        """
        return self.delete_gauss_my_sql_instance_with_http_info(request)

    def delete_gauss_my_sql_instance_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_proxy_async(self, request):
        """关闭数据库代理

        关闭数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlProxyResponse`
        """
        return self.delete_gauss_my_sql_proxy_with_http_info(request)

    def delete_gauss_my_sql_proxy_with_http_info(self, request):
        all_params = ['instance_id', 'x_language', 'close_mysql_proxy_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_gauss_my_sql_readonly_node_async(self, request):
        """删除只读节点

        删除实例的只读节点。多可用区模式删除只读节点时，要保证删除后，剩余的只读节点和主节点在不同的可用区中，否则无法删除该只读节点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGaussMySqlReadonlyNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlReadonlyNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteGaussMySqlReadonlyNodeResponse`
        """
        return self.delete_gauss_my_sql_readonly_node_with_http_info(request)

    def delete_gauss_my_sql_readonly_node_with_http_info(self, request):
        all_params = ['instance_id', 'node_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/nodes/{node_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteGaussMySqlReadonlyNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_task_record_async(self, request):
        """删除指定任务记录

        删除指定任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTaskRecord
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteTaskRecordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteTaskRecordResponse`
        """
        return self.delete_task_record_with_http_info(request)

    def delete_task_record_with_http_info(self, request):
        all_params = ['job_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTaskRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_gauss_my_sql_instance_volume_async(self, request):
        """包周期存储扩容

        包周期存储扩容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandGaussMySqlInstanceVolume
        :type request: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlInstanceVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlInstanceVolumeResponse`
        """
        return self.expand_gauss_my_sql_instance_volume_with_http_info(request)

    def expand_gauss_my_sql_instance_volume_with_http_info(self, request):
        all_params = ['instance_id', 'mysql_extend_instance_volume_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/volume/extend',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandGaussMySqlInstanceVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_gauss_my_sql_proxy_async(self, request):
        """扩容数据库代理节点的数量

        扩容数据库代理节点的数量。
        DeC专属云账号暂不支持数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandGaussMySqlProxy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlProxyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ExpandGaussMySqlProxyResponse`
        """
        return self.expand_gauss_my_sql_proxy_with_http_info(request)

    def expand_gauss_my_sql_proxy_with_http_info(self, request):
        all_params = ['instance_id', 'enlarge_proxy_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/enlarge',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandGaussMySqlProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def invoke_gauss_my_sql_instance_switch_over_async(self, request):
        """手动主备倒换

        用户手动进行主备倒换。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for InvokeGaussMySqlInstanceSwitchOver
        :type request: :class:`huaweicloudsdkgaussdb.v3.InvokeGaussMySqlInstanceSwitchOverRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.InvokeGaussMySqlInstanceSwitchOverResponse`
        """
        return self.invoke_gauss_my_sql_instance_switch_over_with_http_info(request)

    def invoke_gauss_my_sql_instance_switch_over_with_http_info(self, request):
        all_params = ['instance_id', 'taurus_switchover_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/switchover',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InvokeGaussMySqlInstanceSwitchOverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_configurations_async(self, request):
        """查询参数模板

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlConfigurations
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlConfigurationsResponse`
        """
        return self.list_gauss_my_sql_configurations_with_http_info(request)

    def list_gauss_my_sql_configurations_with_http_info(self, request):
        all_params = ['x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlConfigurationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_database_async(self, request):
        """查询数据库列表

        查询 GaussDB(for MySQL)实例数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseResponse`
        """
        return self.list_gauss_my_sql_database_with_http_info(request)

    def list_gauss_my_sql_database_with_http_info(self, request):
        all_params = ['instance_id', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/databases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_database_charsets_async(self, request):
        """查询数据库可用字符集

        查询云数据库 GaussDB(for MySQL)实例数据库可用字符集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlDatabaseCharsets
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseCharsetsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseCharsetsResponse`
        """
        return self.list_gauss_my_sql_database_charsets_with_http_info(request)

    def list_gauss_my_sql_database_charsets_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/databases/charsets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlDatabaseCharsetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_database_user_async(self, request):
        """查询数据库用户

        查询云数据库 GaussDB(for MySQL)实例数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlDatabaseUser
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseUserRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDatabaseUserResponse`
        """
        return self.list_gauss_my_sql_database_user_with_http_info(request)

    def list_gauss_my_sql_database_user_with_http_info(self, request):
        all_params = ['instance_id', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlDatabaseUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_dedicated_resources_async(self, request):
        """查询专属资源池列表

        获取专属资源池列表，包括用户开通的所有专属资源池信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlDedicatedResources
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDedicatedResourcesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlDedicatedResourcesResponse`
        """
        return self.list_gauss_my_sql_dedicated_resources_with_http_info(request)

    def list_gauss_my_sql_dedicated_resources_with_http_info(self, request):
        all_params = ['x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/dedicated-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlDedicatedResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_error_log_async(self, request):
        """查询数据库错误日志

        查询数据库错误日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlErrorLog
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlErrorLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlErrorLogResponse`
        """
        return self.list_gauss_my_sql_error_log_with_http_info(request)

    def list_gauss_my_sql_error_log_with_http_info(self, request):
        all_params = ['instance_id', 'start_date', 'end_date', 'node_id', 'x_language', 'offset', 'limit', 'level']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/errorlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlErrorLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_instance_detail_info_async(self, request):
        """批量查询实例详情

        批量查询实例详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlInstanceDetailInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstanceDetailInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstanceDetailInfoResponse`
        """
        return self.list_gauss_my_sql_instance_detail_info_with_http_info(request)

    def list_gauss_my_sql_instance_detail_info_with_http_info(self, request):
        all_params = ['instance_ids', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/details',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlInstanceDetailInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_instances_async(self, request):
        """查询实例列表

        根据指定条件查询实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlInstances
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlInstancesResponse`
        """
        return self.list_gauss_my_sql_instances_with_http_info(request)

    def list_gauss_my_sql_instances_with_http_info(self, request):
        all_params = ['x_language', 'id', 'name', 'type', 'datastore_type', 'vpc_id', 'subnet_id', 'private_ip', 'offset', 'limit', 'tags']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_gauss_my_sql_slow_log_async(self, request):
        """查询数据库慢日志

        查询数据库慢日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGaussMySqlSlowLog
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlSlowLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListGaussMySqlSlowLogResponse`
        """
        return self.list_gauss_my_sql_slow_log_with_http_info(request)

    def list_gauss_my_sql_slow_log_with_http_info(self, request):
        all_params = ['instance_id', 'start_date', 'end_date', 'node_id', 'x_language', 'offset', 'limit', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGaussMySqlSlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_immediate_jobs_async(self, request):
        """获取即时任务列表

        获取即时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListImmediateJobs
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListImmediateJobsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListImmediateJobsResponse`
        """
        return self.list_immediate_jobs_with_http_info(request)

    def list_immediate_jobs_with_http_info(self, request):
        all_params = ['x_language', 'status', 'job_name', 'job_id', 'offset', 'limit', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/immediate-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImmediateJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListInstanceTagsResponse`
        """
        return self.list_instance_tags_with_http_info(request)

    def list_instance_tags_with_http_info(self, request):
        all_params = ['instance_id', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_tags_async(self, request):
        """查询项目标签

        查询指定project ID下实例的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListProjectTagsResponse`
        """
        return self.list_project_tags_with_http_info(request)

    def list_project_tags_with_http_info(self, request):
        all_params = ['x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_schedule_jobs_async(self, request):
        """获取定时任务列表

        获取定时任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScheduleJobs
        :type request: :class:`huaweicloudsdkgaussdb.v3.ListScheduleJobsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ListScheduleJobsResponse`
        """
        return self.list_schedule_jobs_with_http_info(request)

    def list_schedule_jobs_with_http_info(self, request):
        all_params = ['x_language', 'offset', 'limit', 'status', 'start_time', 'end_time', 'job_id', 'job_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/scheduled-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListScheduleJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_gauss_my_sql_database_password_async(self, request):
        """修改数据库用户密码

        修改云数据库 GaussDB(for MySQL)实例数据库用户密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetGaussMySqlDatabasePassword
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlDatabasePasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlDatabasePasswordResponse`
        """
        return self.reset_gauss_my_sql_database_password_with_http_info(request)

    def reset_gauss_my_sql_database_password_with_http_info(self, request):
        all_params = ['instance_id', 'reset_database_password_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetGaussMySqlDatabasePasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_gauss_my_sql_password_async(self, request):
        """重置数据库密码

        重置数据库密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetGaussMySqlPassword
        :type request: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ResetGaussMySqlPasswordResponse`
        """
        return self.reset_gauss_my_sql_password_with_http_info(request)

    def reset_gauss_my_sql_password_with_http_info(self, request):
        all_params = ['instance_id', 'mysql_reset_password_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetGaussMySqlPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_gauss_my_sql_instance_async(self, request):
        """重启数据库实例

        重启数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartGaussMySqlInstance
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlInstanceResponse`
        """
        return self.restart_gauss_my_sql_instance_with_http_info(request)

    def restart_gauss_my_sql_instance_with_http_info(self, request):
        all_params = ['instance_id', 'taurus_restart_instance_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartGaussMySqlInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_gauss_my_sql_node_async(self, request):
        """节点重启

        节点重启。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartGaussMySqlNode
        :type request: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RestartGaussMySqlNodeResponse`
        """
        return self.restart_gauss_my_sql_node_with_http_info(request)

    def restart_gauss_my_sql_node_with_http_info(self, request):
        all_params = ['instance_id', 'node_id', 'x_language', 'restart_node_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestartGaussMySqlNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_gauss_my_sql_proxy_weight_async(self, request):
        """设置读写分离权重

        设置读写分离权重。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetGaussMySqlProxyWeight
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlProxyWeightRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlProxyWeightResponse`
        """
        return self.set_gauss_my_sql_proxy_weight_with_http_info(request)

    def set_gauss_my_sql_proxy_weight_with_http_info(self, request):
        all_params = ['instance_id', 'proxy_id', 'taurus_modify_proxy_weight_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/weight',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetGaussMySqlProxyWeightResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_gauss_my_sql_quotas_async(self, request):
        """设置租户基于企业项目的资源配额

        设置指定企业项目的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetGaussMySqlQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetGaussMySqlQuotasResponse`
        """
        return self.set_gauss_my_sql_quotas_with_http_info(request)

    def set_gauss_my_sql_quotas_with_http_info(self, request):
        all_params = ['x_language', 'set_quotas_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/quotas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetGaussMySqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_audit_log_async(self, request):
        """查询全量SQL开关状态

        查询全量SQL开关状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuditLog
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowAuditLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowAuditLogResponse`
        """
        return self.show_audit_log_with_http_info(request)

    def show_audit_log_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instance/{instance_id}/audit-log/switch-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAuditLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dedicated_resource_info_async(self, request):
        """查询专属资源信息详情

        查询专属资源信息详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDedicatedResourceInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowDedicatedResourceInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowDedicatedResourceInfoResponse`
        """
        return self.show_dedicated_resource_info_with_http_info(request)

    def show_dedicated_resource_info_with_http_info(self, request):
        all_params = ['dedicated_resource_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/dedicated-resource/{dedicated_resource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDedicatedResourceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_backup_list_async(self, request):
        """查询备份列表

        查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlBackupList
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupListRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupListResponse`
        """
        return self.show_gauss_my_sql_backup_list_with_http_info(request)

    def show_gauss_my_sql_backup_list_with_http_info(self, request):
        all_params = ['x_language', 'instance_id', 'backup_id', 'backup_type', 'offset', 'limit', 'begin_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlBackupListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_backup_policy_async(self, request):
        """查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlBackupPolicyResponse`
        """
        return self.show_gauss_my_sql_backup_policy_with_http_info(request)

    def show_gauss_my_sql_backup_policy_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_configuration_async(self, request):
        """获取参数模板详情

        获取指定参数模板的参数信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlConfigurationResponse`
        """
        return self.show_gauss_my_sql_configuration_with_http_info(request)

    def show_gauss_my_sql_configuration_with_http_info(self, request):
        all_params = ['configuration_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{configuration_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_engine_version_async(self, request):
        """查询数据库引擎的版本

        获取指定数据库引擎对应的数据库版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlEngineVersion
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlEngineVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlEngineVersionResponse`
        """
        return self.show_gauss_my_sql_engine_version_with_http_info(request)

    def show_gauss_my_sql_engine_version_with_http_info(self, request):
        all_params = ['database_name', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/datastores/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlEngineVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_flavors_async(self, request):
        """查询数据库规格

        获取指定数据库引擎版本对应的规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlFlavors
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlFlavorsResponse`
        """
        return self.show_gauss_my_sql_flavors_with_http_info(request)

    def show_gauss_my_sql_flavors_with_http_info(self, request):
        all_params = ['database_name', 'availability_zone_mode', 'x_language', 'version_name', 'spec_code']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/flavors/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_instance_info_async(self, request):
        """查询实例详情信息

        查询实例详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlInstanceInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlInstanceInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlInstanceInfoResponse`
        """
        return self.show_gauss_my_sql_instance_info_with_http_info(request)

    def show_gauss_my_sql_instance_info_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlInstanceInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_job_info_async(self, request):
        """获取指定ID的任务信息

        获取GaussDB(for MySQL)任务中心指定ID的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlJobInfo
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlJobInfoRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlJobInfoResponse`
        """
        return self.show_gauss_my_sql_job_info_with_http_info(request)

    def show_gauss_my_sql_job_info_with_http_info(self, request):
        all_params = ['id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlJobInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_project_quotas_async(self, request):
        """查询租户的实例配额

        获取指定租户的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlProjectQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProjectQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProjectQuotasResponse`
        """
        return self.show_gauss_my_sql_project_quotas_with_http_info(request)

    def show_gauss_my_sql_project_quotas_with_http_info(self, request):
        all_params = ['x_language', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/project-quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlProjectQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_proxy_flavors_async(self, request):
        """查询数据库代理规格信息

        查询数据库代理规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlProxyFlavors
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyFlavorsResponse`
        """
        return self.show_gauss_my_sql_proxy_flavors_with_http_info(request)

    def show_gauss_my_sql_proxy_flavors_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlProxyFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_proxy_list_async(self, request):
        """查询数据库代理信息列表

        查询数据库代理信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlProxyList
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyListRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlProxyListResponse`
        """
        return self.show_gauss_my_sql_proxy_list_with_http_info(request)

    def show_gauss_my_sql_proxy_list_with_http_info(self, request):
        all_params = ['instance_id', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlProxyListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_gauss_my_sql_quotas_async(self, request):
        """查询租户基于企业项目的资源配额

        获取指定企业项目的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGaussMySqlQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowGaussMySqlQuotasResponse`
        """
        return self.show_gauss_my_sql_quotas_with_http_info(request)

    def show_gauss_my_sql_quotas_with_http_info(self, request):
        all_params = ['x_language', 'offset', 'limit', 'enterprise_project_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGaussMySqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_monitor_extend_async(self, request):
        """查询实例秒级监控频率

        查询实例秒级监控频率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceMonitorExtend
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceMonitorExtendRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowInstanceMonitorExtendResponse`
        """
        return self.show_instance_monitor_extend_with_http_info(request)

    def show_instance_monitor_extend_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/monitor-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceMonitorExtendResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_gauss_my_sql_configuration_async(self, request):
        """应用参数模板

        指定实例变更参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlConfigurationResponse`
        """
        return self.switch_gauss_my_sql_configuration_with_http_info(request)

    def switch_gauss_my_sql_configuration_with_http_info(self, request):
        all_params = ['configuration_id', 'apply_configuration_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/configurations/{configuration_id}/apply',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchGaussMySqlConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_gauss_my_sql_instance_ssl_async(self, request):
        """开关SSL

        为实例设置SSL数据加密。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchGaussMySqlInstanceSsl
        :type request: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlInstanceSslRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SwitchGaussMySqlInstanceSslResponse`
        """
        return self.switch_gauss_my_sql_instance_ssl_with_http_info(request)

    def switch_gauss_my_sql_instance_ssl_with_http_info(self, request):
        all_params = ['instance_id', 'switch_ssl_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/ssl-option',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchGaussMySqlInstanceSslResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_audit_log_async(self, request):
        """开启或者关闭全量SQL

        开启或者关闭全量SQL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAuditLog
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateAuditLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateAuditLogResponse`
        """
        return self.update_audit_log_with_http_info(request)

    def update_audit_log_with_http_info(self, request):
        all_params = ['instance_id', 'operate_audit_log_request_v3_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instance/{instance_id}/audit-log/switch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAuditLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_backup_policy_async(self, request):
        """设置备份策略

        设置自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlBackupPolicyResponse`
        """
        return self.update_gauss_my_sql_backup_policy_with_http_info(request)

    def update_gauss_my_sql_backup_policy_with_http_info(self, request):
        all_params = ['instance_id', 'mysql_update_backup_policy_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy/update',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_configuration_async(self, request):
        """修改参数模板

        修改指定参数模板的参数信息，包括名称、描述、指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlConfiguration
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlConfigurationResponse`
        """
        return self.update_gauss_my_sql_configuration_with_http_info(request)

    def update_gauss_my_sql_configuration_with_http_info(self, request):
        all_params = ['configuration_id', 'update_configuration_parameter_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/configurations/{configuration_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_alias_async(self, request):
        """修改实例备注

        修改实例备注。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstanceAlias
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceAliasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceAliasResponse`
        """
        return self.update_gauss_my_sql_instance_alias_with_http_info(request)

    def update_gauss_my_sql_instance_alias_with_http_info(self, request):
        all_params = ['instance_id', 'modify_alias_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/alias',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstanceAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_eip_async(self, request):
        """绑定弹性公网IP

        实例绑定弹性公网IP，供外网连接使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstanceEip
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceEipRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceEipResponse`
        """
        return self.update_gauss_my_sql_instance_eip_with_http_info(request)

    def update_gauss_my_sql_instance_eip_with_http_info(self, request):
        all_params = ['instance_id', 'modify_bind_eip_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/public-ips/bind',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstanceEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_internal_ip_async(self, request):
        """修改内网地址

        修改实例内网地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstanceInternalIp
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceInternalIpRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceInternalIpResponse`
        """
        return self.update_gauss_my_sql_instance_internal_ip_with_http_info(request)

    def update_gauss_my_sql_instance_internal_ip_with_http_info(self, request):
        all_params = ['instance_id', 'modify_internal_ip_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/internal-ip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstanceInternalIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_name_async(self, request):
        """修改实例名称

        修改实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstanceName
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceNameResponse`
        """
        return self.update_gauss_my_sql_instance_name_with_http_info(request)

    def update_gauss_my_sql_instance_name_with_http_info(self, request):
        all_params = ['instance_id', 'mysql_update_instance_name_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstanceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_ops_window_async(self, request):
        """设置可维护时间段

        设置可维护时间段。建议将可维护时间段设置在业务低峰期，避免业务在维护过程中异常中断。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstanceOpsWindow
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceOpsWindowRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceOpsWindowResponse`
        """
        return self.update_gauss_my_sql_instance_ops_window_with_http_info(request)

    def update_gauss_my_sql_instance_ops_window_with_http_info(self, request):
        all_params = ['instance_id', 'modify_ops_window', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/ops-window',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstanceOpsWindowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_port_async(self, request):
        """修改实例端口

        修改实例数据库端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstancePort
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstancePortRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstancePortResponse`
        """
        return self.update_gauss_my_sql_instance_port_with_http_info(request)

    def update_gauss_my_sql_instance_port_with_http_info(self, request):
        all_params = ['instance_id', 'modify_port_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/port',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstancePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_instance_security_group_async(self, request):
        """修改安全组

        修改指定实例安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlInstanceSecurityGroup
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlInstanceSecurityGroupResponse`
        """
        return self.update_gauss_my_sql_instance_security_group_with_http_info(request)

    def update_gauss_my_sql_instance_security_group_with_http_info(self, request):
        all_params = ['instance_id', 'modify_security_group', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/security-group',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlInstanceSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_gauss_my_sql_quotas_async(self, request):
        """修改租户基于企业项目的资源配额

        修改指定企业项目的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateGaussMySqlQuotas
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateGaussMySqlQuotasResponse`
        """
        return self.update_gauss_my_sql_quotas_with_http_info(request)

    def update_gauss_my_sql_quotas_with_http_info(self, request):
        all_params = ['x_language', 'set_quotas_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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
            resource_path='/v3/{project_id}/quotas',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateGaussMySqlQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_monitor_async(self, request):
        """修改实例秒级监控频率

        打开/关闭/修改实例秒级监控。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceMonitor
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateInstanceMonitorRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateInstanceMonitorResponse`
        """
        return self.update_instance_monitor_with_http_info(request)

    def update_instance_monitor_with_http_info(self, request):
        all_params = ['instance_id', 'taurus_modify_instance_monitor_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/monitor-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_proxy_session_consistence_async(self, request):
        """修改代理会话一致性

        修改代理会话一致性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProxySessionConsistence
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateProxySessionConsistenceRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateProxySessionConsistenceResponse`
        """
        return self.update_proxy_session_consistence_with_http_info(request)

    def update_proxy_session_consistence_with_http_info(self, request):
        all_params = ['instance_id', 'proxy_id', 'modify_proxy_consist_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/{proxy_id}/session-consistence',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProxySessionConsistenceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_transaction_split_status_async(self, request):
        """设置proxy事务拆分

        设置proxy事务拆分。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTransactionSplitStatus
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateTransactionSplitStatusRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateTransactionSplitStatusResponse`
        """
        return self.update_transaction_split_status_with_http_info(request)

    def update_transaction_split_status_with_http_info(self, request):
        all_params = ['instance_id', 'proxy_transaction_split_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/transaction-split',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTransactionSplitStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_gauss_my_sql_instance_database_async(self, request):
        """内核版本升级

        内核版本升级。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeGaussMySqlInstanceDatabase
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpgradeGaussMySqlInstanceDatabaseRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpgradeGaussMySqlInstanceDatabaseResponse`
        """
        return self.upgrade_gauss_my_sql_instance_database_with_http_info(request)

    def upgrade_gauss_my_sql_instance_database_with_http_info(self, request):
        all_params = ['instance_id', 'upgrade_database_request', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-upgrade',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpgradeGaussMySqlInstanceDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sql_filter_rule_async(self, request):
        """删除SQL限流规则

        删除SQL限流规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSqlFilterRule
        :type request: :class:`huaweicloudsdkgaussdb.v3.DeleteSqlFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.DeleteSqlFilterRuleResponse`
        """
        return self.delete_sql_filter_rule_with_http_info(request)

    def delete_sql_filter_rule_with_http_info(self, request):
        all_params = ['instance_id', 'delete_sql_filter_rule_req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/sql-filter/rules',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSqlFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_sql_filter_rule_async(self, request):
        """设置SQL限流规则

        设置SQL限流规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetSqlFilterRule
        :type request: :class:`huaweicloudsdkgaussdb.v3.SetSqlFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.SetSqlFilterRuleResponse`
        """
        return self.set_sql_filter_rule_with_http_info(request)

    def set_sql_filter_rule_with_http_info(self, request):
        all_params = ['instance_id', 'operate_sql_filter_rule_req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/sql-filter/rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetSqlFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_filter_control_async(self, request):
        """查询SQL限流开关状态

        查询SQL限流开关状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSqlFilterControl
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterControlRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterControlResponse`
        """
        return self.show_sql_filter_control_with_http_info(request)

    def show_sql_filter_control_with_http_info(self, request):
        all_params = ['instance_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/sql-filter/switch',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlFilterControlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_filter_rule_async(self, request):
        """查询SQL限流规则

        查询SQL限流规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSqlFilterRule
        :type request: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterRuleRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ShowSqlFilterRuleResponse`
        """
        return self.show_sql_filter_rule_with_http_info(request)

    def show_sql_filter_rule_with_http_info(self, request):
        all_params = ['instance_id', 'node_id', 'x_language', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/sql-filter/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSqlFilterRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_sql_filter_control_async(self, request):
        """开启或者关闭SQL限流

        开启或者关闭SQL限流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSqlFilterControl
        :type request: :class:`huaweicloudsdkgaussdb.v3.UpdateSqlFilterControlRequest`
        :rtype: :class:`huaweicloudsdkgaussdb.v3.UpdateSqlFilterControlResponse`
        """
        return self.update_sql_filter_control_with_http_info(request)

    def update_sql_filter_control_with_http_info(self, request):
        all_params = ['instance_id', 'operate_sql_filter_control_req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/sql-filter/switch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateSqlFilterControlResponse',
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

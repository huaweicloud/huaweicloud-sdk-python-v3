# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class RdsAsyncClient(Client):
    def __init__(self):
        super(RdsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkrds.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "RdsClient":
            raise TypeError("client type error, support client type is RdsClient")

        return ClientBuilder(clazz)

    def add_postgresql_hba_conf_async(self, request):
        """在pg_hba.conf文件最后新增单个或多个配置

        以传入配置全量覆盖当前pg_hba.conf文件内容，入参为空时用默认配置覆盖当前文件内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddPostgresqlHbaConf
        :type request: :class:`huaweicloudsdkrds.v3.AddPostgresqlHbaConfRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AddPostgresqlHbaConfResponse`
        """
        return self._add_postgresql_hba_conf_with_http_info(request)

    def _add_postgresql_hba_conf_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/hba-info',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddPostgresqlHbaConfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def apply_configuration_async_async(self, request):
        """应用参数模板

        应用参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyConfigurationAsync
        :type request: :class:`huaweicloudsdkrds.v3.ApplyConfigurationAsyncRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ApplyConfigurationAsyncResponse`
        """
        return self._apply_configuration_async_with_http_info(request)

    def _apply_configuration_async_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/configurations/{config_id}/apply',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyConfigurationAsyncResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_eip_async(self, request):
        """绑定和解绑弹性公网IP

        绑定和解绑弹性公网IP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachEip
        :type request: :class:`huaweicloudsdkrds.v3.AttachEipRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AttachEipResponse`
        """
        return self._attach_eip_with_http_info(request)

    def _attach_eip_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/public-ip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachEipResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_manual_backup_async(self, request):
        """批量删除手动备份

        批量删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteManualBackup
        :type request: :class:`huaweicloudsdkrds.v3.BatchDeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchDeleteManualBackupResponse`
        """
        return self._batch_delete_manual_backup_with_http_info(request)

    def _batch_delete_manual_backup_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteManualBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_tag_add_action_async(self, request):
        """批量添加标签

        批量添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchTagAddAction
        :type request: :class:`huaweicloudsdkrds.v3.BatchTagAddActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchTagAddActionResponse`
        """
        return self._batch_tag_add_action_with_http_info(request)

    def _batch_tag_add_action_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='BatchTagAddActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_tag_del_action_async(self, request):
        """批量删除标签

        批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchTagDelAction
        :type request: :class:`huaweicloudsdkrds.v3.BatchTagDelActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchTagDelActionResponse`
        """
        return self._batch_tag_del_action_with_http_info(request)

    def _batch_tag_del_action_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='BatchTagDelActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_failover_mode_async(self, request):
        """更改主备实例的数据同步方式

        更改主备实例的数据同步方式。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeFailoverMode
        :type request: :class:`huaweicloudsdkrds.v3.ChangeFailoverModeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeFailoverModeResponse`
        """
        return self._change_failover_mode_with_http_info(request)

    def _change_failover_mode_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/failover/mode',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeFailoverModeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_failover_strategy_async(self, request):
        """切换主备实例的倒换策略

        切换主备实例的倒换策略.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeFailoverStrategy
        :type request: :class:`huaweicloudsdkrds.v3.ChangeFailoverStrategyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeFailoverStrategyResponse`
        """
        return self._change_failover_strategy_with_http_info(request)

    def _change_failover_strategy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/failover/strategy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeFailoverStrategyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_ops_window_async(self, request):
        """设置可维护时间段

        设置可维护时间段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeOpsWindow
        :type request: :class:`huaweicloudsdkrds.v3.ChangeOpsWindowRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeOpsWindowResponse`
        """
        return self._change_ops_window_with_http_info(request)

    def _change_ops_window_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='ChangeOpsWindowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_configuration_async(self, request):
        """复制参数模板

        复制参数模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.CopyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CopyConfigurationResponse`
        """
        return self._copy_configuration_with_http_info(request)

    def _copy_configuration_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}/copy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_configuration_async(self, request):
        """创建参数模板

        创建参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.CreateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateConfigurationResponse`
        """
        return self._create_configuration_with_http_info(request)

    def _create_configuration_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

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
            response_type='CreateConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_dns_name_async(self, request):
        """申请域名

        申请域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDnsName
        :type request: :class:`huaweicloudsdkrds.v3.CreateDnsNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateDnsNameResponse`
        """
        return self._create_dns_name_with_http_info(request)

    def _create_dns_name_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/create-dns',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDnsNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_async(self, request):
        """创建数据库实例

        创建数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkrds.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateInstanceResponse`
        """
        return self._create_instance_with_http_info(request)

    def _create_instance_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_manual_backup_async(self, request):
        """创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateManualBackup
        :type request: :class:`huaweicloudsdkrds.v3.CreateManualBackupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateManualBackupResponse`
        """
        return self._create_manual_backup_with_http_info(request)

    def _create_manual_backup_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateManualBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_restore_instance_async(self, request):
        """恢复到新实例

        恢复到新实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRestoreInstance
        :type request: :class:`huaweicloudsdkrds.v3.CreateRestoreInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateRestoreInstanceResponse`
        """
        return self._create_restore_instance_with_http_info(request)

    def _create_restore_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

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
            response_type='CreateRestoreInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_xel_log_download_async(self, request):
        """获取扩展日志下载信息

        获取扩展日志下载信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateXelLogDownload
        :type request: :class:`huaweicloudsdkrds.v3.CreateXelLogDownloadRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateXelLogDownloadResponse`
        """
        return self._create_xel_log_download_with_http_info(request)

    def _create_xel_log_download_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/xellog-download',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateXelLogDownloadResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_configuration_async(self, request):
        """删除参数模板

        删除参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteConfigurationResponse`
        """
        return self._delete_configuration_with_http_info(request)

    def _delete_configuration_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance_async(self, request):
        """删除数据库实例

        删除数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkrds.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteInstanceResponse`
        """
        return self._delete_instance_with_http_info(request)

    def _delete_instance_with_http_info(self, request):
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
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_job_async(self, request):
        """删除即时任务

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkrds.v3.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteJobResponse`
        """
        return self._delete_job_with_http_info(request)

    def _delete_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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
            resource_path='/v3/{project_id}/jobs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_manual_backup_async(self, request):
        """删除手动备份

        删除手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteManualBackup
        :type request: :class:`huaweicloudsdkrds.v3.DeleteManualBackupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteManualBackupResponse`
        """
        return self._delete_manual_backup_with_http_info(request)

    def _delete_manual_backup_with_http_info(self, request):
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
            response_type='DeleteManualBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_postgresql_hba_conf_async(self, request):
        """删除pg_hba.conf文件的单个或多个配置

        删除pg_hba.conf文件的单个或多个配置，以priority做唯一标识
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePostgresqlHbaConf
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlHbaConfRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlHbaConfResponse`
        """
        return self._delete_postgresql_hba_conf_with_http_info(request)

    def _delete_postgresql_hba_conf_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/hba-info',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePostgresqlHbaConfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_slowlog_async(self, request):
        """获取慢日志下载链接

        获取慢日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadSlowlog
        :type request: :class:`huaweicloudsdkrds.v3.DownloadSlowlogRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DownloadSlowlogResponse`
        """
        return self._download_slowlog_with_http_info(request)

    def _download_slowlog_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog-download',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadSlowlogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def enable_configuration_async(self, request):
        """应用参数模板

        应用参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for EnableConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.EnableConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.EnableConfigurationResponse`
        """
        return self._enable_configuration_with_http_info(request)

    def _enable_configuration_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}/apply',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='EnableConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auditlogs_async(self, request):
        """获取审计日志列表

        获取审计日志列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditlogs
        :type request: :class:`huaweicloudsdkrds.v3.ListAuditlogsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuditlogsResponse`
        """
        return self._list_auditlogs_with_http_info(request)

    def _list_auditlogs_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/auditlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditlogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backups_async(self, request):
        """获取备份列表

        获取备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkrds.v3.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListBackupsResponse`
        """
        return self._list_backups_with_http_info(request)

    def _list_backups_with_http_info(self, request):
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
            response_type='ListBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_collations_async(self, request):
        """查询SQLServer可用字符集

        查询SQLServer可用字符集
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCollations
        :type request: :class:`huaweicloudsdkrds.v3.ListCollationsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListCollationsResponse`
        """
        return self._list_collations_with_http_info(request)

    def _list_collations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/collations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCollationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configurations_async(self, request):
        """获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkrds.v3.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListConfigurationsResponse`
        """
        return self._list_configurations_with_http_info(request)

    def _list_configurations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/configurations',
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

    def list_datastores_async(self, request):
        """查询数据库引擎的版本

        查询数据库引擎的版本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatastores
        :type request: :class:`huaweicloudsdkrds.v3.ListDatastoresRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDatastoresResponse`
        """
        return self._list_datastores_with_http_info(request)

    def _list_datastores_with_http_info(self, request):
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
            response_type='ListDatastoresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_dr_relations_async(self, request):
        """list_dr_relations

        批量查询容灾实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDrRelations
        :type request: :class:`huaweicloudsdkrds.v3.ListDrRelationsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDrRelationsResponse`
        """
        return self._list_dr_relations_with_http_info(request)

    def _list_dr_relations_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/instances/disaster-recovery-relation',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDrRelationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_engine_flavors_async(self, request):
        """查询实例可变更规格

        查询实例可变更规格
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEngineFlavors
        :type request: :class:`huaweicloudsdkrds.v3.ListEngineFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListEngineFlavorsResponse`
        """
        return self._list_engine_flavors_with_http_info(request)

    def _list_engine_flavors_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/available-flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEngineFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_error_logs_async(self, request):
        """查询数据库错误日志

        查询数据库错误日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListErrorLogs
        :type request: :class:`huaweicloudsdkrds.v3.ListErrorLogsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListErrorLogsResponse`
        """
        return self._list_error_logs_with_http_info(request)

    def _list_error_logs_with_http_info(self, request):
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
            response_type='ListErrorLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_error_logs_new_async(self, request):
        """查询数据库错误日志

        查询数据库错误日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListErrorLogsNew
        :type request: :class:`huaweicloudsdkrds.v3.ListErrorLogsNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListErrorLogsNewResponse`
        """
        return self._list_error_logs_new_with_http_info(request)

    def _list_error_logs_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/errorlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListErrorLogsNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_errorlog_for_lts_async(self, request):
        """list_errorlog_for_lts

        查询实例的错误日志数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListErrorlogForLts
        :type request: :class:`huaweicloudsdkrds.v3.ListErrorlogForLtsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListErrorlogForLtsResponse`
        """
        return self._list_errorlog_for_lts_with_http_info(request)

    def _list_errorlog_for_lts_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/error-logs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListErrorlogForLtsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询数据库规格

        查询数据库规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkrds.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListFlavorsResponse`
        """
        return self._list_flavors_with_http_info(request)

    def _list_flavors_with_http_info(self, request):
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
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_param_histories_async(self, request):
        """查询实例参数修改历史

        实例参数修改历史。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceParamHistories
        :type request: :class:`huaweicloudsdkrds.v3.ListInstanceParamHistoriesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstanceParamHistoriesResponse`
        """
        return self._list_instance_param_histories_with_http_info(request)

    def _list_instance_param_histories_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/configuration-histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceParamHistoriesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance_tags_async(self, request):
        """查询实例标签

        查询实例标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkrds.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstanceTagsResponse`
        """
        return self._list_instance_tags_with_http_info(request)

    def _list_instance_tags_with_http_info(self, request):
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

    def list_instances_async(self, request):
        """查询数据库实例列表

        查询数据库实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesResponse`
        """
        return self._list_instances_with_http_info(request)

    def _list_instances_with_http_info(self, request):
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
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_recommendation_async(self, request):
        """查询购买推荐

        查询购买推荐
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesRecommendation
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesRecommendationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesRecommendationResponse`
        """
        return self._list_instances_recommendation_with_http_info(request)

    def _list_instances_recommendation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))

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
            resource_path='/v3/{project_id}/instances/product-recommendation',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesRecommendationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_resource_metrics_async(self, request):
        """查询监控大盘列表

        查询监控大盘列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesResourceMetrics
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesResourceMetricsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesResourceMetricsResponse`
        """
        return self._list_instances_resource_metrics_with_http_info(request)

    def _list_instances_resource_metrics_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine' in local_var_params:
            query_params.append(('engine', local_var_params['engine']))
        if 'search_field' in local_var_params:
            query_params.append(('search_field', local_var_params['search_field']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))

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
            resource_path='/v3/{project_id}/instances/resource-monitoring',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesResourceMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_support_fast_restore_async(self, request):
        """获取实例是否能使用极速恢复

        批量获取实例是否能在库表恢复时使用极速恢复。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesSupportFastRestore
        :type request: :class:`huaweicloudsdkrds.v3.ListInstancesSupportFastRestoreRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListInstancesSupportFastRestoreResponse`
        """
        return self._list_instances_support_fast_restore_with_http_info(request)

    def _list_instances_support_fast_restore_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/fast-restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesSupportFastRestoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job_info_async(self, request):
        """获取指定ID的任务信息

        获取指定ID的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobInfo
        :type request: :class:`huaweicloudsdkrds.v3.ListJobInfoRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListJobInfoResponse`
        """
        return self._list_job_info_with_http_info(request)

    def _list_job_info_with_http_info(self, request):
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
            response_type='ListJobInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job_info_detail_async(self, request):
        """获取指定实例和时间范围的任务信息（SQL Server）

        获取指定实例和时间范围的任务信息（SQL Server）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobInfoDetail
        :type request: :class:`huaweicloudsdkrds.v3.ListJobInfoDetailRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListJobInfoDetailResponse`
        """
        return self._list_job_info_detail_with_http_info(request)

    def _list_job_info_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/tasklist/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobInfoDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_off_site_backups_async(self, request):
        """查询跨区域备份列表

        查询跨区域备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOffSiteBackups
        :type request: :class:`huaweicloudsdkrds.v3.ListOffSiteBackupsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListOffSiteBackupsResponse`
        """
        return self._list_off_site_backups_with_http_info(request)

    def _list_off_site_backups_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/offsite-backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOffSiteBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_off_site_instances_async(self, request):
        """查询跨区域备份实例列表

        查询跨区域备份实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOffSiteInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListOffSiteInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListOffSiteInstancesResponse`
        """
        return self._list_off_site_instances_with_http_info(request)

    def _list_off_site_instances_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/backups/offsite-backup-instance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOffSiteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_off_site_restore_times_async(self, request):
        """查询跨区域备份可恢复时间段

        查询跨区域备份可恢复时间段。
        如果您备份策略中的保存天数设置较长，建议您传入查询日期“date”。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOffSiteRestoreTimes
        :type request: :class:`huaweicloudsdkrds.v3.ListOffSiteRestoreTimesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListOffSiteRestoreTimesResponse`
        """
        return self._list_off_site_restore_times_with_http_info(request)

    def _list_off_site_restore_times_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/offsite-restore-time',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListOffSiteRestoreTimesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_postgresql_hba_info_async(self, request):
        """查询实例的pg_hba.conf文件配置

        查询实例的pg_hba.conf文件配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPostgresqlHbaInfo
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoResponse`
        """
        return self._list_postgresql_hba_info_with_http_info(request)

    def _list_postgresql_hba_info_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/instances/{instance_id}/hba-info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPostgresqlHbaInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_postgresql_hba_info_history_async(self, request):
        """查询实例的pg_hba.conf文件修改历史

        查询实例的pg_hba.conf文件修改历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPostgresqlHbaInfoHistory
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoHistoryRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlHbaInfoHistoryResponse`
        """
        return self._list_postgresql_hba_info_history_with_http_info(request)

    def _list_postgresql_hba_info_history_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/hba-info/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPostgresqlHbaInfoHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_predefined_tag_async(self, request):
        """list_predefined_tag

        查询预定义标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPredefinedTag
        :type request: :class:`huaweicloudsdkrds.v3.ListPredefinedTagRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPredefinedTagResponse`
        """
        return self._list_predefined_tag_with_http_info(request)

    def _list_predefined_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/tags/predefined-tag',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPredefinedTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_tags_async(self, request):
        """查询项目标签

        查询项目标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkrds.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListProjectTagsResponse`
        """
        return self._list_project_tags_with_http_info(request)

    def _list_project_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_recycle_instances_async(self, request):
        """查询回收站

        查询回收站实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListRecycleInstancesResponse`
        """
        return self._list_recycle_instances_with_http_info(request)

    def _list_recycle_instances_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/recycle-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRecycleInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_restore_times_async(self, request):
        """查询可恢复时间段

        查询可恢复时间段。
        如果您备份策略中的保存天数设置较长，建议您传入查询日期“date”。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRestoreTimes
        :type request: :class:`huaweicloudsdkrds.v3.ListRestoreTimesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListRestoreTimesResponse`
        """
        return self._list_restore_times_with_http_info(request)

    def _list_restore_times_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/restore-time',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRestoreTimesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_simplified_instances_async(self, request):
        """list_simplified_instances

        获取指定实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSimplifiedInstances
        :type request: :class:`huaweicloudsdkrds.v3.ListSimplifiedInstancesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSimplifiedInstancesResponse`
        """
        return self._list_simplified_instances_with_http_info(request)

    def _list_simplified_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/simplified-instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSimplifiedInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slow_log_file_async(self, request):
        """查询慢日志文件列表

        查询慢日志文件列表。
        调用该接口取到慢日志文件名后，可以调用接口/v3/{project_id}/instances/{instance_id}/slowlog-download 获取慢日志文件下载链接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowLogFile
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogFileRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogFileResponse`
        """
        return self._list_slow_log_file_with_http_info(request)

    def _list_slow_log_file_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSlowLogFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slow_log_statistics_for_lts_async(self, request):
        """list_slow_log_statistics_for_lts

        查询实例慢日志的统计数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowLogStatisticsForLts
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogStatisticsForLtsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogStatisticsForLtsResponse`
        """
        return self._list_slow_log_statistics_for_lts_with_http_info(request)

    def _list_slow_log_statistics_for_lts_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/slow-logs/statistics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSlowLogStatisticsForLtsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slow_logs_async(self, request):
        """查询数据库慢日志

        查询数据库慢日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowLogs
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogsResponse`
        """
        return self._list_slow_logs_with_http_info(request)

    def _list_slow_logs_with_http_info(self, request):
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
            response_type='ListSlowLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slow_logs_new_async(self, request):
        """查询数据库慢日志

        查询数据库慢日志。(与原v3接口相比修改offset,符合华为云服务开放 API遵从性规范3.0)
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowLogsNew
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowLogsNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowLogsNewResponse`
        """
        return self._list_slow_logs_new_with_http_info(request)

    def _list_slow_logs_new_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/slowlog',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSlowLogsNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slowlog_for_lts_async(self, request):
        """list_slowlog_for_lts

        查询实例的慢日志数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowlogForLts
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowlogForLtsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowlogForLtsResponse`
        """
        return self._list_slowlog_for_lts_with_http_info(request)

    def _list_slowlog_for_lts_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slow-logs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSlowlogForLtsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slowlog_statistics_async(self, request):
        """获取慢日志统计信息

        获取慢日志统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowlogStatistics
        :type request: :class:`huaweicloudsdkrds.v3.ListSlowlogStatisticsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSlowlogStatisticsResponse`
        """
        return self._list_slowlog_statistics_with_http_info(request)

    def _list_slowlog_statistics_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSlowlogStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ssl_cert_download_link_async(self, request):
        """获取SSL证书下载地址

        获取SSL证书下载地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSslCertDownloadLink
        :type request: :class:`huaweicloudsdkrds.v3.ListSslCertDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSslCertDownloadLinkResponse`
        """
        return self._list_ssl_cert_download_link_with_http_info(request)

    def _list_ssl_cert_download_link_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/ssl-cert/download-link',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSslCertDownloadLinkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_storage_types_async(self, request):
        """查询数据库磁盘类型

        查询数据库磁盘类型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStorageTypes
        :type request: :class:`huaweicloudsdkrds.v3.ListStorageTypesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListStorageTypesResponse`
        """
        return self._list_storage_types_with_http_info(request)

    def _list_storage_types_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/storage-type/{database_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStorageTypesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_xellog_files_async(self, request):
        """查询扩展日志文件列表

        查询扩展日志文件列表。
        查询扩展日志文件列表，可以调用接口/v3/{project_id}/instances/{instance_id}/xellog-download 获取扩展日志下载链接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListXellogFiles
        :type request: :class:`huaweicloudsdkrds.v3.ListXellogFilesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListXellogFilesResponse`
        """
        return self._list_xellog_files_with_http_info(request)

    def _list_xellog_files_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/xellog-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListXellogFilesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def migrate_follower_async(self, request):
        """迁移主备实例的备机

        迁移主备实例的备机
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for MigrateFollower
        :type request: :class:`huaweicloudsdkrds.v3.MigrateFollowerRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.MigrateFollowerResponse`
        """
        return self._migrate_follower_with_http_info(request)

    def _migrate_follower_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/migrateslave',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='MigrateFollowerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def modify_postgresql_hba_conf_async(self, request):
        """修改pg_hba.conf文件的单个或多个配置

        修改/新增pg_hba.conf文件的单个或多个配置，以priority做唯一标识，priority不存在的新增，存在的修改
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyPostgresqlHbaConf
        :type request: :class:`huaweicloudsdkrds.v3.ModifyPostgresqlHbaConfRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ModifyPostgresqlHbaConfResponse`
        """
        return self._modify_postgresql_hba_conf_with_http_info(request)

    def _modify_postgresql_hba_conf_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/hba-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ModifyPostgresqlHbaConfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_exist_instance_async(self, request):
        """恢复到已有实例

        恢复到已有实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreExistInstance
        :type request: :class:`huaweicloudsdkrds.v3.RestoreExistInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreExistInstanceResponse`
        """
        return self._restore_exist_instance_with_http_info(request)

    def _restore_exist_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/recovery',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreExistInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_tables_async(self, request):
        """表级时间点恢复(MySQL)

        表级时间点恢复(MySQL)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreTables
        :type request: :class:`huaweicloudsdkrds.v3.RestoreTablesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreTablesResponse`
        """
        return self._restore_tables_with_http_info(request)

    def _restore_tables_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/restore/tables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_tables_new_async(self, request):
        """表级时间点恢复(MySQL)

        表级时间点恢复(MySQL)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreTablesNew
        :type request: :class:`huaweicloudsdkrds.v3.RestoreTablesNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreTablesNewResponse`
        """
        return self._restore_tables_new_with_http_info(request)

    def _restore_tables_new_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/restore/tables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreTablesNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_to_existing_instance_async(self, request):
        """恢复到已有实例

        恢复到已有实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreToExistingInstance
        :type request: :class:`huaweicloudsdkrds.v3.RestoreToExistingInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RestoreToExistingInstanceResponse`
        """
        return self._restore_to_existing_instance_with_http_info(request)

    def _restore_to_existing_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/recovery',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreToExistingInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_auditlog_policy_async(self, request):
        """设置审计日志策略

        设置审计日志策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetAuditlogPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetAuditlogPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetAuditlogPolicyResponse`
        """
        return self._set_auditlog_policy_with_http_info(request)

    def _set_auditlog_policy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/auditlog-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetAuditlogPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_auto_enlarge_policy_async(self, request):
        """设置自动扩容策略

        设置实例存储空间自动扩容策略，按扩容量扣除存储费用。
        可用存储空间小于设置值或者10GB时，自动扩容当前存储空间的15%（非10倍数向上取整，账户余额不足，会导致自动扩容失败）。
        设置只读实例自动扩容与主实例自动扩容互不影响，对只读实例设置自动扩容时，可选择大于或等于主实例的存储空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetAutoEnlargePolicyResponse`
        """
        return self._set_auto_enlarge_policy_with_http_info(request)

    def _set_auto_enlarge_policy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/disk-auto-expansion',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetAutoEnlargePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_backup_policy_async(self, request):
        """设置自动备份策略

        设置自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetBackupPolicyResponse`
        """
        return self._set_backup_policy_with_http_info(request)

    def _set_backup_policy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_binlog_clear_policy_async(self, request):
        """设置binlog本地保留时长

        修改指定实例的binlog本地保留时长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetBinlogClearPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetBinlogClearPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetBinlogClearPolicyResponse`
        """
        return self._set_binlog_clear_policy_with_http_info(request)

    def _set_binlog_clear_policy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/binlog/clear-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetBinlogClearPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_off_site_backup_policy_async(self, request):
        """设置跨区域备份策略

        设置跨区域备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetOffSiteBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.SetOffSiteBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetOffSiteBackupPolicyResponse`
        """
        return self._set_off_site_backup_policy_with_http_info(request)

    def _set_off_site_backup_policy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/offsite-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetOffSiteBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_second_level_monitor_async(self, request):
        """设置秒级监控策略

        设置实例秒级监控策略，约五分钟后生效，对于1秒监控和5秒监控，计费方式为按需付费（每小时扣费一次）。
        设置只读实例秒级监控与主实例互不影响。
        规格变更到4U以下的实例，秒级监控功能会自动关闭。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetSecondLevelMonitor
        :type request: :class:`huaweicloudsdkrds.v3.SetSecondLevelMonitorRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetSecondLevelMonitorResponse`
        """
        return self._set_second_level_monitor_with_http_info(request)

    def _set_second_level_monitor_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/second-level-monitor',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetSecondLevelMonitorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_security_group_async(self, request):
        """修改安全组

        修改安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetSecurityGroup
        :type request: :class:`huaweicloudsdkrds.v3.SetSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetSecurityGroupResponse`
        """
        return self._set_security_group_with_http_info(request)

    def _set_security_group_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='SetSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_sensitive_slow_log_async(self, request):
        """慢日志敏感信息的开关

        V3慢日志敏感信息的开关
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetSensitiveSlowLog
        :type request: :class:`huaweicloudsdkrds.v3.SetSensitiveSlowLogRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetSensitiveSlowLogResponse`
        """
        return self._set_sensitive_slow_log_with_http_info(request)

    def _set_sensitive_slow_log_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog-sensitization/{status}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetSensitiveSlowLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auditlog_download_link_async(self, request):
        """生成审计日志下载链接

        生成审计日志下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuditlogDownloadLink
        :type request: :class:`huaweicloudsdkrds.v3.ShowAuditlogDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAuditlogDownloadLinkResponse`
        """
        return self._show_auditlog_download_link_with_http_info(request)

    def _show_auditlog_download_link_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/auditlog-links',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAuditlogDownloadLinkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auditlog_policy_async(self, request):
        """查询审计日志策略

        查询审计日志策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuditlogPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowAuditlogPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAuditlogPolicyResponse`
        """
        return self._show_auditlog_policy_with_http_info(request)

    def _show_auditlog_policy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/auditlog-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAuditlogPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auto_enlarge_policy_async(self, request):
        """查询自动扩容策略

        查询实例存储空间自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowAutoEnlargePolicyResponse`
        """
        return self._show_auto_enlarge_policy_with_http_info(request)

    def _show_auto_enlarge_policy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/disk-auto-expansion',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAutoEnlargePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_backup_download_link_async(self, request):
        """获取备份下载链接

        获取备份下载链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackupDownloadLink
        :type request: :class:`huaweicloudsdkrds.v3.ShowBackupDownloadLinkRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowBackupDownloadLinkResponse`
        """
        return self._show_backup_download_link_with_http_info(request)

    def _show_backup_download_link_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/backup-files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBackupDownloadLinkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_backup_policy_async(self, request):
        """查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowBackupPolicyResponse`
        """
        return self._show_backup_policy_with_http_info(request)

    def _show_backup_policy_with_http_info(self, request):
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
            response_type='ShowBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_binlog_clear_policy_async(self, request):
        """获取binlog本地保留时长

        查寻指定实例的binlog本地保留时长。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBinlogClearPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowBinlogClearPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowBinlogClearPolicyResponse`
        """
        return self._show_binlog_clear_policy_with_http_info(request)

    def _show_binlog_clear_policy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/binlog/clear-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBinlogClearPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_configuration_async(self, request):
        """获取指定参数模板的参数

        获取指定参数模板的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.ShowConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowConfigurationResponse`
        """
        return self._show_configuration_with_http_info(request)

    def _show_configuration_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dns_name_async(self, request):
        """查询实例ipv6域名。

        查询实例ipv6域名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDnsName
        :type request: :class:`huaweicloudsdkrds.v3.ShowDnsNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowDnsNameResponse`
        """
        return self._show_dns_name_with_http_info(request)

    def _show_dns_name_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/dns-ipv6',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDnsNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_domain_name_async(self, request):
        """show_domain_name

        查询实例ipv4域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDomainName
        :type request: :class:`huaweicloudsdkrds.v3.ShowDomainNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowDomainNameResponse`
        """
        return self._show_domain_name_with_http_info(request)

    def _show_domain_name_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/dns',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDomainNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dr_replica_status_async(self, request):
        """查询跨云容灾复制状态

        建立跨云容灾关系后，查询主实例和灾备实例间的复制状态及延迟。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDrReplicaStatus
        :type request: :class:`huaweicloudsdkrds.v3.ShowDrReplicaStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowDrReplicaStatusResponse`
        """
        return self._show_dr_replica_status_with_http_info(request)

    def _show_dr_replica_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/disaster-recovery',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDrReplicaStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_configuration_async(self, request):
        """获取指定实例的参数模板

        获取指定实例的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.ShowInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowInstanceConfigurationResponse`
        """
        return self._show_instance_configuration_with_http_info(request)

    def _show_instance_configuration_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_off_site_backup_policy_async(self, request):
        """查询跨区域备份策略

        查询跨区域备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOffSiteBackupPolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowOffSiteBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowOffSiteBackupPolicyResponse`
        """
        return self._show_off_site_backup_policy_with_http_info(request)

    def _show_off_site_backup_policy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/offsite-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOffSiteBackupPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_async(self, request):
        """查询配额

        查询当前项目下资源配额情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkrds.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowQuotasResponse`
        """
        return self._show_quotas_with_http_info(request)

    def _show_quotas_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_recycle_policy_async(self, request):
        """查询回收站的回收策略。

        查询回收站的回收策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkrds.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowRecyclePolicyResponse`
        """
        return self._show_recycle_policy_with_http_info(request)

    def _show_recycle_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/instances/recycle-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRecyclePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_replication_status_async(self, request):
        """获取实例的复制状态。

        获取实例的复制状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReplicationStatus
        :type request: :class:`huaweicloudsdkrds.v3.ShowReplicationStatusRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowReplicationStatusResponse`
        """
        return self._show_replication_status_with_http_info(request)

    def _show_replication_status_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/replication/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowReplicationStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_second_level_monitoring_async(self, request):
        """查询秒级监控策略

        查询实例秒级监控策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecondLevelMonitoring
        :type request: :class:`huaweicloudsdkrds.v3.ShowSecondLevelMonitoringRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowSecondLevelMonitoringResponse`
        """
        return self._show_second_level_monitoring_with_http_info(request)

    def _show_second_level_monitoring_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/second-level-monitor',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecondLevelMonitoringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_failover_async(self, request):
        """手动倒换主备

        手动倒换主备.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartFailover
        :type request: :class:`huaweicloudsdkrds.v3.StartFailoverRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartFailoverResponse`
        """
        return self._start_failover_with_http_info(request)

    def _start_failover_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/failover',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartFailoverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_instance_enlarge_volume_action_async(self, request):
        """扩容数据库实例的磁盘空间

        扩容数据库实例的磁盘空间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInstanceEnlargeVolumeAction
        :type request: :class:`huaweicloudsdkrds.v3.StartInstanceEnlargeVolumeActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartInstanceEnlargeVolumeActionResponse`
        """
        return self._start_instance_enlarge_volume_action_with_http_info(request)

    def _start_instance_enlarge_volume_action_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='StartInstanceEnlargeVolumeActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_instance_restart_action_async(self, request):
        """重启数据库实例

        重启数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInstanceRestartAction
        :type request: :class:`huaweicloudsdkrds.v3.StartInstanceRestartActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartInstanceRestartActionResponse`
        """
        return self._start_instance_restart_action_with_http_info(request)

    def _start_instance_restart_action_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='StartInstanceRestartActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_instance_single_to_ha_action_async(self, request):
        """单机转主备实例

        单机转主备实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartInstanceSingleToHaAction
        :type request: :class:`huaweicloudsdkrds.v3.StartInstanceSingleToHaActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartInstanceSingleToHaActionResponse`
        """
        return self._start_instance_single_to_ha_action_with_http_info(request)

    def _start_instance_single_to_ha_action_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='StartInstanceSingleToHaActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_recycle_policy_async(self, request):
        """设置回收站策略

        设置回收站策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartRecyclePolicy
        :type request: :class:`huaweicloudsdkrds.v3.StartRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartRecyclePolicyResponse`
        """
        return self._start_recycle_policy_with_http_info(request)

    def _start_recycle_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/recycle-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartRecyclePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_resize_flavor_action_async(self, request):
        """变更数据库实例的规格

        变更数据库实例的规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartResizeFlavorAction
        :type request: :class:`huaweicloudsdkrds.v3.StartResizeFlavorActionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartResizeFlavorActionResponse`
        """
        return self._start_resize_flavor_action_with_http_info(request)

    def _start_resize_flavor_action_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='StartResizeFlavorActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def startup_instance_async(self, request):
        """开启实例

        停止实例以节省费用，在停止数据库实例后，支持手动重新开启实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartupInstance
        :type request: :class:`huaweicloudsdkrds.v3.StartupInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartupInstanceResponse`
        """
        return self._startup_instance_with_http_info(request)

    def _startup_instance_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/action/startup',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartupInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_instance_async(self, request):
        """停止实例

        实例进行关机，通过暂时停止按需实例以节省费用，实例默认停止七天。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopInstance
        :type request: :class:`huaweicloudsdkrds.v3.StopInstanceRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StopInstanceResponse`
        """
        return self._stop_instance_with_http_info(request)

    def _stop_instance_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/action/shutdown',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_ssl_async(self, request):
        """设置SSL数据加密

        设置SSL数据加密。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchSsl
        :type request: :class:`huaweicloudsdkrds.v3.SwitchSslRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SwitchSslResponse`
        """
        return self._switch_ssl_with_http_info(request)

    def _switch_ssl_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/ssl',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchSslResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_configuration_async(self, request):
        """修改参数模板参数

        修改参数模板参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.UpdateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateConfigurationResponse`
        """
        return self._update_configuration_with_http_info(request)

    def _update_configuration_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_ip_async(self, request):
        """修改内网地址

        修改内网地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataIp
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDataIpRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDataIpResponse`
        """
        return self._update_data_ip_with_http_info(request)

    def _update_data_ip_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/ip',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_dns_name_async(self, request):
        """修改域名

        修改域名
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDnsName
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDnsNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDnsNameResponse`
        """
        return self._update_dns_name_with_http_info(request)

    def _update_dns_name_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/modify-dns',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDnsNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_configuration_async(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConfiguration
        :type request: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationResponse`
        """
        return self._update_instance_configuration_with_http_info(request)

    def _update_instance_configuration_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/configurations',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_configuration_async_async(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConfigurationAsync
        :type request: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationAsyncRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateInstanceConfigurationAsyncResponse`
        """
        return self._update_instance_configuration_async_with_http_info(request)

    def _update_instance_configuration_async_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/configurations',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInstanceConfigurationAsyncResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_instance_name_async(self, request):
        """修改实例名称

        修改实例名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkrds.v3.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateInstanceNameResponse`
        """
        return self._update_instance_name_with_http_info(request)

    def _update_instance_name_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='UpdateInstanceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_port_async(self, request):
        """修改数据库端口

        修改数据库端口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePort
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePortRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePortResponse`
        """
        return self._update_port_with_http_info(request)

    def _update_port_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='UpdatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_postgresql_instance_alias_async(self, request):
        """修改实例备注信息

        修改指定数据库实例的备注信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePostgresqlInstanceAlias
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlInstanceAliasRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlInstanceAliasResponse`
        """
        return self._update_postgresql_instance_alias_with_http_info(request)

    def _update_postgresql_instance_alias_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='UpdatePostgresqlInstanceAliasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_db_version_async(self, request):
        """升级内核小版本

        对实例进行小版本升级。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeDbVersion
        :type request: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionResponse`
        """
        return self._upgrade_db_version_with_http_info(request)

    def _upgrade_db_version_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/action/db-upgrade',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpgradeDbVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_db_version_new_async(self, request):
        """升级内核小版本

        对实例进行小版本升级。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeDbVersionNew
        :type request: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpgradeDbVersionNewResponse`
        """
        return self._upgrade_db_version_new_with_http_info(request)

    def _upgrade_db_version_new_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='UpgradeDbVersionNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_version_async(self, request):
        """查询API版本列表

        查询API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdkrds.v3.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListApiVersionResponse`
        """
        return self._list_api_version_with_http_info(request)

    def _list_api_version_with_http_info(self, request):
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
            resource_path='/rds',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_version_new_async(self, request):
        """查询API版本列表

        查询API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersionNew
        :type request: :class:`huaweicloudsdkrds.v3.ListApiVersionNewRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListApiVersionNewResponse`
        """
        return self._list_api_version_new_with_http_info(request)

    def _list_api_version_new_with_http_info(self, request):
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
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListApiVersionNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_version_async(self, request):
        """查询指定的API版本信息

        查询指定的API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkrds.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowApiVersionResponse`
        """
        return self._show_api_version_with_http_info(request)

    def _show_api_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/rds/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApiVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def allow_db_user_privilege_async(self, request):
        """授权数据库帐号

        授权数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AllowDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.AllowDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AllowDbUserPrivilegeResponse`
        """
        return self._allow_db_user_privilege_with_http_info(request)

    def _allow_db_user_privilege_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_privilege',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AllowDbUserPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database_async(self, request):
        """创建数据库

        创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDatabase
        :type request: :class:`huaweicloudsdkrds.v3.CreateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateDatabaseResponse`
        """
        return self._create_database_with_http_info(request)

    def _create_database_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_db_user_async(self, request):
        """创建数据库用户

        在指定实例中创建数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDbUser
        :type request: :class:`huaweicloudsdkrds.v3.CreateDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateDbUserResponse`
        """
        return self._create_db_user_with_http_info(request)

    def _create_db_user_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database_async(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDatabase
        :type request: :class:`huaweicloudsdkrds.v3.DeleteDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteDatabaseResponse`
        """
        return self._delete_database_with_http_info(request)

    def _delete_database_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/{db_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_db_user_async(self, request):
        """删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDbUser
        :type request: :class:`huaweicloudsdkrds.v3.DeleteDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteDbUserResponse`
        """
        return self._delete_db_user_with_http_info(request)

    def _delete_db_user_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/{user_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_authorized_databases_async(self, request):
        """查询指定用户的已授权数据库

        查询指定用户的已授权数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizedDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListAuthorizedDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuthorizedDatabasesResponse`
        """
        return self._list_authorized_databases_with_http_info(request)

    def _list_authorized_databases_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/database',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuthorizedDatabasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_authorized_db_users_async(self, request):
        """查询指定数据库的已授权用户

        查询指定数据库的已授权用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizedDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListAuthorizedDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuthorizedDbUsersResponse`
        """
        return self._list_authorized_db_users_with_http_info(request)

    def _list_authorized_db_users_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/db_user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuthorizedDbUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_databases_async(self, request):
        """查询数据库列表

        查询数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDatabasesResponse`
        """
        return self._list_databases_with_http_info(request)

    def _list_databases_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_db_users_async(self, request):
        """查询数据库用户列表

        查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListDbUsersResponse`
        """
        return self._list_db_users_with_http_info(request)

    def _list_db_users_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDbUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_pwd_async(self, request):
        """重置数据库密码

        重置数据库密码.
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPwd
        :type request: :class:`huaweicloudsdkrds.v3.ResetPwdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ResetPwdResponse`
        """
        return self._reset_pwd_with_http_info(request)

    def _reset_pwd_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='ResetPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def revoke_async(self, request):
        """解除数据库帐号权限

        解除数据库帐号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Revoke
        :type request: :class:`huaweicloudsdkrds.v3.RevokeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RevokeResponse`
        """
        return self._revoke_with_http_info(request)

    def _revoke_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_privilege',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RevokeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_db_user_pwd_async(self, request):
        """设置数据库账号密码

        设置数据库账号密码
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetDbUserPwd
        :type request: :class:`huaweicloudsdkrds.v3.SetDbUserPwdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetDbUserPwdResponse`
        """
        return self._set_db_user_pwd_with_http_info(request)

    def _set_db_user_pwd_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/resetpwd',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetDbUserPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_read_only_switch_async(self, request):
        """设置数据库用户只读参数

        根据业务需求，设置数据库用户只读
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetReadOnlySwitch
        :type request: :class:`huaweicloudsdkrds.v3.SetReadOnlySwitchRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetReadOnlySwitchResponse`
        """
        return self._set_read_only_switch_with_http_info(request)

    def _set_read_only_switch_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/readonly-status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetReadOnlySwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_database_async(self, request):
        """修改指定实例的数据库备注

        修改指定实例中的数据库备注。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDatabase
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDatabaseResponse`
        """
        return self._update_database_with_http_info(request)

    def _update_database_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_db_user_comment_async(self, request):
        """修改数据库用户名备注

        修改数据库用户名备注
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDbUserComment
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDbUserCommentRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDbUserCommentResponse`
        """
        return self._update_db_user_comment_with_http_info(request)

    def _update_db_user_comment_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/{user_name}/comment',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDbUserCommentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def allow_db_privilege_async(self, request):
        """授权数据库帐号

        在指定实例的数据库中, 设置帐号的权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AllowDbPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.AllowDbPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AllowDbPrivilegeResponse`
        """
        return self._allow_db_privilege_with_http_info(request)

    def _allow_db_privilege_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_privilege',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AllowDbPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_proxy_scale_async(self, request):
        """数据库代理规格变更

        数据库代理实例进行规格变更。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeProxyScale
        :type request: :class:`huaweicloudsdkrds.v3.ChangeProxyScaleRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeProxyScaleResponse`
        """
        return self._change_proxy_scale_with_http_info(request)

    def _change_proxy_scale_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/scale',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeProxyScaleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_the_delay_threshold_async(self, request):
        """修改读写分离阈值

        修改指定实例的读写分离延时阈值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeTheDelayThreshold
        :type request: :class:`huaweicloudsdkrds.v3.ChangeTheDelayThresholdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ChangeTheDelayThresholdResponse`
        """
        return self._change_the_delay_threshold_with_http_info(request)

    def _change_the_delay_threshold_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/delay-threshold',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeTheDelayThresholdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_postgresql_database_async(self, request):
        """创建数据库

        在指定实例中创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostgresqlDatabase
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseResponse`
        """
        return self._create_postgresql_database_with_http_info(request)

    def _create_postgresql_database_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePostgresqlDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_postgresql_database_schema_async(self, request):
        """创建数据库SCHEMA

        在指定实例的数据库中, 创建数据库schema。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostgresqlDatabaseSchema
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseSchemaRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDatabaseSchemaResponse`
        """
        return self._create_postgresql_database_schema_with_http_info(request)

    def _create_postgresql_database_schema_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/schema',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePostgresqlDatabaseSchemaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_postgresql_db_user_async(self, request):
        """创建数据库用户

        在指定实例中创建数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostgresqlDbUser
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlDbUserResponse`
        """
        return self._create_postgresql_db_user_with_http_info(request)

    def _create_postgresql_db_user_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePostgresqlDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_postgresql_extension_async(self, request):
        """创建插件

        在指定数据库上创建插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePostgresqlExtension
        :type request: :class:`huaweicloudsdkrds.v3.CreatePostgresqlExtensionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreatePostgresqlExtensionResponse`
        """
        return self._create_postgresql_extension_with_http_info(request)

    def _create_postgresql_extension_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/extensions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePostgresqlExtensionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_postgresql_database_async(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePostgresqlDatabase
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDatabaseResponse`
        """
        return self._delete_postgresql_database_with_http_info(request)

    def _delete_postgresql_database_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/{db_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePostgresqlDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_postgresql_db_user_async(self, request):
        """删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePostgresqlDbUser
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlDbUserResponse`
        """
        return self._delete_postgresql_db_user_with_http_info(request)

    def _delete_postgresql_db_user_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/{user_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePostgresqlDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_postgresql_extension_async(self, request):
        """删除插件

        在指定数据库上删除插件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePostgresqlExtension
        :type request: :class:`huaweicloudsdkrds.v3.DeletePostgresqlExtensionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeletePostgresqlExtensionResponse`
        """
        return self._delete_postgresql_extension_with_http_info(request)

    def _delete_postgresql_extension_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/extensions',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePostgresqlExtensionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_postgresql_database_schemas_async(self, request):
        """查询数据库SCHEMA列表

        查询指定实例的数据库SCHEMA列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPostgresqlDatabaseSchemas
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabaseSchemasRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabaseSchemasResponse`
        """
        return self._list_postgresql_database_schemas_with_http_info(request)

    def _list_postgresql_database_schemas_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/schema/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPostgresqlDatabaseSchemasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_postgresql_databases_async(self, request):
        """查询数据库列表

        查询指定实例中的数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPostgresqlDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlDatabasesResponse`
        """
        return self._list_postgresql_databases_with_http_info(request)

    def _list_postgresql_databases_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPostgresqlDatabasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_postgresql_db_user_paginated_async(self, request):
        """查询数据库用户列表

        在指定实例中查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPostgresqlDbUserPaginated
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlDbUserPaginatedRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlDbUserPaginatedResponse`
        """
        return self._list_postgresql_db_user_paginated_with_http_info(request)

    def _list_postgresql_db_user_paginated_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPostgresqlDbUserPaginatedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_postgresql_extension_async(self, request):
        """查询插件

        获取指定数据库的插件信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPostgresqlExtension
        :type request: :class:`huaweicloudsdkrds.v3.ListPostgresqlExtensionRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListPostgresqlExtensionResponse`
        """
        return self._list_postgresql_extension_with_http_info(request)

    def _list_postgresql_extension_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/extensions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPostgresqlExtensionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_query_scale_compute_flavors_async(self, request):
        """查询数据库代理可变更的规格

        查询数据库代理可变更的规格信息。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchQueryScaleComputeFlavors
        :type request: :class:`huaweicloudsdkrds.v3.SearchQueryScaleComputeFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SearchQueryScaleComputeFlavorsResponse`
        """
        return self._search_query_scale_compute_flavors_with_http_info(request)

    def _search_query_scale_compute_flavors_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/proxy/scale/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchQueryScaleComputeFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_query_scale_flavors_async(self, request):
        """查询数据库代理可变更的规格

        查询数据库代理可变更的规格信息。
        
        - 调用接口前，您需要了解API 认证鉴权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchQueryScaleFlavors
        :type request: :class:`huaweicloudsdkrds.v3.SearchQueryScaleFlavorsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SearchQueryScaleFlavorsResponse`
        """
        return self._search_query_scale_flavors_with_http_info(request)

    def _search_query_scale_flavors_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/scale/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchQueryScaleFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_database_user_privilege_async(self, request):
        """设置数据库用户权限

        设置数据库用户权限：只读或可读写。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetDatabaseUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.SetDatabaseUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetDatabaseUserPrivilegeResponse`
        """
        return self._set_database_user_privilege_with_http_info(request)

    def _set_database_user_privilege_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/user-privilege',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetDatabaseUserPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_postgresql_db_user_pwd_async(self, request):
        """重置数据库帐号密码

        重置指定数据库帐号的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetPostgresqlDbUserPwd
        :type request: :class:`huaweicloudsdkrds.v3.SetPostgresqlDbUserPwdRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.SetPostgresqlDbUserPwdResponse`
        """
        return self._set_postgresql_db_user_pwd_with_http_info(request)

    def _set_postgresql_db_user_pwd_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/resetpwd',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetPostgresqlDbUserPwdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_information_about_database_proxy_async(self, request):
        """查询数据库代理信息

        查询指定实例的数据库代理详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInformationAboutDatabaseProxy
        :type request: :class:`huaweicloudsdkrds.v3.ShowInformationAboutDatabaseProxyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowInformationAboutDatabaseProxyResponse`
        """
        return self._show_information_about_database_proxy_with_http_info(request)

    def _show_information_about_database_proxy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInformationAboutDatabaseProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_postgresql_param_value_async(self, request):
        """获取实例指定参数的值

        获取实例指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPostgresqlParamValue
        :type request: :class:`huaweicloudsdkrds.v3.ShowPostgresqlParamValueRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ShowPostgresqlParamValueResponse`
        """
        return self._show_postgresql_param_value_with_http_info(request)

    def _show_postgresql_param_value_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/parameter/{name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPostgresqlParamValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_database_proxy_async(self, request):
        """开启数据库代理

        为指定实例开启数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartDatabaseProxy
        :type request: :class:`huaweicloudsdkrds.v3.StartDatabaseProxyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StartDatabaseProxyResponse`
        """
        return self._start_database_proxy_with_http_info(request)

    def _start_database_proxy_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='StartDatabaseProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_database_proxy_async(self, request):
        """关闭数据库代理

        为指定实例关闭数据库代理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopDatabaseProxy
        :type request: :class:`huaweicloudsdkrds.v3.StopDatabaseProxyRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.StopDatabaseProxyResponse`
        """
        return self._stop_database_proxy_with_http_info(request)

    def _stop_database_proxy_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='StopDatabaseProxyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_db_user_privilege_async(self, request):
        """update_db_user_privilege

        数据库帐号授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.UpdateDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateDbUserPrivilegeResponse`
        """
        return self._update_db_user_privilege_with_http_info(request)

    def _update_db_user_privilege_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db-user-privilege',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDbUserPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_postgresql_database_async(self, request):
        """修改指定实例的数据库备注

        修改指定实例中的数据库备注。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePostgresqlDatabase
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDatabaseResponse`
        """
        return self._update_postgresql_database_with_http_info(request)

    def _update_postgresql_database_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePostgresqlDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_postgresql_db_user_comment_async(self, request):
        """修改数据库用户名备注

        修改数据库用户名备注
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePostgresqlDbUserComment
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDbUserCommentRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlDbUserCommentResponse`
        """
        return self._update_postgresql_db_user_comment_with_http_info(request)

    def _update_postgresql_db_user_comment_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/{user_name}/comment',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePostgresqlDbUserCommentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_postgresql_parameter_value_async(self, request):
        """修改实例指定参数的值

        修改实例指定参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePostgresqlParameterValue
        :type request: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlParameterValueRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdatePostgresqlParameterValueResponse`
        """
        return self._update_postgresql_parameter_value_with_http_info(request)

    def _update_postgresql_parameter_value_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/parameter/{name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePostgresqlParameterValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_read_weight_async(self, request):
        """修改读写分离权重

        修改指定实例的读写分离权重。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateReadWeight
        :type request: :class:`huaweicloudsdkrds.v3.UpdateReadWeightRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.UpdateReadWeightResponse`
        """
        return self._update_read_weight_with_http_info(request)

    def _update_read_weight_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/proxy/weight',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateReadWeightResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def allow_sqlserver_db_user_privilege_async(self, request):
        """授权数据库帐号

        授权数据库帐号。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AllowSqlserverDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.AllowSqlserverDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.AllowSqlserverDbUserPrivilegeResponse`
        """
        return self._allow_sqlserver_db_user_privilege_with_http_info(request)

    def _allow_sqlserver_db_user_privilege_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_privilege',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AllowSqlserverDbUserPrivilegeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_msdtcs_async(self, request):
        """添加MSDTC

        添加MSDTC相关主机host地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddMsdtcs
        :type request: :class:`huaweicloudsdkrds.v3.BatchAddMsdtcsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.BatchAddMsdtcsResponse`
        """
        return self._batch_add_msdtcs_with_http_info(request)

    def _batch_add_msdtcs_with_http_info(self, request):
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/msdtc/host',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddMsdtcsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sqlserver_database_async(self, request):
        """创建数据库

        创建数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSqlserverDatabase
        :type request: :class:`huaweicloudsdkrds.v3.CreateSqlserverDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSqlserverDatabaseResponse`
        """
        return self._create_sqlserver_database_with_http_info(request)

    def _create_sqlserver_database_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSqlserverDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_sqlserver_db_user_async(self, request):
        """创建数据库用户

        创建数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSqlserverDbUser
        :type request: :class:`huaweicloudsdkrds.v3.CreateSqlserverDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSqlserverDbUserResponse`
        """
        return self._create_sqlserver_db_user_with_http_info(request)

    def _create_sqlserver_db_user_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSqlserverDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sqlserver_database_async(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSqlserverDatabase
        :type request: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseResponse`
        """
        return self._delete_sqlserver_database_with_http_info(request)

    def _delete_sqlserver_database_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/{db_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSqlserverDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sqlserver_database_ex_async(self, request):
        """删除数据库

        删除数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSqlserverDatabaseEx
        :type request: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseExRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDatabaseExResponse`
        """
        return self._delete_sqlserver_database_ex_with_http_info(request)

    def _delete_sqlserver_database_ex_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/instances/{instance_id}/database/{db_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSqlserverDatabaseExResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sqlserver_db_user_async(self, request):
        """删除数据库用户

        删除数据库用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSqlserverDbUser
        :type request: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDbUserRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.DeleteSqlserverDbUserResponse`
        """
        return self._delete_sqlserver_db_user_with_http_info(request)

    def _delete_sqlserver_db_user_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/{user_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSqlserverDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_authorized_sqlserver_db_users_async(self, request):
        """查询指定数据库的已授权用户

        查询指定数据库的已授权用户。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuthorizedSqlserverDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListAuthorizedSqlserverDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListAuthorizedSqlserverDbUsersResponse`
        """
        return self._list_authorized_sqlserver_db_users_with_http_info(request)

    def _list_authorized_sqlserver_db_users_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/db_user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuthorizedSqlserverDbUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_msdtc_hosts_async(self, request):
        """查询MSDTC的hosts信息

        查询MSDTC的hosts信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMsdtcHosts
        :type request: :class:`huaweicloudsdkrds.v3.ListMsdtcHostsRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListMsdtcHostsResponse`
        """
        return self._list_msdtc_hosts_with_http_info(request)

    def _list_msdtc_hosts_with_http_info(self, request):
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
            resource_path='/v3/{project_id}/instances/{instance_id}/msdtc/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMsdtcHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sqlserver_databases_async(self, request):
        """查询数据库列表

        查询数据库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSqlserverDatabases
        :type request: :class:`huaweicloudsdkrds.v3.ListSqlserverDatabasesRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSqlserverDatabasesResponse`
        """
        return self._list_sqlserver_databases_with_http_info(request)

    def _list_sqlserver_databases_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/database/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSqlserverDatabasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sqlserver_db_users_async(self, request):
        """查询数据库用户列表

        查询数据库用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSqlserverDbUsers
        :type request: :class:`huaweicloudsdkrds.v3.ListSqlserverDbUsersRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ListSqlserverDbUsersResponse`
        """
        return self._list_sqlserver_db_users_with_http_info(request)

    def _list_sqlserver_db_users_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_user/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSqlserverDbUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def modify_collation_async(self, request):
        """修改实例字符集

        修改实例字符集。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyCollation
        :type request: :class:`huaweicloudsdkrds.v3.ModifyCollationRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.ModifyCollationResponse`
        """
        return self._modify_collation_with_http_info(request)

    def _modify_collation_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/collations',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ModifyCollationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def revoke_sqlserver_db_user_privilege_async(self, request):
        """解除数据库帐号权限

        解除数据库帐号权限。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokeSqlserverDbUserPrivilege
        :type request: :class:`huaweicloudsdkrds.v3.RevokeSqlserverDbUserPrivilegeRequest`
        :rtype: :class:`huaweicloudsdkrds.v3.RevokeSqlserverDbUserPrivilegeResponse`
        """
        return self._revoke_sqlserver_db_user_privilege_with_http_info(request)

    def _revoke_sqlserver_db_user_privilege_with_http_info(self, request):
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

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db_privilege',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RevokeSqlserverDbUserPrivilegeResponse',
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

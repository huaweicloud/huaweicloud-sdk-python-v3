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


class GaussDBforNoSQLAsyncClient(Client):
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
        super(GaussDBforNoSQLAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkgaussdbfornosql.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "GaussDBforNoSQLClient":
            raise TypeError("client type error, support client type is GaussDBforNoSQLClient")

        return ClientBuilder(clazz)

    def apply_configuration_async(self, request):
        """应用参数模板

        将参数模板应用到实例，可以指定一个或多个实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ApplyConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ApplyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ApplyConfigurationResponse`
        """
        return self.apply_configuration_with_http_info(request)

    def apply_configuration_with_http_info(self, request):
        all_params = ['config_id', 'apply_configuration_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/configurations/{config_id}/apply',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ApplyConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_tag_action_async(self, request):
        """批量添加或删除资源标签

        批量添加或删除指定数据库实例的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.BatchTagActionResponse`
        """
        return self.batch_tag_action_with_http_info(request)

    def batch_tag_action_with_http_info(self, request):
        all_params = ['instance_id', 'batch_tag_action_request_body']
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
            response_type='BatchTagActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_disaster_recovery_operation_async(self, request):
        """校验实例是否可以与指定实例建立/解除容灾关系

        校验实例是否可以与指定实例建立/解除容灾关系。若接口返回成功，表示可以与指定实例建立/解除容灾关系。
        该接口需要对建立/解除容灾关系的两个实例各调用一次，2次调用都响应成功才能进行容灾关系的搭建/解除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDisasterRecoveryOperation
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckDisasterRecoveryOperationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckDisasterRecoveryOperationResponse`
        """
        return self.check_disaster_recovery_operation_with_http_info(request)

    def check_disaster_recovery_operation_with_http_info(self, request):
        all_params = ['instance_id', 'precheck_disaster_recovery_operation_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/disaster-recovery/precheck',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckDisasterRecoveryOperationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_week_password_async(self, request):
        """判断弱密码

        判断弱密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckWeekPassword
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckWeekPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CheckWeekPasswordResponse`
        """
        return self.check_week_password_with_http_info(request)

    def check_week_password_with_http_info(self, request):
        all_params = ['check_week_password_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/weak-password-verification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckWeekPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def compare_configuration_async(self, request):
        """参数模板比较

        比较两个参数模板之间的差异
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CompareConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CompareConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CompareConfigurationResponse`
        """
        return self.compare_configuration_with_http_info(request)

    def compare_configuration_with_http_info(self, request):
        all_params = ['show_param_group_difference_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/configurations/comparison',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CompareConfigurationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_configuration_async(self, request):
        """复制参数模板

        复制参数模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CopyConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CopyConfigurationResponse`
        """
        return self.copy_configuration_with_http_info(request)

    def copy_configuration_with_http_info(self, request):
        all_params = ['config_id', 'copy_tmpl_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def create_back_async(self, request):
        """创建手动备份

        创建手动备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBack
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateBackRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateBackResponse`
        """
        return self.create_back_with_http_info(request)

    def create_back_with_http_info(self, request):
        all_params = ['instance_id', 'create_backup']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBackResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cold_volume_async(self, request):
        """‘创建冷数据存储’

        ‘创建冷数据存储’
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateColdVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateColdVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateColdVolumeResponse`
        """
        return self.create_cold_volume_with_http_info(request)

    def create_cold_volume_with_http_info(self, request):
        all_params = ['instance_id', 'create_cold_volume_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/cold-volume',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateColdVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_configuration_async(self, request):
        """创建参数模板

        创建参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateConfigurationResponse`
        """
        return self.create_configuration_with_http_info(request)

    def create_configuration_with_http_info(self, request):
        all_params = ['create_configuration_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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

    def create_disaster_recovery_async(self, request):
        """搭建实例与特定实例的容灾关系

        搭建实例与特定实例的容灾关系。 该接口需要对搭建容灾关系的两个实例分别各调用一次，2次接口都调用成功才能成功搭建容灾关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDisasterRecovery
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateDisasterRecoveryResponse`
        """
        return self.create_disaster_recovery_with_http_info(request)

    def create_disaster_recovery_with_http_info(self, request):
        all_params = ['instance_id', 'construct_disaster_recovery_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/disaster-recovery/construction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance_async(self, request):
        """创建实例

        创建数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.CreateInstanceResponse`
        """
        return self.create_instance_with_http_info(request)

    def create_instance_with_http_info(self, request):
        all_params = ['create_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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

    def delete_backup_async(self, request):
        """删除手动备份

        删除手动备份
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteBackupResponse`
        """
        return self.delete_backup_with_http_info(request)

    def delete_backup_with_http_info(self, request):
        all_params = ['backup_id']
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
            response_type='DeleteBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_configuration_async(self, request):
        """删除参数模板

        删除指定参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteConfigurationResponse`
        """
        return self.delete_configuration_with_http_info(request)

    def delete_configuration_with_http_info(self, request):
        all_params = ['config_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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

    def delete_disaster_recovery_async(self, request):
        """解除实例与特定实例的容灾关系

        解除实例与特定实例的容灾关系。 该接口需要对搭建容灾关系的两个实例分别各调用一次，2次接口都调用成功才能成功解除容灾关系。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDisasterRecovery
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDisasterRecoveryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteDisasterRecoveryResponse`
        """
        return self.delete_disaster_recovery_with_http_info(request)

    def delete_disaster_recovery_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/disaster-recovery/deconstruction',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDisasterRecoveryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_enlarge_fail_node_async(self, request):
        """删除扩容失败的节点

        删除扩容失败的节点
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEnlargeFailNode
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteEnlargeFailNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteEnlargeFailNodeResponse`
        """
        return self.delete_enlarge_fail_node_with_http_info(request)

    def delete_enlarge_fail_node_with_http_info(self, request):
        all_params = ['instance_id', 'delete_enlarge_fail_node_request_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/enlarge-failed-nodes',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnlargeFailNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance_async(self, request):
        """删除实例

        删除数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.DeleteInstanceResponse`
        """
        return self.delete_instance_with_http_info(request)

    def delete_instance_with_http_info(self, request):
        all_params = ['instance_id']
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

    def expand_instance_node_async(self, request):
        """扩容指定集群实例的节点数量

        扩容指定集群实例的节点数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandInstanceNode
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ExpandInstanceNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ExpandInstanceNodeResponse`
        """
        return self.expand_instance_node_with_http_info(request)

    def expand_instance_node_with_http_info(self, request):
        all_params = ['instance_id', 'enlarge_instance_request_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/enlarge-node',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandInstanceNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_available_flavor_infos_async(self, request):
        """查询实例可变更规格

        查询实例可变更规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableFlavorInfos
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListAvailableFlavorInfosRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListAvailableFlavorInfosResponse`
        """
        return self.list_available_flavor_infos_with_http_info(request)

    def list_available_flavor_infos_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
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
            response_type='ListAvailableFlavorInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configuration_datastores_async(self, request):
        """查询支持参数模板的引擎信息

        查询支持参数模板的引擎信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurationDatastores
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationDatastoresRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationDatastoresResponse`
        """
        return self.list_configuration_datastores_with_http_info(request)

    def list_configuration_datastores_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/configurations/datastores',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigurationDatastoresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configuration_templates_async(self, request):
        """获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurationTemplates
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationTemplatesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationTemplatesResponse`
        """
        return self.list_configuration_templates_with_http_info(request)

    def list_configuration_templates_with_http_info(self, request):
        all_params = ['offset', 'limit']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3.1/{project_id}/configurations',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConfigurationTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_configurations_async(self, request):
        """获取参数模板列表

        获取参数模板列表，包括所有数据库的默认参数模板和用户创建的参数模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConfigurations
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListConfigurationsResponse`
        """
        return self.list_configurations_with_http_info(request)

    def list_configurations_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        """查询指定实例类型的数据库版本信息

        查询指定实例类型的数据库版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDatastores
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDatastoresRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDatastoresResponse`
        """
        return self.list_datastores_with_http_info(request)

    def list_datastores_with_http_info(self, request):
        all_params = ['datastore_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datastore_name' in local_var_params:
            path_params['datastore_name'] = local_var_params['datastore_name']

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
            resource_path='/v3/{project_id}/datastores/{datastore_name}/versions',
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

    def list_dedicated_resources_async(self, request):
        """查询专属资源列表

        查询专属资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDedicatedResources
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDedicatedResourcesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListDedicatedResourcesResponse`
        """
        return self.list_dedicated_resources_with_http_info(request)

    def list_dedicated_resources_with_http_info(self, request):
        all_params = ['offset', 'limit']
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
            response_type='ListDedicatedResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_eps_quotas_async(self, request):
        """查询企业项目配额

        查询企业项目配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEpsQuotas
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListEpsQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListEpsQuotasResponse`
        """
        return self.list_eps_quotas_with_http_info(request)

    def list_eps_quotas_with_http_info(self, request):
        all_params = ['enterprise_project_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/enterprise-projects/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEpsQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavor_infos_async(self, request):
        """查询数据库规格

        查询指定条件下的实例规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavorInfos
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorInfosRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorInfosResponse`
        """
        return self.list_flavor_infos_with_http_info(request)

    def list_flavor_infos_with_http_info(self, request):
        all_params = ['engine_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'engine_name' in local_var_params:
            query_params.append(('engine_name', local_var_params['engine_name']))
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
            resource_path='/v3.1/{project_id}/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors_async(self, request):
        """查询指定条件下的所有实例规格信息

        查询指定条件下的所有实例规格信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        all_params = ['region', 'engine_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/flavors',
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

    def list_instance_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstanceTagsResponse`
        """
        return self.list_instance_tags_with_http_info(request)

    def list_instance_tags_with_http_info(self, request):
        all_params = ['instance_id']
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
        """查询实例列表和详情

        根据指定条件查询数据库实例列表和详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesResponse`
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        all_params = ['id', 'name', 'mode', 'datastore_type', 'vpc_id', 'subnet_id', 'offset', 'limit']
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

    def list_instances_by_resource_tags_async(self, request):
        """查询资源实例

        根据标签查询指定的数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesByResourceTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByResourceTagsResponse`
        """
        return self.list_instances_by_resource_tags_with_http_info(request)

    def list_instances_by_resource_tags_with_http_info(self, request):
        all_params = ['list_instances_by_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/instances/resource-instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesByResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instances_by_tags_async(self, request):
        """查询资源实例

        根据标签查询指定的数据库实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstancesByTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesByTagsResponse`
        """
        return self.list_instances_by_tags_with_http_info(request)

    def list_instances_by_tags_with_http_info(self, request):
        all_params = ['list_instances_by_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/instances/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstancesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_tags_async(self, request):
        """查询项目标签

        查询指定项目的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListProjectTagsResponse`
        """
        return self.list_project_tags_with_http_info(request)

    def list_project_tags_with_http_info(self, request):
        all_params = ['offset', 'limit']
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
        """查询回收站实例列表

        查询回收站所有引擎的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRecycleInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRecycleInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRecycleInstancesResponse`
        """
        return self.list_recycle_instances_with_http_info(request)

    def list_recycle_instances_with_http_info(self, request):
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

    def list_restore_time_async(self, request):
        """查询实例可恢复的时间段

        查询实例可恢复的时间段
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRestoreTime
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreTimeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListRestoreTimeResponse`
        """
        return self.list_restore_time_with_http_info(request)

    def list_restore_time_with_http_info(self, request):
        all_params = ['instance_id', 'start_time', 'end_time', 'offset', 'limit']
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/backups/restorable-time-periods',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRestoreTimeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_slow_logs_async(self, request):
        """查询数据库慢日志

        查询数据库慢日志信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSlowLogs
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListSlowLogsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListSlowLogsResponse`
        """
        return self.list_slow_logs_with_http_info(request)

    def list_slow_logs_with_http_info(self, request):
        all_params = ['instance_id', 'start_date', 'end_date', 'node_id', 'type', 'offset', 'limit']
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

    def modify_eps_quotas_async(self, request):
        """修改企业项目配额

        修改企业项目配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyEpsQuotas
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyEpsQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyEpsQuotasResponse`
        """
        return self.modify_eps_quotas_with_http_info(request)

    def modify_eps_quotas_with_http_info(self, request):
        all_params = ['quotas']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/enterprise-projects/quotas',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ModifyEpsQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def modify_port_async(self, request):
        """修改数据库端口

        修改数据库实例的端口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyPort
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPortRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPortResponse`
        """
        return self.modify_port_with_http_info(request)

    def modify_port_with_http_info(self, request):
        all_params = ['instance_id', 'modify_port_request']
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
            response_type='ModifyPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def modify_public_ip_async(self, request):
        """绑定/解绑弹性公网IP

        实例下的节点绑定弹性公网IP/解绑弹性公网IP
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyPublicIp
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPublicIpRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyPublicIpResponse`
        """
        return self.modify_public_ip_with_http_info(request)

    def modify_public_ip_with_http_info(self, request):
        all_params = ['instance_id', 'node_id', 'bind_eip_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/nodes/{node_id}/public-ip',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ModifyPublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def modify_volume_async(self, request):
        """变更实例存储容量

        变更实例的存储容量大小
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ModifyVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ModifyVolumeResponse`
        """
        return self.modify_volume_with_http_info(request)

    def modify_volume_with_http_info(self, request):
        all_params = ['instance_id', 'adjust_volume_request_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/volume',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ModifyVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def pause_resume_data_synchronization_async(self, request):
        """暂停/恢复具备容灾关系的实例数据同步

        该接口用于暂停/恢复具备容灾关系的实例数据同步。
        
        该接口需要对具备容灾关系的两个实例分别各调用一次，2次接口都调用成功才能成功暂停/恢复容灾实例数据同步。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PauseResumeDataSynchronization
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.PauseResumeDataSynchronizationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.PauseResumeDataSynchronizationResponse`
        """
        return self.pause_resume_data_synchronization_with_http_info(request)

    def pause_resume_data_synchronization_with_http_info(self, request):
        all_params = ['instance_id', 'action_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/disaster-recovery/data-synchronization',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PauseResumeDataSynchronizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reset_password_async(self, request):
        """修改实例的管理员密码

        修改实例的管理员密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResetPassword
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResetPasswordResponse`
        """
        return self.reset_password_with_http_info(request)

    def reset_password_with_http_info(self, request):
        all_params = ['instance_id', 'reset_password_request_body']
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
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_cold_volume_async(self, request):
        """扩容冷数据存储

        扩容冷数据存储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeColdVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeColdVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeColdVolumeResponse`
        """
        return self.resize_cold_volume_with_http_info(request)

    def resize_cold_volume_with_http_info(self, request):
        all_params = ['instance_id', 'resize_cold_volume_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/cold-volume',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeColdVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_instance_async(self, request):
        """变更实例规格

        变更实例的规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceResponse`
        """
        return self.resize_instance_with_http_info(request)

    def resize_instance_with_http_info(self, request):
        all_params = ['instance_id', 'resize_instance_request_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/resize',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_instance_volume_async(self, request):
        """扩容实例存储容量

        扩容实例的存储容量大小。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeInstanceVolume
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceVolumeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ResizeInstanceVolumeResponse`
        """
        return self.resize_instance_volume_with_http_info(request)

    def resize_instance_volume_with_http_info(self, request):
        all_params = ['instance_id', 'resize_instance_volume_request_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/extend-volume',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeInstanceVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restart_instance_async(self, request):
        """重启实例的数据库服务

        重启实例的数据库服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.RestartInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RestartInstanceResponse`
        """
        return self.restart_instance_with_http_info(request)

    def restart_instance_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

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
            response_type='RestartInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_existing_instance_async(self, request):
        """恢复到已有实例

        恢复到已有实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreExistingInstance
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreExistingInstanceRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RestoreExistingInstanceResponse`
        """
        return self.restore_existing_instance_with_http_info(request)

    def restore_existing_instance_with_http_info(self, request):
        all_params = ['instance_id', 'restore_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/recovery',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreExistingInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def set_auto_enlarge_policy_async(self, request):
        """设置磁盘自动扩容策略

        设置磁盘自动扩容策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetAutoEnlargePolicyResponse`
        """
        return self.set_auto_enlarge_policy_with_http_info(request)

    def set_auto_enlarge_policy_with_http_info(self, request):
        all_params = ['set_auto_enlarge_policy_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/instances/disk-auto-expansion',
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
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetBackupPolicyResponse`
        """
        return self.set_backup_policy_with_http_info(request)

    def set_backup_policy_with_http_info(self, request):
        all_params = ['instance_id', 'set_backup_policy_request_body']
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

    def set_recycle_policy_async(self, request):
        """设置回收策略

        设置已删除实例保留天数，修改保留天数后删除的实例按照新的天数保留，修改之前已在回收站的实例保留天数不变。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SetRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SetRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SetRecyclePolicyResponse`
        """
        return self.set_recycle_policy_with_http_info(request)

    def set_recycle_policy_with_http_info(self, request):
        all_params = ['set_recycle_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v3/{project_id}/instances/recycle-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SetRecyclePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_all_instances_backups_async(self, request):
        """查询备份列表

        根据指定条件查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAllInstancesBackups
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAllInstancesBackupsRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAllInstancesBackupsResponse`
        """
        return self.show_all_instances_backups_with_http_info(request)

    def show_all_instances_backups_with_http_info(self, request):
        all_params = ['offset', 'limit', 'datastore_type', 'instance_id', 'backup_id', 'backup_type', 'begin_time', 'end_time']
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
            response_type='ShowAllInstancesBackupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_applicable_instances_async(self, request):
        """查询参数模板可应用的实例列表

        查询参数模板可应用的实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApplicableInstances
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplicableInstancesRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplicableInstancesResponse`
        """
        return self.show_applicable_instances_with_http_info(request)

    def show_applicable_instances_with_http_info(self, request):
        all_params = ['config_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}/applicable-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplicableInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_apply_history_async(self, request):
        """查询参数模板应用历史

        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApplyHistory
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplyHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApplyHistoryResponse`
        """
        return self.show_apply_history_with_http_info(request)

    def show_apply_history_with_http_info(self, request):
        all_params = ['config_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/configurations/{config_id}/applied-histories',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowApplyHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auto_enlarge_policy_async(self, request):
        """查询磁盘自动扩容策略

        查询磁盘自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAutoEnlargePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAutoEnlargePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowAutoEnlargePolicyResponse`
        """
        return self.show_auto_enlarge_policy_with_http_info(request)

    def show_auto_enlarge_policy_with_http_info(self, request):
        all_params = ['instance_id']
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

    def show_backup_policy_async(self, request):
        """查询自动备份策略

        查询自动备份策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowBackupPolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowBackupPolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowBackupPolicyResponse`
        """
        return self.show_backup_policy_with_http_info(request)

    def show_backup_policy_with_http_info(self, request):
        all_params = ['instance_id']
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

    def show_configuration_detail_async(self, request):
        """获取指定参数模板的参数

        获取指定参数模板的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigurationDetail
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowConfigurationDetailRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowConfigurationDetailResponse`
        """
        return self.show_configuration_detail_with_http_info(request)

    def show_configuration_detail_with_http_info(self, request):
        all_params = ['config_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'config_id' in local_var_params:
            path_params['config_id'] = local_var_params['config_id']

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
            resource_path='/v3/{project_id}/configurations/{config_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConfigurationDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_error_log_async(self, request):
        """查询数据库错误日志信息

        查询数据库错误日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowErrorLog
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowErrorLogRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowErrorLogResponse`
        """
        return self.show_error_log_with_http_info(request)

    def show_error_log_with_http_info(self, request):
        all_params = ['instance_id', 'start_time', 'end_time', 'node_id', 'type', 'offset', 'limit']
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/error-log',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowErrorLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_configuration_async(self, request):
        """获取指定实例的参数

        获取指定实例的参数信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceConfigurationResponse`
        """
        return self.show_instance_configuration_with_http_info(request)

    def show_instance_configuration_with_http_info(self, request):
        all_params = ['instance_id']
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

    def show_instance_role_async(self, request):
        """获取容灾实例主/备角色信息

        该接口用于获取容灾实例主/备角色信息，以便后续容灾实例备升主和容灾实例主降备接口调用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceRole
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceRoleRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowInstanceRoleResponse`
        """
        return self.show_instance_role_with_http_info(request)

    def show_instance_role_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/instance-role',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_ip_num_requirement_async(self, request):
        """查询创建实例或扩容节点时需要的IP数量

        查询创建实例或扩容节点时需要的IP数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIpNumRequirement
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowIpNumRequirementRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowIpNumRequirementResponse`
        """
        return self.show_ip_num_requirement_with_http_info(request)

    def show_ip_num_requirement_with_http_info(self, request):
        all_params = ['node_num', 'engine_name', 'instance_mode', 'instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/ip-num-requirement',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIpNumRequirementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_modify_history_async(self, request):
        """查询实例参数的修改历史

        查询实例参数的修改历史
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModifyHistory
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowModifyHistoryRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowModifyHistoryResponse`
        """
        return self.show_modify_history_with_http_info(request)

    def show_modify_history_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit']
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
            response_type='ShowModifyHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_pause_resume_stutus_async(self, request):
        """获取容灾实例数据同步状态

        获取容灾实例数据同步状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPauseResumeStutus
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowPauseResumeStutusRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowPauseResumeStutusResponse`
        """
        return self.show_pause_resume_stutus_with_http_info(request)

    def show_pause_resume_stutus_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/disaster-recovery/data-synchronization',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPauseResumeStutusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas_async(self, request):
        """查询配额

        查询单租户在GaussDBforNoSQL服务下的资源配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowQuotasResponse`
        """
        return self.show_quotas_with_http_info(request)

    def show_quotas_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        """查询回收策略

        查询回收策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRecyclePolicy
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRecyclePolicyRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRecyclePolicyResponse`
        """
        return self.show_recycle_policy_with_http_info(request)

    def show_recycle_policy_with_http_info(self, request):
        all_params = ['x_language']
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

    def show_restorable_list_async(self, request):
        """查询可恢复的实例列表

        查询用户可恢复的实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRestorableList
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRestorableListRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowRestorableListResponse`
        """
        return self.show_restorable_list_with_http_info(request)

    def show_restorable_list_with_http_info(self, request):
        all_params = ['backup_id', 'offset', 'limit']
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
            resource_path='/v3/{project_id}/backups/{backup_id}/restorable-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRestorableListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_slow_log_desensitization_async(self, request):
        """查询慢日志脱敏状态

        查询慢日志脱敏状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSlowLogDesensitization
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowSlowLogDesensitizationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowSlowLogDesensitizationResponse`
        """
        return self.show_slow_log_desensitization_with_http_info(request)

    def show_slow_log_desensitization_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog-desensitization',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSlowLogDesensitizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def shrink_instance_node_async(self, request):
        """缩容指定集群实例的节点数量

        缩容指定集群实例的节点数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShrinkInstanceNode
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShrinkInstanceNodeRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShrinkInstanceNodeResponse`
        """
        return self.shrink_instance_node_with_http_info(request)

    def shrink_instance_node_with_http_info(self, request):
        all_params = ['instance_id', 'enlarge_instance_request_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/reduce-node',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShrinkInstanceNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_slowlog_desensitization_async(self, request):
        """设置慢日志脱敏状态

        设置慢日志脱敏状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchSlowlogDesensitization
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSlowlogDesensitizationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSlowlogDesensitizationResponse`
        """
        return self.switch_slowlog_desensitization_with_http_info(request)

    def switch_slowlog_desensitization_with_http_info(self, request):
        all_params = ['instance_id', 'set_slow_log_plaintext_switch_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/slowlog-desensitization',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchSlowlogDesensitizationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_ssl_async(self, request):
        """切换实例SSL开关

        切换实例SSL开关。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchSsl
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSslRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchSslResponse`
        """
        return self.switch_ssl_with_http_info(request)

    def switch_ssl_with_http_info(self, request):
        all_params = ['instance_id', 'switch_ssl_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/ssl-option',
            method='POST',
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

    def switch_to_master_async(self, request):
        """容灾实例备升主

        该接口用于对已经搭建容灾关系的实例，将备实例升级为主实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchToMaster
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToMasterRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToMasterResponse`
        """
        return self.switch_to_master_with_http_info(request)

    def switch_to_master_with_http_info(self, request):
        all_params = ['instance_id', 'switch_to_master_disaster_recovery_body']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/switchover-master',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchToMasterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_to_slave_async(self, request):
        """容灾实例主降备

        该接口用于对已经搭建容灾关系的实例，将主实例降级为备实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchToSlave
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToSlaveRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.SwitchToSlaveResponse`
        """
        return self.switch_to_slave_with_http_info(request)

    def switch_to_slave_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/switchover-slave',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchToSlaveResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_client_network_async(self, request):
        """修改副本集跨网段访问配置

        修改副本集跨网段访问配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateClientNetwork
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateClientNetworkRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateClientNetworkResponse`
        """
        return self.update_client_network_with_http_info(request)

    def update_client_network_with_http_info(self, request):
        all_params = ['instance_id', 'update_client_network_request']
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
            resource_path='/v3/{project_id}/instances/{instance_id}/client-network',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateClientNetworkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_configuration_async(self, request):
        """修改参数模板参数

        修改参数模板参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateConfigurationResponse`
        """
        return self.update_configuration_with_http_info(request)

    def update_configuration_with_http_info(self, request):
        all_params = ['config_id', 'update_configuration_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def update_instance_configuration_async(self, request):
        """修改指定实例的参数

        修改指定实例的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceConfiguration
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceConfigurationRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceConfigurationResponse`
        """
        return self.update_instance_configuration_with_http_info(request)

    def update_instance_configuration_with_http_info(self, request):
        all_params = ['instance_id', 'update_instance_configuration_request_body']
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

    def update_instance_name_async(self, request):
        """修改实例名称

        修改实例名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInstanceName
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceNameRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateInstanceNameResponse`
        """
        return self.update_instance_name_with_http_info(request)

    def update_instance_name_with_http_info(self, request):
        all_params = ['instance_id', 'update_instance_name_request_body']
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

    def update_security_group_async(self, request):
        """变更实例安全组

        变更实例关联的安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSecurityGroup
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpdateSecurityGroupResponse`
        """
        return self.update_security_group_with_http_info(request)

    def update_security_group_with_http_info(self, request):
        all_params = ['instance_id', 'update_security_group_request_body']
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
            response_type='UpdateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_db_version_async(self, request):
        """数据库补丁升级

        升级数据库补丁版本
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeDbVersion
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.UpgradeDbVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.UpgradeDbVersionResponse`
        """
        return self.upgrade_db_version_with_http_info(request)

    def upgrade_db_version_with_http_info(self, request):
        all_params = ['instance_id']
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

        form_params = {}

        body_params = None
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
            response_type='UpgradeDbVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_version_async(self, request):
        """查询当前支持的API版本信息列表

        查询当前支持的API版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ListApiVersionResponse`
        """
        return self.list_api_version_with_http_info(request)

    def list_api_version_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListApiVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_version_async(self, request):
        """查询指定API版本信息

        查询指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.ShowApiVersionResponse`
        """
        return self.show_api_version_with_http_info(request)

    def show_api_version_with_http_info(self, request):
        all_params = ['version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/{version}',
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

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


class SdrsAsyncClient(Client):
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
        super(SdrsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksdrs.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "SdrsClient":
            raise TypeError("client type error, support client type is SdrsClient")

        return ClientBuilder(clazz)

    def add_protected_instance_nic_async(self, request):
        """保护实例添加网卡

        给指定的保护实例添加网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddProtectedInstanceNic
        :type request: :class:`huaweicloudsdksdrs.v1.AddProtectedInstanceNicRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.AddProtectedInstanceNicResponse`
        """
        return self.add_protected_instance_nic_with_http_info(request)

    def add_protected_instance_nic_with_http_info(self, request):
        all_params = ['protected_instance_id', 'protected_instance_add_nic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/nic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddProtectedInstanceNicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_protected_instance_tags_async(self, request):
        """添加保护实例标签

        一个保护实例上最多有10个标签。此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddProtectedInstanceTags
        :type request: :class:`huaweicloudsdksdrs.v1.AddProtectedInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.AddProtectedInstanceTagsResponse`
        """
        return self.add_protected_instance_tags_with_http_info(request)

    def add_protected_instance_tags_with_http_info(self, request):
        all_params = ['protected_instance_id', 'protected_instance_add_tags_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/tags',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddProtectedInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def attach_protected_instance_replication_async(self, request):
        """保护实例挂载复制对

        将指定的复制对挂载到指定的保护实例上。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachProtectedInstanceReplication
        :type request: :class:`huaweicloudsdksdrs.v1.AttachProtectedInstanceReplicationRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.AttachProtectedInstanceReplicationResponse`
        """
        return self.attach_protected_instance_replication_with_http_info(request)

    def attach_protected_instance_replication_with_http_info(self, request):
        all_params = ['protected_instance_id', 'protected_instance_attach_replication_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/attachreplication',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AttachProtectedInstanceReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_tags_async(self, request):
        """批量添加保护实例标签

        为指定保护实例批量添加或删除标签。一个资源上最多有10个标签。
        此接口为幂等接口：
        创建时如果请求体中存在重复key则报错。
        创建时，不允许设置重复key数据,如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddTags
        :type request: :class:`huaweicloudsdksdrs.v1.BatchAddTagsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.BatchAddTagsResponse`
        """
        return self.batch_add_tags_with_http_info(request)

    def batch_add_tags_with_http_info(self, request):
        all_params = ['protected_instance_id', 'batch_add_or_delete_tags_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_create_protected_instances_async(self, request):
        """批量创建保护实例

        典型场景：没有特殊操作场景
        接口功能：批量创建保护实例。保护实例创建完成后，系统默认容灾站点云服务器名称与生产站点云服务器名称相同，但ID不同。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateProtectedInstances
        :type request: :class:`huaweicloudsdksdrs.v1.BatchCreateProtectedInstancesRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.BatchCreateProtectedInstancesResponse`
        """
        return self.batch_create_protected_instances_with_http_info(request)

    def batch_create_protected_instances_with_http_info(self, request):
        all_params = ['batch_create_protected_instances_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/batch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateProtectedInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_protected_instances_async(self, request):
        """批量删除保护实例

        典型场景：没有特殊操作场景
        接口功能：批量删除保护实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteProtectedInstances
        :type request: :class:`huaweicloudsdksdrs.v1.BatchDeleteProtectedInstancesRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.BatchDeleteProtectedInstancesResponse`
        """
        return self.batch_delete_protected_instances_with_http_info(request)

    def batch_delete_protected_instances_with_http_info(self, request):
        all_params = ['batch_delete_protected_instances_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteProtectedInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_tags_async(self, request):
        """批量删除保护实例标签

        为指定保护实例批量删除标签。一个资源上最多有10个标签。
        此接口为幂等接口：
        删除时，如果删除的标签不存在，默认处理成功,删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdksdrs.v1.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.BatchDeleteTagsResponse`
        """
        return self.batch_delete_tags_with_http_info(request)

    def batch_delete_tags_with_http_info(self, request):
        all_params = ['protected_instance_id', 'batch_add_or_delete_tags_request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/tags/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_disaster_recovery_drill_async(self, request):
        """创建容灾演练

        创建容灾演练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDisasterRecoveryDrill
        :type request: :class:`huaweicloudsdksdrs.v1.CreateDisasterRecoveryDrillRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.CreateDisasterRecoveryDrillResponse`
        """
        return self.create_disaster_recovery_drill_with_http_info(request)

    def create_disaster_recovery_drill_with_http_info(self, request):
        all_params = ['create_disaster_recovery_drill_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/disaster-recovery-drills',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDisasterRecoveryDrillResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_protected_instance_async(self, request):
        """创建保护实例

        创建保护实例。保护实例创建完成后，系统默认容灾站点云服务器名称与生产站点云服务器名称相同，但ID不同。如果需要修改云服务器名称，请在保护实例详情页面单击云服务器名称，进入云服务器详情页面进行修改
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProtectedInstance
        :type request: :class:`huaweicloudsdksdrs.v1.CreateProtectedInstanceRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.CreateProtectedInstanceResponse`
        """
        return self.create_protected_instance_with_http_info(request)

    def create_protected_instance_with_http_info(self, request):
        all_params = ['create_protected_instance_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProtectedInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_protection_group_async(self, request):
        """创建保护组

        创建保护组。
        说明：
        本接口为异步接口，调用成功只是表示请求下发，创建结果需要通过“查询job状态”接口获取
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.CreateProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.CreateProtectionGroupResponse`
        """
        return self.create_protection_group_with_http_info(request)

    def create_protection_group_with_http_info(self, request):
        all_params = ['create_protection_group_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/server-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_replication_async(self, request):
        """创建复制对

        创建复制对，并将其添加到指定的保护组中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateReplication
        :type request: :class:`huaweicloudsdksdrs.v1.CreateReplicationRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.CreateReplicationResponse`
        """
        return self.create_replication_with_http_info(request)

    def create_replication_with_http_info(self, request):
        all_params = ['create_replication_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/replications',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_all_server_group_failure_jobs_async(self, request):
        """删除所有保护组失败任务

        删除所有保护组层级的失败任务，创建、删除保护组失败等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAllServerGroupFailureJobs
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteAllServerGroupFailureJobsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteAllServerGroupFailureJobsResponse`
        """
        return self.delete_all_server_group_failure_jobs_with_http_info(request)

    def delete_all_server_group_failure_jobs_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task-center/failure-jobs/batch',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAllServerGroupFailureJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_disaster_recovery_drill_async(self, request):
        """删除容灾演练

        删除指定的容灾演练。删除后：
        容灾演练服务器、容灾演练服务器上挂载的磁盘和网卡将被一并删除。
        演练VPC、演练VPC的子网不会被删除。您可以继续使用该VPC创建其他云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDisasterRecoveryDrill
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteDisasterRecoveryDrillRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteDisasterRecoveryDrillResponse`
        """
        return self.delete_disaster_recovery_drill_with_http_info(request)

    def delete_disaster_recovery_drill_with_http_info(self, request):
        all_params = ['disaster_recovery_drill_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_drill_id' in local_var_params:
            path_params['disaster_recovery_drill_id'] = local_var_params['disaster_recovery_drill_id']

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
            resource_path='/v1/{project_id}/disaster-recovery-drills/{disaster_recovery_drill_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDisasterRecoveryDrillResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_failure_job_async(self, request):
        """删除单个失败任务

        删除单个失败任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFailureJob
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteFailureJobRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteFailureJobResponse`
        """
        return self.delete_failure_job_with_http_info(request)

    def delete_failure_job_with_http_info(self, request):
        all_params = ['failure_job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'failure_job_id' in local_var_params:
            path_params['failure_job_id'] = local_var_params['failure_job_id']

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
            resource_path='/v1/{project_id}/task-center/failure-jobs/{failure_job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteFailureJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_protected_instance_async(self, request):
        """删除保护实例

        删除指定的保护实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectedInstance
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteProtectedInstanceRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteProtectedInstanceResponse`
        """
        return self.delete_protected_instance_with_http_info(request)

    def delete_protected_instance_with_http_info(self, request):
        all_params = ['protected_instance_id', 'delete_protected_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProtectedInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_protected_instance_nic_async(self, request):
        """保护实例删除网卡

        删除指定保护实例的指定网卡。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectedInstanceNic
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteProtectedInstanceNicRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteProtectedInstanceNicResponse`
        """
        return self.delete_protected_instance_nic_with_http_info(request)

    def delete_protected_instance_nic_with_http_info(self, request):
        all_params = ['protected_instance_id', 'protected_instance_delete_nic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/nic/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProtectedInstanceNicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_protected_instance_tag_async(self, request):
        """删除保护实例标签

        幂等接口：删除时，不对标签字符集做校验，调用接口前必须要做encodeURI，服务端需要对接口URI做decodeURI。
         说明:请自行选择工具执行URI编码。
        删除的key不存在报404，Key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectedInstanceTag
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteProtectedInstanceTagRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteProtectedInstanceTagResponse`
        """
        return self.delete_protected_instance_tag_with_http_info(request)

    def delete_protected_instance_tag_with_http_info(self, request):
        all_params = ['protected_instance_id', 'key']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/tags/{key}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProtectedInstanceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_protection_group_async(self, request):
        """删除保护组

        删除指定的保护组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteProtectionGroupResponse`
        """
        return self.delete_protection_group_with_http_info(request)

    def delete_protection_group_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/server-groups/{server_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_replication_async(self, request):
        """删除复制对

        删除指定的复制对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteReplication
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteReplicationRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteReplicationResponse`
        """
        return self.delete_replication_with_http_info(request)

    def delete_replication_with_http_info(self, request):
        all_params = ['replication_id', 'delete_replication_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replication_id'] = local_var_params['replication_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/replications/{replication_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_server_group_failure_jobs_async(self, request):
        """删除指定保护组内的所有失败任务

        删除指定保护组内的所有失败任务，创建保护实例失败、创建复制对失败、删除保护实例失败、删除复制对失败等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServerGroupFailureJobs
        :type request: :class:`huaweicloudsdksdrs.v1.DeleteServerGroupFailureJobsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DeleteServerGroupFailureJobsResponse`
        """
        return self.delete_server_group_failure_jobs_with_http_info(request)

    def delete_server_group_failure_jobs_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/task-center/{server_group_id}/failure-jobs/batch',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteServerGroupFailureJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detach_protected_instance_replication_async(self, request):
        """保护实例卸载复制对

        将指定的复制对从指定的保护实例上卸载。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachProtectedInstanceReplication
        :type request: :class:`huaweicloudsdksdrs.v1.DetachProtectedInstanceReplicationRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.DetachProtectedInstanceReplicationResponse`
        """
        return self.detach_protected_instance_replication_with_http_info(request)

    def detach_protected_instance_replication_with_http_info(self, request):
        all_params = ['protected_instance_id', 'replication_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']
        if 'replication_id' in local_var_params:
            path_params['replication_id'] = local_var_params['replication_id']

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
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/detachreplication/{replication_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetachProtectedInstanceReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def expand_replication_async(self, request):
        """复制对扩容

        对复制对包含的两个磁盘进行扩容操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandReplication
        :type request: :class:`huaweicloudsdksdrs.v1.ExpandReplicationRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ExpandReplicationResponse`
        """
        return self.expand_replication_with_http_info(request)

    def expand_replication_with_http_info(self, request):
        all_params = ['replication_id', 'extend_replication_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replication_id'] = local_var_params['replication_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/replications/{replication_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExpandReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_active_active_domains_async(self, request):
        """查询双活域

        查询双活域。双活域由本端存储设备、远端存储设备组成，通过双活域，应用服务器可以实现跨站点的数据访问。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListActiveActiveDomains
        :type request: :class:`huaweicloudsdksdrs.v1.ListActiveActiveDomainsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListActiveActiveDomainsResponse`
        """
        return self.list_active_active_domains_with_http_info(request)

    def list_active_active_domains_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/active-domains',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListActiveActiveDomainsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_disaster_recovery_drills_async(self, request):
        """查询容灾演练列表

        查询指定保护组下的所有容灾演练列表，当未指定保护组时查询当前租户下的所有容灾演练列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDisasterRecoveryDrills
        :type request: :class:`huaweicloudsdksdrs.v1.ListDisasterRecoveryDrillsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListDisasterRecoveryDrillsResponse`
        """
        return self.list_disaster_recovery_drills_with_http_info(request)

    def list_disaster_recovery_drills_with_http_info(self, request):
        all_params = ['server_group_id', 'name', 'status', 'drill_vpc_id', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'drill_vpc_id' in local_var_params:
            query_params.append(('drill_vpc_id', local_var_params['drill_vpc_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v1/{project_id}/disaster-recovery-drills',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDisasterRecoveryDrillsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_failure_jobs_async(self, request):
        """查询失败任务列表

        查询所有保护组失败任务列表或者指定保护组下的所有失败任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFailureJobs
        :type request: :class:`huaweicloudsdksdrs.v1.ListFailureJobsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListFailureJobsResponse`
        """
        return self.list_failure_jobs_with_http_info(request)

    def list_failure_jobs_with_http_info(self, request):
        all_params = ['failure_status', 'resource_name', 'server_group_id', 'resource_type', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'failure_status' in local_var_params:
            query_params.append(('failure_status', local_var_params['failure_status']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v1/{project_id}/task-center/failure-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFailureJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protected_instance_tags_async(self, request):
        """查询保护实例标签

        查询指定保护实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectedInstanceTags
        :type request: :class:`huaweicloudsdksdrs.v1.ListProtectedInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListProtectedInstanceTagsResponse`
        """
        return self.list_protected_instance_tags_with_http_info(request)

    def list_protected_instance_tags_with_http_info(self, request):
        all_params = ['protected_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectedInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protected_instances_async(self, request):
        """查询保护实例列表

        查询当前租户下的所有保护实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectedInstances
        :type request: :class:`huaweicloudsdksdrs.v1.ListProtectedInstancesRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListProtectedInstancesResponse`
        """
        return self.list_protected_instances_with_http_info(request)

    def list_protected_instances_with_http_info(self, request):
        all_params = ['server_group_id', 'server_group_ids', 'protected_instance_ids', 'limit', 'offset', 'status', 'name', 'query_type', 'availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'server_group_ids' in local_var_params:
            query_params.append(('server_group_ids', local_var_params['server_group_ids']))
        if 'protected_instance_ids' in local_var_params:
            query_params.append(('protected_instance_ids', local_var_params['protected_instance_ids']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

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
            resource_path='/v1/{project_id}/protected-instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectedInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protected_instances_by_tags_async(self, request):
        """通过标签查询保护实例

        使用标签过滤保护实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectedInstancesByTags
        :type request: :class:`huaweicloudsdksdrs.v1.ListProtectedInstancesByTagsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListProtectedInstancesByTagsResponse`
        """
        return self.list_protected_instances_by_tags_with_http_info(request)

    def list_protected_instances_by_tags_with_http_info(self, request):
        all_params = ['list_protected_instances_by_tags_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/resource_instances/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectedInstancesByTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protected_instances_project_tags_async(self, request):
        """查询保护实例项目标签

        查询租户在指定Project中保护实例的所有资源标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectedInstancesProjectTags
        :type request: :class:`huaweicloudsdksdrs.v1.ListProtectedInstancesProjectTagsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListProtectedInstancesProjectTagsResponse`
        """
        return self.list_protected_instances_project_tags_with_http_info(request)

    def list_protected_instances_project_tags_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/protected-instances/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectedInstancesProjectTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_protection_groups_async(self, request):
        """查询保护组列表

        查询当前租户所有的保护组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProtectionGroups
        :type request: :class:`huaweicloudsdksdrs.v1.ListProtectionGroupsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListProtectionGroupsResponse`
        """
        return self.list_protection_groups_with_http_info(request)

    def list_protection_groups_with_http_info(self, request):
        all_params = ['limit', 'offset', 'status', 'name', 'query_type', 'availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

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
            resource_path='/v1/{project_id}/server-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProtectionGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_replications_async(self, request):
        """查询复制对列表

        查询指定保护组下的所有复制对列表，如果不给定指定保护组则查询当前租户下的所有复制对列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListReplications
        :type request: :class:`huaweicloudsdksdrs.v1.ListReplicationsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListReplicationsResponse`
        """
        return self.list_replications_with_http_info(request)

    def list_replications_with_http_info(self, request):
        all_params = ['server_group_id', 'server_group_ids', 'protected_instance_id', 'protected_instance_ids', 'name', 'status', 'limit', 'offset', 'query_type', 'availability_zone']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'server_group_id' in local_var_params:
            query_params.append(('server_group_id', local_var_params['server_group_id']))
        if 'server_group_ids' in local_var_params:
            query_params.append(('server_group_ids', local_var_params['server_group_ids']))
        if 'protected_instance_id' in local_var_params:
            query_params.append(('protected_instance_id', local_var_params['protected_instance_id']))
        if 'protected_instance_ids' in local_var_params:
            query_params.append(('protected_instance_ids', local_var_params['protected_instance_ids']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))

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
            resource_path='/v1/{project_id}/replications',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListReplicationsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rpo_statistics_async(self, request):
        """查询资源的RPO超标趋势记录列表

        查询当前租户大屏显示中，资源的RPO超标趋势记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRpoStatistics
        :type request: :class:`huaweicloudsdksdrs.v1.ListRpoStatisticsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListRpoStatisticsResponse`
        """
        return self.list_rpo_statistics_with_http_info(request)

    def list_rpo_statistics_with_http_info(self, request):
        all_params = ['limit', 'offset', 'start_time', 'end_time', 'resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

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
            resource_path='/v1/{project_id}/resource/rpo-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRpoStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def resize_protected_instance_async(self, request):
        """保护实例变更规格

        变更指定保护实例中弹性云服务器的规格，包括：同时变更生产站点云服务器和容灾站点云服务器的规格。
        仅变更生产站点云服务器的规格，容灾站点云服务器规格不变。
        生产站点云服务器规格不变，仅变更容灾站点云服务器的规格。
        当且仅当待变更规格的云服务器处于关机状态时，才能执行此操作。
         说明：不同规格的云服务器在性能上存在差异，可能会对云服务器上运行的应用产生影响。
        为保证切换/故障切换后云服务器的性能，建议容灾站点服务器的规格（CPU、内存）不低于生产站点云服务器的规格（CPU、内存）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeProtectedInstance
        :type request: :class:`huaweicloudsdksdrs.v1.ResizeProtectedInstanceRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ResizeProtectedInstanceResponse`
        """
        return self.resize_protected_instance_with_http_info(request)

    def resize_protected_instance_with_http_info(self, request):
        all_params = ['protected_instance_id', 'resize_protected_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}/resize',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ResizeProtectedInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_disaster_recovery_drill_async(self, request):
        """查询单个容灾演练详情

        查询单个容灾演练的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDisasterRecoveryDrill
        :type request: :class:`huaweicloudsdksdrs.v1.ShowDisasterRecoveryDrillRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowDisasterRecoveryDrillResponse`
        """
        return self.show_disaster_recovery_drill_with_http_info(request)

    def show_disaster_recovery_drill_with_http_info(self, request):
        all_params = ['disaster_recovery_drill_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_drill_id' in local_var_params:
            path_params['disaster_recovery_drill_id'] = local_var_params['disaster_recovery_drill_id']

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
            resource_path='/v1/{project_id}/disaster-recovery-drills/{disaster_recovery_drill_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDisasterRecoveryDrillResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_protected_instance_async(self, request):
        """查询单个保护实例详情

        查询单个保护实例的详细信息，如名称、ID等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProtectedInstance
        :type request: :class:`huaweicloudsdksdrs.v1.ShowProtectedInstanceRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowProtectedInstanceResponse`
        """
        return self.show_protected_instance_with_http_info(request)

    def show_protected_instance_with_http_info(self, request):
        all_params = ['protected_instance_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProtectedInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_protection_group_async(self, request):
        """查询保护组详情

        查询单个保护组的详细信息，如ID、名称等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.ShowProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowProtectionGroupResponse`
        """
        return self.show_protection_group_with_http_info(request)

    def show_protection_group_with_http_info(self, request):
        all_params = ['server_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            resource_path='/v1/{project_id}/server-groups/{server_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quota_async(self, request):
        """查询租户配额

        查询资源的配额相关信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuota
        :type request: :class:`huaweicloudsdksdrs.v1.ShowQuotaRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowQuotaResponse`
        """
        return self.show_quota_with_http_info(request)

    def show_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/sdrs/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_replication_async(self, request):
        """查询单个复制对详情

        查询单个复制对的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReplication
        :type request: :class:`huaweicloudsdksdrs.v1.ShowReplicationRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowReplicationResponse`
        """
        return self.show_replication_with_http_info(request)

    def show_replication_with_http_info(self, request):
        all_params = ['replication_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replication_id'] = local_var_params['replication_id']

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
            resource_path='/v1/{project_id}/replications/{replication_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowReplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_failover_protection_group_async(self, request):
        """保护组故障切换

        当保护组的生产站点发生故障时，将保护组的生产站点切到当前的容灾站点，即另一端AZ，启用当前容灾站点的云硬盘以及云服务器等资源。
        故障切换完成之后，保护组的当前生产站点变成故障切换发生之前的容灾站点，且生产站点和容灾站点之间的数据已停止保护，必须调用5.4.6-保护组开启保护/重保护接口成功后，两端的数据才会重新被保护。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartFailoverProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.StartFailoverProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.StartFailoverProtectionGroupResponse`
        """
        return self.start_failover_protection_group_with_http_info(request)

    def start_failover_protection_group_with_http_info(self, request):
        all_params = ['server_group_id', 'failover_protection_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartFailoverProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_protection_group_async(self, request):
        """保护组开启保护/重保护

        对某一个保护组的“开启保护”或“重保护”操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.StartProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.StartProtectionGroupResponse`
        """
        return self.start_protection_group_with_http_info(request)

    def start_protection_group_with_http_info(self, request):
        all_params = ['server_group_id', 'start_protection_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_reverse_protection_group_async(self, request):
        """保护组切换

        对保护组进行切换操作，可以将保护组的当前生产站点，从创建保护组时指定的生产站点切换到创建保护组时指定的容灾站点，也可以从创建保护组时指定的容灾站点切换到创建保护组时指定的生产站点。切换后，生产站点和容灾站点的数据仍然处于被保护状态，只是复制方向与操作之前相反。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartReverseProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.StartReverseProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.StartReverseProtectionGroupResponse`
        """
        return self.start_reverse_protection_group_with_http_info(request)

    def start_reverse_protection_group_with_http_info(self, request):
        all_params = ['server_group_id', 'reverse_protection_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartReverseProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_protection_group_async(self, request):
        """保护组停止保护

        对某一个保护组的停止保护操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopProtectionGroup
        :type request: :class:`huaweicloudsdksdrs.v1.StopProtectionGroupRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.StopProtectionGroupResponse`
        """
        return self.stop_protection_group_with_http_info(request)

    def stop_protection_group_with_http_info(self, request):
        all_params = ['server_group_id', 'stop_protection_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/server-groups/{server_group_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopProtectionGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_disaster_recovery_drill_name_async(self, request):
        """更新容灾演练名称

        更新容灾演练的名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDisasterRecoveryDrillName
        :type request: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameResponse`
        """
        return self.update_disaster_recovery_drill_name_with_http_info(request)

    def update_disaster_recovery_drill_name_with_http_info(self, request):
        all_params = ['disaster_recovery_drill_id', 'update_disaster_recovery_drill_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'disaster_recovery_drill_id' in local_var_params:
            path_params['disaster_recovery_drill_id'] = local_var_params['disaster_recovery_drill_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/disaster-recovery-drills/{disaster_recovery_drill_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDisasterRecoveryDrillNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_protected_instance_name_async(self, request):
        """更新保护实例名称

        更新某一个保护实例的名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProtectedInstanceName
        :type request: :class:`huaweicloudsdksdrs.v1.UpdateProtectedInstanceNameRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateProtectedInstanceNameResponse`
        """
        return self.update_protected_instance_name_with_http_info(request)

    def update_protected_instance_name_with_http_info(self, request):
        all_params = ['protected_instance_id', 'update_protected_instance_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'protected_instance_id' in local_var_params:
            path_params['protected_instance_id'] = local_var_params['protected_instance_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/protected-instances/{protected_instance_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProtectedInstanceNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_protection_group_name_async(self, request):
        """更新保护组名称

        更新某一个保护组的名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateProtectionGroupName
        :type request: :class:`huaweicloudsdksdrs.v1.UpdateProtectionGroupNameRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateProtectionGroupNameResponse`
        """
        return self.update_protection_group_name_with_http_info(request)

    def update_protection_group_name_with_http_info(self, request):
        all_params = ['server_group_id', 'update_protection_group_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_group_id' in local_var_params:
            path_params['server_group_id'] = local_var_params['server_group_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/server-groups/{server_group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProtectionGroupNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_replication_name_async(self, request):
        """更新复制对名称

        更新复制对名称。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateReplicationName
        :type request: :class:`huaweicloudsdksdrs.v1.UpdateReplicationNameRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateReplicationNameResponse`
        """
        return self.update_replication_name_with_http_info(request)

    def update_replication_name_with_http_info(self, request):
        all_params = ['replication_id', 'update_replication_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'replication_id' in local_var_params:
            path_params['replication_id'] = local_var_params['replication_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/replications/{replication_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateReplicationNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_api_versions_async(self, request):
        """查询API版本信息

        查询存储容灾当前所有可用的版本信息列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdksdrs.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ListApiVersionsResponse`
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
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
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_specified_api_version_async(self, request):
        """查询指定API版本信息

        查询存储容灾指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSpecifiedApiVersion
        :type request: :class:`huaweicloudsdksdrs.v1.ShowSpecifiedApiVersionRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowSpecifiedApiVersionResponse`
        """
        return self.show_specified_api_version_with_http_info(request)

    def show_specified_api_version_with_http_info(self, request):
        all_params = ['api_version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'api_version' in local_var_params:
            path_params['api_version'] = local_var_params['api_version']

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
            resource_path='/{api_version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSpecifiedApiVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_status_async(self, request):
        """查询job状态

        查询job的执行状态。
        对于创建保护组、删除保护组、创建保护实例、删除保护实例、创建复制对、删除复制对等异步API，命令下发后，会返回job_id，通过job_id可以查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobStatus
        :type request: :class:`huaweicloudsdksdrs.v1.ShowJobStatusRequest`
        :rtype: :class:`huaweicloudsdksdrs.v1.ShowJobStatusResponse`
        """
        return self.show_job_status_with_http_info(request)

    def show_job_status_with_http_info(self, request):
        all_params = ['job_id']
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

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobStatusResponse',
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

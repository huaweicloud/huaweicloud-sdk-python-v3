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


class DbssClient(Client):
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
        super(DbssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdbss.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DbssClient":
            raise TypeError("client type error, support client type is DbssClient")

        return ClientBuilder(clazz)

    def add_rds_no_agent_database(self, request):
        """添加RDS免agent数据库

        添加RDS免agent数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRdsNoAgentDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseResponse`
        """
        return self.add_rds_no_agent_database_with_http_info(request)

    def add_rds_no_agent_database_with_http_info(self, request):
        all_params = ['instance_id', 'add_rds_no_agent_database_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/databases/rds',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddRdsNoAgentDatabaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_resource_tag(self, request):
        """批量添加资源标签

        批量添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagResponse`
        """
        return self.batch_add_resource_tag_with_http_info(request)

    def batch_add_resource_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'batch_add_resource_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags/create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchAddResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_resource_tag(self, request):
        """批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagResponse`
        """
        return self.batch_delete_resource_tag_with_http_info(request)

    def batch_delete_resource_tag_with_http_info(self, request):
        all_params = ['resource_type', 'resource_id', 'batch_delete_resource_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/{project_id}/{resource_type}/{resource_id}/tags/delete',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteResourceTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def count_resource_instance_by_tag(self, request):
        """根据标签查询资源实例数量

        根据标签查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagResponse`
        """
        return self.count_resource_instance_by_tag_with_http_info(request)

    def count_resource_instance_by_tag_with_http_info(self, request):
        all_params = ['resource_type', 'count_resource_instance_by_tag_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1/{project_id}/{resource_type}/resource-instances/count',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CountResourceInstanceByTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instances_period_order(self, request):
        """包年包月计费模式创建审计实例

        包年包月计费模式创建审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstancesPeriodOrder
        :type request: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderResponse`
        """
        return self.create_instances_period_order_with_http_info(request)

    def create_instances_period_order_with_http_info(self, request):
        all_params = ['create_instances_period_order_request_body']
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
            resource_path='/v2/{project_id}/dbss/audit/charge/period/order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstancesPeriodOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_databases(self, request):
        """查询数据库列表

        查询数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditDatabases
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesResponse`
        """
        return self.list_audit_databases_with_http_info(request)

    def list_audit_databases_with_http_info(self, request):
        all_params = ['instance_id', 'status', 'offset', 'limit']
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/databases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditDatabasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_instance_jobs(self, request):
        """查询实例创建任务信息

        查询实例创建任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstanceJobs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsResponse`
        """
        return self.list_audit_instance_jobs_with_http_info(request)

    def list_audit_instance_jobs_with_http_info(self, request):
        all_params = ['resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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
            resource_path='/v1/{project_id}/dbss/audit/jobs/{resource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditInstanceJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_instances(self, request):
        """查询审计实例列表

        查询审计实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstances
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesResponse`
        """
        return self.list_audit_instances_with_http_info(request)

    def list_audit_instances_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/dbss/audit/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_operate_logs(self, request):
        """查询用户操作日志信息

        查询用户操作日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditOperateLogs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsResponse`
        """
        return self.list_audit_operate_logs_with_http_info(request)

    def list_audit_operate_logs_with_http_info(self, request):
        all_params = ['instance_id', 'list_audit_operate_logs_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/operate-log',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditOperateLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_rule_risks(self, request):
        """查询风险规则策略

        查询风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleRisks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksResponse`
        """
        return self.list_audit_rule_risks_with_http_info(request)

    def list_audit_rule_risks_with_http_info(self, request):
        all_params = ['instance_id', 'name', 'risk_levels']
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'risk_levels' in local_var_params:
            query_params.append(('risk_levels', local_var_params['risk_levels']))

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
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/rule/risk',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditRuleRisksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_rule_scopes(self, request):
        """查询审计范围策略列表

        查询审计范围策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleScopes
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesResponse`
        """
        return self.list_audit_rule_scopes_with_http_info(request)

    def list_audit_rule_scopes_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/rule/scopes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditRuleScopesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_audit_sensitive_masks(self, request):
        """查询隐私数据脱敏规则

        查询隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSensitiveMasks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksResponse`
        """
        return self.list_audit_sensitive_masks_with_http_info(request)

    def list_audit_sensitive_masks_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/sensitive/masks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAuditSensitiveMasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_availability_zone_infos(self, request):
        """查询可用区信息

        查询可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZoneInfos
        :type request: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosResponse`
        """
        return self.list_availability_zone_infos_with_http_info(request)

    def list_availability_zone_infos_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/dbss/audit/availability-zone',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAvailabilityZoneInfosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_ecs_specification(self, request):
        """查询ecs服务器规格信息

        查询ecs服务器规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcsSpecification
        :type request: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationResponse`
        """
        return self.list_ecs_specification_with_http_info(request)

    def list_ecs_specification_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/dbss/audit/specification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEcsSpecificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_resource_tags(self, request):
        """查询项目标签

        查询项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectResourceTags
        :type request: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsResponse`
        """
        return self.list_project_resource_tags_with_http_info(request)

    def list_project_resource_tags_with_http_info(self, request):
        all_params = ['resource_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v1/{project_id}/{resource_type}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectResourceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resource_instance_by_tag(self, request):
        """根据标签查询资源实例列表

        根据标签查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagResponse`
        """
        return self.list_resource_instance_by_tag_with_http_info(request)

    def list_resource_instance_by_tag_with_http_info(self, request):
        all_params = ['resource_type', 'list_resource_instance_by_tag_request_body', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v1/{project_id}/{resource_type}/resource-instances/filter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourceInstanceByTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_sql_injection_rules(self, request):
        """查询SQL注入规则策略

        查询SQL注入规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlInjectionRules
        :type request: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesResponse`
        """
        return self.list_sql_injection_rules_with_http_info(request)

    def list_sql_injection_rules_with_http_info(self, request):
        all_params = ['instance_id', 'list_sql_injection_rules_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/rule/sql-injections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSqlInjectionRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_audit_quota(self, request):
        """查询账户配额信息

        查询账户配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditQuota
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaResponse`
        """
        return self.show_audit_quota_with_http_info(request)

    def show_audit_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/dbss/audit/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAuditQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_audit_rule_risk(self, request):
        """查询指定风险规则策略

        查询指定风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditRuleRisk
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskResponse`
        """
        return self.show_audit_rule_risk_with_http_info(request)

    def show_audit_rule_risk_with_http_info(self, request):
        all_params = ['instance_id', 'risk_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'risk_id' in local_var_params:
            path_params['risk_id'] = local_var_params['risk_id']

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
            resource_path='/v1/{project_id}/{instance_id}/dbss/audit/rule/risk/{risk_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAuditRuleRiskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_agent(self, request):
        """开启关闭Agent

        用于开启和关闭agent的功能，当开启后，开始抓取用户的访问信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAgent
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAgentResponse`
        """
        return self.switch_agent_with_http_info(request)

    def switch_agent_with_http_info(self, request):
        all_params = ['instance_id', 'switch_agent_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{instance_id}/audit/agent/switch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchAgentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def switch_risk_rule(self, request):
        """开启关闭风险规则

        开启关闭风险规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchRiskRule
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleResponse`
        """
        return self.switch_risk_rule_with_http_info(request)

    def switch_risk_rule_with_http_info(self, request):
        all_params = ['instance_id', 'switch_risk_rule_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/{instance_id}/audit/rule/risk/switch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SwitchRiskRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_audit_security_group(self, request):
        """修改安全组

        修改安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditSecurityGroup
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupResponse`
        """
        return self.update_audit_security_group_with_http_info(request)

    def update_audit_security_group_with_http_info(self, request):
        all_params = ['update_audit_security_group_request_body']
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
            resource_path='/v1/{project_id}/dbss/audit/security-group',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAuditSecurityGroupResponse',
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

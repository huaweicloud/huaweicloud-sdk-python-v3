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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdbss'")


class DbssAsyncClient(Client):
    def __init__(self):
        super(DbssAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdbss.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DbssAsyncClient":
                raise TypeError("client type error, support client type is DbssAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_rds_no_agent_database_async(self, request):
        """添加RDS免agent数据库

        添加RDS免agent数据库
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRdsNoAgentDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseResponse`
        """
        http_info = self._add_rds_no_agent_database_http_info(request)
        return self._call_api(**http_info)

    def add_rds_no_agent_database_async_invoker(self, request):
        http_info = self._add_rds_no_agent_database_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_rds_no_agent_database_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "AddRdsNoAgentDatabaseResponse"
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

    def batch_add_resource_tag_async(self, request):
        """批量添加资源标签

        批量添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAddResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagResponse`
        """
        http_info = self._batch_add_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_add_resource_tag_async_invoker(self, request):
        http_info = self._batch_add_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_add_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def batch_delete_resource_tag_async(self, request):
        """批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagResponse`
        """
        http_info = self._batch_delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_tag_async_invoker(self, request):
        http_info = self._batch_delete_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_resource_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def count_resource_instance_by_tag_async(self, request):
        """根据标签查询资源实例数量

        根据标签查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagResponse`
        """
        http_info = self._count_resource_instance_by_tag_http_info(request)
        return self._call_api(**http_info)

    def count_resource_instance_by_tag_async_invoker(self, request):
        http_info = self._count_resource_instance_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_resource_instance_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountResourceInstanceByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def create_instances_period_order_async(self, request):
        """包年包月计费模式创建审计实例

        包年包月计费模式创建审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInstancesPeriodOrder
        :type request: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderResponse`
        """
        http_info = self._create_instances_period_order_http_info(request)
        return self._call_api(**http_info)

    def create_instances_period_order_async_invoker(self, request):
        http_info = self._create_instances_period_order_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_instances_period_order_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/dbss/audit/charge/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInstancesPeriodOrderResponse"
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

    def list_audit_databases_async(self, request):
        """查询数据库列表

        查询数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditDatabases
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesResponse`
        """
        http_info = self._list_audit_databases_http_info(request)
        return self._call_api(**http_info)

    def list_audit_databases_async_invoker(self, request):
        http_info = self._list_audit_databases_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_databases_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/databases",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_audit_instance_jobs_async(self, request):
        """查询实例创建任务信息

        查询实例创建任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditInstanceJobs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsResponse`
        """
        http_info = self._list_audit_instance_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instance_jobs_async_invoker(self, request):
        http_info = self._list_audit_instance_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_instance_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/jobs/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInstanceJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def list_audit_instances_async(self, request):
        """查询审计实例列表

        查询审计实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditInstances
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesResponse`
        """
        http_info = self._list_audit_instances_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instances_async_invoker(self, request):
        http_info = self._list_audit_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_instances_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/instances",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditInstancesResponse"
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

    def list_audit_operate_logs_async(self, request):
        """查询用户操作日志信息

        查询用户操作日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditOperateLogs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsResponse`
        """
        http_info = self._list_audit_operate_logs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_operate_logs_async_invoker(self, request):
        http_info = self._list_audit_operate_logs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_operate_logs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/operate-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditOperateLogsResponse"
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

    def list_audit_rule_risks_async(self, request):
        """查询风险规则策略

        查询风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditRuleRisks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksResponse`
        """
        http_info = self._list_audit_rule_risks_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_risks_async_invoker(self, request):
        http_info = self._list_audit_rule_risks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_rule_risks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/risk",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditRuleRisksResponse"
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
        if 'risk_levels' in local_var_params:
            query_params.append(('risk_levels', local_var_params['risk_levels']))

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

    def list_audit_rule_scopes_async(self, request):
        """查询审计范围策略列表

        查询审计范围策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditRuleScopes
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesResponse`
        """
        http_info = self._list_audit_rule_scopes_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_scopes_async_invoker(self, request):
        http_info = self._list_audit_rule_scopes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_rule_scopes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/scopes",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditRuleScopesResponse"
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

    def list_audit_sensitive_masks_async(self, request):
        """查询隐私数据脱敏规则

        查询隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAuditSensitiveMasks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksResponse`
        """
        http_info = self._list_audit_sensitive_masks_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sensitive_masks_async_invoker(self, request):
        http_info = self._list_audit_sensitive_masks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_audit_sensitive_masks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/sensitive/masks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSensitiveMasksResponse"
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

    def list_availability_zone_infos_async(self, request):
        """查询可用区信息

        查询可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailabilityZoneInfos
        :type request: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosResponse`
        """
        http_info = self._list_availability_zone_infos_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zone_infos_async_invoker(self, request):
        http_info = self._list_availability_zone_infos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_availability_zone_infos_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/dbss/audit/availability-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailabilityZoneInfosResponse"
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

    def list_ecs_specification_async(self, request):
        """查询ecs服务器规格信息

        查询ecs服务器规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEcsSpecification
        :type request: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationResponse`
        """
        http_info = self._list_ecs_specification_http_info(request)
        return self._call_api(**http_info)

    def list_ecs_specification_async_invoker(self, request):
        http_info = self._list_ecs_specification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ecs_specification_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/specification",
            "request_type": request.__class__.__name__,
            "response_type": "ListEcsSpecificationResponse"
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

    def list_project_resource_tags_async(self, request):
        """查询项目标签

        查询项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectResourceTags
        :type request: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsResponse`
        """
        http_info = self._list_project_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_resource_tags_async_invoker(self, request):
        http_info = self._list_project_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_resource_instance_by_tag_async(self, request):
        """根据标签查询资源实例列表

        根据标签查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagResponse`
        """
        http_info = self._list_resource_instance_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instance_by_tag_async_invoker(self, request):
        http_info = self._list_resource_instance_by_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_instance_by_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstanceByTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_sql_injection_rules_async(self, request):
        """查询SQL注入规则策略

        查询SQL注入规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSqlInjectionRules
        :type request: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesResponse`
        """
        http_info = self._list_sql_injection_rules_http_info(request)
        return self._call_api(**http_info)

    def list_sql_injection_rules_async_invoker(self, request):
        http_info = self._list_sql_injection_rules_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sql_injection_rules_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/sql-injections",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlInjectionRulesResponse"
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

    def show_audit_quota_async(self, request):
        """查询账户配额信息

        查询账户配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuditQuota
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaResponse`
        """
        http_info = self._show_audit_quota_http_info(request)
        return self._call_api(**http_info)

    def show_audit_quota_async_invoker(self, request):
        http_info = self._show_audit_quota_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_audit_quota_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/dbss/audit/quota",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditQuotaResponse"
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

    def show_audit_rule_risk_async(self, request):
        """查询指定风险规则策略

        查询指定风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAuditRuleRisk
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskResponse`
        """
        http_info = self._show_audit_rule_risk_http_info(request)
        return self._call_api(**http_info)

    def show_audit_rule_risk_async_invoker(self, request):
        http_info = self._show_audit_rule_risk_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_audit_rule_risk_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/dbss/audit/rule/risk/{risk_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuditRuleRiskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def switch_agent_async(self, request):
        """开启关闭Agent

        用于开启和关闭agent的功能，当开启后，开始抓取用户的访问信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchAgent
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAgentResponse`
        """
        http_info = self._switch_agent_http_info(request)
        return self._call_api(**http_info)

    def switch_agent_async_invoker(self, request):
        http_info = self._switch_agent_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_agent_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/agent/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAgentResponse"
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

    def switch_risk_rule_async(self, request):
        """开启关闭风险规则

        开启关闭风险规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SwitchRiskRule
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleResponse`
        """
        http_info = self._switch_risk_rule_http_info(request)
        return self._call_api(**http_info)

    def switch_risk_rule_async_invoker(self, request):
        http_info = self._switch_risk_rule_http_info(request)
        return AsyncInvoker(self, http_info)

    def _switch_risk_rule_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/rule/risk/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchRiskRuleResponse"
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

    def update_audit_security_group_async(self, request):
        """修改安全组

        修改安全组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAuditSecurityGroup
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupResponse`
        """
        http_info = self._update_audit_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_audit_security_group_async_invoker(self, request):
        http_info = self._update_audit_security_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_audit_security_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/security-group",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditSecurityGroupResponse"
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

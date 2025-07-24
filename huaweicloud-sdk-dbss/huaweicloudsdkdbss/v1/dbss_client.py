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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdbss'")


class DbssClient(Client):
    def __init__(self):
        super(DbssClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdbss.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DbssClient":
                raise TypeError("client type error, support client type is DbssClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_audit_database(self, request):
        r"""添加自建数据库

        添加自建数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAuditDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddAuditDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddAuditDatabaseResponse`
        """
        http_info = self._add_audit_database_http_info(request)
        return self._call_api(**http_info)

    def add_audit_database_invoker(self, request):
        http_info = self._add_audit_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_audit_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/databases",
            "request_type": request.__class__.__name__,
            "response_type": "AddAuditDatabaseResponse"
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

    def add_rds_database(self, request):
        r"""添加RDS数据库

        添加RDS数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRdsDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsDatabaseResponse`
        """
        http_info = self._add_rds_database_http_info(request)
        return self._call_api(**http_info)

    def add_rds_database_invoker(self, request):
        http_info = self._add_rds_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rds_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "AddRdsDatabaseResponse"
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

    def add_rds_no_agent_database(self, request):
        r"""添加RDS数据库(V1待下线)

        添加RDS数据库。V1版本已不再维护，待下线。
        请使用V2版本接口（/v2/{project_id}/{instance_id}/audit/databases/rds）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRdsNoAgentDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddRdsNoAgentDatabaseResponse`
        """
        http_info = self._add_rds_no_agent_database_http_info(request)
        return self._call_api(**http_info)

    def add_rds_no_agent_database_invoker(self, request):
        http_info = self._add_rds_no_agent_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rds_no_agent_database_http_info(cls, request):
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

    def create_instances_period_order(self, request):
        r"""包年包月计费模式创建审计实例

        包年包月计费模式创建审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstancesPeriodOrder
        :type request: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CreateInstancesPeriodOrderResponse`
        """
        http_info = self._create_instances_period_order_http_info(request)
        return self._call_api(**http_info)

    def create_instances_period_order_invoker(self, request):
        http_info = self._create_instances_period_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_instances_period_order_http_info(cls, request):
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

    def delete_audit_database(self, request):
        r"""删除数据库

        删除数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditDatabaseResponse`
        """
        http_info = self._delete_audit_database_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_database_invoker(self, request):
        http_info = self._delete_audit_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_database_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/databases/{db_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditDatabaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_id' in local_var_params:
            path_params['db_id'] = local_var_params['db_id']

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

    def delete_instances(self, request):
        r"""删除审计实例

        只有按需计费模式实例没有任务时 或 包周期模式实例状态为故障时，才能执行此操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstances
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteInstancesResponse`
        """
        http_info = self._delete_instances_http_info(request)
        return self._call_api(**http_info)

    def delete_instances_invoker(self, request):
        http_info = self._delete_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_instances_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/dbss/audit/instances",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInstancesResponse"
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

    def list_alarm_topic_config_info(self, request):
        r"""获取实例告警配置

        获取实例告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAlarmTopicConfigInfo
        :type request: :class:`huaweicloudsdkdbss.v1.ListAlarmTopicConfigInfoRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAlarmTopicConfigInfoResponse`
        """
        http_info = self._list_alarm_topic_config_info_http_info(request)
        return self._call_api(**http_info)

    def list_alarm_topic_config_info_invoker(self, request):
        http_info = self._list_alarm_topic_config_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_alarm_topic_config_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/alarm/topic",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlarmTopicConfigInfoResponse"
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

    def list_audit_alarm_log(self, request):
        r"""查询审计告警信息

        查询审计告警信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditAlarmLog
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditAlarmLogRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditAlarmLogResponse`
        """
        http_info = self._list_audit_alarm_log_http_info(request)
        return self._call_api(**http_info)

    def list_audit_alarm_log_invoker(self, request):
        http_info = self._list_audit_alarm_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_alarm_log_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/alarm-log",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditAlarmLogResponse"
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

    def list_audit_databases(self, request):
        r"""查询数据库列表

        查询数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditDatabases
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditDatabasesResponse`
        """
        http_info = self._list_audit_databases_http_info(request)
        return self._call_api(**http_info)

    def list_audit_databases_invoker(self, request):
        http_info = self._list_audit_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_databases_http_info(cls, request):
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

    def list_audit_instance_jobs(self, request):
        r"""查询实例创建任务信息

        查询实例创建任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstanceJobs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstanceJobsResponse`
        """
        http_info = self._list_audit_instance_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instance_jobs_invoker(self, request):
        http_info = self._list_audit_instance_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_instance_jobs_http_info(cls, request):
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

    def list_audit_instances(self, request):
        r"""查询审计实例列表

        查询审计实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditInstances
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditInstancesResponse`
        """
        http_info = self._list_audit_instances_http_info(request)
        return self._call_api(**http_info)

    def list_audit_instances_invoker(self, request):
        http_info = self._list_audit_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_instances_http_info(cls, request):
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

    def list_audit_operate_logs(self, request):
        r"""查询用户操作日志信息

        查询用户操作日志信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditOperateLogs
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditOperateLogsResponse`
        """
        http_info = self._list_audit_operate_logs_http_info(request)
        return self._call_api(**http_info)

    def list_audit_operate_logs_invoker(self, request):
        http_info = self._list_audit_operate_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_operate_logs_http_info(cls, request):
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

    def list_audit_rule_risks(self, request):
        r"""查询风险规则策略

        查询风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleRisks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleRisksResponse`
        """
        http_info = self._list_audit_rule_risks_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_risks_invoker(self, request):
        http_info = self._list_audit_rule_risks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_rule_risks_http_info(cls, request):
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

    def list_audit_rule_scopes(self, request):
        r"""查询审计范围策略列表

        查询审计范围策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditRuleScopes
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditRuleScopesResponse`
        """
        http_info = self._list_audit_rule_scopes_http_info(request)
        return self._call_api(**http_info)

    def list_audit_rule_scopes_invoker(self, request):
        http_info = self._list_audit_rule_scopes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_rule_scopes_http_info(cls, request):
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

    def list_audit_sensitive_masks(self, request):
        r"""查询隐私数据脱敏规则

        查询隐私数据脱敏规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSensitiveMasks
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSensitiveMasksResponse`
        """
        http_info = self._list_audit_sensitive_masks_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sensitive_masks_invoker(self, request):
        http_info = self._list_audit_sensitive_masks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_sensitive_masks_http_info(cls, request):
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

    def list_audit_sqls(self, request):
        r"""查询审计SQL语句

        查询审计SQL语句
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSqls
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSqlsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSqlsResponse`
        """
        http_info = self._list_audit_sqls_http_info(request)
        return self._call_api(**http_info)

    def list_audit_sqls_invoker(self, request):
        http_info = self._list_audit_sqls_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_sqls_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSqlsResponse"
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

    def list_audit_summary_infos(self, request):
        r"""查询审计汇总信息

        查询审计汇总信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditSummaryInfos
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditSummaryInfosRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditSummaryInfosResponse`
        """
        http_info = self._list_audit_summary_infos_http_info(request)
        return self._call_api(**http_info)

    def list_audit_summary_infos_invoker(self, request):
        http_info = self._list_audit_summary_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_summary_infos_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/summary/info",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditSummaryInfosResponse"
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

    def list_availability_zone_infos(self, request):
        r"""查询可用区信息

        查询可用区信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAvailabilityZoneInfos
        :type request: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAvailabilityZoneInfosResponse`
        """
        http_info = self._list_availability_zone_infos_http_info(request)
        return self._call_api(**http_info)

    def list_availability_zone_infos_invoker(self, request):
        http_info = self._list_availability_zone_infos_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_availability_zone_infos_http_info(cls, request):
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

    def list_ecs_specification(self, request):
        r"""查询ECS服务器规格信息

        查询ECS服务器规格信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEcsSpecification
        :type request: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListEcsSpecificationResponse`
        """
        http_info = self._list_ecs_specification_http_info(request)
        return self._call_api(**http_info)

    def list_ecs_specification_invoker(self, request):
        http_info = self._list_ecs_specification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_ecs_specification_http_info(cls, request):
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

    def list_rds_databases(self, request):
        r"""查询RDS数据库列表

        查询RDS数据库列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRdsDatabases
        :type request: :class:`huaweicloudsdkdbss.v1.ListRdsDatabasesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListRdsDatabasesResponse`
        """
        http_info = self._list_rds_databases_http_info(request)
        return self._call_api(**http_info)

    def list_rds_databases_invoker(self, request):
        http_info = self._list_rds_databases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rds_databases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/audit/databases/rds",
            "request_type": request.__class__.__name__,
            "response_type": "ListRdsDatabasesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'db_type' in local_var_params:
            query_params.append(('db_type', local_var_params['db_type']))
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

    def list_sql_injection_rules(self, request):
        r"""查询SQL注入规则策略

        查询SQL注入规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlInjectionRules
        :type request: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListSqlInjectionRulesResponse`
        """
        http_info = self._list_sql_injection_rules_http_info(request)
        return self._call_api(**http_info)

    def list_sql_injection_rules_invoker(self, request):
        http_info = self._list_sql_injection_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_injection_rules_http_info(cls, request):
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

    def reboot_audit_instance(self, request):
        r"""重启审计实例

        重启审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.RebootAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.RebootAuditInstanceResponse`
        """
        http_info = self._reboot_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def reboot_audit_instance_invoker(self, request):
        http_info = self._reboot_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _reboot_audit_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/instance/reboot",
            "request_type": request.__class__.__name__,
            "response_type": "RebootAuditInstanceResponse"
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

    def set_alarm_topic_config_info(self, request):
        r"""设置实例告警配置

        设置实例告警配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SetAlarmTopicConfigInfo
        :type request: :class:`huaweicloudsdkdbss.v1.SetAlarmTopicConfigInfoRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SetAlarmTopicConfigInfoResponse`
        """
        http_info = self._set_alarm_topic_config_info_http_info(request)
        return self._call_api(**http_info)

    def set_alarm_topic_config_info_invoker(self, request):
        http_info = self._set_alarm_topic_config_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _set_alarm_topic_config_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/{instance_id}/audit/alarm/topic",
            "request_type": request.__class__.__name__,
            "response_type": "SetAlarmTopicConfigInfoResponse"
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

    def show_audit_quota(self, request):
        r"""查询账户配额信息

        查询账户配额信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditQuota
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditQuotaResponse`
        """
        http_info = self._show_audit_quota_http_info(request)
        return self._call_api(**http_info)

    def show_audit_quota_invoker(self, request):
        http_info = self._show_audit_quota_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_quota_http_info(cls, request):
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

    def show_audit_rule_risk(self, request):
        r"""查询指定风险规则策略

        查询指定风险规则策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuditRuleRisk
        :type request: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ShowAuditRuleRiskResponse`
        """
        http_info = self._show_audit_rule_risk_http_info(request)
        return self._call_api(**http_info)

    def show_audit_rule_risk_invoker(self, request):
        http_info = self._show_audit_rule_risk_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_audit_rule_risk_http_info(cls, request):
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

    def start_audit_instance(self, request):
        r"""开启审计实例

        开启审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StartAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StartAuditInstanceResponse`
        """
        http_info = self._start_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def start_audit_instance_invoker(self, request):
        http_info = self._start_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_audit_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/instance/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartAuditInstanceResponse"
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

    def stop_audit_instance(self, request):
        r"""关闭审计实例

        关闭审计实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.StopAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.StopAuditInstanceResponse`
        """
        http_info = self._stop_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_audit_instance_invoker(self, request):
        http_info = self._stop_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_audit_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/dbss/audit/instance/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopAuditInstanceResponse"
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

    def switch_audit_database(self, request):
        r"""开启关闭数据库

        开启关闭数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAuditDatabase
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAuditDatabaseRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAuditDatabaseResponse`
        """
        http_info = self._switch_audit_database_http_info(request)
        return self._call_api(**http_info)

    def switch_audit_database_invoker(self, request):
        http_info = self._switch_audit_database_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_audit_database_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/databases/switch",
            "request_type": request.__class__.__name__,
            "response_type": "SwitchAuditDatabaseResponse"
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

    def switch_risk_rule(self, request):
        r"""开启关闭风险规则

        开启关闭风险规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchRiskRule
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchRiskRuleResponse`
        """
        http_info = self._switch_risk_rule_http_info(request)
        return self._call_api(**http_info)

    def switch_risk_rule_invoker(self, request):
        http_info = self._switch_risk_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_risk_rule_http_info(cls, request):
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

    def update_audit_instance(self, request):
        r"""更新审计实例信息

        更新审计实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditInstance
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditInstanceRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditInstanceResponse`
        """
        http_info = self._update_audit_instance_http_info(request)
        return self._call_api(**http_info)

    def update_audit_instance_invoker(self, request):
        http_info = self._update_audit_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_instance_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/dbss/audit/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAuditInstanceResponse"
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

    def update_audit_security_group(self, request):
        r"""修改实例安全组

        修改实例安全组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAuditSecurityGroup
        :type request: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.UpdateAuditSecurityGroupResponse`
        """
        http_info = self._update_audit_security_group_http_info(request)
        return self._call_api(**http_info)

    def update_audit_security_group_invoker(self, request):
        http_info = self._update_audit_security_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_audit_security_group_http_info(cls, request):
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

    def add_audit_agent(self, request):
        r"""添加审计数据库Agent

        添加审计数据库Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.AddAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.AddAuditAgentResponse`
        """
        http_info = self._add_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def add_audit_agent_invoker(self, request):
        http_info = self._add_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_audit_agent_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents",
            "request_type": request.__class__.__name__,
            "response_type": "AddAuditAgentResponse"
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

    def delete_audit_agent(self, request):
        r"""删除数据库Agent

        删除数据库Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.DeleteAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DeleteAuditAgentResponse`
        """
        http_info = self._delete_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def delete_audit_agent_invoker(self, request):
        http_info = self._delete_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_audit_agent_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

        query_params = []
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))

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

    def download_audit_agent(self, request):
        r"""下载审计Agent

        下载审计Agent
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.DownloadAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.DownloadAuditAgentResponse`
        """
        http_info = self._download_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def download_audit_agent_invoker(self, request):
        http_info = self._download_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _download_audit_agent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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

    def list_audit_agent(self, request):
        r"""查询数据库Agent列表

        查询数据库Agent列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuditAgent
        :type request: :class:`huaweicloudsdkdbss.v1.ListAuditAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListAuditAgentResponse`
        """
        http_info = self._list_audit_agent_http_info(request)
        return self._call_api(**http_info)

    def list_audit_agent_invoker(self, request):
        http_info = self._list_audit_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audit_agent_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{instance_id}/audit/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuditAgentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_id' in local_var_params:
            query_params.append(('db_id', local_var_params['db_id']))
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

    def switch_agent(self, request):
        r"""开启关闭Agent

        用于开启和关闭Agent审计的功能，当开启后，开始抓取用户的访问信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SwitchAgent
        :type request: :class:`huaweicloudsdkdbss.v1.SwitchAgentRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.SwitchAgentResponse`
        """
        http_info = self._switch_agent_http_info(request)
        return self._call_api(**http_info)

    def switch_agent_invoker(self, request):
        http_info = self._switch_agent_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _switch_agent_http_info(cls, request):
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

    def batch_add_resource_tag(self, request):
        r"""批量添加资源标签

        批量添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchAddResourceTagResponse`
        """
        http_info = self._batch_add_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_add_resource_tag_invoker(self, request):
        http_info = self._batch_add_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_resource_tag_http_info(cls, request):
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

    def batch_delete_resource_tag(self, request):
        r"""批量删除资源标签

        批量删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteResourceTag
        :type request: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.BatchDeleteResourceTagResponse`
        """
        http_info = self._batch_delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_tag_invoker(self, request):
        http_info = self._batch_delete_resource_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_delete_resource_tag_http_info(cls, request):
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

    def count_resource_instance_by_tag(self, request):
        r"""根据标签查询资源实例数量

        根据标签查询资源实例数量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CountResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.CountResourceInstanceByTagResponse`
        """
        http_info = self._count_resource_instance_by_tag_http_info(request)
        return self._call_api(**http_info)

    def count_resource_instance_by_tag_invoker(self, request):
        http_info = self._count_resource_instance_by_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _count_resource_instance_by_tag_http_info(cls, request):
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

    def list_project_resource_tags(self, request):
        r"""查询项目标签

        查询项目标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectResourceTags
        :type request: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListProjectResourceTagsResponse`
        """
        http_info = self._list_project_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_resource_tags_invoker(self, request):
        http_info = self._list_project_resource_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_resource_tags_http_info(cls, request):
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

    def list_resource_instance_by_tag(self, request):
        r"""根据标签查询资源实例列表

        根据标签查询资源实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceInstanceByTag
        :type request: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagRequest`
        :rtype: :class:`huaweicloudsdkdbss.v1.ListResourceInstanceByTagResponse`
        """
        http_info = self._list_resource_instance_by_tag_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instance_by_tag_invoker(self, request):
        http_info = self._list_resource_instance_by_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_instance_by_tag_http_info(cls, request):
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

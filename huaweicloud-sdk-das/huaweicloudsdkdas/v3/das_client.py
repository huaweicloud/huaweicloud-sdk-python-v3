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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdas'")


class DasClient(Client):
    def __init__(self):
        super(DasClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdas.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DasClient":
                raise TypeError("client type error, support client type is DasClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_api_versions(self, request):
        """查询API版本列表

        查询API版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdas.v3.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_api_versions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/das",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
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
        """查询指定的API版本信息

        查询指定的API版本信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkdas.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowApiVersionResponse`
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
            "resource_path": "/das/{version}",
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

    def cancel_share_connections(self, request):
        """删除共享链接

        删除共享链接，
        用于用户删除共享链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelShareConnections
        :type request: :class:`huaweicloudsdkdas.v3.CancelShareConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CancelShareConnectionsResponse`
        """
        http_info = self._cancel_share_connections_http_info(request)
        return self._call_api(**http_info)

    def cancel_share_connections_invoker(self, request):
        http_info = self._cancel_share_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_share_connections_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/connections/share",
            "request_type": request.__class__.__name__,
            "response_type": "CancelShareConnectionsResponse"
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

    def change_sql_limit_switch_status(self, request):
        """设置SQL限流开关状态

        设置SQL限流开关状态。目前仅支持MySQL数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSqlLimitSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ChangeSqlLimitSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeSqlLimitSwitchStatusResponse`
        """
        http_info = self._change_sql_limit_switch_status_http_info(request)
        return self._call_api(**http_info)

    def change_sql_limit_switch_status_invoker(self, request):
        http_info = self._change_sql_limit_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_sql_limit_switch_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSqlLimitSwitchStatusResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def change_sql_switch(self, request):
        """开启/关闭全量SQL、慢SQL开关

        打开或者关闭DAS收集全量SQL开关，开启后，实例的性能损耗在5%以内。开启全量SQL后，本服务会对SQL的文本内容进行存储，以便进行分析。用户可自行设置全量SQL的保存时间范围，到期后会自动删除；如果未设置，数据默认保留7天。
        打开或者关闭DAS收集慢SQL开关。开启慢SQL后，本服务会对慢SQL的文本内容进行存储，以便进行分析。用户可自行设置慢SQL的保存时间范围，到期后会自动删除；如果未设置，数据默认保留7天。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeSqlSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ChangeSqlSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeSqlSwitchResponse`
        """
        http_info = self._change_sql_switch_http_info(request)
        return self._call_api(**http_info)

    def change_sql_switch_invoker(self, request):
        http_info = self._change_sql_switch_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_sql_switch_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeSqlSwitchResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_share_connections(self, request):
        """设置共享链接

        设置共享链接，
        用于用户添加共享链接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateShareConnections
        :type request: :class:`huaweicloudsdkdas.v3.CreateShareConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateShareConnectionsResponse`
        """
        http_info = self._create_share_connections_http_info(request)
        return self._call_api(**http_info)

    def create_share_connections_invoker(self, request):
        http_info = self._create_share_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_share_connections_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/share",
            "request_type": request.__class__.__name__,
            "response_type": "CreateShareConnectionsResponse"
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

    def create_space_analysis_task(self, request):
        """创建空间分析任务

        创建空间分析任务，如触发重新分析，支持MySQL和GaussDB(for MySQL)引擎
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSpaceAnalysisTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateSpaceAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSpaceAnalysisTaskResponse`
        """
        http_info = self._create_space_analysis_task_http_info(request)
        return self._call_api(**http_info)

    def create_space_analysis_task_invoker(self, request):
        http_info = self._create_space_analysis_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_space_analysis_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSpaceAnalysisTaskResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_sql_limit_rules(self, request):
        """创建SQL限流规则

        添加SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。
        MySQL使用限制如下：
        1.规则举例详细说明：例如关键字是\&quot;select~a\&quot;, 含义为：select以及a为该并发控制所包含的两个关键字，~为关键字间隔符，即若执行SQL命令包含select与a两个关键字视为命中此条并发控制规则。
        2.当SQL语句匹配多条限流规则时，优先生效最新添加的规则，之前的规则不再生效。
        3.限流规则关键字有顺序要求，只会按顺序匹配。如：a~and~b 只会匹配 xxx a&gt;1 and b&gt;2，而不会匹配 xxx b&gt;2 and a&gt;1。
        4.关键字可能大小写敏感，请执行 \&quot;show variables like &#39;rds_sqlfilter_case_sensitive&#39;或者到实例参数设置页面进行确认。
        5.部分版本只读实例不允许设置限流规则，如果要设置限流规则，请到主实例上进行添加。
        6.系统表不限制、不涉及数据查询的不限制、root账号在特定版本下不限制。
        PostgreSQL使用限制如下：
        1.无法添加相同QUERY_ID或SQL语句的规则。
        2.使用SQL语句添加规则时，需要确保存在数据库表，如：select * from test，需要确保数据库中有test表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.CreateSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSqlLimitRulesResponse`
        """
        http_info = self._create_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def create_sql_limit_rules_invoker(self, request):
        http_info = self._create_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSqlLimitRulesResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_tuning(self, request):
        """执行SQL诊断

        执行SQL诊断，
        用于用户执行SQL诊断。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTuning
        :type request: :class:`huaweicloudsdkdas.v3.CreateTuningRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateTuningResponse`
        """
        http_info = self._create_tuning_http_info(request)
        return self._call_api(**http_info)

    def create_tuning_invoker(self, request):
        http_info = self._create_tuning_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tuning_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/tuning/create-tuning",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTuningResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_db_user(self, request):
        """删除数据库用户

        删除注册在DAS里的数据库用户。此接口只是将注册的数据库用户在DAS系统里删除，不会真正删除数据库用户对象。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDbUser
        :type request: :class:`huaweicloudsdkdas.v3.DeleteDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteDbUserResponse`
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
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_user_id' in local_var_params:
            path_params['db_user_id'] = local_var_params['db_user_id']

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

    def delete_process(self, request):
        """查杀会话

        查杀会话。支持按照用户、数据库、会话列表查杀会话，三个条件至少指定一个。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProcess
        :type request: :class:`huaweicloudsdkdas.v3.DeleteProcessRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteProcessResponse`
        """
        http_info = self._delete_process_http_info(request)
        return self._call_api(**http_info)

    def delete_process_invoker(self, request):
        http_info = self._delete_process_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_process_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/process",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProcessResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_sql_limit_rules(self, request):
        """删除SQL限流规则

        删除SQL限流规则。目前仅支持MySQL和PostgreSQL数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.DeleteSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteSqlLimitRulesResponse`
        """
        http_info = self._delete_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def delete_sql_limit_rules_invoker(self, request):
        http_info = self._delete_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSqlLimitRulesResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_slow_query_logs(self, request):
        """导出慢SQL数据

        DAS收集慢SQL开关打开后，一次性导出指定时间范围内的慢SQL数据，支持分页滚动获取。免费实例仅支持查看最近一小时数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowQueryLogs
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowQueryLogsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowQueryLogsResponse`
        """
        http_info = self._export_slow_query_logs_http_info(request)
        return self._call_api(**http_info)

    def export_slow_query_logs_invoker(self, request):
        http_info = self._export_slow_query_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_query_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-query-logs",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowQueryLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def export_slow_sql_statistics(self, request):
        """导出慢SQL统计数据

        慢SQL开关打开后，导出慢SQL统计数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowSqlStatistics
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowSqlStatisticsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowSqlStatisticsResponse`
        """
        http_info = self._export_slow_sql_statistics_http_info(request)
        return self._call_api(**http_info)

    def export_slow_sql_statistics_invoker(self, request):
        http_info = self._export_slow_sql_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_sql_statistics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-sql-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowSqlStatisticsResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def export_slow_sql_templates_details(self, request):
        """导出慢SQL模板列表

        慢SQL开关打开后，导出慢SQL模板列表。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowSqlTemplatesDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTemplatesDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTemplatesDetailsResponse`
        """
        http_info = self._export_slow_sql_templates_details_http_info(request)
        return self._call_api(**http_info)

    def export_slow_sql_templates_details_invoker(self, request):
        http_info = self._export_slow_sql_templates_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_sql_templates_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-sql-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowSqlTemplatesDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
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

    def export_slow_sql_trend_details(self, request):
        """导出慢SQL数量趋势

        慢SQL开关打开后，导出慢SQL数量趋势。免费实例仅支持查看最近一小时数据。查询时间间隔最长一天。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSlowSqlTrendDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTrendDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowSqlTrendDetailsResponse`
        """
        http_info = self._export_slow_sql_trend_details_http_info(request)
        return self._call_api(**http_info)

    def export_slow_sql_trend_details_invoker(self, request):
        http_info = self._export_slow_sql_trend_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_slow_sql_trend_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/slow-sql-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSlowSqlTrendDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
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

    def export_sql_statements(self, request):
        """导出全量SQL

        全量SQL开关打开后，一次性导出指定时间范围内的全量SQL数据，支持分页滚动获取。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportSqlStatements
        :type request: :class:`huaweicloudsdkdas.v3.ExportSqlStatementsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSqlStatementsResponse`
        """
        http_info = self._export_sql_statements_http_info(request)
        return self._call_api(**http_info)

    def export_sql_statements_invoker(self, request):
        http_info = self._export_sql_statements_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_sql_statements_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-statements",
            "request_type": request.__class__.__name__,
            "response_type": "ExportSqlStatementsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def export_top_sql_templates_details(self, request):
        """导出TopSQL模板列表

        TopSQL开关打开后，导出TopSQL模板列表。该功能仅支持付费实例。查询时间间隔最长一小时。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTopSqlTemplatesDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportTopSqlTemplatesDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportTopSqlTemplatesDetailsResponse`
        """
        http_info = self._export_top_sql_templates_details_http_info(request)
        return self._call_api(**http_info)

    def export_top_sql_templates_details_invoker(self, request):
        http_info = self._export_top_sql_templates_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_top_sql_templates_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/top-sql-templates",
            "request_type": request.__class__.__name__,
            "response_type": "ExportTopSqlTemplatesDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))
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

    def export_top_sql_trend_details(self, request):
        """导出SQL执行耗时区间数据

        TopSQL开关打开后，导出SQL执行耗时区间数据。该功能仅支持付费实例。查询时间间隔最长六小时。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportTopSqlTrendDetails
        :type request: :class:`huaweicloudsdkdas.v3.ExportTopSqlTrendDetailsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportTopSqlTrendDetailsResponse`
        """
        http_info = self._export_top_sql_trend_details_http_info(request)
        return self._call_api(**http_info)

    def export_top_sql_trend_details_invoker(self, request):
        http_info = self._export_top_sql_trend_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_top_sql_trend_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/top-sql-trend",
            "request_type": request.__class__.__name__,
            "response_type": "ExportTopSqlTrendDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'start_at' in local_var_params:
            query_params.append(('start_at', local_var_params['start_at']))
        if 'end_at' in local_var_params:
            query_params.append(('end_at', local_var_params['end_at']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))

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

    def list_db_users(self, request):
        """查询数据库用户列表

        查询注册在DAS里的数据库用户列表，后续调用其他接口时(如查询实例会话列表接口)需要用到此接口返回的db_user_id。此接口不会返回数据库实例上的数据库用户对象。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkdas.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDbUsersResponse`
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
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'db_username' in local_var_params:
            query_params.append(('db_username', local_var_params['db_username']))

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

    def list_innodb_locks(self, request):
        """查询InnoDB锁等待列表

        查询InnoDB锁等待列表。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInnodbLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListInnodbLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInnodbLocksResponse`
        """
        http_info = self._list_innodb_locks_http_info(request)
        return self._call_api(**http_info)

    def list_innodb_locks_invoker(self, request):
        http_info = self._list_innodb_locks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_innodb_locks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/innodb-locks",
            "request_type": request.__class__.__name__,
            "response_type": "ListInnodbLocksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))

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

    def list_metadata_locks(self, request):
        """查询元数据锁列表

        查询元数据锁列表。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetadataLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListMetadataLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListMetadataLocksResponse`
        """
        http_info = self._list_metadata_locks_http_info(request)
        return self._call_api(**http_info)

    def list_metadata_locks_invoker(self, request):
        http_info = self._list_metadata_locks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metadata_locks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/metadata-locks",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetadataLocksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'thread_id' in local_var_params:
            query_params.append(('thread_id', local_var_params['thread_id']))
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'table' in local_var_params:
            query_params.append(('table', local_var_params['table']))

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

    def list_processes(self, request):
        """查询实例会话列表

        支持根据数据库、用户查询实例会话列表。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProcesses
        :type request: :class:`huaweicloudsdkdas.v3.ListProcessesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListProcessesResponse`
        """
        http_info = self._list_processes_http_info(request)
        return self._call_api(**http_info)

    def list_processes_invoker(self, request):
        http_info = self._list_processes_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_processes_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/processes",
            "request_type": request.__class__.__name__,
            "response_type": "ListProcessesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'node_id' in local_var_params:
            query_params.append(('node_id', local_var_params['node_id']))
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

    def list_space_analysis(self, request):
        """获取空间分析数据列表

        获取空间分析数据列表。实例级别数据来源于文件系统，库级别和表级别数据来源于information_schema.tables表。空间&amp;元数据分析最多分析10000张表，若缺少库表空间数据，可能是因为数据库实例表个数过多或者账号未保存密码。如果为保存密码，请使用用户管理接口或页面录入数据库账号。支持MySQL和GaussDB(for MySQL)引擎
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSpaceAnalysis
        :type request: :class:`huaweicloudsdkdas.v3.ListSpaceAnalysisRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSpaceAnalysisResponse`
        """
        http_info = self._list_space_analysis_http_info(request)
        return self._call_api(**http_info)

    def list_space_analysis_invoker(self, request):
        http_info = self._list_space_analysis_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_space_analysis_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/space-analysis",
            "request_type": request.__class__.__name__,
            "response_type": "ListSpaceAnalysisResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'database_id' in local_var_params:
            query_params.append(('database_id', local_var_params['database_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'show_instance_info' in local_var_params:
            query_params.append(('show_instance_info', local_var_params['show_instance_info']))
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def list_sql_limit_rules(self, request):
        """查询SQL限流规则列表

        查询SQL限流规则。目前仅支持MySQL和PostgreSQL数据库。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.ListSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSqlLimitRulesResponse`
        """
        http_info = self._list_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def list_sql_limit_rules_invoker(self, request):
        http_info = self._list_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ListSqlLimitRulesResponse"
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
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))
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

    def parse_sql_limit_rules(self, request):
        """根据原始SQL生成SQL限流关键字

        根据原始SQL生成SQL限流关键字，目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.ParseSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ParseSqlLimitRulesResponse`
        """
        http_info = self._parse_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def parse_sql_limit_rules_invoker(self, request):
        http_info = self._parse_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _parse_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/parse",
            "request_type": request.__class__.__name__,
            "response_type": "ParseSqlLimitRulesResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def register_db_user(self, request):
        """注册数据库用户

        此接口是将数据库用户和密码注册进DAS系统，同时会返回一个数据库用户ID ，后续调用其他接口时（如查询实例会话列表接口）需要用到此数据库用户ID。密码为加密存储，且仅用于DAS API相关功能。此接口不会在数据库实例上创建数据库用户对象。请确保输入的用户名和密码是已经存在并且是正确的。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RegisterDbUser
        :type request: :class:`huaweicloudsdkdas.v3.RegisterDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RegisterDbUserResponse`
        """
        http_info = self._register_db_user_http_info(request)
        return self._call_api(**http_info)

    def register_db_user_invoker(self, request):
        http_info = self._register_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _register_db_user_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterDbUserResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_db_user(self, request):
        """查询数据库用户信息

        查询注册在DAS里的数据库用户信息。此接口不能查询数据库实例上的数据库用户对象。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDbUser
        :type request: :class:`huaweicloudsdkdas.v3.ShowDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDbUserResponse`
        """
        http_info = self._show_db_user_http_info(request)
        return self._call_api(**http_info)

    def show_db_user_invoker(self, request):
        http_info = self._show_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_db_user_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_user_id' in local_var_params:
            path_params['db_user_id'] = local_var_params['db_user_id']

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

    def show_quotas(self, request):
        """查询云DBA配额

        查询云DBA配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkdas.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowQuotasResponse`
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

    def show_sql_execution_plan(self, request):
        """查询SQL执行计划

        查询SQL执行计划。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlExecutionPlan
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlExecutionPlanResponse`
        """
        http_info = self._show_sql_execution_plan_http_info(request)
        return self._call_api(**http_info)

    def show_sql_execution_plan_invoker(self, request):
        http_info = self._show_sql_execution_plan_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_execution_plan_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/explain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlExecutionPlanResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'db_user_id' in local_var_params:
            query_params.append(('db_user_id', local_var_params['db_user_id']))
        if 'database' in local_var_params:
            query_params.append(('database', local_var_params['database']))
        if 'sql' in local_var_params:
            query_params.append(('sql', local_var_params['sql']))

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

    def show_sql_explain(self, request):
        """查询SQL执行计划

        查询SQL执行计划。
        目前仅支持MySQL实例。
        补充GET请求，处理超长SQL
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlExplain
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlExplainRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlExplainResponse`
        """
        http_info = self._show_sql_explain_http_info(request)
        return self._call_api(**http_info)

    def show_sql_explain_invoker(self, request):
        http_info = self._show_sql_explain_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_explain_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/explain",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlExplainResponse"
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
            ['application/json'])

        auth_settings = []

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_sql_limit_job_info(self, request):
        """查询SQL限流任务

        查询指定ID的SQL限流任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitJobInfo
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitJobInfoRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitJobInfoResponse`
        """
        http_info = self._show_sql_limit_job_info_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limit_job_info_invoker(self, request):
        http_info = self._show_sql_limit_job_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limit_job_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/job",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitJobInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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

    def show_sql_limit_switch_status(self, request):
        """查看SQL限流开关状态

        查询SQL限流的开关状态。目前仅支持MySQL实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlLimitSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlLimitSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlLimitSwitchStatusResponse`
        """
        http_info = self._show_sql_limit_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_sql_limit_switch_status_invoker(self, request):
        http_info = self._show_sql_limit_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_limit_switch_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlLimitSwitchStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def show_sql_switch_status(self, request):
        """查询全量SQL和慢SQL的开关状态

        查询DAS收集全量SQL和慢SQL的开关状态。该功能仅支持付费实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSqlSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlSwitchStatusResponse`
        """
        http_info = self._show_sql_switch_status_http_info(request)
        return self._call_api(**http_info)

    def show_sql_switch_status_invoker(self, request):
        http_info = self._show_sql_switch_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_sql_switch_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql/switch",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSqlSwitchStatusResponse"
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
        if 'datastore_type' in local_var_params:
            query_params.append(('datastore_type', local_var_params['datastore_type']))

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

    def show_tuning(self, request):
        """获取诊断结果

        获取诊断结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTuning
        :type request: :class:`huaweicloudsdkdas.v3.ShowTuningRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowTuningResponse`
        """
        http_info = self._show_tuning_http_info(request)
        return self._call_api(**http_info)

    def show_tuning_invoker(self, request):
        http_info = self._show_tuning_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_tuning_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/connections/{connection_id}/tuning/{message_id}/show-tuning-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTuningResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_id' in local_var_params:
            path_params['message_id'] = local_var_params['message_id']
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def update_db_user(self, request):
        """修改数据库用户

        修改注册在DAS里的数据库用户名和密码。此接口不会修改数据库实例上的数据库用户对象的用户名和密码。请确保输入的用户名和密码是已经存在并且是正确的。
        目前仅支持MySQL实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDbUser
        :type request: :class:`huaweicloudsdkdas.v3.UpdateDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateDbUserResponse`
        """
        http_info = self._update_db_user_http_info(request)
        return self._call_api(**http_info)

    def update_db_user_invoker(self, request):
        http_info = self._update_db_user_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_db_user_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDbUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']
        if 'db_user_id' in local_var_params:
            path_params['db_user_id'] = local_var_params['db_user_id']

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

    def update_sql_limit_rules(self, request):
        """修改SQL限流规则

        修改SQL限流规则。目前仅支持PostgreSQL数据库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSqlLimitRules
        :type request: :class:`huaweicloudsdkdas.v3.UpdateSqlLimitRulesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateSqlLimitRulesResponse`
        """
        http_info = self._update_sql_limit_rules_http_info(request)
        return self._call_api(**http_info)

    def update_sql_limit_rules_invoker(self, request):
        http_info = self._update_sql_limit_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_sql_limit_rules_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/instances/{instance_id}/sql-limit/rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSqlLimitRulesResponse"
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
            ['application/json'])

        auth_settings = []

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

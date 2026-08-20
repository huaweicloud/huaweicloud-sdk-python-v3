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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkaidatalakejobserver'")


class AIDataLakeJobServerClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkaidatalakejobserver.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "AIDataLakeJobServerClient":
                raise TypeError("client type error, support client type is AIDataLakeJobServerClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def cancel_aura_sql_statement(self, request):
        r"""取消SQL执行

        取消SQL语句执行。 用户可通过该接口取消SQL语句执行，输入为SQL Session id、statement id，返回操作结果。 此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAuraSqlStatement
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.CancelAuraSqlStatementRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.CancelAuraSqlStatementResponse`
        """
        http_info = self._cancel_aura_sql_statement_http_info(request)
        return self._call_api(**http_info)

    def cancel_aura_sql_statement_invoker(self, request):
        http_info = self._cancel_aura_sql_statement_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_aura_sql_statement_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAuraSqlStatementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

    def close_aura_sql_session(self, request):
        r"""关闭Session

        关闭SQL Session。
        用户可通过此接口关闭SQL Session，输入为Session id，返回操作结果。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CloseAuraSqlSession
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.CloseAuraSqlSessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.CloseAuraSqlSessionResponse`
        """
        http_info = self._close_aura_sql_session_http_info(request)
        return self._call_api(**http_info)

    def close_aura_sql_session_invoker(self, request):
        http_info = self._close_aura_sql_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _close_aura_sql_session_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CloseAuraSqlSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

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

    def create_aura_sql_session(self, request):
        r"""创建Session

        创建SQL Session。
        用户通过此接口在指定端点创建SQL Session，通过输入端点id、LakeFormation配置，返回Session信息。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAuraSqlSession
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.CreateAuraSqlSessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.CreateAuraSqlSessionResponse`
        """
        http_info = self._create_aura_sql_session_http_info(request)
        return self._call_api(**http_info)

    def create_aura_sql_session_invoker(self, request):
        http_info = self._create_aura_sql_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_aura_sql_session_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAuraSqlSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def execute_aura_sql_statement(self, request):
        r"""在指定Session中执行SQL

        在指定的Session下执行SQL语句。
        用户可通过此接口执行SQL语句，输入为SQL语句、SQL Session id、绑定参数等信息，返回语句执行结果或statement id。
        此接口支持异步和同步两种执行模式，由入参is_sync参数决定。如果是异步执行，配套使用[查看SQL执行结果](ShowAuraV2SqlStatementResult.xml)接口查询语句结果。
        如果是同步执行，接口会等待一段时间接收结果，如果执行完毕会返回执行结果，如果没有执行完毕，会返回一个运行中状态，后续可以使用[查看SQL执行结果](ShowAuraV2SqlStatementResult.xml)接口查询语句结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteAuraSqlStatement
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ExecuteAuraSqlStatementRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ExecuteAuraSqlStatementResponse`
        """
        http_info = self._execute_aura_sql_statement_http_info(request)
        return self._call_api(**http_info)

    def execute_aura_sql_statement_invoker(self, request):
        http_info = self._execute_aura_sql_statement_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_aura_sql_statement_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/statements",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteAuraSqlStatementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

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

    def list_aura_session_statement_records(self, request):
        r"""查看指定Session下的SQL执行记录

        查询指定Session下的SQL执行记录。
        输入workspace_id，session_id，statement_id（可选），status（可选），分页查询参数limit和marker；输出此会话下SQL执行记录。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuraSessionStatementRecords
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ListAuraSessionStatementRecordsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ListAuraSessionStatementRecordsResponse`
        """
        http_info = self._list_aura_session_statement_records_http_info(request)
        return self._call_api(**http_info)

    def list_aura_session_statement_records_invoker(self, request):
        http_info = self._list_aura_session_statement_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aura_session_statement_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraSessionStatementRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'statement_id' in local_var_params:
            query_params.append(('statement_id', local_var_params['statement_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_aura_sql_sessions(self, request):
        r"""查看Session列表

        查询SQL Session列表。
        输入workspace_id，endpoint_name（可选），status（可选），session_id（可选），start_time（可选），end_time（可选）,分页查询参数limit和marker；输出SQL会话列表，包含会话id、会话创建时间、结束时间、会话状态等信息。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuraSqlSessions
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ListAuraSqlSessionsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ListAuraSqlSessionsResponse`
        """
        http_info = self._list_aura_sql_sessions_http_info(request)
        return self._call_api(**http_info)

    def list_aura_sql_sessions_invoker(self, request):
        http_info = self._list_aura_sql_sessions_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aura_sql_sessions_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraSqlSessionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'session_id' in local_var_params:
            query_params.append(('session_id', local_var_params['session_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def list_aura_statement_records(self, request):
        r"""查看SQL执行记录

        查询SQL执行记录。 查询指定Session下的SQL执行记录。 输入workspace_id，session_id，statement_id（可选），status（可选），分页查询参数limit和marker；输出此会话下SQL执行记录。 此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAuraStatementRecords
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ListAuraStatementRecordsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ListAuraStatementRecordsResponse`
        """
        http_info = self._list_aura_statement_records_http_info(request)
        return self._call_api(**http_info)

    def list_aura_statement_records_invoker(self, request):
        http_info = self._list_aura_statement_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_aura_statement_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-statement-records",
            "request_type": request.__class__.__name__,
            "response_type": "ListAuraStatementRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'endpoint_id' in local_var_params:
            query_params.append(('endpoint_id', local_var_params['endpoint_id']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'session_id' in local_var_params:
            query_params.append(('session_id', local_var_params['session_id']))
        if 'statement_id' in local_var_params:
            query_params.append(('statement_id', local_var_params['statement_id']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
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

    def show_aura_sql_session(self, request):
        r"""查看Session详情

        查询SQL Session信息。
        用户可通过此接口查询SQL Session信息，输入为Session id，返回操作结果。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuraSqlSession
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraSqlSessionRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraSqlSessionResponse`
        """
        http_info = self._show_aura_sql_session_http_info(request)
        return self._call_api(**http_info)

    def show_aura_sql_session_invoker(self, request):
        http_info = self._show_aura_sql_session_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aura_sql_session_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraSqlSessionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def show_aura_sql_statement_result(self, request):
        r"""查看SQL执行结果。

        查询SQL语句执行结果。
        用户可通过该接口查询SQL语句执行结果，输入为SQL Session id、statement id，返回执行结果。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuraSqlStatementResult
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraSqlStatementResultRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraSqlStatementResultResponse`
        """
        http_info = self._show_aura_sql_statement_result_http_info(request)
        return self._call_api(**http_info)

    def show_aura_sql_statement_result_invoker(self, request):
        http_info = self._show_aura_sql_statement_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aura_sql_statement_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraSqlStatementResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

        query_params = []
        if 'page_num' in local_var_params:
            query_params.append(('page_num', local_var_params['page_num']))
        if 'is_enable_obs_path' in local_var_params:
            query_params.append(('is_enable_obs_path', local_var_params['is_enable_obs_path']))

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

    def show_aura_statement_operator_metrics(self, request):
        r"""查看SQL执行算子监控记录

        查看SQL执行算子监控记录。 用户可通过该接口查看SQL执行算子监控记录，输入为SQL Session id、statement id，返回操作结果。 此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuraStatementOperatorMetrics
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraStatementOperatorMetricsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraStatementOperatorMetricsResponse`
        """
        http_info = self._show_aura_statement_operator_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_aura_statement_operator_metrics_invoker(self, request):
        http_info = self._show_aura_statement_operator_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aura_statement_operator_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}/operator-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraStatementOperatorMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

    def show_aura_statement_query_metrics(self, request):
        r"""查看语句监控详情

        查询语句监控详情信息。
        输入workspace_id，session_id，statement_id，输出此会话下SQL监控数据。
        此接口为同步接口，无配套使用接口和特殊场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAuraStatementQueryMetrics
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraStatementQueryMetricsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowAuraStatementQueryMetricsResponse`
        """
        http_info = self._show_aura_statement_query_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_aura_statement_query_metrics_invoker(self, request):
        http_info = self._show_aura_statement_query_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_aura_statement_query_metrics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/aura-sessions/{session_id}/statements/{statement_id}/query-metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAuraStatementQueryMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'session_id' in local_var_params:
            path_params['session_id'] = local_var_params['session_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

    def cancel_spark_job(self, request):
        r"""取消Spark作业执行

        取消正在执行的Spark作业，此接口为同步接口。调用成功后，作业将被终止执行，直接返回取消结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelSparkJob
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.CancelSparkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.CancelSparkJobResponse`
        """
        http_info = self._cancel_spark_job_http_info(request)
        return self._call_api(**http_info)

    def cancel_spark_job_invoker(self, request):
        http_info = self._cancel_spark_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_spark_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def list_spark_jobs(self, request):
        r"""查询Spark作业列表

        查询工作空间下Spark作业列表，此接口为同步接口。支持按作业ID、作业名称、作业状态、作业类型、创建时间等条件过滤查询，支持分页查询，调用成功后直接返回作业列表数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSparkJobs
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkJobsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkJobsResponse`
        """
        http_info = self._list_spark_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_spark_jobs_invoker(self, request):
        http_info = self._list_spark_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_spark_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSparkJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'states' in local_var_params:
            query_params.append(('states', local_var_params['states']))
            collection_formats['states'] = 'multi'
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'create_user_id' in local_var_params:
            query_params.append(('create_user_id', local_var_params['create_user_id']))
        if 'create_user_name' in local_var_params:
            query_params.append(('create_user_name', local_var_params['create_user_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))

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

    def run_spark_job(self, request):
        r"""启动Spark作业

        启动Spark作业，此接口为异步接口。支持Spark Jar作业、Python作业和SQL Script作业。调用该接口后，作业将提交到队列等待执行，返回作业ID后需通过查询作业状态接口确认作业是否成功启动。查询作业状态请参见[查询Spark作业的状态](ShowSparkJobState.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSparkJob
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkJobResponse`
        """
        http_info = self._run_spark_job_http_info(request)
        return self._call_api(**http_info)

    def run_spark_job_invoker(self, request):
        http_info = self._run_spark_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_spark_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_spark_job(self, request):
        r"""查看Spark作业详情

        查看指定Spark作业的详细信息，此接口为同步接口。包括作业ID、作业名称、作业状态、作业配置、资源配置、镜像配置等完整信息，调用成功后直接返回作业详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkJob
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobResponse`
        """
        http_info = self._show_spark_job_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_invoker(self, request):
        http_info = self._show_spark_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def show_spark_job_state(self, request):
        r"""查询Spark作业的状态

        查询Spark作业的状态，此接口为同步接口。可通过作业ID查询Spark作业的当前执行状态，包括排队中、运行中、已成功、已失败等状态，调用后立即返回作业当前状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkJobState
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkJobStateResponse`
        """
        http_info = self._show_spark_job_state_http_info(request)
        return self._call_api(**http_info)

    def show_spark_job_state_invoker(self, request):
        http_info = self._show_spark_job_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_job_state_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-jobs/{job_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkJobStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def show_spark_operator_state(self, request):
        r"""查询Spark异步操作状态

        查询Spark异步操作的执行状态，用于获取异步操作（如重启集群等）的当前状态和执行结果。该接口为同步接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkOperatorState
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkOperatorStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkOperatorStateResponse`
        """
        http_info = self._show_spark_operator_state_http_info(request)
        return self._call_api(**http_info)

    def show_spark_operator_state_invoker(self, request):
        http_info = self._show_spark_operator_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_operator_state_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-operators/{operation_id}/show-state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkOperatorStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'operation_id' in local_var_params:
            path_params['operation_id'] = local_var_params['operation_id']

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

    def cancel_spark_sql(self, request):
        r"""取消SparkSql作业执行

        取消正在运行或排队中的SparkSql作业，此接口为同步接口。只能取消处于QUEUED或RUNNING状态的作业，调用成功后直接返回取消结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelSparkSql
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.CancelSparkSqlRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.CancelSparkSqlResponse`
        """
        http_info = self._cancel_spark_sql_http_info(request)
        return self._call_api(**http_info)

    def cancel_spark_sql_invoker(self, request):
        http_info = self._cancel_spark_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_spark_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSparkSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

    def list_spark_sqls(self, request):
        r"""查询SparkSql作业列表

        查询工作空间下SparkSql作业列表，此接口为同步接口。支持按作业状态、创建时间、SQL片段等条件进行过滤查询，调用成功后直接返回作业列表数据。可通过[查看SparkSql作业详情](ShowSparkSql.xml)接口查看作业详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSparkSqls
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkSqlsRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkSqlsResponse`
        """
        http_info = self._list_spark_sqls_http_info(request)
        return self._call_api(**http_info)

    def list_spark_sqls_invoker(self, request):
        http_info = self._list_spark_sqls_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_spark_sqls_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls",
            "request_type": request.__class__.__name__,
            "response_type": "ListSparkSqlsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'page_reverse' in local_var_params:
            query_params.append(('page_reverse', local_var_params['page_reverse']))
        if 'endpoint_name' in local_var_params:
            query_params.append(('endpoint_name', local_var_params['endpoint_name']))
        if 'statement' in local_var_params:
            query_params.append(('statement', local_var_params['statement']))
        if 'create_time_after' in local_var_params:
            query_params.append(('create_time_after', local_var_params['create_time_after']))
        if 'create_time_before' in local_var_params:
            query_params.append(('create_time_before', local_var_params['create_time_before']))
        if 'states' in local_var_params:
            query_params.append(('states', local_var_params['states']))
            collection_formats['states'] = 'multi'
        if 'statement_types' in local_var_params:
            query_params.append(('statement_types', local_var_params['statement_types']))
            collection_formats['statement_types'] = 'multi'
        if 'statement_id' in local_var_params:
            query_params.append(('statement_id', local_var_params['statement_id']))
        if 'create_user_id' in local_var_params:
            query_params.append(('create_user_id', local_var_params['create_user_id']))
        if 'create_user_name' in local_var_params:
            query_params.append(('create_user_name', local_var_params['create_user_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))

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

    def preview_spark_sql_result(self, request):
        r"""预览SparkSql作业查询结果

        预览SparkSql作业的查询结果，此接口为同步接口。仅适用于执行成功的DQL类型作业，可查看作业返回的数据内容，调用成功后直接返回查询结果数据。可通过[查看SparkSql作业详情](ShowSparkSql.xml)接口查看作业详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PreviewSparkSqlResult
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.PreviewSparkSqlResultRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.PreviewSparkSqlResultResponse`
        """
        http_info = self._preview_spark_sql_result_http_info(request)
        return self._call_api(**http_info)

    def preview_spark_sql_result_invoker(self, request):
        http_info = self._preview_spark_sql_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _preview_spark_sql_result_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}/preview",
            "request_type": request.__class__.__name__,
            "response_type": "PreviewSparkSqlResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

    def restart_spark_sql_cluster(self, request):
        r"""重启SparkSql集群

        重启SparkSql集群，该接口为异步接口，接口调用成功后会返回操作ID（operation_id），您可以通过查询Spark异步操作状态接口查询操作执行结果，详情请参见[查询Spark异步操作状态](ShowSparkOperatorState.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestartSparkSqlCluster
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.RestartSparkSqlClusterRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.RestartSparkSqlClusterResponse`
        """
        http_info = self._restart_spark_sql_cluster_http_info(request)
        return self._call_api(**http_info)

    def restart_spark_sql_cluster_invoker(self, request):
        http_info = self._restart_spark_sql_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restart_spark_sql_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/endpoints/{endpoint_name}/spark-sqls/restart-cluster",
            "request_type": request.__class__.__name__,
            "response_type": "RestartSparkSqlClusterResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'endpoint_name' in local_var_params:
            path_params['endpoint_name'] = local_var_params['endpoint_name']

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

    def run_spark_sql(self, request):
        r"""执行SparkSql作业

        执行SparkSql作业，此接口为异步接口。接口调用成功后会返回作业ID（statement_id）,您可以通过查询作业状态接口查询作业执行结果，详情请参见[查询SparkSql作业的状态](ShowSparkSqlState.xml)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunSparkSql
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkSqlRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.RunSparkSqlResponse`
        """
        http_info = self._run_spark_sql_http_info(request)
        return self._call_api(**http_info)

    def run_spark_sql_invoker(self, request):
        http_info = self._run_spark_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_spark_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls",
            "request_type": request.__class__.__name__,
            "response_type": "RunSparkSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']

        query_params = []

        header_params = {}
        if 'x_client_token' in local_var_params:
            header_params['X-Client-Token'] = local_var_params['x_client_token']

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

    def show_spark_sql(self, request):
        r"""查看SparkSql作业详情

        查看SparkSql作业的详细信息，此接口为同步接口。包括作业状态、SQL内容、执行参数等，调用成功后直接返回作业详细信息。可通过[执行SparkSql作业](RunSparkSql.xml)接口创建作业，通过[查询SparkSql作业列表](ListSparkSqls.xml)接口查询作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkSql
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlResponse`
        """
        http_info = self._show_spark_sql_http_info(request)
        return self._call_api(**http_info)

    def show_spark_sql_invoker(self, request):
        http_info = self._show_spark_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_sql_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkSqlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

    def show_spark_sql_state(self, request):
        r"""查询SparkSql作业的状态

        查询SparkSql作业的状态，此接口为同步接口。可通过查询SparkSql作业列表接口获取statement_id，调用成功后直接返回作业当前状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSparkSqlState
        :type request: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlStateRequest`
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.ShowSparkSqlStateResponse`
        """
        http_info = self._show_spark_sql_state_http_info(request)
        return self._call_api(**http_info)

    def show_spark_sql_state_invoker(self, request):
        http_info = self._show_spark_sql_state_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_spark_sql_state_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/workspaces/{workspace_id}/spark-sqls/{statement_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSparkSqlStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workspace_id' in local_var_params:
            path_params['workspace_id'] = local_var_params['workspace_id']
        if 'statement_id' in local_var_params:
            path_params['statement_id'] = local_var_params['statement_id']

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

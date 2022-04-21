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


class DasClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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
        super(DasClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdas.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DasClient":
            raise TypeError("client type error, support client type is DasClient")

        return ClientBuilder(clazz)

    def list_api_versions(self, request):
        """查询API版本列表

        查询API版本列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkdas.v3.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListApiVersionsResponse`
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/das',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_api_version(self, request):
        """查询指定的API版本信息

        查询指定的API版本信息
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdkdas.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowApiVersionResponse`
        """
        return self.show_api_version_with_http_info(request)

    def show_api_version_with_http_info(self, request):
        all_params = ['version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/das/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApiVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_sql_switch(self, request):
        """开启/关闭全量SQL、慢SQL开关

        打开或者关闭DAS收集全量SQL开关，开启后，实例的性能损耗在5%以内。开启全量SQL后，本服务会对SQL的文本内容进行存储，以便进行分析。用户可自行设置全量SQL的保存时间范围，到期后会自动删除；如果未设置，数据默认保留7天。
        打开或者关闭DAS收集慢SQL开关。开启慢SQL后，本服务会对慢SQL的文本内容进行存储，以便进行分析。用户可自行设置慢SQL的保存时间范围，到期后会自动删除；如果未设置，数据默认保留7天。该功能仅支持付费实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ChangeSqlSwitch
        :type request: :class:`huaweicloudsdkdas.v3.ChangeSqlSwitchRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ChangeSqlSwitchResponse`
        """
        return self.change_sql_switch_with_http_info(request)

    def change_sql_switch_with_http_info(self, request):
        all_params = ['instance_id', 'change_das_switch_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/sql/switch',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeSqlSwitchResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_space_analysis_task(self, request):
        """创建空间分析任务

        创建空间分析任务，如触发重新分析，支持MySQL和GaussDB(for MySQL)引擎
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateSpaceAnalysisTask
        :type request: :class:`huaweicloudsdkdas.v3.CreateSpaceAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.CreateSpaceAnalysisTaskResponse`
        """
        return self.create_space_analysis_task_with_http_info(request)

    def create_space_analysis_task_with_http_info(self, request):
        all_params = ['instance_id', 'create_space_analysis_task_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/space-analysis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSpaceAnalysisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_db_user(self, request):
        """删除数据库用户

        删除注册在DAS里的数据库用户。此接口只是将注册的数据库用户在DAS系统里删除，不会真正删除数据库用户对象。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteDbUser
        :type request: :class:`huaweicloudsdkdas.v3.DeleteDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteDbUserResponse`
        """
        return self.delete_db_user_with_http_info(request)

    def delete_db_user_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_process(self, request):
        """查杀会话

        查杀会话。支持按照用户、数据库、会话列表查杀会话，三个条件至少指定一个。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for DeleteProcess
        :type request: :class:`huaweicloudsdkdas.v3.DeleteProcessRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.DeleteProcessResponse`
        """
        return self.delete_process_with_http_info(request)

    def delete_process_with_http_info(self, request):
        all_params = ['instance_id', 'delete_process_req', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/process',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteProcessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_slow_query_logs(self, request):
        """导出慢SQL数据

        DAS收集慢SQL开关打开后，一次性导出指定时间范围内的慢SQL数据，支持分页滚动获取。该功能仅支持付费实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ExportSlowQueryLogs
        :type request: :class:`huaweicloudsdkdas.v3.ExportSlowQueryLogsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSlowQueryLogsResponse`
        """
        return self.export_slow_query_logs_with_http_info(request)

    def export_slow_query_logs_with_http_info(self, request):
        all_params = ['instance_id', 'datastore_type', 'start_at', 'end_at', 'limit', 'marker', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/slow-query-logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExportSlowQueryLogsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_sql_statements(self, request):
        """导出全量SQL

        全量SQL开关打开后，一次性导出指定时间范围内的全量SQL数据，支持分页滚动获取。该功能仅支持付费实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ExportSqlStatements
        :type request: :class:`huaweicloudsdkdas.v3.ExportSqlStatementsRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ExportSqlStatementsResponse`
        """
        return self.export_sql_statements_with_http_info(request)

    def export_sql_statements_with_http_info(self, request):
        all_params = ['instance_id', 'start_at', 'end_at', 'limit', 'datastore_type', 'marker', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/sql-statements',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExportSqlStatementsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_db_users(self, request):
        """查询数据库用户列表

        查询注册在DAS里的数据库用户列表，后续调用其他接口时(如查询实例会话列表接口)需要用到此接口返回的db_user_id。此接口不会返回数据库实例上的数据库用户对象。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListDbUsers
        :type request: :class:`huaweicloudsdkdas.v3.ListDbUsersRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListDbUsersResponse`
        """
        return self.list_db_users_with_http_info(request)

    def list_db_users_with_http_info(self, request):
        all_params = ['instance_id', 'offset', 'limit', 'db_user_id', 'db_username', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ListDbUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_innodb_locks(self, request):
        """查询InnoDB锁等待列表

        查询InnoDB锁等待列表。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListInnodbLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListInnodbLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListInnodbLocksResponse`
        """
        return self.list_innodb_locks_with_http_info(request)

    def list_innodb_locks_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/innodb-locks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInnodbLocksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_metadata_locks(self, request):
        """查询元数据锁列表

        查询元数据锁列表。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListMetadataLocks
        :type request: :class:`huaweicloudsdkdas.v3.ListMetadataLocksRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListMetadataLocksResponse`
        """
        return self.list_metadata_locks_with_http_info(request)

    def list_metadata_locks_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'thread_id', 'database', 'table', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/metadata-locks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetadataLocksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_processes(self, request):
        """查询实例会话列表

        支持根据数据库、用户查询实例会话列表。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListProcesses
        :type request: :class:`huaweicloudsdkdas.v3.ListProcessesRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListProcessesResponse`
        """
        return self.list_processes_with_http_info(request)

    def list_processes_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'user', 'database', 'offset', 'limit', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/processes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListProcessesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_space_analysis(self, request):
        """获取空间分析数据列表

        获取空间分析数据列表。实例级别数据来源于文件系统，库级别和表级别数据来源于information_schema.tables表。空间&amp;元数据分析最多分析10000张表，若缺少库表空间数据，可能是因为数据库实例表个数过多或者账号未保存密码。如果为保存密码，请使用用户管理接口或页面录入数据库账号。支持MySQL和GaussDB(for MySQL)引擎
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ListSpaceAnalysis
        :type request: :class:`huaweicloudsdkdas.v3.ListSpaceAnalysisRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ListSpaceAnalysisResponse`
        """
        return self.list_space_analysis_with_http_info(request)

    def list_space_analysis_with_http_info(self, request):
        all_params = ['instance_id', 'object_type', 'datastore_type', 'x_language', 'database_id', 'offset', 'limit', 'show_instance_info']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/space-analysis',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSpaceAnalysisResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def register_db_user(self, request):
        """注册数据库用户

        此接口是将数据库用户和密码注册进DAS系统，同时会返回一个数据库用户ID ，后续调用其他接口时（如查询实例会话列表接口）需要用到此数据库用户ID。密码为加密存储，且仅用于DAS API相关功能。此接口不会在数据库实例上创建数据库用户对象。请确保输入的用户名和密码是已经存在并且是正确的。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RegisterDbUser
        :type request: :class:`huaweicloudsdkdas.v3.RegisterDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.RegisterDbUserResponse`
        """
        return self.register_db_user_with_http_info(request)

    def register_db_user_with_http_info(self, request):
        all_params = ['instance_id', 'register_db_user_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RegisterDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_db_user(self, request):
        """查询数据库用户信息

        查询注册在DAS里的数据库用户信息。此接口不能查询数据库实例上的数据库用户对象。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDbUser
        :type request: :class:`huaweicloudsdkdas.v3.ShowDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowDbUserResponse`
        """
        return self.show_db_user_with_http_info(request)

    def show_db_user_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_quotas(self, request):
        """查询云DBA配额

        查询云DBA配额
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkdas.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowQuotasResponse`
        """
        return self.show_quotas_with_http_info(request)

    def show_quotas_with_http_info(self, request):
        all_params = ['x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='ShowQuotasResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_execution_plan(self, request):
        """查询SQL执行计划

        查询SQL执行计划。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSqlExecutionPlan
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlExecutionPlanRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlExecutionPlanResponse`
        """
        return self.show_sql_execution_plan_with_http_info(request)

    def show_sql_execution_plan_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'database', 'sql', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/sql/explain',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSqlExecutionPlanResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_explain(self, request):
        """查询SQL执行计划

        查询SQL执行计划。
        目前仅支持MySQL实例。
        补充GET请求，处理超长SQL
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSqlExplain
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlExplainRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlExplainResponse`
        """
        return self.show_sql_explain_with_http_info(request)

    def show_sql_explain_with_http_info(self, request):
        all_params = ['instance_id', 'query_sql_plan_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/sql/explain',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSqlExplainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sql_switch_status(self, request):
        """查询全量SQL和慢SQL的开关状态。

        查询DAS收集全量SQL和慢SQL的开关状态。该功能仅支持付费实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowSqlSwitchStatus
        :type request: :class:`huaweicloudsdkdas.v3.ShowSqlSwitchStatusRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.ShowSqlSwitchStatusResponse`
        """
        return self.show_sql_switch_status_with_http_info(request)

    def show_sql_switch_status_with_http_info(self, request):
        all_params = ['instance_id', 'type', 'datastore_type', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/instances/{instance_id}/sql/switch',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSqlSwitchStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_db_user(self, request):
        """修改数据库用户

        修改注册在DAS里的数据库用户名和密码。此接口不会修改数据库实例上的数据库用户对象的用户名和密码。请确保输入的用户名和密码是已经存在并且是正确的。
        目前仅支持MySQL实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for UpdateDbUser
        :type request: :class:`huaweicloudsdkdas.v3.UpdateDbUserRequest`
        :rtype: :class:`huaweicloudsdkdas.v3.UpdateDbUserResponse`
        """
        return self.update_db_user_with_http_info(request)

    def update_db_user_with_http_info(self, request):
        all_params = ['instance_id', 'db_user_id', 'update_db_user_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/instances/{instance_id}/db-users/{db_user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDbUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

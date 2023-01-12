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


class DrsAsyncClient(Client):
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
        super(DrsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdrs.v5.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DrsClient":
            raise TypeError("client type error, support client type is DrsClient")

        return ClientBuilder(clazz)

    def batch_create_jobs_async_async(self, request):
        """批量异步创建任务

        批量异步创建任务，根据请求参数不同，可以批量异步创建实时迁移、实时同步、实时灾备等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateJobsAsync
        :type request: :class:`huaweicloudsdkdrs.v5.BatchCreateJobsAsyncRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchCreateJobsAsyncResponse`
        """
        return self.batch_create_jobs_async_with_http_info(request)

    def batch_create_jobs_async_with_http_info(self, request):
        all_params = ['request_body', 'x_language']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs/batch-async-create',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCreateJobsAsyncResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_jobs_by_id_async(self, request):
        """批量删除任务

        批量删除租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteJobsById
        :type request: :class:`huaweicloudsdkdrs.v5.BatchDeleteJobsByIdRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchDeleteJobsByIdResponse`
        """
        return self.batch_delete_jobs_by_id_with_http_info(request)

    def batch_delete_jobs_by_id_with_http_info(self, request):
        all_params = ['request_body', 'x_language']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteJobsByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_execute_job_actions_async(self, request):
        """批量操作指定ID任务

        批量操作租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchExecuteJobActions
        :type request: :class:`huaweicloudsdkdrs.v5.BatchExecuteJobActionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchExecuteJobActionsResponse`
        """
        return self.batch_execute_job_actions_with_http_info(request)

    def batch_execute_job_actions_with_http_info(self, request):
        all_params = ['request_body', 'x_language']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchExecuteJobActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_db_objects_async_async(self, request):
        """提交查询数据库对象信息

        提交查询数据库对象信息。例如：
        - 当type取值为source时，表示查询源库库表信息。
        - 当源库库表信息有变化时，则type取值为source，is_refresh取值为true。
        - 当已同步到目标库的库表信息过大，需要提前将数据加载到缓存中时，type取值为synchronized。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectDbObjectsAsync
        :type request: :class:`huaweicloudsdkdrs.v5.CollectDbObjectsAsyncRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CollectDbObjectsAsyncResponse`
        """
        return self.collect_db_objects_async_with_http_info(request)

    def collect_db_objects_async_with_http_info(self, request):
        all_params = ['job_id', 'type', 'x_language', 'offset', 'limit', 'is_refresh', 'db_names']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'is_refresh' in local_var_params:
            query_params.append(('is_refresh', local_var_params['is_refresh']))
        if 'db_names' in local_var_params:
            query_params.append(('db_names', local_var_params['db_names']))
            collection_formats['db_names'] = 'csv'

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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-objects/collect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectDbObjectsAsyncResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def commit_async_job_async(self, request):
        """提交批量创建异步任务

        提交批量创建异步任务，当批量异步任务创建或更新参数后，系统会自动开始进行参数校验，待所有任务成功完成参数校验后并且无报错时，可调用此接口开始创建DRS任务实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CommitAsyncJob
        :type request: :class:`huaweicloudsdkdrs.v5.CommitAsyncJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CommitAsyncJobResponse`
        """
        return self.commit_async_job_with_http_info(request)

    def commit_async_job_with_http_info(self, request):
        all_params = ['async_job_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'async_job_id' in local_var_params:
            path_params['async_job_id'] = local_var_params['async_job_id']

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
            resource_path='/v5/{project_id}/batch-async-jobs/{async_job_id}/commit',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CommitAsyncJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_job_async(self, request):
        """创建任务

        创建单个任务，根据请求参数不同，可以创建单个实时迁移、实时同步、实时灾备等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateJob
        :type request: :class:`huaweicloudsdkdrs.v5.CreateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CreateJobResponse`
        """
        return self.create_job_with_http_info(request)

    def create_job_with_http_info(self, request):
        all_params = ['request_body', 'x_language']
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
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_job_async(self, request):
        """删除指定ID任务

        删除租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkdrs.v5.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DeleteJobResponse`
        """
        return self.delete_job_with_http_info(request)

    def delete_job_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/jobs/{job_id}',
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

    def download_db_object_template_async(self, request):
        """对象选择（文件导入 - 模板下载）

        对象选择（文件导入 - 模板下载）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadDbObjectTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.DownloadDbObjectTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DownloadDbObjectTemplateResponse`
        """
        return self.download_db_object_template_with_http_info(request)

    def download_db_object_template_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-object/template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadDbObjectTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_job_action_async(self, request):
        """操作指定ID任务

        操作租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteJobAction
        :type request: :class:`huaweicloudsdkdrs.v5.ExecuteJobActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ExecuteJobActionResponse`
        """
        return self.execute_job_action_with_http_info(request)

    def execute_job_action_with_http_info(self, request):
        all_params = ['job_id', 'request_body', 'x_language']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs/{job_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteJobActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_async_job_detail_async(self, request):
        """查询指定ID批量异步任务详情

        查询租户指定ID批量异步任务详情，默认为任务的“create_time”降序排序获取结果，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAsyncJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ListAsyncJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListAsyncJobDetailResponse`
        """
        return self.list_async_job_detail_with_http_info(request)

    def list_async_job_detail_with_http_info(self, request):
        all_params = ['async_job_id', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'async_job_id' in local_var_params:
            path_params['async_job_id'] = local_var_params['async_job_id']

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
            resource_path='/v5/{project_id}/batch-async-jobs/{async_job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAsyncJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_async_jobs_async(self, request):
        """查询批量异步创建的任务列表

        查询租户批量异步创建的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAsyncJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ListAsyncJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListAsyncJobsResponse`
        """
        return self.list_async_jobs_with_http_info(request)

    def list_async_jobs_with_http_info(self, request):
        all_params = ['x_language', 'async_job_id', 'status', 'domain_name', 'user_name', 'offset', 'limit', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'async_job_id' in local_var_params:
            query_params.append(('async_job_id', local_var_params['async_job_id']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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
            resource_path='/v5/{project_id}/batch-async-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAsyncJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_db_objects_async(self, request):
        """查询数据库对象信息

        查询数据库对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbObjects
        :type request: :class:`huaweicloudsdkdrs.v5.ListDbObjectsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListDbObjectsResponse`
        """
        return self.list_db_objects_with_http_info(request)

    def list_db_objects_with_http_info(self, request):
        all_params = ['job_id', 'type', 'x_language', 'offset', 'limit', 'db_names']
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'db_names' in local_var_params:
            query_params.append(('db_names', local_var_params['db_names']))
            collection_formats['db_names'] = 'csv'

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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDbObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jobs_async(self, request):
        """查询任务列表

        查询租户任务列表，可以根据企业项目，引擎类型，网络类型，任务状态，任务名称，任务ID进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListJobsResponse`
        """
        return self.list_jobs_with_http_info(request)

    def list_jobs_with_http_info(self, request):
        all_params = ['job_type', 'x_language', 'name', 'status', 'engine_type', 'net_type', 'enterprise_project_id', 'offset', 'limit', 'sort_key', 'sort_dir']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'engine_type' in local_var_params:
            query_params.append(('engine_type', local_var_params['engine_type']))
        if 'net_type' in local_var_params:
            query_params.append(('net_type', local_var_params['net_type']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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
            resource_path='/v5/{project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_links_async(self, request):
        """查询可用链路信息

        查询可用链路信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLinks
        :type request: :class:`huaweicloudsdkdrs.v5.ListLinksRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListLinksResponse`
        """
        return self.list_links_with_http_info(request)

    def list_links_with_http_info(self, request):
        all_params = ['job_type', 'x_language', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
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
            resource_path='/v5/{project_id}/links',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLinksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_db_object_collection_status_async(self, request):
        """获取提交查询数据库对象信息的结果

        获取提交查询数据库对象信息的结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectCollectionStatus
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectCollectionStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectCollectionStatusResponse`
        """
        return self.show_db_object_collection_status_with_http_info(request)

    def show_db_object_collection_status_with_http_info(self, request):
        all_params = ['job_id', 'query_id', 'x_language']
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
        if 'query_id' in local_var_params:
            query_params.append(('query_id', local_var_params['query_id']))

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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-objects/collection-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDbObjectCollectionStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_db_object_template_progress_async(self, request):
        """对象选择（文件导入 - 进度查询）

        对象选择（文件导入 - 进度查询）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectTemplateProgress
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateProgressResponse`
        """
        return self.show_db_object_template_progress_with_http_info(request)

    def show_db_object_template_progress_with_http_info(self, request):
        all_params = ['job_id', 'x_language', 'offset', 'limit']
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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-object/template/progress',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDbObjectTemplateProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_db_object_template_result_async(self, request):
        """对象选择（文件导入 - 获取导入结果）

        对象选择（文件导入 - 获取导入结果）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectTemplateResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateResultResponse`
        """
        return self.show_db_object_template_result_with_http_info(request)

    def show_db_object_template_result_with_http_info(self, request):
        all_params = ['job_id', 'type', 'x_language']
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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-object/template/result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDbObjectTemplateResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_detail_async(self, request):
        """查询任务详情

        查询任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowJobDetailResponse`
        """
        return self.show_job_detail_with_http_info(request)

    def show_job_detail_with_http_info(self, request):
        all_params = ['job_id', 'type', 'x_language', 'query_id', 'offset', 'limit', 'compare_type', 'query_type', 'object_type', 'compare_task_id', 'source_db_name', 'target_db_name', 'compare_detail_type']
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
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'query_id' in local_var_params:
            query_params.append(('query_id', local_var_params['query_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'compare_type' in local_var_params:
            query_params.append(('compare_type', local_var_params['compare_type']))
        if 'query_type' in local_var_params:
            query_params.append(('query_type', local_var_params['query_type']))
        if 'object_type' in local_var_params:
            query_params.append(('object_type', local_var_params['object_type']))
        if 'compare_task_id' in local_var_params:
            query_params.append(('compare_task_id', local_var_params['compare_task_id']))
        if 'source_db_name' in local_var_params:
            query_params.append(('source_db_name', local_var_params['source_db_name']))
        if 'target_db_name' in local_var_params:
            query_params.append(('target_db_name', local_var_params['target_db_name']))
        if 'compare_detail_type' in local_var_params:
            query_params.append(('compare_detail_type', local_var_params['compare_detail_type']))

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
            resource_path='/v5/{project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_update_object_saving_status_async(self, request):
        """获取对象保存进度

        获取对象保存进度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUpdateObjectSavingStatus
        :type request: :class:`huaweicloudsdkdrs.v5.ShowUpdateObjectSavingStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowUpdateObjectSavingStatusResponse`
        """
        return self.show_update_object_saving_status_with_http_info(request)

    def show_update_object_saving_status_with_http_info(self, request):
        all_params = ['job_id', 'query_id', 'x_language']
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
        if 'query_id' in local_var_params:
            query_params.append(('query_id', local_var_params['query_id']))

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
            resource_path='/v5/{project_id}/jobs/{job_id}/db-objects/saving-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUpdateObjectSavingStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_batch_async_jobs_async(self, request):
        """更新指定ID批量异步任务详情

        更新租户指定ID批量异步任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBatchAsyncJobs
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateBatchAsyncJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateBatchAsyncJobsResponse`
        """
        return self.update_batch_async_jobs_with_http_info(request)

    def update_batch_async_jobs_with_http_info(self, request):
        all_params = ['async_job_id', 'request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'async_job_id' in local_var_params:
            path_params['async_job_id'] = local_var_params['async_job_id']

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
            resource_path='/v5/{project_id}/batch-async-jobs/{async_job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateBatchAsyncJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job_async(self, request):
        """更新指定ID任务详情

        更新租户指定ID任务详情。
        当type取值为db_object， 进行异步处理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateJobResponse`
        """
        return self.update_job_with_http_info(request)

    def update_job_with_http_info(self, request):
        all_params = ['job_id', 'request_body', 'x_language']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_db_object_template_async(self, request):
        """对象选择（文件导入 - 模板上传）

        对象选择（文件导入 - 模板上传）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadDbObjectTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.UploadDbObjectTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UploadDbObjectTemplateResponse`
        """
        return self.upload_db_object_template_with_http_info(request)

    def upload_db_object_template_with_http_info(self, request):
        all_params = ['job_id', 'file', 'x_language']
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/jobs/{job_id}/db-object/template',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadDbObjectTemplateResponse',
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

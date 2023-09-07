# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DrsClient(Client):
    def __init__(self):
        super(DrsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdrs.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DrsClient":
            raise TypeError("client type error, support client type is DrsClient")

        return ClientBuilder(clazz)

    def batch_create_jobs_async(self, request):
        """批量异步创建任务

        批量异步创建任务，根据请求参数不同，可以批量异步创建实时迁移、实时同步、实时灾备等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateJobsAsync
        :type request: :class:`huaweicloudsdkdrs.v5.BatchCreateJobsAsyncRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchCreateJobsAsyncResponse`
        """
        return self._batch_create_jobs_async_with_http_info(request)

    def _batch_create_jobs_async_with_http_info(self, request):
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

    def batch_delete_jobs_by_id(self, request):
        """批量删除任务

        批量删除租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteJobsById
        :type request: :class:`huaweicloudsdkdrs.v5.BatchDeleteJobsByIdRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchDeleteJobsByIdResponse`
        """
        return self._batch_delete_jobs_by_id_with_http_info(request)

    def _batch_delete_jobs_by_id_with_http_info(self, request):
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

    def batch_execute_job_actions(self, request):
        """批量操作指定ID任务

        批量操作租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchExecuteJobActions
        :type request: :class:`huaweicloudsdkdrs.v5.BatchExecuteJobActionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchExecuteJobActionsResponse`
        """
        return self._batch_execute_job_actions_with_http_info(request)

    def _batch_execute_job_actions_with_http_info(self, request):
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

    def batch_stop_jobs_action(self, request):
        """批量结束任务

        批量结束租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchStopJobsAction
        :type request: :class:`huaweicloudsdkdrs.v5.BatchStopJobsActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchStopJobsActionResponse`
        """
        return self._batch_stop_jobs_action_with_http_info(request)

    def _batch_stop_jobs_action_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/jobs/batch-stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchStopJobsActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_tag_action(self, request):
        """批量添加或删除资源标签

        批量添加删除资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkdrs.v5.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchTagActionResponse`
        """
        return self._batch_tag_action_with_http_info(request)

    def _batch_tag_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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
            resource_path='/v5/{project_id}/jobs/{resource_type}/{job_id}/tags/action',
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

    def check_data_filter(self, request):
        """数据过滤规则校验

        数据过滤规则校验
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDataFilter
        :type request: :class:`huaweicloudsdkdrs.v5.CheckDataFilterRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CheckDataFilterResponse`
        """
        return self._check_data_filter_with_http_info(request)

    def _check_data_filter_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/job/{job_id}/data-filtering/check',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckDataFilterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_columns(self, request):
        """采集指定数据库表的列信息

        采集指定数据库表的列信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectColumns
        :type request: :class:`huaweicloudsdkdrs.v5.CollectColumnsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CollectColumnsResponse`
        """
        return self._collect_columns_with_http_info(request)

    def _collect_columns_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/job/{job_id}/columns/collect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectColumnsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def collect_db_objects_async(self, request):
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
        return self._collect_db_objects_async_with_http_info(request)

    def _collect_db_objects_async_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def collect_db_objects_info(self, request):
        """提交查询数据库对象信息

        提交查询数据库对象信息。例如：
        - 当type取值为source时，表示查询源库库表信息。
        - 当源库库表信息有变化时，则type取值为source，is_refresh取值为true。
        - 当已同步到目标库的库表信息过大，需要提前将数据加载到缓存中时，type取值为synchronized。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectDbObjectsInfo
        :type request: :class:`huaweicloudsdkdrs.v5.CollectDbObjectsInfoRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CollectDbObjectsInfoResponse`
        """
        return self._collect_db_objects_info_with_http_info(request)

    def _collect_db_objects_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5.1/{project_id}/jobs/{job_id}/db-objects/collect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectDbObjectsInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def commit_async_job(self, request):
        """提交批量创建异步任务

        提交批量创建异步任务，当批量异步任务创建或更新参数后，系统会自动开始进行参数校验，待所有任务成功完成参数校验后并且无报错时，可调用此接口开始创建DRS任务实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CommitAsyncJob
        :type request: :class:`huaweicloudsdkdrs.v5.CommitAsyncJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CommitAsyncJobResponse`
        """
        return self._commit_async_job_with_http_info(request)

    def _commit_async_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def copy_job(self, request):
        """克隆任务

        DRS支持通过克隆功能，快速复制现有同步任务的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyJob
        :type request: :class:`huaweicloudsdkdrs.v5.CopyJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CopyJobResponse`
        """
        return self._copy_job_with_http_info(request)

    def _copy_job_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/jobs/clone',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_job(self, request):
        """创建任务

        创建单个任务，根据请求参数不同，可以创建单个实时迁移、实时同步、实时灾备等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateJob
        :type request: :class:`huaweicloudsdkdrs.v5.CreateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CreateJobResponse`
        """
        return self._create_job_with_http_info(request)

    def _create_job_with_http_info(self, request):
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

    def delete_job(self, request):
        """删除指定ID任务

        删除租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkdrs.v5.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DeleteJobResponse`
        """
        return self._delete_job_with_http_info(request)

    def _delete_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def download_batch_create_template(self, request):
        """下载批量导入任务模板

        下载批量导入任务模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadBatchCreateTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.DownloadBatchCreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DownloadBatchCreateTemplateResponse`
        """
        return self._download_batch_create_template_with_http_info(request)

    def _download_batch_create_template_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/jobs/template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadBatchCreateTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_db_object_template(self, request):
        """对象选择（文件导入 - 模板下载）

        对象选择（文件导入 - 模板下载）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadDbObjectTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.DownloadDbObjectTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DownloadDbObjectTemplateResponse`
        """
        return self._download_db_object_template_with_http_info(request)

    def _download_db_object_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'file_import_db_level' in local_var_params:
            query_params.append(('file_import_db_level', local_var_params['file_import_db_level']))

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

    def execute_job_action(self, request):
        """操作指定ID任务

        操作租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteJobAction
        :type request: :class:`huaweicloudsdkdrs.v5.ExecuteJobActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ExecuteJobActionResponse`
        """
        return self._execute_job_action_with_http_info(request)

    def _execute_job_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def export_operation_info(self, request):
        """导出任务操作统计信息

        导出指定任务操作统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportOperationInfo
        :type request: :class:`huaweicloudsdkdrs.v5.ExportOperationInfoRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ExportOperationInfoResponse`
        """
        return self._export_operation_info_with_http_info(request)

    def _export_operation_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/operation-statistics/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportOperationInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_batch_create_jobs(self, request):
        """批量导入任务

        批量导入任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportBatchCreateJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ImportBatchCreateJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ImportBatchCreateJobsResponse`
        """
        return self._import_batch_create_jobs_with_http_info(request)

    def _import_batch_create_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v5/{project_id}/jobs/template',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportBatchCreateJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_async_job_detail(self, request):
        """查询指定ID批量异步任务详情

        查询租户指定ID批量异步任务详情，默认为任务的“create_time”降序排序获取结果，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsyncJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ListAsyncJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListAsyncJobDetailResponse`
        """
        return self._list_async_job_detail_with_http_info(request)

    def _list_async_job_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_async_jobs(self, request):
        """查询批量异步创建的任务列表

        查询租户批量异步创建的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsyncJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ListAsyncJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListAsyncJobsResponse`
        """
        return self._list_async_jobs_with_http_info(request)

    def _list_async_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_db_objects(self, request):
        """查询数据库对象信息

        查询数据库对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbObjects
        :type request: :class:`huaweicloudsdkdrs.v5.ListDbObjectsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListDbObjectsResponse`
        """
        return self._list_db_objects_with_http_info(request)

    def _list_db_objects_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_jobs(self, request):
        """查询任务列表

        查询租户任务列表，可以根据企业项目，引擎类型，网络类型，任务状态，任务名称，任务ID进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListJobsResponse`
        """
        return self._list_jobs_with_http_info(request)

    def _list_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'instance_ids' in local_var_params:
            query_params.append(('instance_ids', local_var_params['instance_ids']))
            collection_formats['instance_ids'] = 'csv'
        if 'instance_ip' in local_var_params:
            query_params.append(('instance_ip', local_var_params['instance_ip']))

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

    def list_links(self, request):
        """查询可用链路信息

        根据参数不同，可查询实时迁移、实时同步、实时灾备等可用链路信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLinks
        :type request: :class:`huaweicloudsdkdrs.v5.ListLinksRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListLinksResponse`
        """
        return self._list_links_with_http_info(request)

    def _list_links_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_project_tags(self, request):
        """查询项目标签

        查询指定project ID下不同任务类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkdrs.v5.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListProjectTagsResponse`
        """
        return self._list_project_tags_with_http_info(request)

    def _list_project_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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
            resource_path='/v5/{project_id}/jobs/{resource_type}/tags',
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

    def show_actions(self, request):
        """获取指定任务操作信息

        获取指定任务允许、不允许、当前操作信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowActions
        :type request: :class:`huaweicloudsdkdrs.v5.ShowActionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowActionsResponse`
        """
        return self._show_actions_with_http_info(request)

    def _show_actions_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/actions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowActionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_column_info_result(self, request):
        """获取指定数据库表列信息

        获取指定数据库表列信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowColumnInfoResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowColumnInfoResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowColumnInfoResultResponse`
        """
        return self._show_column_info_result_with_http_info(request)

    def _show_column_info_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'query_id' in local_var_params:
            query_params.append(('query_id', local_var_params['query_id']))
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
            resource_path='/v5/{project_id}/job/{job_id}/columns',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowColumnInfoResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_compare_policy(self, request):
        """查询对比策略

        查询对比策略。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowComparePolicy
        :type request: :class:`huaweicloudsdkdrs.v5.ShowComparePolicyRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowComparePolicyResponse`
        """
        return self._show_compare_policy_with_http_info(request)

    def _show_compare_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/compare-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowComparePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_filtering_result(self, request):
        """获取数据过滤校验结果

        获取数据过滤校验结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataFilteringResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDataFilteringResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDataFilteringResultResponse`
        """
        return self._show_data_filtering_result_with_http_info(request)

    def _show_data_filtering_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/job/{job_id}/data-filtering/result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataFilteringResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_processing_rules_result(self, request):
        """获取指定任务数据加工规则更新结果

        获取指定任务数据加工规则更新结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataProcessingRulesResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDataProcessingRulesResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDataProcessingRulesResultResponse`
        """
        return self._show_data_processing_rules_result_with_http_info(request)

    def _show_data_processing_rules_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/data-processing-rules/result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataProcessingRulesResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_progress(self, request):
        """查询数据加工规则

        查询数据加工规则:包含数据库表的映射信息、列信息、数据过滤信息、附加列信息、DDL以及DML信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataProgress
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDataProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDataProgressResponse`
        """
        return self._show_data_progress_with_http_info(request)

    def _show_data_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/data-processing-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_db_object_collection_status(self, request):
        """获取提交查询数据库对象信息的结果

        获取提交查询数据库对象信息的结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDbObjectCollectionStatus
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectCollectionStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectCollectionStatusResponse`
        """
        return self._show_db_object_collection_status_with_http_info(request)

    def _show_db_object_collection_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_db_object_template_progress(self, request):
        """对象选择（文件导入 - 进度查询）

        对象选择（文件导入 - 进度查询）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDbObjectTemplateProgress
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateProgressResponse`
        """
        return self._show_db_object_template_progress_with_http_info(request)

    def _show_db_object_template_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_db_object_template_result(self, request):
        """对象选择（文件导入 - 获取导入结果）

        对象选择（文件导入 - 获取导入结果）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDbObjectTemplateResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateResultResponse`
        """
        return self._show_db_object_template_result_with_http_info(request)

    def _show_db_object_template_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_db_objects_list(self, request):
        """查询数据库对象信息

        查询数据库对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDbObjectsList
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectsListRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectsListResponse`
        """
        return self._show_db_objects_list_with_http_info(request)

    def _show_db_objects_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5.1/{project_id}/jobs/{job_id}/db-object',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDbObjectsListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_dirty_data(self, request):
        """查询异常数据列表

        查询异常数据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDirtyData
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDirtyDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDirtyDataResponse`
        """
        return self._show_dirty_data_with_http_info(request)

    def _show_dirty_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
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
            resource_path='/v5/{project_id}/jobs/{job_id}/dirty-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDirtyDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_enterprise_project(self, request):
        """查询企业项目列表

        查询企业项目列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnterpriseProject
        :type request: :class:`huaweicloudsdkdrs.v5.ShowEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowEnterpriseProjectResponse`
        """
        return self._show_enterprise_project_with_http_info(request)

    def _show_enterprise_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

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
            resource_path='/v5/{project_id}/enterprise-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnterpriseProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_health_compare_job_list(self, request):
        """查询健康对比列表

        查询健康对比列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHealthCompareJobList
        :type request: :class:`huaweicloudsdkdrs.v5.ShowHealthCompareJobListRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowHealthCompareJobListResponse`
        """
        return self._show_health_compare_job_list_with_http_info(request)

    def _show_health_compare_job_list_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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
            resource_path='/v5/{project_id}/jobs/{job_id}/health-compare-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHealthCompareJobListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_increment_components_detail(self, request):
        """查询增量组件详情

        查询任务同步的增量组件的详细信息，实时同步任务，任务模式为增量或者全量+增量才支持。具体介绍可以参考：[查询同步进度](https://support.huaweicloud.com/realtimesyn-drs/drs_10_0007.html)
        - 支持的引擎：oracle-to-gaussdbv5，oracle-to-gaussdbv5ha，gaussdbv5，gaussdbv5-to-mysql，gaussdbv5-to-gaussdbv5ha，gaussdbv5ha，gaussdbv5ha-to-gaussdbv5，gaussdbv5-to-dws，gaussdbv5ha-to-dws，gaussdbv5-to-oracle，gaussdbv5ha-to-oracle，oracle-to-dws，oracle-to-mysql
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowIncrementComponentsDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ShowIncrementComponentsDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowIncrementComponentsDetailResponse`
        """
        return self._show_increment_components_detail_with_http_info(request)

    def _show_increment_components_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/increment-components-detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowIncrementComponentsDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_tags(self, request):
        """查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceTags
        :type request: :class:`huaweicloudsdkdrs.v5.ShowInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowInstanceTagsResponse`
        """
        return self._show_instance_tags_with_http_info(request)

    def _show_instance_tags_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
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
            resource_path='/v5/{project_id}/jobs/{resource_type}/{job_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_detail(self, request):
        """查询任务详情

        查询任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowJobDetailResponse`
        """
        return self._show_job_detail_with_http_info(request)

    def _show_job_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_metering(self, request):
        """获取任务价格信息

        获取询价接口的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetering
        :type request: :class:`huaweicloudsdkdrs.v5.ShowMeteringRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowMeteringResponse`
        """
        return self._show_metering_with_http_info(request)

    def _show_metering_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/metering',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMeteringResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_monitor_data(self, request):
        """查询监控数据

        获取任务监控数据。
        - Cassandra灾备不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMonitorData
        :type request: :class:`huaweicloudsdkdrs.v5.ShowMonitorDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowMonitorDataResponse`
        """
        return self._show_monitor_data_with_http_info(request)

    def _show_monitor_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/monitor-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMonitorDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_object_mapping(self, request):
        """查询同步映射列表

        查询实时同步映射关系包括对象选择时的库映射、schema映射、表映射和数据加工时的列映射。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowObjectMapping
        :type request: :class:`huaweicloudsdkdrs.v5.ShowObjectMappingRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowObjectMappingResponse`
        """
        return self._show_object_mapping_with_http_info(request)

    def _show_object_mapping_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/object-mappings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowObjectMappingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_progress_data(self, request):
        """查询数据级流式对比列表

        查询不同迁移对象类型的迁移进度。
        说明：
        - 目前仅MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)、MongoDB-&gt;DDS、DDS-&gt;MongoDB的迁移支持查看迁移明细。
        - 在任务未结束前，不能修改源库和目标库的所有用户、密码和用户权限等。
        - 全量、增量完成不代表任务结束，如果存在触发器和事件将会进行迁移。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProgressData
        :type request: :class:`huaweicloudsdkdrs.v5.ShowProgressDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowProgressDataResponse`
        """
        return self._show_progress_data_with_http_info(request)

    def _show_progress_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

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
            resource_path='/v5/{project_id}/jobs/{job_id}/progress-data/{type}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProgressDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_support_object_type(self, request):
        """查询是否支持对象选择和列映射

        查询任务支持的对象选择类型、列映射、支持搜索的对象类型等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSupportObjectType
        :type request: :class:`huaweicloudsdkdrs.v5.ShowSupportObjectTypeRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowSupportObjectTypeResponse`
        """
        return self._show_support_object_type_with_http_info(request)

    def _show_support_object_type_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/object/support',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSupportObjectTypeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_update_object_saving_status(self, request):
        """获取对象保存进度

        获取对象保存进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUpdateObjectSavingStatus
        :type request: :class:`huaweicloudsdkdrs.v5.ShowUpdateObjectSavingStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowUpdateObjectSavingStatusResponse`
        """
        return self._show_update_object_saving_status_with_http_info(request)

    def _show_update_object_saving_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def stop_job_action(self, request):
        """结束任务

        结束租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJobAction
        :type request: :class:`huaweicloudsdkdrs.v5.StopJobActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.StopJobActionResponse`
        """
        return self._stop_job_action_with_http_info(request)

    def _stop_job_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopJobActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_batch_async_jobs(self, request):
        """更新指定ID批量异步任务详情

        更新租户指定ID批量异步任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBatchAsyncJobs
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateBatchAsyncJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateBatchAsyncJobsResponse`
        """
        return self._update_batch_async_jobs_with_http_info(request)

    def _update_batch_async_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_data_progress(self, request):
        """更新指定任务数据加工规则

        更新指定任务数据加工规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataProgress
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateDataProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateDataProgressResponse`
        """
        return self._update_data_progress_with_http_info(request)

    def _update_data_progress_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/data-processing-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataProgressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job(self, request):
        """更新指定ID任务详情

        更新租户指定ID任务详情。
        当type取值为db_object， 进行异步处理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateJobResponse`
        """
        return self._update_job_with_http_info(request)

    def _update_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_start_position(self, request):
        """更新增量任务启动位点

        更新增量任务的启动位点。
        - 仅engine_type为mysql,mysql-to-dws,mysql-to-taurus,taurus,mysql-to-oracle,taurus-to-oracle,taurus-to-mysql,mysql-to-kafka,taurus-to-kafka,mongodb-to-kafka,mongodb且为单增量实时同步任务支持。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStartPosition
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateStartPositionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateStartPositionResponse`
        """
        return self._update_start_position_with_http_info(request)

    def _update_start_position_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v5/{project_id}/jobs/{job_id}/start-position',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStartPositionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_db_object_template(self, request):
        """对象选择（文件导入 - 模板上传）

        对象选择（文件导入 - 模板上传）。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadDbObjectTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.UploadDbObjectTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UploadDbObjectTemplateResponse`
        """
        return self._upload_db_object_template_with_http_info(request)

    def _upload_db_object_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'file_import_db_level' in local_var_params:
            query_params.append(('file_import_db_level', local_var_params['file_import_db_level']))

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

    def validate_job_name(self, request):
        """任务名称校验

        创建任务时对任务名称进行校验。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateJobName
        :type request: :class:`huaweicloudsdkdrs.v5.ValidateJobNameRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ValidateJobNameResponse`
        """
        return self._validate_job_name_with_http_info(request)

    def _validate_job_name_with_http_info(self, request):
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
            resource_path='/v5/{project_id}/jobs/name-validation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ValidateJobNameResponse',
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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdrs'")


class DrsAsyncClient(Client):
    def __init__(self):
        super(DrsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdrs.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DrsAsyncClient":
                raise TypeError("client type error, support client type is DrsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_jobs_async_async(self, request):
        """批量异步创建任务

        批量异步创建任务，根据请求参数不同，可以批量异步创建实时迁移、实时同步、实时灾备等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateJobsAsync
        :type request: :class:`huaweicloudsdkdrs.v5.BatchCreateJobsAsyncRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchCreateJobsAsyncResponse`
        """
        http_info = self._batch_create_jobs_async_http_info(request)
        return self._call_api(**http_info)

    def batch_create_jobs_async_async_invoker(self, request):
        http_info = self._batch_create_jobs_async_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_jobs_async_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/batch-async-create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateJobsAsyncResponse"
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

    def batch_create_tags_async(self, request):
        """批量添加资源标签

        批量添加资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkdrs.v5.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchCreateTagsResponse`
        """
        http_info = self._batch_create_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tags_async_invoker(self, request):
        http_info = self._batch_create_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagsResponse"
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

    def batch_delete_jobs_by_id_async(self, request):
        """批量删除任务

        批量删除租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteJobsById
        :type request: :class:`huaweicloudsdkdrs.v5.BatchDeleteJobsByIdRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchDeleteJobsByIdResponse`
        """
        http_info = self._batch_delete_jobs_by_id_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_jobs_by_id_async_invoker(self, request):
        http_info = self._batch_delete_jobs_by_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_jobs_by_id_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteJobsByIdResponse"
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

    def batch_delete_tags_async(self, request):
        """批量删除资源标签

        为指定实例批量删除标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkdrs.v5.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchDeleteTagsResponse`
        """
        http_info = self._batch_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_tags_async_invoker(self, request):
        http_info = self._batch_delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTagsResponse"
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

    def batch_execute_job_actions_async(self, request):
        """批量操作指定ID任务

        批量操作租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchExecuteJobActions
        :type request: :class:`huaweicloudsdkdrs.v5.BatchExecuteJobActionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchExecuteJobActionsResponse`
        """
        http_info = self._batch_execute_job_actions_http_info(request)
        return self._call_api(**http_info)

    def batch_execute_job_actions_async_invoker(self, request):
        http_info = self._batch_execute_job_actions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_execute_job_actions_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchExecuteJobActionsResponse"
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

    def batch_stop_jobs_action_async(self, request):
        """批量结束任务

        批量结束租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopJobsAction
        :type request: :class:`huaweicloudsdkdrs.v5.BatchStopJobsActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchStopJobsActionResponse`
        """
        http_info = self._batch_stop_jobs_action_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_jobs_action_async_invoker(self, request):
        http_info = self._batch_stop_jobs_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_jobs_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/batch-stop",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopJobsActionResponse"
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

    def batch_tag_action_async(self, request):
        """批量添加或删除资源标签

        批量添加删除资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchTagAction
        :type request: :class:`huaweicloudsdkdrs.v5.BatchTagActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.BatchTagActionResponse`
        """
        http_info = self._batch_tag_action_http_info(request)
        return self._call_api(**http_info)

    def batch_tag_action_async_invoker(self, request):
        http_info = self._batch_tag_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_tag_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{resource_type}/{job_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchTagActionResponse"
            }

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

    def check_data_filter_async(self, request):
        """数据过滤规则校验

        数据过滤规则校验
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckDataFilter
        :type request: :class:`huaweicloudsdkdrs.v5.CheckDataFilterRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CheckDataFilterResponse`
        """
        http_info = self._check_data_filter_http_info(request)
        return self._call_api(**http_info)

    def check_data_filter_async_invoker(self, request):
        http_info = self._check_data_filter_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_data_filter_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/job/{job_id}/data-filtering/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckDataFilterResponse"
            }

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

    def collect_columns_async(self, request):
        """采集指定数据库表的列信息

        采集指定数据库表的列信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectColumns
        :type request: :class:`huaweicloudsdkdrs.v5.CollectColumnsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CollectColumnsResponse`
        """
        http_info = self._collect_columns_http_info(request)
        return self._call_api(**http_info)

    def collect_columns_async_invoker(self, request):
        http_info = self._collect_columns_http_info(request)
        return AsyncInvoker(self, http_info)

    def _collect_columns_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/job/{job_id}/columns/collect",
            "request_type": request.__class__.__name__,
            "response_type": "CollectColumnsResponse"
            }

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
        http_info = self._collect_db_objects_async_http_info(request)
        return self._call_api(**http_info)

    def collect_db_objects_async_async_invoker(self, request):
        http_info = self._collect_db_objects_async_http_info(request)
        return AsyncInvoker(self, http_info)

    def _collect_db_objects_async_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-objects/collect",
            "request_type": request.__class__.__name__,
            "response_type": "CollectDbObjectsAsyncResponse"
            }

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

    def collect_db_objects_info_async(self, request):
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
        http_info = self._collect_db_objects_info_http_info(request)
        return self._call_api(**http_info)

    def collect_db_objects_info_async_invoker(self, request):
        http_info = self._collect_db_objects_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _collect_db_objects_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5.1/{project_id}/jobs/{job_id}/db-objects/collect",
            "request_type": request.__class__.__name__,
            "response_type": "CollectDbObjectsInfoResponse"
            }

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

    def collect_position_async_async(self, request):
        """采集数据库位点信息

        采集数据库位点信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectPositionAsync
        :type request: :class:`huaweicloudsdkdrs.v5.CollectPositionAsyncRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CollectPositionAsyncResponse`
        """
        http_info = self._collect_position_async_http_info(request)
        return self._call_api(**http_info)

    def collect_position_async_async_invoker(self, request):
        http_info = self._collect_position_async_http_info(request)
        return AsyncInvoker(self, http_info)

    def _collect_position_async_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/collect-db-position",
            "request_type": request.__class__.__name__,
            "response_type": "CollectPositionAsyncResponse"
            }

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

    def commit_async_job_async(self, request):
        """提交批量创建异步任务

        提交批量创建异步任务，当批量异步任务创建或更新参数后，系统会自动开始进行参数校验，待所有任务成功完成参数校验后并且无报错时，可调用此接口开始创建DRS任务实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CommitAsyncJob
        :type request: :class:`huaweicloudsdkdrs.v5.CommitAsyncJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CommitAsyncJobResponse`
        """
        http_info = self._commit_async_job_http_info(request)
        return self._call_api(**http_info)

    def commit_async_job_async_invoker(self, request):
        http_info = self._commit_async_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _commit_async_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/batch-async-jobs/{async_job_id}/commit",
            "request_type": request.__class__.__name__,
            "response_type": "CommitAsyncJobResponse"
            }

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

    def copy_job_async(self, request):
        """克隆任务

        DRS支持通过克隆功能，快速复制现有同步任务的配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyJob
        :type request: :class:`huaweicloudsdkdrs.v5.CopyJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CopyJobResponse`
        """
        http_info = self._copy_job_http_info(request)
        return self._call_api(**http_info)

    def copy_job_async_invoker(self, request):
        http_info = self._copy_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/clone",
            "request_type": request.__class__.__name__,
            "response_type": "CopyJobResponse"
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

    def count_instance_by_tags_async(self, request):
        """查询资源实例数量

        查询资源实例数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CountInstanceByTags
        :type request: :class:`huaweicloudsdkdrs.v5.CountInstanceByTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CountInstanceByTagsResponse`
        """
        http_info = self._count_instance_by_tags_http_info(request)
        return self._call_api(**http_info)

    def count_instance_by_tags_async_invoker(self, request):
        http_info = self._count_instance_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _count_instance_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/resource-instances/count",
            "request_type": request.__class__.__name__,
            "response_type": "CountInstanceByTagsResponse"
            }

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

    def create_job_async(self, request):
        """创建任务

        创建单个任务，根据请求参数不同，可以创建单个实时迁移、实时同步、实时灾备等任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateJob
        :type request: :class:`huaweicloudsdkdrs.v5.CreateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.CreateJobResponse`
        """
        http_info = self._create_job_http_info(request)
        return self._call_api(**http_info)

    def create_job_async_invoker(self, request):
        http_info = self._create_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateJobResponse"
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

    def delete_jdbc_driver_async(self, request):
        """删除驱动文件

        删除驱动文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteJdbcDriver
        :type request: :class:`huaweicloudsdkdrs.v5.DeleteJdbcDriverRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DeleteJdbcDriverResponse`
        """
        http_info = self._delete_jdbc_driver_http_info(request)
        return self._call_api(**http_info)

    def delete_jdbc_driver_async_invoker(self, request):
        http_info = self._delete_jdbc_driver_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_jdbc_driver_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/jdbc-drivers",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJdbcDriverResponse"
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

    def delete_job_async(self, request):
        """删除指定ID任务

        删除租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkdrs.v5.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_async_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobResponse"
            }

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

    def download_batch_create_template_async(self, request):
        """下载批量导入任务模板

        下载批量导入任务模板
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadBatchCreateTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.DownloadBatchCreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DownloadBatchCreateTemplateResponse`
        """
        http_info = self._download_batch_create_template_http_info(request)
        return self._call_api(**http_info)

    def download_batch_create_template_async_invoker(self, request):
        http_info = self._download_batch_create_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_batch_create_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/template",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadBatchCreateTemplateResponse"
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

    def download_db_object_template_async(self, request):
        """对象选择（文件导入 - 模板下载）

        对象选择（文件导入 - 模板下载）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadDbObjectTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.DownloadDbObjectTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.DownloadDbObjectTemplateResponse`
        """
        http_info = self._download_db_object_template_http_info(request)
        return self._call_api(**http_info)

    def download_db_object_template_async_invoker(self, request):
        http_info = self._download_db_object_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_db_object_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-object/template",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadDbObjectTemplateResponse"
            }

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

    def execute_job_action_async(self, request):
        """操作指定ID任务

        操作租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteJobAction
        :type request: :class:`huaweicloudsdkdrs.v5.ExecuteJobActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ExecuteJobActionResponse`
        """
        http_info = self._execute_job_action_http_info(request)
        return self._call_api(**http_info)

    def execute_job_action_async_invoker(self, request):
        http_info = self._execute_job_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_job_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteJobActionResponse"
            }

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

    def export_operation_info_async(self, request):
        """导出任务操作统计信息

        导出指定任务操作统计信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportOperationInfo
        :type request: :class:`huaweicloudsdkdrs.v5.ExportOperationInfoRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ExportOperationInfoResponse`
        """
        http_info = self._export_operation_info_http_info(request)
        return self._call_api(**http_info)

    def export_operation_info_async_invoker(self, request):
        http_info = self._export_operation_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_operation_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/operation-statistics/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportOperationInfoResponse"
            }

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

    def import_batch_create_jobs_async(self, request):
        """批量导入任务

        批量导入任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportBatchCreateJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ImportBatchCreateJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ImportBatchCreateJobsResponse`
        """
        http_info = self._import_batch_create_jobs_http_info(request)
        return self._call_api(**http_info)

    def import_batch_create_jobs_async_invoker(self, request):
        http_info = self._import_batch_create_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_batch_create_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/template",
            "request_type": request.__class__.__name__,
            "response_type": "ImportBatchCreateJobsResponse"
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def list_async_job_detail_async(self, request):
        """查询指定ID批量异步任务详情

        查询租户指定ID批量异步任务详情，默认为任务的“create_time”降序排序获取结果，支持分页查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAsyncJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ListAsyncJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListAsyncJobDetailResponse`
        """
        http_info = self._list_async_job_detail_http_info(request)
        return self._call_api(**http_info)

    def list_async_job_detail_async_invoker(self, request):
        http_info = self._list_async_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_async_job_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/batch-async-jobs/{async_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListAsyncJobDetailResponse"
            }

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

    def list_async_jobs_async(self, request):
        """查询批量异步创建的任务列表

        查询租户批量异步创建的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAsyncJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ListAsyncJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListAsyncJobsResponse`
        """
        http_info = self._list_async_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_async_jobs_async_invoker(self, request):
        http_info = self._list_async_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_async_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/batch-async-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListAsyncJobsResponse"
            }

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

    def list_db_objects_async(self, request):
        """查询数据库对象信息

        查询数据库对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbObjects
        :type request: :class:`huaweicloudsdkdrs.v5.ListDbObjectsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListDbObjectsResponse`
        """
        http_info = self._list_db_objects_http_info(request)
        return self._call_api(**http_info)

    def list_db_objects_async_invoker(self, request):
        http_info = self._list_db_objects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_db_objects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbObjectsResponse"
            }

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

    def list_instance_by_tags_async(self, request):
        """查询资源实例列表

        查询资源实例列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceByTags
        :type request: :class:`huaweicloudsdkdrs.v5.ListInstanceByTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListInstanceByTagsResponse`
        """
        http_info = self._list_instance_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_by_tags_async_invoker(self, request):
        http_info = self._list_instance_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/{resource_type}/resource-instances/filter",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceByTagsResponse"
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

    def list_instance_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInstanceTags
        :type request: :class:`huaweicloudsdkdrs.v5.ListInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListInstanceTagsResponse`
        """
        http_info = self._list_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def list_instance_tags_async_invoker(self, request):
        http_info = self._list_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_instance_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListInstanceTagsResponse"
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

    def list_jdbc_drivers_async(self, request):
        """查询驱动文件列表

        查询驱动文件列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJdbcDrivers
        :type request: :class:`huaweicloudsdkdrs.v5.ListJdbcDriversRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListJdbcDriversResponse`
        """
        http_info = self._list_jdbc_drivers_http_info(request)
        return self._call_api(**http_info)

    def list_jdbc_drivers_async_invoker(self, request):
        http_info = self._list_jdbc_drivers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jdbc_drivers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jdbc-drivers",
            "request_type": request.__class__.__name__,
            "response_type": "ListJdbcDriversResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_job_history_parameters_async(self, request):
        """查询任务的参数配置修改历史

        查询任务的参数配置修改历史
        - 仅engine_type为mysql、mysql-to-pgl、mysql-to-gaussdbv5、mysql-to-gaussdbv5ha、mysql-to-dws、mysql-to-taurus、mysql-to-kafka、mysql-to-elasticsearch、mysql-to-oracle且任务状态只能为配置中、全量中、增量中、全量失败、增量失败、暂停中的实时同步任务支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobHistoryParameters
        :type request: :class:`huaweicloudsdkdrs.v5.ListJobHistoryParametersRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListJobHistoryParametersResponse`
        """
        http_info = self._list_job_history_parameters_http_info(request)
        return self._call_api(**http_info)

    def list_job_history_parameters_async_invoker(self, request):
        http_info = self._list_job_history_parameters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_history_parameters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/configuration-histories",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobHistoryParametersResponse"
            }

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
        if 'begin_time' in local_var_params:
            query_params.append(('begin_time', local_var_params['begin_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_job_parameters_async(self, request):
        """查询任务参数配置列表

        查询任务的参数配置列表信息
        - 仅engine_type为mysql、mysql-to-pgl、mysql-to-gaussdbv5、mysql-to-gaussdbv5ha、mysql-to-dws、mysql-to-taurus、mysql-to-kafka、mysql-to-elasticsearch、mysql-to-oracle且任务状态只能为配置中、全量中、增量中、全量失败、增量失败、暂停中的实时同步任务支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobParameters
        :type request: :class:`huaweicloudsdkdrs.v5.ListJobParametersRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListJobParametersResponse`
        """
        http_info = self._list_job_parameters_http_info(request)
        return self._call_api(**http_info)

    def list_job_parameters_async_invoker(self, request):
        http_info = self._list_job_parameters_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_job_parameters_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/configurations",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobParametersResponse"
            }

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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_jobs_async(self, request):
        """查询任务列表

        查询租户任务列表，可以根据企业项目，引擎类型，网络类型，任务状态，任务名称，任务ID进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkdrs.v5.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_async_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

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

    def list_links_async(self, request):
        """查询可用链路信息

        根据参数不同，可查询实时迁移、实时同步、实时灾备等可用链路信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLinks
        :type request: :class:`huaweicloudsdkdrs.v5.ListLinksRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListLinksResponse`
        """
        http_info = self._list_links_http_info(request)
        return self._call_api(**http_info)

    def list_links_async_invoker(self, request):
        http_info = self._list_links_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_links_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/links",
            "request_type": request.__class__.__name__,
            "response_type": "ListLinksResponse"
            }

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

    def list_project_tags_async(self, request):
        """查询项目标签

        查询指定project ID下不同任务类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdkdrs.v5.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
            }

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

    def list_tags_async(self, request):
        """查询项目标签

        查询租户在指定Project中实例类型的所有资源标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdrs.v5.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

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

    def lists_agency_permissions_async(self, request):
        """查询委托的权限列表

        根据源库类型，目标库类型，是否自建，获取委托所需要的权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListsAgencyPermissions
        :type request: :class:`huaweicloudsdkdrs.v5.ListsAgencyPermissionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ListsAgencyPermissionsResponse`
        """
        http_info = self._lists_agency_permissions_http_info(request)
        return self._call_api(**http_info)

    def lists_agency_permissions_async_invoker(self, request):
        http_info = self._lists_agency_permissions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _lists_agency_permissions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/agency/permissions",
            "request_type": request.__class__.__name__,
            "response_type": "ListsAgencyPermissionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_type' in local_var_params:
            query_params.append(('source_type', local_var_params['source_type']))
        if 'target_type' in local_var_params:
            query_params.append(('target_type', local_var_params['target_type']))
        if 'is_non_dbs' in local_var_params:
            query_params.append(('is_non_dbs', local_var_params['is_non_dbs']))

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

    def show_actions_async(self, request):
        """获取指定任务操作信息

        获取指定任务允许、不允许、当前操作信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowActions
        :type request: :class:`huaweicloudsdkdrs.v5.ShowActionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowActionsResponse`
        """
        http_info = self._show_actions_http_info(request)
        return self._call_api(**http_info)

    def show_actions_async_invoker(self, request):
        http_info = self._show_actions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_actions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/actions",
            "request_type": request.__class__.__name__,
            "response_type": "ShowActionsResponse"
            }

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

    def show_column_info_result_async(self, request):
        """获取指定数据库表列信息

        获取指定数据库表列信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowColumnInfoResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowColumnInfoResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowColumnInfoResultResponse`
        """
        http_info = self._show_column_info_result_http_info(request)
        return self._call_api(**http_info)

    def show_column_info_result_async_invoker(self, request):
        http_info = self._show_column_info_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_column_info_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/job/{job_id}/columns",
            "request_type": request.__class__.__name__,
            "response_type": "ShowColumnInfoResultResponse"
            }

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

    def show_compare_policy_async(self, request):
        """查询对比策略

        查询对比策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowComparePolicy
        :type request: :class:`huaweicloudsdkdrs.v5.ShowComparePolicyRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowComparePolicyResponse`
        """
        http_info = self._show_compare_policy_http_info(request)
        return self._call_api(**http_info)

    def show_compare_policy_async_invoker(self, request):
        http_info = self._show_compare_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_compare_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/compare-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowComparePolicyResponse"
            }

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

    def show_data_filtering_result_async(self, request):
        """获取数据过滤校验结果

        获取数据过滤校验结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataFilteringResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDataFilteringResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDataFilteringResultResponse`
        """
        http_info = self._show_data_filtering_result_http_info(request)
        return self._call_api(**http_info)

    def show_data_filtering_result_async_invoker(self, request):
        http_info = self._show_data_filtering_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_filtering_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/job/{job_id}/data-filtering/result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataFilteringResultResponse"
            }

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

    def show_data_processing_rules_result_async(self, request):
        """获取指定任务数据加工规则更新结果

        获取指定任务数据加工规则更新结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataProcessingRulesResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDataProcessingRulesResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDataProcessingRulesResultResponse`
        """
        http_info = self._show_data_processing_rules_result_http_info(request)
        return self._call_api(**http_info)

    def show_data_processing_rules_result_async_invoker(self, request):
        http_info = self._show_data_processing_rules_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_processing_rules_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/data-processing-rules/result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataProcessingRulesResultResponse"
            }

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

    def show_data_progress_async(self, request):
        """查询数据加工规则

        查询数据加工规则:包含数据库表的映射信息、列信息、数据过滤信息、附加列信息、DDL以及DML信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDataProgress
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDataProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDataProgressResponse`
        """
        http_info = self._show_data_progress_http_info(request)
        return self._call_api(**http_info)

    def show_data_progress_async_invoker(self, request):
        http_info = self._show_data_progress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_data_progress_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/data-processing-rules",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataProgressResponse"
            }

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

    def show_db_object_collection_status_async(self, request):
        """获取提交查询数据库对象信息的结果

        获取提交查询数据库对象信息的结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectCollectionStatus
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectCollectionStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectCollectionStatusResponse`
        """
        http_info = self._show_db_object_collection_status_http_info(request)
        return self._call_api(**http_info)

    def show_db_object_collection_status_async_invoker(self, request):
        http_info = self._show_db_object_collection_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_db_object_collection_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-objects/collection-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDbObjectCollectionStatusResponse"
            }

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

    def show_db_object_template_progress_async(self, request):
        """对象选择（文件导入 - 进度查询）

        对象选择（文件导入 - 进度查询）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectTemplateProgress
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateProgressResponse`
        """
        http_info = self._show_db_object_template_progress_http_info(request)
        return self._call_api(**http_info)

    def show_db_object_template_progress_async_invoker(self, request):
        http_info = self._show_db_object_template_progress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_db_object_template_progress_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-object/template/progress",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDbObjectTemplateProgressResponse"
            }

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

    def show_db_object_template_result_async(self, request):
        """对象选择（文件导入 - 获取导入结果）

        对象选择（文件导入 - 获取导入结果）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectTemplateResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectTemplateResultResponse`
        """
        http_info = self._show_db_object_template_result_http_info(request)
        return self._call_api(**http_info)

    def show_db_object_template_result_async_invoker(self, request):
        http_info = self._show_db_object_template_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_db_object_template_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-object/template/result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDbObjectTemplateResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'file_export_object_level' in local_var_params:
            query_params.append(('file_export_object_level', local_var_params['file_export_object_level']))

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

    def show_db_objects_list_async(self, request):
        """查询数据库对象信息

        查询数据库对象信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDbObjectsList
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDbObjectsListRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDbObjectsListResponse`
        """
        http_info = self._show_db_objects_list_http_info(request)
        return self._call_api(**http_info)

    def show_db_objects_list_async_invoker(self, request):
        http_info = self._show_db_objects_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_db_objects_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5.1/{project_id}/jobs/{job_id}/db-object",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDbObjectsListResponse"
            }

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

    def show_dirty_data_async(self, request):
        """查询异常数据列表

        查询异常数据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDirtyData
        :type request: :class:`huaweicloudsdkdrs.v5.ShowDirtyDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowDirtyDataResponse`
        """
        http_info = self._show_dirty_data_http_info(request)
        return self._call_api(**http_info)

    def show_dirty_data_async_invoker(self, request):
        http_info = self._show_dirty_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_dirty_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/dirty-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDirtyDataResponse"
            }

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

    def show_enterprise_project_async(self, request):
        """查询企业项目列表

        查询企业项目列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEnterpriseProject
        :type request: :class:`huaweicloudsdkdrs.v5.ShowEnterpriseProjectRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowEnterpriseProjectResponse`
        """
        http_info = self._show_enterprise_project_http_info(request)
        return self._call_api(**http_info)

    def show_enterprise_project_async_invoker(self, request):
        http_info = self._show_enterprise_project_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_enterprise_project_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/enterprise-projects",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnterpriseProjectResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'domain_id' in local_var_params:
            query_params.append(('domain_id', local_var_params['domain_id']))

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

    def show_health_compare_job_detail_async(self, request):
        """查询健康对比任务详情

        查询健康对比任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthCompareJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ShowHealthCompareJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowHealthCompareJobDetailResponse`
        """
        http_info = self._show_health_compare_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_health_compare_job_detail_async_invoker(self, request):
        http_info = self._show_health_compare_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_health_compare_job_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/health-compare-jobs/{compare_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthCompareJobDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'compare_job_id' in local_var_params:
            path_params['compare_job_id'] = local_var_params['compare_job_id']

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

    def show_health_compare_job_list_async(self, request):
        """查询健康对比列表

        查询健康对比列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthCompareJobList
        :type request: :class:`huaweicloudsdkdrs.v5.ShowHealthCompareJobListRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowHealthCompareJobListResponse`
        """
        http_info = self._show_health_compare_job_list_http_info(request)
        return self._call_api(**http_info)

    def show_health_compare_job_list_async_invoker(self, request):
        http_info = self._show_health_compare_job_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_health_compare_job_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/health-compare-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthCompareJobListResponse"
            }

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

    def show_health_object_compare_job_overview_async(self, request):
        """获取健康对比对象级对比概览

        获取健康对比对象级对比概览。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHealthObjectCompareJobOverview
        :type request: :class:`huaweicloudsdkdrs.v5.ShowHealthObjectCompareJobOverviewRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowHealthObjectCompareJobOverviewResponse`
        """
        http_info = self._show_health_object_compare_job_overview_http_info(request)
        return self._call_api(**http_info)

    def show_health_object_compare_job_overview_async_invoker(self, request):
        http_info = self._show_health_object_compare_job_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_health_object_compare_job_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/health-compare-jobs/object/{compare_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHealthObjectCompareJobOverviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'compare_job_id' in local_var_params:
            path_params['compare_job_id'] = local_var_params['compare_job_id']

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

    def show_increment_components_detail_async(self, request):
        """查询增量组件详情

        查询任务同步的增量组件的详细信息，实时同步任务，任务模式为增量或者全量+增量才支持。具体介绍可以参考：[查询同步进度](https://support.huaweicloud.com/realtimesyn-drs/drs_10_0007.html)
        - 支持的引擎：oracle-to-gaussdbv5，oracle-to-gaussdbv5ha，gaussdbv5，gaussdbv5-to-mysql，gaussdbv5-to-gaussdbv5ha，gaussdbv5ha，gaussdbv5ha-to-gaussdbv5，gaussdbv5-to-dws，gaussdbv5ha-to-dws，gaussdbv5-to-oracle，gaussdbv5ha-to-oracle，oracle-to-dws，oracle-to-mysql
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowIncrementComponentsDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ShowIncrementComponentsDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowIncrementComponentsDetailResponse`
        """
        http_info = self._show_increment_components_detail_http_info(request)
        return self._call_api(**http_info)

    def show_increment_components_detail_async_invoker(self, request):
        http_info = self._show_increment_components_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_increment_components_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/increment-components-detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowIncrementComponentsDetailResponse"
            }

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

    def show_instance_tags_async(self, request):
        """查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceTags
        :type request: :class:`huaweicloudsdkdrs.v5.ShowInstanceTagsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowInstanceTagsResponse`
        """
        http_info = self._show_instance_tags_http_info(request)
        return self._call_api(**http_info)

    def show_instance_tags_async_invoker(self, request):
        http_info = self._show_instance_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_instance_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{resource_type}/{job_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowInstanceTagsResponse"
            }

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

    def show_job_detail_async(self, request):
        """查询任务详情

        查询任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobDetail
        :type request: :class:`huaweicloudsdkdrs.v5.ShowJobDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowJobDetailResponse`
        """
        http_info = self._show_job_detail_http_info(request)
        return self._call_api(**http_info)

    def show_job_detail_async_invoker(self, request):
        http_info = self._show_job_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobDetailResponse"
            }

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

    def show_metering_async(self, request):
        """获取任务价格信息

        获取询价接口的参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMetering
        :type request: :class:`huaweicloudsdkdrs.v5.ShowMeteringRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowMeteringResponse`
        """
        http_info = self._show_metering_http_info(request)
        return self._call_api(**http_info)

    def show_metering_async_invoker(self, request):
        http_info = self._show_metering_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_metering_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/metering",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMeteringResponse"
            }

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

    def show_monitor_data_async(self, request):
        """查询监控数据

        获取任务监控数据。
        - Cassandra灾备不支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMonitorData
        :type request: :class:`huaweicloudsdkdrs.v5.ShowMonitorDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowMonitorDataResponse`
        """
        http_info = self._show_monitor_data_http_info(request)
        return self._call_api(**http_info)

    def show_monitor_data_async_invoker(self, request):
        http_info = self._show_monitor_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_monitor_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/monitor-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonitorDataResponse"
            }

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

    def show_object_mapping_async(self, request):
        """查询同步映射列表

        查询实时同步映射关系包括对象选择时的库映射、schema映射、表映射和数据加工时的列映射。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowObjectMapping
        :type request: :class:`huaweicloudsdkdrs.v5.ShowObjectMappingRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowObjectMappingResponse`
        """
        http_info = self._show_object_mapping_http_info(request)
        return self._call_api(**http_info)

    def show_object_mapping_async_invoker(self, request):
        http_info = self._show_object_mapping_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_object_mapping_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/object-mappings",
            "request_type": request.__class__.__name__,
            "response_type": "ShowObjectMappingResponse"
            }

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

    def show_position_result_async(self, request):
        """获取查询数据库位点的结果

        获取查询数据库位点的结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPositionResult
        :type request: :class:`huaweicloudsdkdrs.v5.ShowPositionResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowPositionResultResponse`
        """
        http_info = self._show_position_result_http_info(request)
        return self._call_api(**http_info)

    def show_position_result_async_invoker(self, request):
        http_info = self._show_position_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_position_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-position",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPositionResultResponse"
            }

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

    def show_progress_data_async(self, request):
        """查询数据级流式对比列表

        查询不同迁移对象类型的迁移进度。
        说明：
        - 目前仅MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)、MongoDB-&gt;DDS、DDS-&gt;MongoDB的实时迁移和所有实时同步链路支持查看迁移明细。
        - 在任务未结束前，不能修改源库和目标库的所有用户、密码和用户权限等。
        - 全量、增量完成不代表任务结束，如果存在触发器和事件将会进行迁移。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowProgressData
        :type request: :class:`huaweicloudsdkdrs.v5.ShowProgressDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowProgressDataResponse`
        """
        http_info = self._show_progress_data_http_info(request)
        return self._call_api(**http_info)

    def show_progress_data_async_invoker(self, request):
        http_info = self._show_progress_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_progress_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/progress-data/{type}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProgressDataResponse"
            }

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

    def show_replay_results_async(self, request):
        """查询录制回放结果

        获取录制回放结果数据，包括：回放基于时间维度统计信息，异常SQL及统计结果、慢SQL及统计结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowReplayResults
        :type request: :class:`huaweicloudsdkdrs.v5.ShowReplayResultsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowReplayResultsResponse`
        """
        http_info = self._show_replay_results_http_info(request)
        return self._call_api(**http_info)

    def show_replay_results_async_invoker(self, request):
        http_info = self._show_replay_results_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_replay_results_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/replay-results",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReplayResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'target_name' in local_var_params:
            query_params.append(('target_name', local_var_params['target_name']))
        if 'is_sample' in local_var_params:
            query_params.append(('is_sample', local_var_params['is_sample']))
        if 'error_type' in local_var_params:
            query_params.append(('error_type', local_var_params['error_type']))
        if 'sql_template_md5' in local_var_params:
            query_params.append(('sql_template_md5', local_var_params['sql_template_md5']))

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

    def show_support_object_type_async(self, request):
        """查询是否支持对象选择和列映射

        查询任务支持的对象选择类型、列映射、支持搜索的对象类型等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSupportObjectType
        :type request: :class:`huaweicloudsdkdrs.v5.ShowSupportObjectTypeRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowSupportObjectTypeResponse`
        """
        http_info = self._show_support_object_type_http_info(request)
        return self._call_api(**http_info)

    def show_support_object_type_async_invoker(self, request):
        http_info = self._show_support_object_type_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_support_object_type_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/object/support",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSupportObjectTypeResponse"
            }

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

    def show_update_object_saving_status_async(self, request):
        """获取对象保存进度

        获取对象保存进度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowUpdateObjectSavingStatus
        :type request: :class:`huaweicloudsdkdrs.v5.ShowUpdateObjectSavingStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ShowUpdateObjectSavingStatusResponse`
        """
        http_info = self._show_update_object_saving_status_http_info(request)
        return self._call_api(**http_info)

    def show_update_object_saving_status_async_invoker(self, request):
        http_info = self._show_update_object_saving_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_update_object_saving_status_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-objects/saving-status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowUpdateObjectSavingStatusResponse"
            }

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

    def stop_job_action_async(self, request):
        """结束任务

        结束租户指定ID任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopJobAction
        :type request: :class:`huaweicloudsdkdrs.v5.StopJobActionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.StopJobActionResponse`
        """
        http_info = self._stop_job_action_http_info(request)
        return self._call_api(**http_info)

    def stop_job_action_async_invoker(self, request):
        http_info = self._stop_job_action_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_job_action_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobActionResponse"
            }

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

    def sync_jdbc_driver_async(self, request):
        """同步驱动文件

        同步驱动文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SyncJdbcDriver
        :type request: :class:`huaweicloudsdkdrs.v5.SyncJdbcDriverRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.SyncJdbcDriverResponse`
        """
        http_info = self._sync_jdbc_driver_http_info(request)
        return self._call_api(**http_info)

    def sync_jdbc_driver_async_invoker(self, request):
        http_info = self._sync_jdbc_driver_http_info(request)
        return AsyncInvoker(self, http_info)

    def _sync_jdbc_driver_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/update-jdbc-driver",
            "request_type": request.__class__.__name__,
            "response_type": "SyncJdbcDriverResponse"
            }

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

    def update_batch_async_jobs_async(self, request):
        """更新指定ID批量异步任务详情

        更新租户指定ID批量异步任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateBatchAsyncJobs
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateBatchAsyncJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateBatchAsyncJobsResponse`
        """
        http_info = self._update_batch_async_jobs_http_info(request)
        return self._call_api(**http_info)

    def update_batch_async_jobs_async_invoker(self, request):
        http_info = self._update_batch_async_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_batch_async_jobs_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/batch-async-jobs/{async_job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBatchAsyncJobsResponse"
            }

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

    def update_compare_policy_async(self, request):
        """修改对比策略

        修改周期性对比的对比策略，目前仅MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)、MySQL-&gt;GaussDB(DWS)、GaussDB(for MySQL)-&gt;MySQL同步任务，MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)迁移任务，MySQL-&gt;MySQL、MySQL-&gt;GaussDB(for MySQL)、GaussDB(for MySQL)-&gt;GaussDB(for MySQL)、DDM-&gt;DDM、DDS-DDS灾备任务支持对比策略设置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateComparePolicy
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateComparePolicyRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateComparePolicyResponse`
        """
        http_info = self._update_compare_policy_http_info(request)
        return self._call_api(**http_info)

    def update_compare_policy_async_invoker(self, request):
        http_info = self._update_compare_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_compare_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/compare-policy",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateComparePolicyResponse"
            }

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

    def update_data_progress_async(self, request):
        """更新指定任务数据加工规则

        更新指定任务数据加工规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDataProgress
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateDataProgressRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateDataProgressResponse`
        """
        http_info = self._update_data_progress_http_info(request)
        return self._call_api(**http_info)

    def update_data_progress_async_invoker(self, request):
        http_info = self._update_data_progress_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_data_progress_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/data-processing-rules",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataProgressResponse"
            }

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

    def update_job_async(self, request):
        """更新指定ID任务详情

        更新租户指定ID任务详情。
        当type取值为db_object， 进行异步处理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateJobResponse`
        """
        http_info = self._update_job_http_info(request)
        return self._call_api(**http_info)

    def update_job_async_invoker(self, request):
        http_info = self._update_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateJobResponse"
            }

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

    def update_job_configurations_async(self, request):
        """更新任务的参数信息

        更新任务的参数信息。
        - 仅engine_type为mysql、mysql-to-pgl、mysql-to-gaussdbv5、mysql-to-gaussdbv5ha、mysql-to-dws、mysql-to-taurus、mysql-to-kafka、mysql-to-elasticsearch、mysql-to-oracle且任务状态只能为配置中、全量中、增量中、全量失败、增量失败、暂停中的实时同步任务支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateJobConfigurations
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateJobConfigurationsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateJobConfigurationsResponse`
        """
        http_info = self._update_job_configurations_http_info(request)
        return self._call_api(**http_info)

    def update_job_configurations_async_invoker(self, request):
        http_info = self._update_job_configurations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_job_configurations_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/modify-configuration",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateJobConfigurationsResponse"
            }

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

    def update_start_position_async(self, request):
        """更新增量任务启动位点

        更新增量任务的启动位点。
        - 仅engine_type为mysql,mysql-to-dws,mysql-to-taurus,taurus,mysql-to-oracle,taurus-to-oracle,taurus-to-mysql,mysql-to-kafka,taurus-to-kafka,mongodb-to-kafka,mongodb且为单增量实时同步任务支持。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStartPosition
        :type request: :class:`huaweicloudsdkdrs.v5.UpdateStartPositionRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateStartPositionResponse`
        """
        http_info = self._update_start_position_http_info(request)
        return self._call_api(**http_info)

    def update_start_position_async_invoker(self, request):
        http_info = self._update_start_position_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_start_position_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/start-position",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStartPositionResponse"
            }

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

    def upload_db_object_template_async(self, request):
        """对象选择（文件导入 - 模板上传）

        对象选择（文件导入 - 模板上传）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadDbObjectTemplate
        :type request: :class:`huaweicloudsdkdrs.v5.UploadDbObjectTemplateRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UploadDbObjectTemplateResponse`
        """
        http_info = self._upload_db_object_template_http_info(request)
        return self._call_api(**http_info)

    def upload_db_object_template_async_invoker(self, request):
        http_info = self._upload_db_object_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_db_object_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/{job_id}/db-object/template",
            "request_type": request.__class__.__name__,
            "response_type": "UploadDbObjectTemplateResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def upload_jdbc_driver_async(self, request):
        """上传驱动文件

        上传驱动文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadJdbcDriver
        :type request: :class:`huaweicloudsdkdrs.v5.UploadJdbcDriverRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.UploadJdbcDriverResponse`
        """
        http_info = self._upload_jdbc_driver_http_info(request)
        return self._call_api(**http_info)

    def upload_jdbc_driver_async_invoker(self, request):
        http_info = self._upload_jdbc_driver_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_jdbc_driver_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jdbc-driver",
            "request_type": request.__class__.__name__,
            "response_type": "UploadJdbcDriverResponse"
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
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def validate_job_name_async(self, request):
        """任务名称校验

        创建任务时对任务名称进行校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ValidateJobName
        :type request: :class:`huaweicloudsdkdrs.v5.ValidateJobNameRequest`
        :rtype: :class:`huaweicloudsdkdrs.v5.ValidateJobNameResponse`
        """
        http_info = self._validate_job_name_http_info(request)
        return self._call_api(**http_info)

    def validate_job_name_async_invoker(self, request):
        http_info = self._validate_job_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _validate_job_name_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/{project_id}/jobs/name-validation",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateJobNameResponse"
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

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
        self.model_package = importlib.import_module("huaweicloudsdkdrs.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DrsAsyncClient":
                raise TypeError("client type error, support client type is DrsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_change_data_async(self, request):
        """批量数据加工

        数据复制服务支持对同步的对象进行加工，即可以为选择的对象添加规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchChangeData
        :type request: :class:`huaweicloudsdkdrs.v3.BatchChangeDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchChangeDataResponse`
        """
        http_info = self._batch_change_data_http_info(request)
        return self._call_api(**http_info)

    def batch_change_data_async_invoker(self, request):
        http_info = self._batch_change_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_change_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-transformation",
            "request_type": request.__class__.__name__,
            "response_type": "BatchChangeDataResponse"
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

    def batch_check_jobs_async(self, request):
        """批量预检查

        批量预检查，校验是否可进行迁移。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCheckJobs
        :type request: :class:`huaweicloudsdkdrs.v3.BatchCheckJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchCheckJobsResponse`
        """
        http_info = self._batch_check_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_check_jobs_async_invoker(self, request):
        http_info = self._batch_check_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_check_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-precheck",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckJobsResponse"
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

    def batch_check_results_async(self, request):
        """批量查询预检查结果

        批量查询任务的预检查结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCheckResults
        :type request: :class:`huaweicloudsdkdrs.v3.BatchCheckResultsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchCheckResultsResponse`
        """
        http_info = self._batch_check_results_http_info(request)
        return self._call_api(**http_info)

    def batch_check_results_async_invoker(self, request):
        http_info = self._batch_check_results_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_check_results_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-precheck-result",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCheckResultsResponse"
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

    def batch_create_jobs_async(self, request):
        """批量创建任务

        根据请求参数不同，可以批量创建实时迁移、实时同步、实时灾备任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateJobs
        :type request: :class:`huaweicloudsdkdrs.v3.BatchCreateJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchCreateJobsResponse`
        """
        http_info = self._batch_create_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_create_jobs_async_invoker(self, request):
        http_info = self._batch_create_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-creation",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateJobsResponse"
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

    def batch_delete_jobs_async(self, request):
        """批量结束任务或删除任务

        批量结束任务或删除实时迁移、实时同步、实时灾备任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteJobs
        :type request: :class:`huaweicloudsdkdrs.v3.BatchDeleteJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchDeleteJobsResponse`
        """
        http_info = self._batch_delete_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_jobs_async_invoker(self, request):
        http_info = self._batch_delete_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_jobs_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/jobs/batch-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteJobsResponse"
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

    def batch_list_job_details_async(self, request):
        """批量查询任务详情

        根据任务ID批量查询任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListJobDetails
        :type request: :class:`huaweicloudsdkdrs.v3.BatchListJobDetailsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchListJobDetailsResponse`
        """
        http_info = self._batch_list_job_details_http_info(request)
        return self._call_api(**http_info)

    def batch_list_job_details_async_invoker(self, request):
        http_info = self._batch_list_job_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_job_details_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-detail",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListJobDetailsResponse"
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

    def batch_list_job_status_async(self, request):
        """批量查询任务状态

        根据任务ID批量查询任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListJobStatus
        :type request: :class:`huaweicloudsdkdrs.v3.BatchListJobStatusRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchListJobStatusResponse`
        """
        http_info = self._batch_list_job_status_http_info(request)
        return self._call_api(**http_info)

    def batch_list_job_status_async_invoker(self, request):
        http_info = self._batch_list_job_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_job_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-status",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListJobStatusResponse"
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

    def batch_list_progresses_async(self, request):
        """批量查询任务进度

        根据任务ID批量查询全量进度、增量时延信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListProgresses
        :type request: :class:`huaweicloudsdkdrs.v3.BatchListProgressesRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchListProgressesResponse`
        """
        http_info = self._batch_list_progresses_http_info(request)
        return self._call_api(**http_info)

    def batch_list_progresses_async_invoker(self, request):
        http_info = self._batch_list_progresses_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_progresses_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-progress",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListProgressesResponse"
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

    def batch_list_rpos_and_rtos_async(self, request):
        """批量查询RPO和RTO

        批量查询RPO和RTO。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListRposAndRtos
        :type request: :class:`huaweicloudsdkdrs.v3.BatchListRposAndRtosRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchListRposAndRtosResponse`
        """
        http_info = self._batch_list_rpos_and_rtos_http_info(request)
        return self._call_api(**http_info)

    def batch_list_rpos_and_rtos_async_invoker(self, request):
        http_info = self._batch_list_rpos_and_rtos_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_rpos_and_rtos_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-rpo-and-rto",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListRposAndRtosResponse"
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

    def batch_list_struct_detail_async(self, request):
        """批量查询灾备初始化对象详情

        根据任务ID批量查询灾备初始化对象详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListStructDetail
        :type request: :class:`huaweicloudsdkdrs.v3.BatchListStructDetailRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchListStructDetailResponse`
        """
        http_info = self._batch_list_struct_detail_http_info(request)
        return self._call_api(**http_info)

    def batch_list_struct_detail_async_invoker(self, request):
        http_info = self._batch_list_struct_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_struct_detail_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/{type}/batch-struct-detail",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListStructDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

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

    def batch_list_struct_process_async(self, request):
        """批量查询灾备初始化进度

        根据任务ID批量查询灾备初始化进度，虚拟id不支持查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchListStructProcess
        :type request: :class:`huaweicloudsdkdrs.v3.BatchListStructProcessRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchListStructProcessResponse`
        """
        http_info = self._batch_list_struct_process_http_info(request)
        return self._call_api(**http_info)

    def batch_list_struct_process_async_invoker(self, request):
        http_info = self._batch_list_struct_process_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_list_struct_process_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-struct-process",
            "request_type": request.__class__.__name__,
            "response_type": "BatchListStructProcessResponse"
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

    def batch_reset_password_async(self, request):
        """批量修改源库/目标库密码

        任务启动之后需要修改源库/目标库密码时调用此接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchResetPassword
        :type request: :class:`huaweicloudsdkdrs.v3.BatchResetPasswordRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchResetPasswordResponse`
        """
        http_info = self._batch_reset_password_http_info(request)
        return self._call_api(**http_info)

    def batch_reset_password_async_invoker(self, request):
        http_info = self._batch_reset_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_reset_password_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/jobs/batch-modify-pwd",
            "request_type": request.__class__.__name__,
            "response_type": "BatchResetPasswordResponse"
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

    def batch_restore_task_async(self, request):
        """批量续传/重试

        在迁移过程中由于不确定因素导致迁移任务失败，可通过重试功能，重新提交迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchRestoreTask
        :type request: :class:`huaweicloudsdkdrs.v3.BatchRestoreTaskRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchRestoreTaskResponse`
        """
        http_info = self._batch_restore_task_http_info(request)
        return self._call_api(**http_info)

    def batch_restore_task_async_invoker(self, request):
        http_info = self._batch_restore_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_restore_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-retry-task",
            "request_type": request.__class__.__name__,
            "response_type": "BatchRestoreTaskResponse"
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

    def batch_set_definer_async(self, request):
        """批量设置definer

        批量设置Definer迁移是否迁移到到该用户下。
        - 选择是：迁移后，所有源数据库对象的Definer都会迁移至该用户下，其他用户需要授权后才具有数据库对象权限。
        - 选择否：迁移后，将保持源数据库对象Definer定义不变，选择此选项，需要配合下一步用户权限迁移功能，将源数据库的用户全部迁移，这样才能保持源数据库的权限体系完全不变。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetDefiner
        :type request: :class:`huaweicloudsdkdrs.v3.BatchSetDefinerRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchSetDefinerResponse`
        """
        http_info = self._batch_set_definer_http_info(request)
        return self._call_api(**http_info)

    def batch_set_definer_async_invoker(self, request):
        http_info = self._batch_set_definer_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_definer_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-replace-definer",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetDefinerResponse"
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

    def batch_set_objects_async(self, request):
        """批量数据库对象选择

        迁移之前，选择需要迁移的数据库或者表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetObjects
        :type request: :class:`huaweicloudsdkdrs.v3.BatchSetObjectsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchSetObjectsResponse`
        """
        http_info = self._batch_set_objects_http_info(request)
        return self._call_api(**http_info)

    def batch_set_objects_async_invoker(self, request):
        http_info = self._batch_set_objects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_objects_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/jobs/batch-select-objects",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetObjectsResponse"
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

    def batch_set_policy_async(self, request):
        """批量设置同步策略

        - 批量设置同步策略，包括冲突策略、过滤DROP Datase、对象同步范围。
        - 设置kafka同步策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetPolicy
        :type request: :class:`huaweicloudsdkdrs.v3.BatchSetPolicyRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchSetPolicyResponse`
        """
        http_info = self._batch_set_policy_http_info(request)
        return self._call_api(**http_info)

    def batch_set_policy_async_invoker(self, request):
        http_info = self._batch_set_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-sync-policy",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetPolicyResponse"
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

    def batch_set_smn_async(self, request):
        """批量配置异常通知

        批量设置异常通知，已结束的任务不支持设置。
        - 支持选择已有的SMN主题和手动输入手机号、邮箱两种方式，具体根据自己使用情况选择
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetSmn
        :type request: :class:`huaweicloudsdkdrs.v3.BatchSetSmnRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchSetSmnResponse`
        """
        http_info = self._batch_set_smn_http_info(request)
        return self._call_api(**http_info)

    def batch_set_smn_async_invoker(self, request):
        http_info = self._batch_set_smn_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_smn_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-set-smn",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetSmnResponse"
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

    def batch_set_speed_async(self, request):
        """批量设置任务限速

        批量设置任务限速，任务创建成功后默认不限速。
        - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。
        - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSetSpeed
        :type request: :class:`huaweicloudsdkdrs.v3.BatchSetSpeedRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchSetSpeedResponse`
        """
        http_info = self._batch_set_speed_http_info(request)
        return self._call_api(**http_info)

    def batch_set_speed_async_invoker(self, request):
        http_info = self._batch_set_speed_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_set_speed_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/jobs/batch-limit-speed",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSetSpeedResponse"
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

    def batch_show_params_async(self, request):
        """批量获取数据库参数

        在进行数据库迁移时，为了确保迁移成功后业务应用的使用不受影响，数据复制服务提供了参数对比功能帮助您进行源库和目标库参数一致性对比，此接口可以获取源库和目标库的数据库参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchShowParams
        :type request: :class:`huaweicloudsdkdrs.v3.BatchShowParamsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchShowParamsResponse`
        """
        http_info = self._batch_show_params_http_info(request)
        return self._call_api(**http_info)

    def batch_show_params_async_invoker(self, request):
        http_info = self._batch_show_params_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_show_params_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-get-params",
            "request_type": request.__class__.__name__,
            "response_type": "BatchShowParamsResponse"
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

    def batch_start_jobs_async(self, request):
        """批量启动任务

        批量启动实时迁移、同步、灾备任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartJobs
        :type request: :class:`huaweicloudsdkdrs.v3.BatchStartJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchStartJobsResponse`
        """
        http_info = self._batch_start_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_start_jobs_async_invoker(self, request):
        http_info = self._batch_start_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-starting",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartJobsResponse"
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

    def batch_stop_jobs_async(self, request):
        """批量暂停任务

        批量暂停任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopJobs
        :type request: :class:`huaweicloudsdkdrs.v3.BatchStopJobsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchStopJobsResponse`
        """
        http_info = self._batch_stop_jobs_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_jobs_async_invoker(self, request):
        http_info = self._batch_stop_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_jobs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-pause-task",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopJobsResponse"
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

    def batch_switchover_async(self, request):
        """批量主备倒换

        批量主备倒换。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchSwitchover
        :type request: :class:`huaweicloudsdkdrs.v3.BatchSwitchoverRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchSwitchoverResponse`
        """
        http_info = self._batch_switchover_http_info(request)
        return self._call_api(**http_info)

    def batch_switchover_async_invoker(self, request):
        http_info = self._batch_switchover_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_switchover_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-switchover",
            "request_type": request.__class__.__name__,
            "response_type": "BatchSwitchoverResponse"
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

    def batch_update_job_async(self, request):
        """批量修改任务

        批量修改任务名称或描述，设置异常通知信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateJob
        :type request: :class:`huaweicloudsdkdrs.v3.BatchUpdateJobRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchUpdateJobResponse`
        """
        http_info = self._batch_update_job_http_info(request)
        return self._call_api(**http_info)

    def batch_update_job_async_invoker(self, request):
        http_info = self._batch_update_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/jobs/batch-modification",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateJobResponse"
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

    def batch_update_user_async(self, request):
        """批量更新迁移用户信息

        数据库的迁移过程中，迁移用户需要进行单独处理，该接口可以批量设置需要迁移的用户和角色。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateUser
        :type request: :class:`huaweicloudsdkdrs.v3.BatchUpdateUserRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchUpdateUserResponse`
        """
        http_info = self._batch_update_user_http_info(request)
        return self._call_api(**http_info)

    def batch_update_user_async_invoker(self, request):
        http_info = self._batch_update_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_user_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/jobs/batch-update-user",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateUserResponse"
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

    def batch_validate_clusters_connections_async(self, request):
        """批量测试连接-集群模式

        - 批量测试连接（集群模式）。
        - 主备任务测试连接
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchValidateClustersConnections
        :type request: :class:`huaweicloudsdkdrs.v3.BatchValidateClustersConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchValidateClustersConnectionsResponse`
        """
        http_info = self._batch_validate_clusters_connections_http_info(request)
        return self._call_api(**http_info)

    def batch_validate_clusters_connections_async_invoker(self, request):
        http_info = self._batch_validate_clusters_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_validate_clusters_connections_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/cluster/batch-connection",
            "request_type": request.__class__.__name__,
            "response_type": "BatchValidateClustersConnectionsResponse"
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

    def batch_validate_connections_async(self, request):
        """批量测试连接

        批量测试连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchValidateConnections
        :type request: :class:`huaweicloudsdkdrs.v3.BatchValidateConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.BatchValidateConnectionsResponse`
        """
        http_info = self._batch_validate_connections_http_info(request)
        return self._call_api(**http_info)

    def batch_validate_connections_async_invoker(self, request):
        http_info = self._batch_validate_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_validate_connections_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/batch-connection",
            "request_type": request.__class__.__name__,
            "response_type": "BatchValidateConnectionsResponse"
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

    def create_compare_task_async(self, request):
        """创建对比任务

        创建对比任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateCompareTask
        :type request: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResponse`
        """
        http_info = self._create_compare_task_http_info(request)
        return self._call_api(**http_info)

    def create_compare_task_async_invoker(self, request):
        http_info = self._create_compare_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_compare_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/create-compare-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCompareTaskResponse"
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

    def list_available_zone_async(self, request):
        """查询规格未售罄的可用区

        查询规格未售罄的可用区
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAvailableZone
        :type request: :class:`huaweicloudsdkdrs.v3.ListAvailableZoneRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.ListAvailableZoneResponse`
        """
        http_info = self._list_available_zone_http_info(request)
        return self._call_api(**http_info)

    def list_available_zone_async_invoker(self, request):
        http_info = self._list_available_zone_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_available_zone_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/available-zone",
            "request_type": request.__class__.__name__,
            "response_type": "ListAvailableZoneResponse"
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

    def list_compare_result_async(self, request):
        """查询对比结果

        查询对比结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListCompareResult
        :type request: :class:`huaweicloudsdkdrs.v3.ListCompareResultRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.ListCompareResultResponse`
        """
        http_info = self._list_compare_result_http_info(request)
        return self._call_api(**http_info)

    def list_compare_result_async_invoker(self, request):
        http_info = self._list_compare_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_compare_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/query-compare-result",
            "request_type": request.__class__.__name__,
            "response_type": "ListCompareResultResponse"
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

    def list_users_async(self, request):
        """获取源库迁移用户列表

        数据库的迁移过程中，迁移用户需要进行单独处理，该接口可以查询源库的用户信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUsers
        :type request: :class:`huaweicloudsdkdrs.v3.ListUsersRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.ListUsersResponse`
        """
        http_info = self._list_users_http_info(request)
        return self._call_api(**http_info)

    def list_users_async_invoker(self, request):
        http_info = self._list_users_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_users_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/jobs/{job_id}/get-src-user",
            "request_type": request.__class__.__name__,
            "response_type": "ListUsersResponse"
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

    def show_job_list_async(self, request):
        """查询租户任务列表

        查询租户任务列表，可以根据引擎类型，网络类型，任务状态，任务名称，任务ID进行查询。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobList
        :type request: :class:`huaweicloudsdkdrs.v3.ShowJobListRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.ShowJobListResponse`
        """
        http_info = self._show_job_list_http_info(request)
        return self._call_api(**http_info)

    def show_job_list_async_invoker(self, request):
        http_info = self._show_job_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_list_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobListResponse"
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

    def show_monitoring_data_async(self, request):
        """查询容灾监控数据

        根据任务ID查询容灾监控数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMonitoringData
        :type request: :class:`huaweicloudsdkdrs.v3.ShowMonitoringDataRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.ShowMonitoringDataResponse`
        """
        http_info = self._show_monitoring_data_http_info(request)
        return self._call_api(**http_info)

    def show_monitoring_data_async_invoker(self, request):
        http_info = self._show_monitoring_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_monitoring_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/disaster-recovery-monitoring-data",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMonitoringDataResponse"
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

    def show_quotas_async(self, request):
        """查询配额

        查询单租户在某一项目下DRS服务下的配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowQuotas
        :type request: :class:`huaweicloudsdkdrs.v3.ShowQuotasRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.ShowQuotasResponse`
        """
        http_info = self._show_quotas_http_info(request)
        return self._call_api(**http_info)

    def show_quotas_async_invoker(self, request):
        http_info = self._show_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_quotas_http_info(self, request):
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

    def update_params_async(self, request):
        """修改数据库参数

        修改数据库参数。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateParams
        :type request: :class:`huaweicloudsdkdrs.v3.UpdateParamsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.UpdateParamsResponse`
        """
        http_info = self._update_params_http_info(request)
        return self._call_api(**http_info)

    def update_params_async_invoker(self, request):
        http_info = self._update_params_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_params_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/jobs/{job_id}/params",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateParamsResponse"
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

    def update_tuning_params_async(self, request):
        """高级设置

        修改调优参数的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTuningParams
        :type request: :class:`huaweicloudsdkdrs.v3.UpdateTuningParamsRequest`
        :rtype: :class:`huaweicloudsdkdrs.v3.UpdateTuningParamsResponse`
        """
        http_info = self._update_tuning_params_http_info(request)
        return self._call_api(**http_info)

    def update_tuning_params_async_invoker(self, request):
        http_info = self._update_tuning_params_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_tuning_params_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/job/{job_id}/tuning-params/modify-params",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTuningParamsResponse"
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

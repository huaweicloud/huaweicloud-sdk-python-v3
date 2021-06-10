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


class DrsClient(Client):
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
        super(DrsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdrs.v3.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DrsClient":
            raise TypeError("client type error, support client type is DrsClient")

        return ClientBuilder(clazz)

    def batch_change_data(self, request):
        """批量数据加工

        数据复制服务支持对同步的对象进行加工，即可以为选择的对象添加规则。

        :param BatchChangeDataRequest request
        :return: BatchChangeDataResponse
        """
        return self.batch_change_data_with_http_info(request)

    def batch_change_data_with_http_info(self, request):
        """批量数据加工

        数据复制服务支持对同步的对象进行加工，即可以为选择的对象添加规则。

        :param BatchChangeDataRequest request
        :return: BatchChangeDataResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-transformation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchChangeDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_check_jobs(self, request):
        """批量预检查

        批量预检查，校验是否可进行迁移。

        :param BatchCheckJobsRequest request
        :return: BatchCheckJobsResponse
        """
        return self.batch_check_jobs_with_http_info(request)

    def batch_check_jobs_with_http_info(self, request):
        """批量预检查

        批量预检查，校验是否可进行迁移。

        :param BatchCheckJobsRequest request
        :return: BatchCheckJobsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-precheck',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCheckJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_check_results(self, request):
        """批量查询预检查结果

        批量查询任务的预检查结果。

        :param BatchCheckResultsRequest request
        :return: BatchCheckResultsResponse
        """
        return self.batch_check_results_with_http_info(request)

    def batch_check_results_with_http_info(self, request):
        """批量查询预检查结果

        批量查询任务的预检查结果。

        :param BatchCheckResultsRequest request
        :return: BatchCheckResultsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-precheck-result',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCheckResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_create_jobs(self, request):
        """批量创建任务

        根据请求参数不同，可以批量创建实时迁移、实时同步、实时灾备任务。

        :param BatchCreateJobsRequest request
        :return: BatchCreateJobsResponse
        """
        return self.batch_create_jobs_with_http_info(request)

    def batch_create_jobs_with_http_info(self, request):
        """批量创建任务

        根据请求参数不同，可以批量创建实时迁移、实时同步、实时灾备任务。

        :param BatchCreateJobsRequest request
        :return: BatchCreateJobsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-creation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchCreateJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_jobs(self, request):
        """批量结束任务或删除任务

        批量结束任务或删除实时迁移、实时同步、实时灾备任务。

        :param BatchDeleteJobsRequest request
        :return: BatchDeleteJobsResponse
        """
        return self.batch_delete_jobs_with_http_info(request)

    def batch_delete_jobs_with_http_info(self, request):
        """批量结束任务或删除任务

        批量结束任务或删除实时迁移、实时同步、实时灾备任务。

        :param BatchDeleteJobsRequest request
        :return: BatchDeleteJobsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-jobs',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_job_details(self, request):
        """批量查询任务详情

        根据任务ID批量查询任务详情。

        :param BatchListJobDetailsRequest request
        :return: BatchListJobDetailsResponse
        """
        return self.batch_list_job_details_with_http_info(request)

    def batch_list_job_details_with_http_info(self, request):
        """批量查询任务详情

        根据任务ID批量查询任务详情。

        :param BatchListJobDetailsRequest request
        :return: BatchListJobDetailsResponse
        """

        all_params = ['x_language', 'batch_query_job_req']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-detail',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListJobDetailsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_job_status(self, request):
        """批量查询任务状态

        根据任务ID批量查询任务状态。

        :param BatchListJobStatusRequest request
        :return: BatchListJobStatusResponse
        """
        return self.batch_list_job_status_with_http_info(request)

    def batch_list_job_status_with_http_info(self, request):
        """批量查询任务状态

        根据任务ID批量查询任务状态。

        :param BatchListJobStatusRequest request
        :return: BatchListJobStatusResponse
        """

        all_params = ['x_language', 'batch_query_job_req']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListJobStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_progresses(self, request):
        """批量查询任务进度

        根据任务ID批量查询全量进度、增量时延信息。

        :param BatchListProgressesRequest request
        :return: BatchListProgressesResponse
        """
        return self.batch_list_progresses_with_http_info(request)

    def batch_list_progresses_with_http_info(self, request):
        """批量查询任务进度

        根据任务ID批量查询全量进度、增量时延信息。

        :param BatchListProgressesRequest request
        :return: BatchListProgressesResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-progress',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListProgressesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_rpos_and_rtos(self, request):
        """批量查询RPO和RTO

        批量查询RPO和RTO。

        :param BatchListRposAndRtosRequest request
        :return: BatchListRposAndRtosResponse
        """
        return self.batch_list_rpos_and_rtos_with_http_info(request)

    def batch_list_rpos_and_rtos_with_http_info(self, request):
        """批量查询RPO和RTO

        批量查询RPO和RTO。

        :param BatchListRposAndRtosRequest request
        :return: BatchListRposAndRtosResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-rpo-and-rto',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListRposAndRtosResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_struct_detail(self, request):
        """批量查询灾备初始化对象详情

        根据任务ID批量查询灾备初始化对象详情。

        :param BatchListStructDetailRequest request
        :return: BatchListStructDetailResponse
        """
        return self.batch_list_struct_detail_with_http_info(request)

    def batch_list_struct_detail_with_http_info(self, request):
        """批量查询灾备初始化对象详情

        根据任务ID批量查询灾备初始化对象详情。

        :param BatchListStructDetailRequest request
        :return: BatchListStructDetailResponse
        """

        all_params = ['type', 'x_language', 'batch_query_struct_process']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'type' in local_var_params:
            path_params['type'] = local_var_params['type']

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
            resource_path='/v3/{project_id}/jobs/{type}/batch-struct-detail',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListStructDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_list_struct_process(self, request):
        """批量查询灾备初始化进度

        根据任务ID批量查询灾备初始化进度，虚拟id不支持查询。

        :param BatchListStructProcessRequest request
        :return: BatchListStructProcessResponse
        """
        return self.batch_list_struct_process_with_http_info(request)

    def batch_list_struct_process_with_http_info(self, request):
        """批量查询灾备初始化进度

        根据任务ID批量查询灾备初始化进度，虚拟id不支持查询。

        :param BatchListStructProcessRequest request
        :return: BatchListStructProcessResponse
        """

        all_params = ['x_language', 'batch_query_struct_process']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-struct-process',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchListStructProcessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_reset_password(self, request):
        """批量修改源库/目标库密码

        任务启动之后需要修改源库/目标库密码时调用此接口。

        :param BatchResetPasswordRequest request
        :return: BatchResetPasswordResponse
        """
        return self.batch_reset_password_with_http_info(request)

    def batch_reset_password_with_http_info(self, request):
        """批量修改源库/目标库密码

        任务启动之后需要修改源库/目标库密码时调用此接口。

        :param BatchResetPasswordRequest request
        :return: BatchResetPasswordResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-modify-pwd',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchResetPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_restore_task(self, request):
        """批量续传/重试

        在迁移过程中由于不确定因素导致迁移任务失败，可通过重试功能，重新提交迁移任务。

        :param BatchRestoreTaskRequest request
        :return: BatchRestoreTaskResponse
        """
        return self.batch_restore_task_with_http_info(request)

    def batch_restore_task_with_http_info(self, request):
        """批量续传/重试

        在迁移过程中由于不确定因素导致迁移任务失败，可通过重试功能，重新提交迁移任务。

        :param BatchRestoreTaskRequest request
        :return: BatchRestoreTaskResponse
        """

        all_params = ['x_language', 'jobs']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-retry-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchRestoreTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_set_definer(self, request):
        """批量设置definer

        批量设置Definer迁移是否迁移到到该用户下。 - 选择是：迁移后，所有源数据库对象的Definer都会迁移至该用户下，其他用户需要授权后才具有数据库对象权限。 - 选择否：迁移后，将保持源数据库对象Definer定义不变，选择此选项，需要配合下一步用户权限迁移功能，将源数据库的用户全部迁移，这样才能保持源数据库的权限体系完全不变。

        :param BatchSetDefinerRequest request
        :return: BatchSetDefinerResponse
        """
        return self.batch_set_definer_with_http_info(request)

    def batch_set_definer_with_http_info(self, request):
        """批量设置definer

        批量设置Definer迁移是否迁移到到该用户下。 - 选择是：迁移后，所有源数据库对象的Definer都会迁移至该用户下，其他用户需要授权后才具有数据库对象权限。 - 选择否：迁移后，将保持源数据库对象Definer定义不变，选择此选项，需要配合下一步用户权限迁移功能，将源数据库的用户全部迁移，这样才能保持源数据库的权限体系完全不变。

        :param BatchSetDefinerRequest request
        :return: BatchSetDefinerResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-replace-definer',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchSetDefinerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_set_objects(self, request):
        """批量数据库对象选择

        迁移之前，选择需要迁移的数据库或者表。

        :param BatchSetObjectsRequest request
        :return: BatchSetObjectsResponse
        """
        return self.batch_set_objects_with_http_info(request)

    def batch_set_objects_with_http_info(self, request):
        """批量数据库对象选择

        迁移之前，选择需要迁移的数据库或者表。

        :param BatchSetObjectsRequest request
        :return: BatchSetObjectsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-select-objects',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchSetObjectsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_set_speed(self, request):
        """批量设置任务限速

        批量设置任务限速，任务创建成功后默认不限速。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :param BatchSetSpeedRequest request
        :return: BatchSetSpeedResponse
        """
        return self.batch_set_speed_with_http_info(request)

    def batch_set_speed_with_http_info(self, request):
        """批量设置任务限速

        批量设置任务限速，任务创建成功后默认不限速。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :param BatchSetSpeedRequest request
        :return: BatchSetSpeedResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-limit-speed',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchSetSpeedResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_show_params(self, request):
        """批量获取数据库参数

        在进行数据库迁移时，为了确保迁移成功后业务应用的使用不受影响，数据复制服务提供了参数对比功能帮助您进行源库和目标库参数一致性对比，此接口可以获取源库和目标库的数据库参数。

        :param BatchShowParamsRequest request
        :return: BatchShowParamsResponse
        """
        return self.batch_show_params_with_http_info(request)

    def batch_show_params_with_http_info(self, request):
        """批量获取数据库参数

        在进行数据库迁移时，为了确保迁移成功后业务应用的使用不受影响，数据复制服务提供了参数对比功能帮助您进行源库和目标库参数一致性对比，此接口可以获取源库和目标库的数据库参数。

        :param BatchShowParamsRequest request
        :return: BatchShowParamsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-get-params',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchShowParamsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_start_jobs(self, request):
        """批量启动任务

        批量启动实时迁移、同步、灾备任务。

        :param BatchStartJobsRequest request
        :return: BatchStartJobsResponse
        """
        return self.batch_start_jobs_with_http_info(request)

    def batch_start_jobs_with_http_info(self, request):
        """批量启动任务

        批量启动实时迁移、同步、灾备任务。

        :param BatchStartJobsRequest request
        :return: BatchStartJobsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-starting',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStartJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_stop_jobs(self, request):
        """批量暂停任务

        批量暂停任务。

        :param BatchStopJobsRequest request
        :return: BatchStopJobsResponse
        """
        return self.batch_stop_jobs_with_http_info(request)

    def batch_stop_jobs_with_http_info(self, request):
        """批量暂停任务

        批量暂停任务。

        :param BatchStopJobsRequest request
        :return: BatchStopJobsResponse
        """

        all_params = ['x_language', 'req']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-pause-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStopJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_switchover(self, request):
        """批量主备倒换

        批量主备倒换。

        :param BatchSwitchoverRequest request
        :return: BatchSwitchoverResponse
        """
        return self.batch_switchover_with_http_info(request)

    def batch_switchover_with_http_info(self, request):
        """批量主备倒换

        批量主备倒换。

        :param BatchSwitchoverRequest request
        :return: BatchSwitchoverResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-switchover',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchSwitchoverResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_update_job(self, request):
        """批量修改任务

        批量修改任务名称或描述，设置异常通知信息。

        :param BatchUpdateJobRequest request
        :return: BatchUpdateJobResponse
        """
        return self.batch_update_job_with_http_info(request)

    def batch_update_job_with_http_info(self, request):
        """批量修改任务

        批量修改任务名称或描述，设置异常通知信息。

        :param BatchUpdateJobRequest request
        :return: BatchUpdateJobResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-modification',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_update_user(self, request):
        """批量更新迁移用户信息

        数据库的迁移过程中，迁移用户需要进行单独处理，该接口可以批量设置需要迁移的用户和角色。

        :param BatchUpdateUserRequest request
        :return: BatchUpdateUserResponse
        """
        return self.batch_update_user_with_http_info(request)

    def batch_update_user_with_http_info(self, request):
        """批量更新迁移用户信息

        数据库的迁移过程中，迁移用户需要进行单独处理，该接口可以批量设置需要迁移的用户和角色。

        :param BatchUpdateUserRequest request
        :return: BatchUpdateUserResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-update-user',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchUpdateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_validate_clusters_connections(self, request):
        """批量测试连接-集群模式

        批量测试连接（集群模式）。

        :param BatchValidateClustersConnectionsRequest request
        :return: BatchValidateClustersConnectionsResponse
        """
        return self.batch_validate_clusters_connections_with_http_info(request)

    def batch_validate_clusters_connections_with_http_info(self, request):
        """批量测试连接-集群模式

        批量测试连接（集群模式）。

        :param BatchValidateClustersConnectionsRequest request
        :return: BatchValidateClustersConnectionsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/cluster/batch-connection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchValidateClustersConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_validate_connections(self, request):
        """批量测试连接

        批量测试连接。

        :param BatchValidateConnectionsRequest request
        :return: BatchValidateConnectionsResponse
        """
        return self.batch_validate_connections_with_http_info(request)

    def batch_validate_connections_with_http_info(self, request):
        """批量测试连接

        批量测试连接。

        :param BatchValidateConnectionsRequest request
        :return: BatchValidateConnectionsResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/batch-connection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchValidateConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_compare_task(self, request):
        """创建对比任务

        创建对比任务。

        :param CreateCompareTaskRequest request
        :return: CreateCompareTaskResponse
        """
        return self.create_compare_task_with_http_info(request)

    def create_compare_task_with_http_info(self, request):
        """创建对比任务

        创建对比任务。

        :param CreateCompareTaskRequest request
        :return: CreateCompareTaskResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/create-compare-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateCompareTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_compare_result(self, request):
        """查询对比结果

        查询对比结果。

        :param ListCompareResultRequest request
        :return: ListCompareResultResponse
        """
        return self.list_compare_result_with_http_info(request)

    def list_compare_result_with_http_info(self, request):
        """查询对比结果

        查询对比结果。

        :param ListCompareResultRequest request
        :return: ListCompareResultResponse
        """

        all_params = ['x_language', 'request_body']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/query-compare-result',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListCompareResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_users(self, request):
        """获取源库迁移用户列表

        数据库的迁移过程中，迁移用户需要进行单独处理，该接口可以查询源库的用户信息。

        :param ListUsersRequest request
        :return: ListUsersResponse
        """
        return self.list_users_with_http_info(request)

    def list_users_with_http_info(self, request):
        """获取源库迁移用户列表

        数据库的迁移过程中，迁移用户需要进行单独处理，该接口可以查询源库的用户信息。

        :param ListUsersRequest request
        :return: ListUsersResponse
        """

        all_params = ['x_language', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/jobs/{job_id}/get-src-user',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job_list(self, request):
        """查询租户任务列表

        查询租户任务列表，可以根据引擎类型，网络类型，任务状态，任务名称，任务ID进行查询。

        :param ShowJobListRequest request
        :return: ShowJobListResponse
        """
        return self.show_job_list_with_http_info(request)

    def show_job_list_with_http_info(self, request):
        """查询租户任务列表

        查询租户任务列表，可以根据引擎类型，网络类型，任务状态，任务名称，任务ID进行查询。

        :param ShowJobListRequest request
        :return: ShowJobListResponse
        """

        all_params = ['x_language', 'query_jobs_req_v3']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_monitoring_data(self, request):
        """查询容灾监控数据

        根据任务ID查询容灾监控数据。

        :param ShowMonitoringDataRequest request
        :return: ShowMonitoringDataResponse
        """
        return self.show_monitoring_data_with_http_info(request)

    def show_monitoring_data_with_http_info(self, request):
        """查询容灾监控数据

        根据任务ID查询容灾监控数据。

        :param ShowMonitoringDataRequest request
        :return: ShowMonitoringDataResponse
        """

        all_params = ['x_language', 'req']
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
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v3/{project_id}/jobs/disaster-recovery-monitoring-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMonitoringDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_quotas(self, request):
        """查询配额

        查询单租户在DRS服务下的配额信息。

        :param ShowQuotasRequest request
        :return: ShowQuotasResponse
        """
        return self.show_quotas_with_http_info(request)

    def show_quotas_with_http_info(self, request):
        """查询配额

        查询单租户在DRS服务下的配额信息。

        :param ShowQuotasRequest request
        :return: ShowQuotasResponse
        """

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


    def update_params(self, request):
        """修改数据库参数

        修改数据库参数。

        :param UpdateParamsRequest request
        :return: UpdateParamsResponse
        """
        return self.update_params_with_http_info(request)

    def update_params_with_http_info(self, request):
        """修改数据库参数

        修改数据库参数。

        :param UpdateParamsRequest request
        :return: UpdateParamsResponse
        """

        all_params = ['job_id', 'x_language', 'request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/jobs/{job_id}/params',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateParamsResponse',
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

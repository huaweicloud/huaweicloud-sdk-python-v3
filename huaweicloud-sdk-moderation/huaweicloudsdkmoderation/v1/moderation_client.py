# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils


class ModerationClient(Client):
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
        super(ModerationClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmoderation.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}



    def run_image_batch_moderation(self, request):
        """图像内容检测（批量）

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。

        :param RunImageBatchModerationRequest request
        :return: RunImageBatchModerationResponse
        """
        return self.run_image_batch_moderation_with_http_info(request)

    def run_image_batch_moderation_with_http_info(self, request):
        """图像内容检测（批量）

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。

        :param RunImageBatchModerationRequest request
        :return: tuple(RunImageBatchModerationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.0/moderation/image/batch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunImageBatchModerationResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_moderation(self, request):
        """图像内容检测

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。

        :param RunImageModerationRequest request
        :return: RunImageModerationResponse
        """
        return self.run_image_moderation_with_http_info(request)

    def run_image_moderation_with_http_info(self, request):
        """图像内容检测

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。

        :param RunImageModerationRequest request
        :return: tuple(RunImageModerationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['image_detection_req']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.0/moderation/image', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunImageModerationResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_text_moderation(self, request):
        """文本内容检测

        分析并识别用户上传的文本内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户。

        :param RunTextModerationRequest request
        :return: RunTextModerationResponse
        """
        return self.run_text_moderation_with_http_info(request)

    def run_text_moderation_with_http_info(self, request):
        """文本内容检测

        分析并识别用户上传的文本内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户。

        :param RunTextModerationRequest request
        :return: tuple(RunTextModerationResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['text_detection_req']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.0/moderation/text', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunTextModerationResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def run_check_result(self, request):
        """图像内容检测（异步批量）- 处理结果查询

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。 > 说明： 任务最长保留时间为30分钟，过期后会被清理掉。建议在任务提交后，每30s进行一次周期查询。 

        :param RunCheckResultRequest request
        :return: RunCheckResultResponse
        """
        return self.run_check_result_with_http_info(request)

    def run_check_result_with_http_info(self, request):
        """图像内容检测（异步批量）- 处理结果查询

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。 > 说明： 任务最长保留时间为30分钟，过期后会被清理掉。建议在任务提交后，每30s进行一次周期查询。 

        :param RunCheckResultRequest request
        :return: tuple(RunCheckResultResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['job_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1.0/moderation/image/batch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunCheckResultResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_check_task_jobs(self, request):
        """图像内容检测（批量）- 任务列表查询

        查询批量图像内容检测任务列表，可通过指定任务状态查询来对任务列表进行过滤。

        :param RunCheckTaskJobsRequest request
        :return: RunCheckTaskJobsResponse
        """
        return self.run_check_task_jobs_with_http_info(request)

    def run_check_task_jobs_with_http_info(self, request):
        """图像内容检测（批量）- 任务列表查询

        查询批量图像内容检测任务列表，可通过指定任务状态查询来对任务列表进行过滤。

        :param RunCheckTaskJobsRequest request
        :return: tuple(RunCheckTaskJobsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['status']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}

        form_params = []

        body_params = None

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        auth_settings = []

        return self.call_api(
            '/v1.0/moderation/image/batch/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunCheckTaskJobsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_task_sumbit(self, request):
        """图像内容检测（批量）- 任务提交

        提交批量图像内容检测任务，返回任务标识，任务标识可用于查询任务结果。此接口为异步接口，相对于批量接口，支持更大图片列表批次。

        :param RunTaskSumbitRequest request
        :return: RunTaskSumbitResponse
        """
        return self.run_task_sumbit_with_http_info(request)

    def run_task_sumbit_with_http_info(self, request):
        """图像内容检测（批量）- 任务提交

        提交批量图像内容检测任务，返回任务标识，任务标识可用于查询任务结果。此接口为异步接口，相对于批量接口，支持更大图片列表批次。

        :param RunTaskSumbitRequest request
        :return: tuple(RunTaskSumbitResponse, status_code(int), headers(HTTPHeaderDict))
        """

        all_params = ['body']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        header_params['Accept'] = http_utils.select_header_accept(
            ['*/*', 'application/json'])

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])
        auth_settings = []

        return self.call_api(
            '/v1.0/moderation/image/batch/jobs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunTaskSumbitResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, response_type=None, auth_settings=None, collection_formats=None,
                 request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :return:
            Return the response directly.
        """
        return self.do_http_request(method, resource_path, path_params,
                                    query_params, header_params, body, post_params,
                                    response_type, collection_formats, request_type)
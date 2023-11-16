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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmoderation'")


class ModerationClient(Client):
    def __init__(self):
        super(ModerationClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmoderation.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ModerationClient":
                raise TypeError("client type error, support client type is ModerationClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def run_check_result(self, request):
        """处理结果查询

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。
        &gt; 任务最长保留时间为30分钟，过期后会被清理掉。建议在任务提交后，每30s进行一次周期查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCheckResult
        :type request: :class:`huaweicloudsdkmoderation.v2.RunCheckResultRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunCheckResultResponse`
        """
        http_info = self._run_check_result_http_info(request)
        return self._call_api(**http_info)

    def run_check_result_invoker(self, request):
        http_info = self._run_check_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_check_result_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/moderation/image/batch",
            "request_type": request.__class__.__name__,
            "response_type": "RunCheckResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))

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

    def run_check_task_jobs(self, request):
        """任务列表查询

        查询批量图像内容审核任务列表，可通过指定任务状态查询来对任务列表进行过滤。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCheckTaskJobs
        :type request: :class:`huaweicloudsdkmoderation.v2.RunCheckTaskJobsRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunCheckTaskJobsResponse`
        """
        http_info = self._run_check_task_jobs_http_info(request)
        return self._call_api(**http_info)

    def run_check_task_jobs_invoker(self, request):
        http_info = self._run_check_task_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_check_task_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/moderation/image/batch/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunCheckTaskJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def run_image_batch_moderation(self, request):
        """图像内容审核（批量）

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunImageBatchModeration
        :type request: :class:`huaweicloudsdkmoderation.v2.RunImageBatchModerationRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunImageBatchModerationResponse`
        """
        http_info = self._run_image_batch_moderation_http_info(request)
        return self._call_api(**http_info)

    def run_image_batch_moderation_invoker(self, request):
        http_info = self._run_image_batch_moderation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_image_batch_moderation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/moderation/image/batch",
            "request_type": request.__class__.__name__,
            "response_type": "RunImageBatchModerationResponse"
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

    def run_image_moderation(self, request):
        """图像内容审核

        分析并识别用户上传的图像内容是否有敏感内容（如涉及政治人物、暴恐元素、涉黄内容等），并将识别结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunImageModeration
        :type request: :class:`huaweicloudsdkmoderation.v2.RunImageModerationRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunImageModerationResponse`
        """
        http_info = self._run_image_moderation_http_info(request)
        return self._call_api(**http_info)

    def run_image_moderation_invoker(self, request):
        http_info = self._run_image_moderation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_image_moderation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/moderation/image",
            "request_type": request.__class__.__name__,
            "response_type": "RunImageModerationResponse"
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

    def run_moderation_audio(self, request):
        """语音内容审核

        分析并识别用户上传的语音内容是否有敏感内容（如色情、政治等），并将识别结果 返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunModerationAudio
        :type request: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunModerationAudioResponse`
        """
        http_info = self._run_moderation_audio_http_info(request)
        return self._call_api(**http_info)

    def run_moderation_audio_invoker(self, request):
        http_info = self._run_moderation_audio_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_moderation_audio_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/moderation/voice",
            "request_type": request.__class__.__name__,
            "response_type": "RunModerationAudioResponse"
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

    def run_task_sumbit(self, request):
        """任务提交

        提交批量图像内容审核任务，返回任务标识，任务标识可用于查询任务结果。此接口为异步接口，相对于批量接口，支持更大图片列表批次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTaskSumbit
        :type request: :class:`huaweicloudsdkmoderation.v2.RunTaskSumbitRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunTaskSumbitResponse`
        """
        http_info = self._run_task_sumbit_http_info(request)
        return self._call_api(**http_info)

    def run_task_sumbit_invoker(self, request):
        http_info = self._run_task_sumbit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_task_sumbit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/moderation/image/batch/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunTaskSumbitResponse"
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

    def run_text_moderation(self, request):
        """文本内容审核

        分析并识别用户上传的文本内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTextModeration
        :type request: :class:`huaweicloudsdkmoderation.v2.RunTextModerationRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v2.RunTextModerationResponse`
        """
        http_info = self._run_text_moderation_http_info(request)
        return self._call_api(**http_info)

    def run_text_moderation_invoker(self, request):
        http_info = self._run_text_moderation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_text_moderation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/moderation/text",
            "request_type": request.__class__.__name__,
            "response_type": "RunTextModerationResponse"
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

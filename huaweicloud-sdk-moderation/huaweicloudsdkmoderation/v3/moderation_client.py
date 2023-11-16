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
        self.model_package = importlib.import_module("huaweicloudsdkmoderation.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ModerationClient":
                raise TypeError("client type error, support client type is ModerationClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def check_image_moderation(self, request):
        """图像内容审核

        分析并识别用户上传的图像内容是否有敏感内容（如涉及暴恐元素、涉黄内容等），并将识别结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckImageModeration
        :type request: :class:`huaweicloudsdkmoderation.v3.CheckImageModerationRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.CheckImageModerationResponse`
        """
        http_info = self._check_image_moderation_http_info(request)
        return self._call_api(**http_info)

    def check_image_moderation_invoker(self, request):
        http_info = self._check_image_moderation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_image_moderation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/image",
            "request_type": request.__class__.__name__,
            "response_type": "CheckImageModerationResponse"
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

    def run_close_audio_stream_moderation_job(self, request):
        """关闭音频流内容审核作业

        关闭音频流内容审核作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCloseAudioStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCloseAudioStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCloseAudioStreamModerationJobResponse`
        """
        http_info = self._run_close_audio_stream_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_close_audio_stream_moderation_job_invoker(self, request):
        http_info = self._run_close_audio_stream_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_close_audio_stream_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/audio-stream/jobs/stop/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunCloseAudioStreamModerationJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def run_close_video_stream_moderation_job(self, request):
        """关闭视频流内容审核作业

        关闭视频流审核接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCloseVideoStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCloseVideoStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCloseVideoStreamModerationJobResponse`
        """
        http_info = self._run_close_video_stream_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_close_video_stream_moderation_job_invoker(self, request):
        http_info = self._run_close_video_stream_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_close_video_stream_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/video-stream/jobs/stop/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunCloseVideoStreamModerationJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def run_create_audio_moderation_job(self, request):
        """创建音频内容审核作业

        分析并识别用户上传的音频内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateAudioModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioModerationJobResponse`
        """
        http_info = self._run_create_audio_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_create_audio_moderation_job_invoker(self, request):
        http_info = self._run_create_audio_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_create_audio_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/audio/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunCreateAudioModerationJobResponse"
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

    def run_create_audio_stream_moderation_job(self, request):
        """创建音频流内容审核作业

        创建音频流内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateAudioStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioStreamModerationJobResponse`
        """
        http_info = self._run_create_audio_stream_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_create_audio_stream_moderation_job_invoker(self, request):
        http_info = self._run_create_audio_stream_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_create_audio_stream_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/audio-stream/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunCreateAudioStreamModerationJobResponse"
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

    def run_create_document_moderation_job(self, request):
        """创建文档内容审核作业

        创建文档内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateDocumentModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateDocumentModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateDocumentModerationJobResponse`
        """
        http_info = self._run_create_document_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_create_document_moderation_job_invoker(self, request):
        http_info = self._run_create_document_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_create_document_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/document/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunCreateDocumentModerationJobResponse"
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

    def run_create_video_moderation_job(self, request):
        """创建视频内容审核作业

        创建视频内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateVideoModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoModerationJobResponse`
        """
        http_info = self._run_create_video_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_create_video_moderation_job_invoker(self, request):
        http_info = self._run_create_video_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_create_video_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/video/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunCreateVideoModerationJobResponse"
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

    def run_create_video_stream_moderation_job(self, request):
        """创建视频流内容审核作业

        创建视频流内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateVideoStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoStreamModerationJobResponse`
        """
        http_info = self._run_create_video_stream_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_create_video_stream_moderation_job_invoker(self, request):
        http_info = self._run_create_video_stream_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_create_video_stream_moderation_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/moderation/video-stream/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "RunCreateVideoStreamModerationJobResponse"
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

    def run_query_audio_moderation_job(self, request):
        """查询音频内容审核作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueryAudioModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunQueryAudioModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunQueryAudioModerationJobResponse`
        """
        http_info = self._run_query_audio_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_query_audio_moderation_job_invoker(self, request):
        http_info = self._run_query_audio_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_query_audio_moderation_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/moderation/audio/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunQueryAudioModerationJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def run_query_document_moderation_job(self, request):
        """查询文档审核作业结果

        查询文档审核结果接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueryDocumentModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunQueryDocumentModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunQueryDocumentModerationJobResponse`
        """
        http_info = self._run_query_document_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_query_document_moderation_job_invoker(self, request):
        http_info = self._run_query_document_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_query_document_moderation_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/moderation/document/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunQueryDocumentModerationJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def run_query_video_moderation_job(self, request):
        """查询视频内容审核作业

        查询视频审核作业处理状态与结果，并将识别结果返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueryVideoModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunQueryVideoModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunQueryVideoModerationJobResponse`
        """
        http_info = self._run_query_video_moderation_job_http_info(request)
        return self._call_api(**http_info)

    def run_query_video_moderation_job_invoker(self, request):
        http_info = self._run_query_video_moderation_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_query_video_moderation_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/moderation/video/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "RunQueryVideoModerationJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def run_text_moderation(self, request):
        """文本内容审核

        分析并识别用户上传的文本内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTextModeration
        :type request: :class:`huaweicloudsdkmoderation.v3.RunTextModerationRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunTextModerationResponse`
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
            "resource_path": "/v3/{project_id}/moderation/text",
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

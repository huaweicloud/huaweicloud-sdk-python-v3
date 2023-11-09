# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


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
        return self._check_image_moderation_with_http_info(request)

    def _check_image_moderation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckImageModerationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_close_audio_stream_moderation_job(self, request):
        """关闭音频流内容审核作业

        关闭音频流内容审核作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCloseAudioStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCloseAudioStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCloseAudioStreamModerationJobResponse`
        """
        return self._run_close_audio_stream_moderation_job_with_http_info(request)

    def _run_close_audio_stream_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v3/{project_id}/moderation/audio-stream/jobs/stop/{job_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCloseAudioStreamModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_close_video_stream_moderation_job(self, request):
        """关闭视频流内容审核作业

        关闭视频流审核接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCloseVideoStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCloseVideoStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCloseVideoStreamModerationJobResponse`
        """
        return self._run_close_video_stream_moderation_job_with_http_info(request)

    def _run_close_video_stream_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v3/{project_id}/moderation/video-stream/jobs/stop/{job_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCloseVideoStreamModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_create_audio_moderation_job(self, request):
        """创建音频内容审核作业

        分析并识别用户上传的音频内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateAudioModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioModerationJobResponse`
        """
        return self._run_create_audio_moderation_job_with_http_info(request)

    def _run_create_audio_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/audio/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCreateAudioModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_create_audio_stream_moderation_job(self, request):
        """创建音频流内容审核作业

        创建音频流内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateAudioStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateAudioStreamModerationJobResponse`
        """
        return self._run_create_audio_stream_moderation_job_with_http_info(request)

    def _run_create_audio_stream_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/audio-stream/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCreateAudioStreamModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_create_document_moderation_job(self, request):
        """创建文档内容审核作业

        创建文档内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateDocumentModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateDocumentModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateDocumentModerationJobResponse`
        """
        return self._run_create_document_moderation_job_with_http_info(request)

    def _run_create_document_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/document/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCreateDocumentModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_create_video_moderation_job(self, request):
        """创建视频内容审核作业

        创建视频内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateVideoModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoModerationJobResponse`
        """
        return self._run_create_video_moderation_job_with_http_info(request)

    def _run_create_video_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/video/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCreateVideoModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_create_video_stream_moderation_job(self, request):
        """创建视频流内容审核作业

        创建视频流内容审核作业，创建成功会将作业ID返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunCreateVideoStreamModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoStreamModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunCreateVideoStreamModerationJobResponse`
        """
        return self._run_create_video_stream_moderation_job_with_http_info(request)

    def _run_create_video_stream_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/video-stream/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCreateVideoStreamModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_audio_moderation_job(self, request):
        """查询音频内容审核作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueryAudioModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunQueryAudioModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunQueryAudioModerationJobResponse`
        """
        return self._run_query_audio_moderation_job_with_http_info(request)

    def _run_query_audio_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v3/{project_id}/moderation/audio/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunQueryAudioModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_document_moderation_job(self, request):
        """查询文档审核作业结果

        查询文档审核结果接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueryDocumentModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunQueryDocumentModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunQueryDocumentModerationJobResponse`
        """
        return self._run_query_document_moderation_job_with_http_info(request)

    def _run_query_document_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v3/{project_id}/moderation/document/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunQueryDocumentModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_video_moderation_job(self, request):
        """查询视频内容审核作业

        查询视频审核作业处理状态与结果，并将识别结果返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunQueryVideoModerationJob
        :type request: :class:`huaweicloudsdkmoderation.v3.RunQueryVideoModerationJobRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunQueryVideoModerationJobResponse`
        """
        return self._run_query_video_moderation_job_with_http_info(request)

    def _run_query_video_moderation_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v3/{project_id}/moderation/video/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunQueryVideoModerationJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_text_moderation(self, request):
        """文本内容审核

        分析并识别用户上传的文本内容是否有敏感内容（如色情、政治等），并将识别结果返回给用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTextModeration
        :type request: :class:`huaweicloudsdkmoderation.v3.RunTextModerationRequest`
        :rtype: :class:`huaweicloudsdkmoderation.v3.RunTextModerationResponse`
        """
        return self._run_text_moderation_with_http_info(request)

    def _run_text_moderation_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            resource_path='/v3/{project_id}/moderation/text',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunTextModerationResponse',
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

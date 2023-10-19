# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class SisClient(Client):
    def __init__(self):
        super(SisClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksis.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SisClient":
                raise TypeError("client type error, support client type is SisClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def collect_transcriber_job(self, request):
        """获取录音文件识别结果

        该接口用于获取录音文件识别结果及识别状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CollectTranscriberJob
        :type request: :class:`huaweicloudsdksis.v1.CollectTranscriberJobRequest`
        :rtype: :class:`huaweicloudsdksis.v1.CollectTranscriberJobResponse`
        """
        return self._collect_transcriber_job_with_http_info(request)

    def _collect_transcriber_job_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/asr/transcriber/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CollectTranscriberJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_vocabulary(self, request):
        """创建热词表

        新建一个热词表，创建成功返回id。每个用户限制创建10个热词表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVocabulary
        :type request: :class:`huaweicloudsdksis.v1.CreateVocabularyRequest`
        :rtype: :class:`huaweicloudsdksis.v1.CreateVocabularyResponse`
        """
        return self._create_vocabulary_with_http_info(request)

    def _create_vocabulary_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/asr/vocabularies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVocabularyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_vocabulary(self, request):
        """删除热词表

        通过热词表id删除热词表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVocabulary
        :type request: :class:`huaweicloudsdksis.v1.DeleteVocabularyRequest`
        :rtype: :class:`huaweicloudsdksis.v1.DeleteVocabularyResponse`
        """
        return self._delete_vocabulary_with_http_info(request)

    def _delete_vocabulary_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vocabulary_id' in local_var_params:
            path_params['vocabulary_id'] = local_var_params['vocabulary_id']

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
            resource_path='/v1/{project_id}/asr/vocabularies/{vocabulary_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVocabularyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def push_transcriber_jobs(self, request):
        """提交录音文件识别任务

        **录音文件识别**
        录音文件识别接口，用于识别长录音文件，录音文件放在华为云OBS（对象存储服务）上。
        
        由于录音文件识别通常会需要较长的时间，因此识别是异步的，也即接口分为创建识别任务和查询任务状态两个接口。创建识别任务接口创建任务完成后返回，然后用户通过调用查询任务状态接口来获得转写状态和结果。
        
        **功能介绍**
        该接口用于提交录音文件识别任务，其中录音文件保存在用户的OBS桶中。用户开通录音识别服务时，需授权录音文件引擎读取用户OBS桶权限。
        
        接口约束
        录音时长不超过5小时，文件大小不超过300M，识别结果保存72小时（从识别完成的时间算起）。72小时后如果再访问，将会返回 \&quot;task id is not found\&quot;错误。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PushTranscriberJobs
        :type request: :class:`huaweicloudsdksis.v1.PushTranscriberJobsRequest`
        :rtype: :class:`huaweicloudsdksis.v1.PushTranscriberJobsResponse`
        """
        return self._push_transcriber_jobs_with_http_info(request)

    def _push_transcriber_jobs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/asr/transcriber/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PushTranscriberJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_flash_asr(self, request):
        """录音文件识别极速版

        极速版ASR(Restful API 接口, 适用于音频(文件大小&lt;&#x3D;100M,语音时长&lt;&#x3D;30分钟)文件的同步识别。
        此接口以POST方式一次性上传整个音频或从华为OBS中下载音频， 识别结果将在请求响应中即刻返回，用于语音文件极速转写，质检分析的离线场景。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeFlashAsr
        :type request: :class:`huaweicloudsdksis.v1.RecognizeFlashAsrRequest`
        :rtype: :class:`huaweicloudsdksis.v1.RecognizeFlashAsrResponse`
        """
        return self._recognize_flash_asr_with_http_info(request)

    def _recognize_flash_asr_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))
        if 'audio_format' in local_var_params:
            query_params.append(('audio_format', local_var_params['audio_format']))
        if 'add_punc' in local_var_params:
            query_params.append(('add_punc', local_var_params['add_punc']))
        if 'digit_norm' in local_var_params:
            query_params.append(('digit_norm', local_var_params['digit_norm']))
        if 'need_word_info' in local_var_params:
            query_params.append(('need_word_info', local_var_params['need_word_info']))
        if 'vocabulary_id' in local_var_params:
            query_params.append(('vocabulary_id', local_var_params['vocabulary_id']))
        if 'obs_bucket_name' in local_var_params:
            query_params.append(('obs_bucket_name', local_var_params['obs_bucket_name']))
        if 'obs_object_key' in local_var_params:
            query_params.append(('obs_object_key', local_var_params['obs_object_key']))
        if 'first_channel_only' in local_var_params:
            query_params.append(('first_channel_only', local_var_params['first_channel_only']))

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
            resource_path='/v1/{project_id}/asr/flash',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeFlashAsrResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_short_audio(self, request):
        """一句话识别

        一句话识别接口，用于短语音的同步识别。一次性上传整个音频，响应中即返回识别结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeShortAudio
        :type request: :class:`huaweicloudsdksis.v1.RecognizeShortAudioRequest`
        :rtype: :class:`huaweicloudsdksis.v1.RecognizeShortAudioResponse`
        """
        return self._recognize_short_audio_with_http_info(request)

    def _recognize_short_audio_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/asr/short-audio',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeShortAudioResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_tts(self, request):
        """语音合成

        语音合成，是一种将文本转换成逼真语音的服务。用户通过实时访问和调用API获取语音合成结果，将用户输入的文字合成为音频。通过音色选择、自定义音量、语速，为企业和个人提供个性化的发音服务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunTts
        :type request: :class:`huaweicloudsdksis.v1.RunTtsRequest`
        :rtype: :class:`huaweicloudsdksis.v1.RunTtsResponse`
        """
        return self._run_tts_with_http_info(request)

    def _run_tts_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/tts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunTtsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vocabularies(self, request):
        """查询热词表列表

        查询用户所有热词表列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVocabularies
        :type request: :class:`huaweicloudsdksis.v1.ShowVocabulariesRequest`
        :rtype: :class:`huaweicloudsdksis.v1.ShowVocabulariesResponse`
        """
        return self._show_vocabularies_with_http_info(request)

    def _show_vocabularies_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/asr/vocabularies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVocabulariesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vocabulary(self, request):
        """查询热词表信息

        通过热词表id查询热词表的信息和内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVocabulary
        :type request: :class:`huaweicloudsdksis.v1.ShowVocabularyRequest`
        :rtype: :class:`huaweicloudsdksis.v1.ShowVocabularyResponse`
        """
        return self._show_vocabulary_with_http_info(request)

    def _show_vocabulary_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vocabulary_id' in local_var_params:
            path_params['vocabulary_id'] = local_var_params['vocabulary_id']

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
            resource_path='/v1/{project_id}/asr/vocabularies/{vocabulary_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVocabularyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vocabulary(self, request):
        """更新热词表

        更新一个热词表，更新成功返回id。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVocabulary
        :type request: :class:`huaweicloudsdksis.v1.UpdateVocabularyRequest`
        :rtype: :class:`huaweicloudsdksis.v1.UpdateVocabularyResponse`
        """
        return self._update_vocabulary_with_http_info(request)

    def _update_vocabulary_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'vocabulary_id' in local_var_params:
            path_params['vocabulary_id'] = local_var_params['vocabulary_id']

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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/asr/vocabularies/{vocabulary_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVocabularyResponse',
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

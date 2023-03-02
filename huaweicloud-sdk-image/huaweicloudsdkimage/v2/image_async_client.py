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


class ImageAsyncClient(Client):
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
        super(ImageAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkimage.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ImageClient":
            raise TypeError("client type error, support client type is ImageClient")

        return ClientBuilder(clazz)

    def create_image_highresolution_matting_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImageHighresolutionMattingTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateImageHighresolutionMattingTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateImageHighresolutionMattingTaskResponse`
        """
        return self.create_image_highresolution_matting_task_with_http_info(request)

    def create_image_highresolution_matting_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/image-highresolution-matting/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateImageHighresolutionMattingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_to_video_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImageToVideoTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateImageToVideoTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateImageToVideoTaskResponse`
        """
        return self.create_image_to_video_task_with_http_info(request)

    def create_image_to_video_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/image-to-video/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateImageToVideoTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_translate_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateImageTranslateTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateImageTranslateTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateImageTranslateTaskResponse`
        """
        return self.create_image_translate_task_with_http_info(request)

    def create_image_translate_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/image-wisedesign-translate/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateImageTranslateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_video_cover_analysis_task_async(self, request):
        """创建任务

        创建视频封面任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoCoverAnalysisTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateVideoCoverAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateVideoCoverAnalysisTaskResponse`
        """
        return self.create_video_cover_analysis_task_with_http_info(request)

    def create_video_cover_analysis_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-cover-analysis/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVideoCoverAnalysisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_video_cutting_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoCuttingTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateVideoCuttingTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateVideoCuttingTaskResponse`
        """
        return self.create_video_cutting_task_with_http_info(request)

    def create_video_cutting_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-cutting/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVideoCuttingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_video_shot_split_task_async(self, request):
        """创建任务

        创建视频拆条任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoShotSplitTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateVideoShotSplitTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateVideoShotSplitTaskResponse`
        """
        return self.create_video_shot_split_task_with_http_info(request)

    def create_video_shot_split_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/video-shot-split/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVideoShotSplitTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_video_summarization_analysis_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoSummarizationAnalysisTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateVideoSummarizationAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateVideoSummarizationAnalysisTaskResponse`
        """
        return self.create_video_summarization_analysis_task_with_http_info(request)

    def create_video_summarization_analysis_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/video-summarization-analysis/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVideoSummarizationAnalysisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_video_synthesis_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoSynthesisTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateVideoSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateVideoSynthesisTaskResponse`
        """
        return self.create_video_synthesis_task_with_http_info(request)

    def create_video_synthesis_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-synthesis/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVideoSynthesisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_video_translate_task_async(self, request):
        """创建任务

        Create Task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoTranslateTask
        :type request: :class:`huaweicloudsdkimage.v2.CreateVideoTranslateTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.CreateVideoTranslateTaskResponse`
        """
        return self.create_video_translate_task_with_http_info(request)

    def create_video_translate_task_with_http_info(self, request):
        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-translate/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVideoTranslateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_celebrity_recognition_async(self, request):
        """名人识别

        分析并识别图片中包含的政治人物、明星及网红人物，返回人物信息及人脸坐标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunCelebrityRecognition
        :type request: :class:`huaweicloudsdkimage.v2.RunCelebrityRecognitionRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunCelebrityRecognitionResponse`
        """
        return self.run_celebrity_recognition_with_http_info(request)

    def run_celebrity_recognition_with_http_info(self, request):
        all_params = ['run_celebrity_recognition_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/celebrity-recognition',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunCelebrityRecognitionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_description_async(self, request):
        """图像描述

        图像描述
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageDescription
        :type request: :class:`huaweicloudsdkimage.v2.RunImageDescriptionRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageDescriptionResponse`
        """
        return self.run_image_description_with_http_info(request)

    def run_image_description_with_http_info(self, request):
        all_params = ['run_image_description_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/description',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageDescriptionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_main_object_detection_async(self, request):
        """主体识别

        检测图像中的主要内容，返回主要内容的坐标信息，这里的主要内容包括两方面：bounding_box和main_object_box
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageMainObjectDetection
        :type request: :class:`huaweicloudsdkimage.v2.RunImageMainObjectDetectionRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageMainObjectDetectionResponse`
        """
        return self.run_image_main_object_detection_with_http_info(request)

    def run_image_main_object_detection_with_http_info(self, request):
        all_params = ['run_image_main_object_detection_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v3/{project_id}/image/main-object-detection',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageMainObjectDetectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_super_resolution_async(self, request):
        """图像超分

        图像数据，base64编码，输入图像范围200px ~ 1080px，支持JPG/PNG/BMP/JPEG/WEBP格式
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageSuperResolution
        :type request: :class:`huaweicloudsdkimage.v2.RunImageSuperResolutionRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageSuperResolutionResponse`
        """
        return self.run_image_super_resolution_with_http_info(request)

    def run_image_super_resolution_with_http_info(self, request):
        all_params = ['run_image_super_resolution_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/image-super-resolution',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageSuperResolutionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_tagging_async(self, request):
        """图像标签

        自然图像的语义内容非常丰富，一个图像包含多个标签内容，图像标签服务准确识别自然图片中数百种场景、上千种通用物体及其属性，让智能相册管理、照片检索和分类、基于场景内容或者物体的广告推荐等功能更加直观。使用时用户发送待处理图片，返回图片标签内容及相应置信度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageTagging
        :type request: :class:`huaweicloudsdkimage.v2.RunImageTaggingRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageTaggingResponse`
        """
        return self.run_image_tagging_with_http_info(request)

    def run_image_tagging_with_http_info(self, request):
        all_params = ['run_image_tagging_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/tagging',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageTaggingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_wisedesign_colorfilter_async(self, request):
        """智能设计图像滤镜

        智能设计图像滤镜服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageWisedesignColorfilter
        :type request: :class:`huaweicloudsdkimage.v2.RunImageWisedesignColorfilterRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageWisedesignColorfilterResponse`
        """
        return self.run_image_wisedesign_colorfilter_with_http_info(request)

    def run_image_wisedesign_colorfilter_with_http_info(self, request):
        all_params = ['run_image_wisedesign_colorfilter_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/image-wisedesign-colorfilter',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageWisedesignColorfilterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_wisedesign_combine_async(self, request):
        """智能设计图像合图

        智能设计图像合图服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageWisedesignCombine
        :type request: :class:`huaweicloudsdkimage.v2.RunImageWisedesignCombineRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageWisedesignCombineResponse`
        """
        return self.run_image_wisedesign_combine_with_http_info(request)

    def run_image_wisedesign_combine_with_http_info(self, request):
        all_params = ['run_image_wisedesign_combine_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/image-wisedesign-combine',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageWisedesignCombineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_wisedesign_crop_async(self, request):
        """智能设计图像裁剪

        智能设计图像裁剪服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageWisedesignCrop
        :type request: :class:`huaweicloudsdkimage.v2.RunImageWisedesignCropRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageWisedesignCropResponse`
        """
        return self.run_image_wisedesign_crop_with_http_info(request)

    def run_image_wisedesign_crop_with_http_info(self, request):
        all_params = ['run_image_wisedesign_crop_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/image-wisedesign-crop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageWisedesignCropResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_wisedesign_inpainting_async(self, request):
        """智能设计图像修复

        智能设计图像修复服务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageWisedesignInpainting
        :type request: :class:`huaweicloudsdkimage.v2.RunImageWisedesignInpaintingRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageWisedesignInpaintingResponse`
        """
        return self.run_image_wisedesign_inpainting_with_http_info(request)

    def run_image_wisedesign_inpainting_with_http_info(self, request):
        all_params = ['run_image_wisedesign_inpainting_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/image-wisedesign-inpainting',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageWisedesignInpaintingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_recapture_detect_async(self, request):
        """翻拍识别

        零售行业通常根据零售店的销售量进行销售奖励，拍摄售出商品的条形码上传后台是常用的统计方式。翻拍识别利用深度神经网络算法判断条形码图片为原始拍摄，还是经过二次翻拍、打印翻拍等手法二次处理的图片。利用翻拍识别，可以检测出经过二次处理的不合规范图片，使得统计数据更准确、有效。。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunRecaptureDetect
        :type request: :class:`huaweicloudsdkimage.v2.RunRecaptureDetectRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunRecaptureDetectResponse`
        """
        return self.run_recapture_detect_with_http_info(request)

    def run_recapture_detect_with_http_info(self, request):
        all_params = ['run_recapture_detect_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/recapture-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunRecaptureDetectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_highresolution_matting_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageHighresolutionMattingTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowImageHighresolutionMattingTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowImageHighresolutionMattingTaskResponse`
        """
        return self.show_image_highresolution_matting_task_with_http_info(request)

    def show_image_highresolution_matting_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/image-highresolution-matting/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowImageHighresolutionMattingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_to_video_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageToVideoTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowImageToVideoTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowImageToVideoTaskResponse`
        """
        return self.show_image_to_video_task_with_http_info(request)

    def show_image_to_video_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/image-to-video/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowImageToVideoTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_translate_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowImageTranslateTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowImageTranslateTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowImageTranslateTaskResponse`
        """
        return self.show_image_translate_task_with_http_info(request)

    def show_image_translate_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/image-wisedesign-translate/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowImageTranslateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_video_cover_analysis_task_async(self, request):
        """查询任务

        查询视频封面任务完成状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoCoverAnalysisTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowVideoCoverAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowVideoCoverAnalysisTaskResponse`
        """
        return self.show_video_cover_analysis_task_with_http_info(request)

    def show_video_cover_analysis_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-cover-analysis/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVideoCoverAnalysisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_video_cutting_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoCuttingTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowVideoCuttingTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowVideoCuttingTaskResponse`
        """
        return self.show_video_cutting_task_with_http_info(request)

    def show_video_cutting_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-cutting/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVideoCuttingTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_video_shot_split_task_async(self, request):
        """查询任务

        查询拆条任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoShotSplitTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowVideoShotSplitTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowVideoShotSplitTaskResponse`
        """
        return self.show_video_shot_split_task_with_http_info(request)

    def show_video_shot_split_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-shot-split/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVideoShotSplitTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_video_summarization_analysis_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoSummarizationAnalysisTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowVideoSummarizationAnalysisTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowVideoSummarizationAnalysisTaskResponse`
        """
        return self.show_video_summarization_analysis_task_with_http_info(request)

    def show_video_summarization_analysis_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-summarization-analysis/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVideoSummarizationAnalysisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_video_synthesis_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoSynthesisTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowVideoSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowVideoSynthesisTaskResponse`
        """
        return self.show_video_synthesis_task_with_http_info(request)

    def show_video_synthesis_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-synthesis/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVideoSynthesisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_video_translate_task_async(self, request):
        """查询任务

        show task
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoTranslateTask
        :type request: :class:`huaweicloudsdkimage.v2.ShowVideoTranslateTaskRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.ShowVideoTranslateTaskResponse`
        """
        return self.show_video_translate_task_with_http_info(request)

    def show_video_translate_task_with_http_info(self, request):
        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = ["X-request-id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/image/video-translate/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVideoTranslateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_delete_custom_tags_async(self, request):
        """删除媒资图像标签

        用于用户删除自定义的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDeleteCustomTags
        :type request: :class:`huaweicloudsdkimage.v2.RunDeleteCustomTagsRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunDeleteCustomTagsResponse`
        """
        return self.run_delete_custom_tags_with_http_info(request)

    def run_delete_custom_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v2/{project_id}/image/media-tagging/custom-tags',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunDeleteCustomTagsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_media_tagging_async(self, request):
        """标签识别

        自然图像的语义内容非常丰富，一个图像包含多个标签内容，图像标签服务准确识别自然图片中数百种场景、上千种通用物体及其属性，让智能相册管理、照片检索和分类、基于场景内容或者物体的广告推荐等功能更加直观。使用时用户发送待处理图片，返回图片标签内容及相应置信度。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageMediaTagging
        :type request: :class:`huaweicloudsdkimage.v2.RunImageMediaTaggingRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageMediaTaggingResponse`
        """
        return self.run_image_media_tagging_with_http_info(request)

    def run_image_media_tagging_with_http_info(self, request):
        all_params = ['run_image_media_tagging_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/media-tagging',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageMediaTaggingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_image_media_tagging_det_async(self, request):
        """媒资图像标签检测

        自然图像的语义内容非常丰富，一个图像包含多个标签内容，图像标签服务准确识别自然图片中数百种场景、上千种通用物体及其属性，让智能相册管理、照片检索和分类、基于场景内容或者物体的广告推荐等功能更加直观。使用时用户发送待处理图片，返回图片标签内容及相应的位置坐标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunImageMediaTaggingDet
        :type request: :class:`huaweicloudsdkimage.v2.RunImageMediaTaggingDetRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunImageMediaTaggingDetResponse`
        """
        return self.run_image_media_tagging_det_with_http_info(request)

    def run_image_media_tagging_det_with_http_info(self, request):
        all_params = ['run_image_media_tagging_det_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/image/media-tagging-det',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunImageMediaTaggingDetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_custom_tags_async(self, request):
        """查询媒资图像标签

        用于用户自查是否存在自定义的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunQueryCustomTags
        :type request: :class:`huaweicloudsdkimage.v2.RunQueryCustomTagsRequest`
        :rtype: :class:`huaweicloudsdkimage.v2.RunQueryCustomTagsResponse`
        """
        return self.run_query_custom_tags_with_http_info(request)

    def run_query_custom_tags_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v2/{project_id}/image/media-tagging/custom-tags/check',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunQueryCustomTagsResponse',
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

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


class MpcClient(Client):
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
        super(MpcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmpc.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def create_animated_graphics_task(self, request):
        """新建转动图任务

        创建动图任务，用于将完整的视频文件或视频文件中的一部分转换为动态图文件，暂只支持输出GIF文件。 待转动图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。 

        :param CreateAnimatedGraphicsTaskRequest request
        :return: CreateAnimatedGraphicsTaskResponse
        """
        return self.create_animated_graphics_task_with_http_info(request)

    def create_animated_graphics_task_with_http_info(self, request):
        """新建转动图任务

        创建动图任务，用于将完整的视频文件或视频文件中的一部分转换为动态图文件，暂只支持输出GIF文件。 待转动图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。 

        :param CreateAnimatedGraphicsTaskRequest request
        :return: CreateAnimatedGraphicsTaskResponse
        """

        all_params = ['create_animated_graphics_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAnimatedGraphicsTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_animated_graphics_task(self, request):
        """取消转动图任务

        取消已下发的生成动图任务，仅支持取消正在排队中的任务。 

        :param DeleteAnimatedGraphicsTaskRequest request
        :return: DeleteAnimatedGraphicsTaskResponse
        """
        return self.delete_animated_graphics_task_with_http_info(request)

    def delete_animated_graphics_task_with_http_info(self, request):
        """取消转动图任务

        取消已下发的生成动图任务，仅支持取消正在排队中的任务。 

        :param DeleteAnimatedGraphicsTaskRequest request
        :return: DeleteAnimatedGraphicsTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAnimatedGraphicsTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_animated_graphics_task(self, request):
        """查询转动图任务

        查询动图任务的状态。 

        :param ListAnimatedGraphicsTaskRequest request
        :return: ListAnimatedGraphicsTaskResponse
        """
        return self.list_animated_graphics_task_with_http_info(request)

    def list_animated_graphics_task_with_http_info(self, request):
        """查询转动图任务

        查询动图任务的状态。 

        :param ListAnimatedGraphicsTaskRequest request
        :return: ListAnimatedGraphicsTaskResponse
        """

        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/animated-graphics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAnimatedGraphicsTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_encrypt_task(self, request):
        """新建独立加密任务

        支持独立加密，包括创建、查询、删除独立加密任务。  约束：   - 只支持转码后的文件进行加密。   - 加密的文件必须是m3u8或者mpd结尾的文件。 

        :param CreateEncryptTaskRequest request
        :return: CreateEncryptTaskResponse
        """
        return self.create_encrypt_task_with_http_info(request)

    def create_encrypt_task_with_http_info(self, request):
        """新建独立加密任务

        支持独立加密，包括创建、查询、删除独立加密任务。  约束：   - 只支持转码后的文件进行加密。   - 加密的文件必须是m3u8或者mpd结尾的文件。 

        :param CreateEncryptTaskRequest request
        :return: CreateEncryptTaskResponse
        """

        all_params = ['create_encrypt_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateEncryptTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_encrypt_task(self, request):
        """取消独立加密任务

        取消独立加密任务。  约束：    只能取消正在任务队列中排队的任务。已开始加密或已完成的加密任务不能取消。 

        :param DeleteEncryptTaskRequest request
        :return: DeleteEncryptTaskResponse
        """
        return self.delete_encrypt_task_with_http_info(request)

    def delete_encrypt_task_with_http_info(self, request):
        """取消独立加密任务

        取消独立加密任务。  约束：    只能取消正在任务队列中排队的任务。已开始加密或已完成的加密任务不能取消。 

        :param DeleteEncryptTaskRequest request
        :return: DeleteEncryptTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEncryptTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_encrypt_task(self, request):
        """查询独立加密任务

        查询独立加密任务状态。返回任务执行结果或当前状态。 

        :param ListEncryptTaskRequest request
        :return: ListEncryptTaskResponse
        """
        return self.list_encrypt_task_with_http_info(request)

    def list_encrypt_task_with_http_info(self, request):
        """查询独立加密任务

        查询独立加密任务状态。返回任务执行结果或当前状态。 

        :param ListEncryptTaskRequest request
        :return: ListEncryptTaskResponse
        """

        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/encryptions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEncryptTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_extract_task(self, request):
        """新建视频解析任务

        创建视频解析任务，解析视频元数据。 

        :param CreateExtractTaskRequest request
        :return: CreateExtractTaskResponse
        """
        return self.create_extract_task_with_http_info(request)

    def create_extract_task_with_http_info(self, request):
        """新建视频解析任务

        创建视频解析任务，解析视频元数据。 

        :param CreateExtractTaskRequest request
        :return: CreateExtractTaskResponse
        """

        all_params = ['create_extract_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateExtractTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_extract_task(self, request):
        """取消视频解析任务

        取消已下发的视频解析任务，仅支持取消正在排队中的任务。 

        :param DeleteExtractTaskRequest request
        :return: DeleteExtractTaskResponse
        """
        return self.delete_extract_task_with_http_info(request)

    def delete_extract_task_with_http_info(self, request):
        """取消视频解析任务

        取消已下发的视频解析任务，仅支持取消正在排队中的任务。 

        :param DeleteExtractTaskRequest request
        :return: DeleteExtractTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteExtractTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_extract_task(self, request):
        """查询视频解析任务

        查询解析任务的状态和结果。 

        :param ListExtractTaskRequest request
        :return: ListExtractTaskResponse
        """
        return self.list_extract_task_with_http_info(request)

    def list_extract_task_with_http_info(self, request):
        """查询视频解析任务

        查询解析任务的状态和结果。 

        :param ListExtractTaskRequest request
        :return: ListExtractTaskResponse
        """

        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/extract-metadata',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListExtractTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job_status(self, request):
        """云服务操作异步查询接口

        云服务操作异步查询接口：云运营系统通过此接口，异步查询云服务的操作结果。 

        :param ShowJobStatusRequest request
        :return: ShowJobStatusResponse
        """
        return self.show_job_status_with_http_info(request)

    def show_job_status_with_http_info(self, request):
        """云服务操作异步查询接口

        云服务操作异步查询接口：云运营系统通过此接口，异步查询云服务的操作结果。 

        :param ShowJobStatusRequest request
        :return: ShowJobStatusResponse
        """

        all_params = ['tenant_id', 'job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenantId'] = local_var_params['tenant_id']
        if 'job_id' in local_var_params:
            path_params['jobId'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{tenantId}/jobs/{jobId}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobStatusResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_all_buckets(self, request):
        """查询桶列表

        查询桶列表（仅供Console调用）。 

        :param ListAllBucketsRequest request
        :return: ListAllBucketsResponse
        """
        return self.list_all_buckets_with_http_info(request)

    def list_all_buckets_with_http_info(self, request):
        """查询桶列表

        查询桶列表（仅供Console调用）。 

        :param ListAllBucketsRequest request
        :return: ListAllBucketsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAllBucketsResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_bucket_authorized(self, request):
        """桶授权或取消授权

        桶授权或取消授权（仅供Console调用）。 

        :param UpdateBucketAuthorizedRequest request
        :return: UpdateBucketAuthorizedResponse
        """
        return self.update_bucket_authorized_with_http_info(request)

    def update_bucket_authorized_with_http_info(self, request):
        """桶授权或取消授权

        桶授权或取消授权（仅供Console调用）。 

        :param UpdateBucketAuthorizedRequest request
        :return: UpdateBucketAuthorizedResponse
        """

        all_params = ['update_bucket_authorized_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/authority',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBucketAuthorizedResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_all_obs_obj_list(self, request):
        """查询桶里的object

        查询桶里的object（仅供Console调用）。 

        :param ListAllObsObjListRequest request
        :return: ListAllObsObjListResponse
        """
        return self.list_all_obs_obj_list_with_http_info(request)

    def list_all_obs_obj_list_with_http_info(self, request):
        """查询桶里的object

        查询桶里的object（仅供Console调用）。 

        :param ListAllObsObjListRequest request
        :return: ListAllObsObjListResponse
        """

        all_params = ['bucket', 'prefix', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))
        if 'prefix' in local_var_params:
            query_params.append(('prefix', local_var_params['prefix']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1.0-ext/{project_id}/objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAllObsObjListResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_quality_enhance_template(self, request):
        """创建视频增强模板

        创建视频增强模板

        :param CreateQualityEnhanceTemplateRequest request
        :return: CreateQualityEnhanceTemplateResponse
        """
        return self.create_quality_enhance_template_with_http_info(request)

    def create_quality_enhance_template_with_http_info(self, request):
        """创建视频增强模板

        创建视频增强模板

        :param CreateQualityEnhanceTemplateRequest request
        :return: CreateQualityEnhanceTemplateResponse
        """

        all_params = ['create_quality_enhance_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateQualityEnhanceTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_quality_enhance_template(self, request):
        """删除用户视频增强模板

        删除用户视频增强模板。

        :param DeleteQualityEnhanceTemplateRequest request
        :return: DeleteQualityEnhanceTemplateResponse
        """
        return self.delete_quality_enhance_template_with_http_info(request)

    def delete_quality_enhance_template_with_http_info(self, request):
        """删除用户视频增强模板

        删除用户视频增强模板。

        :param DeleteQualityEnhanceTemplateRequest request
        :return: DeleteQualityEnhanceTemplateResponse
        """

        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteQualityEnhanceTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_quality_enhance_default_template(self, request):
        """查询视频增强预置模板

        查询视频增强预置模板，返回所有结果。 

        :param ListQualityEnhanceDefaultTemplateRequest request
        :return: ListQualityEnhanceDefaultTemplateResponse
        """
        return self.list_quality_enhance_default_template_with_http_info(request)

    def list_quality_enhance_default_template_with_http_info(self, request):
        """查询视频增强预置模板

        查询视频增强预置模板，返回所有结果。 

        :param ListQualityEnhanceDefaultTemplateRequest request
        :return: ListQualityEnhanceDefaultTemplateResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance/default',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQualityEnhanceDefaultTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_quality_enhance_template(self, request):
        """查询用户视频增强模板

        查询用户自定义视频增强模板。 支持指定模板ID查询，或分页全量查询。模板ID，最多10个。 

        :param ListQualityEnhanceTemplateRequest request
        :return: ListQualityEnhanceTemplateResponse
        """
        return self.list_quality_enhance_template_with_http_info(request)

    def list_quality_enhance_template_with_http_info(self, request):
        """查询用户视频增强模板

        查询用户自定义视频增强模板。 支持指定模板ID查询，或分页全量查询。模板ID，最多10个。 

        :param ListQualityEnhanceTemplateRequest request
        :return: ListQualityEnhanceTemplateResponse
        """

        all_params = ['template_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQualityEnhanceTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_quality_enhance_template(self, request):
        """更新视频增强模板

        更新视频增强模板。

        :param UpdateQualityEnhanceTemplateRequest request
        :return: UpdateQualityEnhanceTemplateResponse
        """
        return self.update_quality_enhance_template_with_http_info(request)

    def update_quality_enhance_template_with_http_info(self, request):
        """更新视频增强模板

        更新视频增强模板。

        :param UpdateQualityEnhanceTemplateRequest request
        :return: UpdateQualityEnhanceTemplateResponse
        """

        all_params = ['update_quality_enhance_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/qualityenhance',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateQualityEnhanceTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_transcode_detail(self, request):
        """查询媒资转码详情

        查询媒资转码详情

        :param ListTranscodeDetailRequest request
        :return: ListTranscodeDetailResponse
        """
        return self.list_transcode_detail_with_http_info(request)

    def list_transcode_detail_with_http_info(self, request):
        """查询媒资转码详情

        查询媒资转码详情

        :param ListTranscodeDetailRequest request
        :return: ListTranscodeDetailResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTranscodeDetailResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def cancel_remux_task(self, request):
        """取消转封装任务

        取消已下发的转封装任务，仅支持取消正在排队中的任务。。 

        :param CancelRemuxTaskRequest request
        :return: CancelRemuxTaskResponse
        """
        return self.cancel_remux_task_with_http_info(request)

    def cancel_remux_task_with_http_info(self, request):
        """取消转封装任务

        取消已下发的转封装任务，仅支持取消正在排队中的任务。。 

        :param CancelRemuxTaskRequest request
        :return: CancelRemuxTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CancelRemuxTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_remux_task(self, request):
        """新建转封装任务

        创建转封装任务，转换音视频文件的格式，但不改变其分辨率和码率。 待转封装的媒资文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。 

        :param CreateRemuxTaskRequest request
        :return: CreateRemuxTaskResponse
        """
        return self.create_remux_task_with_http_info(request)

    def create_remux_task_with_http_info(self, request):
        """新建转封装任务

        创建转封装任务，转换音视频文件的格式，但不改变其分辨率和码率。 待转封装的媒资文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。 

        :param CreateRemuxTaskRequest request
        :return: CreateRemuxTaskResponse
        """

        all_params = ['create_remux_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRemuxTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_retry_remux_task(self, request):
        """重试转封装任务

        对失败的转封装任务进行重试。 

        :param CreateRetryRemuxTaskRequest request
        :return: CreateRetryRemuxTaskResponse
        """
        return self.create_retry_remux_task_with_http_info(request)

    def create_retry_remux_task_with_http_info(self, request):
        """重试转封装任务

        对失败的转封装任务进行重试。 

        :param CreateRetryRemuxTaskRequest request
        :return: CreateRetryRemuxTaskResponse
        """

        all_params = ['create_retry_remux_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRetryRemuxTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_remux_task(self, request):
        """删除转封装任务(仅供Console调用)

        删除转封装任务 

        :param DeleteRemuxTaskRequest request
        :return: DeleteRemuxTaskResponse
        """
        return self.delete_remux_task_with_http_info(request)

    def delete_remux_task_with_http_info(self, request):
        """删除转封装任务(仅供Console调用)

        删除转封装任务 

        :param DeleteRemuxTaskRequest request
        :return: DeleteRemuxTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRemuxTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_remux_task(self, request):
        """查询转封装任务

        查询转封装任务状态。 

        :param ListRemuxTaskRequest request
        :return: ListRemuxTaskResponse
        """
        return self.list_remux_task_with_http_info(request)

    def list_remux_task_with_http_info(self, request):
        """查询转封装任务

        查询转封装任务状态。 

        :param ListRemuxTaskRequest request
        :return: ListRemuxTaskResponse
        """

        all_params = ['task_id', 'status', 'start_time', 'end_time', 'input_bucket', 'input_object', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'input_bucket' in local_var_params:
            query_params.append(('input_bucket', local_var_params['input_bucket']))
        if 'input_object' in local_var_params:
            query_params.append(('input_object', local_var_params['input_object']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/remux',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRemuxTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_notify_event(self, request):
        """查询转码服务端所有事件

        ## 典型场景 ##   转码Console查询转码服务端所有事件，并将查询到的事件展示在页面供用户配置  ## 接口功能 ##   查询转码服务端所有事件 。  ## 接口约束 ##   无。 

        :param ListNotifyEventRequest request
        :return: ListNotifyEventResponse
        """
        return self.list_notify_event_with_http_info(request)

    def list_notify_event_with_http_info(self, request):
        """查询转码服务端所有事件

        ## 典型场景 ##   转码Console查询转码服务端所有事件，并将查询到的事件展示在页面供用户配置  ## 接口功能 ##   查询转码服务端所有事件 。  ## 接口约束 ##   无。 

        :param ListNotifyEventRequest request
        :return: ListNotifyEventResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/notification/event',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNotifyEventResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_notify_smn_topic_config(self, request):
        """查询转码服务端事件通知

        ## 典型场景 ##   查询转码服务端事件通知。  ## 接口功能 ##   查询转码服务端事件通知。  ## 接口约束 ##   无。 

        :param ListNotifySmnTopicConfigRequest request
        :return: ListNotifySmnTopicConfigResponse
        """
        return self.list_notify_smn_topic_config_with_http_info(request)

    def list_notify_smn_topic_config_with_http_info(self, request):
        """查询转码服务端事件通知

        ## 典型场景 ##   查询转码服务端事件通知。  ## 接口功能 ##   查询转码服务端事件通知。  ## 接口约束 ##   无。 

        :param ListNotifySmnTopicConfigRequest request
        :return: ListNotifySmnTopicConfigResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/notification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNotifySmnTopicConfigResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_notify_template(self, request):
        """查询规定的消息通知模板内容

        查询规定的消息通知模板内容。

        :param ListNotifyTemplateRequest request
        :return: ListNotifyTemplateResponse
        """
        return self.list_notify_template_with_http_info(request)

    def list_notify_template_with_http_info(self, request):
        """查询规定的消息通知模板内容

        查询规定的消息通知模板内容。

        :param ListNotifyTemplateRequest request
        :return: ListNotifyTemplateResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/notification/template',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListNotifyTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def notify_smn_topic_config(self, request):
        """配置转码服务端事件通知

        配置转码服务端事件通知。

        :param NotifySmnTopicConfigRequest request
        :return: NotifySmnTopicConfigResponse
        """
        return self.notify_smn_topic_config_with_http_info(request)

    def notify_smn_topic_config_with_http_info(self, request):
        """配置转码服务端事件通知

        配置转码服务端事件通知。

        :param NotifySmnTopicConfigRequest request
        :return: NotifySmnTopicConfigResponse
        """

        all_params = ['notify_smn_topic_config_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/notification',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='NotifySmnTopicConfigResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_stat_summary(self, request):
        """查询点播概览信息

        查询点播概览信息（仅供Console调用）。 

        :param ListStatSummaryRequest request
        :return: ListStatSummaryResponse
        """
        return self.list_stat_summary_with_http_info(request)

    def list_stat_summary_with_http_info(self, request):
        """查询点播概览信息

        查询点播概览信息（仅供Console调用）。 

        :param ListStatSummaryRequest request
        :return: ListStatSummaryResponse
        """

        all_params = ['start_time', 'end_time', 'stat_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'stat_type' in local_var_params:
            query_params.append(('stat_type', local_var_params['stat_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings/summaries',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListStatSummaryResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_summary(self, request):
        """查询转码概览信息

        查询转码概览信息，（仅供Console调用）。 转码Console有个概览页面，用于展示登录租户最近一个月或最近一周转码时长（分钟）、转码任务数量。仅展示转码成功的，按结束时间算。 

        :param ListSummaryRequest request
        :return: ListSummaryResponse
        """
        return self.list_summary_with_http_info(request)

    def list_summary_with_http_info(self, request):
        """查询转码概览信息

        查询转码概览信息，（仅供Console调用）。 转码Console有个概览页面，用于展示登录租户最近一个月或最近一周转码时长（分钟）、转码任务数量。仅展示转码成功的，按结束时间算。 

        :param ListSummaryRequest request
        :return: ListSummaryResponse
        """

        all_params = ['range']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'range' in local_var_params:
            query_params.append(('range', local_var_params['range']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings/summary',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSummaryResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_template_group(self, request):
        """新建转码模板组

        新建转码模板组，最多支持一进六出。 

        :param CreateTemplateGroupRequest request
        :return: CreateTemplateGroupResponse
        """
        return self.create_template_group_with_http_info(request)

    def create_template_group_with_http_info(self, request):
        """新建转码模板组

        新建转码模板组，最多支持一进六出。 

        :param CreateTemplateGroupRequest request
        :return: CreateTemplateGroupResponse
        """

        all_params = ['create_template_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTemplateGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_template_group(self, request):
        """删除转码模板组

        删除转码模板组。 

        :param DeleteTemplateGroupRequest request
        :return: DeleteTemplateGroupResponse
        """
        return self.delete_template_group_with_http_info(request)

    def delete_template_group_with_http_info(self, request):
        """删除转码模板组

        删除转码模板组。 

        :param DeleteTemplateGroupRequest request
        :return: DeleteTemplateGroupResponse
        """

        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_template_group(self, request):
        """查询转码模板组

        查询转码模板组列表。 

        :param ListTemplateGroupRequest request
        :return: ListTemplateGroupResponse
        """
        return self.list_template_group_with_http_info(request)

    def list_template_group_with_http_info(self, request):
        """查询转码模板组

        查询转码模板组列表。 

        :param ListTemplateGroupRequest request
        :return: ListTemplateGroupResponse
        """

        all_params = ['group_id', 'group_name', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
            collection_formats['group_id'] = 'multi'
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))
            collection_formats['group_name'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_template_group(self, request):
        """更新转码模板组

        修改模板组接口。 

        :param UpdateTemplateGroupRequest request
        :return: UpdateTemplateGroupResponse
        """
        return self.update_template_group_with_http_info(request)

    def update_template_group_with_http_info(self, request):
        """更新转码模板组

        修改模板组接口。 

        :param UpdateTemplateGroupRequest request
        :return: UpdateTemplateGroupResponse
        """

        all_params = ['update_template_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template_group/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTemplateGroupResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_tenant_status(self, request):
        """更新租户状态

        ## 典型场景 ##   更新租户状态。  ## 接口功能 ##   更新租户状态。  ## 接口约束 ##   无。 

        :param UpdateTenantStatusRequest request
        :return: UpdateTenantStatusResponse
        """
        return self.update_tenant_status_with_http_info(request)

    def update_tenant_status_with_http_info(self, request):
        """更新租户状态

        ## 典型场景 ##   更新租户状态。  ## 接口功能 ##   更新租户状态。  ## 接口约束 ##   无。 

        :param UpdateTenantStatusRequest request
        :return: UpdateTenantStatusResponse
        """

        all_params = ['update_tenant_status_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/services/status',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTenantStatusResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_tenant_info(self, request):
        """查询租户状态信息

        ## 典型场景 ##   查询租户信息，查询租户的欠费、冻结状态、是否实名认证、是否开通服务  ## 接口功能 ##   查询租户信息，查询租户的欠费、冻结状态、是否实名认证、是否开通服务  ## 接口约束 ##   无 

        :param ShowTenantInfoRequest request
        :return: ShowTenantInfoResponse
        """
        return self.show_tenant_info_with_http_info(request)

    def show_tenant_info_with_http_info(self, request):
        """查询租户状态信息

        ## 典型场景 ##   查询租户信息，查询租户的欠费、冻结状态、是否实名认证、是否开通服务  ## 接口功能 ##   查询租户信息，查询租户的欠费、冻结状态、是否实名认证、是否开通服务  ## 接口约束 ##   无 

        :param ShowTenantInfoRequest request
        :return: ShowTenantInfoResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/tenant_info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTenantInfoResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_tenant_info(self, request):
        """修改租户信息，如开通点播服务

        ## 典型场景 ##   修改租户信息，如开通点播服务  ## 接口功能 ##   修改租户信息，如开通点播服务  ## 接口约束 ##   无 

        :param UpdateTenantInfoRequest request
        :return: UpdateTenantInfoResponse
        """
        return self.update_tenant_info_with_http_info(request)

    def update_tenant_info_with_http_info(self, request):
        """修改租户信息，如开通点播服务

        ## 典型场景 ##   修改租户信息，如开通点播服务  ## 接口功能 ##   修改租户信息，如开通点播服务  ## 接口约束 ##   无 

        :param UpdateTenantInfoRequest request
        :return: UpdateTenantInfoResponse
        """

        all_params = ['update_tenant_info_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/tenant_info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTenantInfoResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_thumbnails_task(self, request):
        """新建截图任务

        新建截图任务，视频截图将从首帧开始，按设置的时间间隔截图，最后截取末帧。 待截图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。  约束：   暂只支持生成JPG格式的图片文件。 

        :param CreateThumbnailsTaskRequest request
        :return: CreateThumbnailsTaskResponse
        """
        return self.create_thumbnails_task_with_http_info(request)

    def create_thumbnails_task_with_http_info(self, request):
        """新建截图任务

        新建截图任务，视频截图将从首帧开始，按设置的时间间隔截图，最后截取末帧。 待截图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。  约束：   暂只支持生成JPG格式的图片文件。 

        :param CreateThumbnailsTaskRequest request
        :return: CreateThumbnailsTaskResponse
        """

        all_params = ['create_thumbnails_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateThumbnailsTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_thumbnails_task(self, request):
        """取消截图任务

        取消已下发截图任务。 只能取消已接受尚在队列中等待处理的任务，已完成或正在执行阶段的任务不能取消。 

        :param DeleteThumbnailsTaskRequest request
        :return: DeleteThumbnailsTaskResponse
        """
        return self.delete_thumbnails_task_with_http_info(request)

    def delete_thumbnails_task_with_http_info(self, request):
        """取消截图任务

        取消已下发截图任务。 只能取消已接受尚在队列中等待处理的任务，已完成或正在执行阶段的任务不能取消。 

        :param DeleteThumbnailsTaskRequest request
        :return: DeleteThumbnailsTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteThumbnailsTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_thumbnails_task(self, request):
        """查询截图任务

        查询截图任务状态。返回任务执行结果，包括状态、输入、输出等信息。 

        :param ListThumbnailsTaskRequest request
        :return: ListThumbnailsTaskResponse
        """
        return self.list_thumbnails_task_with_http_info(request)

    def list_thumbnails_task_with_http_info(self, request):
        """查询截图任务

        查询截图任务状态。返回任务执行结果，包括状态、输入、输出等信息。 

        :param ListThumbnailsTaskRequest request
        :return: ListThumbnailsTaskResponse
        """

        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/thumbnails',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListThumbnailsTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_transcoding_task(self, request):
        """新建转码任务

        新建转码任务可以将视频进行转码，并在转码过程中压制水印、内容质检、视频截图等。视频转码前需要配置转码模板。 待转码的音视频需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。 

        :param CreateTranscodingTaskRequest request
        :return: CreateTranscodingTaskResponse
        """
        return self.create_transcoding_task_with_http_info(request)

    def create_transcoding_task_with_http_info(self, request):
        """新建转码任务

        新建转码任务可以将视频进行转码，并在转码过程中压制水印、内容质检、视频截图等。视频转码前需要配置转码模板。 待转码的音视频需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。 

        :param CreateTranscodingTaskRequest request
        :return: CreateTranscodingTaskResponse
        """

        all_params = ['create_transcoding_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTranscodingTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_transcoding_task(self, request):
        """取消转码任务

        取消已下发转码任务。 只能取消正在转码任务队列中排队的转码任务。已开始转码或已完成的转码任务不能取消。 

        :param DeleteTranscodingTaskRequest request
        :return: DeleteTranscodingTaskResponse
        """
        return self.delete_transcoding_task_with_http_info(request)

    def delete_transcoding_task_with_http_info(self, request):
        """取消转码任务

        取消已下发转码任务。 只能取消正在转码任务队列中排队的转码任务。已开始转码或已完成的转码任务不能取消。 

        :param DeleteTranscodingTaskRequest request
        :return: DeleteTranscodingTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTranscodingTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_transcoding_task_by_console(self, request):
        """删除转码任务(仅供Console调用)

        删除转码任务(仅供Console调用)。 

        :param DeleteTranscodingTaskByConsoleRequest request
        :return: DeleteTranscodingTaskByConsoleResponse
        """
        return self.delete_transcoding_task_by_console_with_http_info(request)

    def delete_transcoding_task_by_console_with_http_info(self, request):
        """删除转码任务(仅供Console调用)

        删除转码任务(仅供Console调用)。 

        :param DeleteTranscodingTaskByConsoleRequest request
        :return: DeleteTranscodingTaskByConsoleResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTranscodingTaskByConsoleResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_transcoding_task(self, request):
        """查询转码任务

        查询转码任务状态。 

        :param ListTranscodingTaskRequest request
        :return: ListTranscodingTaskResponse
        """
        return self.list_transcoding_task_with_http_info(request)

    def list_transcoding_task_with_http_info(self, request):
        """查询转码任务

        查询转码任务状态。 

        :param ListTranscodingTaskRequest request
        :return: ListTranscodingTaskResponse
        """

        all_params = ['task_id', 'status', 'start_time', 'end_time', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTranscodingTaskResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_trans_template(self, request):
        """新建转码模板

        新建转码模板，采用自定义的模板转码。 

        :param CreateTransTemplateRequest request
        :return: CreateTransTemplateResponse
        """
        return self.create_trans_template_with_http_info(request)

    def create_trans_template_with_http_info(self, request):
        """新建转码模板

        新建转码模板，采用自定义的模板转码。 

        :param CreateTransTemplateRequest request
        :return: CreateTransTemplateResponse
        """

        all_params = ['create_trans_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTransTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_template(self, request):
        """删除转码模板

        删除转码模板。

        :param DeleteTemplateRequest request
        :return: DeleteTemplateResponse
        """
        return self.delete_template_with_http_info(request)

    def delete_template_with_http_info(self, request):
        """删除转码模板

        删除转码模板。

        :param DeleteTemplateRequest request
        :return: DeleteTemplateResponse
        """

        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_template(self, request):
        """查询转码模板

        查询用户自定义转码配置模板。 支持指定模板ID查询，或分页全量查询。转码配置模板ID，最多10个。 

        :param ListTemplateRequest request
        :return: ListTemplateResponse
        """
        return self.list_template_with_http_info(request)

    def list_template_with_http_info(self, request):
        """查询转码模板

        查询用户自定义转码配置模板。 支持指定模板ID查询，或分页全量查询。转码配置模板ID，最多10个。 

        :param ListTemplateRequest request
        :return: ListTemplateResponse
        """

        all_params = ['template_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_trans_template(self, request):
        """更新转码模板

        更新转码模板。

        :param UpdateTransTemplateRequest request
        :return: UpdateTransTemplateResponse
        """
        return self.update_trans_template_with_http_info(request)

    def update_trans_template_with_http_info(self, request):
        """更新转码模板

        更新转码模板。

        :param UpdateTransTemplateRequest request
        :return: UpdateTransTemplateResponse
        """

        all_params = ['update_trans_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/transcodings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateTransTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_watermark_template(self, request):
        """新建水印模板

        自定义水印模板。 

        :param CreateWatermarkTemplateRequest request
        :return: CreateWatermarkTemplateResponse
        """
        return self.create_watermark_template_with_http_info(request)

    def create_watermark_template_with_http_info(self, request):
        """新建水印模板

        自定义水印模板。 

        :param CreateWatermarkTemplateRequest request
        :return: CreateWatermarkTemplateResponse
        """

        all_params = ['create_watermark_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateWatermarkTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_watermark_template(self, request):
        """删除水印模板

        删除自定义水印模板。 

        :param DeleteWatermarkTemplateRequest request
        :return: DeleteWatermarkTemplateResponse
        """
        return self.delete_watermark_template_with_http_info(request)

    def delete_watermark_template_with_http_info(self, request):
        """删除水印模板

        删除自定义水印模板。 

        :param DeleteWatermarkTemplateRequest request
        :return: DeleteWatermarkTemplateResponse
        """

        all_params = ['template_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteWatermarkTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_watermark_template(self, request):
        """查询水印模板

        查询自定义水印模板。支持指定模板ID查询，或分页全量查询。 

        :param ListWatermarkTemplateRequest request
        :return: ListWatermarkTemplateResponse
        """
        return self.list_watermark_template_with_http_info(request)

    def list_watermark_template_with_http_info(self, request):
        """查询水印模板

        查询自定义水印模板。支持指定模板ID查询，或分页全量查询。 

        :param ListWatermarkTemplateRequest request
        :return: ListWatermarkTemplateResponse
        """

        all_params = ['template_id', 'page', 'size']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))
            collection_formats['template_id'] = 'multi'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()


        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListWatermarkTemplateResponse',
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_watermark_template(self, request):
        """更新水印模板

        更新自定义水印模板。 

        :param UpdateWatermarkTemplateRequest request
        :return: UpdateWatermarkTemplateResponse
        """
        return self.update_watermark_template_with_http_info(request)

    def update_watermark_template_with_http_info(self, request):
        """更新水印模板

        更新自定义水印模板。 

        :param UpdateWatermarkTemplateRequest request
        :return: UpdateWatermarkTemplateResponse
        """

        all_params = ['update_watermark_template_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/template/watermark',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateWatermarkTemplateResponse',
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
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            collection_formats=collection_formats,
            request_type=request_type)

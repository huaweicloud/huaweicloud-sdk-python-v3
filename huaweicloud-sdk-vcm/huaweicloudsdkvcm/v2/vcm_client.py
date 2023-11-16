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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkvcm'")


class VcmClient(Client):
    def __init__(self):
        super(VcmClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvcm.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VcmClient":
                raise TypeError("client type error, support client type is VcmClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def check_audio_job(self, request):
        """查询单个作业

        该 API 用于查询并显示单个作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckAudioJob
        :type request: :class:`huaweicloudsdkvcm.v2.CheckAudioJobRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.CheckAudioJobResponse`
        """
        http_info = self._check_audio_job_http_info(request)
        return self._call_api(**http_info)

    def check_audio_job_invoker(self, request):
        http_info = self._check_audio_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_audio_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/audio-moderation/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckAudioJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def check_video_job(self, request):
        """查询单个作业

        该API用于查询并显示单个作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckVideoJob
        :type request: :class:`huaweicloudsdkvcm.v2.CheckVideoJobRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.CheckVideoJobResponse`
        """
        http_info = self._check_video_job_http_info(request)
        return self._call_api(**http_info)

    def check_video_job_invoker(self, request):
        http_info = self._check_video_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_video_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/video-moderation/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CheckVideoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def create_audio_job(self, request):
        """创建作业

        该接口用于创建语音内容审核的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAudioJob
        :type request: :class:`huaweicloudsdkvcm.v2.CreateAudioJobRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.CreateAudioJobResponse`
        """
        http_info = self._create_audio_job_http_info(request)
        return self._call_api(**http_info)

    def create_audio_job_invoker(self, request):
        http_info = self._create_audio_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_audio_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/audio-moderation/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAudioJobResponse"
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

    def create_video_job(self, request):
        """创建作业

        该接口用于创建视频内容审核的作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVideoJob
        :type request: :class:`huaweicloudsdkvcm.v2.CreateVideoJobRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.CreateVideoJobResponse`
        """
        http_info = self._create_video_job_http_info(request)
        return self._call_api(**http_info)

    def create_video_job_invoker(self, request):
        http_info = self._create_video_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_video_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/services/video-moderation/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVideoJobResponse"
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

    def delete_demo_info(self, request):
        """删除语音作业

        删除语音作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDemoInfo
        :type request: :class:`huaweicloudsdkvcm.v2.DeleteDemoInfoRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.DeleteDemoInfoResponse`
        """
        http_info = self._delete_demo_info_http_info(request)
        return self._call_api(**http_info)

    def delete_demo_info_invoker(self, request):
        http_info = self._delete_demo_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_demo_info_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/audio-moderation/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDemoInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def delete_video_job(self, request):
        """删除作业

        该API用于删除指定作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVideoJob
        :type request: :class:`huaweicloudsdkvcm.v2.DeleteVideoJobRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.DeleteVideoJobResponse`
        """
        http_info = self._delete_video_job_http_info(request)
        return self._call_api(**http_info)

    def delete_video_job_invoker(self, request):
        http_info = self._delete_video_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_video_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/services/video-moderation/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVideoJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def list_audio_jobs(self, request):
        """查询作业列表

        查询作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAudioJobs
        :type request: :class:`huaweicloudsdkvcm.v2.ListAudioJobsRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.ListAudioJobsResponse`
        """
        http_info = self._list_audio_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_audio_jobs_invoker(self, request):
        http_info = self._list_audio_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_audio_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/audio-moderation/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListAudioJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def list_video_jobs(self, request):
        """查询作业列表

        该API用于查询并显示视频内容审核的作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVideoJobs
        :type request: :class:`huaweicloudsdkvcm.v2.ListVideoJobsRequest`
        :rtype: :class:`huaweicloudsdkvcm.v2.ListVideoJobsResponse`
        """
        http_info = self._list_video_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_video_jobs_invoker(self, request):
        http_info = self._list_video_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_video_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/services/video-moderation/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListVideoJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

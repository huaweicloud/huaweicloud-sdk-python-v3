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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmpc'")


class MpcClient(Client):
    def __init__(self):
        super(MpcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmpc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MpcClient":
                raise TypeError("client type error, support client type is MpcClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_animated_graphics_task(self, request):
        """新建转动图任务

        创建动图任务，用于将完整的视频文件或视频文件中的一部分转换为动态图文件，暂只支持输出GIF文件。
        待转动图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAnimatedGraphicsTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateAnimatedGraphicsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateAnimatedGraphicsTaskResponse`
        """
        http_info = self._create_animated_graphics_task_http_info(request)
        return self._call_api(**http_info)

    def create_animated_graphics_task_invoker(self, request):
        http_info = self._create_animated_graphics_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_animated_graphics_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/animated-graphics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAnimatedGraphicsTaskResponse"
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

    def delete_animated_graphics_task(self, request):
        """取消转动图任务

        取消已下发的生成动图任务，仅支持取消正在排队中的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAnimatedGraphicsTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteAnimatedGraphicsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteAnimatedGraphicsTaskResponse`
        """
        http_info = self._delete_animated_graphics_task_http_info(request)
        return self._call_api(**http_info)

    def delete_animated_graphics_task_invoker(self, request):
        http_info = self._delete_animated_graphics_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_animated_graphics_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/animated-graphics",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAnimatedGraphicsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_animated_graphics_task(self, request):
        """查询转动图任务

        查询动图任务的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAnimatedGraphicsTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListAnimatedGraphicsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListAnimatedGraphicsTaskResponse`
        """
        http_info = self._list_animated_graphics_task_http_info(request)
        return self._call_api(**http_info)

    def list_animated_graphics_task_invoker(self, request):
        http_info = self._list_animated_graphics_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_animated_graphics_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/animated-graphics",
            "request_type": request.__class__.__name__,
            "response_type": "ListAnimatedGraphicsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_agencies_task(self, request):
        """请求委托任务

        开启或关闭\&quot;委托授权\&quot;, 开启后，媒体处理服务将拥有您所有桶的读写权限，子账号不支持委托授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAgenciesTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateAgenciesTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateAgenciesTaskResponse`
        """
        http_info = self._create_agencies_task_http_info(request)
        return self._call_api(**http_info)

    def create_agencies_task_invoker(self, request):
        http_info = self._create_agencies_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_agencies_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgenciesTaskResponse"
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

    def list_all_buckets(self, request):
        """查询桶列表

        请求查询自己创建的指定的桶区域位置的桶列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllBuckets
        :type request: :class:`huaweicloudsdkmpc.v1.ListAllBucketsRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListAllBucketsResponse`
        """
        http_info = self._list_all_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_all_buckets_invoker(self, request):
        http_info = self._list_all_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_buckets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllBucketsResponse"
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

    def list_all_obs_obj_list(self, request):
        """查询桶里的object

        查询桶里的object。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllObsObjList
        :type request: :class:`huaweicloudsdkmpc.v1.ListAllObsObjListRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListAllObsObjListResponse`
        """
        http_info = self._list_all_obs_obj_list_http_info(request)
        return self._call_api(**http_info)

    def list_all_obs_obj_list_invoker(self, request):
        http_info = self._list_all_obs_obj_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_obs_obj_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0-ext/{project_id}/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllObsObjListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_notify_event(self, request):
        """查询转码服务端所有事件

        查询消息订阅功能板块, SMN主题的所有订阅事件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotifyEvent
        :type request: :class:`huaweicloudsdkmpc.v1.ListNotifyEventRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListNotifyEventResponse`
        """
        http_info = self._list_notify_event_http_info(request)
        return self._call_api(**http_info)

    def list_notify_event_invoker(self, request):
        http_info = self._list_notify_event_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notify_event_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notification/event",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotifyEventResponse"
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

    def list_notify_smn_topic_config(self, request):
        """查询转码服务端事件通知

        查询消息订阅功能板块, SMN主题的订阅事件的启用状态和订阅消息的启用状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotifySmnTopicConfig
        :type request: :class:`huaweicloudsdkmpc.v1.ListNotifySmnTopicConfigRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListNotifySmnTopicConfigResponse`
        """
        http_info = self._list_notify_smn_topic_config_http_info(request)
        return self._call_api(**http_info)

    def list_notify_smn_topic_config_invoker(self, request):
        http_info = self._list_notify_smn_topic_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_notify_smn_topic_config_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/notification",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotifySmnTopicConfigResponse"
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

    def notify_smn_topic_config(self, request):
        """配置转码服务端事件通知

        配置转码服务端事件通知。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for NotifySmnTopicConfig
        :type request: :class:`huaweicloudsdkmpc.v1.NotifySmnTopicConfigRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.NotifySmnTopicConfigResponse`
        """
        http_info = self._notify_smn_topic_config_http_info(request)
        return self._call_api(**http_info)

    def notify_smn_topic_config_invoker(self, request):
        http_info = self._notify_smn_topic_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _notify_smn_topic_config_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/notification",
            "request_type": request.__class__.__name__,
            "response_type": "NotifySmnTopicConfigResponse"
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

    def show_agencies_task(self, request):
        """查询创建委托任务状态

        查询创建委托任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgenciesTask
        :type request: :class:`huaweicloudsdkmpc.v1.ShowAgenciesTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ShowAgenciesTaskResponse`
        """
        http_info = self._show_agencies_task_http_info(request)
        return self._call_api(**http_info)

    def show_agencies_task_invoker(self, request):
        http_info = self._show_agencies_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_agencies_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgenciesTaskResponse"
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

    def update_bucket_authorized(self, request):
        """桶授权或取消授权

        对OBS桶进行授权或取消授权，媒体处理服务仅拥有已授权桶的读写权限。（暂不支持KMS加密桶的授权）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBucketAuthorized
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateBucketAuthorizedRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateBucketAuthorizedResponse`
        """
        http_info = self._update_bucket_authorized_http_info(request)
        return self._call_api(**http_info)

    def update_bucket_authorized_invoker(self, request):
        http_info = self._update_bucket_authorized_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_bucket_authorized_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/authority",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBucketAuthorizedResponse"
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

    def create_editing_job(self, request):
        """新建剪辑任务

        创建剪辑任务，用于将多个视频文件进行裁剪成多个视频分段，并且可以把这些视频分段合并成一个视频，剪切和拼接功能可以单独使用。
        待剪辑的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEditingJob
        :type request: :class:`huaweicloudsdkmpc.v1.CreateEditingJobRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateEditingJobResponse`
        """
        http_info = self._create_editing_job_http_info(request)
        return self._call_api(**http_info)

    def create_editing_job_invoker(self, request):
        http_info = self._create_editing_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_editing_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/editing/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEditingJobResponse"
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

    def delete_editing_job(self, request):
        """取消剪辑任务

        取消已下发的生成剪辑任务，仅支持取消正在排队中的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEditingJob
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteEditingJobRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteEditingJobResponse`
        """
        http_info = self._delete_editing_job_http_info(request)
        return self._call_api(**http_info)

    def delete_editing_job_invoker(self, request):
        http_info = self._delete_editing_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_editing_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/editing/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEditingJobResponse"
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

    def list_editing_job(self, request):
        """查询剪辑任务

        查询剪辑任务的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEditingJob
        :type request: :class:`huaweicloudsdkmpc.v1.ListEditingJobRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListEditingJobResponse`
        """
        http_info = self._list_editing_job_http_info(request)
        return self._call_api(**http_info)

    def list_editing_job_invoker(self, request):
        http_info = self._list_editing_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_editing_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/editing/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEditingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
            collection_formats['job_id'] = 'multi'
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
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_encrypt_task(self, request):
        """新建独立加密任务

        支持独立加密，包括创建、查询、删除独立加密任务。该API已废弃。
        
        约束：
          - 只支持转码后的文件进行加密。
          - 加密的文件必须是m3u8或者mpd结尾的文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEncryptTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateEncryptTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateEncryptTaskResponse`
        """
        http_info = self._create_encrypt_task_http_info(request)
        return self._call_api(**http_info)

    def create_encrypt_task_invoker(self, request):
        http_info = self._create_encrypt_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_encrypt_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/encryptions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEncryptTaskResponse"
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

    def delete_encrypt_task(self, request):
        """取消独立加密任务

        取消独立加密任务。该API已废弃。
        
        约束：
        
          只能取消正在任务队列中排队的任务。已开始加密或已完成的加密任务不能取消。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEncryptTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteEncryptTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteEncryptTaskResponse`
        """
        http_info = self._delete_encrypt_task_http_info(request)
        return self._call_api(**http_info)

    def delete_encrypt_task_invoker(self, request):
        http_info = self._delete_encrypt_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_encrypt_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/encryptions",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEncryptTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_encrypt_task(self, request):
        """查询独立加密任务

        查询独立加密任务状态。返回任务执行结果或当前状态。该API已废弃。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEncryptTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListEncryptTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListEncryptTaskResponse`
        """
        http_info = self._list_encrypt_task_http_info(request)
        return self._call_api(**http_info)

    def list_encrypt_task_invoker(self, request):
        http_info = self._list_encrypt_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_encrypt_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/encryptions",
            "request_type": request.__class__.__name__,
            "response_type": "ListEncryptTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def create_extract_task(self, request):
        """新建视频解析任务

        创建视频解析任务，解析视频元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExtractTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateExtractTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateExtractTaskResponse`
        """
        http_info = self._create_extract_task_http_info(request)
        return self._call_api(**http_info)

    def create_extract_task_invoker(self, request):
        http_info = self._create_extract_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_extract_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/extract-metadata",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExtractTaskResponse"
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

    def delete_extract_task(self, request):
        """取消视频解析任务

        取消已下发的视频解析任务，仅支持取消正在排队中的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteExtractTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteExtractTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteExtractTaskResponse`
        """
        http_info = self._delete_extract_task_http_info(request)
        return self._call_api(**http_info)

    def delete_extract_task_invoker(self, request):
        http_info = self._delete_extract_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_extract_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/extract-metadata",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteExtractTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_extract_task(self, request):
        """查询视频解析任务

        查询解析任务的状态和结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListExtractTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListExtractTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListExtractTaskResponse`
        """
        http_info = self._list_extract_task_http_info(request)
        return self._call_api(**http_info)

    def list_extract_task_invoker(self, request):
        http_info = self._list_extract_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_extract_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/extract-metadata",
            "request_type": request.__class__.__name__,
            "response_type": "ListExtractTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_mb_tasks_report(self, request):
        """合并多声道任务、重置声轨任务上报接口

        ## 典型场景 ##
          合并音频多声道文件任务、重置音频文件声轨任务上报结果接口。
        ## 接口功能 ##
          合并音频多声道文件任务、重置音频文件声轨任务上报结果接口。
        ## 接口约束 ##
          无。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMbTasksReport
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMbTasksReportRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMbTasksReportResponse`
        """
        http_info = self._create_mb_tasks_report_http_info(request)
        return self._call_api(**http_info)

    def create_mb_tasks_report_invoker(self, request):
        http_info = self._create_mb_tasks_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_mb_tasks_report_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/mediabox/tasks/report",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMbTasksReportResponse"
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

    def create_merge_channels_task(self, request):
        """创建声道合并任务

        创建声道合并任务，合并声道任务支持将每个声道各放一个文件中的片源，合并为单个音频文件。
        执行合并声道的源音频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMergeChannelsTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMergeChannelsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMergeChannelsTaskResponse`
        """
        http_info = self._create_merge_channels_task_http_info(request)
        return self._call_api(**http_info)

    def create_merge_channels_task_invoker(self, request):
        http_info = self._create_merge_channels_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_merge_channels_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audio/services/merge_channels/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMergeChannelsTaskResponse"
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

    def create_reset_tracks_task(self, request):
        """创建音轨重置任务

        创建音轨重置任务，重置音轨任务支持按人工指定关系声道layout，语言标签，转封装片源，使其满足转码输入。
        执行音轨重置的源音频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResetTracksTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateResetTracksTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateResetTracksTaskResponse`
        """
        http_info = self._create_reset_tracks_task_http_info(request)
        return self._call_api(**http_info)

    def create_reset_tracks_task_invoker(self, request):
        http_info = self._create_reset_tracks_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_reset_tracks_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/audio/services/reset_tracks/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResetTracksTaskResponse"
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

    def delete_merge_channels_task(self, request):
        """取消声道合并任务

        取消合并音频多声道文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMergeChannelsTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteMergeChannelsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteMergeChannelsTaskResponse`
        """
        http_info = self._delete_merge_channels_task_http_info(request)
        return self._call_api(**http_info)

    def delete_merge_channels_task_invoker(self, request):
        http_info = self._delete_merge_channels_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_merge_channels_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audio/services/merge_channels/task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMergeChannelsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def delete_reset_tracks_task(self, request):
        """取消音轨重置任务

        取消重置音频文件声轨任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResetTracksTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteResetTracksTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteResetTracksTaskResponse`
        """
        http_info = self._delete_reset_tracks_task_http_info(request)
        return self._call_api(**http_info)

    def delete_reset_tracks_task_invoker(self, request):
        http_info = self._delete_reset_tracks_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_reset_tracks_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/audio/services/reset_tracks/task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResetTracksTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_merge_channels_task(self, request):
        """查询声道合并任务

        查询声道合并任务的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMergeChannelsTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListMergeChannelsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListMergeChannelsTaskResponse`
        """
        http_info = self._list_merge_channels_task_http_info(request)
        return self._call_api(**http_info)

    def list_merge_channels_task_invoker(self, request):
        http_info = self._list_merge_channels_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_merge_channels_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audio/services/merge_channels/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListMergeChannelsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_reset_tracks_task(self, request):
        """查询音轨重置任务

        查询音轨重置任务的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResetTracksTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListResetTracksTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListResetTracksTaskResponse`
        """
        http_info = self._list_reset_tracks_task_http_info(request)
        return self._call_api(**http_info)

    def list_reset_tracks_task_invoker(self, request):
        http_info = self._list_reset_tracks_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_reset_tracks_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/audio/services/reset_tracks/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListResetTracksTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def create_media_process_task(self, request):
        """创建视频增强任务

        ## 典型场景 ##
          创建视频增强任务。
        
        ## 接口功能 ##
          创建视频增强任务。
        
        ## 接口约束 ##
          无。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMediaProcessTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMediaProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMediaProcessTaskResponse`
        """
        http_info = self._create_media_process_task_http_info(request)
        return self._call_api(**http_info)

    def create_media_process_task_invoker(self, request):
        http_info = self._create_media_process_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_media_process_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/enhancements",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMediaProcessTaskResponse"
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

    def delete_media_process_task(self, request):
        """取消视频增强任务

        ## 典型场景 ##
          取消视频增强任务。
        
        ## 接口功能 ##
          取消视频增强任务。
        
        ## 接口约束 ##
          仅可删除正在排队中的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMediaProcessTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteMediaProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteMediaProcessTaskResponse`
        """
        http_info = self._delete_media_process_task_http_info(request)
        return self._call_api(**http_info)

    def delete_media_process_task_invoker(self, request):
        http_info = self._delete_media_process_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_media_process_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/enhancements",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMediaProcessTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_media_process_task(self, request):
        """查询视频增强任务

        ## 典型场景 ##
          查询视频增强任务。
        
        ## 接口功能 ##
          查询视频增强任务。
        
        ## 接口约束 ##
          无。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMediaProcessTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListMediaProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListMediaProcessTaskResponse`
        """
        http_info = self._list_media_process_task_http_info(request)
        return self._call_api(**http_info)

    def list_media_process_task_invoker(self, request):
        http_info = self._list_media_process_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_media_process_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/enhancements",
            "request_type": request.__class__.__name__,
            "response_type": "ListMediaProcessTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def create_mpe_call_back(self, request):
        """mpe通知mpc

        ## 典型场景 ##
          mpe通知mpc。
        ## 接口功能 ##
          mpe调用此接口通知mpc转封装等结果。
        ## 接口约束 ##
          无。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateMpeCallBack
        :type request: :class:`huaweicloudsdkmpc.v1.CreateMpeCallBackRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateMpeCallBackResponse`
        """
        http_info = self._create_mpe_call_back_http_info(request)
        return self._call_api(**http_info)

    def create_mpe_call_back_invoker(self, request):
        http_info = self._create_mpe_call_back_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_mpe_call_back_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/mpe/notification",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMpeCallBackResponse"
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

    def create_quality_enhance_template(self, request):
        """创建视频增强模板

        创建视频增强模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateQualityEnhanceTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.CreateQualityEnhanceTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateQualityEnhanceTemplateResponse`
        """
        http_info = self._create_quality_enhance_template_http_info(request)
        return self._call_api(**http_info)

    def create_quality_enhance_template_invoker(self, request):
        http_info = self._create_quality_enhance_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_quality_enhance_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template/qualityenhance",
            "request_type": request.__class__.__name__,
            "response_type": "CreateQualityEnhanceTemplateResponse"
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

    def delete_quality_enhance_template(self, request):
        """删除用户视频增强模板

        删除用户视频增强模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteQualityEnhanceTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteQualityEnhanceTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteQualityEnhanceTemplateResponse`
        """
        http_info = self._delete_quality_enhance_template_http_info(request)
        return self._call_api(**http_info)

    def delete_quality_enhance_template_invoker(self, request):
        http_info = self._delete_quality_enhance_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_quality_enhance_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/template/qualityenhance",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteQualityEnhanceTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

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

    def list_quality_enhance_default_template(self, request):
        """查询视频增强预置模板

        查询视频增强预置模板，返回所有结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQualityEnhanceDefaultTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.ListQualityEnhanceDefaultTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListQualityEnhanceDefaultTemplateResponse`
        """
        http_info = self._list_quality_enhance_default_template_http_info(request)
        return self._call_api(**http_info)

    def list_quality_enhance_default_template_invoker(self, request):
        http_info = self._list_quality_enhance_default_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_quality_enhance_default_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/template/qualityenhance/default",
            "request_type": request.__class__.__name__,
            "response_type": "ListQualityEnhanceDefaultTemplateResponse"
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

    def update_quality_enhance_template(self, request):
        """更新视频增强模板

        更新视频增强模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateQualityEnhanceTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateQualityEnhanceTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateQualityEnhanceTemplateResponse`
        """
        http_info = self._update_quality_enhance_template_http_info(request)
        return self._call_api(**http_info)

    def update_quality_enhance_template_invoker(self, request):
        http_info = self._update_quality_enhance_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_quality_enhance_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/template/qualityenhance",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateQualityEnhanceTemplateResponse"
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

    def list_transcode_detail(self, request):
        """查询媒资转码详情

        查询媒资转码详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTranscodeDetail
        :type request: :class:`huaweicloudsdkmpc.v1.ListTranscodeDetailRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTranscodeDetailResponse`
        """
        http_info = self._list_transcode_detail_http_info(request)
        return self._call_api(**http_info)

    def list_transcode_detail_invoker(self, request):
        http_info = self._list_transcode_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_transcode_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/transcodings/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListTranscodeDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
            collection_formats['task_id'] = 'multi'

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

    def cancel_remux_task(self, request):
        """取消转封装任务

        取消已下发的转封装任务，仅支持取消正在排队中的任务。。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.CancelRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CancelRemuxTaskResponse`
        """
        http_info = self._cancel_remux_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_remux_task_invoker(self, request):
        http_info = self._cancel_remux_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_remux_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/remux",
            "request_type": request.__class__.__name__,
            "response_type": "CancelRemuxTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def create_remux_task(self, request):
        """新建转封装任务

        创建转封装任务，转换音视频文件的格式，但不改变其分辨率和码率。
        待转封装的媒资文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateRemuxTaskResponse`
        """
        http_info = self._create_remux_task_http_info(request)
        return self._call_api(**http_info)

    def create_remux_task_invoker(self, request):
        http_info = self._create_remux_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_remux_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/remux",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRemuxTaskResponse"
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

    def create_retry_remux_task(self, request):
        """重试转封装任务

        对失败的转封装任务进行重试。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRetryRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateRetryRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateRetryRemuxTaskResponse`
        """
        http_info = self._create_retry_remux_task_http_info(request)
        return self._call_api(**http_info)

    def create_retry_remux_task_invoker(self, request):
        http_info = self._create_retry_remux_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_retry_remux_task_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/remux",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRetryRemuxTaskResponse"
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

    def delete_remux_task(self, request):
        """删除转封装任务记录

        删除转封装任务记录，只能删除状态为“已取消”，“转码成功”，“转码失败”的任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteRemuxTaskResponse`
        """
        http_info = self._delete_remux_task_http_info(request)
        return self._call_api(**http_info)

    def delete_remux_task_invoker(self, request):
        http_info = self._delete_remux_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_remux_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/remux/task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRemuxTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_remux_task(self, request):
        """查询转封装任务

        查询转封装任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRemuxTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListRemuxTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListRemuxTaskResponse`
        """
        http_info = self._list_remux_task_http_info(request)
        return self._call_api(**http_info)

    def list_remux_task_invoker(self, request):
        http_info = self._list_remux_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_remux_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/remux",
            "request_type": request.__class__.__name__,
            "response_type": "ListRemuxTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def create_template_group(self, request):
        """新建转码模板组

        新建转码模板组，最多支持一进六出。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.CreateTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateTemplateGroupResponse`
        """
        http_info = self._create_template_group_http_info(request)
        return self._call_api(**http_info)

    def create_template_group_invoker(self, request):
        http_info = self._create_template_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template_group/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateGroupResponse"
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

    def delete_template_group(self, request):
        """删除转码模板组

        删除转码模板组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTemplateGroupResponse`
        """
        http_info = self._delete_template_group_http_info(request)
        return self._call_api(**http_info)

    def delete_template_group_invoker(self, request):
        http_info = self._delete_template_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_template_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/template_group/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))

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

    def list_template_group(self, request):
        """查询转码模板组

        查询转码模板组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.ListTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTemplateGroupResponse`
        """
        http_info = self._list_template_group_http_info(request)
        return self._call_api(**http_info)

    def list_template_group_invoker(self, request):
        http_info = self._list_template_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_group_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/template_group/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def update_template_group(self, request):
        """更新转码模板组

        修改模板组接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplateGroup
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateTemplateGroupResponse`
        """
        http_info = self._update_template_group_http_info(request)
        return self._call_api(**http_info)

    def update_template_group_invoker(self, request):
        http_info = self._update_template_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_template_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/template_group/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateGroupResponse"
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

    def create_thumbnails_task(self, request):
        """新建截图任务

        新建截图任务，视频截图将从首帧开始，按设置的时间间隔截图，最后截取末帧。
        待截图的视频文件需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        约束：
          暂只支持生成JPG格式的图片文件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateThumbnailsTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateThumbnailsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateThumbnailsTaskResponse`
        """
        http_info = self._create_thumbnails_task_http_info(request)
        return self._call_api(**http_info)

    def create_thumbnails_task_invoker(self, request):
        http_info = self._create_thumbnails_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_thumbnails_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/thumbnails",
            "request_type": request.__class__.__name__,
            "response_type": "CreateThumbnailsTaskResponse"
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

    def delete_thumbnails_task(self, request):
        """取消截图任务

        取消已下发截图任务。
        只能取消已接受尚在队列中等待处理的任务，已完成或正在执行阶段的任务不能取消。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteThumbnailsTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteThumbnailsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteThumbnailsTaskResponse`
        """
        http_info = self._delete_thumbnails_task_http_info(request)
        return self._call_api(**http_info)

    def delete_thumbnails_task_invoker(self, request):
        http_info = self._delete_thumbnails_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_thumbnails_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/thumbnails",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteThumbnailsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_thumbnails_task(self, request):
        """查询截图任务

        查询截图任务状态。返回任务执行结果，包括状态、输入、输出等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListThumbnailsTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListThumbnailsTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListThumbnailsTaskResponse`
        """
        http_info = self._list_thumbnails_task_http_info(request)
        return self._call_api(**http_info)

    def list_thumbnails_task_invoker(self, request):
        http_info = self._list_thumbnails_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_thumbnails_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/thumbnails",
            "request_type": request.__class__.__name__,
            "response_type": "ListThumbnailsTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_transcoding_task(self, request):
        """新建转码任务

        新建转码任务可以将视频进行转码，并在转码过程中压制水印、视频截图等。视频转码前需要配置转码模板。
        待转码的音视频需要存储在与媒体处理服务同区域的OBS桶中，且该OBS桶已授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTranscodingTask
        :type request: :class:`huaweicloudsdkmpc.v1.CreateTranscodingTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateTranscodingTaskResponse`
        """
        http_info = self._create_transcoding_task_http_info(request)
        return self._call_api(**http_info)

    def create_transcoding_task_invoker(self, request):
        http_info = self._create_transcoding_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_transcoding_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTranscodingTaskResponse"
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

    def delete_transcoding_task(self, request):
        """取消转码任务

        取消已下发转码任务。
        只能取消正在转码任务队列中排队的转码任务。已开始转码或已完成的转码任务不能取消。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTranscodingTask
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTranscodingTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTranscodingTaskResponse`
        """
        http_info = self._delete_transcoding_task_http_info(request)
        return self._call_api(**http_info)

    def delete_transcoding_task_invoker(self, request):
        http_info = self._delete_transcoding_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_transcoding_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTranscodingTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def delete_transcoding_task_by_console(self, request):
        """删除转码任务记录

        删除转码任务记录，只能删除状态为“已取消”，“转码成功”，“转码失败”的转码任务记录。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTranscodingTaskByConsole
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTranscodingTaskByConsoleRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTranscodingTaskByConsoleResponse`
        """
        http_info = self._delete_transcoding_task_by_console_http_info(request)
        return self._call_api(**http_info)

    def delete_transcoding_task_by_console_invoker(self, request):
        http_info = self._delete_transcoding_task_by_console_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_transcoding_task_by_console_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/transcodings/task",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTranscodingTaskByConsoleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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

    def list_stat_summary(self, request):
        """查询点播概览信息

        查询最近一周，最近一月或者自定义时间段的“转码时长”，“调用转码API次数”。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStatSummary
        :type request: :class:`huaweicloudsdkmpc.v1.ListStatSummaryRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListStatSummaryResponse`
        """
        http_info = self._list_stat_summary_http_info(request)
        return self._call_api(**http_info)

    def list_stat_summary_invoker(self, request):
        http_info = self._list_stat_summary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stat_summary_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/transcodings/summaries",
            "request_type": request.__class__.__name__,
            "response_type": "ListStatSummaryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def list_transcoding_task(self, request):
        """查询转码任务

        查询转码任务状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTranscodingTask
        :type request: :class:`huaweicloudsdkmpc.v1.ListTranscodingTaskRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTranscodingTaskResponse`
        """
        http_info = self._list_transcoding_task_http_info(request)
        return self._call_api(**http_info)

    def list_transcoding_task_invoker(self, request):
        http_info = self._list_transcoding_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_transcoding_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ListTranscodingTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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
        if 'x_language' in local_var_params:
            header_params['x-language'] = local_var_params['x_language']

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

    def create_trans_template(self, request):
        """新建转码模板

        新建转码模板，采用自定义的模板转码。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTransTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.CreateTransTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateTransTemplateResponse`
        """
        http_info = self._create_trans_template_http_info(request)
        return self._call_api(**http_info)

    def create_trans_template_invoker(self, request):
        http_info = self._create_trans_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_trans_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTransTemplateResponse"
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

    def delete_template(self, request):
        """删除转码模板

        删除转码模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

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

    def list_template(self, request):
        """查询转码模板

        查询用户自定义转码配置模板。
        支持指定模板ID查询，或分页全量查询。转码配置模板ID，最多10个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.ListTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListTemplateResponse`
        """
        http_info = self._list_template_http_info(request)
        return self._call_api(**http_info)

    def list_template_invoker(self, request):
        http_info = self._list_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def update_trans_template(self, request):
        """更新转码模板

        更新转码模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTransTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateTransTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateTransTemplateResponse`
        """
        http_info = self._update_trans_template_http_info(request)
        return self._call_api(**http_info)

    def update_trans_template_invoker(self, request):
        http_info = self._update_trans_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_trans_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTransTemplateResponse"
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

    def create_watermark_template(self, request):
        """新建水印模板

        自定义水印模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.CreateWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.CreateWatermarkTemplateResponse`
        """
        http_info = self._create_watermark_template_http_info(request)
        return self._call_api(**http_info)

    def create_watermark_template_invoker(self, request):
        http_info = self._create_watermark_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_watermark_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/template/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "CreateWatermarkTemplateResponse"
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

    def delete_watermark_template(self, request):
        """删除水印模板

        删除自定义水印模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.DeleteWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.DeleteWatermarkTemplateResponse`
        """
        http_info = self._delete_watermark_template_http_info(request)
        return self._call_api(**http_info)

    def delete_watermark_template_invoker(self, request):
        http_info = self._delete_watermark_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_watermark_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/template/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWatermarkTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_id' in local_var_params:
            query_params.append(('template_id', local_var_params['template_id']))

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

    def list_watermark_template(self, request):
        """查询水印模板

        查询自定义水印模板。支持指定模板ID查询，或分页全量查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.ListWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.ListWatermarkTemplateResponse`
        """
        http_info = self._list_watermark_template_http_info(request)
        return self._call_api(**http_info)

    def list_watermark_template_invoker(self, request):
        http_info = self._list_watermark_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_watermark_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/template/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "ListWatermarkTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

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

    def update_watermark_template(self, request):
        """更新水印模板

        更新自定义水印模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWatermarkTemplate
        :type request: :class:`huaweicloudsdkmpc.v1.UpdateWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkmpc.v1.UpdateWatermarkTemplateResponse`
        """
        http_info = self._update_watermark_template_http_info(request)
        return self._call_api(**http_info)

    def update_watermark_template_invoker(self, request):
        http_info = self._update_watermark_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_watermark_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/template/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateWatermarkTemplateResponse"
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

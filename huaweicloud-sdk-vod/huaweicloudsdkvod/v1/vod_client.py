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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkvod'")


class VodClient(Client):
    def __init__(self):
        super(VodClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkvod.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "VodClient":
                raise TypeError("client type error, support client type is VodClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def cancel_asset_transcode_task(self, request):
        """取消媒资转码任务

        取消媒资转码任务，只能取消排队中的转码任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelAssetTranscodeTask
        :type request: :class:`huaweicloudsdkvod.v1.CancelAssetTranscodeTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CancelAssetTranscodeTaskResponse`
        """
        http_info = self._cancel_asset_transcode_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_asset_transcode_task_invoker(self, request):
        http_info = self._cancel_asset_transcode_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_asset_transcode_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/asset/process",
            "request_type": request.__class__.__name__,
            "response_type": "CancelAssetTranscodeTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))

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

    def cancel_extract_audio_task(self, request):
        """取消提取音频任务

        取消提取音频任务，只有排队中的提取音频任务才可以取消。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelExtractAudioTask
        :type request: :class:`huaweicloudsdkvod.v1.CancelExtractAudioTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CancelExtractAudioTaskResponse`
        """
        http_info = self._cancel_extract_audio_task_http_info(request)
        return self._call_api(**http_info)

    def cancel_extract_audio_task_invoker(self, request):
        http_info = self._cancel_extract_audio_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_extract_audio_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/asset/extract_audio",
            "request_type": request.__class__.__name__,
            "response_type": "CancelExtractAudioTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))

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

    def check_md5_duplication(self, request):
        """上传检验

        校验媒资文件是否已存储于视频点播服务中。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckMd5Duplication
        :type request: :class:`huaweicloudsdkvod.v1.CheckMd5DuplicationRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CheckMd5DuplicationResponse`
        """
        http_info = self._check_md5_duplication_http_info(request)
        return self._call_api(**http_info)

    def check_md5_duplication_invoker(self, request):
        http_info = self._check_md5_duplication_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_md5_duplication_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/duplication",
            "request_type": request.__class__.__name__,
            "response_type": "CheckMd5DuplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'md5' in local_var_params:
            query_params.append(('md5', local_var_params['md5']))

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

    def confirm_asset_upload(self, request):
        """确认媒资上传

        媒资分段上传完成后，需要调用此接口通知点播服务媒资上传的状态，表示媒资上传创建完成。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmAssetUpload
        :type request: :class:`huaweicloudsdkvod.v1.ConfirmAssetUploadRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ConfirmAssetUploadResponse`
        """
        http_info = self._confirm_asset_upload_http_info(request)
        return self._call_api(**http_info)

    def confirm_asset_upload_invoker(self, request):
        http_info = self._confirm_asset_upload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_asset_upload_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/status/uploaded",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmAssetUploadResponse"
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

    def confirm_image_upload(self, request):
        """确认水印图片上传

        确认水印图片上传状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ConfirmImageUpload
        :type request: :class:`huaweicloudsdkvod.v1.ConfirmImageUploadRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ConfirmImageUploadResponse`
        """
        http_info = self._confirm_image_upload_http_info(request)
        return self._call_api(**http_info)

    def confirm_image_upload_invoker(self, request):
        http_info = self._confirm_image_upload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _confirm_image_upload_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/watermark/status/uploaded",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmImageUploadResponse"
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

    def create_asset_by_file_upload(self, request):
        """创建媒资：上传方式

        调用该接口创建媒资时，需要将对应的媒资文件上传到点播服务的OBS桶中。
        
        若上传的单媒资文件大小小于20M，则可以直接用PUT方法对该接口返回的地址进行上传。具体使用方法请参考[示例1：媒资上传（20M以下）](https://support.huaweicloud.com/api-vod/vod_04_0195.html)。
        
        若上传的单个媒资大小大于20M，则需要进行二进制流分割后上传，该接口的具体使用方法请参考[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetByFileUpload
        :type request: :class:`huaweicloudsdkvod.v1.CreateAssetByFileUploadRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateAssetByFileUploadResponse`
        """
        http_info = self._create_asset_by_file_upload_http_info(request)
        return self._call_api(**http_info)

    def create_asset_by_file_upload_invoker(self, request):
        http_info = self._create_asset_by_file_upload_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_by_file_upload_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetByFileUploadResponse"
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

    def create_asset_category(self, request):
        """创建媒资分类

        创建媒资分类。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetCategory
        :type request: :class:`huaweicloudsdkvod.v1.CreateAssetCategoryRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateAssetCategoryResponse`
        """
        http_info = self._create_asset_category_http_info(request)
        return self._call_api(**http_info)

    def create_asset_category_invoker(self, request):
        http_info = self._create_asset_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_category_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/category",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetCategoryResponse"
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

    def create_asset_process_task(self, request):
        """媒资处理

        实现视频转码、截图、加密等处理。既可以同时启动多种操作，也可以只启动一种操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetProcessTask
        :type request: :class:`huaweicloudsdkvod.v1.CreateAssetProcessTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateAssetProcessTaskResponse`
        """
        http_info = self._create_asset_process_task_http_info(request)
        return self._call_api(**http_info)

    def create_asset_process_task_invoker(self, request):
        http_info = self._create_asset_process_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_process_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/process",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetProcessTaskResponse"
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

    def create_asset_review_task(self, request):
        """创建审核媒资任务

        对上传的媒资进行审核。审核后，可以调用[查询媒资详细信息](https://support.huaweicloud.com/api-vod/vod_04_0202.html)接口查看审核结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetReviewTask
        :type request: :class:`huaweicloudsdkvod.v1.CreateAssetReviewTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateAssetReviewTaskResponse`
        """
        http_info = self._create_asset_review_task_http_info(request)
        return self._call_api(**http_info)

    def create_asset_review_task_invoker(self, request):
        http_info = self._create_asset_review_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_review_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/review",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetReviewTaskResponse"
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

    def create_extract_audio_task(self, request):
        """音频提取

        本接口为异步接口，创建音频提取任务下发成功后会返回asset_id和提取的audio_asset_id，但此时音频提取任务并没有立即完成，可通过消息订阅界面配置的音频提取完成事件来获取音频提取任务完成与否。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateExtractAudioTask
        :type request: :class:`huaweicloudsdkvod.v1.CreateExtractAudioTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateExtractAudioTaskResponse`
        """
        http_info = self._create_extract_audio_task_http_info(request)
        return self._call_api(**http_info)

    def create_extract_audio_task_invoker(self, request):
        http_info = self._create_extract_audio_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_extract_audio_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/extract_audio",
            "request_type": request.__class__.__name__,
            "response_type": "CreateExtractAudioTaskResponse"
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

    def create_preheating_asset(self, request):
        """CDN预热

        媒资发布后，可通过指定媒资ID或URL向CDN预热。用户初次请求时，将由CDN节点提供请求媒资，加快用户下载缓存时间，提高用户体验。单租户每天最多预热1000个。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePreheatingAsset
        :type request: :class:`huaweicloudsdkvod.v1.CreatePreheatingAssetRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreatePreheatingAssetResponse`
        """
        http_info = self._create_preheating_asset_http_info(request)
        return self._call_api(**http_info)

    def create_preheating_asset_invoker(self, request):
        http_info = self._create_preheating_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_preheating_asset_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/preheating",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePreheatingAssetResponse"
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

    def create_take_over_task(self, request):
        """创建媒资：OBS托管方式

        通过存量托管的方式，将已存储在OBS桶中的音视频文件同步到点播服务。
        
        OBS托管方式分为增量托管和存量托管，增量托管暂只支持通过视频点播控制台配置，配置后，若OBS有新增音视频文件，则会自动同步到点播服务中，具体请参见[增量托管](https://support.huaweicloud.com/usermanual-vod/vod010032.html)。两个托管方式都需要先将对应的OBS桶授权给点播服务，具体请参见[桶授权](https://support.huaweicloud.com/usermanual-vod/vod010031.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTakeOverTask
        :type request: :class:`huaweicloudsdkvod.v1.CreateTakeOverTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateTakeOverTaskResponse`
        """
        http_info = self._create_take_over_task_http_info(request)
        return self._call_api(**http_info)

    def create_take_over_task_invoker(self, request):
        http_info = self._create_take_over_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_take_over_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/obs/host/stock/task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTakeOverTaskResponse"
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

    def create_template_group(self, request):
        """创建自定义转码模板组

        创建自定义转码模板组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplateGroup
        :type request: :class:`huaweicloudsdkvod.v1.CreateTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateTemplateGroupResponse`
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
            "resource_path": "/v1.0/{project_id}/asset/template_group/transcodings",
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

    def create_template_group_collection(self, request):
        """创建转码模板组集合

        创建转码模板组集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplateGroupCollection
        :type request: :class:`huaweicloudsdkvod.v1.CreateTemplateGroupCollectionRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateTemplateGroupCollectionResponse`
        """
        http_info = self._create_template_group_collection_http_info(request)
        return self._call_api(**http_info)

    def create_template_group_collection_invoker(self, request):
        http_info = self._create_template_group_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_template_group_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/template-collection/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateGroupCollectionResponse"
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

    def create_transcode_template(self, request):
        """创建自定义转码模板

        创建自定义转码模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTranscodeTemplate
        :type request: :class:`huaweicloudsdkvod.v1.CreateTranscodeTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateTranscodeTemplateResponse`
        """
        http_info = self._create_transcode_template_http_info(request)
        return self._call_api(**http_info)

    def create_transcode_template_invoker(self, request):
        http_info = self._create_transcode_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_transcode_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/asset/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTranscodeTemplateResponse"
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
        """创建水印模板

        创建水印模板。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWatermarkTemplate
        :type request: :class:`huaweicloudsdkvod.v1.CreateWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.CreateWatermarkTemplateResponse`
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
            "resource_path": "/v1.0/{project_id}/template/watermark",
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

    def delete_asset_category(self, request):
        """删除媒资分类

        删除媒资分类。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssetCategory
        :type request: :class:`huaweicloudsdkvod.v1.DeleteAssetCategoryRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.DeleteAssetCategoryResponse`
        """
        http_info = self._delete_asset_category_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_category_invoker(self, request):
        http_info = self._delete_asset_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_asset_category_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/asset/category",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetCategoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def delete_assets(self, request):
        """删除媒资

        删除媒资。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssets
        :type request: :class:`huaweicloudsdkvod.v1.DeleteAssetsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.DeleteAssetsResponse`
        """
        http_info = self._delete_assets_http_info(request)
        return self._call_api(**http_info)

    def delete_assets_invoker(self, request):
        http_info = self._delete_assets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_assets_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/asset",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'multi'
        if 'delete_type' in local_var_params:
            query_params.append(('delete_type', local_var_params['delete_type']))

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

    def delete_template_group(self, request):
        """删除自定义转码模板组

        删除自定义转码模板组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateGroup
        :type request: :class:`huaweicloudsdkvod.v1.DeleteTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.DeleteTemplateGroupResponse`
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
            "resource_path": "/v1.0/{project_id}/asset/template_group/transcodings",
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

    def delete_template_group_collection(self, request):
        """删除转码模板组集合

        删除转码模板组集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplateGroupCollection
        :type request: :class:`huaweicloudsdkvod.v1.DeleteTemplateGroupCollectionRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.DeleteTemplateGroupCollectionResponse`
        """
        http_info = self._delete_template_group_collection_http_info(request)
        return self._call_api(**http_info)

    def delete_template_group_collection_invoker(self, request):
        http_info = self._delete_template_group_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_template_group_collection_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/asset/template-collection/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateGroupCollectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_collection_id' in local_var_params:
            query_params.append(('group_collection_id', local_var_params['group_collection_id']))

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

    def delete_transcode_template(self, request):
        """删除自定义模板

        删除自定义模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTranscodeTemplate
        :type request: :class:`huaweicloudsdkvod.v1.DeleteTranscodeTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.DeleteTranscodeTemplateResponse`
        """
        http_info = self._delete_transcode_template_http_info(request)
        return self._call_api(**http_info)

    def delete_transcode_template_invoker(self, request):
        http_info = self._delete_transcode_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_transcode_template_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/asset/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTranscodeTemplateResponse"
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

    def delete_watermark_template(self, request):
        """删除水印模板

        删除水印模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWatermarkTemplate
        :type request: :class:`huaweicloudsdkvod.v1.DeleteWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.DeleteWatermarkTemplateResponse`
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
            "resource_path": "/v1.0/{project_id}/template/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteWatermarkTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def list_asset_category(self, request):
        """查询指定分类信息

        查询指定分类信息，及其子分类（即下一级分类）的列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssetCategory
        :type request: :class:`huaweicloudsdkvod.v1.ListAssetCategoryRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListAssetCategoryResponse`
        """
        http_info = self._list_asset_category_http_info(request)
        return self._call_api(**http_info)

    def list_asset_category_invoker(self, request):
        http_info = self._list_asset_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_asset_category_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/category",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetCategoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

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

    def list_asset_daily_summary_log(self, request):
        """查询媒资日播放统计数据

        查询媒资日播放统计数据。
        
        使用媒资日播放统计查询API前，需要先提交工单开通统计功能，才能触发统计任务。
        
        支持查询最近一年的播放统计数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssetDailySummaryLog
        :type request: :class:`huaweicloudsdkvod.v1.ListAssetDailySummaryLogRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListAssetDailySummaryLogResponse`
        """
        http_info = self._list_asset_daily_summary_log_http_info(request)
        return self._call_api(**http_info)

    def list_asset_daily_summary_log_invoker(self, request):
        http_info = self._list_asset_daily_summary_log_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_asset_daily_summary_log_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/asset/daily-summary",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetDailySummaryLogResponse"
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

    def list_asset_list(self, request):
        """查询媒资列表

        查询媒资列表，列表中的每一条记录包含媒资的概要信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssetList
        :type request: :class:`huaweicloudsdkvod.v1.ListAssetListRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListAssetListResponse`
        """
        http_info = self._list_asset_list_http_info(request)
        return self._call_api(**http_info)

    def list_asset_list_invoker(self, request):
        http_info = self._list_asset_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_asset_list_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'csv'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'query_string' in local_var_params:
            query_params.append(('query_string', local_var_params['query_string']))
        if 'media_type' in local_var_params:
            query_params.append(('media_type', local_var_params['media_type']))
            collection_formats['media_type'] = 'csv'
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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

    def list_domain_logs(self, request):
        """查询域名播放日志

        查询指定点播域名某段时间内在CDN的相关日志。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainLogs
        :type request: :class:`huaweicloudsdkvod.v1.ListDomainLogsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListDomainLogsResponse`
        """
        http_info = self._list_domain_logs_http_info(request)
        return self._call_api(**http_info)

    def list_domain_logs_invoker(self, request):
        http_info = self._list_domain_logs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_logs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/vod/cdn/logs",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainLogsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain_name' in local_var_params:
            query_params.append(('domain_name', local_var_params['domain_name']))
        if 'query_date' in local_var_params:
            query_params.append(('query_date', local_var_params['query_date']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'page_number' in local_var_params:
            query_params.append(('page_number', local_var_params['page_number']))

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
        """查询转码模板组列表

        查询转码模板组列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateGroup
        :type request: :class:`huaweicloudsdkvod.v1.ListTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListTemplateGroupResponse`
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
            "resource_path": "/v1.0/{project_id}/asset/template_group/transcodings",
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
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_template_group_collection(self, request):
        """查询自定义模板组集合

        查询转码模板组集合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplateGroupCollection
        :type request: :class:`huaweicloudsdkvod.v1.ListTemplateGroupCollectionRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListTemplateGroupCollectionResponse`
        """
        http_info = self._list_template_group_collection_http_info(request)
        return self._call_api(**http_info)

    def list_template_group_collection_invoker(self, request):
        http_info = self._list_template_group_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_template_group_collection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/template-collection/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplateGroupCollectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_collection_id' in local_var_params:
            query_params.append(('group_collection_id', local_var_params['group_collection_id']))
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

    def list_top_statistics(self, request):
        """查询TopN媒资信息

        查询指定域名在指定日期播放次数排名Top 100的媒资统计数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTopStatistics
        :type request: :class:`huaweicloudsdkvod.v1.ListTopStatisticsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListTopStatisticsResponse`
        """
        http_info = self._list_top_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_top_statistics_invoker(self, request):
        http_info = self._list_top_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_top_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/top-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'date' in local_var_params:
            query_params.append(('date', local_var_params['date']))

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

    def list_transcode_template(self, request):
        """查询转码模板列表

        查询转码模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTranscodeTemplate
        :type request: :class:`huaweicloudsdkvod.v1.ListTranscodeTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListTranscodeTemplateResponse`
        """
        http_info = self._list_transcode_template_http_info(request)
        return self._call_api(**http_info)

    def list_transcode_template_invoker(self, request):
        http_info = self._list_transcode_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_transcode_template_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/asset/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "ListTranscodeTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'is_default' in local_var_params:
            query_params.append(('is_default', local_var_params['is_default']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query_string' in local_var_params:
            query_params.append(('query_string', local_var_params['query_string']))

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
        """查询水印列表

        查询水印模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWatermarkTemplate
        :type request: :class:`huaweicloudsdkvod.v1.ListWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListWatermarkTemplateResponse`
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
            "resource_path": "/v1.0/{project_id}/template/watermark",
            "request_type": request.__class__.__name__,
            "response_type": "ListWatermarkTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
            collection_formats['id'] = 'multi'
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

    def publish_asset_from_obs(self, request):
        """创建媒资：OBS转存方式

        若您在使用点播服务前，已经在OBS桶中存储了音视频文件，您可以使用该接口将存储在OBS桶中的音视频文件转存到点播服务中，使用点播服务的音视频管理功能。调用该接口前，您需要调用[桶授权](https://support.huaweicloud.com/api-vod/vod_04_0199.html)接口，将存储音视频文件的OBS桶授权给点播服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishAssetFromObs
        :type request: :class:`huaweicloudsdkvod.v1.PublishAssetFromObsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.PublishAssetFromObsResponse`
        """
        http_info = self._publish_asset_from_obs_http_info(request)
        return self._call_api(**http_info)

    def publish_asset_from_obs_invoker(self, request):
        http_info = self._publish_asset_from_obs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_asset_from_obs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/reproduction",
            "request_type": request.__class__.__name__,
            "response_type": "PublishAssetFromObsResponse"
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

    def publish_assets(self, request):
        """媒资发布

        将媒资设置为发布状态。支持批量发布。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishAssets
        :type request: :class:`huaweicloudsdkvod.v1.PublishAssetsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.PublishAssetsResponse`
        """
        http_info = self._publish_assets_http_info(request)
        return self._call_api(**http_info)

    def publish_assets_invoker(self, request):
        http_info = self._publish_assets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_assets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/status/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishAssetsResponse"
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

    def show_asset_cipher(self, request):
        """密钥查询

        终端播放HLS加密视频时，向租户管理系统请求密钥，租户管理系统先查询其本地有没有已缓存的密钥，没有时则调用此接口向VOD查询。该接口的具体使用场景请参见[通过HLS加密防止视频泄露](https://support.huaweicloud.com/bestpractice-vod/vod_10_0004.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetCipher
        :type request: :class:`huaweicloudsdkvod.v1.ShowAssetCipherRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowAssetCipherResponse`
        """
        http_info = self._show_asset_cipher_http_info(request)
        return self._call_api(**http_info)

    def show_asset_cipher_invoker(self, request):
        http_info = self._show_asset_cipher_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_cipher_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/ciphers",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetCipherResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))

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

    def show_asset_detail(self, request):
        """查询指定媒资的详细信息

        查询指定媒资的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetDetail
        :type request: :class:`huaweicloudsdkvod.v1.ShowAssetDetailRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowAssetDetailResponse`
        """
        http_info = self._show_asset_detail_http_info(request)
        return self._call_api(**http_info)

    def show_asset_detail_invoker(self, request):
        http_info = self._show_asset_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
        if 'categories' in local_var_params:
            query_params.append(('categories', local_var_params['categories']))
            collection_formats['categories'] = 'csv'

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

    def show_asset_meta(self, request):
        """查询媒资信息

        查询媒资信息，支持指定媒资ID、分类、状态、起止时间查询。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetMeta
        :type request: :class:`huaweicloudsdkvod.v1.ShowAssetMetaRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowAssetMetaResponse`
        """
        http_info = self._show_asset_meta_http_info(request)
        return self._call_api(**http_info)

    def show_asset_meta_invoker(self, request):
        http_info = self._show_asset_meta_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_meta_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetMetaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
            collection_formats['asset_id'] = 'multi'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
            collection_formats['status'] = 'multi'
        if 'transcode_status' in local_var_params:
            query_params.append(('transcodeStatus', local_var_params['transcode_status']))
            collection_formats['transcodeStatus'] = 'multi'
        if 'asset_status' in local_var_params:
            query_params.append(('assetStatus', local_var_params['asset_status']))
            collection_formats['assetStatus'] = 'multi'
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'category_id' in local_var_params:
            query_params.append(('category_id', local_var_params['category_id']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))
        if 'query_string' in local_var_params:
            query_params.append(('query_string', local_var_params['query_string']))
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

    def show_asset_temp_authority(self, request):
        """获取分段上传授权

        客户端请求创建媒资时，如果媒资文件超过20MB，需采用分段的方式向OBS上传，在每次与OBS交互前，客户端需通过此接口获取到授权方可与OBS交互。
        
        该接口可以获取[初始化多段上传任务](https://support.huaweicloud.com/api-obs/obs_04_0098.html)、[上传段](https://support.huaweicloud.com/api-obs/obs_04_0099.html)、[合并段](https://support.huaweicloud.com/api-obs/obs_04_0102.html)、[列举已上传段](https://support.huaweicloud.com/api-obs/obs_04_0101.html)、[取消段合并](https://support.huaweicloud.com/api-obs/obs_04_0103.html)的带有临时授权的URL，用户需要根据OBS的接口文档配置相应请求的HTTP请求方法、请求头、请求体，然后请求对应的带有临时授权的URL。
        
        视频分段上传方式和OBS的接口文档保持一致，包括HTTP请求方法、请求头、请求体等各种入参，此接口的作用是为用户生成带有鉴权信息的URL（鉴权信息即query_str），用来替换OBS接口中对应的URL，临时给用户开通向点播服务的桶上传文件的权限。
        
        调用获取授权接口时需要传入bucket、object_key、http_verb，其中bucket和object_key是由[创建媒资：上传方式](https://support.huaweicloud.com/api-vod/vod_04_0196.html)接口中返回的响应体中的target字段获得的bucket和object，http_verb需要根据指定的操作选择。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetTempAuthority
        :type request: :class:`huaweicloudsdkvod.v1.ShowAssetTempAuthorityRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowAssetTempAuthorityResponse`
        """
        http_info = self._show_asset_temp_authority_http_info(request)
        return self._call_api(**http_info)

    def show_asset_temp_authority_invoker(self, request):
        http_info = self._show_asset_temp_authority_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_temp_authority_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.1/{project_id}/asset/authority",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetTempAuthorityResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'http_verb' in local_var_params:
            query_params.append(('http_verb', local_var_params['http_verb']))
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))
        if 'object_key' in local_var_params:
            query_params.append(('object_key', local_var_params['object_key']))
        if 'content_type' in local_var_params:
            query_params.append(('content_type', local_var_params['content_type']))
        if 'content_md5' in local_var_params:
            query_params.append(('content_md5', local_var_params['content_md5']))
        if 'upload_id' in local_var_params:
            query_params.append(('upload_id', local_var_params['upload_id']))
        if 'part_number' in local_var_params:
            query_params.append(('part_number', local_var_params['part_number']))

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

    def show_cdn_statistics(self, request):
        """查询CDN统计信息

        查询CDN的统计数据，包括流量、峰值带宽、请求总数、请求命中率、流量命中率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCdnStatistics
        :type request: :class:`huaweicloudsdkvod.v1.ShowCdnStatisticsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowCdnStatisticsResponse`
        """
        http_info = self._show_cdn_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_cdn_statistics_invoker(self, request):
        http_info = self._show_cdn_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_cdn_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/cdn-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCdnStatisticsResponse"
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
        if 'domain' in local_var_params:
            query_params.append(('domain', local_var_params['domain']))
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

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

    def show_preheating_asset(self, request):
        """查询CDN预热

        查询预热结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPreheatingAsset
        :type request: :class:`huaweicloudsdkvod.v1.ShowPreheatingAssetRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowPreheatingAssetResponse`
        """
        http_info = self._show_preheating_asset_http_info(request)
        return self._call_api(**http_info)

    def show_preheating_asset_invoker(self, request):
        http_info = self._show_preheating_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_preheating_asset_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/preheating",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPreheatingAssetResponse"
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

    def show_vod_statistics(self, request):
        """查询源站统计信息

        查询点播源站的统计数据，包括流量、存储空间、转码时长。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVodStatistics
        :type request: :class:`huaweicloudsdkvod.v1.ShowVodStatisticsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowVodStatisticsResponse`
        """
        http_info = self._show_vod_statistics_http_info(request)
        return self._call_api(**http_info)

    def show_vod_statistics_invoker(self, request):
        http_info = self._show_vod_statistics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vod_statistics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/vod-statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVodStatisticsResponse"
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
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

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

    def unpublish_assets(self, request):
        """媒资发布取消

        将媒资设置为未发布状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UnpublishAssets
        :type request: :class:`huaweicloudsdkvod.v1.UnpublishAssetsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UnpublishAssetsResponse`
        """
        http_info = self._unpublish_assets_http_info(request)
        return self._call_api(**http_info)

    def unpublish_assets_invoker(self, request):
        http_info = self._unpublish_assets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _unpublish_assets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/status/unpublish",
            "request_type": request.__class__.__name__,
            "response_type": "UnpublishAssetsResponse"
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

    def update_asset(self, request):
        """视频更新

        媒资创建后，单独上传封面、更新视频文件或更新已有封面。
        
        如果是更新视频文件，更新完后要通过[确认媒资上传](https://support.huaweicloud.com/api-vod/vod_04_0198.html)接口通知点播服务。
        
        如果是更新封面或单独上传封面，则不需通知。
        
        更新视频可以使用分段上传，具体方式可以参考[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAsset
        :type request: :class:`huaweicloudsdkvod.v1.UpdateAssetRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateAssetResponse`
        """
        http_info = self._update_asset_http_info(request)
        return self._call_api(**http_info)

    def update_asset_invoker(self, request):
        http_info = self._update_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_asset_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/asset",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetResponse"
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

    def update_asset_category(self, request):
        """修改媒资分类

        修改媒资分类。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssetCategory
        :type request: :class:`huaweicloudsdkvod.v1.UpdateAssetCategoryRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateAssetCategoryResponse`
        """
        http_info = self._update_asset_category_http_info(request)
        return self._call_api(**http_info)

    def update_asset_category_invoker(self, request):
        http_info = self._update_asset_category_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_asset_category_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/asset/category",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetCategoryResponse"
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

    def update_asset_meta(self, request):
        """修改媒资属性

        修改媒资属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssetMeta
        :type request: :class:`huaweicloudsdkvod.v1.UpdateAssetMetaRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateAssetMetaResponse`
        """
        http_info = self._update_asset_meta_http_info(request)
        return self._call_api(**http_info)

    def update_asset_meta_invoker(self, request):
        http_info = self._update_asset_meta_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_asset_meta_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/asset/info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetMetaResponse"
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

    def update_bucket_authorized(self, request):
        """桶授权

        用户可以通过该接口将OBS桶授权给点播服务或取消点播服务的授权。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBucketAuthorized
        :type request: :class:`huaweicloudsdkvod.v1.UpdateBucketAuthorizedRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateBucketAuthorizedResponse`
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
            "resource_path": "/v1.0/{project_id}/asset/authority",
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

    def update_cover_by_thumbnail(self, request):
        """设置封面

        将视频截图生成的某张图片设置成封面。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCoverByThumbnail
        :type request: :class:`huaweicloudsdkvod.v1.UpdateCoverByThumbnailRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateCoverByThumbnailResponse`
        """
        http_info = self._update_cover_by_thumbnail_http_info(request)
        return self._call_api(**http_info)

    def update_cover_by_thumbnail_invoker(self, request):
        http_info = self._update_cover_by_thumbnail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_cover_by_thumbnail_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/asset/cover",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCoverByThumbnailResponse"
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

    def update_template_group(self, request):
        """修改自定义转码模板组

        修改自定义转码模板组。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplateGroup
        :type request: :class:`huaweicloudsdkvod.v1.UpdateTemplateGroupRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateTemplateGroupResponse`
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
            "resource_path": "/v1.0/{project_id}/asset/template_group/transcodings",
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

    def update_template_group_collection(self, request):
        """修改转码模板组集合

        修改转码模板组结合
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemplateGroupCollection
        :type request: :class:`huaweicloudsdkvod.v1.UpdateTemplateGroupCollectionRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateTemplateGroupCollectionResponse`
        """
        http_info = self._update_template_group_collection_http_info(request)
        return self._call_api(**http_info)

    def update_template_group_collection_invoker(self, request):
        http_info = self._update_template_group_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_template_group_collection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/asset/template-collection/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateGroupCollectionResponse"
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

    def update_transcode_template(self, request):
        """修改转码模板

        修改转码模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTranscodeTemplate
        :type request: :class:`huaweicloudsdkvod.v1.UpdateTranscodeTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateTranscodeTemplateResponse`
        """
        http_info = self._update_transcode_template_http_info(request)
        return self._call_api(**http_info)

    def update_transcode_template_invoker(self, request):
        http_info = self._update_transcode_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_transcode_template_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/asset/template/transcodings",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTranscodeTemplateResponse"
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

    def update_watermark_template(self, request):
        """修改水印模板

        修改水印模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWatermarkTemplate
        :type request: :class:`huaweicloudsdkvod.v1.UpdateWatermarkTemplateRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateWatermarkTemplateResponse`
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
            "resource_path": "/v1.0/{project_id}/template/watermark",
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

    def upload_meta_data_by_url(self, request):
        """创建媒资：URL拉取注入

        基于音视频源文件URL，将音视频文件离线拉取上传到点播服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadMetaDataByUrl
        :type request: :class:`huaweicloudsdkvod.v1.UploadMetaDataByUrlRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UploadMetaDataByUrlResponse`
        """
        http_info = self._upload_meta_data_by_url_http_info(request)
        return self._call_api(**http_info)

    def upload_meta_data_by_url_invoker(self, request):
        http_info = self._upload_meta_data_by_url_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_meta_data_by_url_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/asset/upload_by_url",
            "request_type": request.__class__.__name__,
            "response_type": "UploadMetaDataByUrlResponse"
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

    def list_take_over_task(self, request):
        """查询托管任务

        查询OBS存量托管任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTakeOverTask
        :type request: :class:`huaweicloudsdkvod.v1.ListTakeOverTaskRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ListTakeOverTaskResponse`
        """
        http_info = self._list_take_over_task_http_info(request)
        return self._call_api(**http_info)

    def list_take_over_task_invoker(self, request):
        http_info = self._list_take_over_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_take_over_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/obs/host/stock/task",
            "request_type": request.__class__.__name__,
            "response_type": "ListTakeOverTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
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

    def show_take_over_asset_details(self, request):
        """查询托管媒资详情

        查询OBS托管媒资的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTakeOverAssetDetails
        :type request: :class:`huaweicloudsdkvod.v1.ShowTakeOverAssetDetailsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowTakeOverAssetDetailsResponse`
        """
        http_info = self._show_take_over_asset_details_http_info(request)
        return self._call_api(**http_info)

    def show_take_over_asset_details_invoker(self, request):
        http_info = self._show_take_over_asset_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_take_over_asset_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/obs/host/task/details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTakeOverAssetDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_bucket' in local_var_params:
            query_params.append(('source_bucket', local_var_params['source_bucket']))
        if 'source_object' in local_var_params:
            query_params.append(('source_object', local_var_params['source_object']))

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

    def show_take_over_task_details(self, request):
        """查询托管任务详情

        查询OBS存量托管任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTakeOverTaskDetails
        :type request: :class:`huaweicloudsdkvod.v1.ShowTakeOverTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowTakeOverTaskDetailsResponse`
        """
        http_info = self._show_take_over_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_take_over_task_details_invoker(self, request):
        http_info = self._show_take_over_task_details_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_take_over_task_details_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/asset/obs/host/stock/task/details",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTakeOverTaskDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))
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

    def show_vod_retrieval(self, request):
        """查询取回数据信息

        ## 典型场景 ##
         用于查询点播低频和归档取回量统计数据。&lt;br/&gt;
        
        ## 接口功能 ##
         用于查询点播低频和归档取回量统计数据。&lt;br/&gt;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVodRetrieval
        :type request: :class:`huaweicloudsdkvod.v1.ShowVodRetrievalRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ShowVodRetrievalResponse`
        """
        http_info = self._show_vod_retrieval_http_info(request)
        return self._call_api(**http_info)

    def show_vod_retrieval_invoker(self, request):
        http_info = self._show_vod_retrieval_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_vod_retrieval_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/asset/vod-retrieval",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVodRetrievalResponse"
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
        if 'interval' in local_var_params:
            query_params.append(('interval', local_var_params['interval']))

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

    def update_storage_mode(self, request):
        """修改媒资文件在obs的存储模式

        ## 接口功能 ##
          修改媒资文件在obs的存储模式&lt;br/&gt;
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStorageMode
        :type request: :class:`huaweicloudsdkvod.v1.UpdateStorageModeRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.UpdateStorageModeResponse`
        """
        http_info = self._update_storage_mode_http_info(request)
        return self._call_api(**http_info)

    def update_storage_mode_invoker(self, request):
        http_info = self._update_storage_mode_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_storage_mode_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/asset/storage-mode",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStorageModeResponse"
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

    def modify_subtitle(self, request):
        """多字幕封装

        多字幕封装，仅支持 HLS VTT格式
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ModifySubtitle
        :type request: :class:`huaweicloudsdkvod.v1.ModifySubtitleRequest`
        :rtype: :class:`huaweicloudsdkvod.v1.ModifySubtitleResponse`
        """
        http_info = self._modify_subtitle_http_info(request)
        return self._call_api(**http_info)

    def modify_subtitle_invoker(self, request):
        http_info = self._modify_subtitle_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _modify_subtitle_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/asset/subtitles",
            "request_type": request.__class__.__name__,
            "response_type": "ModifySubtitleResponse"
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

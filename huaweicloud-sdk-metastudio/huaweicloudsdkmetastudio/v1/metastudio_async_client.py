# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkmetastudio'")


class MetaStudioAsyncClient(Client):
    def __init__(self):
        super(MetaStudioAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkmetastudio.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "MetaStudioAsyncClient":
                raise TypeError("client type error, support client type is MetaStudioAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_dialog_url_async(self, request):
        """创建对话链接

        该接口用于创建对话链接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDialogUrl
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDialogUrlRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDialogUrlResponse`
        """
        http_info = self._create_dialog_url_http_info(request)
        return self._call_api(**http_info)

    def create_dialog_url_async_invoker(self, request):
        http_info = self._create_dialog_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_dialog_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/create-dialog-url",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDialogUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_smart_chat_job_async(self, request):
        """查询数字人智能交互任务

        该接口用于查询数字人智能交互任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatJobResponse`
        """
        http_info = self._show_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def show_smart_chat_job_async_invoker(self, request):
        http_info = self._show_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs/{job_id}/state",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def start_smart_chat_job_async(self, request):
        """启动数字人智能交互任务

        该接口用于启动数字人智能交互任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.StartSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StartSmartChatJobResponse`
        """
        http_info = self._start_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def start_smart_chat_job_async_invoker(self, request):
        http_info = self._start_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "StartSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []
        if 'robot_id' in local_var_params:
            query_params.append(('robot_id', local_var_params['robot_id']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def stop_smart_chat_job_async(self, request):
        """结束数字人智能交互任务

        该接口用于结束数字人智能交互任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSmartChatJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.StopSmartChatJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StopSmartChatJobResponse`
        """
        http_info = self._stop_smart_chat_job_http_info(request)
        return self._call_api(**http_info)

    def stop_smart_chat_job_async_invoker(self, request):
        http_info = self._stop_smart_chat_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_smart_chat_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/smart-chat-rooms/{room_id}/smart-chat-jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSmartChatJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_digital_asset_async(self, request):
        """创建资产

        该接口用于在资产库中添加上传新的媒体资产。可上传的资产类型包括：分身数字人模型、背景图片、素材图片、素材视频、PPT等。
        * &gt; 资产类型是IMAGE时，通过system_properties来区分背景图片（BACKGROUND_IMG）、素材图片（MATERIAL_IMG）。
        * &gt; 资产类型是VIDEO时，通过system_properties来区分素材视频（MATERIAL_VIDEO）、名片视频（BUSSINESS_CARD_VIDEO）。
        * &gt; MetaStudio平台生成的视频，system_properties带CREATED_BY_PLATFORM。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDigitalAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalAssetResponse`
        """
        http_info = self._create_digital_asset_http_info(request)
        return self._call_api(**http_info)

    def create_digital_asset_async_invoker(self, request):
        http_info = self._create_digital_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_digital_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDigitalAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_asset_async(self, request):
        """删除资产

        该接口用于删除资产库中的媒体资产。调用该接口删除媒体资产时，媒体资产会放入回收站中，不会彻底删除。如需彻底删除资产，需增加“mode&#x3D;force”参数配置。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteAssetResponse`
        """
        http_info = self._delete_asset_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_async_invoker(self, request):
        http_info = self._delete_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_asset_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_asset_summary_async(self, request):
        """查询资产概要

        该接口用于查询媒体资产库中指定的多个资产的概要信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAssetSummary
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListAssetSummaryRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListAssetSummaryResponse`
        """
        http_info = self._list_asset_summary_http_info(request)
        return self._call_api(**http_info)

    def list_asset_summary_async_invoker(self, request):
        http_info = self._list_asset_summary_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_asset_summary_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets/summarys",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetSummaryResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def list_assets_async(self, request):
        """查询资产列表

        该接口用于查询资产库中的媒体资产列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAssets
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListAssetsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListAssetsResponse`
        """
        http_info = self._list_assets_http_info(request)
        return self._call_api(**http_info)

    def list_assets_async_invoker(self, request):
        http_info = self._list_assets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_assets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-assets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'asset_source' in local_var_params:
            query_params.append(('asset_source', local_var_params['asset_source']))
        if 'asset_state' in local_var_params:
            query_params.append(('asset_state', local_var_params['asset_state']))
        if 'style_id' in local_var_params:
            query_params.append(('style_id', local_var_params['style_id']))
        if 'render_engine' in local_var_params:
            query_params.append(('render_engine', local_var_params['render_engine']))
        if 'sex' in local_var_params:
            query_params.append(('sex', local_var_params['sex']))
        if 'language' in local_var_params:
            query_params.append(('language', local_var_params['language']))
        if 'system_property' in local_var_params:
            query_params.append(('system_property', local_var_params['system_property']))
        if 'action_editable' in local_var_params:
            query_params.append(('action_editable', local_var_params['action_editable']))
        if 'is_movable' in local_var_params:
            query_params.append(('is_movable', local_var_params['is_movable']))
        if 'voice_provider' in local_var_params:
            query_params.append(('voice_provider', local_var_params['voice_provider']))
        if 'role' in local_var_params:
            query_params.append(('role', local_var_params['role']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def restore_asset_async(self, request):
        """恢复被删除的资产

        该接口用于恢复被删除至回收站的媒体资产。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestoreAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.RestoreAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RestoreAssetResponse`
        """
        http_info = self._restore_asset_http_info(request)
        return self._call_api(**http_info)

    def restore_asset_async_invoker(self, request):
        http_info = self._restore_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restore_asset_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}/restore",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_asset_async(self, request):
        """查询资产详情

        该接口用于查询资产库中指定媒体资产的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowAssetResponse`
        """
        http_info = self._show_asset_http_info(request)
        return self._call_api(**http_info)

    def show_asset_async_invoker(self, request):
        http_info = self._show_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_asset_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_digital_asset_async(self, request):
        """更新资产

        该接口用于更新资产库中的媒体资产信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDigitalAsset
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalAssetRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalAssetResponse`
        """
        http_info = self._update_digital_asset_http_info(request)
        return self._call_api(**http_info)

    def update_digital_asset_async_invoker(self, request):
        http_info = self._update_digital_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_digital_asset_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDigitalAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_digital_human_business_card_async(self, request):
        """创建数字人名片制作

        该接口用于数字人名片制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateDigitalHumanBusinessCardResponse`
        """
        http_info = self._create_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def create_digital_human_business_card_async_invoker(self, request):
        http_info = self._create_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-business-cards",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_digital_human_business_card_async(self, request):
        """删除数字人名片制作任务

        该接口用于删除数字人名片制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteDigitalHumanBusinessCardResponse`
        """
        http_info = self._delete_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def delete_digital_human_business_card_async_invoker(self, request):
        http_info = self._delete_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-business-cards/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_digital_human_business_card_async(self, request):
        """查询数字人名片制作任务列表

        该接口用于查询数字人名片制作任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanBusinessCardResponse`
        """
        http_info = self._list_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def list_digital_human_business_card_async_invoker(self, request):
        http_info = self._list_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-business-cards",
            "request_type": request.__class__.__name__,
            "response_type": "ListDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'video_asset_name' in local_var_params:
            query_params.append(('video_asset_name', local_var_params['video_asset_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_digital_human_business_card_async(self, request):
        """查询数字人名片制作任务详情

        该接口用于查询数字人名片制作任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowDigitalHumanBusinessCardResponse`
        """
        http_info = self._show_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def show_digital_human_business_card_async_invoker(self, request):
        http_info = self._show_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-business-cards/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_digital_human_business_card_async(self, request):
        """更新数字人名片制作

        该接口用于更新数字人名片制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDigitalHumanBusinessCard
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalHumanBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateDigitalHumanBusinessCardResponse`
        """
        http_info = self._update_digital_human_business_card_http_info(request)
        return self._call_api(**http_info)

    def update_digital_human_business_card_async_invoker(self, request):
        http_info = self._update_digital_human_business_card_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_digital_human_business_card_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-business-cards/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDigitalHumanBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_digital_human_video_async(self, request):
        """查询视频制作任务列表

        该接口用于查询视频制作任务列表。可查询分身数字人视频制作列表，照片数字人视频制作列表等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListDigitalHumanVideoResponse`
        """
        http_info = self._list_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def list_digital_human_video_async_invoker(self, request):
        http_info = self._list_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_digital_human_video_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-videos",
            "request_type": request.__class__.__name__,
            "response_type": "ListDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'script_id' in local_var_params:
            query_params.append(('script_id', local_var_params['script_id']))
        if 'asset_name' in local_var_params:
            query_params.append(('asset_name', local_var_params['asset_name']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def cancel2_d_digital_human_video_async(self, request):
        """取消等待中的分身数字人视频制作任务

        该接口用于取消等待中的分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Cancel2DDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.Cancel2DDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Cancel2DDigitalHumanVideoResponse`
        """
        http_info = self._cancel2_d_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def cancel2_d_digital_human_video_async_invoker(self, request):
        http_info = self._cancel2_d_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel2_d_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/2d-digital-human-videos/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "Cancel2DDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create2_d_digital_human_video_async(self, request):
        """创建分身数字人视频制作任务

        该接口用于创建分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Create2DDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.Create2DDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Create2DDigitalHumanVideoResponse`
        """
        http_info = self._create2_d_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def create2_d_digital_human_video_async_invoker(self, request):
        http_info = self._create2_d_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create2_d_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/2d-digital-human-videos",
            "request_type": request.__class__.__name__,
            "response_type": "Create2DDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def show2_d_digital_human_video_async(self, request):
        """查询分身数字人视频制作任务详情

        该接口用于查询分身数字人视频制作任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Show2DDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.Show2DDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Show2DDigitalHumanVideoResponse`
        """
        http_info = self._show2_d_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def show2_d_digital_human_video_async_invoker(self, request):
        http_info = self._show2_d_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show2_d_digital_human_video_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/2d-digital-human-videos/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Show2DDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'show_script' in local_var_params:
            query_params.append(('show_script', local_var_params['show_script']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def cancel_photo_digital_human_video_async(self, request):
        """取消等待中的照片分身数字人视频制作任务

        该接口用于取消等待中的照片分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelPhotoDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.CancelPhotoDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CancelPhotoDigitalHumanVideoResponse`
        """
        http_info = self._cancel_photo_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def cancel_photo_digital_human_video_async_invoker(self, request):
        http_info = self._cancel_photo_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_photo_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/photo-digital-human-videos/{job_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelPhotoDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_photo_detection_async(self, request):
        """创建照片检测任务

        该接口用于创建照片检测任务，检测照片是否满足制作照片数字人的要求。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePhotoDetection
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDetectionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDetectionResponse`
        """
        http_info = self._create_photo_detection_http_info(request)
        return self._call_api(**http_info)

    def create_photo_detection_async_invoker(self, request):
        http_info = self._create_photo_detection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_photo_detection_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/photo-detection",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePhotoDetectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_photo_digital_human_video_async(self, request):
        """创建照片分身数字人视频制作任务

        该接口用于创建照片分身数字人视频制作任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePhotoDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePhotoDigitalHumanVideoResponse`
        """
        http_info = self._create_photo_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def create_photo_digital_human_video_async_invoker(self, request):
        http_info = self._create_photo_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_photo_digital_human_video_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/photo-digital-human-videos",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePhotoDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def show_photo_detection_async(self, request):
        """查询照片检测任务详情

        该接口用于查询照片检测任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPhotoDetection
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDetectionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDetectionResponse`
        """
        http_info = self._show_photo_detection_http_info(request)
        return self._call_api(**http_info)

    def show_photo_detection_async_invoker(self, request):
        http_info = self._show_photo_detection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_photo_detection_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/photo-detection/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPhotoDetectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_photo_digital_human_video_async(self, request):
        """查询照片分身数字人视频制作任务详情

        该接口用于查询照片分身数字人视频制作任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPhotoDigitalHumanVideo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDigitalHumanVideoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPhotoDigitalHumanVideoResponse`
        """
        http_info = self._show_photo_digital_human_video_http_info(request)
        return self._call_api(**http_info)

    def show_photo_digital_human_video_async_invoker(self, request):
        http_info = self._show_photo_digital_human_video_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_photo_digital_human_video_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/photo-digital-human-videos/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPhotoDigitalHumanVideoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'show_script' in local_var_params:
            query_params.append(('show_script', local_var_params['show_script']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def confirm_file_upload_async(self, request):
        """确认文件已上传

        资产文件上传完毕后，通过该接口确认上传完成。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmFileUpload
        :type request: :class:`huaweicloudsdkmetastudio.v1.ConfirmFileUploadRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ConfirmFileUploadResponse`
        """
        http_info = self._confirm_file_upload_http_info(request)
        return self._call_api(**http_info)

    def confirm_file_upload_async_invoker(self, request):
        http_info = self._confirm_file_upload_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_file_upload_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/files/{file_id}/complete",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmFileUploadResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_file_async(self, request):
        """创建文件并获取上传URL

        该接口用于创建文件并获取上传URL。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateFileResponse`
        """
        http_info = self._create_file_http_info(request)
        return self._call_api(**http_info)

    def create_file_async_invoker(self, request):
        http_info = self._create_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def delete_file_async(self, request):
        """删除文件

        该接口用于删除媒体资产库中指定的文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteFileResponse`
        """
        http_info = self._delete_file_http_info(request)
        return self._call_api(**http_info)

    def delete_file_async_invoker(self, request):
        http_info = self._delete_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_file_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/files/{file_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'file_id' in local_var_params:
            path_params['file_id'] = local_var_params['file_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_once_code_async(self, request):
        """创建一次性鉴权码

        该接口用于创建一次性鉴权码，有效期5分钟，鉴权码只能使用一次，每次使用后需要重新获取。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateOnceCode
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateOnceCodeRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateOnceCodeResponse`
        """
        http_info = self._create_once_code_http_info(request)
        return self._call_api(**http_info)

    def create_once_code_async_invoker(self, request):
        http_info = self._create_once_code_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_once_code_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/once-code",
            "request_type": request.__class__.__name__,
            "response_type": "CreateOnceCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_picture_modeling_by_url_job_async(self, request):
        """基于图片URL创建照片建模任务

        该接口用于从URL中获取图片进行照片建模任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePictureModelingByUrlJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingByUrlJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingByUrlJobResponse`
        """
        http_info = self._create_picture_modeling_by_url_job_http_info(request)
        return self._call_api(**http_info)

    def create_picture_modeling_by_url_job_async_invoker(self, request):
        http_info = self._create_picture_modeling_by_url_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_picture_modeling_by_url_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings-by-url",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePictureModelingByUrlJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_picture_modeling_job_async(self, request):
        """创建照片建模任务

        该接口用于创建风格化照片建模任务。通过上传照片，生成风格化数字人模型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePictureModelingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreatePictureModelingJobResponse`
        """
        http_info = self._create_picture_modeling_job_http_info(request)
        return self._call_api(**http_info)

    def create_picture_modeling_job_async_invoker(self, request):
        http_info = self._create_picture_modeling_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_picture_modeling_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePictureModelingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'style_id' in local_var_params:
            form_params['style_id'] = local_var_params['style_id']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'notify_url' in local_var_params:
            form_params['notify_url'] = local_var_params['notify_url']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

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

    def list_picture_modeling_jobs_async(self, request):
        """照片建模任务列表查询

        该接口用于查询风格化照片建模任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPictureModelingJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListPictureModelingJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListPictureModelingJobsResponse`
        """
        http_info = self._list_picture_modeling_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_picture_modeling_jobs_async_invoker(self, request):
        http_info = self._list_picture_modeling_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_picture_modeling_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings",
            "request_type": request.__class__.__name__,
            "response_type": "ListPictureModelingJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_picture_modeling_job_async(self, request):
        """照片建模任务详情查询

        该接口用于风格化查询照片建模任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPictureModelingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowPictureModelingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowPictureModelingJobResponse`
        """
        http_info = self._show_picture_modeling_job_http_info(request)
        return self._call_api(**http_info)

    def show_picture_modeling_job_async_invoker(self, request):
        http_info = self._show_picture_modeling_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_picture_modeling_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human/stylized/picture-modelings/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPictureModelingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_robot_async(self, request):
        """创建应用

        该接口用于创建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateRobotResponse`
        """
        http_info = self._create_robot_http_info(request)
        return self._call_api(**http_info)

    def create_robot_async_invoker(self, request):
        http_info = self._create_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_robot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_robot_async(self, request):
        """删除应用

        该接口用于删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteRobotResponse`
        """
        http_info = self._delete_robot_http_info(request)
        return self._call_api(**http_info)

    def delete_robot_async_invoker(self, request):
        http_info = self._delete_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_robot_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_robot_async(self, request):
        """查询应用列表

        该接口用于查询应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListRobotResponse`
        """
        http_info = self._list_robot_http_info(request)
        return self._call_api(**http_info)

    def list_robot_async_invoker(self, request):
        http_info = self._list_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_robot_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot",
            "request_type": request.__class__.__name__,
            "response_type": "ListRobotResponse"
            }

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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_robot_async(self, request):
        """查询应用详情

        该接口用于查询应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowRobotResponse`
        """
        http_info = self._show_robot_http_info(request)
        return self._call_api(**http_info)

    def show_robot_async_invoker(self, request):
        http_info = self._show_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_robot_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/{robot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'robot_id' in local_var_params:
            path_params['robot_id'] = local_var_params['robot_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_robot_async(self, request):
        """修改应用

        该接口用于修改应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateRobot
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateRobotResponse`
        """
        http_info = self._update_robot_http_info(request)
        return self._call_api(**http_info)

    def update_robot_async_invoker(self, request):
        http_info = self._update_robot_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_robot_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-chat/robot/{robot_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateRobotResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'robot_id' in local_var_params:
            path_params['robot_id'] = local_var_params['robot_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_smart_chat_room_async(self, request):
        """创建智能交互对话直播间

        该接口用于创建智能交互对话直播间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateSmartChatRoomResponse`
        """
        http_info = self._create_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def create_smart_chat_room_async_invoker(self, request):
        http_info = self._create_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-chat-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_smart_chat_room_async(self, request):
        """删除智能交互对话直播间

        该接口用于删除智能交互对话直播间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartChatRoomResponse`
        """
        http_info = self._delete_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def delete_smart_chat_room_async_invoker(self, request):
        http_info = self._delete_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/smart-chat-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_smart_chat_rooms_async(self, request):
        """查询智能交互对话直播间列表

        该接口用于智能交互对话直播间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartChatRooms
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartChatRoomsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartChatRoomsResponse`
        """
        http_info = self._list_smart_chat_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_smart_chat_rooms_async_invoker(self, request):
        http_info = self._list_smart_chat_rooms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_chat_rooms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-chat-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartChatRoomsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'room_name' in local_var_params:
            query_params.append(('room_name', local_var_params['room_name']))
        if 'model_name' in local_var_params:
            query_params.append(('model_name', local_var_params['model_name']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_smart_chat_room_async(self, request):
        """查询智能交互对话直播间详情

        该接口用于查询智能交互对话直播间详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartChatRoomResponse`
        """
        http_info = self._show_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def show_smart_chat_room_async_invoker(self, request):
        http_info = self._show_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-chat-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_smart_chat_room_async(self, request):
        """更新智能交互对话直播间信息

        该接口用于智能交互对话直播间信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSmartChatRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartChatRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartChatRoomResponse`
        """
        http_info = self._update_smart_chat_room_http_info(request)
        return self._call_api(**http_info)

    def update_smart_chat_room_async_invoker(self, request):
        http_info = self._update_smart_chat_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_smart_chat_room_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/smart-chat-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSmartChatRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def execute_smart_live_command_async(self, request):
        """控制数字人直播过程

        该接口用于控制数字人直播过程。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteSmartLiveCommand
        :type request: :class:`huaweicloudsdkmetastudio.v1.ExecuteSmartLiveCommandRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExecuteSmartLiveCommandResponse`
        """
        http_info = self._execute_smart_live_command_http_info(request)
        return self._call_api(**http_info)

    def execute_smart_live_command_async_invoker(self, request):
        http_info = self._execute_smart_live_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_smart_live_command_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteSmartLiveCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_smart_live_async(self, request):
        """查询数字人智能直播任务列表

        该接口用于查询数字人智能直播任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveResponse`
        """
        http_info = self._list_smart_live_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_async_invoker(self, request):
        http_info = self._list_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_smart_live_jobs_async(self, request):
        """查询数字人智能直播任务列表

        该接口用于查询数字人智能直播任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLiveJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveJobsResponse`
        """
        http_info = self._list_smart_live_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_jobs_async_invoker(self, request):
        http_info = self._list_smart_live_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'room_name' in local_var_params:
            query_params.append(('room_name', local_var_params['room_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def live_event_report_async(self, request):
        """上报直播间事件

        该接口用于上报直播间事件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for LiveEventReport
        :type request: :class:`huaweicloudsdkmetastudio.v1.LiveEventReportRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventReportResponse`
        """
        http_info = self._live_event_report_http_info(request)
        return self._call_api(**http_info)

    def live_event_report_async_invoker(self, request):
        http_info = self._live_event_report_http_info(request)
        return AsyncInvoker(self, http_info)

    def _live_event_report_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/live-event-report",
            "request_type": request.__class__.__name__,
            "response_type": "LiveEventReportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'auth_key' in local_var_params:
            query_params.append(('auth_key', local_var_params['auth_key']))
        if 'expires_time' in local_var_params:
            query_params.append(('expires_time', local_var_params['expires_time']))
        if 'refresh_url' in local_var_params:
            query_params.append(('refresh_url', local_var_params['refresh_url']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_smart_live_async(self, request):
        """查询数字人智能直播任务详情

        该接口用于查询数字人智能直播任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveResponse`
        """
        http_info = self._show_smart_live_http_info(request)
        return self._call_api(**http_info)

    def show_smart_live_async_invoker(self, request):
        http_info = self._show_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_live_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def start_smart_live_async(self, request):
        """启动数字人智能直播任务

        该接口用于启动数字人智能直播任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.StartSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StartSmartLiveResponse`
        """
        http_info = self._start_smart_live_http_info(request)
        return self._call_api(**http_info)

    def start_smart_live_async_invoker(self, request):
        http_info = self._start_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_smart_live_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "StartSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def stop_smart_live_async(self, request):
        """结束数字人智能直播任务

        该接口用于结束数字人智能直播任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopSmartLive
        :type request: :class:`huaweicloudsdkmetastudio.v1.StopSmartLiveRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StopSmartLiveResponse`
        """
        http_info = self._stop_smart_live_http_info(request)
        return self._call_api(**http_info)

    def stop_smart_live_async_invoker(self, request):
        http_info = self._stop_smart_live_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_smart_live_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}/smart-live-jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSmartLiveResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def check_text_language_async(self, request):
        """检测音色与文本的语言一致性

        检测音色与文本的语言一致性，音色与文本不一致会导致报错
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckTextLanguage
        :type request: :class:`huaweicloudsdkmetastudio.v1.CheckTextLanguageRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CheckTextLanguageResponse`
        """
        http_info = self._check_text_language_http_info(request)
        return self._call_api(**http_info)

    def check_text_language_async_invoker(self, request):
        http_info = self._check_text_language_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_text_language_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms-scripts/language-check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckTextLanguageResponse"
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

    def create_interaction_rule_group_async(self, request):
        """创建智能直播间互动规则库

        该接口用于创建智能直播间互动规则库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateInteractionRuleGroup
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateInteractionRuleGroupResponse`
        """
        http_info = self._create_interaction_rule_group_http_info(request)
        return self._call_api(**http_info)

    def create_interaction_rule_group_async_invoker(self, request):
        http_info = self._create_interaction_rule_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_interaction_rule_group_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateInteractionRuleGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_smart_live_room_async(self, request):
        """创建智能直播间

        该接口用于创建智能直播间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateSmartLiveRoomResponse`
        """
        http_info = self._create_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def create_smart_live_room_async_invoker(self, request):
        http_info = self._create_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_smart_live_room_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/smart-live-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_interaction_rule_group_async(self, request):
        """删除智能直播间互动规则库

        该接口用于删除智能直播间互动规则库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteInteractionRuleGroup
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteInteractionRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteInteractionRuleGroupResponse`
        """
        http_info = self._delete_interaction_rule_group_http_info(request)
        return self._call_api(**http_info)

    def delete_interaction_rule_group_async_invoker(self, request):
        http_info = self._delete_interaction_rule_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_interaction_rule_group_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteInteractionRuleGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_smart_live_room_async(self, request):
        """删除智能直播间

        该接口用于删除智能直播间。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteSmartLiveRoomResponse`
        """
        http_info = self._delete_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def delete_smart_live_room_async_invoker(self, request):
        http_info = self._delete_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_smart_live_room_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_interaction_rule_groups_async(self, request):
        """查询智能直播间互动规则库列表

        该接口用于智能直播间互动规则库列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListInteractionRuleGroups
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListInteractionRuleGroupsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListInteractionRuleGroupsResponse`
        """
        http_info = self._list_interaction_rule_groups_http_info(request)
        return self._call_api(**http_info)

    def list_interaction_rule_groups_async_invoker(self, request):
        http_info = self._list_interaction_rule_groups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_interaction_rule_groups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListInteractionRuleGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'group_name' in local_var_params:
            query_params.append(('group_name', local_var_params['group_name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_smart_live_rooms_async(self, request):
        """查询智能直播间列表

        该接口用于智能直播间列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSmartLiveRooms
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRoomsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListSmartLiveRoomsResponse`
        """
        http_info = self._list_smart_live_rooms_http_info(request)
        return self._call_api(**http_info)

    def list_smart_live_rooms_async_invoker(self, request):
        http_info = self._list_smart_live_rooms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_smart_live_rooms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms",
            "request_type": request.__class__.__name__,
            "response_type": "ListSmartLiveRoomsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'room_name' in local_var_params:
            query_params.append(('room_name', local_var_params['room_name']))
        if 'dh_id' in local_var_params:
            query_params.append(('dh_id', local_var_params['dh_id']))
        if 'model_name' in local_var_params:
            query_params.append(('model_name', local_var_params['model_name']))
        if 'live_state' in local_var_params:
            query_params.append(('live_state', local_var_params['live_state']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'room_type' in local_var_params:
            query_params.append(('room_type', local_var_params['room_type']))
        if 'template_own_type' in local_var_params:
            query_params.append(('template_own_type', local_var_params['template_own_type']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_smart_live_room_async(self, request):
        """查询智能直播剧本详情

        该接口用于查询智能直播剧本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowSmartLiveRoomResponse`
        """
        http_info = self._show_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def show_smart_live_room_async_invoker(self, request):
        http_info = self._show_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_smart_live_room_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_interaction_rule_group_async(self, request):
        """更新智能直播间互动规则库

        该接口用于更新智能直播间互动规则库。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateInteractionRuleGroup
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateInteractionRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateInteractionRuleGroupResponse`
        """
        http_info = self._update_interaction_rule_group_http_info(request)
        return self._call_api(**http_info)

    def update_interaction_rule_group_async_invoker(self, request):
        http_info = self._update_interaction_rule_group_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_interaction_rule_group_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/smart-live-interaction-rule-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateInteractionRuleGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_smart_live_room_async(self, request):
        """更新智能直播间信息

        该接口用于智能直播间信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSmartLiveRoom
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartLiveRoomRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateSmartLiveRoomResponse`
        """
        http_info = self._update_smart_live_room_http_info(request)
        return self._call_api(**http_info)

    def update_smart_live_room_async_invoker(self, request):
        http_info = self._update_smart_live_room_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_smart_live_room_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/smart-live-rooms/{room_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSmartLiveRoomResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'room_id' in local_var_params:
            path_params['room_id'] = local_var_params['room_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_styles_async(self, request):
        """查询数字人风格列表

        查询数字人风格列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStyles
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListStylesRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListStylesResponse`
        """
        http_info = self._list_styles_http_info(request)
        return self._call_api(**http_info)

    def list_styles_async_invoker(self, request):
        http_info = self._list_styles_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_styles_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/styles",
            "request_type": request.__class__.__name__,
            "response_type": "ListStylesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_facial_animations_async(self, request):
        """创建语音驱动表情动画任务

        该接口用于创建驱动数字人表情的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFacialAnimations
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateFacialAnimationsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateFacialAnimationsResponse`
        """
        http_info = self._create_facial_animations_http_info(request)
        return self._call_api(**http_info)

    def create_facial_animations_async_invoker(self, request):
        http_info = self._create_facial_animations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_facial_animations_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsa/fas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFacialAnimationsResponse"
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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_ttsa_async(self, request):
        """创建语音驱动任务

        该接口用于创建驱动数字人表情、动作及语音的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTtsa
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTtsaRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTtsaResponse`
        """
        http_info = self._create_ttsa_http_info(request)
        return self._call_api(**http_info)

    def create_ttsa_async_invoker(self, request):
        http_info = self._create_ttsa_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_ttsa_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsa-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTtsaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_facial_animations_data_async(self, request):
        """获取语音驱动表情数据

        该接口用于获取生成的数字人表情驱动数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFacialAnimationsData
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListFacialAnimationsDataRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListFacialAnimationsDataResponse`
        """
        http_info = self._list_facial_animations_data_http_info(request)
        return self._call_api(**http_info)

    def list_facial_animations_data_async_invoker(self, request):
        http_info = self._list_facial_animations_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_facial_animations_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/fas-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListFacialAnimationsDataResponse"
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

    def list_ttsa_data_async(self, request):
        """获取语音驱动数据

        该接口用于获取生成的数字人驱动数据，包括语音、表情、动作等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTtsaData
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTtsaDataRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTtsaDataResponse`
        """
        http_info = self._list_ttsa_data_http_info(request)
        return self._call_api(**http_info)

    def list_ttsa_data_async_invoker(self, request):
        http_info = self._list_ttsa_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ttsa_data_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsa-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTtsaDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_ttsa_jobs_async(self, request):
        """获取语音驱动任务列表

        该接口用于查询驱动数字人表情、动作及语音的任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTtsaJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListTtsaJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListTtsaJobsResponse`
        """
        http_info = self._list_ttsa_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_ttsa_jobs_async_invoker(self, request):
        http_info = self._list_ttsa_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_ttsa_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsa-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListTtsaJobsResponse"
            }

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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def commit_voice_training_job_async(self, request):
        """提交语音训练任务

        提交训练任务,执行该接口后,任务会进入审核状态,审核完成后会等待训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CommitVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CommitVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CommitVoiceTrainingJobResponse`
        """
        http_info = self._commit_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def commit_voice_training_job_async_invoker(self, request):
        http_info = self._commit_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _commit_voice_training_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CommitVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def confirm_training_segment_async(self, request):
        """确认在线录音结果

        确认在线录音结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConfirmTrainingSegment
        :type request: :class:`huaweicloudsdkmetastudio.v1.ConfirmTrainingSegmentRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ConfirmTrainingSegmentResponse`
        """
        http_info = self._confirm_training_segment_http_info(request)
        return self._call_api(**http_info)

    def confirm_training_segment_async_invoker(self, request):
        http_info = self._confirm_training_segment_http_info(request)
        return AsyncInvoker(self, http_info)

    def _confirm_training_segment_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/training-segment",
            "request_type": request.__class__.__name__,
            "response_type": "ConfirmTrainingSegmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'index' in local_var_params:
            query_params.append(('index', local_var_params['index']))

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

    def create_training_advance_job_async(self, request):
        """创建高级版语音训练任务

        用户创建语音训练基础版任务,该接口会返回一个obs上传地址，用于上传语音文件。
        仅支持zip包方式上传语音文件：
        * 语音文件打包成zip上传：上传的训练数据为一个zip格式压缩文件,其中包含一段wav格式的长音频文件。
        
        &gt; * 文件上传后，调用“提交语音训练任务”接口，启动审核和训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingAdvanceJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingAdvanceJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingAdvanceJobResponse`
        """
        http_info = self._create_training_advance_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_advance_job_async_invoker(self, request):
        http_info = self._create_training_advance_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_advance_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/advance-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingAdvanceJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_training_basic_job_async(self, request):
        """创建基础版语音训练任务

        用户创建语音训练基础版任务,该接口会返回一个obs上传地址，用于上传语音文件。
        支持2种方式上传语音文件：
        * 语音文件和文本文件打包成zip上传：语音文件已经切分成20个wav文件，每个语音文件对应一个txt文本文件，所有文件打包成zip文件。语音文件命名规则：0.wav~19.wav；文本文件命名规则：0.txt~19.txt。
        * 语音文件和文本文件逐句上传：每次上传一句语料的语音文件和文本文件，再调用“确认在线录音结果”接口确认语音和文本内容是否一致。确认成功后再上传和确认下一句。
        
        &gt; * 文件上传后，调用“提交语音训练任务”接口，启动审核和训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingBasicJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingBasicJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingBasicJobResponse`
        """
        http_info = self._create_training_basic_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_basic_job_async_invoker(self, request):
        http_info = self._create_training_basic_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_basic_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/basic-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingBasicJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_training_middle_job_async(self, request):
        """创建进阶版语音训练任务

        用户创建语音训练基础版任务,该接口会返回一个obs上传地址，用于上传语音文件。
        支持2种方式上传语音文件：
        * 语音文件和文本文件打包成zip上传：语音文件已经切分成100个wav文件，每个语音文件对应一个txt文本文件，所有文件打包成zip文件。语音文件命名规则：0.wav~99.wav；文本文件命名规则：0.txt~99.txt。
        * 语音文件和文本文件逐句上传：每次上传一句语料的语音文件和文本文件，再调用“确认在线录音结果”接口确认语音和文本内容是否一致。确认成功后再上传和确认下一句。
        
        &gt; * 文件上传后，调用“提交语音训练任务”接口，启动审核和训练。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTrainingMiddleJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingMiddleJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTrainingMiddleJobResponse`
        """
        http_info = self._create_training_middle_job_http_info(request)
        return self._call_api(**http_info)

    def create_training_middle_job_async_invoker(self, request):
        http_info = self._create_training_middle_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_training_middle_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/middle-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrainingMiddleJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def delete_voice_training_job_async(self, request):
        """删除语音训练任务

        删除语音训练任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteVoiceTrainingJobResponse`
        """
        http_info = self._delete_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def delete_voice_training_job_async_invoker(self, request):
        http_info = self._delete_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_voice_training_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def list_voice_training_job_async(self, request):
        """查询语音训练任务列表

        查询语音训练任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListVoiceTrainingJobResponse`
        """
        http_info = self._list_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def list_voice_training_job_async_invoker(self, request):
        http_info = self._list_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_voice_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'voice_name' in local_var_params:
            query_params.append(('voice_name', local_var_params['voice_name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_job_audit_result_async(self, request):
        """获取语音训练任务审核结果

        获取语音训练任务审核结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobAuditResult
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowJobAuditResultRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowJobAuditResultResponse`
        """
        http_info = self._show_job_audit_result_http_info(request)
        return self._call_api(**http_info)

    def show_job_audit_result_async_invoker(self, request):
        http_info = self._show_job_audit_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_audit_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}/audit-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobAuditResultResponse"
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

    def show_job_uploading_address_async(self, request):
        """获取语音文件上传地址

        获取语音文件上传地址
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJobUploadingAddress
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowJobUploadingAddressResponse`
        """
        http_info = self._show_job_uploading_address_http_info(request)
        return self._call_api(**http_info)

    def show_job_uploading_address_async_invoker(self, request):
        http_info = self._show_job_uploading_address_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_uploading_address_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}/uploading-address-url",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobUploadingAddressResponse"
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

    def show_training_segment_info_async(self, request):
        """获取在线录音确认结果

        获取在线录音确认结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTrainingSegmentInfo
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTrainingSegmentInfoRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTrainingSegmentInfoResponse`
        """
        http_info = self._show_training_segment_info_http_info(request)
        return self._call_api(**http_info)

    def show_training_segment_info_async_invoker(self, request):
        http_info = self._show_training_segment_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_training_segment_info_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/training-segment",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTrainingSegmentInfoResponse"
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

    def show_voice_training_job_async(self, request):
        """查询语音训练任务详情

        查询语音训练任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVoiceTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVoiceTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVoiceTrainingJobResponse`
        """
        http_info = self._show_voice_training_job_http_info(request)
        return self._call_api(**http_info)

    def show_voice_training_job_async_invoker(self, request):
        http_info = self._show_voice_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_voice_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/voice-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVoiceTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create2d_model_training_job_async(self, request):
        """创建分身数字人模型训练任务

        该接口用于创建分身数字人模型训练任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Create2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Create2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Create2dModelTrainingJobResponse`
        """
        http_info = self._create2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def create2d_model_training_job_async_invoker(self, request):
        http_info = self._create2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "Create2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def delete2d_model_training_job_async(self, request):
        """删除分身数字人模型训练任务

        该接口用于删除分身数字人模型训练任务。同时需要删除训练任务相关的训练视频、身份证照片、授权文件、模型资产等。
        &gt; * 该接口应当在任务处于以下状态时调用：WAIT_FILE_UPLOAD、AUTO_VERIFY_FAILED、MANUAL_VERIFYING、MANUAL_VERIFY_FAILED、TRAINING_DATA_PREPROCESS_FAILED、TRAIN_FAILED、INFERENCE_DATA_PREPROCESS_FAILED、JOB_SUCCESS、WAIT_USER_CONFIRM、JOB_REJECT、JOB_FINISH
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Delete2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Delete2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Delete2dModelTrainingJobResponse`
        """
        http_info = self._delete2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def delete2d_model_training_job_async_invoker(self, request):
        http_info = self._delete2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Delete2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def execute2d_model_training_command_by_user_async(self, request):
        """租户执行分身数字人模型训练任务命令

        该接口用于租户执行分身数字人模型训练任务命令，如提交训练审核等。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Execute2dModelTrainingCommandByUser
        :type request: :class:`huaweicloudsdkmetastudio.v1.Execute2dModelTrainingCommandByUserRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Execute2dModelTrainingCommandByUserResponse`
        """
        http_info = self._execute2d_model_training_command_by_user_http_info(request)
        return self._call_api(**http_info)

    def execute2d_model_training_command_by_user_async_invoker(self, request):
        http_info = self._execute2d_model_training_command_by_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute2d_model_training_command_by_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "Execute2dModelTrainingCommandByUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def list2d_model_training_job_async(self, request):
        """查询分身数字人模型训练任务列表

        该接口用于查询分身数字人模型训练任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for List2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.List2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.List2dModelTrainingJobResponse`
        """
        http_info = self._list2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def list2d_model_training_job_async_invoker(self, request):
        http_info = self._list2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "List2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'create_until' in local_var_params:
            query_params.append(('create_until', local_var_params['create_until']))
        if 'create_since' in local_var_params:
            query_params.append(('create_since', local_var_params['create_since']))
        if 'batch_name' in local_var_params:
            query_params.append(('batch_name', local_var_params['batch_name']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'job_id' in local_var_params:
            query_params.append(('job_id', local_var_params['job_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show2d_model_training_job_async(self, request):
        """查询分身数字人模型训练任务详情

        该接口用于查询分身数字人模型训练任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Show2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Show2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Show2dModelTrainingJobResponse`
        """
        http_info = self._show2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def show2d_model_training_job_async_invoker(self, request):
        http_info = self._show2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Show2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update2d_model_training_job_async(self, request):
        """更新分身数字人模型训练任务

        该接口用于更新分身数字人模型训练任务。用于在自动审核或者人工审核不通过情况下，更新训练视频、身份证照片等。
        &gt; * 该接口只能在AUTO_VERIFY_FAILED或者MANUAL_VERIFY_FAILED状态下调用
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for Update2dModelTrainingJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.Update2dModelTrainingJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.Update2dModelTrainingJobResponse`
        """
        http_info = self._update2d_model_training_job_http_info(request)
        return self._call_api(**http_info)

    def update2d_model_training_job_async_invoker(self, request):
        http_info = self._update2d_model_training_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update2d_model_training_job_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-training-manage/user/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "Update2dModelTrainingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def create_tts_audition_async(self, request):
        """创建TTS试听任务

        该接口用于创建生成播报内容的语音试听文件任务。第三方音色试听需要收费，收费标准参考：https://marketplace.huaweicloud.com/product/OFFI919400645308506112#productid&#x3D;OFFI919400645308506112
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTtsAudition
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateTtsAuditionRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateTtsAuditionResponse`
        """
        http_info = self._create_tts_audition_http_info(request)
        return self._call_api(**http_info)

    def create_tts_audition_async_invoker(self, request):
        http_info = self._create_tts_audition_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tts_audition_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/ttsc/audition",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTtsAuditionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def show_tts_audition_file_async(self, request):
        """获取TTS试听文件

        该接口用于获取TTS试听文件下载链接，返回List中包含当前已生产的试听文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTtsAuditionFile
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowTtsAuditionFileRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowTtsAuditionFileResponse`
        """
        http_info = self._show_tts_audition_file_http_info(request)
        return self._call_api(**http_info)

    def show_tts_audition_file_async_invoker(self, request):
        http_info = self._show_tts_audition_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_tts_audition_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/ttsc/audition-file/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTtsAuditionFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_request_id' in local_var_params:
            header_params['X-Request-Id'] = local_var_params['x_request_id']
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

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

    def create_video_motion_capture_job_async(self, request):
        """创建视频驱动任务

        该接口用于创建视频驱动任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoMotionCaptureJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateVideoMotionCaptureJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateVideoMotionCaptureJobResponse`
        """
        http_info = self._create_video_motion_capture_job_http_info(request)
        return self._call_api(**http_info)

    def create_video_motion_capture_job_async_invoker(self, request):
        http_info = self._create_video_motion_capture_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_video_motion_capture_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVideoMotionCaptureJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']
        if 'x_user_privilege' in local_var_params:
            header_params['X-User-Privilege'] = local_var_params['x_user_privilege']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def execute_video_motion_capture_command_async(self, request):
        """控制数字人驱动

        该接口用于控制数字人驱动。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExecuteVideoMotionCaptureCommand
        :type request: :class:`huaweicloudsdkmetastudio.v1.ExecuteVideoMotionCaptureCommandRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ExecuteVideoMotionCaptureCommandResponse`
        """
        http_info = self._execute_video_motion_capture_command_http_info(request)
        return self._call_api(**http_info)

    def execute_video_motion_capture_command_async_invoker(self, request):
        http_info = self._execute_video_motion_capture_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _execute_video_motion_capture_command_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs/{job_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteVideoMotionCaptureCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

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

    def list_video_motion_capture_jobs_async(self, request):
        """查询视频驱动任务列表

        该接口用于查询视频驱动任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVideoMotionCaptureJobs
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListVideoMotionCaptureJobsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListVideoMotionCaptureJobsResponse`
        """
        http_info = self._list_video_motion_capture_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_video_motion_capture_jobs_async_invoker(self, request):
        http_info = self._list_video_motion_capture_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_video_motion_capture_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListVideoMotionCaptureJobsResponse"
            }

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
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_video_motion_capture_job_async(self, request):
        """查询视频驱动任务详情

        该接口用于查询视频驱动任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoMotionCaptureJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVideoMotionCaptureJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVideoMotionCaptureJobResponse`
        """
        http_info = self._show_video_motion_capture_job_http_info(request)
        return self._call_api(**http_info)

    def show_video_motion_capture_job_async_invoker(self, request):
        http_info = self._show_video_motion_capture_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_video_motion_capture_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVideoMotionCaptureJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def stop_video_motion_capture_job_async(self, request):
        """停止视频驱动任务

        该接口用于停止视频驱动任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopVideoMotionCaptureJob
        :type request: :class:`huaweicloudsdkmetastudio.v1.StopVideoMotionCaptureJobRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.StopVideoMotionCaptureJobResponse`
        """
        http_info = self._stop_video_motion_capture_job_http_info(request)
        return self._call_api(**http_info)

    def stop_video_motion_capture_job_async_invoker(self, request):
        http_info = self._stop_video_motion_capture_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_video_motion_capture_job_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/video-motion-capture-jobs/{job_id}/finish",
            "request_type": request.__class__.__name__,
            "response_type": "StopVideoMotionCaptureJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def copy_video_scripts_async(self, request):
        """复制视频制作剧本

        该接口用于复制视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CopyVideoScripts
        :type request: :class:`huaweicloudsdkmetastudio.v1.CopyVideoScriptsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CopyVideoScriptsResponse`
        """
        http_info = self._copy_video_scripts_http_info(request)
        return self._call_api(**http_info)

    def copy_video_scripts_async_invoker(self, request):
        http_info = self._copy_video_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _copy_video_scripts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}/copy",
            "request_type": request.__class__.__name__,
            "response_type": "CopyVideoScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_video_scripts_async(self, request):
        """创建视频制作剧本

        该接口用于创建视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateVideoScripts
        :type request: :class:`huaweicloudsdkmetastudio.v1.CreateVideoScriptsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CreateVideoScriptsResponse`
        """
        http_info = self._create_video_scripts_http_info(request)
        return self._call_api(**http_info)

    def create_video_scripts_async_invoker(self, request):
        http_info = self._create_video_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_video_scripts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVideoScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_video_script_async(self, request):
        """删除视频制作剧本

        该接口用于删除视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteVideoScript
        :type request: :class:`huaweicloudsdkmetastudio.v1.DeleteVideoScriptRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.DeleteVideoScriptResponse`
        """
        http_info = self._delete_video_script_http_info(request)
        return self._call_api(**http_info)

    def delete_video_script_async_invoker(self, request):
        http_info = self._delete_video_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_video_script_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVideoScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_video_scripts_async(self, request):
        """查询视频制作剧本列表

        该接口用于查询视频制作剧本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVideoScripts
        :type request: :class:`huaweicloudsdkmetastudio.v1.ListVideoScriptsRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ListVideoScriptsResponse`
        """
        http_info = self._list_video_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_video_scripts_async_invoker(self, request):
        http_info = self._list_video_scripts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_video_scripts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListVideoScriptsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'script_catalog' in local_var_params:
            query_params.append(('script_catalog', local_var_params['script_catalog']))
        if 'view_mode' in local_var_params:
            query_params.append(('view_mode', local_var_params['view_mode']))

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_video_script_async(self, request):
        """查询视频制作剧本详情

        该接口用于查询视频制作剧本详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowVideoScript
        :type request: :class:`huaweicloudsdkmetastudio.v1.ShowVideoScriptRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ShowVideoScriptResponse`
        """
        http_info = self._show_video_script_http_info(request)
        return self._call_api(**http_info)

    def show_video_script_async_invoker(self, request):
        http_info = self._show_video_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_video_script_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowVideoScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_video_script_async(self, request):
        """更新视频制作剧本

        该接口用于更新视频制作剧本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateVideoScript
        :type request: :class:`huaweicloudsdkmetastudio.v1.UpdateVideoScriptRequest`
        :rtype: :class:`huaweicloudsdkmetastudio.v1.UpdateVideoScriptResponse`
        """
        http_info = self._update_video_script_http_info(request)
        return self._call_api(**http_info)

    def update_video_script_async_invoker(self, request):
        http_info = self._update_video_script_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_video_script_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/digital-human-video-scripts/{script_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVideoScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_id' in local_var_params:
            path_params['script_id'] = local_var_params['script_id']

        query_params = []

        header_params = {}
        if 'x_app_user_id' in local_var_params:
            header_params['X-App-UserId'] = local_var_params['x_app_user_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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
            kwargs["async_request"] = True
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

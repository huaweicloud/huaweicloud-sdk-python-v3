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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkoptverse'")


class OptVerseAsyncClient(Client):
    def __init__(self):
        super().__init__()
        self.model_package = importlib.import_module("huaweicloudsdkoptverse.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "OptVerseAsyncClient":
                raise TypeError("client type error, support client type is OptVerseAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def delete_model_asset_async(self, request):
        r"""删除模型资产

        删除模型资产。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteModelAsset
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteModelAssetRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteModelAssetResponse`
        """
        http_info = self._delete_model_asset_http_info(request)
        return self._call_api(**http_info)

    def delete_model_asset_async_invoker(self, request):
        http_info = self._delete_model_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_model_asset_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/asset-manager/model-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteModelAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def list_model_assets_async(self, request):
        r"""获取模型资产列表

        获取模型资产列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListModelAssets
        :type request: :class:`huaweicloudsdkoptverse.v1.ListModelAssetsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListModelAssetsResponse`
        """
        http_info = self._list_model_assets_http_info(request)
        return self._call_api(**http_info)

    def list_model_assets_async_invoker(self, request):
        http_info = self._list_model_assets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_model_assets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/asset-manager/model-assets",
            "request_type": request.__class__.__name__,
            "response_type": "ListModelAssetsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'asset_code' in local_var_params:
            query_params.append(('asset_code', local_var_params['asset_code']))
        if 'asset_source' in local_var_params:
            query_params.append(('asset_source', local_var_params['asset_source']))
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'sub_asset_type' in local_var_params:
            query_params.append(('sub_asset_type', local_var_params['sub_asset_type']))
        if 'chat_id' in local_var_params:
            query_params.append(('chat_id', local_var_params['chat_id']))
        if 'asset_actions' in local_var_params:
            query_params.append(('asset_actions', local_var_params['asset_actions']))
            collection_formats['asset_actions'] = 'csv'
        if 'asset_name' in local_var_params:
            query_params.append(('asset_name', local_var_params['asset_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_model_asset_detail_async(self, request):
        r"""查询资产详情

        查询资产详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModelAssetDetail
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowModelAssetDetailRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowModelAssetDetailResponse`
        """
        http_info = self._show_model_asset_detail_http_info(request)
        return self._call_api(**http_info)

    def show_model_asset_detail_async_invoker(self, request):
        http_info = self._show_model_asset_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_model_asset_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/asset-manager/model-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModelAssetDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def update_model_asset_async(self, request):
        r"""编辑模型资产

        编辑模型资产描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateModelAsset
        :type request: :class:`huaweicloudsdkoptverse.v1.UpdateModelAssetRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UpdateModelAssetResponse`
        """
        http_info = self._update_model_asset_http_info(request)
        return self._call_api(**http_info)

    def update_model_asset_async_invoker(self, request):
        http_info = self._update_model_asset_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_model_asset_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/asset-manager/model-assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModelAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def cancel_chat_async(self, request):
        r"""取消对话

        取消对话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelChat
        :type request: :class:`huaweicloudsdkoptverse.v1.CancelChatRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CancelChatResponse`
        """
        http_info = self._cancel_chat_http_info(request)
        return self._call_api(**http_info)

    def cancel_chat_async_invoker(self, request):
        http_info = self._cancel_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_chat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/cancel",
            "request_type": request.__class__.__name__,
            "response_type": "CancelChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

        query_params = []

        header_params = {}
        if 'x_chat_route_id' in local_var_params:
            header_params['X-Chat-Route-Id'] = local_var_params['x_chat_route_id']

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

    def create_artifacts_async(self, request):
        r"""产物中心

        创建产物中心产物。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateArtifacts
        :type request: :class:`huaweicloudsdkoptverse.v1.CreateArtifactsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CreateArtifactsResponse`
        """
        http_info = self._create_artifacts_http_info(request)
        return self._call_api(**http_info)

    def create_artifacts_async_invoker(self, request):
        http_info = self._create_artifacts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_artifacts_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/artifacts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateArtifactsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

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

    def delete_chat_async(self, request):
        r"""删除对话

        删除对话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteChat
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteChatRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteChatResponse`
        """
        http_info = self._delete_chat_http_info(request)
        return self._call_api(**http_info)

    def delete_chat_async_invoker(self, request):
        http_info = self._delete_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_chat_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/chats/{chat_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

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

    def download_file_async(self, request):
        r"""下载文件

        下载文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DownloadFile
        :type request: :class:`huaweicloudsdkoptverse.v1.DownloadFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DownloadFileResponse`
        """
        http_info = self._download_file_http_info(request)
        return self._call_api(**http_info)

    def download_file_async_invoker(self, request):
        http_info = self._download_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _download_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/file/{filename}/download",
            "request_type": request.__class__.__name__,
            "response_type": "DownloadFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']
        if 'filename' in local_var_params:
            path_params['filename'] = local_var_params['filename']

        query_params = []

        header_params = {}
        if 'x_need_content' in local_var_params:
            header_params['X-Need-Content'] = local_var_params['x_need_content']

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

    def list_artifacts_async(self, request):
        r"""获取产物中心列表

        获取产物中心列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListArtifacts
        :type request: :class:`huaweicloudsdkoptverse.v1.ListArtifactsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListArtifactsResponse`
        """
        http_info = self._list_artifacts_http_info(request)
        return self._call_api(**http_info)

    def list_artifacts_async_invoker(self, request):
        http_info = self._list_artifacts_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_artifacts_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/artifacts",
            "request_type": request.__class__.__name__,
            "response_type": "ListArtifactsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

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

    def list_chat_async(self, request):
        r"""获取对话列表

        获取对话列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListChat
        :type request: :class:`huaweicloudsdkoptverse.v1.ListChatRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListChatResponse`
        """
        http_info = self._list_chat_http_info(request)
        return self._call_api(**http_info)

    def list_chat_async_invoker(self, request):
        http_info = self._list_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_chat_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/chats",
            "request_type": request.__class__.__name__,
            "response_type": "ListChatResponse"
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
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'title' in local_var_params:
            query_params.append(('title', local_var_params['title']))
        if 'agent_type' in local_var_params:
            query_params.append(('agent_type', local_var_params['agent_type']))

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

    def publish_chat_async(self, request):
        r"""发布助手

        发布助手。
        发布前会校验当前助手最后一个阶段的文档是否已确认，确认后才可发布。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishChat
        :type request: :class:`huaweicloudsdkoptverse.v1.PublishChatRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.PublishChatResponse`
        """
        http_info = self._publish_chat_http_info(request)
        return self._call_api(**http_info)

    def publish_chat_async_invoker(self, request):
        http_info = self._publish_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_chat_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/chats/{chat_id}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

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

    def show_chat_async(self, request):
        r"""获取对话详情

        获取对话详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowChat
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowChatRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowChatResponse`
        """
        http_info = self._show_chat_http_info(request)
        return self._call_api(**http_info)

    def show_chat_async_invoker(self, request):
        http_info = self._show_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_chat_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/chats/{chat_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Chat-Route-Id", ]

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

    def update_chat_async(self, request):
        r"""更新对话

        更新对话。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateChat
        :type request: :class:`huaweicloudsdkoptverse.v1.UpdateChatRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UpdateChatResponse`
        """
        http_info = self._update_chat_http_info(request)
        return self._call_api(**http_info)

    def update_chat_async_invoker(self, request):
        http_info = self._update_chat_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_chat_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/chats/{chat_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateChatResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'chat_id' in local_var_params:
            path_params['chat_id'] = local_var_params['chat_id']

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

    def upload_file_async(self, request):
        r"""上传文件

        上传文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadFile
        :type request: :class:`huaweicloudsdkoptverse.v1.UploadFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UploadFileResponse`
        """
        http_info = self._upload_file_http_info(request)
        return self._call_api(**http_info)

    def upload_file_async_invoker(self, request):
        http_info = self._upload_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/chats/file/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_chat_route_id' in local_var_params:
            header_params['X-Chat-Route-Id'] = local_var_params['x_chat_route_id']

        form_params = {}
        if 'chat_id' in local_var_params:
            form_params['chat_id'] = local_var_params['chat_id']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'agent_type' in local_var_params:
            form_params['agent_type'] = local_var_params['agent_type']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_model_service_async(self, request):
        r"""创建模型服务

        创建模型服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateModelService
        :type request: :class:`huaweicloudsdkoptverse.v1.CreateModelServiceRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CreateModelServiceResponse`
        """
        http_info = self._create_model_service_http_info(request)
        return self._call_api(**http_info)

    def create_model_service_async_invoker(self, request):
        http_info = self._create_model_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_model_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-service/services",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModelServiceResponse"
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

    def create_model_service_task_async(self, request):
        r"""调用模型服务创建任务

        调用模型服务创建任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateModelServiceTask
        :type request: :class:`huaweicloudsdkoptverse.v1.CreateModelServiceTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CreateModelServiceTaskResponse`
        """
        http_info = self._create_model_service_task_http_info(request)
        return self._call_api(**http_info)

    def create_model_service_task_async_invoker(self, request):
        http_info = self._create_model_service_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_model_service_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateModelServiceTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def delete_model_service_async(self, request):
        r"""删除模型服务

        删除模型服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteModelService
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteModelServiceRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteModelServiceResponse`
        """
        http_info = self._delete_model_service_http_info(request)
        return self._call_api(**http_info)

    def delete_model_service_async_invoker(self, request):
        http_info = self._delete_model_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_model_service_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteModelServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def list_model_service_tasks_async(self, request):
        r"""获取模型服务任务列表

        获取模型服务任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListModelServiceTasks
        :type request: :class:`huaweicloudsdkoptverse.v1.ListModelServiceTasksRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListModelServiceTasksResponse`
        """
        http_info = self._list_model_service_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_model_service_tasks_async_invoker(self, request):
        http_info = self._list_model_service_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_model_service_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListModelServiceTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def show_model_service_detail_async(self, request):
        r"""获取模型服务详情

        获取模型服务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModelServiceDetail
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowModelServiceDetailRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowModelServiceDetailResponse`
        """
        http_info = self._show_model_service_detail_http_info(request)
        return self._call_api(**http_info)

    def show_model_service_detail_async_invoker(self, request):
        http_info = self._show_model_service_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_model_service_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModelServiceDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def show_model_service_list_async(self, request):
        r"""获取模型服务列表

        获取模型服务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModelServiceList
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowModelServiceListRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowModelServiceListResponse`
        """
        http_info = self._show_model_service_list_http_info(request)
        return self._call_api(**http_info)

    def show_model_service_list_async_invoker(self, request):
        http_info = self._show_model_service_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_model_service_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/model-service/services",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModelServiceListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'infer_type' in local_var_params:
            query_params.append(('infer_type', local_var_params['infer_type']))
        if 'asset_id' in local_var_params:
            query_params.append(('asset_id', local_var_params['asset_id']))
        if 'asset_type' in local_var_params:
            query_params.append(('asset_type', local_var_params['asset_type']))
        if 'asset_sub_type' in local_var_params:
            query_params.append(('asset_sub_type', local_var_params['asset_sub_type']))
        if 'chip_type' in local_var_params:
            query_params.append(('chip_type', local_var_params['chip_type']))
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'use_type' in local_var_params:
            query_params.append(('use_type', local_var_params['use_type']))
        if 'model_name' in local_var_params:
            query_params.append(('model_name', local_var_params['model_name']))
        if 'service_name' in local_var_params:
            query_params.append(('service_name', local_var_params['service_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_model_service_task_async(self, request):
        r"""获取模型服务任务详情

        获取模型服务任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowModelServiceTask
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowModelServiceTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowModelServiceTaskResponse`
        """
        http_info = self._show_model_service_task_http_info(request)
        return self._call_api(**http_info)

    def show_model_service_task_async_invoker(self, request):
        http_info = self._show_model_service_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_model_service_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowModelServiceTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']
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

    def start_model_service_async(self, request):
        r"""启动模型服务

        启动模型服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartModelService
        :type request: :class:`huaweicloudsdkoptverse.v1.StartModelServiceRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.StartModelServiceResponse`
        """
        http_info = self._start_model_service_http_info(request)
        return self._call_api(**http_info)

    def start_model_service_async_invoker(self, request):
        http_info = self._start_model_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_model_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartModelServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def stop_model_service_async(self, request):
        r"""停止模型服务

        停止模型服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopModelService
        :type request: :class:`huaweicloudsdkoptverse.v1.StopModelServiceRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.StopModelServiceResponse`
        """
        http_info = self._stop_model_service_http_info(request)
        return self._call_api(**http_info)

    def stop_model_service_async_invoker(self, request):
        http_info = self._stop_model_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_model_service_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopModelServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def update_model_service_async(self, request):
        r"""编辑推理服务

        编辑推理服务，仅支持修改服务名称和服务描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateModelService
        :type request: :class:`huaweicloudsdkoptverse.v1.UpdateModelServiceRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UpdateModelServiceResponse`
        """
        http_info = self._update_model_service_http_info(request)
        return self._call_api(**http_info)

    def update_model_service_async_invoker(self, request):
        http_info = self._update_model_service_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_model_service_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateModelServiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

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

    def upload_model_service_task_file_async(self, request):
        r"""上传任务依赖的输入文件

        上传任务依赖的输入文件。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadModelServiceTaskFile
        :type request: :class:`huaweicloudsdkoptverse.v1.UploadModelServiceTaskFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UploadModelServiceTaskFileResponse`
        """
        http_info = self._upload_model_service_task_file_http_info(request)
        return self._call_api(**http_info)

    def upload_model_service_task_file_async_invoker(self, request):
        http_info = self._upload_model_service_task_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_model_service_task_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-service/services/{service_id}/files/upload",
            "request_type": request.__class__.__name__,
            "response_type": "UploadModelServiceTaskFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_id' in local_var_params:
            path_params['service_id'] = local_var_params['service_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def publish_model_async(self, request):
        r"""发布模型

        发布训练任务生成的模型。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishModel
        :type request: :class:`huaweicloudsdkoptverse.v1.PublishModelRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.PublishModelResponse`
        """
        http_info = self._publish_model_http_info(request)
        return self._call_api(**http_info)

    def publish_model_async_invoker(self, request):
        http_info = self._publish_model_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_model_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/model-train/model/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishModelResponse"
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

    def batch_delete_evolve_task_async(self, request):
        r"""删除算法演化任务

        删除算法演化任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteEvolveTask
        :type request: :class:`huaweicloudsdkoptverse.v1.BatchDeleteEvolveTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.BatchDeleteEvolveTaskResponse`
        """
        http_info = self._batch_delete_evolve_task_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_evolve_task_async_invoker(self, request):
        http_info = self._batch_delete_evolve_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_evolve_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/batch-delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteEvolveTaskResponse"
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

    def create_algorithm_async(self, request):
        r"""创建设计项目

        创建设计项目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAlgorithm
        :type request: :class:`huaweicloudsdkoptverse.v1.CreateAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CreateAlgorithmResponse`
        """
        http_info = self._create_algorithm_http_info(request)
        return self._call_api(**http_info)

    def create_algorithm_async_invoker(self, request):
        http_info = self._create_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_algorithm_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAlgorithmResponse"
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

    def create_evolve_task_async(self, request):
        r"""创建演化任务

        创建演化任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEvolveTask
        :type request: :class:`huaweicloudsdkoptverse.v1.CreateEvolveTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CreateEvolveTaskResponse`
        """
        http_info = self._create_evolve_task_http_info(request)
        return self._call_api(**http_info)

    def create_evolve_task_async_invoker(self, request):
        http_info = self._create_evolve_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_evolve_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEvolveTaskResponse"
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

    def delete_algorithm_async(self, request):
        r"""删除算法设计项目

        删除算法设计项目
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlgorithm
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteAlgorithmResponse`
        """
        http_info = self._delete_algorithm_http_info(request)
        return self._call_api(**http_info)

    def delete_algorithm_async_invoker(self, request):
        http_info = self._delete_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_algorithm_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlgorithmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

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

    def delete_algorithm_file_async(self, request):
        r"""删除算法设计项目中的文件

        删除算法设计项目中的文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAlgorithmFile
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteAlgorithmFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteAlgorithmFileResponse`
        """
        http_info = self._delete_algorithm_file_http_info(request)
        return self._call_api(**http_info)

    def delete_algorithm_file_async_invoker(self, request):
        http_info = self._delete_algorithm_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_algorithm_file_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}/editor/files",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAlgorithmFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))

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

    def delete_evolve_task_async(self, request):
        r"""删除算法演化任务

        删除算法演化任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEvolveTask
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteEvolveTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteEvolveTaskResponse`
        """
        http_info = self._delete_evolve_task_http_info(request)
        return self._call_api(**http_info)

    def delete_evolve_task_async_invoker(self, request):
        http_info = self._delete_evolve_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_evolve_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEvolveTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

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

    def import_algorithm_file_async(self, request):
        r"""保存算法文件

        保存算法文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportAlgorithmFile
        :type request: :class:`huaweicloudsdkoptverse.v1.ImportAlgorithmFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ImportAlgorithmFileResponse`
        """
        http_info = self._import_algorithm_file_http_info(request)
        return self._call_api(**http_info)

    def import_algorithm_file_async_invoker(self, request):
        http_info = self._import_algorithm_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_algorithm_file_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}/editor/init",
            "request_type": request.__class__.__name__,
            "response_type": "ImportAlgorithmFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'last_update_time' in local_var_params:
            form_params['last_update_time'] = local_var_params['last_update_time']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def list_algorithms_async(self, request):
        r"""批量查询设计项目列表

        批量查询设计项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAlgorithms
        :type request: :class:`huaweicloudsdkoptverse.v1.ListAlgorithmsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListAlgorithmsResponse`
        """
        http_info = self._list_algorithms_http_info(request)
        return self._call_api(**http_info)

    def list_algorithms_async_invoker(self, request):
        http_info = self._list_algorithms_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_algorithms_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms",
            "request_type": request.__class__.__name__,
            "response_type": "ListAlgorithmsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'lang' in local_var_params:
            query_params.append(('lang', local_var_params['lang']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'user_id' in local_var_params:
            query_params.append(('user_id', local_var_params['user_id']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'create_time_start' in local_var_params:
            query_params.append(('create_time_start', local_var_params['create_time_start']))
        if 'create_time_end' in local_var_params:
            query_params.append(('create_time_end', local_var_params['create_time_end']))

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

    def list_directory_by_algorithm_id_async(self, request):
        r"""获取某一算法设计项目文件目录

        获取某一算法设计项目文件目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDirectoryByAlgorithmId
        :type request: :class:`huaweicloudsdkoptverse.v1.ListDirectoryByAlgorithmIdRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListDirectoryByAlgorithmIdResponse`
        """
        http_info = self._list_directory_by_algorithm_id_http_info(request)
        return self._call_api(**http_info)

    def list_directory_by_algorithm_id_async_invoker(self, request):
        http_info = self._list_directory_by_algorithm_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_directory_by_algorithm_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}/editor/root",
            "request_type": request.__class__.__name__,
            "response_type": "ListDirectoryByAlgorithmIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

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

    def list_directory_by_result_commit_id_async(self, request):
        r"""获取某一演化任务某次结果的commit的目录

        获取某一演化任务某次结果的commit的目录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDirectoryByResultCommitId
        :type request: :class:`huaweicloudsdkoptverse.v1.ListDirectoryByResultCommitIdRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListDirectoryByResultCommitIdResponse`
        """
        http_info = self._list_directory_by_result_commit_id_http_info(request)
        return self._call_api(**http_info)

    def list_directory_by_result_commit_id_async_invoker(self, request):
        http_info = self._list_directory_by_result_commit_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_directory_by_result_commit_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/result/{commit_id}/root",
            "request_type": request.__class__.__name__,
            "response_type": "ListDirectoryByResultCommitIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']
        if 'commit_id' in local_var_params:
            path_params['commit_id'] = local_var_params['commit_id']

        query_params = []
        if 'iteration' in local_var_params:
            query_params.append(('iteration', local_var_params['iteration']))

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

    def list_evolve_task_metas_async(self, request):
        r"""批量查询演化项目列表

        批量查询演化项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvolveTaskMetas
        :type request: :class:`huaweicloudsdkoptverse.v1.ListEvolveTaskMetasRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListEvolveTaskMetasResponse`
        """
        http_info = self._list_evolve_task_metas_http_info(request)
        return self._call_api(**http_info)

    def list_evolve_task_metas_async_invoker(self, request):
        http_info = self._list_evolve_task_metas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_evolve_task_metas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListEvolveTaskMetasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'algorithm_id' in local_var_params:
            query_params.append(('algorithm_id', local_var_params['algorithm_id']))
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_evolve_task_stats_async(self, request):
        r"""查询演化任务状态统计

        查询演化任务状态统计
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEvolveTaskStats
        :type request: :class:`huaweicloudsdkoptverse.v1.ListEvolveTaskStatsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListEvolveTaskStatsResponse`
        """
        http_info = self._list_evolve_task_stats_http_info(request)
        return self._call_api(**http_info)

    def list_evolve_task_stats_async_invoker(self, request):
        http_info = self._list_evolve_task_stats_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_evolve_task_stats_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/stats",
            "request_type": request.__class__.__name__,
            "response_type": "ListEvolveTaskStatsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'algorithm_id' in local_var_params:
            query_params.append(('algorithm_id', local_var_params['algorithm_id']))

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

    def save_algorithm_file_async(self, request):
        r"""保存算法文件

        保存算法文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SaveAlgorithmFile
        :type request: :class:`huaweicloudsdkoptverse.v1.SaveAlgorithmFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.SaveAlgorithmFileResponse`
        """
        http_info = self._save_algorithm_file_http_info(request)
        return self._call_api(**http_info)

    def save_algorithm_file_async_invoker(self, request):
        http_info = self._save_algorithm_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _save_algorithm_file_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}/editor/files",
            "request_type": request.__class__.__name__,
            "response_type": "SaveAlgorithmFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file_path' in local_var_params:
            form_params['file_path'] = local_var_params['file_path']
        if 'last_update_time' in local_var_params:
            form_params['last_update_time'] = local_var_params['last_update_time']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_algorithm_async(self, request):
        r"""获取某一算法信息详情

        获取某一算法信息详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlgorithm
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowAlgorithmResponse`
        """
        http_info = self._show_algorithm_http_info(request)
        return self._call_api(**http_info)

    def show_algorithm_async_invoker(self, request):
        http_info = self._show_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_algorithm_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlgorithmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

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

    def show_algorithm_file_async(self, request):
        r"""获取某一算法设计项目某一文件中的内容

        获取某一算法设计项目某一文件中的内容
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAlgorithmFile
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowAlgorithmFileRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowAlgorithmFileResponse`
        """
        http_info = self._show_algorithm_file_http_info(request)
        return self._call_api(**http_info)

    def show_algorithm_file_async_invoker(self, request):
        http_info = self._show_algorithm_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_algorithm_file_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}/editor/files",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAlgorithmFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

        query_params = []
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))

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

    def show_task_details_async(self, request):
        r"""获取某一演化任务详情

        获取某一演化任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskDetails
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowTaskDetailsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowTaskDetailsResponse`
        """
        http_info = self._show_task_details_http_info(request)
        return self._call_api(**http_info)

    def show_task_details_async_invoker(self, request):
        http_info = self._show_task_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

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

    def show_task_result_commit_async(self, request):
        r"""获取某一演化任务某次结果的commit文件

        获取某一演化任务某次结果的commit文件
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskResultCommit
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowTaskResultCommitRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowTaskResultCommitResponse`
        """
        http_info = self._show_task_result_commit_http_info(request)
        return self._call_api(**http_info)

    def show_task_result_commit_async_invoker(self, request):
        http_info = self._show_task_result_commit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_result_commit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/result/{commit_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResultCommitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']
        if 'commit_id' in local_var_params:
            path_params['commit_id'] = local_var_params['commit_id']

        query_params = []
        if 'iteration' in local_var_params:
            query_params.append(('iteration', local_var_params['iteration']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'file_path' in local_var_params:
            query_params.append(('file_path', local_var_params['file_path']))

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

    def show_task_result_list_async(self, request):
        r"""获取某一演化任务运行详结果列表

        获取某一演化任务运行详结果列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskResultList
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowTaskResultListRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowTaskResultListResponse`
        """
        http_info = self._show_task_result_list_http_info(request)
        return self._call_api(**http_info)

    def show_task_result_list_async_invoker(self, request):
        http_info = self._show_task_result_list_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_result_list_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResultListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

        query_params = []
        if 'iteration' in local_var_params:
            query_params.append(('iteration', local_var_params['iteration']))

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

    def show_task_running_details_async(self, request):
        r"""获取某一演化任务运行详情

        获取某一演化任务运行详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskRunningDetails
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowTaskRunningDetailsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowTaskRunningDetailsResponse`
        """
        http_info = self._show_task_running_details_http_info(request)
        return self._call_api(**http_info)

    def show_task_running_details_async_invoker(self, request):
        http_info = self._show_task_running_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_running_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/stats",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskRunningDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

        query_params = []
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

    def show_task_running_log_async(self, request):
        r"""获取某一演化任务运行日志

        获取某一演化任务运行日志
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTaskRunningLog
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowTaskRunningLogRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowTaskRunningLogResponse`
        """
        http_info = self._show_task_running_log_http_info(request)
        return self._call_api(**http_info)

    def show_task_running_log_async_invoker(self, request):
        http_info = self._show_task_running_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_running_log_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskRunningLogResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

        query_params = []
        if 'start_byte' in local_var_params:
            query_params.append(('start_byte', local_var_params['start_byte']))
        if 'end_byte' in local_var_params:
            query_params.append(('end_byte', local_var_params['end_byte']))

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

    def start_evolve_task_async(self, request):
        r"""启动演化任务

        启动演化任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartEvolveTask
        :type request: :class:`huaweicloudsdkoptverse.v1.StartEvolveTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.StartEvolveTaskResponse`
        """
        http_info = self._start_evolve_task_http_info(request)
        return self._call_api(**http_info)

    def start_evolve_task_async_invoker(self, request):
        http_info = self._start_evolve_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_evolve_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartEvolveTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

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

    def stop_evolve_task_async(self, request):
        r"""停止演化任务

        停止演化任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopEvolveTask
        :type request: :class:`huaweicloudsdkoptverse.v1.StopEvolveTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.StopEvolveTaskResponse`
        """
        http_info = self._stop_evolve_task_http_info(request)
        return self._call_api(**http_info)

    def stop_evolve_task_async_invoker(self, request):
        http_info = self._stop_evolve_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_evolve_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopEvolveTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

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

    def update_algorithm_async(self, request):
        r"""更新算法设计项目信息

        更新算法设计项目信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAlgorithm
        :type request: :class:`huaweicloudsdkoptverse.v1.UpdateAlgorithmRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UpdateAlgorithmResponse`
        """
        http_info = self._update_algorithm_http_info(request)
        return self._call_api(**http_info)

    def update_algorithm_async_invoker(self, request):
        http_info = self._update_algorithm_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_algorithm_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/llm4ad/algorithms/{algorithm_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAlgorithmResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'algorithm_id' in local_var_params:
            path_params['algorithm_id'] = local_var_params['algorithm_id']

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

    def update_evolve_task_async(self, request):
        r"""更新算法演化任务信息

        更新算法演化任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEvolveTask
        :type request: :class:`huaweicloudsdkoptverse.v1.UpdateEvolveTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.UpdateEvolveTaskResponse`
        """
        http_info = self._update_evolve_task_http_info(request)
        return self._call_api(**http_info)

    def update_evolve_task_async_invoker(self, request):
        http_info = self._update_evolve_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_evolve_task_http_info(self, request):
        http_info = {
            "method": "PATCH",
            "resource_path": "/v1/{project_id}/llm4ad/evolve-tasks/{evolve_task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEvolveTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'evolve_task_id' in local_var_params:
            path_params['evolve_task_id'] = local_var_params['evolve_task_id']

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

    def authorize_permission_async(self, request):
        r"""授权

        授予LLM4AD操作用户桶的权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AuthorizePermission
        :type request: :class:`huaweicloudsdkoptverse.v1.AuthorizePermissionRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.AuthorizePermissionResponse`
        """
        http_info = self._authorize_permission_http_info(request)
        return self._call_api(**http_info)

    def authorize_permission_async_invoker(self, request):
        http_info = self._authorize_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _authorize_permission_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/llm4ad/obs/permission/{bucket}",
            "request_type": request.__class__.__name__,
            "response_type": "AuthorizePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket' in local_var_params:
            path_params['bucket'] = local_var_params['bucket']

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

    def list_buckets_async(self, request):
        r"""获取Bucket清单

        获取Bucket清单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuckets
        :type request: :class:`huaweicloudsdkoptverse.v1.ListBucketsRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListBucketsResponse`
        """
        http_info = self._list_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_buckets_async_invoker(self, request):
        http_info = self._list_buckets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_buckets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/obs/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListBucketsResponse"
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

    def list_object_async(self, request):
        r"""获取Object清单

        获取Object清单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObject
        :type request: :class:`huaweicloudsdkoptverse.v1.ListObjectRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListObjectResponse`
        """
        http_info = self._list_object_http_info(request)
        return self._call_api(**http_info)

    def list_object_async_invoker(self, request):
        http_info = self._list_object_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_object_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/obs/objects",
            "request_type": request.__class__.__name__,
            "response_type": "ListObjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bucket' in local_var_params:
            query_params.append(('bucket', local_var_params['bucket']))
        if 'key' in local_var_params:
            query_params.append(('key', local_var_params['key']))

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

    def list_permission_async(self, request):
        r"""检查桶的权限

        检查桶的权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPermission
        :type request: :class:`huaweicloudsdkoptverse.v1.ListPermissionRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListPermissionResponse`
        """
        http_info = self._list_permission_http_info(request)
        return self._call_api(**http_info)

    def list_permission_async_invoker(self, request):
        http_info = self._list_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_permission_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/llm4ad/obs/permission/{bucket}",
            "request_type": request.__class__.__name__,
            "response_type": "ListPermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket' in local_var_params:
            path_params['bucket'] = local_var_params['bucket']

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

    def revoke_permission_async(self, request):
        r"""取消授权

        取消LLM4AD对用户桶的权限
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RevokePermission
        :type request: :class:`huaweicloudsdkoptverse.v1.RevokePermissionRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.RevokePermissionResponse`
        """
        http_info = self._revoke_permission_http_info(request)
        return self._call_api(**http_info)

    def revoke_permission_async_invoker(self, request):
        http_info = self._revoke_permission_http_info(request)
        return AsyncInvoker(self, http_info)

    def _revoke_permission_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/llm4ad/obs/permission/{bucket}",
            "request_type": request.__class__.__name__,
            "response_type": "RevokePermissionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket' in local_var_params:
            path_params['bucket'] = local_var_params['bucket']

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

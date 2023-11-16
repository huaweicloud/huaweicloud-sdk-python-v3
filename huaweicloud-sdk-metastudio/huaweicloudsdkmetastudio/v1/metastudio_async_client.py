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

    def create_digital_asset_async(self, request):
        """创建资产

        该接口用于在资产库中添加上传新的媒体资产。可上传的资产类型包括：数字人模型、素材、视频、图片、场景等。
        
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

        该接口用于删除资产库中的媒体资产。第一次调用删除接口，将指定资产放入回收站；第二次调用删除接口，将指定资产彻底删除。
        
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
            ['application/json'])

        auth_settings = []

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
            ['application/json'])

        auth_settings = []

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
            ['application/json'])

        auth_settings = []

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
            ['application/json'])

        auth_settings = []

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
            ['application/json'])

        auth_settings = []

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
            ['application/json'])

        auth_settings = []

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

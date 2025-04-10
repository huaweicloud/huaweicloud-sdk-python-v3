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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkiotanalytics'")


class IoTAnalyticsClient(Client):
    def __init__(self):
        super(IoTAnalyticsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotanalytics.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IoTAnalyticsClient":
                raise TypeError("client type error, support client type is IoTAnalyticsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_asset_model(self, request):
        r"""创建资产模型

        创建资产模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetModel
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateAssetModelRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateAssetModelResponse`
        """
        http_info = self._create_asset_model_http_info(request)
        return self._call_api(**http_info)

    def create_asset_model_invoker(self, request):
        http_info = self._create_asset_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_model_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/asset-models",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetModelResponse"
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

    def delete_asset_model(self, request):
        r"""删除资产模型

        删除资产模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssetModel
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteAssetModelRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteAssetModelResponse`
        """
        http_info = self._delete_asset_model_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_model_invoker(self, request):
        http_info = self._delete_asset_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_asset_model_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/asset-models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def list_asset_models(self, request):
        r"""获取资产模型列表

        获取资产模型列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssetModels
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListAssetModelsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListAssetModelsResponse`
        """
        http_info = self._list_asset_models_http_info(request)
        return self._call_api(**http_info)

    def list_asset_models_invoker(self, request):
        http_info = self._list_asset_models_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_asset_models_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/asset-models",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetModelsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
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

    def show_asset_model(self, request):
        r"""获取资产模型详情

        获取资产模型详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetModel
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowAssetModelRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowAssetModelResponse`
        """
        http_info = self._show_asset_model_http_info(request)
        return self._call_api(**http_info)

    def show_asset_model_invoker(self, request):
        http_info = self._show_asset_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_model_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/asset-models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def update_asset_model(self, request):
        r"""修改资产模型

        修改资产模型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssetModel
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateAssetModelRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateAssetModelResponse`
        """
        http_info = self._update_asset_model_http_info(request)
        return self._call_api(**http_info)

    def update_asset_model_invoker(self, request):
        http_info = self._update_asset_model_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_asset_model_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/asset-models/{model_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetModelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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

    def create_asset_new(self, request):
        r"""创建资产

        创建资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAssetNew
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateAssetNewRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateAssetNewResponse`
        """
        http_info = self._create_asset_new_http_info(request)
        return self._call_api(**http_info)

    def create_asset_new_invoker(self, request):
        http_info = self._create_asset_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_asset_new_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAssetNewResponse"
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

    def delete_asset_new(self, request):
        r"""删除资产

        删除资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssetNew
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteAssetNewRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteAssetNewResponse`
        """
        http_info = self._delete_asset_new_http_info(request)
        return self._call_api(**http_info)

    def delete_asset_new_invoker(self, request):
        http_info = self._delete_asset_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_asset_new_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAssetNewResponse"
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

    def list_assets_new(self, request):
        r"""获取资产列表

        获取资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAssetsNew
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListAssetsNewRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListAssetsNewResponse`
        """
        http_info = self._list_assets_new_http_info(request)
        return self._call_api(**http_info)

    def list_assets_new_invoker(self, request):
        http_info = self._list_assets_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_assets_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets",
            "request_type": request.__class__.__name__,
            "response_type": "ListAssetsNewResponse"
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
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
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

    def publish_root_asset(self, request):
        r"""发布资产

        发布资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishRootAsset
        :type request: :class:`huaweicloudsdkiotanalytics.v1.PublishRootAssetRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.PublishRootAssetResponse`
        """
        http_info = self._publish_root_asset_http_info(request)
        return self._call_api(**http_info)

    def publish_root_asset_invoker(self, request):
        http_info = self._publish_root_asset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _publish_root_asset_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets/{root_asset_id}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishRootAssetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'root_asset_id' in local_var_params:
            path_params['root_asset_id'] = local_var_params['root_asset_id']

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

    def show_asset_new(self, request):
        r"""获取资产详情

        获取资产详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetNew
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowAssetNewRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowAssetNewResponse`
        """
        http_info = self._show_asset_new_http_info(request)
        return self._call_api(**http_info)

    def show_asset_new_invoker(self, request):
        http_info = self._show_asset_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_asset_new_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAssetNewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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

    def update_asset_new(self, request):
        r"""修改资产

        修改资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssetNew
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateAssetNewRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateAssetNewResponse`
        """
        http_info = self._update_asset_new_http_info(request)
        return self._call_api(**http_info)

    def update_asset_new_invoker(self, request):
        http_info = self._update_asset_new_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_asset_new_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/assets/{asset_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetNewResponse"
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

    def show_last_property_value(self, request):
        r"""获取资产属性最新值

        获取资产属性最新值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLastPropertyValue
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowLastPropertyValueRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowLastPropertyValueResponse`
        """
        http_info = self._show_last_property_value_http_info(request)
        return self._call_api(**http_info)

    def show_last_property_value_invoker(self, request):
        http_info = self._show_last_property_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_last_property_value_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/property-values/query-last",
            "request_type": request.__class__.__name__,
            "response_type": "ShowLastPropertyValueResponse"
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

    def show_metric_value(self, request):
        r"""获取资产属性聚合值

        获取资产属性聚合值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMetricValue
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowMetricValueRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowMetricValueResponse`
        """
        http_info = self._show_metric_value_http_info(request)
        return self._call_api(**http_info)

    def show_metric_value_invoker(self, request):
        http_info = self._show_metric_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_metric_value_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/metrics/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetricValueResponse"
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

    def show_property_raw_value(self, request):
        r"""获取资产属性历史值

        获取资产属性历史值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPropertyRawValue
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowPropertyRawValueRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowPropertyRawValueResponse`
        """
        http_info = self._show_property_raw_value_http_info(request)
        return self._call_api(**http_info)

    def show_property_raw_value_invoker(self, request):
        http_info = self._show_property_raw_value_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_property_raw_value_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/assets/{asset_id}/property-values/query",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPropertyRawValueResponse"
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

    def create_datasource(self, request):
        r"""创建数据源

        创建数据源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatasource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateDatasourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateDatasourceResponse`
        """
        http_info = self._create_datasource_http_info(request)
        return self._call_api(**http_info)

    def create_datasource_invoker(self, request):
        http_info = self._create_datasource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_datasource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/datasources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatasourceResponse"
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

    def delete_datasource(self, request):
        r"""删除数据源

        删除数据源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatasource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteDatasourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteDatasourceResponse`
        """
        http_info = self._delete_datasource_http_info(request)
        return self._call_api(**http_info)

    def delete_datasource_invoker(self, request):
        http_info = self._delete_datasource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_datasource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/datasources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDatasourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def show_all_data_source(self, request):
        r"""查询数据源列表

        查询数据源列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllDataSource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowAllDataSourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowAllDataSourceResponse`
        """
        http_info = self._show_all_data_source_http_info(request)
        return self._call_api(**http_info)

    def show_all_data_source_invoker(self, request):
        http_info = self._show_all_data_source_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_all_data_source_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/datasources",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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

    def show_data_source(self, request):
        r"""查询数据源详情

        查询数据源详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataSource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowDataSourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowDataSourceResponse`
        """
        http_info = self._show_data_source_http_info(request)
        return self._call_api(**http_info)

    def show_data_source_invoker(self, request):
        http_info = self._show_data_source_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_data_source_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/datasources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def update_data_source(self, request):
        r"""修改数据源

        修改数据源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataSource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateDataSourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateDataSourceResponse`
        """
        http_info = self._update_data_source_http_info(request)
        return self._call_api(**http_info)

    def update_data_source_invoker(self, request):
        http_info = self._update_data_source_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_data_source_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/datasources/{datasource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def create_group(self, request):
        r"""创建存储组

        创建存储组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGroup
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateGroupRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateGroupResponse`
        """
        http_info = self._create_group_http_info(request)
        return self._call_api(**http_info)

    def create_group_invoker(self, request):
        http_info = self._create_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-store-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGroupResponse"
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

    def delete_group(self, request):
        r"""删除存储组

        删除存储组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteGroup
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteGroupRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteGroupResponse`
        """
        http_info = self._delete_group_http_info(request)
        return self._call_api(**http_info)

    def delete_group_invoker(self, request):
        http_info = self._delete_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/data-store-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_groups(self, request):
        r"""查询存储组列表

        查询存储组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGroups
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListGroupsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListGroupsResponse`
        """
        http_info = self._list_groups_http_info(request)
        return self._call_api(**http_info)

    def list_groups_invoker(self, request):
        http_info = self._list_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/data-store-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'unit' in local_var_params:
            query_params.append(('unit', local_var_params['unit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def update_group(self, request):
        r"""更新存储组

        更新存储组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateGroup
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateGroupRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateGroupResponse`
        """
        http_info = self._update_group_http_info(request)
        return self._call_api(**http_info)

    def update_group_invoker(self, request):
        http_info = self._update_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/data-store-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def delete_data_store(self, request):
        r"""删除存储

        删除存储
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataStore
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteDataStoreRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteDataStoreResponse`
        """
        http_info = self._delete_data_store_http_info(request)
        return self._call_api(**http_info)

    def delete_data_store_invoker(self, request):
        http_info = self._delete_data_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_data_store_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/data-stores/{data_store_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDataStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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

    def list_data_stores(self, request):
        r"""查询存储列表

        查询存储列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataStores
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListDataStoresRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListDataStoresResponse`
        """
        http_info = self._list_data_stores_http_info(request)
        return self._call_api(**http_info)

    def list_data_stores_invoker(self, request):
        http_info = self._list_data_stores_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_data_stores_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/data-stores",
            "request_type": request.__class__.__name__,
            "response_type": "ListDataStoresResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'data_store_id' in local_var_params:
            query_params.append(('data_store_id', local_var_params['data_store_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
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

    def update_data_store(self, request):
        r"""更新存储

        更新存储
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataStore
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateDataStoreRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateDataStoreResponse`
        """
        http_info = self._update_data_store_http_info(request)
        return self._call_api(**http_info)

    def update_data_store_invoker(self, request):
        http_info = self._update_data_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_data_store_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/data-stores/{data_store_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDataStoreResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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

    def list_history(self, request):
        r"""根据标签查询设备历史值

        根据标签查询设备历史值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHistory
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListHistoryRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListHistoryResponse`
        """
        http_info = self._list_history_http_info(request)
        return self._call_api(**http_info)

    def list_history_invoker(self, request):
        http_info = self._list_history_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_history_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-stores/{data_store_id}/property-values/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListHistoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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

    def list_metrics(self, request):
        r"""根据标签聚合、查询指标数据

        根据标签聚合、查询数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMetrics
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListMetricsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListMetricsResponse`
        """
        http_info = self._list_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_metrics_invoker(self, request):
        http_info = self._list_metrics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_metrics_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-stores/{data_store_id}/metrics/query",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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

    def show_property_values(self, request):
        r"""查询设备属性最新状态值

        查询设备属性最新状态值
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPropertyValues
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowPropertyValuesRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowPropertyValuesResponse`
        """
        http_info = self._show_property_values_http_info(request)
        return self._call_api(**http_info)

    def show_property_values_invoker(self, request):
        http_info = self._show_property_values_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_property_values_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data-stores/{data_store_id}/property-values/query-last",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPropertyValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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

    def list_tag_values(self, request):
        r"""查询标签的值列表

        查询标签的值列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTagValues
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListTagValuesRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListTagValuesResponse`
        """
        http_info = self._list_tag_values_http_info(request)
        return self._call_api(**http_info)

    def list_tag_values_invoker(self, request):
        http_info = self._list_tag_values_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tag_values_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/data-stores/{data_store_id}/tags/{tag_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagValuesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']
        if 'tag_name' in local_var_params:
            path_params['tag_name'] = local_var_params['tag_name']

        query_params = []
        if 'filters' in local_var_params:
            query_params.append(('filters', local_var_params['filters']))
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

    def add_dev_data(self, request):
        r"""通过API数据源上报设备数据

        通过API数据源上报设备数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddDevData
        :type request: :class:`huaweicloudsdkiotanalytics.v1.AddDevDataRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AddDevDataResponse`
        """
        http_info = self._add_dev_data_http_info(request)
        return self._call_api(**http_info)

    def add_dev_data_invoker(self, request):
        http_info = self._add_dev_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_dev_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/datasources/{datasource_id}/dev-data",
            "request_type": request.__class__.__name__,
            "response_type": "AddDevDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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

    def add_pipeline_job(self, request):
        r"""新建管道作业

        新建管道作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。（作业中各算子的详细配置请参考算子配置章节。） check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查。当检查不通过时，将作业状态修改为草稿；检查通过时，将作业状态修改为就绪，并返回成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddPipelineJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.AddPipelineJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.AddPipelineJobResponse`
        """
        http_info = self._add_pipeline_job_http_info(request)
        return self._call_api(**http_info)

    def add_pipeline_job_invoker(self, request):
        http_info = self._add_pipeline_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_pipeline_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/pipelines",
            "request_type": request.__class__.__name__,
            "response_type": "AddPipelineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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

    def delete_pipeline_job(self, request):
        r"""删除管道作业

        删除用户指定的管道作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipelineJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeletePipelineJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeletePipelineJobResponse`
        """
        http_info = self._delete_pipeline_job_http_info(request)
        return self._call_api(**http_info)

    def delete_pipeline_job_invoker(self, request):
        http_info = self._delete_pipeline_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_pipeline_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/pipelines/{pipeline_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeletePipelineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def list_pipeline_jobs(self, request):
        r"""获取管道作业列表

        获取用户下的所有管道作业，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineJobs
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListPipelineJobsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListPipelineJobsResponse`
        """
        http_info = self._list_pipeline_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_pipeline_jobs_invoker(self, request):
        http_info = self._list_pipeline_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_pipeline_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/pipelines",
            "request_type": request.__class__.__name__,
            "response_type": "ListPipelineJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_store_id' in local_var_params:
            query_params.append(('data_store_id', local_var_params['data_store_id']))
        if 'data_store_group_id' in local_var_params:
            query_params.append(('data_store_group_id', local_var_params['data_store_group_id']))
        if 'data_source_id' in local_var_params:
            query_params.append(('data_source_id', local_var_params['data_source_id']))
        if 'pipeline_name' in local_var_params:
            query_params.append(('pipeline_name', local_var_params['pipeline_name']))
        if 'operator_class_name' in local_var_params:
            query_params.append(('operator_class_name', local_var_params['operator_class_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))

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

    def show_pipeline_job(self, request):
        r"""获取管道作业详情

        获取指定管道作业的详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipelineJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowPipelineJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowPipelineJobResponse`
        """
        http_info = self._show_pipeline_job_http_info(request)
        return self._call_api(**http_info)

    def show_pipeline_job_invoker(self, request):
        http_info = self._show_pipeline_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_pipeline_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/pipelines/{pipeline_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPipelineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def start_pipeline_job(self, request):
        r"""启动管道作业

        提交管道作业到运行环境，实时接收数据源的数据并按用户定义的数据清洗逻辑对数据进行处理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartPipelineJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.StartPipelineJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StartPipelineJobResponse`
        """
        http_info = self._start_pipeline_job_http_info(request)
        return self._call_api(**http_info)

    def start_pipeline_job_invoker(self, request):
        http_info = self._start_pipeline_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_pipeline_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/pipelines/{pipeline_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartPipelineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'parallel' in local_var_params:
            query_params.append(('parallel', local_var_params['parallel']))
        if 'rtu' in local_var_params:
            query_params.append(('rtu', local_var_params['rtu']))
        if 'resume_savepoint' in local_var_params:
            query_params.append(('resume_savepoint', local_var_params['resume_savepoint']))

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

    def stop_pipeline_job(self, request):
        r"""停止管道作业

        停止一个正在运行中的管道作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopPipelineJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.StopPipelineJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StopPipelineJobResponse`
        """
        http_info = self._stop_pipeline_job_http_info(request)
        return self._call_api(**http_info)

    def stop_pipeline_job_invoker(self, request):
        http_info = self._stop_pipeline_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_pipeline_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/pipelines/{pipeline_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopPipelineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'trigger_savepoint' in local_var_params:
            query_params.append(('trigger_savepoint', local_var_params['trigger_savepoint']))

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

    def update_pipeline_job(self, request):
        r"""更新管道作业

        更新管道作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。（管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。） check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查。当检查不通过时，将作业状态修改为草稿；检查通过时，将作业状态修改为就绪，并返回成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePipelineJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdatePipelineJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdatePipelineJobResponse`
        """
        http_info = self._update_pipeline_job_http_info(request)
        return self._call_api(**http_info)

    def update_pipeline_job_invoker(self, request):
        http_info = self._update_pipeline_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_pipeline_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/pipelines/{pipeline_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePipelineJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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

    def create_streaming_job(self, request):
        r"""新建实时作业

        除名称和描述外，可先不提供作业的详细配置信息。 check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查，无论检查是否通过，都将作业及配置信息保存为草稿，当检查不通过时，返回失败及错误信息，检查通过时，将作业状态修改为就绪，并返回成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStreamingJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateStreamingJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateStreamingJobResponse`
        """
        http_info = self._create_streaming_job_http_info(request)
        return self._call_api(**http_info)

    def create_streaming_job_invoker(self, request):
        http_info = self._create_streaming_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_streaming_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/streaming/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStreamingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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

    def delete_streaming_job_by_id(self, request):
        r"""删除实时作业

        删除用户指定的作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStreamingJobById
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteStreamingJobByIdRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteStreamingJobByIdResponse`
        """
        http_info = self._delete_streaming_job_by_id_http_info(request)
        return self._call_api(**http_info)

    def delete_streaming_job_by_id_invoker(self, request):
        http_info = self._delete_streaming_job_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_streaming_job_by_id_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/streaming/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStreamingJobByIdResponse"
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

    def show_job_by_id(self, request):
        r"""获取实时作业详情

        获取指定作业的详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobById
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowJobByIdRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowJobByIdResponse`
        """
        http_info = self._show_job_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_job_by_id_invoker(self, request):
        http_info = self._show_job_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/streaming/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobByIdResponse"
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

    def show_jobs(self, request):
        r"""获取实时作业列表

        获取用户下的所有实时分析作业，支持分页。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobs
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowJobsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowJobsResponse`
        """
        http_info = self._show_jobs_http_info(request)
        return self._call_api(**http_info)

    def show_jobs_invoker(self, request):
        http_info = self._show_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/streaming/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_input_type' in local_var_params:
            query_params.append(('job_input_type', local_var_params['job_input_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))

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

    def update_streaming_job(self, request):
        r"""更新实时作业

        更新作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。 check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查，无论检查是否通过，都将作业及配置信息保存为草稿，当检查不通过时，返回失败及错误信息，检查通过时，将作业状态修改为就绪，并返回成功。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStreamingJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateStreamingJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateStreamingJobResponse`
        """
        http_info = self._update_streaming_job_http_info(request)
        return self._call_api(**http_info)

    def update_streaming_job_invoker(self, request):
        http_info = self._update_streaming_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_streaming_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/streaming/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStreamingJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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

    def start_job(self, request):
        r"""启动实时作业

        提交作业到运行环境，实时接收数据并按用户定义的业务逻辑对数据进行处理。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.StartJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StartJobResponse`
        """
        http_info = self._start_job_http_info(request)
        return self._call_api(**http_info)

    def start_job_invoker(self, request):
        http_info = self._start_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/streaming/jobs/{job_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'parallel' in local_var_params:
            query_params.append(('parallel', local_var_params['parallel']))
        if 'rtu' in local_var_params:
            query_params.append(('rtu', local_var_params['rtu']))
        if 'resume_savepoint' in local_var_params:
            query_params.append(('resume_savepoint', local_var_params['resume_savepoint']))

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

    def stop_job(self, request):
        r"""停止实时作业

        停止一个正在运行中的作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.StopJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StopJobResponse`
        """
        http_info = self._stop_job_http_info(request)
        return self._call_api(**http_info)

    def stop_job_invoker(self, request):
        http_info = self._stop_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/streaming/jobs/{job_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'trigger_savepoint' in local_var_params:
            query_params.append(('trigger_savepoint', local_var_params['trigger_savepoint']))

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

    def create_computing_resource(self, request):
        r"""创建批计算资源

        创建批计算资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateComputingResource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateComputingResourceResponse`
        """
        http_info = self._create_computing_resource_http_info(request)
        return self._call_api(**http_info)

    def create_computing_resource_invoker(self, request):
        http_info = self._create_computing_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_computing_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch-computing-resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateComputingResourceResponse"
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

    def delete_computing_resource(self, request):
        r"""删除批计算资源

        删除批计算资源。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteComputingResource
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteComputingResourceResponse`
        """
        http_info = self._delete_computing_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_computing_resource_invoker(self, request):
        http_info = self._delete_computing_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_computing_resource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/batch-computing-resources/{computing_resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteComputingResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'computing_resource_id' in local_var_params:
            path_params['computing_resource_id'] = local_var_params['computing_resource_id']

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

    def list_computing_resources(self, request):
        r"""查询批计算资源列表

        查询批计算资源列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComputingResources
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListComputingResourcesRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListComputingResourcesResponse`
        """
        http_info = self._list_computing_resources_http_info(request)
        return self._call_api(**http_info)

    def list_computing_resources_invoker(self, request):
        http_info = self._list_computing_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_computing_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/batch-computing-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListComputingResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'computing_resource_name' in local_var_params:
            query_params.append(('computing_resource_name', local_var_params['computing_resource_name']))
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

    def export_dataset(self, request):
        r"""下载离线作业结果

        将SQL语句的查询结果下载到本地，只支持下载“QUERY”类型作业的查询结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportDataset
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ExportDatasetRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ExportDatasetResponse`
        """
        http_info = self._export_dataset_http_info(request)
        return self._call_api(**http_info)

    def export_dataset_invoker(self, request):
        http_info = self._export_dataset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_dataset_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}/export-dataset",
            "request_type": request.__class__.__name__,
            "response_type": "ExportDatasetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

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

    def import_data(self, request):
        r"""执行导入数据离线作业

        将数据从文件导入OBS表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportData
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ImportDataRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ImportDataResponse`
        """
        http_info = self._import_data_http_info(request)
        return self._call_api(**http_info)

    def import_data_invoker(self, request):
        http_info = self._import_data_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_data_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch/jobs/import/runs",
            "request_type": request.__class__.__name__,
            "response_type": "ImportDataResponse"
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

    def show_dataset(self, request):
        r"""查询离线作业结果

        在执行SQL查询语句的作业完成后，查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。该API只能查看前1000条的结果记录，若要查看全部的结果记录，需要先导出查询结果再进行查看。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataset
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowDatasetRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowDatasetResponse`
        """
        http_info = self._show_dataset_http_info(request)
        return self._call_api(**http_info)

    def show_dataset_invoker(self, request):
        http_info = self._show_dataset_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_dataset_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}/query-dataset",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatasetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

        query_params = []
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

    def validate_sql(self, request):
        r"""检查离线作业SQL语法

        检查离线作业SQL语法。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateSql
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ValidateSqlRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ValidateSqlResponse`
        """
        http_info = self._validate_sql_http_info(request)
        return self._call_api(**http_info)

    def validate_sql_invoker(self, request):
        http_info = self._validate_sql_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _validate_sql_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch/validate-sql",
            "request_type": request.__class__.__name__,
            "response_type": "ValidateSqlResponse"
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

    def create_batch_job(self, request):
        r"""创建离线作业

        创建离线作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBatchJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateBatchJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateBatchJobResponse`
        """
        http_info = self._create_batch_job_http_info(request)
        return self._call_api(**http_info)

    def create_batch_job_invoker(self, request):
        http_info = self._create_batch_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_batch_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBatchJobResponse"
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

    def delete_batch_job(self, request):
        r"""删除离线作业

        删除离线作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBatchJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteBatchJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteBatchJobResponse`
        """
        http_info = self._delete_batch_job_http_info(request)
        return self._call_api(**http_info)

    def delete_batch_job_invoker(self, request):
        http_info = self._delete_batch_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_batch_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBatchJobResponse"
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

    def list_batch_jobs(self, request):
        r"""查询离线作业列表

        查询离线作业列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBatchJobs
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListBatchJobsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListBatchJobsResponse`
        """
        http_info = self._list_batch_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_batch_jobs_invoker(self, request):
        http_info = self._list_batch_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_batch_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/batch/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListBatchJobsResponse"
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
        if 'has_schedule' in local_var_params:
            query_params.append(('has_schedule', local_var_params['has_schedule']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'schedule_status' in local_var_params:
            query_params.append(('schedule_status', local_var_params['schedule_status']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
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

    def show_batch_job(self, request):
        r"""查询离线作业详情

        查询离线作业详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBatchJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowBatchJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowBatchJobResponse`
        """
        http_info = self._show_batch_job_http_info(request)
        return self._call_api(**http_info)

    def show_batch_job_invoker(self, request):
        http_info = self._show_batch_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_batch_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowBatchJobResponse"
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

    def update_batch_job(self, request):
        r"""修改离线作业

        修改离线作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateBatchJob
        :type request: :class:`huaweicloudsdkiotanalytics.v1.UpdateBatchJobRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.UpdateBatchJobResponse`
        """
        http_info = self._update_batch_job_http_info(request)
        return self._call_api(**http_info)

    def update_batch_job_invoker(self, request):
        http_info = self._update_batch_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_batch_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateBatchJobResponse"
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

    def create_run(self, request):
        r"""执行离线作业

        执行离线作业。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateRun
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateRunRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateRunResponse`
        """
        http_info = self._create_run_http_info(request)
        return self._call_api(**http_info)

    def create_run_invoker(self, request):
        http_info = self._create_run_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_run_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}/runs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateRunResponse"
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

    def delete_run(self, request):
        r"""停止离线作业

        停止提交中或运行中的离线作业，若作业已经执行结束或失败则无法停止。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRun
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteRunRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteRunResponse`
        """
        http_info = self._delete_run_http_info(request)
        return self._call_api(**http_info)

    def delete_run_invoker(self, request):
        http_info = self._delete_run_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_run_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRunResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

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

    def list_runs(self, request):
        r"""查询离线作业运行列表

        查询离线作业运行列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRuns
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListRunsRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListRunsResponse`
        """
        http_info = self._list_runs_http_info(request)
        return self._call_api(**http_info)

    def list_runs_invoker(self, request):
        http_info = self._list_runs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_runs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/batch/jobs/runs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRunsResponse"
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'sql_pattern' in local_var_params:
            query_params.append(('sql_pattern', local_var_params['sql_pattern']))
        if 'sql_type' in local_var_params:
            query_params.append(('sql_type', local_var_params['sql_type']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))

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

    def show_run(self, request):
        r"""查询离线作业运行详情

        查询离线作业运行详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRun
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowRunRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowRunResponse`
        """
        http_info = self._show_run_http_info(request)
        return self._call_api(**http_info)

    def show_run_invoker(self, request):
        http_info = self._show_run_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_run_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRunResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

        query_params = []
        if 'with_details' in local_var_params:
            query_params.append(('with_details', local_var_params['with_details']))

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

    def create_table(self, request):
        r"""创建离线数据表

        创建离线数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTable
        :type request: :class:`huaweicloudsdkiotanalytics.v1.CreateTableRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.CreateTableResponse`
        """
        http_info = self._create_table_http_info(request)
        return self._call_api(**http_info)

    def create_table_invoker(self, request):
        http_info = self._create_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableResponse"
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

    def delete_table(self, request):
        r"""删除离线数据表

        删除离线数据表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTable
        :type request: :class:`huaweicloudsdkiotanalytics.v1.DeleteTableRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DeleteTableResponse`
        """
        http_info = self._delete_table_http_info(request)
        return self._call_api(**http_info)

    def delete_table_invoker(self, request):
        http_info = self._delete_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_table_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/tables/{table_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def list_tables(self, request):
        r"""查询离线数据表列表

        查询离线数据表列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTables
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ListTablesRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ListTablesResponse`
        """
        http_info = self._list_tables_http_info(request)
        return self._call_api(**http_info)

    def list_tables_invoker(self, request):
        http_info = self._list_tables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListTablesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
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

    def show_table_preview(self, request):
        r"""预览离线数据表内容

        预览离线数据表内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTablePreview
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowTablePreviewRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowTablePreviewResponse`
        """
        http_info = self._show_table_preview_http_info(request)
        return self._call_api(**http_info)

    def show_table_preview_invoker(self, request):
        http_info = self._show_table_preview_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_table_preview_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tables/{table_id}/preview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTablePreviewResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

    def show_table_schema(self, request):
        r"""查询离线数据表结构

        查询离线数据表结构。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTableSchema
        :type request: :class:`huaweicloudsdkiotanalytics.v1.ShowTableSchemaRequest`
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.ShowTableSchemaResponse`
        """
        http_info = self._show_table_schema_http_info(request)
        return self._call_api(**http_info)

    def show_table_schema_invoker(self, request):
        http_info = self._show_table_schema_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_table_schema_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tables/{table_id}/schema",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTableSchemaResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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

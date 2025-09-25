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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdcos'")


class DcosClient(Client):
    def __init__(self):
        super(DcosClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdcos.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DcosClient":
                raise TypeError("client type error, support client type is DcosClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_order(self, request):
        r"""客户查询服务单列表

        客户查询服务单列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListOrder
        :type request: :class:`huaweicloudsdkdcos.v1.ListOrderRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.ListOrderResponse`
        """
        http_info = self._list_order_http_info(request)
        return self._call_api(**http_info)

    def list_order_invoker(self, request):
        http_info = self._list_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_order_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/orders/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'sub_type' in local_var_params:
            query_params.append(('sub_type', local_var_params['sub_type']))
        if 'stage' in local_var_params:
            query_params.append(('stage', local_var_params['stage']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'applicant' in local_var_params:
            query_params.append(('applicant', local_var_params['applicant']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
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

    def save_order(self, request):
        r"""客户创建服务单

        客户创建服务单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SaveOrder
        :type request: :class:`huaweicloudsdkdcos.v1.SaveOrderRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.SaveOrderResponse`
        """
        http_info = self._save_order_http_info(request)
        return self._call_api(**http_info)

    def save_order_invoker(self, request):
        http_info = self._save_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _save_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/orders/save",
            "request_type": request.__class__.__name__,
            "response_type": "SaveOrderResponse"
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

    def show_order(self, request):
        r"""客户查询服务单详情

        客户查询服务单详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrder
        :type request: :class:`huaweicloudsdkdcos.v1.ShowOrderRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.ShowOrderResponse`
        """
        http_info = self._show_order_http_info(request)
        return self._call_api(**http_info)

    def show_order_invoker(self, request):
        http_info = self._show_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_order_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/orders/{number}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'number' in local_var_params:
            path_params['number'] = local_var_params['number']

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

    def show_order_catalogue(self, request):
        r"""获取服务单目录列表

        获取服务单目录列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrderCatalogue
        :type request: :class:`huaweicloudsdkdcos.v1.ShowOrderCatalogueRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.ShowOrderCatalogueResponse`
        """
        http_info = self._show_order_catalogue_http_info(request)
        return self._call_api(**http_info)

    def show_order_catalogue_invoker(self, request):
        http_info = self._show_order_catalogue_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_order_catalogue_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/orders/catalogue",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrderCatalogueResponse"
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

    def show_order_information(self, request):
        r"""获取服务服务单项目信息

        获取服务服务单项目信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOrderInformation
        :type request: :class:`huaweicloudsdkdcos.v1.ShowOrderInformationRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.ShowOrderInformationResponse`
        """
        http_info = self._show_order_information_http_info(request)
        return self._call_api(**http_info)

    def show_order_information_invoker(self, request):
        http_info = self._show_order_information_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_order_information_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/orders/information/{model_code}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOrderInformationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'model_code' in local_var_params:
            path_params['model_code'] = local_var_params['model_code']

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

    def show_page_asset_list_result(self, request):
        r"""资产列表

        资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPageAssetListResult
        :type request: :class:`huaweicloudsdkdcos.v1.ShowPageAssetListResultRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.ShowPageAssetListResultResponse`
        """
        http_info = self._show_page_asset_list_result_http_info(request)
        return self._call_api(**http_info)

    def show_page_asset_list_result_invoker(self, request):
        http_info = self._show_page_asset_list_result_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_page_asset_list_result_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/assets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPageAssetListResultResponse"
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

    def upload_file(self, request):
        r"""上传附件

        上传附件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadFile
        :type request: :class:`huaweicloudsdkdcos.v1.UploadFileRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.UploadFileResponse`
        """
        http_info = self._upload_file_http_info(request)
        return self._call_api(**http_info)

    def upload_file_invoker(self, request):
        http_info = self._upload_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upload_file_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/files/upload-file",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'scene_code' in local_var_params:
            form_params['scene_code'] = local_var_params['scene_code']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-request-id", ]

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

    def verify_order(self, request):
        r"""验收服务单

        验收服务单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for VerifyOrder
        :type request: :class:`huaweicloudsdkdcos.v1.VerifyOrderRequest`
        :rtype: :class:`huaweicloudsdkdcos.v1.VerifyOrderResponse`
        """
        http_info = self._verify_order_http_info(request)
        return self._call_api(**http_info)

    def verify_order_invoker(self, request):
        http_info = self._verify_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _verify_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/orders/verify/{number}",
            "request_type": request.__class__.__name__,
            "response_type": "VerifyOrderResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'number' in local_var_params:
            path_params['number'] = local_var_params['number']

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkimagesearch'")


class ImageSearchAsyncClient(Client):
    def __init__(self):
        super(ImageSearchAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkimagesearch.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "ImageSearchAsyncClient":
                raise TypeError("client type error, support client type is ImageSearchAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def run_add_data_async(self, request):
        r"""添加数据

        添加数据到指定服务实例中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunAddData
        :type request: :class:`huaweicloudsdkimagesearch.v2.RunAddDataRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v2.RunAddDataResponse`
        """
        http_info = self._run_add_data_http_info(request)
        return self._call_api(**http_info)

    def run_add_data_async_invoker(self, request):
        http_info = self._run_add_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_add_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mms/{service_name}/data/add",
            "request_type": request.__class__.__name__,
            "response_type": "RunAddDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

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

    def run_check_data_async(self, request):
        r"""检查数据

        检查指定服务实例中的对应数据，支持指定ID检查和条件检查。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunCheckData
        :type request: :class:`huaweicloudsdkimagesearch.v2.RunCheckDataRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v2.RunCheckDataResponse`
        """
        http_info = self._run_check_data_http_info(request)
        return self._call_api(**http_info)

    def run_check_data_async_invoker(self, request):
        http_info = self._run_check_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_check_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mms/{service_name}/data/check",
            "request_type": request.__class__.__name__,
            "response_type": "RunCheckDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

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

    def run_delete_data_async(self, request):
        r"""删除数据

        删除指定服务实例中的对应数据，支持指定ID删除和条件删除。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunDeleteData
        :type request: :class:`huaweicloudsdkimagesearch.v2.RunDeleteDataRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v2.RunDeleteDataResponse`
        """
        http_info = self._run_delete_data_http_info(request)
        return self._call_api(**http_info)

    def run_delete_data_async_invoker(self, request):
        http_info = self._run_delete_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_delete_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mms/{service_name}/data/delete",
            "request_type": request.__class__.__name__,
            "response_type": "RunDeleteDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

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

    def run_search_async(self, request):
        r"""搜索

        从指定服务实例中进行搜索。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunSearch
        :type request: :class:`huaweicloudsdkimagesearch.v2.RunSearchRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v2.RunSearchResponse`
        """
        http_info = self._run_search_http_info(request)
        return self._call_api(**http_info)

    def run_search_async_invoker(self, request):
        http_info = self._run_search_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_search_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mms/{service_name}/search",
            "request_type": request.__class__.__name__,
            "response_type": "RunSearchResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

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

    def run_update_data_async(self, request):
        r"""更新数据

        更新指定服务实例中的对应数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunUpdateData
        :type request: :class:`huaweicloudsdkimagesearch.v2.RunUpdateDataRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v2.RunUpdateDataResponse`
        """
        http_info = self._run_update_data_http_info(request)
        return self._call_api(**http_info)

    def run_update_data_async_invoker(self, request):
        http_info = self._run_update_data_http_info(request)
        return AsyncInvoker(self, http_info)

    def _run_update_data_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/mms/{service_name}/data/update",
            "request_type": request.__class__.__name__,
            "response_type": "RunUpdateDataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_name' in local_var_params:
            path_params['service_name'] = local_var_params['service_name']

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

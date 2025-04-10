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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcce'")


class CceClient(Client):
    def __init__(self):
        super(CceClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcce.v5.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CceClient":
                raise TypeError("client type error, support client type is CceClient")
            client_builder = ClientBuilder(clazz)

        
        try:
            from .cce_exception_handler import CceExceptionHandler
            client_builder.with_exception_handler(CceExceptionHandler())
        except (ImportError, AttributeError):
            warnings.warn("failed to import 'CceExceptionHandler', please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcce'")

        return client_builder

    def create_image_cache(self, request):
        r"""创建镜像缓存

        创建镜像缓存。创建过程会在指定集群中启动临时Pod进行镜像缓存构建，创建镜像缓存后，可在负载创建时通过使用镜像缓存功能大幅减少下载容器镜像的耗时，实现容器的快速启动。单租户创建镜像缓存数量上限为50。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImageCache
        :type request: :class:`huaweicloudsdkcce.v5.CreateImageCacheRequest`
        :rtype: :class:`huaweicloudsdkcce.v5.CreateImageCacheResponse`
        """
        http_info = self._create_image_cache_http_info(request)
        return self._call_api(**http_info)

    def create_image_cache_invoker(self, request):
        http_info = self._create_image_cache_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_image_cache_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v5/imagecaches",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageCacheResponse"
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

    def delete_image_cache(self, request):
        r"""删除镜像缓存

        删除镜像缓存
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImageCache
        :type request: :class:`huaweicloudsdkcce.v5.DeleteImageCacheRequest`
        :rtype: :class:`huaweicloudsdkcce.v5.DeleteImageCacheResponse`
        """
        http_info = self._delete_image_cache_http_info(request)
        return self._call_api(**http_info)

    def delete_image_cache_invoker(self, request):
        http_info = self._delete_image_cache_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_image_cache_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v5/imagecaches/{image_cache_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteImageCacheResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_cache_id' in local_var_params:
            path_params['image_cache_id'] = local_var_params['image_cache_id']

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

    def list_image_caches(self, request):
        r"""查询镜像缓存列表

        查询镜像缓存列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImageCaches
        :type request: :class:`huaweicloudsdkcce.v5.ListImageCachesRequest`
        :rtype: :class:`huaweicloudsdkcce.v5.ListImageCachesResponse`
        """
        http_info = self._list_image_caches_http_info(request)
        return self._call_api(**http_info)

    def list_image_caches_invoker(self, request):
        http_info = self._list_image_caches_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_image_caches_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/imagecaches",
            "request_type": request.__class__.__name__,
            "response_type": "ListImageCachesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def show_image_cache(self, request):
        r"""查询镜像缓存详情

        查询镜像缓存详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageCache
        :type request: :class:`huaweicloudsdkcce.v5.ShowImageCacheRequest`
        :rtype: :class:`huaweicloudsdkcce.v5.ShowImageCacheResponse`
        """
        http_info = self._show_image_cache_http_info(request)
        return self._call_api(**http_info)

    def show_image_cache_invoker(self, request):
        http_info = self._show_image_cache_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_image_cache_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v5/imagecaches/{image_cache_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageCacheResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'image_cache_id' in local_var_params:
            path_params['image_cache_id'] = local_var_params['image_cache_id']

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

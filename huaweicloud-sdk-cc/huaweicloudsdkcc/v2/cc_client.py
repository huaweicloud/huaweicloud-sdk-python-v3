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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcc'")


class CcClient(Client):
    def __init__(self):
        super(CcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcc.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls, "GlobalCredentials")
        else:
            if clazz.__name__ != "CcClient":
                raise TypeError("client type error, support client type is CcClient")
            client_builder = ClientBuilder(clazz, "GlobalCredentials")

        

        return client_builder

    def batch_create_delete_tags(self, request):
        """批量创建和删除资源标签

        批量创建和删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCreateDeleteTags
        :type request: :class:`huaweicloudsdkcc.v2.BatchCreateDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v2.BatchCreateDeleteTagsResponse`
        """
        http_info = self._batch_create_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_delete_tags_invoker(self, request):
        http_info = self._batch_create_delete_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_create_delete_tags_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateDeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def create_tag(self, request):
        """添加资源标签

        添加资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkcc.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkcc.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def delete_tag(self, request):
        """删除资源标签

        删除资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkcc.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkcc.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_tag_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags/{tag_key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'tag_key' in local_var_params:
            path_params['tag_key'] = local_var_params['tag_key']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_domain_tags(self, request):
        """查询账户资源标签

        查询账户资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDomainTags
        :type request: :class:`huaweicloudsdkcc.v2.ListDomainTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v2.ListDomainTagsResponse`
        """
        http_info = self._list_domain_tags_http_info(request)
        return self._call_api(**http_info)

    def list_domain_tags_invoker(self, request):
        http_info = self._list_domain_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_domain_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListDomainTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_resource_by_filter_tag(self, request):
        """查询资源实例

        查询资源实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResourceByFilterTag
        :type request: :class:`huaweicloudsdkcc.v2.ListResourceByFilterTagRequest`
        :rtype: :class:`huaweicloudsdkcc.v2.ListResourceByFilterTagResponse`
        """
        http_info = self._list_resource_by_filter_tag_http_info(request)
        return self._call_api(**http_info)

    def list_resource_by_filter_tag_invoker(self, request):
        http_info = self._list_resource_by_filter_tag_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resource_by_filter_tag_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/ccaas/{resource_type}/resource-instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceByFilterTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_tags(self, request):
        """查询资源标签

        查询资源标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkcc.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkcc.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_tags_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/ccaas/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DscAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(DscAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdsc.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DscClient":
            raise TypeError("client type error, support client type is DscClient")

        return ClientBuilder(clazz)

    def batch_add_data_mask_async(self, request):
        """对数据进行脱敏

        对数据进行脱敏

        :param BatchAddDataMaskRequest request
        :return: BatchAddDataMaskResponse
        """
        return self.batch_add_data_mask_with_http_info(request)

    def batch_add_data_mask_with_http_info(self, request):
        """对数据进行脱敏

        对数据进行脱敏

        :param BatchAddDataMaskRequest request
        :return: BatchAddDataMaskResponse
        """

        all_params = ['batch_add_data_mask_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/data/mask',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchAddDataMaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_database_water_mark_async(self, request):
        """嵌入数据水印

        对json体中数据动态添加水印

        :param CreateDatabaseWaterMarkRequest request
        :return: CreateDatabaseWaterMarkResponse
        """
        return self.create_database_water_mark_with_http_info(request)

    def create_database_water_mark_with_http_info(self, request):
        """嵌入数据水印

        对json体中数据动态添加水印

        :param CreateDatabaseWaterMarkRequest request
        :return: CreateDatabaseWaterMarkResponse
        """

        all_params = ['create_database_water_mark_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sdg/database/watermark/embed',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDatabaseWaterMarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_doc_watermark_async(self, request):
        """嵌入文档水印

        嵌入文档水印

        :param CreateDocWatermarkRequest request
        :return: CreateDocWatermarkResponse
        """
        return self.create_doc_watermark_with_http_info(request)

    def create_doc_watermark_with_http_info(self, request):
        """嵌入文档水印

        嵌入文档水印

        :param CreateDocWatermarkRequest request
        :return: CreateDocWatermarkResponse
        """

        all_params = ['doc_type', 'file', 'file_password', 'visible_watermark', 'font_size', 'rotation', 'opacity', 'blind_watermark', 'image_mark', 'visible_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'doc_type' in local_var_params:
            form_params['doc_type'] = local_var_params['doc_type']
        if 'file_password' in local_var_params:
            form_params['file_password'] = local_var_params['file_password']
        if 'visible_watermark' in local_var_params:
            form_params['visible_watermark'] = local_var_params['visible_watermark']
        if 'font_size' in local_var_params:
            form_params['font_size'] = local_var_params['font_size']
        if 'rotation' in local_var_params:
            form_params['rotation'] = local_var_params['rotation']
        if 'opacity' in local_var_params:
            form_params['opacity'] = local_var_params['opacity']
        if 'blind_watermark' in local_var_params:
            form_params['blind_watermark'] = local_var_params['blind_watermark']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'image_mark' in local_var_params:
            form_params['image_mark'] = local_var_params['image_mark']
        if 'visible_type' in local_var_params:
            form_params['visible_type'] = local_var_params['visible_type']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sdg/doc/watermark/embed',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDocWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_image_watermark_async(self, request):
        """嵌入图片水印

        给上传的图片添加暗水印，目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。

        :param CreateImageWatermarkRequest request
        :return: CreateImageWatermarkResponse
        """
        return self.create_image_watermark_with_http_info(request)

    def create_image_watermark_with_http_info(self, request):
        """嵌入图片水印

        给上传的图片添加暗水印，目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。

        :param CreateImageWatermarkRequest request
        :return: CreateImageWatermarkResponse
        """

        all_params = ['file', 'blind_watermark']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'blind_watermark' in local_var_params:
            form_params['blind_watermark'] = local_var_params['blind_watermark']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/image/watermark/embed',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateImageWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_database_water_mark_async(self, request):
        """提取数据水印

        提取请求数据中水印内容

        :param ShowDatabaseWaterMarkRequest request
        :return: ShowDatabaseWaterMarkResponse
        """
        return self.show_database_water_mark_with_http_info(request)

    def show_database_water_mark_with_http_info(self, request):
        """提取数据水印

        提取请求数据中水印内容

        :param ShowDatabaseWaterMarkRequest request
        :return: ShowDatabaseWaterMarkResponse
        """

        all_params = ['show_database_water_mark_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sdg/database/watermark/extract',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDatabaseWaterMarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_doc_watermark_async(self, request):
        """提取文档水印

        提取文档水印

        :param ShowDocWatermarkRequest request
        :return: ShowDocWatermarkResponse
        """
        return self.show_doc_watermark_with_http_info(request)

    def show_doc_watermark_with_http_info(self, request):
        """提取文档水印

        提取文档水印

        :param ShowDocWatermarkRequest request
        :return: ShowDocWatermarkResponse
        """

        all_params = ['doc_type', 'file', 'file_password']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'doc_type' in local_var_params:
            form_params['doc_type'] = local_var_params['doc_type']
        if 'file_password' in local_var_params:
            form_params['file_password'] = local_var_params['file_password']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sdg/doc/watermark/extract',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDocWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_image_watermark_async(self, request):
        """提取图片水印

        提取图片中的暗水印内容

        :param ShowImageWatermarkRequest request
        :return: ShowImageWatermarkResponse
        """
        return self.show_image_watermark_with_http_info(request)

    def show_image_watermark_with_http_info(self, request):
        """提取图片水印

        提取图片中的暗水印内容

        :param ShowImageWatermarkRequest request
        :return: ShowImageWatermarkResponse
        """

        all_params = ['file', 'mark_len']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'mark_len' in local_var_params:
            form_params['mark_len'] = local_var_params['mark_len']

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/image/watermark/extract',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)

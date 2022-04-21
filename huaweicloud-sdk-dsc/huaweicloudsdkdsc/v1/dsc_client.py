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


class DscClient(Client):
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
        super(DscClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdsc.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DscClient":
            raise TypeError("client type error, support client type is DscClient")

        return ClientBuilder(clazz)

    def batch_add_data_mask(self, request):
        """对数据进行脱敏

        对数据进行脱敏
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for BatchAddDataMask
        :type request: :class:`huaweicloudsdkdsc.v1.BatchAddDataMaskRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.BatchAddDataMaskResponse`
        """
        return self.batch_add_data_mask_with_http_info(request)

    def batch_add_data_mask_with_http_info(self, request):
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

    def create_database_water_mark(self, request):
        """嵌入数据水印

        对json体中数据动态添加水印
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseWaterMark
        :type request: :class:`huaweicloudsdkdsc.v1.CreateDatabaseWaterMarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateDatabaseWaterMarkResponse`
        """
        return self.create_database_water_mark_with_http_info(request)

    def create_database_water_mark_with_http_info(self, request):
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

    def create_doc_watermark(self, request):
        """文档嵌入水印

        对WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf) 类型的文件嵌入文字暗水印、文字明水印或者图片明水印，用户以formData的格式传入待加水印的文件和水印相关信息，DSC服务给文件加完水印后返回给用户已嵌入水印的文件的二进制流。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDocWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkResponse`
        """
        return self.create_doc_watermark_with_http_info(request)

    def create_doc_watermark_with_http_info(self, request):
        all_params = ['doc_type', 'file', 'file_password', 'marked_file_password', 'readonly_password', 'visible_watermark', 'font_size', 'rotation', 'opacity', 'blind_watermark', 'image_mark', 'visible_type']
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
        if 'marked_file_password' in local_var_params:
            form_params['marked_file_password'] = local_var_params['marked_file_password']
        if 'readonly_password' in local_var_params:
            form_params['readonly_password'] = local_var_params['readonly_password']
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

    def create_doc_watermark_by_address(self, request):
        """文档嵌入水印（文件地址版本）

        对WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)*类型的文档嵌入文字暗水印、文字明水印或者图片明水印，用户传入待加水印的文档地址（目前支持OBS)和水印相关信息，DSC服务对文档加完水印后返回给用户已嵌入水印的文档的存放地址。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateDocWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkByAddressResponse`
        """
        return self.create_doc_watermark_by_address_with_http_info(request)

    def create_doc_watermark_by_address_with_http_info(self, request):
        all_params = ['create_doc_watermark_by_address_request_body']
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
            resource_path='/v1/{project_id}/doc-address/watermark/embed',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDocWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_watermark(self, request):
        """图片嵌入暗水印

        对图片嵌入文字暗水印或者图片暗水印，用户以formData的格式传入待加水印图片和水印相关信息，DSC服务对图片加完水印后返回给用户已嵌入水印的图片二进制流，目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateImageWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkResponse`
        """
        return self.create_image_watermark_with_http_info(request)

    def create_image_watermark_with_http_info(self, request):
        all_params = ['file', 'blind_watermark', 'image_watermark']
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
        if 'image_watermark' in local_var_params:
            form_params['image_watermark'] = local_var_params['image_watermark']

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

    def create_image_watermark_by_address(self, request):
        """图片嵌入暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的图片嵌入文字暗水印或者图片暗水印，已嵌入的水印的图片将存放在用户指定的位置（目前支持华为云OBS），支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for CreateImageWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkByAddressResponse`
        """
        return self.create_image_watermark_by_address_with_http_info(request)

    def create_image_watermark_by_address_with_http_info(self, request):
        all_params = ['create_image_watermark_by_address_request_body']
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
            resource_path='/v1/{project_id}/image-address/watermark/embed',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateImageWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_database_water_mark(self, request):
        """提取数据水印

        提取请求数据中水印内容
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDatabaseWaterMark
        :type request: :class:`huaweicloudsdkdsc.v1.ShowDatabaseWaterMarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowDatabaseWaterMarkResponse`
        """
        return self.show_database_water_mark_with_http_info(request)

    def show_database_water_mark_with_http_info(self, request):
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

    def show_doc_watermark(self, request):
        """文档提取暗水印

        对已嵌入文字暗水印的WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)类型的文档进行文字暗水印提取，用户以formData的格式传入待提取水印的文件，DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDocWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkResponse`
        """
        return self.show_doc_watermark_with_http_info(request)

    def show_doc_watermark_with_http_info(self, request):
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

    def show_doc_watermark_by_address(self, request):
        """文档提取暗水印（文档地址版本）

        支持对已嵌入文字暗水印的WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)类型的文档进行水印提取，用户传入待提取水印的文档地址（目前支持OBS），DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowDocWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkByAddressResponse`
        """
        return self.show_doc_watermark_by_address_with_http_info(request)

    def show_doc_watermark_by_address_with_http_info(self, request):
        all_params = ['show_doc_watermark_by_address_request_body']
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
            resource_path='/v1/{project_id}/doc-address/watermark/extract',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDocWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark(self, request):
        """提取图片中的文字暗水印

        对已嵌入文字暗水印的图片进行水印提取，用户以formData的格式传入待提取水印的图片，DSC服务以JSON的格式返回从图片里提取的出的文字暗水印。目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkResponse`
        """
        return self.show_image_watermark_with_http_info(request)

    def show_image_watermark_with_http_info(self, request):
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

    def show_image_watermark_by_address(self, request):
        """提取图片中的文字暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的已嵌入文字暗水印的图片提取文字暗水印，支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkByAddressResponse`
        """
        return self.show_image_watermark_by_address_with_http_info(request)

    def show_image_watermark_by_address_with_http_info(self, request):
        all_params = ['show_image_watermark_by_address_request_body']
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
            resource_path='/v1/{project_id}/image-address/watermark/extract',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark_with_image(self, request):
        """提取图片中的图片暗水印

        对已嵌入图片暗水印的图片进行水印提取，用户以formData的格式传入待提取水印的图片，DSC服务以图片二进制流的格式返回从图片里提取的出的图片暗水印。目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermarkWithImage
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageResponse`
        """
        return self.show_image_watermark_with_image_with_http_info(request)

    def show_image_watermark_with_image_with_http_info(self, request):
        all_params = ['file']
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
            resource_path='/v1/{project_id}/image/watermark/extract-image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageWatermarkWithImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark_with_image_by_address(self, request):
        """提取图片中的图片暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的已嵌入图片暗水印的图片提取图片暗水印，提取出的水印图片将存放在用户指定的位置（目前支持华为云OBS），支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermarkWithImageByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageByAddressResponse`
        """
        return self.show_image_watermark_with_image_by_address_with_http_info(request)

    def show_image_watermark_with_image_by_address_with_http_info(self, request):
        all_params = ['show_image_watermark_with_image_by_address_request_body']
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
            resource_path='/v1/{project_id}/image-address/watermark/extract-image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageWatermarkWithImageByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_scan_job_results(self, request):
        """查询指定任务扫描结果

        查询指定任务扫描结果
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowScanJobResults
        :type request: :class:`huaweicloudsdkdsc.v1.ShowScanJobResultsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowScanJobResultsResponse`
        """
        return self.show_scan_job_results_with_http_info(request)

    def show_scan_job_results_with_http_info(self, request):
        all_params = ['job_id', 'offset', 'limit', 'type', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sdg/scan/job/{job_id}/results',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowScanJobResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_scan_jobs(self, request):
        """查询扫描任务列表

        查询扫描任务列表
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowScanJobs
        :type request: :class:`huaweicloudsdkdsc.v1.ShowScanJobsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowScanJobsResponse`
        """
        return self.show_scan_jobs_with_http_info(request)

    def show_scan_jobs_with_http_info(self, request):
        all_params = ['offset', 'limit', 'content', 'start_time', 'end_time']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'content' in local_var_params:
            query_params.append(('content', local_var_params['content']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/sdg/scan/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowScanJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_open_api_called_records(self, request):
        """查询OpenApi调用记录

        查询OpenApi调用记录
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for ShowOpenApiCalledRecords
        :type request: :class:`huaweicloudsdkdsc.v1.ShowOpenApiCalledRecordsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowOpenApiCalledRecordsResponse`
        """
        return self.show_open_api_called_records_with_http_info(request)

    def show_open_api_called_records_with_http_info(self, request):
        all_params = ['limit', 'called_url', 'start_time', 'end_time', 'marker']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'called_url' in local_var_params:
            query_params.append(('called_url', local_var_params['called_url']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/openapi/called-records',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowOpenApiCalledRecordsResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)

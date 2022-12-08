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

    def add_buckets_async(self, request):
        """添加资产授权

        添加数据资产扫描授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddBuckets
        :type request: :class:`huaweicloudsdkdsc.v1.AddBucketsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddBucketsResponse`
        """
        return self.add_buckets_with_http_info(request)

    def add_buckets_with_http_info(self, request):
        all_params = ['add_buckets_request_body', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/sdg/asset/obs/buckets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddBucketsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_rule_async(self, request):
        """创建扫描规则

        根据指定的规则名称、规则类型、风险等级、最小匹配次数等参数创建自定义的敏感数据识别规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRule
        :type request: :class:`huaweicloudsdkdsc.v1.AddRuleRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddRuleResponse`
        """
        return self.add_rule_with_http_info(request)

    def add_rule_with_http_info(self, request):
        all_params = ['add_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/sdg/server/scan/rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_rule_group_async(self, request):
        """创建扫描规则组

        根据指定的规则组名称和扫描规则列表创建敏感数据扫描规则组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddRuleGroup
        :type request: :class:`huaweicloudsdkdsc.v1.AddRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddRuleGroupResponse`
        """
        return self.add_rule_group_with_http_info(request)

    def add_rule_group_with_http_info(self, request):
        all_params = ['add_rule_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/sdg/server/scan/groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddRuleGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_scan_job_async(self, request):
        """创建扫描任务

        根据指定的任务名称、扫描方式、扫描周期、扫描规则组、扫描时间创建扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddScanJob
        :type request: :class:`huaweicloudsdkdsc.v1.AddScanJobRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddScanJobResponse`
        """
        return self.add_scan_job_with_http_info(request)

    def add_scan_job_with_http_info(self, request):
        all_params = ['add_scan_job_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/sdg/scan/job',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddScanJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_add_data_mask_async(self, request):
        """对数据进行脱敏

        对数据进行脱敏
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='BatchAddDataMaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_db_template_operation_async(self, request):
        """开启/停止脱敏任务

        开启/停止脱敏任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeDbTemplateOperation
        :type request: :class:`huaweicloudsdkdsc.v1.ChangeDbTemplateOperationRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ChangeDbTemplateOperationResponse`
        """
        return self.change_db_template_operation_with_http_info(request)

    def change_db_template_operation_with_http_info(self, request):
        all_params = ['template_id', 'change_db_template_operation_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1/{project_id}/sdg/server/mask/dbs/templates/{template_id}/operation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeDbTemplateOperationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_rule_async(self, request):
        """修改扫描规则

        修改自定义的敏感数据识别规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ChangeRule
        :type request: :class:`huaweicloudsdkdsc.v1.ChangeRuleRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ChangeRuleResponse`
        """
        return self.change_rule_with_http_info(request)

    def change_rule_with_http_info(self, request):
        all_params = ['change_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/sdg/server/scan/rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangeRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database_water_mark_async(self, request):
        """嵌入数据水印

        对json体中数据动态添加水印
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='CreateDatabaseWaterMarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_doc_watermark_async(self, request):
        """文档嵌入水印

        对WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf) 类型的文件嵌入文字暗水印、文字明水印或者图片明水印，用户以formData的格式传入待加水印的文件和水印相关信息，DSC服务给文件加完水印后返回给用户已嵌入水印的文件的二进制流。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='CreateDocWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_doc_watermark_by_address_async(self, request):
        """文档嵌入水印（文件地址版本）

        对WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)*类型的文档嵌入文字暗水印、文字明水印或者图片明水印，用户传入待加水印的文档地址（目前支持OBS)和水印相关信息，DSC服务对文档加完水印后返回给用户已嵌入水印的文档的存放地址。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='CreateDocWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_watermark_async(self, request):
        """图片嵌入暗水印

        对图片嵌入文字暗水印或者图片暗水印，用户以formData的格式传入待加水印图片和水印相关信息，DSC服务对图片加完水印后返回给用户已嵌入水印的图片二进制流，目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='CreateImageWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image_watermark_by_address_async(self, request):
        """图片嵌入暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的图片嵌入文字暗水印或者图片暗水印，已嵌入的水印的图片将存放在用户指定的位置（目前支持华为云OBS），支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='CreateImageWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_product_order_async(self, request):
        """实例下单

        根据计费方式、计费周期等信息进行实例下单
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateProductOrder
        :type request: :class:`huaweicloudsdkdsc.v1.CreateProductOrderRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateProductOrderResponse`
        """
        return self.create_product_order_with_http_info(request)

    def create_product_order_with_http_info(self, request):
        all_params = ['create_product_order_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/period/order',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProductOrderResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_bucket_async(self, request):
        """删除资产授权

        删除数据资产扫描授权
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBucket
        :type request: :class:`huaweicloudsdkdsc.v1.DeleteBucketRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.DeleteBucketResponse`
        """
        return self.delete_bucket_with_http_info(request)

    def delete_bucket_with_http_info(self, request):
        all_params = ['bucket_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucket_id'] = local_var_params['bucket_id']

        query_params = []

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
            resource_path='/v1/{project_id}/sdg/asset/obs/bucket/{bucket_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule_async(self, request):
        """删除扫描规则

        删除指定的敏感数据识别规则
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkdsc.v1.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.DeleteRuleResponse`
        """
        return self.delete_rule_with_http_info(request)

    def delete_rule_with_http_info(self, request):
        all_params = ['rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

        query_params = []

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
            resource_path='/v1/{project_id}/sdg/server/scan/rules/{rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_rule_group_async(self, request):
        """删除扫描规则组

        根据扫描规则组ID删除指定的扫描规则组
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteRuleGroup
        :type request: :class:`huaweicloudsdkdsc.v1.DeleteRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.DeleteRuleGroupResponse`
        """
        return self.delete_rule_group_with_http_info(request)

    def delete_rule_group_with_http_info(self, request):
        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []

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
            resource_path='/v1/{project_id}/sdg/server/scan/groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteRuleGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_buckets_async(self, request):
        """查看资产列表

        查询数据资产扫描授权列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBuckets
        :type request: :class:`huaweicloudsdkdsc.v1.ListBucketsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListBucketsResponse`
        """
        return self.list_buckets_with_http_info(request)

    def list_buckets_with_http_info(self, request):
        all_params = ['added', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'added' in local_var_params:
            query_params.append(('added', local_var_params['added']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/asset/obs/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBucketsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_db_mask_task_async(self, request):
        """查询脱敏任务执行列表

        查询脱敏任务执行列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListDbMaskTask
        :type request: :class:`huaweicloudsdkdsc.v1.ListDbMaskTaskRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListDbMaskTaskResponse`
        """
        return self.list_db_mask_task_with_http_info(request)

    def list_db_mask_task_with_http_info(self, request):
        all_params = ['template_id', 'workspace_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'workspace_id' in local_var_params:
            query_params.append(('workspace_id', local_var_params['workspace_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/mask/dbs/templates/{template_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDbMaskTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relation_buckets_async(self, request):
        """OBS血缘图桶级查询

        OBS血缘图桶级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelationBuckets
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationBucketsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationBucketsResponse`
        """
        return self.list_relation_buckets_with_http_info(request)

    def list_relation_buckets_with_http_info(self, request):
        all_params = ['job_id', 'risk_start', 'risk_end', 'assets_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'assets_name' in local_var_params:
            query_params.append(('assets_name', local_var_params['assets_name']))
        if 'risk_start' in local_var_params:
            query_params.append(('risk_start', local_var_params['risk_start']))
        if 'risk_end' in local_var_params:
            query_params.append(('risk_end', local_var_params['risk_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/relation/jobs/{job_id}/obs/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelationBucketsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relation_column_async(self, request):
        """数据库血缘图表字段级查询

        数据库血缘图表字段级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelationColumn
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationColumnRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationColumnResponse`
        """
        return self.list_relation_column_with_http_info(request)

    def list_relation_column_with_http_info(self, request):
        all_params = ['job_id', 'table_id', 'risk_start', 'risk_end', 'assets_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

        query_params = []
        if 'assets_name' in local_var_params:
            query_params.append(('assets_name', local_var_params['assets_name']))
        if 'risk_start' in local_var_params:
            query_params.append(('risk_start', local_var_params['risk_start']))
        if 'risk_end' in local_var_params:
            query_params.append(('risk_end', local_var_params['risk_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/relation/jobs/{job_id}/dbs/{table_id}/columns',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelationColumnResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relation_db_async(self, request):
        """数据库血缘图数据库级查询

        数据库血缘图数据库级查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelationDb
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationDbRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationDbResponse`
        """
        return self.list_relation_db_with_http_info(request)

    def list_relation_db_with_http_info(self, request):
        all_params = ['job_id', 'risk_start', 'risk_end', 'assets_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'assets_name' in local_var_params:
            query_params.append(('assets_name', local_var_params['assets_name']))
        if 'risk_start' in local_var_params:
            query_params.append(('risk_start', local_var_params['risk_start']))
        if 'risk_end' in local_var_params:
            query_params.append(('risk_end', local_var_params['risk_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/relation/jobs/{job_id}/dbs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelationDbResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relation_file_async(self, request):
        """OBS血缘图文件分页查询

        OBS血缘图文件分页查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelationFile
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationFileRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationFileResponse`
        """
        return self.list_relation_file_with_http_info(request)

    def list_relation_file_with_http_info(self, request):
        all_params = ['job_id', 'bucket_id', 'risk_start', 'risk_end', 'offset', 'size', 'assets_name', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'bucket_id' in local_var_params:
            path_params['bucket_id'] = local_var_params['bucket_id']

        query_params = []
        if 'assets_name' in local_var_params:
            query_params.append(('assets_name', local_var_params['assets_name']))
        if 'risk_start' in local_var_params:
            query_params.append(('risk_start', local_var_params['risk_start']))
        if 'risk_end' in local_var_params:
            query_params.append(('risk_end', local_var_params['risk_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/relation/jobs/{job_id}/obs/{bucket_id}/files',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelationFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_relation_table_async(self, request):
        """数据库血缘图表分页查询

        数据库血缘图表分页查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRelationTable
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationTableRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationTableResponse`
        """
        return self.list_relation_table_with_http_info(request)

    def list_relation_table_with_http_info(self, request):
        all_params = ['job_id', 'db_id', 'risk_start', 'risk_end', 'offset', 'size', 'assets_name', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'db_id' in local_var_params:
            path_params['db_id'] = local_var_params['db_id']

        query_params = []
        if 'assets_name' in local_var_params:
            query_params.append(('assets_name', local_var_params['assets_name']))
        if 'risk_start' in local_var_params:
            query_params.append(('risk_start', local_var_params['risk_start']))
        if 'risk_end' in local_var_params:
            query_params.append(('risk_end', local_var_params['risk_end']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/relation/jobs/{job_id}/dbs/{db_id}/tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRelationTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_rule_groups_async(self, request):
        """查询扫描规则组列表

        根据指定的项目ID查询扫描规则组列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRuleGroups
        :type request: :class:`huaweicloudsdkdsc.v1.ListRuleGroupsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRuleGroupsResponse`
        """
        return self.list_rule_groups_with_http_info(request)

    def list_rule_groups_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/scan/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListRuleGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_database_water_mark_async(self, request):
        """提取数据水印

        提取请求数据中水印内容
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowDatabaseWaterMarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_doc_watermark_async(self, request):
        """文档提取暗水印

        对已嵌入文字暗水印的WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)类型的文档进行文字暗水印提取，用户以formData的格式传入待提取水印的文件，DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowDocWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_doc_watermark_by_address_async(self, request):
        """文档提取暗水印（文档地址版本）

        支持对已嵌入文字暗水印的WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)类型的文档进行水印提取，用户传入待提取水印的文档地址（目前支持OBS），DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowDocWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark_async(self, request):
        """提取图片中的文字暗水印

        对已嵌入文字暗水印的图片进行水印提取，用户以formData的格式传入待提取水印的图片，DSC服务以JSON的格式返回从图片里提取的出的文字暗水印。目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowImageWatermarkResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark_by_address_async(self, request):
        """提取图片中的文字暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的已嵌入文字暗水印的图片提取文字暗水印，支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowImageWatermarkByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark_with_image_async(self, request):
        """提取图片中的图片暗水印

        对已嵌入图片暗水印的图片进行水印提取，用户以formData的格式传入待提取水印的图片，DSC服务以图片二进制流的格式返回从图片里提取的出的图片暗水印。目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowImageWatermarkWithImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_image_watermark_with_image_by_address_async(self, request):
        """提取图片中的图片暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的已嵌入图片暗水印的图片提取图片暗水印，提取出的水印图片将存放在用户指定的位置（目前支持华为云OBS），支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowImageWatermarkWithImageByAddressResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_rules_async(self, request):
        """查看规则列表

        查询扫描规则列表，返回扫描规则总数和扫描规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowRules
        :type request: :class:`huaweicloudsdkdsc.v1.ShowRulesRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowRulesResponse`
        """
        return self.show_rules_with_http_info(request)

    def show_rules_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/server/scan/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_scan_job_results_async(self, request):
        """查询指定任务扫描结果

        查询指定任务扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowScanJobResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_scan_jobs_async(self, request):
        """查询扫描任务列表

        查询扫描任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowScanJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_specification_async(self, request):
        """查询资源开通信息

        查询资源开通信息，根据项目ID查询订单详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSpecification
        :type request: :class:`huaweicloudsdkdsc.v1.ShowSpecificationRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowSpecificationResponse`
        """
        return self.show_specification_with_http_info(request)

    def show_specification_with_http_info(self, request):
        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

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
            resource_path='/v1/{project_id}/period/product/specification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSpecificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_topics_async(self, request):
        """查询告警通知主题

        查询告警通知主题，返回默认主题、已确认主题数量及列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTopics
        :type request: :class:`huaweicloudsdkdsc.v1.ShowTopicsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowTopicsResponse`
        """
        return self.show_topics_with_http_info(request)

    def show_topics_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/sdg/smn/topics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTopicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_asset_name_async(self, request):
        """编辑资产名称

        编辑数据资产名称
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateAssetName
        :type request: :class:`huaweicloudsdkdsc.v1.UpdateAssetNameRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.UpdateAssetNameResponse`
        """
        return self.update_asset_name_with_http_info(request)

    def update_asset_name_with_http_info(self, request):
        all_params = ['asset_id', 'update_asset_name_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/sdg/asset/{asset_id}/name',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAssetNameResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_default_topic_async(self, request):
        """修改告警通知主题

        修改告警通知的关联项目ID、通知主题、通知状态(0为关闭通知，1为开启通知)等通用配置
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDefaultTopic
        :type request: :class:`huaweicloudsdkdsc.v1.UpdateDefaultTopicRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.UpdateDefaultTopicResponse`
        """
        return self.update_default_topic_with_http_info(request)

    def update_default_topic_with_http_info(self, request):
        all_params = ['update_default_topic_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            resource_path='/v1/{project_id}/sdg/smn/topic',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDefaultTopicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_open_api_called_records_async(self, request):
        """查询OpenApi调用记录

        查询OpenApi调用记录
        
        Please refer to HUAWEI cloud API Explorer for details.


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

        cname = None

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
            cname=cname,
            response_type='ShowOpenApiCalledRecordsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

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

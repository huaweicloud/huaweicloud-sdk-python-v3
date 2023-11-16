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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdsc'")


class DscClient(Client):
    def __init__(self):
        super(DscClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdsc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DscClient":
                raise TypeError("client type error, support client type is DscClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_buckets(self, request):
        """添加资产授权

        添加数据资产扫描授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddBuckets
        :type request: :class:`huaweicloudsdkdsc.v1.AddBucketsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddBucketsResponse`
        """
        http_info = self._add_buckets_http_info(request)
        return self._call_api(**http_info)

    def add_buckets_invoker(self, request):
        http_info = self._add_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_buckets_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/asset/obs/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "AddBucketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def add_rule(self, request):
        """创建扫描规则

        根据指定的规则名称、规则类型、风险等级、最小匹配次数等参数创建自定义的敏感数据识别规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRule
        :type request: :class:`huaweicloudsdkdsc.v1.AddRuleRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddRuleResponse`
        """
        http_info = self._add_rule_http_info(request)
        return self._call_api(**http_info)

    def add_rule_invoker(self, request):
        http_info = self._add_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rule_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/server/scan/rules",
            "request_type": request.__class__.__name__,
            "response_type": "AddRuleResponse"
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

    def add_rule_group(self, request):
        """创建扫描规则组

        根据指定的规则组名称和扫描规则列表创建敏感数据扫描规则组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddRuleGroup
        :type request: :class:`huaweicloudsdkdsc.v1.AddRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddRuleGroupResponse`
        """
        http_info = self._add_rule_group_http_info(request)
        return self._call_api(**http_info)

    def add_rule_group_invoker(self, request):
        http_info = self._add_rule_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_rule_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/server/scan/groups",
            "request_type": request.__class__.__name__,
            "response_type": "AddRuleGroupResponse"
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

    def add_scan_job(self, request):
        """创建扫描任务

        根据指定的任务名称、扫描方式、扫描周期、扫描规则组、扫描时间创建扫描任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddScanJob
        :type request: :class:`huaweicloudsdkdsc.v1.AddScanJobRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.AddScanJobResponse`
        """
        http_info = self._add_scan_job_http_info(request)
        return self._call_api(**http_info)

    def add_scan_job_invoker(self, request):
        http_info = self._add_scan_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _add_scan_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/scan/job",
            "request_type": request.__class__.__name__,
            "response_type": "AddScanJobResponse"
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

    def batch_add_data_mask(self, request):
        """对数据进行脱敏

        对数据进行脱敏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchAddDataMask
        :type request: :class:`huaweicloudsdkdsc.v1.BatchAddDataMaskRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.BatchAddDataMaskResponse`
        """
        http_info = self._batch_add_data_mask_http_info(request)
        return self._call_api(**http_info)

    def batch_add_data_mask_invoker(self, request):
        http_info = self._batch_add_data_mask_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_add_data_mask_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/data/mask",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAddDataMaskResponse"
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

    def change_db_template_operation(self, request):
        """开启/停止脱敏任务

        开启/停止脱敏任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeDbTemplateOperation
        :type request: :class:`huaweicloudsdkdsc.v1.ChangeDbTemplateOperationRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ChangeDbTemplateOperationResponse`
        """
        http_info = self._change_db_template_operation_http_info(request)
        return self._call_api(**http_info)

    def change_db_template_operation_invoker(self, request):
        http_info = self._change_db_template_operation_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_db_template_operation_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/server/mask/dbs/templates/{template_id}/operation",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeDbTemplateOperationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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

    def change_rule(self, request):
        """修改扫描规则

        修改自定义的敏感数据识别规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangeRule
        :type request: :class:`huaweicloudsdkdsc.v1.ChangeRuleRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ChangeRuleResponse`
        """
        http_info = self._change_rule_http_info(request)
        return self._call_api(**http_info)

    def change_rule_invoker(self, request):
        http_info = self._change_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _change_rule_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sdg/server/scan/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ChangeRuleResponse"
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

    def create_database_water_mark(self, request):
        """嵌入数据水印

        对json体中数据动态添加水印
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseWaterMark
        :type request: :class:`huaweicloudsdkdsc.v1.CreateDatabaseWaterMarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateDatabaseWaterMarkResponse`
        """
        http_info = self._create_database_water_mark_http_info(request)
        return self._call_api(**http_info)

    def create_database_water_mark_invoker(self, request):
        http_info = self._create_database_water_mark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_database_water_mark_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/database/watermark/embed",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDatabaseWaterMarkResponse"
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

    def create_doc_watermark(self, request):
        """文档嵌入水印

        对WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf) 类型的文件嵌入文字暗水印、文字明水印或者图片明水印，用户以formData的格式传入待加水印的文件和水印相关信息，DSC服务给文件加完水印后返回给用户已嵌入水印的文件的二进制流。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDocWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkResponse`
        """
        http_info = self._create_doc_watermark_http_info(request)
        return self._call_api(**http_info)

    def create_doc_watermark_invoker(self, request):
        http_info = self._create_doc_watermark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_doc_watermark_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/doc/watermark/embed",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDocWatermarkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_doc_watermark_by_address(self, request):
        """文档嵌入水印（文件地址版本）

        对WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)*类型的文档嵌入文字暗水印、文字明水印或者图片明水印，用户传入待加水印的文档地址（目前支持OBS)和水印相关信息，DSC服务对文档加完水印后返回给用户已嵌入水印的文档的存放地址。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDocWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateDocWatermarkByAddressResponse`
        """
        http_info = self._create_doc_watermark_by_address_http_info(request)
        return self._call_api(**http_info)

    def create_doc_watermark_by_address_invoker(self, request):
        http_info = self._create_doc_watermark_by_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_doc_watermark_by_address_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/doc-address/watermark/embed",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDocWatermarkByAddressResponse"
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

    def create_image_watermark(self, request):
        """图片嵌入暗水印

        对图片嵌入文字暗水印或者图片暗水印，用户以formData的格式传入待加水印图片和水印相关信息，DSC服务对图片加完水印后返回给用户已嵌入水印的图片二进制流，目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImageWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkResponse`
        """
        http_info = self._create_image_watermark_http_info(request)
        return self._call_api(**http_info)

    def create_image_watermark_invoker(self, request):
        http_info = self._create_image_watermark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_image_watermark_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image/watermark/embed",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageWatermarkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_image_watermark_by_address(self, request):
        """图片嵌入暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的图片嵌入文字暗水印或者图片暗水印，已嵌入的水印的图片将存放在用户指定的位置（目前支持华为云OBS），支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImageWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateImageWatermarkByAddressResponse`
        """
        http_info = self._create_image_watermark_by_address_http_info(request)
        return self._call_api(**http_info)

    def create_image_watermark_by_address_invoker(self, request):
        http_info = self._create_image_watermark_by_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_image_watermark_by_address_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image-address/watermark/embed",
            "request_type": request.__class__.__name__,
            "response_type": "CreateImageWatermarkByAddressResponse"
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

    def create_product_order(self, request):
        """实例下单

        根据计费方式、计费周期等信息进行实例下单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProductOrder
        :type request: :class:`huaweicloudsdkdsc.v1.CreateProductOrderRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.CreateProductOrderResponse`
        """
        http_info = self._create_product_order_http_info(request)
        return self._call_api(**http_info)

    def create_product_order_invoker(self, request):
        http_info = self._create_product_order_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_product_order_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/period/order",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProductOrderResponse"
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

    def delete_bucket(self, request):
        """删除资产授权

        删除数据资产扫描授权
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBucket
        :type request: :class:`huaweicloudsdkdsc.v1.DeleteBucketRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.DeleteBucketResponse`
        """
        http_info = self._delete_bucket_http_info(request)
        return self._call_api(**http_info)

    def delete_bucket_invoker(self, request):
        http_info = self._delete_bucket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_bucket_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sdg/asset/obs/bucket/{bucket_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBucketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket_id' in local_var_params:
            path_params['bucket_id'] = local_var_params['bucket_id']

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

    def delete_rule(self, request):
        """删除扫描规则

        删除指定的敏感数据识别规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRule
        :type request: :class:`huaweicloudsdkdsc.v1.DeleteRuleRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.DeleteRuleResponse`
        """
        http_info = self._delete_rule_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_invoker(self, request):
        http_info = self._delete_rule_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rule_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sdg/server/scan/rules/{rule_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'rule_id' in local_var_params:
            path_params['rule_id'] = local_var_params['rule_id']

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

    def delete_rule_group(self, request):
        """删除扫描规则组

        根据扫描规则组ID删除指定的扫描规则组
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteRuleGroup
        :type request: :class:`huaweicloudsdkdsc.v1.DeleteRuleGroupRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.DeleteRuleGroupResponse`
        """
        http_info = self._delete_rule_group_http_info(request)
        return self._call_api(**http_info)

    def delete_rule_group_invoker(self, request):
        http_info = self._delete_rule_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_rule_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sdg/server/scan/groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteRuleGroupResponse"
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

    def list_buckets(self, request):
        """查看资产列表

        查询数据资产扫描授权列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBuckets
        :type request: :class:`huaweicloudsdkdsc.v1.ListBucketsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListBucketsResponse`
        """
        http_info = self._list_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_buckets_invoker(self, request):
        http_info = self._list_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_buckets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/asset/obs/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListBucketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_db_mask_task(self, request):
        """查询脱敏任务执行列表

        查询脱敏任务执行列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDbMaskTask
        :type request: :class:`huaweicloudsdkdsc.v1.ListDbMaskTaskRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListDbMaskTaskResponse`
        """
        http_info = self._list_db_mask_task_http_info(request)
        return self._call_api(**http_info)

    def list_db_mask_task_invoker(self, request):
        http_info = self._list_db_mask_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_db_mask_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/mask/dbs/templates/{template_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListDbMaskTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_relation_buckets(self, request):
        """OBS血缘图桶级查询

        OBS血缘图桶级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelationBuckets
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationBucketsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationBucketsResponse`
        """
        http_info = self._list_relation_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_relation_buckets_invoker(self, request):
        http_info = self._list_relation_buckets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_relation_buckets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/relation/jobs/{job_id}/obs/buckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationBucketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_relation_column(self, request):
        """数据库血缘图表字段级查询

        数据库血缘图表字段级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelationColumn
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationColumnRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationColumnResponse`
        """
        http_info = self._list_relation_column_http_info(request)
        return self._call_api(**http_info)

    def list_relation_column_invoker(self, request):
        http_info = self._list_relation_column_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_relation_column_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/relation/jobs/{job_id}/dbs/{table_id}/columns",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationColumnResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_relation_db(self, request):
        """数据库血缘图数据库级查询

        数据库血缘图数据库级查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelationDb
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationDbRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationDbResponse`
        """
        http_info = self._list_relation_db_http_info(request)
        return self._call_api(**http_info)

    def list_relation_db_invoker(self, request):
        http_info = self._list_relation_db_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_relation_db_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/relation/jobs/{job_id}/dbs",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationDbResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_relation_file(self, request):
        """OBS血缘图文件分页查询

        OBS血缘图文件分页查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelationFile
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationFileRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationFileResponse`
        """
        http_info = self._list_relation_file_http_info(request)
        return self._call_api(**http_info)

    def list_relation_file_invoker(self, request):
        http_info = self._list_relation_file_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_relation_file_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/relation/jobs/{job_id}/obs/{bucket_id}/files",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_relation_table(self, request):
        """数据库血缘图表分页查询

        数据库血缘图表分页查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRelationTable
        :type request: :class:`huaweicloudsdkdsc.v1.ListRelationTableRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRelationTableResponse`
        """
        http_info = self._list_relation_table_http_info(request)
        return self._call_api(**http_info)

    def list_relation_table_invoker(self, request):
        http_info = self._list_relation_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_relation_table_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/relation/jobs/{job_id}/dbs/{db_id}/tables",
            "request_type": request.__class__.__name__,
            "response_type": "ListRelationTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_rule_groups(self, request):
        """查询扫描规则组列表

        根据指定的项目ID查询扫描规则组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListRuleGroups
        :type request: :class:`huaweicloudsdkdsc.v1.ListRuleGroupsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ListRuleGroupsResponse`
        """
        http_info = self._list_rule_groups_http_info(request)
        return self._call_api(**http_info)

    def list_rule_groups_invoker(self, request):
        http_info = self._list_rule_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_rule_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/scan/groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListRuleGroupsResponse"
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

    def show_database_water_mark(self, request):
        """提取数据水印

        提取请求数据中水印内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDatabaseWaterMark
        :type request: :class:`huaweicloudsdkdsc.v1.ShowDatabaseWaterMarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowDatabaseWaterMarkResponse`
        """
        http_info = self._show_database_water_mark_http_info(request)
        return self._call_api(**http_info)

    def show_database_water_mark_invoker(self, request):
        http_info = self._show_database_water_mark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_database_water_mark_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/database/watermark/extract",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDatabaseWaterMarkResponse"
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

    def show_doc_watermark(self, request):
        """文档提取暗水印

        对已嵌入文字暗水印的WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)类型的文档进行文字暗水印提取，用户以formData的格式传入待提取水印的文件，DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDocWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkResponse`
        """
        http_info = self._show_doc_watermark_http_info(request)
        return self._call_api(**http_info)

    def show_doc_watermark_invoker(self, request):
        http_info = self._show_doc_watermark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_doc_watermark_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sdg/doc/watermark/extract",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDocWatermarkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_doc_watermark_by_address(self, request):
        """文档提取暗水印（文档地址版本）

        支持对已嵌入文字暗水印的WORD(.docx)，PPT(.pptx)，EXCEL(.xlsx)，PDF(.pdf)类型的文档进行水印提取，用户传入待提取水印的文档地址（目前支持OBS），DSC服务以JSON的格式返回从文档里提取的出的文字暗水印内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDocWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowDocWatermarkByAddressResponse`
        """
        http_info = self._show_doc_watermark_by_address_http_info(request)
        return self._call_api(**http_info)

    def show_doc_watermark_by_address_invoker(self, request):
        http_info = self._show_doc_watermark_by_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_doc_watermark_by_address_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/doc-address/watermark/extract",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDocWatermarkByAddressResponse"
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

    def show_image_watermark(self, request):
        """提取图片中的文字暗水印

        对已嵌入文字暗水印的图片进行水印提取，用户以formData的格式传入待提取水印的图片，DSC服务以JSON的格式返回从图片里提取的出的文字暗水印。目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermark
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkResponse`
        """
        http_info = self._show_image_watermark_http_info(request)
        return self._call_api(**http_info)

    def show_image_watermark_invoker(self, request):
        http_info = self._show_image_watermark_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_image_watermark_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image/watermark/extract",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageWatermarkResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_image_watermark_by_address(self, request):
        """提取图片中的文字暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的已嵌入文字暗水印的图片提取文字暗水印，支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermarkByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkByAddressResponse`
        """
        http_info = self._show_image_watermark_by_address_http_info(request)
        return self._call_api(**http_info)

    def show_image_watermark_by_address_invoker(self, request):
        http_info = self._show_image_watermark_by_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_image_watermark_by_address_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image-address/watermark/extract",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageWatermarkByAddressResponse"
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

    def show_image_watermark_with_image(self, request):
        """提取图片中的图片暗水印

        对已嵌入图片暗水印的图片进行水印提取，用户以formData的格式传入待提取水印的图片，DSC服务以图片二进制流的格式返回从图片里提取的出的图片暗水印。目前支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermarkWithImage
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageResponse`
        """
        http_info = self._show_image_watermark_with_image_http_info(request)
        return self._call_api(**http_info)

    def show_image_watermark_with_image_invoker(self, request):
        http_info = self._show_image_watermark_with_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_image_watermark_with_image_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image/watermark/extract-image",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageWatermarkWithImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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

    def show_image_watermark_with_image_by_address(self, request):
        """提取图片中的图片暗水印（文件地址版本）

        对指定存储地址信息（目前支持华为云OBS）的已嵌入图片暗水印的图片提取图片暗水印，提取出的水印图片将存放在用户指定的位置（目前支持华为云OBS），支持的图片格式为：*.jpg, *.jpeg, *.jpe, *.png, *.bmp, *.dib, *.rle, *.tiff, *.tif, *.ppm, *.webp, *.tga, *.tpic, *.gif。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowImageWatermarkWithImageByAddress
        :type request: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageByAddressRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowImageWatermarkWithImageByAddressResponse`
        """
        http_info = self._show_image_watermark_with_image_by_address_http_info(request)
        return self._call_api(**http_info)

    def show_image_watermark_with_image_by_address_invoker(self, request):
        http_info = self._show_image_watermark_with_image_by_address_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_image_watermark_with_image_by_address_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/image-address/watermark/extract-image",
            "request_type": request.__class__.__name__,
            "response_type": "ShowImageWatermarkWithImageByAddressResponse"
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

    def show_rules(self, request):
        """查看规则列表

        查询扫描规则列表，返回扫描规则总数和扫描规则列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowRules
        :type request: :class:`huaweicloudsdkdsc.v1.ShowRulesRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowRulesResponse`
        """
        http_info = self._show_rules_http_info(request)
        return self._call_api(**http_info)

    def show_rules_invoker(self, request):
        http_info = self._show_rules_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_rules_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/server/scan/rules",
            "request_type": request.__class__.__name__,
            "response_type": "ShowRulesResponse"
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

    def show_scan_job_results(self, request):
        """查询指定任务扫描结果

        查询指定任务扫描结果
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScanJobResults
        :type request: :class:`huaweicloudsdkdsc.v1.ShowScanJobResultsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowScanJobResultsResponse`
        """
        http_info = self._show_scan_job_results_http_info(request)
        return self._call_api(**http_info)

    def show_scan_job_results_invoker(self, request):
        http_info = self._show_scan_job_results_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_scan_job_results_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/scan/job/{job_id}/results",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScanJobResultsResponse"
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

    def show_scan_jobs(self, request):
        """查询扫描任务列表

        查询扫描任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScanJobs
        :type request: :class:`huaweicloudsdkdsc.v1.ShowScanJobsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowScanJobsResponse`
        """
        http_info = self._show_scan_jobs_http_info(request)
        return self._call_api(**http_info)

    def show_scan_jobs_invoker(self, request):
        http_info = self._show_scan_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_scan_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/scan/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScanJobsResponse"
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
        if 'content' in local_var_params:
            query_params.append(('content', local_var_params['content']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_specification(self, request):
        """查询资源开通信息

        查询资源开通信息，根据项目ID查询订单详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSpecification
        :type request: :class:`huaweicloudsdkdsc.v1.ShowSpecificationRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowSpecificationResponse`
        """
        http_info = self._show_specification_http_info(request)
        return self._call_api(**http_info)

    def show_specification_invoker(self, request):
        http_info = self._show_specification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_specification_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/period/product/specification",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSpecificationResponse"
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

    def show_topics(self, request):
        """查询告警通知主题

        查询告警通知主题，返回默认主题、已确认主题数量及列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTopics
        :type request: :class:`huaweicloudsdkdsc.v1.ShowTopicsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowTopicsResponse`
        """
        http_info = self._show_topics_http_info(request)
        return self._call_api(**http_info)

    def show_topics_invoker(self, request):
        http_info = self._show_topics_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_topics_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sdg/smn/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTopicsResponse"
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

    def update_asset_name(self, request):
        """编辑资产名称

        编辑数据资产名称
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssetName
        :type request: :class:`huaweicloudsdkdsc.v1.UpdateAssetNameRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.UpdateAssetNameResponse`
        """
        http_info = self._update_asset_name_http_info(request)
        return self._call_api(**http_info)

    def update_asset_name_invoker(self, request):
        http_info = self._update_asset_name_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_asset_name_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sdg/asset/{asset_id}/name",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAssetNameResponse"
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

    def update_default_topic(self, request):
        """修改告警通知主题

        修改告警通知的关联项目ID、通知主题、通知状态(0为关闭通知，1为开启通知)等通用配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDefaultTopic
        :type request: :class:`huaweicloudsdkdsc.v1.UpdateDefaultTopicRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.UpdateDefaultTopicResponse`
        """
        http_info = self._update_default_topic_http_info(request)
        return self._call_api(**http_info)

    def update_default_topic_invoker(self, request):
        http_info = self._update_default_topic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_default_topic_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sdg/smn/topic",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDefaultTopicResponse"
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

    def show_open_api_called_records(self, request):
        """查询OpenApi调用记录

        查询OpenApi调用记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOpenApiCalledRecords
        :type request: :class:`huaweicloudsdkdsc.v1.ShowOpenApiCalledRecordsRequest`
        :rtype: :class:`huaweicloudsdkdsc.v1.ShowOpenApiCalledRecordsResponse`
        """
        http_info = self._show_open_api_called_records_http_info(request)
        return self._call_api(**http_info)

    def show_open_api_called_records_invoker(self, request):
        http_info = self._show_open_api_called_records_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_open_api_called_records_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/openapi/called-records",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOpenApiCalledRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

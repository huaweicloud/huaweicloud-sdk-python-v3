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


class OcrClient(Client):
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
        super(OcrClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkocr.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "OcrClient":
            raise TypeError("client type error, support client type is OcrClient")

        return ClientBuilder(clazz)

    def recognize_auto_classification(self, request):
        """智能分类识别

        检测定位图片上指定要识别的票证（票据、证件或其他文字载体），并对其进行结构化识别。接口以列表形式返回图片上要识别票证的位置坐标、结构化识别的内容以及对应的类别。
        
        计费次数说明：
        
        只对识别成功的票证进行计费，识别失败的票证不计费。例如图片中包含三张票证，有两张识别成功，一张识别失败，此时接口计费两次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeAutoClassification
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeAutoClassificationRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeAutoClassificationResponse`
        """
        return self.recognize_auto_classification_with_http_info(request)

    def recognize_auto_classification_with_http_info(self, request):
        all_params = ['auto_classification_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/auto-classification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeAutoClassificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_bankcard(self, request):
        """银行卡识别

        识别银行卡上的关键文字信息，并返回识别的结构化结果。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeBankcard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeBankcardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeBankcardResponse`
        """
        return self.recognize_bankcard_with_http_info(request)

    def recognize_bankcard_with_http_info(self, request):
        all_params = ['bankcard_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/bankcard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeBankcardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_business_card(self, request):
        """名片识别

        识别名片图片上的文字信息，并返回识别的结构化结果。支持对多种不同版式名片进行结构化信息提取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeBusinessCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeBusinessCardResponse`
        """
        return self.recognize_business_card_with_http_info(request)

    def recognize_business_card_with_http_info(self, request):
        all_params = ['business_card_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/business-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeBusinessCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_business_license(self, request):
        """营业执照识别

        识别营业执照首页图片中的文字信息，并返回识别的结构化结果。
        
        说明： 
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeBusinessLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeBusinessLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeBusinessLicenseResponse`
        """
        return self.recognize_business_license_with_http_info(request)

    def recognize_business_license_with_http_info(self, request):
        all_params = ['business_license_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/business-license',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeBusinessLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_cambodian_id_card(self, request):
        """柬文身份证识别

        识别柬文身份证图片中的文字内容，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeCambodianIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeCambodianIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeCambodianIdCardResponse`
        """
        return self.recognize_cambodian_id_card_with_http_info(request)

    def recognize_cambodian_id_card_with_http_info(self, request):
        all_params = ['cambodian_id_card_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/cambodian-idcard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeCambodianIdCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_chile_id_card(self, request):
        """智利身份证识别

        识别智利身份证图片中的文字内容，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeChileIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeChileIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeChileIdCardResponse`
        """
        return self.recognize_chile_id_card_with_http_info(request)

    def recognize_chile_id_card_with_http_info(self, request):
        all_params = ['chile_id_card_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/chile-id-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeChileIdCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_driver_license(self, request):
        """驾驶证识别

        识别用户上传的驾驶证图片（或者用户提供的华为云上OBS的驾驶证图片文件的URL）中主页与副页的文字内容，并将识别的结果返回给用户。
        
        说明： 
        
        如果图片中包含多张卡证票据，请调用智能分类识别服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeDriverLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeDriverLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeDriverLicenseResponse`
        """
        return self.recognize_driver_license_with_http_info(request)

    def recognize_driver_license_with_http_info(self, request):
        all_params = ['driver_license_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/driver-license',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeDriverLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_exit_entry_permit(self, request):
        """往来港澳台通行证识别

        识别往来港澳台证件图片中的文字内容，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeExitEntryPermit
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeExitEntryPermitRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeExitEntryPermitResponse`
        """
        return self.recognize_exit_entry_permit_with_http_info(request)

    def recognize_exit_entry_permit_with_http_info(self, request):
        all_params = ['exit_entry_permit_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/exit-entry-permit',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeExitEntryPermitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_financial_statement(self, request):
        """财务报表识别

        识别用户上传的表格图片中的文字内容，并将识别的结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeFinancialStatement
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeFinancialStatementRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeFinancialStatementResponse`
        """
        return self.recognize_financial_statement_with_http_info(request)

    def recognize_financial_statement_with_http_info(self, request):
        all_params = ['financial_statement_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/financial-statement',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeFinancialStatementResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_flight_itinerary(self, request):
        """飞机行程单识别

        识别飞机行程单中的文字信息，并返回识别的结构化结果。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用智能分类识别服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeFlightItinerary
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeFlightItineraryRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeFlightItineraryResponse`
        """
        return self.recognize_flight_itinerary_with_http_info(request)

    def recognize_flight_itinerary_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'flight_itinerary_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/flight-itinerary',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeFlightItineraryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_general_table(self, request):
        """通用表格识别

        识别用于识别用户上传的通用表格图片（或者用户提供的华为云上OBS的通用表格图片文件的URL）中的文字内容，并将识别的结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeGeneralTable
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTableRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTableResponse`
        """
        return self.recognize_general_table_with_http_info(request)

    def recognize_general_table_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'general_table_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/general-table',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeGeneralTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_general_text(self, request):
        """通用文字识别

        识别图片上的文字信息，返回识别的文字和坐标。支持扫描文件、电子文档、书籍、票据和表单等多种场景的文字识别。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeGeneralText
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTextRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTextResponse`
        """
        return self.recognize_general_text_with_http_info(request)

    def recognize_general_text_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'general_text_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/general-text',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeGeneralTextResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_handwriting(self, request):
        """手写文字识别

        识别文档中的手写文字信息，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeHandwriting
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeHandwritingRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeHandwritingResponse`
        """
        return self.recognize_handwriting_with_http_info(request)

    def recognize_handwriting_with_http_info(self, request):
        all_params = ['handwriting_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/handwriting',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeHandwritingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_health_code(self, request):
        """防疫健康码识别

        支持对全国各地区不同版式的防疫健康码、核酸检测记录、行程卡中的14个关键字段进行结构化识别；支持识别4种健康码颜色，包括绿码、黄码、红码、灰码；支持返回各个关键字段的置信度，以便提高人工校验效率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeHealthCode
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeHealthCodeRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeHealthCodeResponse`
        """
        return self.recognize_health_code_with_http_info(request)

    def recognize_health_code_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'health_code_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/health-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeHealthCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_hk_id_card(self, request):
        """香港身份证识别

        识别香港身份证中的文字内容，并将识别的结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeHkIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeHkIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeHkIdCardResponse`
        """
        return self.recognize_hk_id_card_with_http_info(request)

    def recognize_hk_id_card_with_http_info(self, request):
        all_params = ['hk_id_card_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/hk-id-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeHkIdCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_id_card(self, request):
        """身份证识别

        识别身份证图片中的文字内容，并将识别的结果返回给用户。
        
        说明： 
        
        身份证识别支持中华人民共和国居民身份证识别。
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeIdCardResponse`
        """
        return self.recognize_id_card_with_http_info(request)

    def recognize_id_card_with_http_info(self, request):
        all_params = ['id_card_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/id-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeIdCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_id_document(self, request):
        """通用证件识别

        识别身份证件图像，并将识别的结构化结果返回给用户。支持多个国家/地区的身份证、驾驶证和护照，具体国家/地区和证件列表详见表1国家/地区和证件列表。
        
        **表1国家/地区和证件列表**
        
        | 国家/地区  | 英文名称    | 国家/地区代码 country_region | 支持证件类型 id_type      |
        | ---------- | ----------- | ---------------------------- | ------------------------- |
        | 越南       | Vietnam     | VNM                          | PP、DL、ID                |
        | 印度       | India       | IND                          | PP                        |
        | 菲律宾     | Philippines | PHL                          | PP、DL、ID（仅支持UUMID） |
        | 阿尔巴尼亚 | Albania     | ALB                          | PP、DL、ID                |
        | 巴西       | BRAZIL      | BRA                          | PP                        |
        | 印度尼西亚 | INDONESIA   | IDN                          | PP                        |
        | 马来西亚   | MALAYSIA    | MYS                          | PP                        |
        | 尼日利亚   | NIGERIA     | NGA                          | PP                        |
        | 巴基斯坦   | PAKISTAN    | PAK                          | PP                        |
        | 俄罗斯     | RUSSIA      | RUS                          | PP（仅支持国际标准版本）  |
        | 中国台湾   | TAIWAN      | TWN                          | PP                        |
        | 乌克兰     | UKRAINE     | UKR                          | PP                        |
        | 泰国       | THAILAND    | THA                          | ID、PP                    |
        | 智利       | CHILE       | CHL                          | ID、PP                    |
        | 中国香港   | HONGKONG    | HKG                          | ID                        |
        
        - PP: passport,国际护照
        - DL: driving license,驾驶证
        - ID: identification card,各国颁发的身份证类型证件，比如身份证、选民证、社保卡等。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeIdDocument
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeIdDocumentRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeIdDocumentResponse`
        """
        return self.recognize_id_document_with_http_info(request)

    def recognize_id_document_with_http_info(self, request):
        all_params = ['id_document_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/id-document',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeIdDocumentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_insurance_policy(self, request):
        """保险单识别

        识别保险单图片上的文字信息，并将识别的结构化结果返回给用户。支持对多板式保险单的扫描图片及手机照片进行结构化信息提取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeInsurancePolicy
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeInsurancePolicyRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeInsurancePolicyResponse`
        """
        return self.recognize_insurance_policy_with_http_info(request)

    def recognize_insurance_policy_with_http_info(self, request):
        all_params = ['insurance_policy_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/insurance-policy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeInsurancePolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_invoice_verification(self, request):
        """发票验真

        发票验真服务支持10种增值税发票的信息核验，包括增值税专用发票、增值税普通发票、增值税普通发票（卷式）、增值税电子专用发票、增值税电子普通发票、增值税电子普通发票（通行费）、二手车销售统一发票、机动车销售统一发票、区块链电子发票、全电发票，支持返回票面的全部信息。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeInvoiceVerification
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeInvoiceVerificationRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeInvoiceVerificationResponse`
        """
        return self.recognize_invoice_verification_with_http_info(request)

    def recognize_invoice_verification_with_http_info(self, request):
        all_params = ['invoice_verification_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/invoice-verification',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeInvoiceVerificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_license_plate(self, request):
        """车牌识别

        识别输入图片中的车牌信息，并返回其坐标和内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeLicensePlate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeLicensePlateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeLicensePlateResponse`
        """
        return self.recognize_license_plate_with_http_info(request)

    def recognize_license_plate_with_http_info(self, request):
        all_params = ['license_plate_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/license-plate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeLicensePlateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_macao_id_card(self, request):
        """澳门身份证识别

        识别澳门身份证图片中的文字内容，并将识别的结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMacaoIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMacaoIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMacaoIdCardResponse`
        """
        return self.recognize_macao_id_card_with_http_info(request)

    def recognize_macao_id_card_with_http_info(self, request):
        all_params = ['macao_id_card_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/macao-id-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeMacaoIdCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_mainland_travel_permit(self, request):
        """港澳台居民来往内地通行证识别

        识别港澳居民来往内地通行证上的文字内容，并将识别的结构化结果返回给用户。支持港澳居民来往内地通行证和台湾居民来往内地通行证两种卡证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMainlandTravelPermit
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMainlandTravelPermitRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMainlandTravelPermitResponse`
        """
        return self.recognize_mainland_travel_permit_with_http_info(request)

    def recognize_mainland_travel_permit_with_http_info(self, request):
        all_params = ['mainland_travel_permit_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/mainland-travel-permit',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeMainlandTravelPermitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_mvs_invoice(self, request):
        """机动车销售发票识别

        识别机动车销售发票图片中的文字内容，并将识别的结果返回给用户。
        
        说明：
        
        该增值税发票仅限于中华人民共和国境内使用的增值税发票。
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMvsInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMvsInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMvsInvoiceResponse`
        """
        return self.recognize_mvs_invoice_with_http_info(request)

    def recognize_mvs_invoice_with_http_info(self, request):
        all_params = ['mvs_invoice_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/mvs-invoice',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeMvsInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_myanmar_driver_license(self, request):
        """缅文驾驶证识别

        识别缅甸驾驶证中的文字信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMyanmarDriverLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarDriverLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarDriverLicenseResponse`
        """
        return self.recognize_myanmar_driver_license_with_http_info(request)

    def recognize_myanmar_driver_license_with_http_info(self, request):
        all_params = ['myanmar_driver_license_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/myanmar-driver-license',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeMyanmarDriverLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_myanmar_idcard(self, request):
        """缅文身份证识别

        识别缅文身份证中的文字信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMyanmarIdcard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarIdcardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarIdcardResponse`
        """
        return self.recognize_myanmar_idcard_with_http_info(request)

    def recognize_myanmar_idcard_with_http_info(self, request):
        all_params = ['myanmar_idcard_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/myanmar-id-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeMyanmarIdcardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_passport(self, request):
        """护照识别

        识别用户上传的护照首页图片中的文字信息，并返回识别的结构化结果。当前版本支持中国护照的全字段识别。外国护照支持护照下方两行国际标准化的机读码识别，并可从中提取6-7个关键字段信息。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizePassport
        :type request: :class:`huaweicloudsdkocr.v1.RecognizePassportRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizePassportResponse`
        """
        return self.recognize_passport_with_http_info(request)

    def recognize_passport_with_http_info(self, request):
        all_params = ['passport_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/passport',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizePassportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_pcr_test_record(self, request):
        """核酸检测记录识别

        识别核酸检测记录中的文字信息，并将识别的结构化结果返回给用户。PCR，全称Polymerase chain reaction,即聚合酶链式反应.PCR-test也为大众所认知为新型冠状病毒核酸检测测试。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizePcrTestRecord
        :type request: :class:`huaweicloudsdkocr.v1.RecognizePcrTestRecordRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizePcrTestRecordResponse`
        """
        return self.recognize_pcr_test_record_with_http_info(request)

    def recognize_pcr_test_record_with_http_info(self, request):
        all_params = ['enterprise_project_id', 'pcr_test_record_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/pcr-test-record',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizePcrTestRecordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_qualification_certificate(self, request):
        """道路运输从业资格证识别

        识别道路运输从业资格证上的关键文字信息，并返回识别的结构化结果。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeQualificationCertificate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeQualificationCertificateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeQualificationCertificateResponse`
        """
        return self.recognize_qualification_certificate_with_http_info(request)

    def recognize_qualification_certificate_with_http_info(self, request):
        all_params = ['qualification_certificate_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/transportation-qualification-certificate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeQualificationCertificateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_quota_invoice(self, request):
        """定额发票识别

        识别定额发票中的文字信息，并返回识别的结构化结果。
        
        说明： 
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeQuotaInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeQuotaInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeQuotaInvoiceResponse`
        """
        return self.recognize_quota_invoice_with_http_info(request)

    def recognize_quota_invoice_with_http_info(self, request):
        all_params = ['quota_invoice_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/quota-invoice',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeQuotaInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_taxi_invoice(self, request):
        """出租车发票识别

        识别出租车发票中的文字信息，并返回识别的结构化结果。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用智能分类识别服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTaxiInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTaxiInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTaxiInvoiceResponse`
        """
        return self.recognize_taxi_invoice_with_http_info(request)

    def recognize_taxi_invoice_with_http_info(self, request):
        all_params = ['taxi_invoice_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/taxi-invoice',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeTaxiInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_thailand_idcard(self, request):
        """泰文身份证识别

        识别泰国身份证中的文字信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeThailandIdcard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeThailandIdcardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeThailandIdcardResponse`
        """
        return self.recognize_thailand_idcard_with_http_info(request)

    def recognize_thailand_idcard_with_http_info(self, request):
        all_params = ['thailand_idcard_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/thailand-id-card',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeThailandIdcardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_thailand_license_plate(self, request):
        """泰国车牌识别

        识别泰国车牌图片中的车牌信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeThailandLicensePlate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeThailandLicensePlateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeThailandLicensePlateResponse`
        """
        return self.recognize_thailand_license_plate_with_http_info(request)

    def recognize_thailand_license_plate_with_http_info(self, request):
        all_params = ['thailand_license_plate_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/thailand-license-plate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeThailandLicensePlateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_toll_invoice(self, request):
        """车辆通行费发票识别

        识别车辆通行费发票中的文字信息，并返回识别的结构化结果。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTollInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTollInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTollInvoiceResponse`
        """
        return self.recognize_toll_invoice_with_http_info(request)

    def recognize_toll_invoice_with_http_info(self, request):
        all_params = ['toll_invoice_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/toll-invoice',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeTollInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_train_ticket(self, request):
        """火车票识别

        识别火车票中的文字信息，并返回识别的结构化结果。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTrainTicket
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTrainTicketRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTrainTicketResponse`
        """
        return self.recognize_train_ticket_with_http_info(request)

    def recognize_train_ticket_with_http_info(self, request):
        all_params = ['train_ticket_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/train-ticket',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeTrainTicketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_transportation_license(self, request):
        """道路运输证识别

        识别道路运输证首页中的文字信息，并返回识别的结构化结果。
        
        说明： 如果图片中包含多张卡证票据，请调用智能分类识别服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTransportationLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTransportationLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTransportationLicenseResponse`
        """
        return self.recognize_transportation_license_with_http_info(request)

    def recognize_transportation_license_with_http_info(self, request):
        all_params = ['transportation_license_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/transportation-license',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeTransportationLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_vat_invoice(self, request):
        """增值税发票识别

        识别增值税发票的类别，以及图片中的文字内容，并以json格式返回识别的结构化结果，不支持真伪验证。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section15)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        说明：
        
        该增值税发票仅限于中华人民共和国境内使用的增值税发票。
        
        支持的增值税发票包括：增值税专用发票、增值税普通发票、增值税电子普通发票、增值税电子专用发票、增值税电子普通发票（通行费）、增值税普通发票（卷票）。
        
        如果图片中包含多张卡证票据，请调用智能分类识别服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVatInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVatInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVatInvoiceResponse`
        """
        return self.recognize_vat_invoice_with_http_info(request)

    def recognize_vat_invoice_with_http_info(self, request):
        all_params = ['vat_invoice_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/vat-invoice',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeVatInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_vehicle_license(self, request):
        """行驶证识别

        识别用户上传的行驶证图片（或者用户提供的华为云上OBS的行驶证图片文件的URL）中主页和副页的文字内容，并将识别的结果返回给用户。
        
        说明：
        
        如果图片中包含多张卡证票据，请调用智能分类识别服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVehicleLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVehicleLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVehicleLicenseResponse`
        """
        return self.recognize_vehicle_license_with_http_info(request)

    def recognize_vehicle_license_with_http_info(self, request):
        all_params = ['vehicle_license_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/vehicle-license',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeVehicleLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_waybill_electronic(self, request):
        """电子面单识别

        识别用户上传的韵达电子面单图片中的文字内容，并将识别的结果以json格式返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeWaybillElectronic
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeWaybillElectronicRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeWaybillElectronicResponse`
        """
        return self.recognize_waybill_electronic_with_http_info(request)

    def recognize_waybill_electronic_with_http_info(self, request):
        all_params = ['waybill_electronic_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/waybill-electronic',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeWaybillElectronicResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_web_image(self, request):
        """网络图片识别

        识别网络图片中的文字内容，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeWebImage
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeWebImageRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeWebImageResponse`
        """
        return self.recognize_web_image_with_http_info(request)

    def recognize_web_image_with_http_info(self, request):
        all_params = ['web_image_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/web-image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeWebImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_vin(self, request):
        """VIN码识别

        识别图片中的车架号信息，并将识别结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVin
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVinRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVinResponse`
        """
        return self.recognize_vin_with_http_info(request)

    def recognize_vin_with_http_info(self, request):
        all_params = ['vin_request_body', 'enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/ocr/vin',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeVinResponse',
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

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

        检测定位图片上指定要识别的票证（票据、证件或其他文字载体），并对其进行结构化识别。接口以列表形式返回图片上要识别票证的位置坐标、结构化识别的内容以及对应的类别。  计费次数说明：  只对识别成功的票证进行计费，识别失败的票证不计费。例如图片中包含三张票证，有两张识别成功，一张识别失败，此时接口计费两次。 

        :param RecognizeAutoClassificationRequest request
        :return: RecognizeAutoClassificationResponse
        """
        return self.recognize_auto_classification_with_http_info(request)

    def recognize_auto_classification_with_http_info(self, request):
        """智能分类识别

        检测定位图片上指定要识别的票证（票据、证件或其他文字载体），并对其进行结构化识别。接口以列表形式返回图片上要识别票证的位置坐标、结构化识别的内容以及对应的类别。  计费次数说明：  只对识别成功的票证进行计费，识别失败的票证不计费。例如图片中包含三张票证，有两张识别成功，一张识别失败，此时接口计费两次。 

        :param RecognizeAutoClassificationRequest request
        :return: RecognizeAutoClassificationResponse
        """

        all_params = ['project_id', 'auto_classification_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeAutoClassificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_bankcard(self, request):
        """银行卡识别

        识别银行卡上的关键文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeBankcardRequest request
        :return: RecognizeBankcardResponse
        """
        return self.recognize_bankcard_with_http_info(request)

    def recognize_bankcard_with_http_info(self, request):
        """银行卡识别

        识别银行卡上的关键文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeBankcardRequest request
        :return: RecognizeBankcardResponse
        """

        all_params = ['project_id', 'bank_card_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeBankcardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_business_card(self, request):
        """名片识别

        识别名片图片上的文字信息，并返回识别的结构化结果。支持对多种不同版式名片进行结构化信息提取。

        :param RecognizeBusinessCardRequest request
        :return: RecognizeBusinessCardResponse
        """
        return self.recognize_business_card_with_http_info(request)

    def recognize_business_card_with_http_info(self, request):
        """名片识别

        识别名片图片上的文字信息，并返回识别的结构化结果。支持对多种不同版式名片进行结构化信息提取。

        :param RecognizeBusinessCardRequest request
        :return: RecognizeBusinessCardResponse
        """

        all_params = ['project_id', 'business_card_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeBusinessCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_business_license(self, request):
        """营业执照识别

        识别营业执照首页图片中的文字信息，并返回识别的结构化结果。  说明：   如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeBusinessLicenseRequest request
        :return: RecognizeBusinessLicenseResponse
        """
        return self.recognize_business_license_with_http_info(request)

    def recognize_business_license_with_http_info(self, request):
        """营业执照识别

        识别营业执照首页图片中的文字信息，并返回识别的结构化结果。  说明：   如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeBusinessLicenseRequest request
        :return: RecognizeBusinessLicenseResponse
        """

        all_params = ['project_id', 'bankcard_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeBusinessLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_driver_license(self, request):
        """驾驶证识别

        识别用户上传的驾驶证图片（或者用户提供的华为云上OBS的驾驶证图片文件的URL）中主页与副页的文字内容，并将识别的结果返回给用户。  说明：   如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeDriverLicenseRequest request
        :return: RecognizeDriverLicenseResponse
        """
        return self.recognize_driver_license_with_http_info(request)

    def recognize_driver_license_with_http_info(self, request):
        """驾驶证识别

        识别用户上传的驾驶证图片（或者用户提供的华为云上OBS的驾驶证图片文件的URL）中主页与副页的文字内容，并将识别的结果返回给用户。  说明：   如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeDriverLicenseRequest request
        :return: RecognizeDriverLicenseResponse
        """

        all_params = ['project_id', 'driver_license_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeDriverLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_flight_itinerary(self, request):
        """飞机行程单识别

        识别飞机行程单中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeFlightItineraryRequest request
        :return: RecognizeFlightItineraryResponse
        """
        return self.recognize_flight_itinerary_with_http_info(request)

    def recognize_flight_itinerary_with_http_info(self, request):
        """飞机行程单识别

        识别飞机行程单中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeFlightItineraryRequest request
        :return: RecognizeFlightItineraryResponse
        """

        all_params = ['project_id', 'flight_itinerary_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeFlightItineraryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_general_table(self, request):
        """通用表格识别

        识别用于识别用户上传的通用表格图片（或者用户提供的华为云上OBS的通用表格图片文件的URL）中的文字内容，并将识别的结果返回给用户。

        :param RecognizeGeneralTableRequest request
        :return: RecognizeGeneralTableResponse
        """
        return self.recognize_general_table_with_http_info(request)

    def recognize_general_table_with_http_info(self, request):
        """通用表格识别

        识别用于识别用户上传的通用表格图片（或者用户提供的华为云上OBS的通用表格图片文件的URL）中的文字内容，并将识别的结果返回给用户。

        :param RecognizeGeneralTableRequest request
        :return: RecognizeGeneralTableResponse
        """

        all_params = ['project_id', 'general_table_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeGeneralTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_general_text(self, request):
        """通用文字识别

        识别图片上的文字信息，返回识别的文字和坐标。支持扫描文件、电子文档、书籍、票据和表单等多种场景的文字识别。

        :param RecognizeGeneralTextRequest request
        :return: RecognizeGeneralTextResponse
        """
        return self.recognize_general_text_with_http_info(request)

    def recognize_general_text_with_http_info(self, request):
        """通用文字识别

        识别图片上的文字信息，返回识别的文字和坐标。支持扫描文件、电子文档、书籍、票据和表单等多种场景的文字识别。

        :param RecognizeGeneralTextRequest request
        :return: RecognizeGeneralTextResponse
        """

        all_params = ['project_id', 'general_text_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeGeneralTextResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_handwriting(self, request):
        """手写文字识别

        识别文档中的手写文字信息，并将识别的结构化结果返回给用户。

        :param RecognizeHandwritingRequest request
        :return: RecognizeHandwritingResponse
        """
        return self.recognize_handwriting_with_http_info(request)

    def recognize_handwriting_with_http_info(self, request):
        """手写文字识别

        识别文档中的手写文字信息，并将识别的结构化结果返回给用户。

        :param RecognizeHandwritingRequest request
        :return: RecognizeHandwritingResponse
        """

        all_params = ['project_id', 'handwriting_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeHandwritingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_id_card(self, request):
        """身份证识别

        识别身份证图片中的文字内容，并将识别的结果返回给用户。  说明：   身份证识别只支持中国大陆汉族身份证识别。  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeIDCardRequest request
        :return: RecognizeIDCardResponse
        """
        return self.recognize_id_card_with_http_info(request)

    def recognize_id_card_with_http_info(self, request):
        """身份证识别

        识别身份证图片中的文字内容，并将识别的结果返回给用户。  说明：   身份证识别只支持中国大陆汉族身份证识别。  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeIDCardRequest request
        :return: RecognizeIDCardResponse
        """

        all_params = ['project_id', 'id_card_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeIDCardResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_license_plate(self, request):
        """车牌识别

        识别输入图片中的车牌信息，并返回其坐标和内容。 

        :param RecognizeLicensePlateRequest request
        :return: RecognizeLicensePlateResponse
        """
        return self.recognize_license_plate_with_http_info(request)

    def recognize_license_plate_with_http_info(self, request):
        """车牌识别

        识别输入图片中的车牌信息，并返回其坐标和内容。 

        :param RecognizeLicensePlateRequest request
        :return: RecognizeLicensePlateResponse
        """

        all_params = ['project_id', 'license_plate_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeLicensePlateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_mvs_invoice(self, request):
        """机动车销售发票识别

        识别机动车销售发票图片中的文字内容，并将识别的结果返回给用户。  说明：  该增值税发票仅限于中华人民共和国境内使用的增值税发票。  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeMvsInvoiceRequest request
        :return: RecognizeMvsInvoiceResponse
        """
        return self.recognize_mvs_invoice_with_http_info(request)

    def recognize_mvs_invoice_with_http_info(self, request):
        """机动车销售发票识别

        识别机动车销售发票图片中的文字内容，并将识别的结果返回给用户。  说明：  该增值税发票仅限于中华人民共和国境内使用的增值税发票。  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeMvsInvoiceRequest request
        :return: RecognizeMvsInvoiceResponse
        """

        all_params = ['project_id', 'mvs_invoice_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeMvsInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_passport(self, request):
        """护照识别

        识别用户上传的护照首页图片中的文字信息，并返回识别的结构化结果。当前版本支持中国护照的全字段识别。外国护照支持护照下方两行国际标准化的机读码识别，并可从中提取6-7个关键字段信息。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizePassportRequest request
        :return: RecognizePassportResponse
        """
        return self.recognize_passport_with_http_info(request)

    def recognize_passport_with_http_info(self, request):
        """护照识别

        识别用户上传的护照首页图片中的文字信息，并返回识别的结构化结果。当前版本支持中国护照的全字段识别。外国护照支持护照下方两行国际标准化的机读码识别，并可从中提取6-7个关键字段信息。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizePassportRequest request
        :return: RecognizePassportResponse
        """

        all_params = ['project_id', 'passport_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizePassportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_quota_invoice(self, request):
        """定额发票识别

        识别定额发票中的文字信息，并返回识别的结构化结果。  说明：   如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeQuotaInvoiceRequest request
        :return: RecognizeQuotaInvoiceResponse
        """
        return self.recognize_quota_invoice_with_http_info(request)

    def recognize_quota_invoice_with_http_info(self, request):
        """定额发票识别

        识别定额发票中的文字信息，并返回识别的结构化结果。  说明：   如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeQuotaInvoiceRequest request
        :return: RecognizeQuotaInvoiceResponse
        """

        all_params = ['project_id', 'train_ticket_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeQuotaInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_taxi_invoice(self, request):
        """出租车发票识别

        识别出租车发票中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeTaxiInvoiceRequest request
        :return: RecognizeTaxiInvoiceResponse
        """
        return self.recognize_taxi_invoice_with_http_info(request)

    def recognize_taxi_invoice_with_http_info(self, request):
        """出租车发票识别

        识别出租车发票中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeTaxiInvoiceRequest request
        :return: RecognizeTaxiInvoiceResponse
        """

        all_params = ['project_id', 'taxi_invoice_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeTaxiInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_toll_invoice(self, request):
        """车辆通行费发票识别

        识别车辆通行费发票中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeTollInvoiceRequest request
        :return: RecognizeTollInvoiceResponse
        """
        return self.recognize_toll_invoice_with_http_info(request)

    def recognize_toll_invoice_with_http_info(self, request):
        """车辆通行费发票识别

        识别车辆通行费发票中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeTollInvoiceRequest request
        :return: RecognizeTollInvoiceResponse
        """

        all_params = ['project_id', 'recognize_toll_invoice_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeTollInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_train_ticket(self, request):
        """火车票识别

        识别火车票中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeTrainTicketRequest request
        :return: RecognizeTrainTicketResponse
        """
        return self.recognize_train_ticket_with_http_info(request)

    def recognize_train_ticket_with_http_info(self, request):
        """火车票识别

        识别火车票中的文字信息，并返回识别的结构化结果。  说明：  如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=OCR&api=AutoClassification)服务。 

        :param RecognizeTrainTicketRequest request
        :return: RecognizeTrainTicketResponse
        """

        all_params = ['project_id', 'train_ticket_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeTrainTicketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_transportation_license(self, request):
        """道路运输证识别

        识别道路运输证首页中的文字信息，并返回识别的结构化结果。  说明： 如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeTransportationLicenseRequest request
        :return: RecognizeTransportationLicenseResponse
        """
        return self.recognize_transportation_license_with_http_info(request)

    def recognize_transportation_license_with_http_info(self, request):
        """道路运输证识别

        识别道路运输证首页中的文字信息，并返回识别的结构化结果。  说明： 如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeTransportationLicenseRequest request
        :return: RecognizeTransportationLicenseResponse
        """

        all_params = ['project_id', 'transportation_license_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeTransportationLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_vat_invoice(self, request):
        """增值税发票识别

        识别用户上传的增值税发票图片（或者用户提供的华为云上OBS的增值税发票图片文件的URL）中的文字内容，并将识别的结果返回给用户。  说明：  该增值税发票仅限于中华人民共和国境内使用的增值税发票。  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeVatInvoiceRequest request
        :return: RecognizeVatInvoiceResponse
        """
        return self.recognize_vat_invoice_with_http_info(request)

    def recognize_vat_invoice_with_http_info(self, request):
        """增值税发票识别

        识别用户上传的增值税发票图片（或者用户提供的华为云上OBS的增值税发票图片文件的URL）中的文字内容，并将识别的结果返回给用户。  说明：  该增值税发票仅限于中华人民共和国境内使用的增值税发票。  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeVatInvoiceRequest request
        :return: RecognizeVatInvoiceResponse
        """

        all_params = ['project_id', 'recognize_vat_invoice_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeVatInvoiceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_vehicle_license(self, request):
        """行驶证识别

        识别用户上传的行驶证图片（或者用户提供的华为云上OBS的行驶证图片文件的URL）中主页和副页的文字内容，并将识别的结果返回给用户。  说明：  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeVehicleLicenseRequest request
        :return: RecognizeVehicleLicenseResponse
        """
        return self.recognize_vehicle_license_with_http_info(request)

    def recognize_vehicle_license_with_http_info(self, request):
        """行驶证识别

        识别用户上传的行驶证图片（或者用户提供的华为云上OBS的行驶证图片文件的URL）中主页和副页的文字内容，并将识别的结果返回给用户。  说明：  如果图片中包含多张卡证票据，请调用智能分类识别服务。 

        :param RecognizeVehicleLicenseRequest request
        :return: RecognizeVehicleLicenseResponse
        """

        all_params = ['project_id', 'recognize_vehicle_license_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeVehicleLicenseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_web_image(self, request):
        """网络图片识别

        识别网络图片中的文字内容，并返回识别的结构化结果。

        :param RecognizeWebImageRequest request
        :return: RecognizeWebImageResponse
        """
        return self.recognize_web_image_with_http_info(request)

    def recognize_web_image_with_http_info(self, request):
        """网络图片识别

        识别网络图片中的文字内容，并返回识别的结构化结果。

        :param RecognizeWebImageRequest request
        :return: RecognizeWebImageResponse
        """

        all_params = ['project_id', 'recognize_web_image_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeWebImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def recognize_vin(self, request):
        """VIN码识别

        识别图片中的车架号信息，并将识别结果返回给用户。 

        :param RecognizeVINRequest request
        :return: RecognizeVINResponse
        """
        return self.recognize_vin_with_http_info(request)

    def recognize_vin_with_http_info(self, request):
        """VIN码识别

        识别图片中的车架号信息，并将识别结果返回给用户。 

        :param RecognizeVINRequest request
        :return: RecognizeVINResponse
        """

        all_params = ['project_id', 'recognize_vin_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            response_type='RecognizeVINResponse',
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

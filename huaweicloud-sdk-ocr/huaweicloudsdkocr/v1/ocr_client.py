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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkocr'")


class OcrClient(Client):
    def __init__(self):
        super(OcrClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkocr.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "OcrClient":
                raise TypeError("client type error, support client type is OcrClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def recognize_acceptance_bill(self, request):
        """承兑汇票识别

        识别承兑汇票中的关键信息, 并以json格式返回结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeAcceptanceBill
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeAcceptanceBillRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeAcceptanceBillResponse`
        """
        http_info = self._recognize_acceptance_bill_http_info(request)
        return self._call_api(**http_info)

    def recognize_acceptance_bill_invoker(self, request):
        http_info = self._recognize_acceptance_bill_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_acceptance_bill_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/acceptance-bill",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeAcceptanceBillResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_auto_classification(self, request):
        """智能分类识别

        检测定位图片上指定要识别的票证（票据、证件或其他文字载体），并对其进行结构化识别。接口以列表形式返回图片上要识别票证的位置坐标、结构化识别的内容以及对应的类别。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section3)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        计费次数说明：
        只对识别成功的票证进行计费，识别失败的票证不计费。例如图片中包含三张票证，有两张识别成功，一张识别失败，此时接口计费两次。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeAutoClassification
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeAutoClassificationRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeAutoClassificationResponse`
        """
        http_info = self._recognize_auto_classification_http_info(request)
        return self._call_api(**http_info)

    def recognize_auto_classification_invoker(self, request):
        http_info = self._recognize_auto_classification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_auto_classification_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/auto-classification",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeAutoClassificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_bankcard(self, request):
        """银行卡识别

        识别银行卡上的关键文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section9)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeBankcard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeBankcardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeBankcardResponse`
        """
        http_info = self._recognize_bankcard_http_info(request)
        return self._call_api(**http_info)

    def recognize_bankcard_invoker(self, request):
        http_info = self._recognize_bankcard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_bankcard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/bankcard",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeBankcardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_business_card(self, request):
        """名片识别

        识别名片图片上的文字信息，并返回识别的结构化结果。支持对多种不同版式名片进行结构化信息提取。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section13)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeBusinessCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeBusinessCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeBusinessCardResponse`
        """
        http_info = self._recognize_business_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_business_card_invoker(self, request):
        http_info = self._recognize_business_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_business_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/business-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeBusinessCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_business_license(self, request):
        """营业执照识别

        识别营业执照首页图片中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section10)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        说明： 
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeBusinessLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeBusinessLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeBusinessLicenseResponse`
        """
        http_info = self._recognize_business_license_http_info(request)
        return self._call_api(**http_info)

    def recognize_business_license_invoker(self, request):
        http_info = self._recognize_business_license_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_business_license_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/business-license",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeBusinessLicenseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_cambodian_id_card(self, request):
        """柬文身份证识别

        识别柬文身份证图片中的文字内容，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeCambodianIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeCambodianIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeCambodianIdCardResponse`
        """
        http_info = self._recognize_cambodian_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_cambodian_id_card_invoker(self, request):
        http_info = self._recognize_cambodian_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_cambodian_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/cambodian-idcard",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeCambodianIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_chile_id_card(self, request):
        """智利身份证识别

        识别智利身份证图片中的文字内容，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeChileIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeChileIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeChileIdCardResponse`
        """
        http_info = self._recognize_chile_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_chile_id_card_invoker(self, request):
        http_info = self._recognize_chile_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_chile_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/chile-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeChileIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_colombia_id_card(self, request):
        """哥伦比亚身份证识别

        识别哥伦比亚身份证中的文字信息，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeColombiaIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeColombiaIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeColombiaIdCardResponse`
        """
        http_info = self._recognize_colombia_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_colombia_id_card_invoker(self, request):
        http_info = self._recognize_colombia_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_colombia_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/colombia-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeColombiaIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_driver_license(self, request):
        """驾驶证识别

        识别用户上传的驾驶证图片（或者用户提供的华为云上OBS的驾驶证图片文件的URL）中主页与副页的文字内容，并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section6)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        说明： 
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeDriverLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeDriverLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeDriverLicenseResponse`
        """
        http_info = self._recognize_driver_license_http_info(request)
        return self._call_api(**http_info)

    def recognize_driver_license_invoker(self, request):
        http_info = self._recognize_driver_license_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_driver_license_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/driver-license",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeDriverLicenseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_exit_entry_permit(self, request):
        """往来港澳台通行证识别

        识别往来港澳台证件图片中的文字内容，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeExitEntryPermit
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeExitEntryPermitRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeExitEntryPermitResponse`
        """
        http_info = self._recognize_exit_entry_permit_http_info(request)
        return self._call_api(**http_info)

    def recognize_exit_entry_permit_invoker(self, request):
        http_info = self._recognize_exit_entry_permit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_exit_entry_permit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/exit-entry-permit",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeExitEntryPermitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_financial_statement(self, request):
        """财务报表识别

        识别用户上传的表格图片中的文字内容，并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section24)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeFinancialStatement
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeFinancialStatementRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeFinancialStatementResponse`
        """
        http_info = self._recognize_financial_statement_http_info(request)
        return self._call_api(**http_info)

    def recognize_financial_statement_invoker(self, request):
        http_info = self._recognize_financial_statement_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_financial_statement_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/financial-statement",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeFinancialStatementResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_flight_itinerary(self, request):
        """飞机行程单识别

        识别飞机行程单中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section20)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeFlightItinerary
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeFlightItineraryRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeFlightItineraryResponse`
        """
        http_info = self._recognize_flight_itinerary_http_info(request)
        return self._call_api(**http_info)

    def recognize_flight_itinerary_invoker(self, request):
        http_info = self._recognize_flight_itinerary_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_flight_itinerary_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/flight-itinerary",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeFlightItineraryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_general_table(self, request):
        """通用表格识别

        用于识别用户上传的通用表格图片（或者用户提供的华为云上OBS的通用表格图片文件的URL）中的文字内容，并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section0)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeGeneralTable
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTableRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTableResponse`
        """
        http_info = self._recognize_general_table_http_info(request)
        return self._call_api(**http_info)

    def recognize_general_table_invoker(self, request):
        http_info = self._recognize_general_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_general_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/general-table",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeGeneralTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_general_text(self, request):
        """通用文字识别

        识别图片上的文字信息，返回识别的文字和坐标。支持扫描文件、电子文档、书籍、票据和表单等多种场景的文字识别。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section1)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeGeneralText
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTextRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeGeneralTextResponse`
        """
        http_info = self._recognize_general_text_http_info(request)
        return self._call_api(**http_info)

    def recognize_general_text_invoker(self, request):
        http_info = self._recognize_general_text_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_general_text_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/general-text",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeGeneralTextResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_handwriting(self, request):
        """手写文字识别

        识别文档中的手写文字信息，并将识别的结构化结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section4)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeHandwriting
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeHandwritingRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeHandwritingResponse`
        """
        http_info = self._recognize_handwriting_http_info(request)
        return self._call_api(**http_info)

    def recognize_handwriting_invoker(self, request):
        http_info = self._recognize_handwriting_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_handwriting_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/handwriting",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeHandwritingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_health_code(self, request):
        """防疫健康码识别

        支持对全国各地区不同版式的防疫健康码、核酸检测记录、行程卡中的14个关键字段进行结构化识别；支持识别4种健康码颜色，包括绿码、黄码、红码、灰码；支持返回各个关键字段的置信度，以便提高人工校验效率。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section26)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeHealthCode
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeHealthCodeRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeHealthCodeResponse`
        """
        http_info = self._recognize_health_code_http_info(request)
        return self._call_api(**http_info)

    def recognize_health_code_invoker(self, request):
        http_info = self._recognize_health_code_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_health_code_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/health-code",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeHealthCodeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_hk_id_card(self, request):
        """香港身份证识别

        识别香港身份证中的文字内容，并将识别的结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeHkIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeHkIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeHkIdCardResponse`
        """
        http_info = self._recognize_hk_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_hk_id_card_invoker(self, request):
        http_info = self._recognize_hk_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_hk_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/hk-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeHkIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_id_card(self, request):
        """身份证识别

        识别身份证图片中的文字内容，并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section5)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        说明： 
        
        身份证识别支持中华人民共和国居民身份证识别。
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeIdCardResponse`
        """
        http_info = self._recognize_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_id_card_invoker(self, request):
        http_info = self._recognize_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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
        http_info = self._recognize_id_document_http_info(request)
        return self._call_api(**http_info)

    def recognize_id_document_invoker(self, request):
        http_info = self._recognize_id_document_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_id_document_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/id-document",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeIdDocumentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_insurance_policy(self, request):
        """保险单识别

        识别保险单图片上的文字信息，并将识别的结构化结果返回给用户。支持对多种版式保险单的扫描图片及手机照片进行结构化信息提取。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section23)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeInsurancePolicy
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeInsurancePolicyRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeInsurancePolicyResponse`
        """
        http_info = self._recognize_insurance_policy_http_info(request)
        return self._call_api(**http_info)

    def recognize_insurance_policy_invoker(self, request):
        http_info = self._recognize_insurance_policy_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_insurance_policy_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/insurance-policy",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeInsurancePolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_invoice_verification(self, request):
        """发票验真

        发票验真服务支持10种增值税发票的信息核验，包括增值税专用发票、增值税普通发票、增值税普通发票（卷式）、增值税电子专用发票、增值税电子普通发票、增值税电子普通发票（通行费）、二手车销售统一发票、机动车销售统一发票、区块链电子发票、全电发票，支持返回票面的全部信息。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section16)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeInvoiceVerification
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeInvoiceVerificationRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeInvoiceVerificationResponse`
        """
        http_info = self._recognize_invoice_verification_http_info(request)
        return self._call_api(**http_info)

    def recognize_invoice_verification_invoker(self, request):
        http_info = self._recognize_invoice_verification_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_invoice_verification_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/invoice-verification",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeInvoiceVerificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_license_plate(self, request):
        """车牌识别

        识别输入图片中的车牌信息，并返回其坐标和内容。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section12)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeLicensePlate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeLicensePlateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeLicensePlateResponse`
        """
        http_info = self._recognize_license_plate_http_info(request)
        return self._call_api(**http_info)

    def recognize_license_plate_invoker(self, request):
        http_info = self._recognize_license_plate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_license_plate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/license-plate",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeLicensePlateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_macao_id_card(self, request):
        """澳门身份证识别

        识别澳门身份证图片中的文字内容，并将识别的结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMacaoIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMacaoIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMacaoIdCardResponse`
        """
        http_info = self._recognize_macao_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_macao_id_card_invoker(self, request):
        http_info = self._recognize_macao_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_macao_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/macao-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeMacaoIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_mainland_travel_permit(self, request):
        """港澳台居民来往内地通行证识别

        识别港澳居民来往内地通行证上的文字内容，并将识别的结构化结果返回给用户。支持港澳居民来往内地通行证和台湾居民来往内地通行证两种卡证。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMainlandTravelPermit
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMainlandTravelPermitRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMainlandTravelPermitResponse`
        """
        http_info = self._recognize_mainland_travel_permit_http_info(request)
        return self._call_api(**http_info)

    def recognize_mainland_travel_permit_invoker(self, request):
        http_info = self._recognize_mainland_travel_permit_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_mainland_travel_permit_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/mainland-travel-permit",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeMainlandTravelPermitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_mvs_invoice(self, request):
        """机动车销售发票识别

        识别机动车销售发票、二手车销售发票图片（服务能自动分辨两种类型，返回对应的字段）中的文字内容，并将识别的结果以JSON格式返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section17)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        该增值税发票仅限于中华人民共和国境内使用的增值税发票。
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMvsInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMvsInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMvsInvoiceResponse`
        """
        http_info = self._recognize_mvs_invoice_http_info(request)
        return self._call_api(**http_info)

    def recognize_mvs_invoice_invoker(self, request):
        http_info = self._recognize_mvs_invoice_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_mvs_invoice_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/mvs-invoice",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeMvsInvoiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_myanmar_driver_license(self, request):
        """缅文驾驶证识别

        识别缅甸驾驶证中的文字信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMyanmarDriverLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarDriverLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarDriverLicenseResponse`
        """
        http_info = self._recognize_myanmar_driver_license_http_info(request)
        return self._call_api(**http_info)

    def recognize_myanmar_driver_license_invoker(self, request):
        http_info = self._recognize_myanmar_driver_license_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_myanmar_driver_license_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/myanmar-driver-license",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeMyanmarDriverLicenseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_myanmar_idcard(self, request):
        """缅文身份证识别

        识别缅文身份证中的文字信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeMyanmarIdcard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarIdcardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeMyanmarIdcardResponse`
        """
        http_info = self._recognize_myanmar_idcard_http_info(request)
        return self._call_api(**http_info)

    def recognize_myanmar_idcard_invoker(self, request):
        http_info = self._recognize_myanmar_idcard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_myanmar_idcard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/myanmar-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeMyanmarIdcardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_passport(self, request):
        """护照识别

        识别用户上传的护照首页图片中的文字信息，并返回识别的结构化结果。当前版本支持中国护照的全字段识别。外国护照支持护照下方两行国际标准化的机读码识别，并可从中提取6-7个关键字段信息。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section8)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizePassport
        :type request: :class:`huaweicloudsdkocr.v1.RecognizePassportRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizePassportResponse`
        """
        http_info = self._recognize_passport_http_info(request)
        return self._call_api(**http_info)

    def recognize_passport_invoker(self, request):
        http_info = self._recognize_passport_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_passport_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/passport",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizePassportResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_pcr_test_record(self, request):
        """核酸检测记录识别

        识别核酸检测记录中的文字信息，并将识别的结构化结果返回给用户。PCR，全称Polymerase chain reaction,即聚合酶链式反应。PCR-test也为大众所认知为新型冠状病毒核酸检测测试。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizePcrTestRecord
        :type request: :class:`huaweicloudsdkocr.v1.RecognizePcrTestRecordRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizePcrTestRecordResponse`
        """
        http_info = self._recognize_pcr_test_record_http_info(request)
        return self._call_api(**http_info)

    def recognize_pcr_test_record_invoker(self, request):
        http_info = self._recognize_pcr_test_record_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_pcr_test_record_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/pcr-test-record",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizePcrTestRecordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_peru_id_card(self, request):
        """秘鲁身份证识别

        识别秘鲁身份证图片中的文字内容，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizePeruIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizePeruIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizePeruIdCardResponse`
        """
        http_info = self._recognize_peru_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_peru_id_card_invoker(self, request):
        http_info = self._recognize_peru_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_peru_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/peru-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizePeruIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_qualification_certificate(self, request):
        """道路运输从业资格证识别

        识别道路运输从业资格证上的关键文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section25)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeQualificationCertificate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeQualificationCertificateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeQualificationCertificateResponse`
        """
        http_info = self._recognize_qualification_certificate_http_info(request)
        return self._call_api(**http_info)

    def recognize_qualification_certificate_invoker(self, request):
        http_info = self._recognize_qualification_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_qualification_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/transportation-qualification-certificate",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeQualificationCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_quota_invoice(self, request):
        """定额发票识别

        识别定额发票中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section21)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        说明： 
        
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeQuotaInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeQuotaInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeQuotaInvoiceResponse`
        """
        http_info = self._recognize_quota_invoice_http_info(request)
        return self._call_api(**http_info)

    def recognize_quota_invoice_invoker(self, request):
        http_info = self._recognize_quota_invoice_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_quota_invoice_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/quota-invoice",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeQuotaInvoiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_real_estate_certificate(self, request):
        """不动产证识别

        识别不动产证中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明： 如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeRealEstateCertificate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeRealEstateCertificateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeRealEstateCertificateResponse`
        """
        http_info = self._recognize_real_estate_certificate_http_info(request)
        return self._call_api(**http_info)

    def recognize_real_estate_certificate_invoker(self, request):
        http_info = self._recognize_real_estate_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_real_estate_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/real-estate-certificate",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeRealEstateCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_smart_document_recognizer(self, request):
        """智能文档解析

        对证件、票据、表单等任意版式文档进行键值对提取、文字识别、以及表格识别等任务，实现进阶高效的自动化结构化返回。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeSmartDocumentRecognizer
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeSmartDocumentRecognizerRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeSmartDocumentRecognizerResponse`
        """
        http_info = self._recognize_smart_document_recognizer_http_info(request)
        return self._call_api(**http_info)

    def recognize_smart_document_recognizer_invoker(self, request):
        http_info = self._recognize_smart_document_recognizer_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_smart_document_recognizer_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/smart-document-recognizer",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeSmartDocumentRecognizerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_taxi_invoice(self, request):
        """出租车发票识别

        识别出租车发票中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section18)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTaxiInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTaxiInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTaxiInvoiceResponse`
        """
        http_info = self._recognize_taxi_invoice_http_info(request)
        return self._call_api(**http_info)

    def recognize_taxi_invoice_invoker(self, request):
        http_info = self._recognize_taxi_invoice_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_taxi_invoice_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/taxi-invoice",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeTaxiInvoiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_thailand_idcard(self, request):
        """泰文身份证识别

        识别泰国身份证中的文字信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeThailandIdcard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeThailandIdcardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeThailandIdcardResponse`
        """
        http_info = self._recognize_thailand_idcard_http_info(request)
        return self._call_api(**http_info)

    def recognize_thailand_idcard_invoker(self, request):
        http_info = self._recognize_thailand_idcard_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_thailand_idcard_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/thailand-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeThailandIdcardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_thailand_license_plate(self, request):
        """泰国车牌识别

        识别泰国车牌图片中的车牌信息，并返回识别的结构化结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeThailandLicensePlate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeThailandLicensePlateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeThailandLicensePlateResponse`
        """
        http_info = self._recognize_thailand_license_plate_http_info(request)
        return self._call_api(**http_info)

    def recognize_thailand_license_plate_invoker(self, request):
        http_info = self._recognize_thailand_license_plate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_thailand_license_plate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/thailand-license-plate",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeThailandLicensePlateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_toll_invoice(self, request):
        """车辆通行费发票识别

        识别车辆通行费发票中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section19)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTollInvoice
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTollInvoiceRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTollInvoiceResponse`
        """
        http_info = self._recognize_toll_invoice_http_info(request)
        return self._call_api(**http_info)

    def recognize_toll_invoice_invoker(self, request):
        http_info = self._recognize_toll_invoice_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_toll_invoice_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/toll-invoice",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeTollInvoiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_train_ticket(self, request):
        """火车票识别

        识别火车票中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section22)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTrainTicket
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTrainTicketRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTrainTicketResponse`
        """
        http_info = self._recognize_train_ticket_http_info(request)
        return self._call_api(**http_info)

    def recognize_train_ticket_invoker(self, request):
        http_info = self._recognize_train_ticket_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_train_ticket_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/train-ticket",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeTrainTicketResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_transportation_license(self, request):
        """道路运输证识别

        识别道路运输证首页中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明： 如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeTransportationLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeTransportationLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeTransportationLicenseResponse`
        """
        http_info = self._recognize_transportation_license_http_info(request)
        return self._call_api(**http_info)

    def recognize_transportation_license_invoker(self, request):
        http_info = self._recognize_transportation_license_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_transportation_license_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/transportation-license",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeTransportationLicenseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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
        http_info = self._recognize_vat_invoice_http_info(request)
        return self._call_api(**http_info)

    def recognize_vat_invoice_invoker(self, request):
        http_info = self._recognize_vat_invoice_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_vat_invoice_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/vat-invoice",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeVatInvoiceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_vehicle_certificate(self, request):
        """车辆合格证识别

        识别车辆合格证中的文字信息，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section11)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVehicleCertificate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVehicleCertificateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVehicleCertificateResponse`
        """
        http_info = self._recognize_vehicle_certificate_http_info(request)
        return self._call_api(**http_info)

    def recognize_vehicle_certificate_invoker(self, request):
        http_info = self._recognize_vehicle_certificate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_vehicle_certificate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/vehicle-certificate",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeVehicleCertificateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_vehicle_license(self, request):
        """行驶证识别

        识别用户上传的行驶证图片（或者用户提供的华为云上OBS的行驶证图片文件的URL）中主页和副页的文字内容，并将识别的结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section7)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        说明：
        如果图片中包含多张卡证票据，请调用[智能分类识别](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;OCR&amp;api&#x3D;AutoClassification)服务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVehicleLicense
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVehicleLicenseRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVehicleLicenseResponse`
        """
        http_info = self._recognize_vehicle_license_http_info(request)
        return self._call_api(**http_info)

    def recognize_vehicle_license_invoker(self, request):
        http_info = self._recognize_vehicle_license_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_vehicle_license_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/vehicle-license",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeVehicleLicenseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_vietnam_id_card(self, request):
        """越南身份证识别

        识别越南身份证中的文字信息，并将识别的结构化结果返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVietnamIdCard
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVietnamIdCardRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVietnamIdCardResponse`
        """
        http_info = self._recognize_vietnam_id_card_http_info(request)
        return self._call_api(**http_info)

    def recognize_vietnam_id_card_invoker(self, request):
        http_info = self._recognize_vietnam_id_card_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_vietnam_id_card_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/vietnam-id-card",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeVietnamIdCardResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_waybill_electronic(self, request):
        """电子面单识别

        识别用户上传的电子面单图片中的文字内容，并将识别的结果以json格式返回给用户。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeWaybillElectronic
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeWaybillElectronicRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeWaybillElectronicResponse`
        """
        http_info = self._recognize_waybill_electronic_http_info(request)
        return self._call_api(**http_info)

    def recognize_waybill_electronic_invoker(self, request):
        http_info = self._recognize_waybill_electronic_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_waybill_electronic_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/waybill-electronic",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeWaybillElectronicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_web_image(self, request):
        """网络图片识别

        识别网络图片中的文字内容，并返回识别的结构化结果。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section2)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeWebImage
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeWebImageRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeWebImageResponse`
        """
        http_info = self._recognize_web_image_http_info(request)
        return self._call_api(**http_info)

    def recognize_web_image_invoker(self, request):
        http_info = self._recognize_web_image_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_web_image_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/web-image",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeWebImageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_custom_template(self, request):
        """自定义模板OCR

        自定义模板OCR，支持用户自定义模板，对于版式固定的各种票据和卡证，通过可视化界面操作，指定需要识别的关键字段，实现用户特定格式图片的自动识别和结构化提取。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeCustomTemplate
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeCustomTemplateRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeCustomTemplateResponse`
        """
        http_info = self._recognize_custom_template_http_info(request)
        return self._call_api(**http_info)

    def recognize_custom_template_invoker(self, request):
        http_info = self._recognize_custom_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_custom_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/custom-template",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeCustomTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

    def recognize_vin(self, request):
        """VIN码识别

        识别图片中的车架号信息，并将识别结果返回给用户。该接口的使用限制请参见[约束与限制](https://support.huaweicloud.com/productdesc-ocr/ocr_01_0006.html#section14)，详细使用指导请参见[OCR服务使用简介](https://support.huaweicloud.com/qs-ocr/ocr_05_0001.html)章节。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeVin
        :type request: :class:`huaweicloudsdkocr.v1.RecognizeVinRequest`
        :rtype: :class:`huaweicloudsdkocr.v1.RecognizeVinResponse`
        """
        http_info = self._recognize_vin_http_info(request)
        return self._call_api(**http_info)

    def recognize_vin_invoker(self, request):
        http_info = self._recognize_vin_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _recognize_vin_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/ocr/vin",
            "request_type": request.__class__.__name__,
            "response_type": "RecognizeVinResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

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

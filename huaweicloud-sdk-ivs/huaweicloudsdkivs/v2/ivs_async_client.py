# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class IvsAsyncClient(Client):
    def __init__(self):
        super(IvsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkivs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "IvsAsyncClient":
                raise TypeError("client type error, support client type is IvsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def detect_extention_by_id_card_image_async(self, request):
        """人证核身证件版（二要素）

        使用姓名、身份证号码二要素进行身份审核。身份验证时，传入的数据为身份证信息。提取身份证信息时，可以使用身份证正反面图片，也可以直接输入姓名、身份证号文本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectExtentionByIdCardImage
        :type request: :class:`huaweicloudsdkivs.v2.DetectExtentionByIdCardImageRequest`
        :rtype: :class:`huaweicloudsdkivs.v2.DetectExtentionByIdCardImageResponse`
        """
        return self._detect_extention_by_id_card_image_with_http_info(request)

    def _detect_extention_by_id_card_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/ivs-idcard-extention',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectExtentionByIdCardImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_extention_by_name_and_id_async(self, request):
        """人证核身证件版（二要素）

        使用姓名、身份证号码二要素进行身份审核。身份验证时，传入的数据为身份证信息。提取身份证信息时，可以使用身份证正反面图片，也可以直接输入姓名、身份证号文本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectExtentionByNameAndId
        :type request: :class:`huaweicloudsdkivs.v2.DetectExtentionByNameAndIdRequest`
        :rtype: :class:`huaweicloudsdkivs.v2.DetectExtentionByNameAndIdResponse`
        """
        return self._detect_extention_by_name_and_id_with_http_info(request)

    def _detect_extention_by_name_and_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/ivs-idcard-extention',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectExtentionByNameAndIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_standard_by_id_card_image_async(self, request):
        """人证核身标准版（三要素）

        使用身份证正反面图片提取姓名和身份证号码，与人脸图片进行三要素身份审核。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectStandardByIdCardImage
        :type request: :class:`huaweicloudsdkivs.v2.DetectStandardByIdCardImageRequest`
        :rtype: :class:`huaweicloudsdkivs.v2.DetectStandardByIdCardImageResponse`
        """
        return self._detect_standard_by_id_card_image_with_http_info(request)

    def _detect_standard_by_id_card_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/ivs-standard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectStandardByIdCardImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_standard_by_name_and_id_async(self, request):
        """人证核身标准版（三要素）

        使用姓名、身份证号文本和人脸图片进行三要素身份审核。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectStandardByNameAndId
        :type request: :class:`huaweicloudsdkivs.v2.DetectStandardByNameAndIdRequest`
        :rtype: :class:`huaweicloudsdkivs.v2.DetectStandardByNameAndIdResponse`
        """
        return self._detect_standard_by_name_and_id_with_http_info(request)

    def _detect_standard_by_name_and_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/ivs-standard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectStandardByNameAndIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_standard_by_video_and_id_card_image_async(self, request):
        """人证核身标准版（三要素）

        从身份证正反面图片中提取姓名和身份证号码，并对视频做活体检测后提取人脸图片，以此进行三要素身份审核。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectStandardByVideoAndIdCardImage
        :type request: :class:`huaweicloudsdkivs.v2.DetectStandardByVideoAndIdCardImageRequest`
        :rtype: :class:`huaweicloudsdkivs.v2.DetectStandardByVideoAndIdCardImageResponse`
        """
        return self._detect_standard_by_video_and_id_card_image_with_http_info(request)

    def _detect_standard_by_video_and_id_card_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/ivs-standard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectStandardByVideoAndIdCardImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_standard_by_video_and_name_and_id_async(self, request):
        """人证核身标准版（三要素）

        使用姓名、身份证号文本，并对视频做活体检测后提取人脸图片，以此进行三要素身份审核。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectStandardByVideoAndNameAndId
        :type request: :class:`huaweicloudsdkivs.v2.DetectStandardByVideoAndNameAndIdRequest`
        :rtype: :class:`huaweicloudsdkivs.v2.DetectStandardByVideoAndNameAndIdResponse`
        """
        return self._detect_standard_by_video_and_name_and_id_with_http_info(request)

    def _detect_standard_by_video_and_name_and_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

        response_headers = ["X-Request-Id", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2.0/ivs-standard',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectStandardByVideoAndNameAndIdResponse',
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

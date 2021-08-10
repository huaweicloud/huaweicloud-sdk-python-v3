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


class FrsClient(Client):
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
        super(FrsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkfrs.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "FrsClient":
            raise TypeError("client type error, support client type is FrsClient")

        return ClientBuilder(clazz)

    def add_faces_by_base64(self, request):
        """添加人脸

        添加人脸到人脸库中，检测到传入的单张图片中存在多少张人脸，则增加多少张人脸到人脸库当中。

        :param AddFacesByBase64Request request
        :return: AddFacesByBase64Response
        """
        return self.add_faces_by_base64_with_http_info(request)

    def add_faces_by_base64_with_http_info(self, request):
        """添加人脸

        添加人脸到人脸库中，检测到传入的单张图片中存在多少张人脸，则增加多少张人脸到人脸库当中。

        :param AddFacesByBase64Request request
        :return: AddFacesByBase64Response
        """

        all_params = ['face_set_name', 'add_faces_base64_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddFacesByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_faces_by_file(self, request):
        """添加人脸

        添加人脸到人脸库中，检测到传入的单张图片中存在多少张人脸，则增加多少张人脸到人脸库当中。

        :param AddFacesByFileRequest request
        :return: AddFacesByFileResponse
        """
        return self.add_faces_by_file_with_http_info(request)

    def add_faces_by_file_with_http_info(self, request):
        """添加人脸

        添加人脸到人脸库中，检测到传入的单张图片中存在多少张人脸，则增加多少张人脸到人脸库当中。

        :param AddFacesByFileRequest request
        :return: AddFacesByFileResponse
        """

        all_params = ['face_set_name', 'image_file', 'external_image_id', 'external_fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'image_file' in local_var_params:
            form_params['image_file'] =  local_var_params['image_file']
        if 'external_image_id' in local_var_params:
            form_params['external_image_id'] =  local_var_params['external_image_id']
        if 'external_fields' in local_var_params:
            form_params['external_fields'] =  local_var_params['external_fields']

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddFacesByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_faces_by_url(self, request):
        """添加人脸

        添加人脸到人脸库中，检测到传入的单张图片中存在多少张人脸，则增加多少张人脸到人脸库当中。

        :param AddFacesByUrlRequest request
        :return: AddFacesByUrlResponse
        """
        return self.add_faces_by_url_with_http_info(request)

    def add_faces_by_url_with_http_info(self, request):
        """添加人脸

        添加人脸到人脸库中，检测到传入的单张图片中存在多少张人脸，则增加多少张人脸到人脸库当中。

        :param AddFacesByUrlRequest request
        :return: AddFacesByUrlResponse
        """

        all_params = ['face_set_name', 'add_faces_url_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddFacesByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_delete_faces(self, request):
        """批量删除人脸

        自定义筛选条件，批量删除人脸库中的符合指定条件的多张人脸。

        :param BatchDeleteFacesRequest request
        :return: BatchDeleteFacesResponse
        """
        return self.batch_delete_faces_with_http_info(request)

    def batch_delete_faces_with_http_info(self, request):
        """批量删除人脸

        自定义筛选条件，批量删除人脸库中的符合指定条件的多张人脸。

        :param BatchDeleteFacesRequest request
        :return: BatchDeleteFacesResponse
        """

        all_params = ['face_set_name', 'delete_faces_batch_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces/batch',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchDeleteFacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def compare_face_by_base64(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。

        :param CompareFaceByBase64Request request
        :return: CompareFaceByBase64Response
        """
        return self.compare_face_by_base64_with_http_info(request)

    def compare_face_by_base64_with_http_info(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。

        :param CompareFaceByBase64Request request
        :return: CompareFaceByBase64Response
        """

        all_params = ['face_compare_base64_req']
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
            resource_path='/v2/{project_id}/face-compare',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CompareFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def compare_face_by_file(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。

        :param CompareFaceByFileRequest request
        :return: CompareFaceByFileResponse
        """
        return self.compare_face_by_file_with_http_info(request)

    def compare_face_by_file_with_http_info(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。

        :param CompareFaceByFileRequest request
        :return: CompareFaceByFileResponse
        """

        all_params = ['image1_file', 'image2_file']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'image1_file' in local_var_params:
            form_params['image1_file'] =  local_var_params['image1_file']
        if 'image2_file' in local_var_params:
            form_params['image2_file'] =  local_var_params['image2_file']

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/face-compare',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CompareFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def compare_face_by_url(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。

        :param CompareFaceByUrlRequest request
        :return: CompareFaceByUrlResponse
        """
        return self.compare_face_by_url_with_http_info(request)

    def compare_face_by_url_with_http_info(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。

        :param CompareFaceByUrlRequest request
        :return: CompareFaceByUrlResponse
        """

        all_params = ['face_compare_url_req']
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
            resource_path='/v2/{project_id}/face-compare',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CompareFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_face_set(self, request):
        """创建人脸库

        创建用于存储人脸特征的人脸库。您最多可以创建10个人脸库，每个人脸库最大容量为10万个人脸特征。如有更大规格的需求请联系客服。

        :param CreateFaceSetRequest request
        :return: CreateFaceSetResponse
        """
        return self.create_face_set_with_http_info(request)

    def create_face_set_with_http_info(self, request):
        """创建人脸库

        创建用于存储人脸特征的人脸库。您最多可以创建10个人脸库，每个人脸库最大容量为10万个人脸特征。如有更大规格的需求请联系客服。

        :param CreateFaceSetRequest request
        :return: CreateFaceSetResponse
        """

        all_params = ['create_face_set_req']
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
            resource_path='/v2/{project_id}/face-sets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFaceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_face_by_external_image_id(self, request):
        """删除人脸

        根据external_image_id删除人脸。

        :param DeleteFaceByExternalImageIdRequest request
        :return: DeleteFaceByExternalImageIdResponse
        """
        return self.delete_face_by_external_image_id_with_http_info(request)

    def delete_face_by_external_image_id_with_http_info(self, request):
        """删除人脸

        根据external_image_id删除人脸。

        :param DeleteFaceByExternalImageIdRequest request
        :return: DeleteFaceByExternalImageIdResponse
        """

        all_params = ['face_set_name', 'external_image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []
        if 'external_image_id' in local_var_params:
            query_params.append(('external_image_id', local_var_params['external_image_id']))

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteFaceByExternalImageIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_face_by_face_id(self, request):
        """删除人脸

        根据face_id删除人脸。

        :param DeleteFaceByFaceIdRequest request
        :return: DeleteFaceByFaceIdResponse
        """
        return self.delete_face_by_face_id_with_http_info(request)

    def delete_face_by_face_id_with_http_info(self, request):
        """删除人脸

        根据face_id删除人脸。

        :param DeleteFaceByFaceIdRequest request
        :return: DeleteFaceByFaceIdResponse
        """

        all_params = ['face_set_name', 'face_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []
        if 'face_id' in local_var_params:
            query_params.append(('face_id', local_var_params['face_id']))

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteFaceByFaceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_face_set(self, request):
        """删除人脸库

        删除人脸库以及其中所有的人脸。

        :param DeleteFaceSetRequest request
        :return: DeleteFaceSetResponse
        """
        return self.delete_face_set_with_http_info(request)

    def delete_face_set_with_http_info(self, request):
        """删除人脸库

        删除人脸库以及其中所有的人脸。

        :param DeleteFaceSetRequest request
        :return: DeleteFaceSetResponse
        """

        all_params = ['face_set_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteFaceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def detect_face_by_base64(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。

        :param DetectFaceByBase64Request request
        :return: DetectFaceByBase64Response
        """
        return self.detect_face_by_base64_with_http_info(request)

    def detect_face_by_base64_with_http_info(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。

        :param DetectFaceByBase64Request request
        :return: DetectFaceByBase64Response
        """

        all_params = ['face_detect_base64_req']
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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DetectFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def detect_face_by_file(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。

        :param DetectFaceByFileRequest request
        :return: DetectFaceByFileResponse
        """
        return self.detect_face_by_file_with_http_info(request)

    def detect_face_by_file_with_http_info(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。

        :param DetectFaceByFileRequest request
        :return: DetectFaceByFileResponse
        """

        all_params = ['image_file', 'attributes']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'image_file' in local_var_params:
            form_params['image_file'] =  local_var_params['image_file']
        if 'attributes' in local_var_params:
            form_params['attributes'] =  local_var_params['attributes']

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DetectFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def detect_face_by_url(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。

        :param DetectFaceByUrlRequest request
        :return: DetectFaceByUrlResponse
        """
        return self.detect_face_by_url_with_http_info(request)

    def detect_face_by_url_with_http_info(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。

        :param DetectFaceByUrlRequest request
        :return: DetectFaceByUrlResponse
        """

        all_params = ['face_detect_url_req']
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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DetectFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_face_by_base64(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByBase64Request request
        :return: SearchFaceByBase64Response
        """
        return self.search_face_by_base64_with_http_info(request)

    def search_face_by_base64_with_http_info(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByBase64Request request
        :return: SearchFaceByBase64Response
        """

        all_params = ['face_set_name', 'face_search_base64_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_face_by_face_id(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByFaceIdRequest request
        :return: SearchFaceByFaceIdResponse
        """
        return self.search_face_by_face_id_with_http_info(request)

    def search_face_by_face_id_with_http_info(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByFaceIdRequest request
        :return: SearchFaceByFaceIdResponse
        """

        all_params = ['face_set_name', 'face_search_face_id_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchFaceByFaceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_face_by_file(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByFileRequest request
        :return: SearchFaceByFileResponse
        """
        return self.search_face_by_file_with_http_info(request)

    def search_face_by_file_with_http_info(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByFileRequest request
        :return: SearchFaceByFileResponse
        """

        all_params = ['face_set_name', 'image_file', 'top_n', 'threshold', 'sort', 'filter', 'return_fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'image_file' in local_var_params:
            form_params['image_file'] =  local_var_params['image_file']
        if 'top_n' in local_var_params:
            form_params['top_n'] =  local_var_params['top_n']
        if 'threshold' in local_var_params:
            form_params['threshold'] =  local_var_params['threshold']
        if 'sort' in local_var_params:
            form_params['sort'] =  local_var_params['sort']
        if 'filter' in local_var_params:
            form_params['filter'] =  local_var_params['filter']
        if 'return_fields' in local_var_params:
            form_params['return_fields'] =  local_var_params['return_fields']

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['multipart/form-data'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def search_face_by_url(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByUrlRequest request
        :return: SearchFaceByUrlResponse
        """
        return self.search_face_by_url_with_http_info(request)

    def search_face_by_url_with_http_info(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。 支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。

        :param SearchFaceByUrlRequest request
        :return: SearchFaceByUrlResponse
        """

        all_params = ['face_set_name', 'face_search_url_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='SearchFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_all_face_sets(self, request):
        """查询所有人脸库

        查询当前用户所有人脸库的状态信息。

        :param ShowAllFaceSetsRequest request
        :return: ShowAllFaceSetsResponse
        """
        return self.show_all_face_sets_with_http_info(request)

    def show_all_face_sets_with_http_info(self, request):
        """查询所有人脸库

        查询当前用户所有人脸库的状态信息。

        :param ShowAllFaceSetsRequest request
        :return: ShowAllFaceSetsResponse
        """

        all_params = []
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
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/face-sets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAllFaceSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_face_set(self, request):
        """查询人脸库

        查询人脸库当前的状态。

        :param ShowFaceSetRequest request
        :return: ShowFaceSetResponse
        """
        return self.show_face_set_with_http_info(request)

    def show_face_set_with_http_info(self, request):
        """查询人脸库

        查询人脸库当前的状态。

        :param ShowFaceSetRequest request
        :return: ShowFaceSetResponse
        """

        all_params = ['face_set_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFaceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_faces_by_face_id(self, request):
        """查询人脸

        查询指定人脸库中人脸信息。

        :param ShowFacesByFaceIdRequest request
        :return: ShowFacesByFaceIdResponse
        """
        return self.show_faces_by_face_id_with_http_info(request)

    def show_faces_by_face_id_with_http_info(self, request):
        """查询人脸

        查询指定人脸库中人脸信息。

        :param ShowFacesByFaceIdRequest request
        :return: ShowFacesByFaceIdResponse
        """

        all_params = ['face_set_name', 'face_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []
        if 'face_id' in local_var_params:
            query_params.append(('face_id', local_var_params['face_id']))

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFacesByFaceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_faces_by_limit(self, request):
        """查询人脸

        查询指定人脸库中人脸信息。

        :param ShowFacesByLimitRequest request
        :return: ShowFacesByLimitResponse
        """
        return self.show_faces_by_limit_with_http_info(request)

    def show_faces_by_limit_with_http_info(self, request):
        """查询人脸

        查询指定人脸库中人脸信息。

        :param ShowFacesByLimitRequest request
        :return: ShowFacesByLimitResponse
        """

        all_params = ['face_set_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFacesByLimitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_face(self, request):
        """更新人脸

        根据人脸ID（face_id）更新单张人脸信息。

        :param UpdateFaceRequest request
        :return: UpdateFaceResponse
        """
        return self.update_face_with_http_info(request)

    def update_face_with_http_info(self, request):
        """更新人脸

        根据人脸ID（face_id）更新单张人脸信息。

        :param UpdateFaceRequest request
        :return: UpdateFaceResponse
        """

        all_params = ['face_set_name', 'update_face_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFaceResponse',
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

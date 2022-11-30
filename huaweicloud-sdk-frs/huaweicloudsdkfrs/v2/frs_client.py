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

        添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中，支持添加最大人脸或所有人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddFacesByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.AddFacesByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesByBase64Response`
        """
        return self.add_faces_by_base64_with_http_info(request)

    def add_faces_by_base64_with_http_info(self, request):
        all_params = ['face_set_name', 'add_faces_base64_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddFacesByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_faces_by_file(self, request):
        """添加人脸

        添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中，支持添加最大人脸或所有人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddFacesByFile
        :type request: :class:`huaweicloudsdkfrs.v2.AddFacesByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesByFileResponse`
        """
        return self.add_faces_by_file_with_http_info(request)

    def add_faces_by_file_with_http_info(self, request):
        all_params = ['face_set_name', 'image_file', 'external_image_id', 'external_fields', 'single']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']
        if 'external_image_id' in local_var_params:
            form_params['external_image_id'] = local_var_params['external_image_id']
        if 'external_fields' in local_var_params:
            form_params['external_fields'] = local_var_params['external_fields']
        if 'single' in local_var_params:
            form_params['single'] = local_var_params['single']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/faces',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='AddFacesByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def add_faces_by_url(self, request):
        """添加人脸

        添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中，支持添加最大人脸或所有人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for AddFacesByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.AddFacesByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesByUrlResponse`
        """
        return self.add_faces_by_url_with_http_info(request)

    def add_faces_by_url_with_http_info(self, request):
        all_params = ['face_set_name', 'add_faces_url_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='AddFacesByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_faces(self, request):
        """批量删除人脸

        自定义筛选条件，批量删除人脸库中的符合指定条件的多张人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteFaces
        :type request: :class:`huaweicloudsdkfrs.v2.BatchDeleteFacesRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.BatchDeleteFacesResponse`
        """
        return self.batch_delete_faces_with_http_info(request)

    def batch_delete_faces_with_http_info(self, request):
        all_params = ['face_set_name', 'delete_faces_batch_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='BatchDeleteFacesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def compare_face_by_base64(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.CompareFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFaceByBase64Response`
        """
        return self.compare_face_by_base64_with_http_info(request)

    def compare_face_by_base64_with_http_info(self, request):
        all_params = ['face_compare_base64_req']
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
            resource_path='/v2/{project_id}/face-compare',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CompareFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def compare_face_by_file(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.CompareFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFaceByFileResponse`
        """
        return self.compare_face_by_file_with_http_info(request)

    def compare_face_by_file_with_http_info(self, request):
        all_params = ['image1_file', 'image2_file']
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
        if 'image1_file' in local_var_params:
            form_params['image1_file'] = local_var_params['image1_file']
        if 'image2_file' in local_var_params:
            form_params['image2_file'] = local_var_params['image2_file']

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
            resource_path='/v2/{project_id}/face-compare',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CompareFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def compare_face_by_url(self, request):
        """人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CompareFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.CompareFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFaceByUrlResponse`
        """
        return self.compare_face_by_url_with_http_info(request)

    def compare_face_by_url_with_http_info(self, request):
        all_params = ['face_compare_url_req']
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
            resource_path='/v2/{project_id}/face-compare',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CompareFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_face_set(self, request):
        """创建人脸库

        创建用于存储人脸特征的人脸库。您最多可以创建10个人脸库，每个人脸库最大容量为10万个人脸特征。如有更大规格的需求请联系客服。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFaceSet
        :type request: :class:`huaweicloudsdkfrs.v2.CreateFaceSetRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.CreateFaceSetResponse`
        """
        return self.create_face_set_with_http_info(request)

    def create_face_set_with_http_info(self, request):
        all_params = ['create_face_set_req']
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
            resource_path='/v2/{project_id}/face-sets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFaceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_face_by_external_image_id(self, request):
        """删除人脸

        根据external_image_id删除人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFaceByExternalImageId
        :type request: :class:`huaweicloudsdkfrs.v2.DeleteFaceByExternalImageIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFaceByExternalImageIdResponse`
        """
        return self.delete_face_by_external_image_id_with_http_info(request)

    def delete_face_by_external_image_id_with_http_info(self, request):
        all_params = ['face_set_name', 'external_image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteFaceByExternalImageIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_face_by_face_id(self, request):
        """删除人脸

        根据face_id删除人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFaceByFaceId
        :type request: :class:`huaweicloudsdkfrs.v2.DeleteFaceByFaceIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFaceByFaceIdResponse`
        """
        return self.delete_face_by_face_id_with_http_info(request)

    def delete_face_by_face_id_with_http_info(self, request):
        all_params = ['face_set_name', 'face_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteFaceByFaceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_face_set(self, request):
        """删除人脸库

        删除人脸库以及其中所有的人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteFaceSet
        :type request: :class:`huaweicloudsdkfrs.v2.DeleteFaceSetRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFaceSetResponse`
        """
        return self.delete_face_set_with_http_info(request)

    def delete_face_set_with_http_info(self, request):
        all_params = ['face_set_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='DeleteFaceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_face_by_base64(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64Response`
        """
        return self.detect_face_by_base64_with_http_info(request)

    def detect_face_by_base64_with_http_info(self, request):
        all_params = ['face_detect_base64_req']
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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_face_by_base64_intl(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectFaceByBase64Intl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64IntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64IntlResponse`
        """
        return self.detect_face_by_base64_intl_with_http_info(request)

    def detect_face_by_base64_intl_with_http_info(self, request):
        all_params = ['face_detect_base64_req']
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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectFaceByBase64IntlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_face_by_file(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileResponse`
        """
        return self.detect_face_by_file_with_http_info(request)

    def detect_face_by_file_with_http_info(self, request):
        all_params = ['image_file', 'attributes']
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
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']
        if 'attributes' in local_var_params:
            form_params['attributes'] = local_var_params['attributes']

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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_face_by_file_intl(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectFaceByFileIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileIntlResponse`
        """
        return self.detect_face_by_file_intl_with_http_info(request)

    def detect_face_by_file_intl_with_http_info(self, request):
        all_params = ['image_file']
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
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']

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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectFaceByFileIntlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_face_by_url(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlResponse`
        """
        return self.detect_face_by_url_with_http_info(request)

    def detect_face_by_url_with_http_info(self, request):
        all_params = ['face_detect_url_req']
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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_face_by_url_intl(self, request):
        """人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectFaceByUrlIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlIntlResponse`
        """
        return self.detect_face_by_url_intl_with_http_info(request)

    def detect_face_by_url_intl_with_http_info(self, request):
        all_params = ['face_detect_url_req']
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
            resource_path='/v2/{project_id}/face-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectFaceByUrlIntlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_by_base64(self, request):
        """动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64Response`
        """
        return self.detect_live_by_base64_with_http_info(request)

    def detect_live_by_base64_with_http_info(self, request):
        all_params = ['live_detect_base64_req']
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
            resource_path='/v1/{project_id}/live-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_by_base64_intl(self, request):
        """动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveByBase64Intl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64IntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64IntlResponse`
        """
        return self.detect_live_by_base64_intl_with_http_info(request)

    def detect_live_by_base64_intl_with_http_info(self, request):
        all_params = ['live_detect_base64_req']
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
            resource_path='/v2/{project_id}/live-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveByBase64IntlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_by_file(self, request):
        """动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveByFile
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileResponse`
        """
        return self.detect_live_by_file_with_http_info(request)

    def detect_live_by_file_with_http_info(self, request):
        all_params = ['video_file', 'actions', 'action_time']
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
        if 'video_file' in local_var_params:
            form_params['video_file'] = local_var_params['video_file']
        if 'actions' in local_var_params:
            form_params['actions'] = local_var_params['actions']
        if 'action_time' in local_var_params:
            form_params['action_time'] = local_var_params['action_time']

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
            resource_path='/v1/{project_id}/live-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_by_file_intl(self, request):
        """动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveByFileIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileIntlResponse`
        """
        return self.detect_live_by_file_intl_with_http_info(request)

    def detect_live_by_file_intl_with_http_info(self, request):
        all_params = ['video_file', 'actions', 'action_time']
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
        if 'video_file' in local_var_params:
            form_params['video_file'] = local_var_params['video_file']
        if 'actions' in local_var_params:
            form_params['actions'] = local_var_params['actions']
        if 'action_time' in local_var_params:
            form_params['action_time'] = local_var_params['action_time']

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
            resource_path='/v2/{project_id}/live-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveByFileIntlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_by_url(self, request):
        """动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlResponse`
        """
        return self.detect_live_by_url_with_http_info(request)

    def detect_live_by_url_with_http_info(self, request):
        all_params = ['live_detect_url_req']
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
            resource_path='/v1/{project_id}/live-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_by_url_intl(self, request):
        """动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveByUrlIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlIntlResponse`
        """
        return self.detect_live_by_url_intl_with_http_info(request)

    def detect_live_by_url_intl_with_http_info(self, request):
        all_params = ['live_detect_url_req']
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
            resource_path='/v2/{project_id}/live-detect',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveByUrlIntlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_face_by_base64(self, request):
        """静默活体检测

        静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息，判断图片中的人脸是否来自于真人活体，有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片，不支持多人脸图片。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByBase64Response`
        """
        return self.detect_live_face_by_base64_with_http_info(request)

    def detect_live_face_by_base64_with_http_info(self, request):
        all_params = ['live_detect_face_base64_req']
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
            resource_path='/v1/{project_id}/live-detect-face',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_face_by_file(self, request):
        """静默活体检测

        静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息，判断图片中的人脸是否来自于真人活体，有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片，不支持多人脸图片。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByFileResponse`
        """
        return self.detect_live_face_by_file_with_http_info(request)

    def detect_live_face_by_file_with_http_info(self, request):
        all_params = ['image_file']
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
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']

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
            resource_path='/v1/{project_id}/live-detect-face',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def detect_live_face_by_url(self, request):
        """静默活体检测

        静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息，判断图片中的人脸是否来自于真人活体，有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片，不支持多人脸图片。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DetectLiveFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByUrlResponse`
        """
        return self.detect_live_face_by_url_with_http_info(request)

    def detect_live_face_by_url_with_http_info(self, request):
        all_params = ['live_detect_face_url_req']
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
            resource_path='/v1/{project_id}/live-detect-face',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DetectLiveFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_face_by_base64(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByBase64Response`
        """
        return self.search_face_by_base64_with_http_info(request)

    def search_face_by_base64_with_http_info(self, request):
        all_params = ['face_set_name', 'face_search_base64_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='SearchFaceByBase64Response',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_face_by_face_id(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchFaceByFaceId
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByFaceIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByFaceIdResponse`
        """
        return self.search_face_by_face_id_with_http_info(request)

    def search_face_by_face_id_with_http_info(self, request):
        all_params = ['face_set_name', 'face_search_face_id_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='SearchFaceByFaceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_face_by_file(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByFileResponse`
        """
        return self.search_face_by_file_with_http_info(request)

    def search_face_by_file_with_http_info(self, request):
        all_params = ['face_set_name', 'image_file', 'top_n', 'threshold', 'sort', 'filter', 'return_fields']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}

        form_params = {}
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']
        if 'top_n' in local_var_params:
            form_params['top_n'] = local_var_params['top_n']
        if 'threshold' in local_var_params:
            form_params['threshold'] = local_var_params['threshold']
        if 'sort' in local_var_params:
            form_params['sort'] = local_var_params['sort']
        if 'filter' in local_var_params:
            form_params['filter'] = local_var_params['filter']
        if 'return_fields' in local_var_params:
            form_params['return_fields'] = local_var_params['return_fields']

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
            resource_path='/v2/{project_id}/face-sets/{face_set_name}/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SearchFaceByFileResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def search_face_by_url(self, request):
        """人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByUrlResponse`
        """
        return self.search_face_by_url_with_http_info(request)

    def search_face_by_url_with_http_info(self, request):
        all_params = ['face_set_name', 'face_search_url_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='SearchFaceByUrlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_all_face_sets(self, request):
        """查询所有人脸库

        查询当前用户所有人脸库的状态信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAllFaceSets
        :type request: :class:`huaweicloudsdkfrs.v2.ShowAllFaceSetsRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowAllFaceSetsResponse`
        """
        return self.show_all_face_sets_with_http_info(request)

    def show_all_face_sets_with_http_info(self, request):
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
            resource_path='/v2/{project_id}/face-sets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAllFaceSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_face_set(self, request):
        """查询人脸库

        查询人脸库当前的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFaceSet
        :type request: :class:`huaweicloudsdkfrs.v2.ShowFaceSetRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowFaceSetResponse`
        """
        return self.show_face_set_with_http_info(request)

    def show_face_set_with_http_info(self, request):
        all_params = ['face_set_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowFaceSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_faces_by_face_id(self, request):
        """查询人脸

        查询指定人脸库中人脸信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFacesByFaceId
        :type request: :class:`huaweicloudsdkfrs.v2.ShowFacesByFaceIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowFacesByFaceIdResponse`
        """
        return self.show_faces_by_face_id_with_http_info(request)

    def show_faces_by_face_id_with_http_info(self, request):
        all_params = ['face_set_name', 'face_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowFacesByFaceIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_faces_by_limit(self, request):
        """查询人脸

        查询指定人脸库中人脸信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFacesByLimit
        :type request: :class:`huaweicloudsdkfrs.v2.ShowFacesByLimitRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowFacesByLimitResponse`
        """
        return self.show_faces_by_limit_with_http_info(request)

    def show_faces_by_limit_with_http_info(self, request):
        all_params = ['face_set_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='ShowFacesByLimitResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_face(self, request):
        """更新人脸

        根据人脸ID（face_id）更新单张人脸信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateFace
        :type request: :class:`huaweicloudsdkfrs.v2.UpdateFaceRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.UpdateFaceResponse`
        """
        return self.update_face_with_http_info(request)

    def update_face_with_http_info(self, request):
        all_params = ['face_set_name', 'update_face_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

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
            cname=cname,
            response_type='UpdateFaceResponse',
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

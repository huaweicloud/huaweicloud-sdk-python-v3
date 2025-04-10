# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest

try:
    from huaweicloudsdkcore.invoker.invoker import AsyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkfrs'")


class FrsAsyncClient(Client):
    def __init__(self):
        super(FrsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkfrs.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "FrsAsyncClient":
                raise TypeError("client type error, support client type is FrsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_faces_by_base64_async(self, request):
        r"""添加人脸

        添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中，支持添加最大人脸或所有人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddFacesByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.AddFacesByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesByBase64Response`
        """
        http_info = self._add_faces_by_base64_http_info(request)
        return self._call_api(**http_info)

    def add_faces_by_base64_async_invoker(self, request):
        http_info = self._add_faces_by_base64_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_faces_by_base64_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "AddFacesByBase64Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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

    def add_faces_by_file_async(self, request):
        r"""添加人脸

        添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中，支持添加最大人脸或所有人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddFacesByFile
        :type request: :class:`huaweicloudsdkfrs.v2.AddFacesByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesByFileResponse`
        """
        http_info = self._add_faces_by_file_http_info(request)
        return self._call_api(**http_info)

    def add_faces_by_file_async_invoker(self, request):
        http_info = self._add_faces_by_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_faces_by_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "AddFacesByFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']
        if 'external_image_id' in local_var_params:
            form_params['external_image_id'] = local_var_params['external_image_id']
        if 'external_fields' in local_var_params:
            form_params['external_fields'] = local_var_params['external_fields']
        if 'single' in local_var_params:
            form_params['single'] = local_var_params['single']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def add_faces_by_url_async(self, request):
        r"""添加人脸

        添加人脸到人脸库中。将单张图片中的人脸添加至人脸库中，支持添加最大人脸或所有人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddFacesByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.AddFacesByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.AddFacesByUrlResponse`
        """
        http_info = self._add_faces_by_url_http_info(request)
        return self._call_api(**http_info)

    def add_faces_by_url_async_invoker(self, request):
        http_info = self._add_faces_by_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_faces_by_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "AddFacesByUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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

    def batch_delete_faces_async(self, request):
        r"""批量删除人脸

        自定义筛选条件，批量删除人脸库中的符合指定条件的多张人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteFaces
        :type request: :class:`huaweicloudsdkfrs.v2.BatchDeleteFacesRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.BatchDeleteFacesResponse`
        """
        http_info = self._batch_delete_faces_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_faces_async_invoker(self, request):
        http_info = self._batch_delete_faces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_faces_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces/batch",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteFacesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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

    def compare_face_by_base64_async(self, request):
        r"""人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CompareFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.CompareFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFaceByBase64Response`
        """
        http_info = self._compare_face_by_base64_http_info(request)
        return self._call_api(**http_info)

    def compare_face_by_base64_async_invoker(self, request):
        http_info = self._compare_face_by_base64_http_info(request)
        return AsyncInvoker(self, http_info)

    def _compare_face_by_base64_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-compare",
            "request_type": request.__class__.__name__,
            "response_type": "CompareFaceByBase64Response"
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

        response_headers = ["X-Request-Id", ]

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

    def compare_face_by_file_async(self, request):
        r"""人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CompareFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.CompareFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFaceByFileResponse`
        """
        http_info = self._compare_face_by_file_http_info(request)
        return self._call_api(**http_info)

    def compare_face_by_file_async_invoker(self, request):
        http_info = self._compare_face_by_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _compare_face_by_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-compare",
            "request_type": request.__class__.__name__,
            "response_type": "CompareFaceByFileResponse"
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
        if 'image1_file' in local_var_params:
            form_params['image1_file'] = local_var_params['image1_file']
        if 'image2_file' in local_var_params:
            form_params['image2_file'] = local_var_params['image2_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def compare_face_by_url_async(self, request):
        r"""人脸比对

        人脸比对是将两个人脸进行比对，来判断是否为同一个人，返回比对置信度。如果传入的图片中包含多个人脸，选取最大的人脸进行比对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CompareFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.CompareFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFaceByUrlResponse`
        """
        http_info = self._compare_face_by_url_http_info(request)
        return self._call_api(**http_info)

    def compare_face_by_url_async_invoker(self, request):
        http_info = self._compare_face_by_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _compare_face_by_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-compare",
            "request_type": request.__class__.__name__,
            "response_type": "CompareFaceByUrlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_face_set_async(self, request):
        r"""创建人脸库

        创建用于存储人脸特征的人脸库。您最多可以创建10个人脸库，每个人脸库最大容量为10万个人脸特征。如有更大规格的需求请联系客服。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateFaceSet
        :type request: :class:`huaweicloudsdkfrs.v2.CreateFaceSetRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.CreateFaceSetResponse`
        """
        http_info = self._create_face_set_http_info(request)
        return self._call_api(**http_info)

    def create_face_set_async_invoker(self, request):
        http_info = self._create_face_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_face_set_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateFaceSetResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def delete_face_by_external_image_id_async(self, request):
        r"""删除人脸

        根据external_image_id删除人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFaceByExternalImageId
        :type request: :class:`huaweicloudsdkfrs.v2.DeleteFaceByExternalImageIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFaceByExternalImageIdResponse`
        """
        http_info = self._delete_face_by_external_image_id_http_info(request)
        return self._call_api(**http_info)

    def delete_face_by_external_image_id_async_invoker(self, request):
        http_info = self._delete_face_by_external_image_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_face_by_external_image_id_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFaceByExternalImageIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []
        if 'external_image_id' in local_var_params:
            query_params.append(('external_image_id', local_var_params['external_image_id']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_face_by_face_id_async(self, request):
        r"""删除人脸

        根据face_id删除人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFaceByFaceId
        :type request: :class:`huaweicloudsdkfrs.v2.DeleteFaceByFaceIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFaceByFaceIdResponse`
        """
        http_info = self._delete_face_by_face_id_http_info(request)
        return self._call_api(**http_info)

    def delete_face_by_face_id_async_invoker(self, request):
        http_info = self._delete_face_by_face_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_face_by_face_id_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFaceByFaceIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []
        if 'face_id' in local_var_params:
            query_params.append(('face_id', local_var_params['face_id']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_face_set_async(self, request):
        r"""删除人脸库

        删除人脸库以及其中所有的人脸。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFaceSet
        :type request: :class:`huaweicloudsdkfrs.v2.DeleteFaceSetRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DeleteFaceSetResponse`
        """
        http_info = self._delete_face_set_http_info(request)
        return self._call_api(**http_info)

    def delete_face_set_async_invoker(self, request):
        http_info = self._delete_face_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_face_set_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFaceSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def detect_face_by_base64_async(self, request):
        r"""人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64Response`
        """
        http_info = self._detect_face_by_base64_http_info(request)
        return self._call_api(**http_info)

    def detect_face_by_base64_async_invoker(self, request):
        http_info = self._detect_face_by_base64_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_face_by_base64_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectFaceByBase64Response"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_face_by_base64_intl_async(self, request):
        r"""人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectFaceByBase64Intl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64IntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByBase64IntlResponse`
        """
        http_info = self._detect_face_by_base64_intl_http_info(request)
        return self._call_api(**http_info)

    def detect_face_by_base64_intl_async_invoker(self, request):
        http_info = self._detect_face_by_base64_intl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_face_by_base64_intl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectFaceByBase64IntlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_face_by_file_async(self, request):
        r"""人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileResponse`
        """
        http_info = self._detect_face_by_file_http_info(request)
        return self._call_api(**http_info)

    def detect_face_by_file_async_invoker(self, request):
        http_info = self._detect_face_by_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_face_by_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectFaceByFileResponse"
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
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']
        if 'attributes' in local_var_params:
            form_params['attributes'] = local_var_params['attributes']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def detect_face_by_file_intl_async(self, request):
        r"""人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectFaceByFileIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByFileIntlResponse`
        """
        http_info = self._detect_face_by_file_intl_http_info(request)
        return self._call_api(**http_info)

    def detect_face_by_file_intl_async_invoker(self, request):
        http_info = self._detect_face_by_file_intl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_face_by_file_intl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectFaceByFileIntlResponse"
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
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def detect_face_by_url_async(self, request):
        r"""人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlResponse`
        """
        http_info = self._detect_face_by_url_http_info(request)
        return self._call_api(**http_info)

    def detect_face_by_url_async_invoker(self, request):
        http_info = self._detect_face_by_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_face_by_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectFaceByUrlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_face_by_url_intl_async(self, request):
        r"""人脸检测

        人脸检测是对输入图片进行人脸检测和分析，输出人脸在图像中的位置、人脸关键点位置和人脸关键属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectFaceByUrlIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectFaceByUrlIntlResponse`
        """
        http_info = self._detect_face_by_url_intl_http_info(request)
        return self._call_api(**http_info)

    def detect_face_by_url_intl_async_invoker(self, request):
        http_info = self._detect_face_by_url_intl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_face_by_url_intl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectFaceByUrlIntlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_live_by_base64_async(self, request):
        r"""动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64Response`
        """
        http_info = self._detect_live_by_base64_http_info(request)
        return self._call_api(**http_info)

    def detect_live_by_base64_async_invoker(self, request):
        http_info = self._detect_live_by_base64_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_by_base64_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveByBase64Response"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_live_by_base64_intl_async(self, request):
        r"""动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveByBase64Intl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64IntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByBase64IntlResponse`
        """
        http_info = self._detect_live_by_base64_intl_http_info(request)
        return self._call_api(**http_info)

    def detect_live_by_base64_intl_async_invoker(self, request):
        http_info = self._detect_live_by_base64_intl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_by_base64_intl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/live-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveByBase64IntlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_live_by_file_async(self, request):
        r"""动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveByFile
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileResponse`
        """
        http_info = self._detect_live_by_file_http_info(request)
        return self._call_api(**http_info)

    def detect_live_by_file_async_invoker(self, request):
        http_info = self._detect_live_by_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_by_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveByFileResponse"
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
        if 'video_file' in local_var_params:
            form_params['video_file'] = local_var_params['video_file']
        if 'actions' in local_var_params:
            form_params['actions'] = local_var_params['actions']
        if 'action_time' in local_var_params:
            form_params['action_time'] = local_var_params['action_time']
        if 'nod_threshold' in local_var_params:
            form_params['nod_threshold'] = local_var_params['nod_threshold']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def detect_live_by_file_intl_async(self, request):
        r"""动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveByFileIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByFileIntlResponse`
        """
        http_info = self._detect_live_by_file_intl_http_info(request)
        return self._call_api(**http_info)

    def detect_live_by_file_intl_async_invoker(self, request):
        http_info = self._detect_live_by_file_intl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_by_file_intl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/live-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveByFileIntlResponse"
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
        if 'video_file' in local_var_params:
            form_params['video_file'] = local_var_params['video_file']
        if 'actions' in local_var_params:
            form_params['actions'] = local_var_params['actions']
        if 'action_time' in local_var_params:
            form_params['action_time'] = local_var_params['action_time']
        if 'nod_threshold' in local_var_params:
            form_params['nod_threshold'] = local_var_params['nod_threshold']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def detect_live_by_url_async(self, request):
        r"""动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlResponse`
        """
        http_info = self._detect_live_by_url_http_info(request)
        return self._call_api(**http_info)

    def detect_live_by_url_async_invoker(self, request):
        http_info = self._detect_live_by_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_by_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveByUrlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_live_by_url_intl_async(self, request):
        r"""动作活体检测

        动作活体检测是通过判断视频中的人物动作与传入动作列表是否一致来识别视频中人物是否为活体。如果有多张人脸出现，则选取最大的人脸进行判定。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveByUrlIntl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlIntlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveByUrlIntlResponse`
        """
        http_info = self._detect_live_by_url_intl_http_info(request)
        return self._call_api(**http_info)

    def detect_live_by_url_intl_async_invoker(self, request):
        http_info = self._detect_live_by_url_intl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_by_url_intl_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/live-detect",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveByUrlIntlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_live_face_by_base64_async(self, request):
        r"""静默活体检测

        静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息，判断图片中的人脸是否来自于真人活体，有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片，不支持多人脸图片。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByBase64Response`
        """
        http_info = self._detect_live_face_by_base64_http_info(request)
        return self._call_api(**http_info)

    def detect_live_face_by_base64_async_invoker(self, request):
        http_info = self._detect_live_face_by_base64_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_face_by_base64_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-detect-face",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveFaceByBase64Response"
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

        response_headers = ["X-Request-Id", ]

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

    def detect_live_face_by_file_async(self, request):
        r"""静默活体检测

        静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息，判断图片中的人脸是否来自于真人活体，有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片，不支持多人脸图片。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByFileResponse`
        """
        http_info = self._detect_live_face_by_file_http_info(request)
        return self._call_api(**http_info)

    def detect_live_face_by_file_async_invoker(self, request):
        http_info = self._detect_live_face_by_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_face_by_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-detect-face",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveFaceByFileResponse"
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
        if 'image_file' in local_var_params:
            form_params['image_file'] = local_var_params['image_file']

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def detect_live_face_by_url_async(self, request):
        r"""静默活体检测

        静默活体检测是基于人脸图片中可能存在的畸变、摩尔纹、反光、倒影、边框等信息，判断图片中的人脸是否来自于真人活体，有效抵御纸质翻拍照、电子翻拍照以及视频翻拍等各种攻击方式。静默活体检测支持单张图片，不支持多人脸图片。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetectLiveFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.DetectLiveFaceByUrlResponse`
        """
        http_info = self._detect_live_face_by_url_http_info(request)
        return self._call_api(**http_info)

    def detect_live_face_by_url_async_invoker(self, request):
        http_info = self._detect_live_face_by_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detect_live_face_by_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/live-detect-face",
            "request_type": request.__class__.__name__,
            "response_type": "DetectLiveFaceByUrlResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def search_face_by_base64_async(self, request):
        r"""人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchFaceByBase64
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByBase64Request`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByBase64Response`
        """
        http_info = self._search_face_by_base64_http_info(request)
        return self._call_api(**http_info)

    def search_face_by_base64_async_invoker(self, request):
        http_info = self._search_face_by_base64_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_face_by_base64_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchFaceByBase64Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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

    def search_face_by_face_id_async(self, request):
        r"""人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchFaceByFaceId
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByFaceIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByFaceIdResponse`
        """
        http_info = self._search_face_by_face_id_http_info(request)
        return self._call_api(**http_info)

    def search_face_by_face_id_async_invoker(self, request):
        http_info = self._search_face_by_face_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_face_by_face_id_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchFaceByFaceIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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

    def search_face_by_file_async(self, request):
        r"""人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchFaceByFile
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByFileRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByFileResponse`
        """
        http_info = self._search_face_by_file_http_info(request)
        return self._call_api(**http_info)

    def search_face_by_file_async_invoker(self, request):
        http_info = self._search_face_by_file_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_face_by_file_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchFaceByFileResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def search_face_by_url_async(self, request):
        r"""人脸搜索

        人脸搜索是指在已有的人脸库中，查询与目标人脸相似的一张或者多张人脸，并返回相应的置信度。
        支持传入图片或者faceID进行人脸搜索，如果传入的是多张人脸图片，选取图片中检测到的最大尺寸人脸作为检索的输入。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SearchFaceByUrl
        :type request: :class:`huaweicloudsdkfrs.v2.SearchFaceByUrlRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.SearchFaceByUrlResponse`
        """
        http_info = self._search_face_by_url_http_info(request)
        return self._call_api(**http_info)

    def search_face_by_url_async_invoker(self, request):
        http_info = self._search_face_by_url_http_info(request)
        return AsyncInvoker(self, http_info)

    def _search_face_by_url_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchFaceByUrlResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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

    def show_all_face_sets_async(self, request):
        r"""查询所有人脸库

        查询当前用户所有人脸库的状态信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowAllFaceSets
        :type request: :class:`huaweicloudsdkfrs.v2.ShowAllFaceSetsRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowAllFaceSetsResponse`
        """
        http_info = self._show_all_face_sets_http_info(request)
        return self._call_api(**http_info)

    def show_all_face_sets_async_invoker(self, request):
        http_info = self._show_all_face_sets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_all_face_sets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/face-sets",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAllFaceSetsResponse"
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
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_face_set_async(self, request):
        r"""查询人脸库

        查询人脸库当前的状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFaceSet
        :type request: :class:`huaweicloudsdkfrs.v2.ShowFaceSetRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowFaceSetResponse`
        """
        http_info = self._show_face_set_http_info(request)
        return self._call_api(**http_info)

    def show_face_set_async_invoker(self, request):
        http_info = self._show_face_set_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_face_set_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFaceSetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_faces_by_face_id_async(self, request):
        r"""查询人脸

        查询指定人脸库中人脸信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFacesByFaceId
        :type request: :class:`huaweicloudsdkfrs.v2.ShowFacesByFaceIdRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowFacesByFaceIdResponse`
        """
        http_info = self._show_faces_by_face_id_http_info(request)
        return self._call_api(**http_info)

    def show_faces_by_face_id_async_invoker(self, request):
        http_info = self._show_faces_by_face_id_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_faces_by_face_id_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFacesByFaceIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

        query_params = []
        if 'face_id' in local_var_params:
            query_params.append(('face_id', local_var_params['face_id']))

        header_params = {}
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_faces_by_limit_async(self, request):
        r"""查询人脸

        查询指定人脸库中人脸信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowFacesByLimit
        :type request: :class:`huaweicloudsdkfrs.v2.ShowFacesByLimitRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.ShowFacesByLimitResponse`
        """
        http_info = self._show_faces_by_limit_http_info(request)
        return self._call_api(**http_info)

    def show_faces_by_limit_async_invoker(self, request):
        http_info = self._show_faces_by_limit_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_faces_by_limit_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFacesByLimitResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
        if 'enterprise_project_id' in local_var_params:
            header_params['Enterprise-Project-Id'] = local_var_params['enterprise_project_id']

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_face_async(self, request):
        r"""更新人脸

        根据人脸ID（face_id）更新单张人脸信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateFace
        :type request: :class:`huaweicloudsdkfrs.v2.UpdateFaceRequest`
        :rtype: :class:`huaweicloudsdkfrs.v2.UpdateFaceResponse`
        """
        http_info = self._update_face_http_info(request)
        return self._call_api(**http_info)

    def update_face_async_invoker(self, request):
        http_info = self._update_face_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_face_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/face-sets/{face_set_name}/faces",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateFaceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'face_set_name' in local_var_params:
            path_params['face_set_name'] = local_var_params['face_set_name']

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

        response_headers = ["X-Request-Id", ]

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
            kwargs["async_request"] = True
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

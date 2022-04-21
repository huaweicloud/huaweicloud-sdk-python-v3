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


class ImageSearchAsyncClient(Client):
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
        super(ImageSearchAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkimagesearch.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "ImageSearchClient":
            raise TypeError("client type error, support client type is ImageSearchClient")

        return ClientBuilder(clazz)

    def run_add_picture_async(self, request):
        """添加图片

        添加图片
        将图片导入图片索引库，该图片可以是同一区域OBS桶内的图片或请求消息体里的图片，只有导入图片索引库的图片方可被搜索到。
        
        &gt; - 添加或搜索的图片存储在OBS的桶中时，需要对OBS的桶授权。在图像搜索服务管理控制台“实例管理”页面，单击实例操作列的“离线导入”，进入“离线导入”页面。选择存放数据的OBS桶，单击“授权”按钮，字体显示为灰色即完成OBS授权访问。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunAddPicture
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunAddPictureRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunAddPictureResponse`
        """
        return self.run_add_picture_with_http_info(request)

    def run_add_picture_with_http_info(self, request):
        all_params = ['instance_name', 'run_add_picture_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/{instance_name}/image',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunAddPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_check_picture_async(self, request):
        """查询图片

        通过图片路径查询索引库中对应图片是否存在。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunCheckPicture
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunCheckPictureRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunCheckPictureResponse`
        """
        return self.run_check_picture_with_http_info(request)

    def run_check_picture_with_http_info(self, request):
        all_params = ['instance_name', 'run_check_picture_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/{instance_name}/image/check',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunCheckPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_create_instance_async(self, request):
        """创建实例

        创建实例，实例中会生成图片索引库，用来存放图片特征。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunCreateInstance
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunCreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunCreateInstanceResponse`
        """
        return self.run_create_instance_with_http_info(request)

    def run_create_instance_with_http_info(self, request):
        all_params = ['run_create_instance_request_body']
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/service',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunCreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_delete_instance_async(self, request):
        """删除实例

        删除已存在的实例。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunDeleteInstance
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunDeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunDeleteInstanceResponse`
        """
        return self.run_delete_instance_with_http_info(request)

    def run_delete_instance_with_http_info(self, request):
        all_params = ['instance_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/service/{instance_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunDeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_delete_picture_async(self, request):
        """删除图片

        通过图片路径删除索引库中对应图片。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunDeletePicture
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunDeletePictureRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunDeletePictureResponse`
        """
        return self.run_delete_picture_with_http_info(request)

    def run_delete_picture_with_http_info(self, request):
        all_params = ['instance_name', 'run_delete_picture_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/{instance_name}/image',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunDeletePictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_modify_picture_async(self, request):
        """修改图片信息

        修改图像索引库中已存在的图片信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunModifyPicture
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunModifyPictureRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunModifyPictureResponse`
        """
        return self.run_modify_picture_with_http_info(request)

    def run_modify_picture_with_http_info(self, request):
        all_params = ['instance_name', 'run_modify_picture_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/{instance_name}/image',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunModifyPictureResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_query_instance_async(self, request):
        """查询用户实例信息

        查看用户指定实例详细信息。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunQueryInstance
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunQueryInstanceRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunQueryInstanceResponse`
        """
        return self.run_query_instance_with_http_info(request)

    def run_query_instance_with_http_info(self, request):
        all_params = ['instance_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/service/{instance_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunQueryInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_search_picture_async(self, request):
        """搜索图片

        从图片索引库中搜索相似图片。
        
        详细说明请参考华为云API Explorer。
        Please refer to Huawei cloud API Explorer for details.

        :param request: Request instance for RunSearchPicture
        :type request: :class:`huaweicloudsdkimagesearch.v1.RunSearchPictureRequest`
        :rtype: :class:`huaweicloudsdkimagesearch.v1.RunSearchPictureResponse`
        """
        return self.run_search_picture_with_http_info(request)

    def run_search_picture_with_http_info(self, request):
        all_params = ['instance_name', 'run_search_picture_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

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
            resource_path='/v1/{project_id}/{instance_name}/image/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RunSearchPictureResponse',
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
        :param header_params: Header parameters to be
            placed in the request header.
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
            request_type=request_type,
	    async_request=True)

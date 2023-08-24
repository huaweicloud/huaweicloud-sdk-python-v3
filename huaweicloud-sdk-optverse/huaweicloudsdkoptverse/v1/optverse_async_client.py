# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class OptVerseAsyncClient(Client):
    def __init__(self):
        super(OptVerseAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkoptverse.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "OptVerseClient":
            raise TypeError("client type error, support client type is OptVerseClient")

        return ClientBuilder(clazz)

    def create_task_async(self, request):
        """创建任务

        创建任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkoptverse.v1.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.CreateTaskResponse`
        """
        return self._create_task_with_http_info(request)

    def _create_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_group' in local_var_params:
            path_params['service_group'] = local_var_params['service_group']
        if 'service_type' in local_var_params:
            path_params['service_type'] = local_var_params['service_type']

        query_params = []

        header_params = {}
        if 'x_apig_app_code' in local_var_params:
            header_params['X-Apig-AppCode'] = local_var_params['x_apig_app_code']

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=utf-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/optverse/{service_group}/{service_type}/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_task_async(self, request):
        """删除任务

        删除任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkoptverse.v1.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.DeleteTaskResponse`
        """
        return self._delete_task_with_http_info(request)

    def _delete_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_group' in local_var_params:
            path_params['service_group'] = local_var_params['service_group']
        if 'service_type' in local_var_params:
            path_params['service_type'] = local_var_params['service_type']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}
        if 'x_apig_app_code' in local_var_params:
            header_params['X-Apig-AppCode'] = local_var_params['x_apig_app_code']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/optverse/{service_group}/{service_type}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_task_async(self, request):
        """查询任务列表

        查询任务列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTask
        :type request: :class:`huaweicloudsdkoptverse.v1.ListTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ListTaskResponse`
        """
        return self._list_task_with_http_info(request)

    def _list_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_group' in local_var_params:
            path_params['service_group'] = local_var_params['service_group']
        if 'service_type' in local_var_params:
            path_params['service_type'] = local_var_params['service_type']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}
        if 'x_apig_app_code' in local_var_params:
            header_params['X-Apig-AppCode'] = local_var_params['x_apig_app_code']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/optverse/{service_group}/{service_type}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_async(self, request):
        """获取任务详情

        获取任务详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkoptverse.v1.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkoptverse.v1.ShowTaskResponse`
        """
        return self._show_task_with_http_info(request)

    def _show_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'service_group' in local_var_params:
            path_params['service_group'] = local_var_params['service_group']
        if 'service_type' in local_var_params:
            path_params['service_type'] = local_var_params['service_type']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'input_enable' in local_var_params:
            query_params.append(('input_enable', local_var_params['input_enable']))

        header_params = {}
        if 'x_apig_app_code' in local_var_params:
            header_params['X-Apig-AppCode'] = local_var_params['x_apig_app_code']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/optverse/{service_group}/{service_type}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskResponse',
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

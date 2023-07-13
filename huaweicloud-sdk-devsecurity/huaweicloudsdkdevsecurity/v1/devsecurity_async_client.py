# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class DevSecurityAsyncClient(Client):
    def __init__(self):
        super(DevSecurityAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdevsecurity.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DevSecurityClient":
            raise TypeError("client type error, support client type is DevSecurityClient")

        return ClientBuilder(clazz)

    def create_sec_app_task_async(self, request):
        """创建移动应用安全任务并启动

        创建移动应用安全任务并启动
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSecAppTask
        :type request: :class:`huaweicloudsdkdevsecurity.v1.CreateSecAppTaskRequest`
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.CreateSecAppTaskResponse`
        """
        return self._create_sec_app_task_with_http_info(request)

    def _create_sec_app_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'version' in local_var_params:
            form_params['version'] = local_var_params['version']
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'privacy_statement_url' in local_var_params:
            form_params['privacy_statement_url'] = local_var_params['privacy_statement_url']
        if 'personal_info_share_url' in local_var_params:
            form_params['personal_info_share_url'] = local_var_params['personal_info_share_url']

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
            resource_path='/v1/{project_id}/secapp/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSecAppTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_sec_app_task_async(self, request):
        """删除移动应用安全任务

        删除移动应用安全任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSecAppTask
        :type request: :class:`huaweicloudsdkdevsecurity.v1.DeleteSecAppTaskRequest`
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.DeleteSecAppTaskResponse`
        """
        return self._delete_sec_app_task_with_http_info(request)

    def _delete_sec_app_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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
            resource_path='/v1/{project_id}/secapp/task',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteSecAppTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sec_app_task_result_async(self, request):
        """获取移动应用安全任务结果

        获取移动应用安全任务结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecAppTaskResult
        :type request: :class:`huaweicloudsdkdevsecurity.v1.ShowSecAppTaskResultRequest`
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.ShowSecAppTaskResultResponse`
        """
        return self._show_sec_app_task_result_with_http_info(request)

    def _show_sec_app_task_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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
            resource_path='/v1/{project_id}/secapp/task-result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecAppTaskResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_sec_app_task_status_async(self, request):
        """查询移动应用安全任务状态

        查询移动应用安全任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSecAppTaskStatus
        :type request: :class:`huaweicloudsdkdevsecurity.v1.ShowSecAppTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkdevsecurity.v1.ShowSecAppTaskStatusResponse`
        """
        return self._show_sec_app_task_status_with_http_info(request)

    def _show_sec_app_task_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in local_var_params:
            query_params.append(('task_id', local_var_params['task_id']))

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
            resource_path='/v1/{project_id}/secapp/task-status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSecAppTaskStatusResponse',
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

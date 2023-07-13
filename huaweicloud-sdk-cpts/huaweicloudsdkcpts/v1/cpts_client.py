# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CptsClient(Client):
    def __init__(self):
        super(CptsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcpts.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CptsClient":
            raise TypeError("client type error, support client type is CptsClient")

        return ClientBuilder(clazz)

    def batch_update_task_status(self, request):
        """批量启停任务

        批量启停任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateTaskStatus
        :type request: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusResponse`
        """
        return self._batch_update_task_status_with_http_info(request)

    def _batch_update_task_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suit_id' in local_var_params:
            path_params['test_suit_id'] = local_var_params['test_suit_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suit_id}/tasks/batch-update-task-status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateTaskStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_case(self, request):
        """创建用例

        创建用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCase
        :type request: :class:`huaweicloudsdkcpts.v1.CreateCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateCaseResponse`
        """
        return self._create_case_with_http_info(request)

    def _create_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/task-cases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_directory(self, request):
        """创建目录

        创建目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDirectory
        :type request: :class:`huaweicloudsdkcpts.v1.CreateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateDirectoryResponse`
        """
        return self._create_directory_with_http_info(request)

    def _create_directory_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}/directory',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDirectoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_new_case(self, request):
        """创建用例v2

        创建用例v2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNewCase
        :type request: :class:`huaweicloudsdkcpts.v1.CreateNewCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateNewCaseResponse`
        """
        return self._create_new_case_with_http_info(request)

    def _create_new_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v2/{project_id}/test-cases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNewCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_new_task(self, request):
        """创建任务v3

        创建任务v3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNewTask
        :type request: :class:`huaweicloudsdkcpts.v1.CreateNewTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateNewTaskResponse`
        """
        return self._create_new_task_with_http_info(request)

    def _create_new_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v3/{project_id}/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNewTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_task(self, request):
        """创建任务

        创建任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkcpts.v1.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateTaskResponse`
        """
        return self._create_task_with_http_info(request)

    def _create_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/tasks',
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

    def create_temp(self, request):
        """创建事务

        创建事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemp
        :type request: :class:`huaweicloudsdkcpts.v1.CreateTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateTempResponse`
        """
        return self._create_temp_with_http_info(request)

    def _create_temp_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTempResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_variable(self, request):
        """创建变量

        创建变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVariable
        :type request: :class:`huaweicloudsdkcpts.v1.CreateVariableRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateVariableResponse`
        """
        return self._create_variable_with_http_info(request)

    def _create_variable_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/variables/{test_suite_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateVariableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def debug_case(self, request):
        """调试用例

        调试用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugCase
        :type request: :class:`huaweicloudsdkcpts.v1.DebugCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DebugCaseResponse`
        """
        return self._debug_case_with_http_info(request)

    def _debug_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}/tasks/{task_id}/cases/{case_id}/debug',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DebugCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_case(self, request):
        """删除用例

        删除用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCase
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteCaseResponse`
        """
        return self._delete_case_with_http_info(request)

    def _delete_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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
            resource_path='/v1/{project_id}/task-cases/{case_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_directory(self, request):
        """删除目录

        删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDirectory
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteDirectoryRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteDirectoryResponse`
        """
        return self._delete_directory_with_http_info(request)

    def _delete_directory_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'directory_id' in local_var_params:
            path_params['directory_id'] = local_var_params['directory_id']
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}/directory/{directory_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDirectoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_new_case(self, request):
        """删除用例v2

        删除用例v2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNewCase
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteNewCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteNewCaseResponse`
        """
        return self._delete_new_case_with_http_info(request)

    def _delete_new_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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
            resource_path='/v2/{project_id}/test-cases/{case_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNewCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_new_task(self, request):
        """删除任务v3

        删除任务v3
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNewTask
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteNewTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteNewTaskResponse`
        """
        return self._delete_new_task_with_http_info(request)

    def _delete_new_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/{project_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNewTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_task(self, request):
        """删除任务

        删除任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteTaskResponse`
        """
        return self._delete_task_with_http_info(request)

    def _delete_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1/{project_id}/tasks/{task_id}',
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

    def delete_temp(self, request):
        """删除事务

        删除事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemp
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteTempResponse`
        """
        return self._delete_temp_with_http_info(request)

    def _delete_temp_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1/{project_id}/templates/{template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTempResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_variable(self, request):
        """删除全局变量

        删除全局变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVariable
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteVariableRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteVariableResponse`
        """
        return self._delete_variable_with_http_info(request)

    def _delete_variable_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'variable_id' in local_var_params:
            query_params.append(('variable_id', local_var_params['variable_id']))
        if 'test_suite_id' in local_var_params:
            query_params.append(('test_suite_id', local_var_params['test_suite_id']))

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
            resource_path='/v1/{project_id}/variables',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteVariableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_test_case(self, request):
        """查询用例树

        查询用例树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTestCase
        :type request: :class:`huaweicloudsdkcpts.v1.ListProjectTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListProjectTestCaseResponse`
        """
        return self._list_project_test_case_with_http_info(request)

    def _list_project_test_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}/directory',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectTestCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_task_cases(self, request):
        """获取任务关联的用例列表

        获取任务关联的用例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskCases
        :type request: :class:`huaweicloudsdkcpts.v1.ListTaskCasesRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListTaskCasesResponse`
        """
        return self._list_task_cases_with_http_info(request)

    def _list_task_cases_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suit_id' in local_var_params:
            path_params['test_suit_id'] = local_var_params['test_suit_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suit_id}/tasks/{task_id}/test-cases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTaskCasesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_variables(self, request):
        """查询全局变量

        查询全局变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVariables
        :type request: :class:`huaweicloudsdkcpts.v1.ListVariablesRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListVariablesResponse`
        """
        return self._list_variables_with_http_info(request)

    def _list_variables_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'variable_type' in local_var_params:
            path_params['variable_type'] = local_var_params['variable_type']
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/variables/{variable_type}/test-suites/{test_suite_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVariablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_agent_config(self, request):
        """全链路压测探针获取配置信息

        全链路压测探针获取配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgentConfig
        :type request: :class:`huaweicloudsdkcpts.v1.ShowAgentConfigRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowAgentConfigResponse`
        """
        return self._show_agent_config_with_http_info(request)

    def _show_agent_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/stress/agents',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAgentConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_case(self, request):
        """查询用例

        查询用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCase
        :type request: :class:`huaweicloudsdkcpts.v1.ShowCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowCaseResponse`
        """
        return self._show_case_with_http_info(request)

    def _show_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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
            resource_path='/v2/{project_id}/test-cases/{case_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_history_run_info(self, request):
        """查询PerfTest任务离线报告列表

        查询PerfTest任务离线报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryRunInfo
        :type request: :class:`huaweicloudsdkcpts.v1.ShowHistoryRunInfoRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowHistoryRunInfoResponse`
        """
        return self._show_history_run_info_with_http_info(request)

    def _show_history_run_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1/{project_id}/tasks/history-run-list/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHistoryRunInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_merge_case_detail(self, request):
        """内外融合单个用例的详情数据

        查询单个用例的详情数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeCaseDetail
        :type request: :class:`huaweicloudsdkcpts.v1.ShowMergeCaseDetailRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowMergeCaseDetailResponse`
        """
        return self._show_merge_case_detail_with_http_info(request)

    def _show_merge_case_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']
        if 'case_run_id' in local_var_params:
            path_params['case_run_id'] = local_var_params['case_run_id']

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
            resource_path='/v2/{project_id}/task-run-infos/{task_run_id}/case-run-infos/{case_run_id}/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMergeCaseDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_merge_report_logs_outline(self, request):
        """查询报告汇总数据接口

        查询报告汇总数据接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeReportLogsOutline
        :type request: :class:`huaweicloudsdkcpts.v1.ShowMergeReportLogsOutlineRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowMergeReportLogsOutlineResponse`
        """
        return self._show_merge_report_logs_outline_with_http_info(request)

    def _show_merge_report_logs_outline_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']

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
            resource_path='/v2/{project_id}/task-run-infos/{task_run_id}/reports/log-outline',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMergeReportLogsOutlineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_merge_task_case(self, request):
        """内外融合当前任务用例列表接口

        查询当前任务用例列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeTaskCase
        :type request: :class:`huaweicloudsdkcpts.v1.ShowMergeTaskCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowMergeTaskCaseResponse`
        """
        return self._show_merge_task_case_with_http_info(request)

    def _show_merge_task_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']

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
            resource_path='/v2/{project_id}/task-run-infos/{task_run_id}/cases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMergeTaskCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_report(self, request):
        """查询报告

        查询报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReport
        :type request: :class:`huaweicloudsdkcpts.v1.ShowReportRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowReportResponse`
        """
        return self._show_report_with_http_info(request)

    def _show_report_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']
        if 'case_run_id' in local_var_params:
            path_params['case_run_id'] = local_var_params['case_run_id']

        query_params = []
        if 'brokens_limit_count' in local_var_params:
            query_params.append(('brokens_limit_count', local_var_params['brokens_limit_count']))

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
            resource_path='/v1/{project_id}/task-run-infos/{task_run_id}/case-run-infos/{case_run_id}/reports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowReportResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task(self, request):
        """查询任务

        查询任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTaskResponse`
        """
        return self._show_task_with_http_info(request)

    def _show_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1/{project_id}/tasks/{task_id}',
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

    def show_task_case_aw_chart(self, request):
        """内外融合获取用例的AW曲线图获取接口

        内外融合获取用例的AW曲线图获取接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskCaseAwChart
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTaskCaseAwChartRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTaskCaseAwChartResponse`
        """
        return self._show_task_case_aw_chart_with_http_info(request)

    def _show_task_case_aw_chart_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']
        if 'case_run_id' in local_var_params:
            path_params['case_run_id'] = local_var_params['case_run_id']
        if 'detail_id' in local_var_params:
            path_params['detail_id'] = local_var_params['detail_id']

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
            resource_path='/v2/{project_id}/task-run-infos/{task_run_id}/case-run-infos/{case_run_id}/detail/{detail_id}/chart',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskCaseAwChartResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_set(self, request):
        """查询任务集

        查询任务集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskSet
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTaskSetRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTaskSetResponse`
        """
        return self._show_task_set_with_http_info(request)

    def _show_task_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/all-tasks/{test_suite_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_temp(self, request):
        """查询事务

        查询事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemp
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTempResponse`
        """
        return self._show_temp_with_http_info(request)

    def _show_temp_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1/{project_id}/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTempResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_temp_set(self, request):
        """查询事务集

        查询事务集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTempSet
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTempSetRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTempSetResponse`
        """
        return self._show_temp_set_with_http_info(request)

    def _show_temp_set_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/all-templates/{test_suite_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTempSetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_agent_health_status(self, request):
        """全链路压测探针上报健康状态

        全链路压测探针上报健康状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgentHealthStatus
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateAgentHealthStatusRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateAgentHealthStatusResponse`
        """
        return self._update_agent_health_status_with_http_info(request)

    def _update_agent_health_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

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
            resource_path='/v1/{project_id}/stress/agents/{agent_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAgentHealthStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_case(self, request):
        """修改用例

        修改用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCase
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateCaseResponse`
        """
        return self._update_case_with_http_info(request)

    def _update_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']
        if 'target' in local_var_params:
            path_params['target'] = local_var_params['target']

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
            resource_path='/v1/{project_id}/task-cases/{case_id}/target/{target}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_directory(self, request):
        """修改目录

        修改目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDirectory
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryResponse`
        """
        return self._update_directory_with_http_info(request)

    def _update_directory_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'directory_id' in local_var_params:
            path_params['directory_id'] = local_var_params['directory_id']
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}/directory/{directory_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDirectoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_new_case(self, request):
        """修改用例v2

        修改用例v2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNewCase
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateNewCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateNewCaseResponse`
        """
        return self._update_new_case_with_http_info(request)

    def _update_new_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

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
            resource_path='/v2/{project_id}/test-cases/{case_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNewCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_task(self, request):
        """修改任务

        修改任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTask
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskResponse`
        """
        return self._update_task_with_http_info(request)

    def _update_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1/{project_id}/tasks/{task_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_task_related_test_case(self, request):
        """修改任务关联用例

        修改任务关联用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskRelatedTestCase
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTaskRelatedTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskRelatedTestCaseResponse`
        """
        return self._update_task_related_test_case_with_http_info(request)

    def _update_task_related_test_case_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v3/{project_id}/tasks/{task_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskRelatedTestCaseResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_task_status(self, request):
        """更新任务状态

        更新任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskStatus
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusResponse`
        """
        return self._update_task_status_with_http_info(request)

    def _update_task_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}/tasks/{task_id}',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTaskStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_temp(self, request):
        """修改事务

        修改事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemp
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTempResponse`
        """
        return self._update_temp_with_http_info(request)

    def _update_temp_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

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
            resource_path='/v1/{project_id}/templates/{template_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateTempResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_variable(self, request):
        """修改变量

        修改变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVariable
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateVariableRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateVariableResponse`
        """
        return self._update_variable_with_http_info(request)

    def _update_variable_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/variables/{test_suite_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVariableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project(self, request):
        """创建工程

        创建工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkcpts.v1.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateProjectResponse`
        """
        return self._create_project_with_http_info(request)

    def _create_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/test-suites',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_project(self, request):
        """删除工程

        删除工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProject
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteProjectResponse`
        """
        return self._delete_project_with_http_info(request)

    def _delete_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_project_sets(self, request):
        """查询工程集

        查询工程集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectSets
        :type request: :class:`huaweicloudsdkcpts.v1.ListProjectSetsRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListProjectSetsResponse`
        """
        return self._list_project_sets_with_http_info(request)

    def _list_project_sets_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

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
            resource_path='/v1/{project_id}/test-suites',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectSetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_process(self, request):
        """查询导入进度

        查询导入进度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProcess
        :type request: :class:`huaweicloudsdkcpts.v1.ShowProcessRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowProcessResponse`
        """
        return self._show_process_with_http_info(request)

    def _show_process_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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
            resource_path='/v1/{project_id}/test-suites/upload/processes',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProcessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project(self, request):
        """查询工程

        查询工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProject
        :type request: :class:`huaweicloudsdkcpts.v1.ShowProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowProjectResponse`
        """
        return self._show_project_with_http_info(request)

    def _show_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project(self, request):
        """修改工程

        修改工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProject
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateProjectResponse`
        """
        return self._update_project_with_http_info(request)

    def _update_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

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
            resource_path='/v1/{project_id}/test-suites/{test_suite_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProjectResponse',
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

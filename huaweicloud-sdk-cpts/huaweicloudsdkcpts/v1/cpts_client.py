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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcpts'")


class CptsClient(Client):
    def __init__(self):
        super(CptsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcpts.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CptsClient":
                raise TypeError("client type error, support client type is CptsClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_update_task_status(self, request):
        """批量启停任务

        批量启停任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateTaskStatus
        :type request: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusResponse`
        """
        http_info = self._batch_update_task_status_http_info(request)
        return self._call_api(**http_info)

    def batch_update_task_status_invoker(self, request):
        http_info = self._batch_update_task_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_update_task_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/test-suites/{test_suit_id}/tasks/batch-update-task-status",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateTaskStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suit_id' in local_var_params:
            path_params['test_suit_id'] = local_var_params['test_suit_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_case(self, request):
        """创建用例（旧版）

        创建用例（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCase
        :type request: :class:`huaweicloudsdkcpts.v1.CreateCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateCaseResponse`
        """
        http_info = self._create_case_http_info(request)
        return self._call_api(**http_info)

    def create_case_invoker(self, request):
        http_info = self._create_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/task-cases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_directory(self, request):
        """创建目录

        创建目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDirectory
        :type request: :class:`huaweicloudsdkcpts.v1.CreateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateDirectoryResponse`
        """
        http_info = self._create_directory_http_info(request)
        return self._call_api(**http_info)

    def create_directory_invoker(self, request):
        http_info = self._create_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_directory_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}/directory",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDirectoryResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_new_case(self, request):
        """创建用例

        创建用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNewCase
        :type request: :class:`huaweicloudsdkcpts.v1.CreateNewCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateNewCaseResponse`
        """
        http_info = self._create_new_case_http_info(request)
        return self._call_api(**http_info)

    def create_new_case_invoker(self, request):
        http_info = self._create_new_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_new_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/test-cases",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNewCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_new_task(self, request):
        """创建任务

        创建任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNewTask
        :type request: :class:`huaweicloudsdkcpts.v1.CreateNewTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateNewTaskResponse`
        """
        http_info = self._create_new_task_http_info(request)
        return self._call_api(**http_info)

    def create_new_task_invoker(self, request):
        http_info = self._create_new_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_new_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNewTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_task(self, request):
        """创建任务（旧版）

        创建任务（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdkcpts.v1.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateTaskResponse`
        """
        http_info = self._create_task_http_info(request)
        return self._call_api(**http_info)

    def create_task_invoker(self, request):
        http_info = self._create_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_temp(self, request):
        """创建事务

        创建事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemp
        :type request: :class:`huaweicloudsdkcpts.v1.CreateTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateTempResponse`
        """
        http_info = self._create_temp_http_info(request)
        return self._call_api(**http_info)

    def create_temp_invoker(self, request):
        http_info = self._create_temp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_temp_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTempResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_variable(self, request):
        """创建变量

        创建变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateVariable
        :type request: :class:`huaweicloudsdkcpts.v1.CreateVariableRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateVariableResponse`
        """
        http_info = self._create_variable_http_info(request)
        return self._call_api(**http_info)

    def create_variable_invoker(self, request):
        http_info = self._create_variable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_variable_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/variables/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "CreateVariableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def debug_case(self, request):
        """调试用例

        调试用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DebugCase
        :type request: :class:`huaweicloudsdkcpts.v1.DebugCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DebugCaseResponse`
        """
        http_info = self._debug_case_http_info(request)
        return self._call_api(**http_info)

    def debug_case_invoker(self, request):
        http_info = self._debug_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _debug_case_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}/tasks/{task_id}/cases/{case_id}/debug",
            "request_type": request.__class__.__name__,
            "response_type": "DebugCaseResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_case(self, request):
        """删除用例（旧版）

        删除用例（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCase
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteCaseResponse`
        """
        http_info = self._delete_case_http_info(request)
        return self._call_api(**http_info)

    def delete_case_invoker(self, request):
        http_info = self._delete_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_case_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/task-cases/{case_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_directory(self, request):
        """删除目录

        删除目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDirectory
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteDirectoryRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteDirectoryResponse`
        """
        http_info = self._delete_directory_http_info(request)
        return self._call_api(**http_info)

    def delete_directory_invoker(self, request):
        http_info = self._delete_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_directory_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}/directory/{directory_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDirectoryResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_new_case(self, request):
        """删除用例

        删除用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNewCase
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteNewCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteNewCaseResponse`
        """
        http_info = self._delete_new_case_http_info(request)
        return self._call_api(**http_info)

    def delete_new_case_invoker(self, request):
        http_info = self._delete_new_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_new_case_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/test-cases/{case_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNewCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_new_task(self, request):
        """删除任务

        删除任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNewTask
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteNewTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteNewTaskResponse`
        """
        http_info = self._delete_new_task_http_info(request)
        return self._call_api(**http_info)

    def delete_new_task_invoker(self, request):
        http_info = self._delete_new_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_new_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNewTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_task(self, request):
        """删除任务（旧版）

        删除任务（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteTaskResponse`
        """
        http_info = self._delete_task_http_info(request)
        return self._call_api(**http_info)

    def delete_task_invoker(self, request):
        http_info = self._delete_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_temp(self, request):
        """删除事务

        删除事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemp
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteTempResponse`
        """
        http_info = self._delete_temp_http_info(request)
        return self._call_api(**http_info)

    def delete_temp_invoker(self, request):
        http_info = self._delete_temp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_temp_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTempResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_variable(self, request):
        """删除全局变量

        删除全局变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteVariable
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteVariableRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteVariableResponse`
        """
        http_info = self._delete_variable_http_info(request)
        return self._call_api(**http_info)

    def delete_variable_invoker(self, request):
        http_info = self._delete_variable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_variable_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/variables",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteVariableResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def list_project_test_case(self, request):
        """查询用例树

        查询用例树
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectTestCase
        :type request: :class:`huaweicloudsdkcpts.v1.ListProjectTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListProjectTestCaseResponse`
        """
        http_info = self._list_project_test_case_http_info(request)
        return self._call_api(**http_info)

    def list_project_test_case_invoker(self, request):
        http_info = self._list_project_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_test_case_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}/directory",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTestCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def list_task_cases(self, request):
        """获取任务关联的用例列表

        获取任务关联的用例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskCases
        :type request: :class:`huaweicloudsdkcpts.v1.ListTaskCasesRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListTaskCasesResponse`
        """
        http_info = self._list_task_cases_http_info(request)
        return self._call_api(**http_info)

    def list_task_cases_invoker(self, request):
        http_info = self._list_task_cases_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_task_cases_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/test-suites/{test_suit_id}/tasks/{task_id}/test-cases",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskCasesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def list_variables(self, request):
        """查询全局变量

        查询全局变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVariables
        :type request: :class:`huaweicloudsdkcpts.v1.ListVariablesRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListVariablesResponse`
        """
        http_info = self._list_variables_http_info(request)
        return self._call_api(**http_info)

    def list_variables_invoker(self, request):
        http_info = self._list_variables_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_variables_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/variables/{variable_type}/test-suites/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListVariablesResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_agent_config(self, request):
        """全链路压测探针获取配置信息

        全链路压测探针获取配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAgentConfig
        :type request: :class:`huaweicloudsdkcpts.v1.ShowAgentConfigRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowAgentConfigResponse`
        """
        http_info = self._show_agent_config_http_info(request)
        return self._call_api(**http_info)

    def show_agent_config_invoker(self, request):
        http_info = self._show_agent_config_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_agent_config_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/stress/agents",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAgentConfigResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_case(self, request):
        """查询用例

        查询用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCase
        :type request: :class:`huaweicloudsdkcpts.v1.ShowCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowCaseResponse`
        """
        http_info = self._show_case_http_info(request)
        return self._call_api(**http_info)

    def show_case_invoker(self, request):
        http_info = self._show_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_case_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/test-cases/{case_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_history_run_info(self, request):
        """查询PerfTest任务离线报告列表

        查询PerfTest任务离线报告列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHistoryRunInfo
        :type request: :class:`huaweicloudsdkcpts.v1.ShowHistoryRunInfoRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowHistoryRunInfoResponse`
        """
        http_info = self._show_history_run_info_http_info(request)
        return self._call_api(**http_info)

    def show_history_run_info_invoker(self, request):
        http_info = self._show_history_run_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_history_run_info_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tasks/history-run-list/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHistoryRunInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_merge_case_detail(self, request):
        """查询用例报告详情

        查询用例报告详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeCaseDetail
        :type request: :class:`huaweicloudsdkcpts.v1.ShowMergeCaseDetailRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowMergeCaseDetailResponse`
        """
        http_info = self._show_merge_case_detail_http_info(request)
        return self._call_api(**http_info)

    def show_merge_case_detail_invoker(self, request):
        http_info = self._show_merge_case_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_merge_case_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/task-run-infos/{task_run_id}/case-run-infos/{case_run_id}/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeCaseDetailResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_merge_report_logs_outline(self, request):
        """查询报告汇总数据

        查询报告汇总数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeReportLogsOutline
        :type request: :class:`huaweicloudsdkcpts.v1.ShowMergeReportLogsOutlineRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowMergeReportLogsOutlineResponse`
        """
        http_info = self._show_merge_report_logs_outline_http_info(request)
        return self._call_api(**http_info)

    def show_merge_report_logs_outline_invoker(self, request):
        http_info = self._show_merge_report_logs_outline_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_merge_report_logs_outline_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/task-run-infos/{task_run_id}/reports/log-outline",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeReportLogsOutlineResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_merge_task_case(self, request):
        """查询任务报告的用例列表

        查询任务报告的用例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMergeTaskCase
        :type request: :class:`huaweicloudsdkcpts.v1.ShowMergeTaskCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowMergeTaskCaseResponse`
        """
        http_info = self._show_merge_task_case_http_info(request)
        return self._call_api(**http_info)

    def show_merge_task_case_invoker(self, request):
        http_info = self._show_merge_task_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_merge_task_case_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/task-run-infos/{task_run_id}/cases",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMergeTaskCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_run_id' in local_var_params:
            path_params['task_run_id'] = local_var_params['task_run_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_report(self, request):
        """查询报告

        查询报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowReport
        :type request: :class:`huaweicloudsdkcpts.v1.ShowReportRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowReportResponse`
        """
        http_info = self._show_report_http_info(request)
        return self._call_api(**http_info)

    def show_report_invoker(self, request):
        http_info = self._show_report_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_report_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/task-run-infos/{task_run_id}/case-run-infos/{case_run_id}/reports",
            "request_type": request.__class__.__name__,
            "response_type": "ShowReportResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_task(self, request):
        """查询任务（旧版）

        查询任务（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_task_case_aw_chart(self, request):
        """查询用例的AW曲线图

        查询用例的AW曲线图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskCaseAwChart
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTaskCaseAwChartRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTaskCaseAwChartResponse`
        """
        http_info = self._show_task_case_aw_chart_http_info(request)
        return self._call_api(**http_info)

    def show_task_case_aw_chart_invoker(self, request):
        http_info = self._show_task_case_aw_chart_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_case_aw_chart_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/task-run-infos/{task_run_id}/case-run-infos/{case_run_id}/detail/{detail_id}/chart",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskCaseAwChartResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_task_set(self, request):
        """查询任务集

        查询任务集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskSet
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTaskSetRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTaskSetResponse`
        """
        http_info = self._show_task_set_http_info(request)
        return self._call_api(**http_info)

    def show_task_set_invoker(self, request):
        http_info = self._show_task_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_task_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/all-tasks/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTaskSetResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_temp(self, request):
        """查询事务

        查询事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemp
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTempResponse`
        """
        http_info = self._show_temp_http_info(request)
        return self._call_api(**http_info)

    def show_temp_invoker(self, request):
        http_info = self._show_temp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_temp_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTempResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_temp_set(self, request):
        """查询事务集

        查询事务集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTempSet
        :type request: :class:`huaweicloudsdkcpts.v1.ShowTempSetRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowTempSetResponse`
        """
        http_info = self._show_temp_set_http_info(request)
        return self._call_api(**http_info)

    def show_temp_set_invoker(self, request):
        http_info = self._show_temp_set_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_temp_set_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/all-templates/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTempSetResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_agent_health_status(self, request):
        """全链路压测探针上报健康状态

        全链路压测探针上报健康状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAgentHealthStatus
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateAgentHealthStatusRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateAgentHealthStatusResponse`
        """
        http_info = self._update_agent_health_status_http_info(request)
        return self._call_api(**http_info)

    def update_agent_health_status_invoker(self, request):
        http_info = self._update_agent_health_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_agent_health_status_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/stress/agents/{agent_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateAgentHealthStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_case(self, request):
        """修改用例（旧版）

        修改用例（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateCase
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateCaseResponse`
        """
        http_info = self._update_case_http_info(request)
        return self._call_api(**http_info)

    def update_case_invoker(self, request):
        http_info = self._update_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_case_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/task-cases/{case_id}/target/{target}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCaseResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_directory(self, request):
        """修改目录

        修改目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDirectory
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateDirectoryResponse`
        """
        http_info = self._update_directory_http_info(request)
        return self._call_api(**http_info)

    def update_directory_invoker(self, request):
        http_info = self._update_directory_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_directory_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}/directory/{directory_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDirectoryResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_new_case(self, request):
        """修改用例

        修改用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNewCase
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateNewCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateNewCaseResponse`
        """
        http_info = self._update_new_case_http_info(request)
        return self._call_api(**http_info)

    def update_new_case_invoker(self, request):
        http_info = self._update_new_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_new_case_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/test-cases/{case_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNewCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'case_id' in local_var_params:
            path_params['case_id'] = local_var_params['case_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_task(self, request):
        """修改任务（旧版）

        修改任务（旧版）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTask
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTaskRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskResponse`
        """
        http_info = self._update_task_http_info(request)
        return self._call_api(**http_info)

    def update_task_invoker(self, request):
        http_info = self._update_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_task_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_task_related_test_case(self, request):
        """修改任务关联用例

        修改任务关联用例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskRelatedTestCase
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTaskRelatedTestCaseRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskRelatedTestCaseResponse`
        """
        http_info = self._update_task_related_test_case_http_info(request)
        return self._call_api(**http_info)

    def update_task_related_test_case_invoker(self, request):
        http_info = self._update_task_related_test_case_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_task_related_test_case_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskRelatedTestCaseResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_task_status(self, request):
        """更新任务状态

        更新任务状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTaskStatus
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusResponse`
        """
        http_info = self._update_task_status_http_info(request)
        return self._call_api(**http_info)

    def update_task_status_invoker(self, request):
        http_info = self._update_task_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_task_status_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskStatusResponse"
            }

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

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_temp(self, request):
        """修改事务

        修改事务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateTemp
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateTempRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTempResponse`
        """
        http_info = self._update_temp_http_info(request)
        return self._call_api(**http_info)

    def update_temp_invoker(self, request):
        http_info = self._update_temp_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_temp_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/templates/{template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTempResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_variable(self, request):
        """修改变量

        修改变量
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVariable
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateVariableRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateVariableResponse`
        """
        http_info = self._update_variable_http_info(request)
        return self._call_api(**http_info)

    def update_variable_invoker(self, request):
        http_info = self._update_variable_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_variable_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/variables/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateVariableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def create_project(self, request):
        """创建工程

        创建工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkcpts.v1.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.CreateProjectResponse`
        """
        http_info = self._create_project_http_info(request)
        return self._call_api(**http_info)

    def create_project_invoker(self, request):
        http_info = self._create_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_project_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/test-suites",
            "request_type": request.__class__.__name__,
            "response_type": "CreateProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def delete_project(self, request):
        """删除工程

        删除工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProject
        :type request: :class:`huaweicloudsdkcpts.v1.DeleteProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.DeleteProjectResponse`
        """
        http_info = self._delete_project_http_info(request)
        return self._call_api(**http_info)

    def delete_project_invoker(self, request):
        http_info = self._delete_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_project_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def list_project_sets(self, request):
        """查询工程集

        查询工程集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProjectSets
        :type request: :class:`huaweicloudsdkcpts.v1.ListProjectSetsRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ListProjectSetsResponse`
        """
        http_info = self._list_project_sets_http_info(request)
        return self._call_api(**http_info)

    def list_project_sets_invoker(self, request):
        http_info = self._list_project_sets_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_project_sets_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/test-suites",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectSetsResponse"
            }

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

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_process(self, request):
        """查询导入进度

        查询导入进度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProcess
        :type request: :class:`huaweicloudsdkcpts.v1.ShowProcessRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowProcessResponse`
        """
        http_info = self._show_process_http_info(request)
        return self._call_api(**http_info)

    def show_process_invoker(self, request):
        http_info = self._show_process_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_process_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/test-suites/upload/processes",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProcessResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def show_project(self, request):
        """查询工程

        查询工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProject
        :type request: :class:`huaweicloudsdkcpts.v1.ShowProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.ShowProjectResponse`
        """
        http_info = self._show_project_http_info(request)
        return self._call_api(**http_info)

    def show_project_invoker(self, request):
        http_info = self._show_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

    def update_project(self, request):
        """修改工程

        修改工程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProject
        :type request: :class:`huaweicloudsdkcpts.v1.UpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateProjectResponse`
        """
        http_info = self._update_project_http_info(request)
        return self._call_api(**http_info)

    def update_project_invoker(self, request):
        http_info = self._update_project_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_project_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/test-suites/{test_suite_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateProjectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'test_suite_id' in local_var_params:
            path_params['test_suite_id'] = local_var_params['test_suite_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

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

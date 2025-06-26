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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksms'")


class SmsAsyncClient(Client):
    def __init__(self):
        super(SmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksms.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SmsAsyncClient":
                raise TypeError("client type error, support client type is SmsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def collect_log_async(self, request):
        r"""上传迁移任务的日志

        上传迁移任务的日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CollectLog
        :type request: :class:`huaweicloudsdksms.v3.CollectLogRequest`
        :rtype: :class:`huaweicloudsdksms.v3.CollectLogResponse`
        """
        http_info = self._collect_log_http_info(request)
        return self._call_api(**http_info)

    def collect_log_async_invoker(self, request):
        http_info = self._collect_log_http_info(request)
        return AsyncInvoker(self, http_info)

    def _collect_log_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/{task_id}/log",
            "request_type": request.__class__.__name__,
            "response_type": "CollectLogResponse"
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

    def create_migproject_async(self, request):
        r"""新建迁移项目

        新建迁移项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMigproject
        :type request: :class:`huaweicloudsdksms.v3.CreateMigprojectRequest`
        :rtype: :class:`huaweicloudsdksms.v3.CreateMigprojectResponse`
        """
        http_info = self._create_migproject_http_info(request)
        return self._call_api(**http_info)

    def create_migproject_async_invoker(self, request):
        http_info = self._create_migproject_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_migproject_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/migprojects",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMigprojectResponse"
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

    def create_privacy_agreements_async(self, request):
        r"""同意隐私协议

        同意隐私协议接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePrivacyAgreements
        :type request: :class:`huaweicloudsdksms.v3.CreatePrivacyAgreementsRequest`
        :rtype: :class:`huaweicloudsdksms.v3.CreatePrivacyAgreementsResponse`
        """
        http_info = self._create_privacy_agreements_http_info(request)
        return self._call_api(**http_info)

    def create_privacy_agreements_async_invoker(self, request):
        http_info = self._create_privacy_agreements_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_privacy_agreements_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/privacy-agreements",
            "request_type": request.__class__.__name__,
            "response_type": "CreatePrivacyAgreementsResponse"
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

    def create_task_async(self, request):
        r"""创建迁移任务

        根据源端服务器创建一个迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTask
        :type request: :class:`huaweicloudsdksms.v3.CreateTaskRequest`
        :rtype: :class:`huaweicloudsdksms.v3.CreateTaskResponse`
        """
        http_info = self._create_task_http_info(request)
        return self._call_api(**http_info)

    def create_task_async_invoker(self, request):
        http_info = self._create_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks",
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

    def create_template_async(self, request):
        r"""新增模板信息

        新增源端模板信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdksms.v3.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdksms.v3.CreateTemplateResponse`
        """
        http_info = self._create_template_http_info(request)
        return self._call_api(**http_info)

    def create_template_async_invoker(self, request):
        http_info = self._create_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/vm/templates",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTemplateResponse"
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

    def delete_migproject_async(self, request):
        r"""删除迁移项目

        删除指定ID的迁移项目。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMigproject
        :type request: :class:`huaweicloudsdksms.v3.DeleteMigprojectRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteMigprojectResponse`
        """
        http_info = self._delete_migproject_http_info(request)
        return self._call_api(**http_info)

    def delete_migproject_async_invoker(self, request):
        http_info = self._delete_migproject_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_migproject_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/migprojects/{mig_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMigprojectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

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

    def delete_server_async(self, request):
        r"""删除指定ID的源端服务器信息

        从主机迁移服务界面上删除指定ID的源端服务器信息。一旦源端服务器信息被删除，则只能通过重启源端服务器上的迁移Agent来将源端服务器信息重新添加在主机迁移服务界面。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServer
        :type request: :class:`huaweicloudsdksms.v3.DeleteServerRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteServerResponse`
        """
        http_info = self._delete_server_http_info(request)
        return self._call_api(**http_info)

    def delete_server_async_invoker(self, request):
        http_info = self._delete_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_server_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def delete_servers_async(self, request):
        r"""批量删除源端服务器信息

        批量删除源端服务器信息。一旦源端服务器信息被删除，则只能通过重启源端服务器上的迁移Agent来将源端服务器信息重新添加在主机迁移服务界面。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteServers
        :type request: :class:`huaweicloudsdksms.v3.DeleteServersRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteServersResponse`
        """
        http_info = self._delete_servers_http_info(request)
        return self._call_api(**http_info)

    def delete_servers_async_invoker(self, request):
        http_info = self._delete_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_servers_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/sources/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteServersResponse"
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

    def delete_task_async(self, request):
        r"""删除指定ID的迁移任务

        删除指定ID的迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTask
        :type request: :class:`huaweicloudsdksms.v3.DeleteTaskRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteTaskResponse`
        """
        http_info = self._delete_task_http_info(request)
        return self._call_api(**http_info)

    def delete_task_async_invoker(self, request):
        http_info = self._delete_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/tasks/{task_id}",
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

    def delete_tasks_async(self, request):
        r"""批量删除迁移任务

        批量删除迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTasks
        :type request: :class:`huaweicloudsdksms.v3.DeleteTasksRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteTasksResponse`
        """
        http_info = self._delete_tasks_http_info(request)
        return self._call_api(**http_info)

    def delete_tasks_async_invoker(self, request):
        http_info = self._delete_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tasks_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTasksResponse"
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

    def delete_template_async(self, request):
        r"""删除指定ID的模板

        删除指定ID的模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdksms.v3.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteTemplateResponse`
        """
        http_info = self._delete_template_http_info(request)
        return self._call_api(**http_info)

    def delete_template_async_invoker(self, request):
        http_info = self._delete_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/vm/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def delete_templates_async(self, request):
        r"""批量删除指定ID的模板

        批量删除指定ID的模板。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTemplates
        :type request: :class:`huaweicloudsdksms.v3.DeleteTemplatesRequest`
        :rtype: :class:`huaweicloudsdksms.v3.DeleteTemplatesResponse`
        """
        http_info = self._delete_templates_http_info(request)
        return self._call_api(**http_info)

    def delete_templates_async_invoker(self, request):
        http_info = self._delete_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_templates_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/vm/templates/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTemplatesResponse"
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

    def export_consistency_results_async(self, request):
        r"""批量获取一致性校验结果

        使用该接口批量导出一致性校验结果
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportConsistencyResults
        :type request: :class:`huaweicloudsdksms.v3.ExportConsistencyResultsRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ExportConsistencyResultsResponse`
        """
        http_info = self._export_consistency_results_http_info(request)
        return self._call_api(**http_info)

    def export_consistency_results_async_invoker(self, request):
        http_info = self._export_consistency_results_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_consistency_results_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/consistency-results/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportConsistencyResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_error_servers_async(self, request):
        r"""查询待迁移源端的所有错误

        主机迁移过程中可能发生错误，使用该接口可以批量查询迁移过程中出现错误的源端服务器信息，以及它们的错误信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListErrorServers
        :type request: :class:`huaweicloudsdksms.v3.ListErrorServersRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ListErrorServersResponse`
        """
        http_info = self._list_error_servers_http_info(request)
        return self._call_api(**http_info)

    def list_error_servers_async_invoker(self, request):
        http_info = self._list_error_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_error_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/errors",
            "request_type": request.__class__.__name__,
            "response_type": "ListErrorServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'migproject' in local_var_params:
            query_params.append(('migproject', local_var_params['migproject']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def list_migprojects_async(self, request):
        r"""获取项目列表

        主机迁移服务中可以使用迁移项目来对源端进行项目管理，使用该接口获取当前账户下所有的迁移项目列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMigprojects
        :type request: :class:`huaweicloudsdksms.v3.ListMigprojectsRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ListMigprojectsResponse`
        """
        http_info = self._list_migprojects_http_info(request)
        return self._call_api(**http_info)

    def list_migprojects_async_invoker(self, request):
        http_info = self._list_migprojects_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_migprojects_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/migprojects",
            "request_type": request.__class__.__name__,
            "response_type": "ListMigprojectsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def list_servers_async(self, request):
        r"""查询源端服务器列表

        用户在源端安装并成功启动Agent后，Agent会将源端服务器信息注册在主机迁移服务中，调用该接口查询已注册的源端服务器列表信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListServers
        :type request: :class:`huaweicloudsdksms.v3.ListServersRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ListServersResponse`
        """
        http_info = self._list_servers_http_info(request)
        return self._call_api(**http_info)

    def list_servers_async_invoker(self, request):
        http_info = self._list_servers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_servers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/sources",
            "request_type": request.__class__.__name__,
            "response_type": "ListServersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))
        if 'migproject' in local_var_params:
            query_params.append(('migproject', local_var_params['migproject']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'migration_cycle' in local_var_params:
            query_params.append(('migration_cycle', local_var_params['migration_cycle']))
        if 'connected' in local_var_params:
            query_params.append(('connected', local_var_params['connected']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'is_consistency_result_exist' in local_var_params:
            query_params.append(('is_consistency_result_exist', local_var_params['is_consistency_result_exist']))

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

    def list_tasks_async(self, request):
        r"""查询迁移任务列表

        在设置目的端后，主机迁移服务会自动创建迁移任务，使用该接口可以查询迁移任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTasks
        :type request: :class:`huaweicloudsdksms.v3.ListTasksRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ListTasksResponse`
        """
        http_info = self._list_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_tasks_async_invoker(self, request):
        http_info = self._list_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in local_var_params:
            query_params.append(('state', local_var_params['state']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'source_server_id' in local_var_params:
            query_params.append(('source_server_id', local_var_params['source_server_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def list_templates_async(self, request):
        r"""查询模板列表

        查询弹性云服务器模板列表，迁移时选择“新建服务器”时可使用该模板创建弹性云服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdksms.v3.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ListTemplatesResponse`
        """
        http_info = self._list_templates_http_info(request)
        return self._call_api(**http_info)

    def list_templates_async_invoker(self, request):
        http_info = self._list_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/vm/templates",
            "request_type": request.__class__.__name__,
            "response_type": "ListTemplatesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'availability_zone' in local_var_params:
            query_params.append(('availability_zone', local_var_params['availability_zone']))
        if 'region' in local_var_params:
            query_params.append(('region', local_var_params['region']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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

    def register_server_async(self, request):
        r"""上报源端服务器基本信息

        上报源端服务器信息，上报成功后会在sms服务器列表中看到对应的源端服务器信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterServer
        :type request: :class:`huaweicloudsdksms.v3.RegisterServerRequest`
        :rtype: :class:`huaweicloudsdksms.v3.RegisterServerResponse`
        """
        http_info = self._register_server_http_info(request)
        return self._call_api(**http_info)

    def register_server_async_invoker(self, request):
        http_info = self._register_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_server_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/sources",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterServerResponse"
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

    def show_cert_key_async(self, request):
        r"""获取SSL证书和私钥

        当迁移采用块级迁移的方式时，安装在源端服务器上的迁移Agent通过SSLSocket同目的端服务器通信，该接口用于下载迁移传输过程所需要的证书和私钥(PEM格式)。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCertKey
        :type request: :class:`huaweicloudsdksms.v3.ShowCertKeyRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowCertKeyResponse`
        """
        http_info = self._show_cert_key_http_info(request)
        return self._call_api(**http_info)

    def show_cert_key_async_invoker(self, request):
        http_info = self._show_cert_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cert_key_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{task_id}/certkey",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCertKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'enable_ca_cert' in local_var_params:
            query_params.append(('enable_ca_cert', local_var_params['enable_ca_cert']))

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

    def show_command_async(self, request):
        r"""获取服务端命令

        迁移Agent调用该接口从SMS服务端获取下发给指定源端迁移Agent的命令。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCommand
        :type request: :class:`huaweicloudsdksms.v3.ShowCommandRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowCommandResponse`
        """
        http_info = self._show_command_http_info(request)
        return self._call_api(**http_info)

    def show_command_async_invoker(self, request):
        http_info = self._show_command_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_command_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/sources/{server_id}/command",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCommandResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def show_config_setting_async(self, request):
        r"""查询配置资源

        使用该接口查询指定任务的指定配置类型的配置信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfigSetting
        :type request: :class:`huaweicloudsdksms.v3.ShowConfigSettingRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowConfigSettingResponse`
        """
        http_info = self._show_config_setting_http_info(request)
        return self._call_api(**http_info)

    def show_config_setting_async_invoker(self, request):
        http_info = self._show_config_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_config_setting_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{task_id}/configuration-setting",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigSettingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'config_key' in local_var_params:
            query_params.append(('config_key', local_var_params['config_key']))

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

    def show_consistency_result_async(self, request):
        r"""获取一致性校验结果

        获取一致性校验结果简报
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConsistencyResult
        :type request: :class:`huaweicloudsdksms.v3.ShowConsistencyResultRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowConsistencyResultResponse`
        """
        http_info = self._show_consistency_result_http_info(request)
        return self._call_api(**http_info)

    def show_consistency_result_async_invoker(self, request):
        http_info = self._show_consistency_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_consistency_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{task_id}/consistency-result",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConsistencyResultResponse"
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

    def show_migproject_async(self, request):
        r"""查询指定ID迁移项目详情

        查询指定ID的迁移项目详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMigproject
        :type request: :class:`huaweicloudsdksms.v3.ShowMigprojectRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowMigprojectResponse`
        """
        http_info = self._show_migproject_http_info(request)
        return self._call_api(**http_info)

    def show_migproject_async_invoker(self, request):
        http_info = self._show_migproject_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_migproject_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/migprojects/{mig_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMigprojectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

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

    def show_overview_async(self, request):
        r"""获取服务器总览

        获取服务器总览
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdksms.v3.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowOverviewResponse`
        """
        http_info = self._show_overview_http_info(request)
        return self._call_api(**http_info)

    def show_overview_async_invoker(self, request):
        http_info = self._show_overview_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_overview_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/sources/overview",
            "request_type": request.__class__.__name__,
            "response_type": "ShowOverviewResponse"
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

    def show_passphrase_async(self, request):
        r"""查询指定任务ID的安全传输通道的证书passphrase

        查询指定任务ID的安全传输通道的证书passphrase。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPassphrase
        :type request: :class:`huaweicloudsdksms.v3.ShowPassphraseRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowPassphraseResponse`
        """
        http_info = self._show_passphrase_http_info(request)
        return self._call_api(**http_info)

    def show_passphrase_async_invoker(self, request):
        http_info = self._show_passphrase_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_passphrase_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{task_id}/passphrase",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPassphraseResponse"
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

    def show_privacy_agreements_async(self, request):
        r"""查询用户是否同意隐私协议

        查询用户是否同意隐私协议接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPrivacyAgreements
        :type request: :class:`huaweicloudsdksms.v3.ShowPrivacyAgreementsRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowPrivacyAgreementsResponse`
        """
        http_info = self._show_privacy_agreements_http_info(request)
        return self._call_api(**http_info)

    def show_privacy_agreements_async_invoker(self, request):
        http_info = self._show_privacy_agreements_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_privacy_agreements_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/privacy-agreements",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPrivacyAgreementsResponse"
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

    def show_server_async(self, request):
        r"""查询指定ID的源端服务器

        迁移Agent将源端服务器信息上报到主机迁移服务后，主机迁移服务会对迁移的可行性进行检测，该接口返回源端服务器的基本信息和检查结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowServer
        :type request: :class:`huaweicloudsdksms.v3.ShowServerRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowServerResponse`
        """
        http_info = self._show_server_http_info(request)
        return self._call_api(**http_info)

    def show_server_async_invoker(self, request):
        http_info = self._show_server_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_server_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowServerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def show_target_password_async(self, request):
        r"""查询指定ID的模板中的目的端服务器的密码

        查询指定ID的模板中的目的端服务器的密码。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTargetPassword
        :type request: :class:`huaweicloudsdksms.v3.ShowTargetPasswordRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowTargetPasswordResponse`
        """
        http_info = self._show_target_password_http_info(request)
        return self._call_api(**http_info)

    def show_target_password_async_invoker(self, request):
        http_info = self._show_target_password_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_target_password_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/vm/templates/{id}/target-password",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTargetPasswordResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def show_task_async(self, request):
        r"""查询指定ID的迁移任务

        查询指定ID的迁移任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTask
        :type request: :class:`huaweicloudsdksms.v3.ShowTaskRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowTaskResponse`
        """
        http_info = self._show_task_http_info(request)
        return self._call_api(**http_info)

    def show_task_async_invoker(self, request):
        http_info = self._show_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{task_id}",
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

    def show_template_async(self, request):
        r"""查询指定ID模板信息

        查询指定ID的弹性云服务器模板信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTemplate
        :type request: :class:`huaweicloudsdksms.v3.ShowTemplateRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowTemplateResponse`
        """
        http_info = self._show_template_http_info(request)
        return self._call_api(**http_info)

    def show_template_async_invoker(self, request):
        http_info = self._show_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_template_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/vm/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def shows_speed_limits_async(self, request):
        r"""查询任务限速规则

        按时间段查询迁移任务的迁移速率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowsSpeedLimits
        :type request: :class:`huaweicloudsdksms.v3.ShowsSpeedLimitsRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowsSpeedLimitsResponse`
        """
        http_info = self._shows_speed_limits_http_info(request)
        return self._call_api(**http_info)

    def shows_speed_limits_async_invoker(self, request):
        http_info = self._shows_speed_limits_http_info(request)
        return AsyncInvoker(self, http_info)

    def _shows_speed_limits_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{task_id}/speed-limit",
            "request_type": request.__class__.__name__,
            "response_type": "ShowsSpeedLimitsResponse"
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

    def update_command_result_async(self, request):
        r"""上报服务端命令执行结果

        迁移Agent调用该接口向SMS服务端反馈指定指令的执行结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCommandResult
        :type request: :class:`huaweicloudsdksms.v3.UpdateCommandResultRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateCommandResultResponse`
        """
        http_info = self._update_command_result_http_info(request)
        return self._call_api(**http_info)

    def update_command_result_async_invoker(self, request):
        http_info = self._update_command_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_command_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/sources/{server_id}/command_result",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCommandResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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

    def update_consistency_result_async(self, request):
        r"""上传一致性校验结果

        Agent 上传一致性校验结果简报
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConsistencyResult
        :type request: :class:`huaweicloudsdksms.v3.UpdateConsistencyResultRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateConsistencyResultResponse`
        """
        http_info = self._update_consistency_result_http_info(request)
        return self._call_api(**http_info)

    def update_consistency_result_async_invoker(self, request):
        http_info = self._update_consistency_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_consistency_result_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/{task_id}/consistency-result",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConsistencyResultResponse"
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

    def update_copy_state_async(self, request):
        r"""更新任务对应源端复制状态

        更新任务对应源端复制状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateCopyState
        :type request: :class:`huaweicloudsdksms.v3.UpdateCopyStateRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateCopyStateResponse`
        """
        http_info = self._update_copy_state_http_info(request)
        return self._call_api(**http_info)

    def update_copy_state_async_invoker(self, request):
        http_info = self._update_copy_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_copy_state_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/sources/{source_id}/changestate",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateCopyStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def update_default_migproject_async(self, request):
        r"""更新默认迁移项目

        更改默认迁移项目，注册源端会注册在当前的默认项目下。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDefaultMigproject
        :type request: :class:`huaweicloudsdksms.v3.UpdateDefaultMigprojectRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateDefaultMigprojectResponse`
        """
        http_info = self._update_default_migproject_http_info(request)
        return self._call_api(**http_info)

    def update_default_migproject_async_invoker(self, request):
        http_info = self._update_default_migproject_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_default_migproject_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/migprojects/{mig_project_id}/default",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDefaultMigprojectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

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

    def update_disk_info_async(self, request):
        r"""更新磁盘信息

        更新服务器的磁盘信息，此接口会把服务器原有磁盘信息清空，然后更新成新磁盘信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateDiskInfo
        :type request: :class:`huaweicloudsdksms.v3.UpdateDiskInfoRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateDiskInfoResponse`
        """
        http_info = self._update_disk_info_http_info(request)
        return self._call_api(**http_info)

    def update_disk_info_async_invoker(self, request):
        http_info = self._update_disk_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_disk_info_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/sources/{source_id}/diskinfo",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDiskInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def update_migproject_async(self, request):
        r"""更新迁移项目信息

        更新迁移项目的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMigproject
        :type request: :class:`huaweicloudsdksms.v3.UpdateMigprojectRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateMigprojectResponse`
        """
        http_info = self._update_migproject_http_info(request)
        return self._call_api(**http_info)

    def update_migproject_async_invoker(self, request):
        http_info = self._update_migproject_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_migproject_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/migprojects/{mig_project_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMigprojectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'mig_project_id' in local_var_params:
            path_params['mig_project_id'] = local_var_params['mig_project_id']

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

    def update_network_check_info_async(self, request):
        r"""更新网络检测相关的信息

        Agent 上报网络检测相关的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNetworkCheckInfo
        :type request: :class:`huaweicloudsdksms.v3.UpdateNetworkCheckInfoRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateNetworkCheckInfoResponse`
        """
        http_info = self._update_network_check_info_http_info(request)
        return self._call_api(**http_info)

    def update_network_check_info_async_invoker(self, request):
        http_info = self._update_network_check_info_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_network_check_info_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{task_id}/update-network-check-info",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNetworkCheckInfoResponse"
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

    def update_server_name_async(self, request):
        r"""修改指定ID的源端服务器信息

        该功能用来修改SMS服务端的源端信息，方便用户对源端进行管理。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateServerName
        :type request: :class:`huaweicloudsdksms.v3.UpdateServerNameRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateServerNameResponse`
        """
        http_info = self._update_server_name_http_info(request)
        return self._call_api(**http_info)

    def update_server_name_async_invoker(self, request):
        http_info = self._update_server_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_server_name_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateServerNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def update_speed_async(self, request):
        r"""设置迁移限速规则

        设置迁移任务的迁移速率。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSpeed
        :type request: :class:`huaweicloudsdksms.v3.UpdateSpeedRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateSpeedResponse`
        """
        http_info = self._update_speed_http_info(request)
        return self._call_api(**http_info)

    def update_speed_async_invoker(self, request):
        http_info = self._update_speed_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_speed_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/{task_id}/speed-limit",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSpeedResponse"
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

    def update_task_async(self, request):
        r"""更新指定ID的迁移任务

        更新指定ID的迁移任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTask
        :type request: :class:`huaweicloudsdksms.v3.UpdateTaskRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateTaskResponse`
        """
        http_info = self._update_task_http_info(request)
        return self._call_api(**http_info)

    def update_task_async_invoker(self, request):
        http_info = self._update_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_task_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/tasks/{task_id}",
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

    def update_task_speed_async(self, request):
        r"""上报数据迁移进度和速率

        此接口由安装在源端服务器上的迁移Agent在数据迁移阶段调用，用来将迁移的具体进度上报给SMS服务端。
        迁移Agent自动调用此接口用于上报数据迁移进度，您无需调用此接口。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTaskSpeed
        :type request: :class:`huaweicloudsdksms.v3.UpdateTaskSpeedRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateTaskSpeedResponse`
        """
        http_info = self._update_task_speed_http_info(request)
        return self._call_api(**http_info)

    def update_task_speed_async_invoker(self, request):
        http_info = self._update_task_speed_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_task_speed_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/tasks/{task_id}/progress",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskSpeedResponse"
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

    def update_task_status_async(self, request):
        r"""管理迁移任务

        管理迁移任务，包括启动任务，暂停任务，同步任务，日志上传，回滚失败迁移任务，删除快照资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTaskStatus
        :type request: :class:`huaweicloudsdksms.v3.UpdateTaskStatusRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateTaskStatusResponse`
        """
        http_info = self._update_task_status_http_info(request)
        return self._call_api(**http_info)

    def update_task_status_async_invoker(self, request):
        http_info = self._update_task_status_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_task_status_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/{task_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTaskStatusResponse"
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

    def update_template_async(self, request):
        r"""修改模板信息

        修改源端模板信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTemplate
        :type request: :class:`huaweicloudsdksms.v3.UpdateTemplateRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UpdateTemplateResponse`
        """
        http_info = self._update_template_http_info(request)
        return self._call_api(**http_info)

    def update_template_async_invoker(self, request):
        http_info = self._update_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/vm/templates/{id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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

    def upload_special_configuration_setting_async(self, request):
        r"""迁移任务配置设置

        配置迁移任务特殊设置，例如配置指定同步的文件或路径
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadSpecialConfigurationSetting
        :type request: :class:`huaweicloudsdksms.v3.UploadSpecialConfigurationSettingRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UploadSpecialConfigurationSettingResponse`
        """
        http_info = self._upload_special_configuration_setting_http_info(request)
        return self._call_api(**http_info)

    def upload_special_configuration_setting_async_invoker(self, request):
        http_info = self._upload_special_configuration_setting_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_special_configuration_setting_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/{task_id}/configuration-setting",
            "request_type": request.__class__.__name__,
            "response_type": "UploadSpecialConfigurationSettingResponse"
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

    def check_net_acl_async(self, request):
        r"""检查网卡安全组端口是否符合要求

        检查网卡安全组。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckNetAcl
        :type request: :class:`huaweicloudsdksms.v3.CheckNetAclRequest`
        :rtype: :class:`huaweicloudsdksms.v3.CheckNetAclResponse`
        """
        warnings.warn("Method 'check_net_acl_async' of SmsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._check_net_acl_http_info(request)
        return self._call_api(**http_info)

    def check_net_acl_async_invoker(self, request):
        warnings.warn("Method 'check_net_acl_async_invoker' of SmsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._check_net_acl_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_net_acl_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/tasks/{t_project_id}/networkacl/{t_network_id}/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckNetAclResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 't_project_id' in local_var_params:
            path_params['t_project_id'] = local_var_params['t_project_id']
        if 't_network_id' in local_var_params:
            path_params['t_network_id'] = local_var_params['t_network_id']

        query_params = []
        if 'region_id' in local_var_params:
            query_params.append(('region_id', local_var_params['region_id']))
        if 'os_type' in local_var_params:
            query_params.append(('os_type', local_var_params['os_type']))

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

    def list_api_version_async(self, request):
        r"""查询主机迁移服务的API版本信息

        查询主机迁移服务的API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersion
        :type request: :class:`huaweicloudsdksms.v3.ListApiVersionRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ListApiVersionResponse`
        """
        http_info = self._list_api_version_http_info(request)
        return self._call_api(**http_info)

    def list_api_version_async_invoker(self, request):
        http_info = self._list_api_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionResponse"
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

    def show_api_version_async(self, request):
        r"""查询主机迁移服务指定API版本信息

        查询主机迁移服务指定API版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApiVersion
        :type request: :class:`huaweicloudsdksms.v3.ShowApiVersionRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowApiVersionResponse`
        """
        http_info = self._show_api_version_http_info(request)
        return self._call_api(**http_info)

    def show_api_version_async_invoker(self, request):
        http_info = self._show_api_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_api_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/{version}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowApiVersionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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

    def show_sha256_async(self, request):
        r"""计算sha256

        计算sha256，加密字段值为uuid。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowSha256
        :type request: :class:`huaweicloudsdksms.v3.ShowSha256Request`
        :rtype: :class:`huaweicloudsdksms.v3.ShowSha256Response`
        """
        warnings.warn("Method 'show_sha256_async' of SmsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_sha256_http_info(request)
        return self._call_api(**http_info)

    def show_sha256_async_invoker(self, request):
        warnings.warn("Method 'show_sha256_async_invoker' of SmsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._show_sha256_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_sha256_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/sha256/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowSha256Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def unlock_target_ecs_async(self, request):
        r"""解锁指定任务的目的端服务器

        解锁指定任务的目的端服务器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UnlockTargetEcs
        :type request: :class:`huaweicloudsdksms.v3.UnlockTargetEcsRequest`
        :rtype: :class:`huaweicloudsdksms.v3.UnlockTargetEcsResponse`
        """
        warnings.warn("Method 'unlock_target_ecs_async' of SmsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._unlock_target_ecs_http_info(request)
        return self._call_api(**http_info)

    def unlock_target_ecs_async_invoker(self, request):
        warnings.warn("Method 'unlock_target_ecs_async_invoker' of SmsAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._unlock_target_ecs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _unlock_target_ecs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/tasks/{task_id}/unlock",
            "request_type": request.__class__.__name__,
            "response_type": "UnlockTargetEcsResponse"
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

    def show_config_async(self, request):
        r"""获取Agent配置信息

        源端Agent启动后，访问此接口获取配置信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConfig
        :type request: :class:`huaweicloudsdksms.v3.ShowConfigRequest`
        :rtype: :class:`huaweicloudsdksms.v3.ShowConfigResponse`
        """
        http_info = self._show_config_http_info(request)
        return self._call_api(**http_info)

    def show_config_async_invoker(self, request):
        http_info = self._show_config_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_config_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/config",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConfigResponse"
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

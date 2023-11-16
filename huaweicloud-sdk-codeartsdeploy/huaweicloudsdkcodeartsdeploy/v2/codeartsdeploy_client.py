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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcodeartsdeploy'")


class CodeArtsDeployClient(Client):
    def __init__(self):
        super(CodeArtsDeployClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsdeploy.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsDeployClient":
                raise TypeError("client type error, support client type is CodeArtsDeployClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def list_task_success_rate(self, request):
        """获取指定应用的应用部署成功率

        获取指定应用的应用部署成功率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskSuccessRate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListTaskSuccessRateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListTaskSuccessRateResponse`
        """
        http_info = self._list_task_success_rate_http_info(request)
        return self._call_api(**http_info)

    def list_task_success_rate_invoker(self, request):
        http_info = self._list_task_success_rate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_task_success_rate_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/tasks/metrics/success-rate",
            "request_type": request.__class__.__name__,
            "response_type": "ListTaskSuccessRateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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

    def show_project_success_rate(self, request):
        """获取指定项目的应用部署成功率

        获取指定项目的应用部署成功率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectSuccessRate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowProjectSuccessRateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowProjectSuccessRateResponse`
        """
        http_info = self._show_project_success_rate_http_info(request)
        return self._call_api(**http_info)

    def show_project_success_rate_invoker(self, request):
        http_info = self._show_project_success_rate_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_project_success_rate_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/metrics/success-rate",
            "request_type": request.__class__.__name__,
            "response_type": "ShowProjectSuccessRateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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

    def create_app(self, request):
        """新建应用

        新建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
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

    def create_deploy_task_by_template(self, request):
        """通过模板新建应用

        通过模板新建应用。该接口于2024年09月30日后不再维护，推荐使用新版CreateApp接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeployTaskByTemplate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeployTaskByTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeployTaskByTemplateResponse`
        """
        http_info = self._create_deploy_task_by_template_http_info(request)
        return self._call_api(**http_info)

    def create_deploy_task_by_template_invoker(self, request):
        http_info = self._create_deploy_task_by_template_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_deploy_task_by_template_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/tasks/template-task",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeployTaskByTemplateResponse"
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

    def delete_application(self, request):
        """删除应用

        根据应用id删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteApplicationResponse`
        """
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_invoker(self, request):
        http_info = self._delete_application_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_application_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/applications/{app_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def delete_deploy_task(self, request):
        """删除应用

        根据部署任务id删除应用。该接口于2024年09月30日后不再维护，推荐使用新版DeleteApplication接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployTask
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeployTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeployTaskResponse`
        """
        http_info = self._delete_deploy_task_http_info(request)
        return self._call_api(**http_info)

    def delete_deploy_task_invoker(self, request):
        http_info = self._delete_deploy_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_deploy_task_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeployTaskResponse"
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

    def list_all_app(self, request):
        """获取应用列表

        查询项目下应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllApp
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListAllAppRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListAllAppResponse`
        """
        http_info = self._list_all_app_http_info(request)
        return self._call_api(**http_info)

    def list_all_app_invoker(self, request):
        http_info = self._list_all_app_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_all_app_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/applications/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListAllAppResponse"
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

    def list_deploy_task_history_by_date(self, request):
        """根据开始时间和结束时间查询项目下指定应用的历史部署记录列表

        根据开始时间和结束时间查询项目下指定应用的历史部署记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeployTaskHistoryByDate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTaskHistoryByDateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTaskHistoryByDateResponse`
        """
        http_info = self._list_deploy_task_history_by_date_http_info(request)
        return self._call_api(**http_info)

    def list_deploy_task_history_by_date_invoker(self, request):
        http_info = self._list_deploy_task_history_by_date_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_deploy_task_history_by_date_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/task/{id}/history",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeployTaskHistoryByDateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))

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

    def list_deploy_tasks(self, request):
        """获取应用列表

        查询项目下应用列表。该接口于2024年09月30日后不再维护，推荐使用新版ListAllApp接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeployTasks
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTasksResponse`
        """
        http_info = self._list_deploy_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_deploy_tasks_invoker(self, request):
        http_info = self._list_deploy_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_deploy_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/tasks/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListDeployTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))

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

    def show_app_detail_by_id(self, request):
        """获取应用详情

        根据应用id获取应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppDetailById
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowAppDetailByIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowAppDetailByIdResponse`
        """
        http_info = self._show_app_detail_by_id_http_info(request)
        return self._call_api(**http_info)

    def show_app_detail_by_id_invoker(self, request):
        http_info = self._show_app_detail_by_id_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_app_detail_by_id_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications/{app_id}/info",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppDetailByIdResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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

    def show_deploy_task_detail(self, request):
        """获取应用详情

        根据部署任务id获取应用详情。该接口于2024年09月30日后不再维护，推荐使用新版ShowAppDetailById接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeployTaskDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeployTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeployTaskDetailResponse`
        """
        http_info = self._show_deploy_task_detail_http_info(request)
        return self._call_api(**http_info)

    def show_deploy_task_detail_invoker(self, request):
        http_info = self._show_deploy_task_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_deploy_task_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeployTaskDetailResponse"
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

    def show_execution_params(self, request):
        """查询部署记录的执行参数

        查询部署记录的执行参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExecutionParams
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowExecutionParamsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowExecutionParamsResponse`
        """
        http_info = self._show_execution_params_http_info(request)
        return self._call_api(**http_info)

    def show_execution_params_invoker(self, request):
        http_info = self._show_execution_params_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_execution_params_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/history/tasks/{task_id}/params",
            "request_type": request.__class__.__name__,
            "response_type": "ShowExecutionParamsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []
        if 'record_id' in local_var_params:
            query_params.append(('record_id', local_var_params['record_id']))

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

    def start_deploy_task(self, request):
        """部署应用

        根据部署任务id部署应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDeployTask
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.StartDeployTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.StartDeployTaskResponse`
        """
        http_info = self._start_deploy_task_http_info(request)
        return self._call_api(**http_info)

    def start_deploy_task_invoker(self, request):
        http_info = self._start_deploy_task_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_deploy_task_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/tasks/{task_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartDeployTaskResponse"
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

    def create_environment(self, request):
        """应用下创建环境

        应用下创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateEnvironmentResponse`
        """
        http_info = self._create_environment_http_info(request)
        return self._call_api(**http_info)

    def create_environment_invoker(self, request):
        http_info = self._create_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_environment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/applications/{application_id}/environments",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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

    def delete_environment(self, request):
        """删除应用下的环境

        删除应用下的环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteEnvironmentResponse`
        """
        http_info = self._delete_environment_http_info(request)
        return self._call_api(**http_info)

    def delete_environment_invoker(self, request):
        http_info = self._delete_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_environment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def delete_host_from_environment(self, request):
        """环境下删除主机

        环境下删除主机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHostFromEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteHostFromEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteHostFromEnvironmentResponse`
        """
        http_info = self._delete_host_from_environment_http_info(request)
        return self._call_api(**http_info)

    def delete_host_from_environment_invoker(self, request):
        http_info = self._delete_host_from_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_host_from_environment_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_id}/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteHostFromEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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

    def import_host_to_environment(self, request):
        """环境下导入主机

        环境下导入主机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportHostToEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ImportHostToEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ImportHostToEnvironmentResponse`
        """
        http_info = self._import_host_to_environment_http_info(request)
        return self._call_api(**http_info)

    def import_host_to_environment_invoker(self, request):
        http_info = self._import_host_to_environment_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_host_to_environment_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_id}/hosts/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportHostToEnvironmentResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def list_environments(self, request):
        """查询应用下环境列表

        查询应用下环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListEnvironmentsResponse`
        """
        http_info = self._list_environments_http_info(request)
        return self._call_api(**http_info)

    def list_environments_invoker(self, request):
        http_info = self._list_environments_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_environments_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications/{application_id}/environments",
            "request_type": request.__class__.__name__,
            "response_type": "ListEnvironmentsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_environment_detail(self, request):
        """查询环境详情

        查询环境详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvironmentDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowEnvironmentDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowEnvironmentDetailResponse`
        """
        http_info = self._show_environment_detail_http_info(request)
        return self._call_api(**http_info)

    def show_environment_detail_invoker(self, request):
        http_info = self._show_environment_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_environment_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/applications/{application_id}/environments/{environment_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEnvironmentDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']
        if 'environment_id' in local_var_params:
            path_params['environment_id'] = local_var_params['environment_id']

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

    def create_deployment_host(self, request):
        """新建主机

        在指定主机集群下新建主机。该接口于2024年09月30日后不再维护，推荐使用新版CreateHost接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeploymentHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentHostResponse`
        """
        http_info = self._create_deployment_host_http_info(request)
        return self._call_api(**http_info)

    def create_deployment_host_invoker(self, request):
        http_info = self._create_deployment_host_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_deployment_host_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/host-groups/{group_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeploymentHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def create_host(self, request):
        """新建主机

        在指定主机集群下新建主机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostResponse`
        """
        http_info = self._create_host_http_info(request)
        return self._call_api(**http_info)

    def create_host_invoker(self, request):
        http_info = self._create_host_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_host_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resources/host-groups/{group_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def delete_deployment_host(self, request):
        """删除主机

        根据主机id删除主机。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeploymentHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentHostResponse`
        """
        http_info = self._delete_deployment_host_http_info(request)
        return self._call_api(**http_info)

    def delete_deployment_host_invoker(self, request):
        http_info = self._delete_deployment_host_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_deployment_host_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/host-groups/{group_id}/hosts/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeploymentHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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

    def list_hosts(self, request):
        """查询主机列表

        根据主机集群id查询指定主机集群下的主机列表。该接口于2024年09月30日后不再维护，推荐使用新版ListNewHosts接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHosts
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostsResponse`
        """
        http_info = self._list_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_hosts_invoker(self, request):
        http_info = self._list_hosts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_hosts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/host-groups/{group_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'as_proxy' in local_var_params:
            query_params.append(('as_proxy', local_var_params['as_proxy']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'with_auth' in local_var_params:
            query_params.append(('with_auth', local_var_params['with_auth']))

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

    def list_new_hosts(self, request):
        """查询主机列表

        根据主机集群id查询指定主机集群下的主机列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNewHosts
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListNewHostsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListNewHostsResponse`
        """
        http_info = self._list_new_hosts_http_info(request)
        return self._call_api(**http_info)

    def list_new_hosts_invoker(self, request):
        http_info = self._list_new_hosts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_new_hosts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources/host-groups/{group_id}/hosts",
            "request_type": request.__class__.__name__,
            "response_type": "ListNewHostsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

        query_params = []
        if 'key_field' in local_var_params:
            query_params.append(('key_field', local_var_params['key_field']))
        if 'environment_id' in local_var_params:
            query_params.append(('environment_id', local_var_params['environment_id']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'as_proxy' in local_var_params:
            query_params.append(('as_proxy', local_var_params['as_proxy']))

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

    def show_deployment_host_detail(self, request):
        """查询主机详情

        根据主机id查询主机详情。该接口于2024年09月30日后不再维护，推荐使用新版ShowHostDetail接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentHostDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentHostDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentHostDetailResponse`
        """
        http_info = self._show_deployment_host_detail_http_info(request)
        return self._call_api(**http_info)

    def show_deployment_host_detail_invoker(self, request):
        http_info = self._show_deployment_host_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_deployment_host_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/host-groups/{group_id}/hosts/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeploymentHostDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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

    def show_host_detail(self, request):
        """查询主机详情

        根据主机id查询主机详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHostDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostDetailResponse`
        """
        http_info = self._show_host_detail_http_info(request)
        return self._call_api(**http_info)

    def show_host_detail_invoker(self, request):
        http_info = self._show_host_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_host_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources/host-groups/{group_id}/hosts/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHostDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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

    def update_deployment_host(self, request):
        """修改主机

        根据主机id修改主机信息。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeploymentHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentHostResponse`
        """
        http_info = self._update_deployment_host_http_info(request)
        return self._call_api(**http_info)

    def update_deployment_host_invoker(self, request):
        http_info = self._update_deployment_host_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_deployment_host_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/host-groups/{group_id}/hosts/{host_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeploymentHostResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']
        if 'host_id' in local_var_params:
            path_params['host_id'] = local_var_params['host_id']

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

    def create_deployment_group(self, request):
        """新建主机集群

        在项目下新建主机集群。该接口于2024年09月30日后不再维护，推荐使用新版CreateHostCluster接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeploymentGroup
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentGroupResponse`
        """
        http_info = self._create_deployment_group_http_info(request)
        return self._call_api(**http_info)

    def create_deployment_group_invoker(self, request):
        http_info = self._create_deployment_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_deployment_group_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/host-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateDeploymentGroupResponse"
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

    def create_host_cluster(self, request):
        """新建主机集群

        在项目下新建主机集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHostCluster
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostClusterRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostClusterResponse`
        """
        http_info = self._create_host_cluster_http_info(request)
        return self._call_api(**http_info)

    def create_host_cluster_invoker(self, request):
        http_info = self._create_host_cluster_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_host_cluster_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/resources/host-groups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateHostClusterResponse"
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

    def delete_deployment_group(self, request):
        """删除主机集群

        根据主机集群id删除主机集群。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeploymentGroup
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentGroupResponse`
        """
        http_info = self._delete_deployment_group_http_info(request)
        return self._call_api(**http_info)

    def delete_deployment_group_invoker(self, request):
        http_info = self._delete_deployment_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_deployment_group_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/host-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteDeploymentGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def list_host_clusters(self, request):
        """查询主机集群列表

        按条件查询主机集群列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostClusters
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostClustersRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostClustersResponse`
        """
        http_info = self._list_host_clusters_http_info(request)
        return self._call_api(**http_info)

    def list_host_clusters_invoker(self, request):
        http_info = self._list_host_clusters_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_host_clusters_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources/host-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostClustersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'os' in local_var_params:
            query_params.append(('os', local_var_params['os']))
        if 'page_index' in local_var_params:
            query_params.append(('page_index', local_var_params['page_index']))
        if 'page_size' in local_var_params:
            query_params.append(('page_size', local_var_params['page_size']))
        if 'sort_field' in local_var_params:
            query_params.append(('sort_field', local_var_params['sort_field']))
        if 'sort_type' in local_var_params:
            query_params.append(('sort_type', local_var_params['sort_type']))
        if 'is_proxy_mode' in local_var_params:
            query_params.append(('is_proxy_mode', local_var_params['is_proxy_mode']))
        if 'slave_cluster_id' in local_var_params:
            query_params.append(('slave_cluster_id', local_var_params['slave_cluster_id']))

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

    def list_host_groups(self, request):
        """查询主机集群列表

        按条件查询主机集群列表。该接口于2024年09月30日后不再维护，推荐使用新版ListHostClusters接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostGroups
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostGroupsResponse`
        """
        http_info = self._list_host_groups_http_info(request)
        return self._call_api(**http_info)

    def list_host_groups_invoker(self, request):
        http_info = self._list_host_groups_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_host_groups_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/host-groups",
            "request_type": request.__class__.__name__,
            "response_type": "ListHostGroupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'region_name' in local_var_params:
            query_params.append(('region_name', local_var_params['region_name']))
        if 'os' in local_var_params:
            query_params.append(('os', local_var_params['os']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

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

    def show_deployment_group_detail(self, request):
        """查询主机集群详情

        根据主机集群id查询主机集群详情。该接口于2024年09月30日后不再维护，推荐使用新版ShowHostClusterDetail接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentGroupDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentGroupDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentGroupDetailResponse`
        """
        http_info = self._show_deployment_group_detail_http_info(request)
        return self._call_api(**http_info)

    def show_deployment_group_detail_invoker(self, request):
        http_info = self._show_deployment_group_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_deployment_group_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/host-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDeploymentGroupDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def show_host_cluster_detail(self, request):
        """查询主机集群详情

        根据主机集群id查询主机集群详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHostClusterDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostClusterDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostClusterDetailResponse`
        """
        http_info = self._show_host_cluster_detail_http_info(request)
        return self._call_api(**http_info)

    def show_host_cluster_detail_invoker(self, request):
        http_info = self._show_host_cluster_detail_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_host_cluster_detail_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/resources/host-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHostClusterDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

    def update_deployment_group(self, request):
        """修改主机集群

        根据主机集群id修改主机集群信息。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeploymentGroup
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentGroupResponse`
        """
        http_info = self._update_deployment_group_http_info(request)
        return self._call_api(**http_info)

    def update_deployment_group_invoker(self, request):
        http_info = self._update_deployment_group_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_deployment_group_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/host-groups/{group_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateDeploymentGroupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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

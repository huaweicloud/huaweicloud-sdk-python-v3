# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeArtsDeployClient(Client):
    def __init__(self):
        super(CodeArtsDeployClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartsdeploy.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CodeArtsDeployClient":
            raise TypeError("client type error, support client type is CodeArtsDeployClient")

        return ClientBuilder(clazz)

    def list_task_success_rate(self, request):
        """获取指定应用的应用部署成功率

        获取指定应用的应用部署成功率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTaskSuccessRate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListTaskSuccessRateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListTaskSuccessRateResponse`
        """
        return self._list_task_success_rate_with_http_info(request)

    def _list_task_success_rate_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

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
            resource_path='/v2/{project_id}/tasks/metrics/success-rate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTaskSuccessRateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_success_rate(self, request):
        """获取指定项目的应用部署成功率

        获取指定项目的应用部署成功率。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectSuccessRate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowProjectSuccessRateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowProjectSuccessRateResponse`
        """
        return self._show_project_success_rate_with_http_info(request)

    def _show_project_success_rate_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/metrics/success-rate',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectSuccessRateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app(self, request):
        """新建应用

        新建应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateAppResponse`
        """
        return self._create_app_with_http_info(request)

    def _create_app_with_http_info(self, request):
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
            resource_path='/v1/applications',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_deploy_task_by_template(self, request):
        """通过模板新建应用

        通过模板新建应用。该接口于2024年09月30日后不再维护，推荐使用新版CreateApp接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeployTaskByTemplate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeployTaskByTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeployTaskByTemplateResponse`
        """
        return self._create_deploy_task_by_template_with_http_info(request)

    def _create_deploy_task_by_template_with_http_info(self, request):
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
            resource_path='/v2/tasks/template-task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDeployTaskByTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_application(self, request):
        """删除应用

        根据应用id删除应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteApplicationResponse`
        """
        return self._delete_application_with_http_info(request)

    def _delete_application_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v1/applications/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteApplicationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deploy_task(self, request):
        """删除应用

        根据部署任务id删除应用。该接口于2024年09月30日后不再维护，推荐使用新版DeleteApplication接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeployTask
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeployTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeployTaskResponse`
        """
        return self._delete_deploy_task_with_http_info(request)

    def _delete_deploy_task_with_http_info(self, request):
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
            resource_path='/v2/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeployTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_all_app(self, request):
        """获取应用列表

        查询项目下应用列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAllApp
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListAllAppRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListAllAppResponse`
        """
        return self._list_all_app_with_http_info(request)

    def _list_all_app_with_http_info(self, request):
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
            resource_path='/v1/applications/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAllAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_deploy_task_history_by_date(self, request):
        """根据开始时间和结束时间查询项目下指定应用的历史部署记录列表

        根据开始时间和结束时间查询项目下指定应用的历史部署记录列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeployTaskHistoryByDate
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTaskHistoryByDateRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTaskHistoryByDateResponse`
        """
        return self._list_deploy_task_history_by_date_with_http_info(request)

    def _list_deploy_task_history_by_date_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/task/{id}/history',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDeployTaskHistoryByDateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_deploy_tasks(self, request):
        """获取应用列表

        查询项目下应用列表。该接口于2024年09月30日后不再维护，推荐使用新版ListAllApp接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDeployTasks
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTasksRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListDeployTasksResponse`
        """
        return self._list_deploy_tasks_with_http_info(request)

    def _list_deploy_tasks_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/list',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDeployTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app_detail_by_id(self, request):
        """获取应用详情

        根据应用id获取应用详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAppDetailById
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowAppDetailByIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowAppDetailByIdResponse`
        """
        return self._show_app_detail_by_id_with_http_info(request)

    def _show_app_detail_by_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v1/applications/{app_id}/info',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppDetailByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_deploy_task_detail(self, request):
        """获取应用详情

        根据部署任务id获取应用详情。该接口于2024年09月30日后不再维护，推荐使用新版ShowAppDetailById接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeployTaskDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeployTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeployTaskDetailResponse`
        """
        return self._show_deploy_task_detail_with_http_info(request)

    def _show_deploy_task_detail_with_http_info(self, request):
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
            resource_path='/v2/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeployTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_execution_params(self, request):
        """查询部署记录的执行参数

        查询部署记录的执行参数
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExecutionParams
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowExecutionParamsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowExecutionParamsResponse`
        """
        return self._show_execution_params_with_http_info(request)

    def _show_execution_params_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/history/tasks/{task_id}/params',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowExecutionParamsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_deploy_task(self, request):
        """部署应用

        根据部署任务id部署应用。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartDeployTask
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.StartDeployTaskRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.StartDeployTaskResponse`
        """
        return self._start_deploy_task_with_http_info(request)

    def _start_deploy_task_with_http_info(self, request):
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
            resource_path='/v2/tasks/{task_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartDeployTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_environment(self, request):
        """应用下创建环境

        应用下创建环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateEnvironmentResponse`
        """
        return self._create_environment_with_http_info(request)

    def _create_environment_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_id' in local_var_params:
            path_params['application_id'] = local_var_params['application_id']

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
            resource_path='/v1/applications/{application_id}/environments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_environment(self, request):
        """删除应用下的环境

        删除应用下的环境。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteEnvironmentResponse`
        """
        return self._delete_environment_with_http_info(request)

    def _delete_environment_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/applications/{application_id}/environments/{environment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_host_from_environment(self, request):
        """环境下删除主机

        环境下删除主机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteHostFromEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteHostFromEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteHostFromEnvironmentResponse`
        """
        return self._delete_host_from_environment_with_http_info(request)

    def _delete_host_from_environment_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/applications/{application_id}/environments/{environment_id}/{host_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteHostFromEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_host_to_environment(self, request):
        """环境下导入主机

        环境下导入主机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportHostToEnvironment
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ImportHostToEnvironmentRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ImportHostToEnvironmentResponse`
        """
        return self._import_host_to_environment_with_http_info(request)

    def _import_host_to_environment_with_http_info(self, request):
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
            resource_path='/v1/applications/{application_id}/environments/{environment_id}/hosts/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportHostToEnvironmentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_environments(self, request):
        """查询应用下环境列表

        查询应用下环境列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEnvironments
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListEnvironmentsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListEnvironmentsResponse`
        """
        return self._list_environments_with_http_info(request)

    def _list_environments_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/applications/{application_id}/environments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnvironmentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_environment_detail(self, request):
        """查询环境详情

        查询环境详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnvironmentDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowEnvironmentDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowEnvironmentDetailResponse`
        """
        return self._show_environment_detail_with_http_info(request)

    def _show_environment_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/applications/{application_id}/environments/{environment_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnvironmentDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_deployment_host(self, request):
        """新建主机

        在指定主机集群下新建主机。该接口于2024年09月30日后不再维护，推荐使用新版CreateHost接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeploymentHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentHostResponse`
        """
        return self._create_deployment_host_with_http_info(request)

    def _create_deployment_host_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/host-groups/{group_id}/hosts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDeploymentHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_host(self, request):
        """新建主机

        在指定主机集群下新建主机。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostResponse`
        """
        return self._create_host_with_http_info(request)

    def _create_host_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v1/resources/host-groups/{group_id}/hosts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deployment_host(self, request):
        """删除主机

        根据主机id删除主机。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeploymentHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentHostResponse`
        """
        return self._delete_deployment_host_with_http_info(request)

    def _delete_deployment_host_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/host-groups/{group_id}/hosts/{host_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeploymentHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_hosts(self, request):
        """查询主机列表

        根据主机集群id查询指定主机集群下的主机列表。该接口于2024年09月30日后不再维护，推荐使用新版ListNewHosts接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHosts
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostsResponse`
        """
        return self._list_hosts_with_http_info(request)

    def _list_hosts_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/host-groups/{group_id}/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_new_hosts(self, request):
        """查询主机列表

        根据主机集群id查询指定主机集群下的主机列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNewHosts
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListNewHostsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListNewHostsResponse`
        """
        return self._list_new_hosts_with_http_info(request)

    def _list_new_hosts_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resources/host-groups/{group_id}/hosts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNewHostsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_deployment_host_detail(self, request):
        """查询主机详情

        根据主机id查询主机详情。该接口于2024年09月30日后不再维护，推荐使用新版ShowHostDetail接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentHostDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentHostDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentHostDetailResponse`
        """
        return self._show_deployment_host_detail_with_http_info(request)

    def _show_deployment_host_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/host-groups/{group_id}/hosts/{host_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeploymentHostDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_host_detail(self, request):
        """查询主机详情

        根据主机id查询主机详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHostDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostDetailResponse`
        """
        return self._show_host_detail_with_http_info(request)

    def _show_host_detail_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resources/host-groups/{group_id}/hosts/{host_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHostDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_deployment_host(self, request):
        """修改主机

        根据主机id修改主机信息。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeploymentHost
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentHostRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentHostResponse`
        """
        return self._update_deployment_host_with_http_info(request)

    def _update_deployment_host_with_http_info(self, request):
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
            resource_path='/v2/host-groups/{group_id}/hosts/{host_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDeploymentHostResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_deployment_group(self, request):
        """新建主机集群

        在项目下新建主机集群。该接口于2024年09月30日后不再维护，推荐使用新版CreateHostCluster接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDeploymentGroup
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateDeploymentGroupResponse`
        """
        return self._create_deployment_group_with_http_info(request)

    def _create_deployment_group_with_http_info(self, request):
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
            resource_path='/v2/host-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDeploymentGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_host_cluster(self, request):
        """新建主机集群

        在项目下新建主机集群。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateHostCluster
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostClusterRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.CreateHostClusterResponse`
        """
        return self._create_host_cluster_with_http_info(request)

    def _create_host_cluster_with_http_info(self, request):
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
            resource_path='/v1/resources/host-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateHostClusterResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_deployment_group(self, request):
        """删除主机集群

        根据主机集群id删除主机集群。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDeploymentGroup
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeleteDeploymentGroupResponse`
        """
        return self._delete_deployment_group_with_http_info(request)

    def _delete_deployment_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/host-groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDeploymentGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_clusters(self, request):
        """查询主机集群列表

        按条件查询主机集群列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostClusters
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostClustersRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostClustersResponse`
        """
        return self._list_host_clusters_with_http_info(request)

    def _list_host_clusters_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/resources/host-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostClustersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_host_groups(self, request):
        """查询主机集群列表

        按条件查询主机集群列表。该接口于2024年09月30日后不再维护，推荐使用新版ListHostClusters接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListHostGroups
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostGroupsRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ListHostGroupsResponse`
        """
        return self._list_host_groups_with_http_info(request)

    def _list_host_groups_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/host-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListHostGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_deployment_group_detail(self, request):
        """查询主机集群详情

        根据主机集群id查询主机集群详情。该接口于2024年09月30日后不再维护，推荐使用新版ShowHostClusterDetail接口。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDeploymentGroupDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentGroupDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowDeploymentGroupDetailResponse`
        """
        return self._show_deployment_group_detail_with_http_info(request)

    def _show_deployment_group_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/host-groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDeploymentGroupDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_host_cluster_detail(self, request):
        """查询主机集群详情

        根据主机集群id查询主机集群详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowHostClusterDetail
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostClusterDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.ShowHostClusterDetailResponse`
        """
        return self._show_host_cluster_detail_with_http_info(request)

    def _show_host_cluster_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v1/resources/host-groups/{group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowHostClusterDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_deployment_group(self, request):
        """修改主机集群

        根据主机集群id修改主机集群信息。该接口于2024年9月30日后不再维护。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDeploymentGroup
        :type request: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentGroupRequest`
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.UpdateDeploymentGroupResponse`
        """
        return self._update_deployment_group_with_http_info(request)

    def _update_deployment_group_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v2/host-groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDeploymentGroupResponse',
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

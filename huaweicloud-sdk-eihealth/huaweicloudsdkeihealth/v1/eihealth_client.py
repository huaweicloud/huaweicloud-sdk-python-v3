# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class EiHealthClient(Client):
    def __init__(self):
        super(EiHealthClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeihealth.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "EiHealthClient":
            raise TypeError("client type error, support client type is EiHealthClient")

        return ClientBuilder(clazz)

    def show_admet_properties(self, request):
        """ADMET属性预测接口

        计算小分子的物化性质，包括吸收(adsorption)、分布(distribution)、代谢(metabolism)、清除(excretion)与毒性(toxicity)。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAdmetProperties
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAdmetPropertiesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAdmetPropertiesResponse`
        """
        return self._show_admet_properties_with_http_info(request)

    def _show_admet_properties_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/admet',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAdmetPropertiesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_cpi_task(self, request):
        """新建CPI任务接口

        输入蛋白序列、小分子库，创建分子-蛋白互作预测任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCpiTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCpiTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCpiTaskResponse`
        """
        return self._create_cpi_task_with_http_info(request)

    def _create_cpi_task_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/cpi',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCpiTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_cpi_task_result(self, request):
        """查询CPI任务

        通过CPI任务ID查询CPI任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCpiTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowCpiTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowCpiTaskResultResponse`
        """
        return self._show_cpi_task_result_with_http_info(request)

    def _show_cpi_task_result_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/cpi/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCpiTaskResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_custom_props_task(self, request):
        """新建自定义属性任务接口

        输入自定义属性的任务数据，创建自定义属性建模任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCustomPropsTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCustomPropsTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCustomPropsTaskResponse`
        """
        return self._create_custom_props_task_with_http_info(request)

    def _create_custom_props_task_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/custom-props',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCustomPropsTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_custom_props_task_result(self, request):
        """查询自定义属性任务

        通过自定义属性任务ID查询任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowCustomPropsTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowCustomPropsTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowCustomPropsTaskResultResponse`
        """
        return self._show_custom_props_task_result_with_http_info(request)

    def _show_custom_props_task_result_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/custom-props/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowCustomPropsTaskResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_generation_task(self, request):
        """新建分子生成任务接口

        输入分子属性约束，创建分子生成任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateGenerationTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateGenerationTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateGenerationTaskResponse`
        """
        return self._create_generation_task_with_http_info(request)

    def _create_generation_task_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/generation',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateGenerationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_generation_task_result(self, request):
        """查询分子生成任务

        通过分子生成任务ID查询分子生成任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowGenerationTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowGenerationTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowGenerationTaskResultResponse`
        """
        return self._show_generation_task_result_with_http_info(request)

    def _show_generation_task_result_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/generation/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowGenerationTaskResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_import_app(self, request):
        """导入应用

        批量导入应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchImportApp
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchImportAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchImportAppResponse`
        """
        return self._batch_import_app_with_http_info(request)

    def _batch_import_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/batch-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchImportAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_app(self, request):
        """创建应用

        创建应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAppResponse`
        """
        return self._create_app_with_http_info(request)

    def _create_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps',
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

    def delete_app(self, request):
        """删除应用

        删除应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAppResponse`
        """
        return self._delete_app_with_http_info(request)

    def _delete_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_app(self, request):
        """获取应用列表

        获取应用列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAppResponse`
        """
        return self._list_app_with_http_info(request)

    def _list_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_app(self, request):
        """发布应用

        发布应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishApp
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishAppResponse`
        """
        return self._publish_app_with_http_info(request)

    def _publish_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_app(self, request):
        """获取应用详情

        获取应用详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAppResponse`
        """
        return self._show_app_with_http_info(request)

    def _show_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_app(self, request):
        """订阅应用

        订阅应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeApp
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeAppResponse`
        """
        return self._subscribe_app_with_http_info(request)

    def _subscribe_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SubscribeAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_app(self, request):
        """更新应用

        更新应用
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateApp
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAppRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAppResponse`
        """
        return self._update_app_with_http_info(request)

    def _update_app_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_id' in local_var_params:
            path_params['app_id'] = local_var_params['app_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/apps/{app_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAppResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_asset_version(self, request):
        """删除资产指定版本

        删除资产指定版本
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAssetVersionResponse`
        """
        return self._delete_asset_version_with_http_info(request)

    def _delete_asset_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/versions/{version}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAssetVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_asset_action(self, request):
        """操作资产发布状态

        操作资产发布状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteAssetAction
        :type request: :class:`huaweicloudsdkeihealth.v1.ExecuteAssetActionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExecuteAssetActionResponse`
        """
        return self._execute_asset_action_with_http_info(request)

    def _execute_asset_action_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/versions/{version}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteAssetActionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_asset(self, request):
        """获取资产列表

        获取资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAssetResponse`
        """
        return self._list_asset_with_http_info(request)

    def _list_asset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'categories' in local_var_params:
            query_params.append(('categories', local_var_params['categories']))
        if 'key_word' in local_var_params:
            query_params.append(('key_word', local_var_params['key_word']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'publishers' in local_var_params:
            query_params.append(('publishers', local_var_params['publishers']))
        if 'scope' in local_var_params:
            query_params.append(('scope', local_var_params['scope']))
        if 'vendor_ids' in local_var_params:
            query_params.append(('vendor_ids', local_var_params['vendor_ids']))

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
            resource_path='/v1/{project_id}/assets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_property(self, request):
        """获取属性值列表

        获取属性值列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProperty
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPropertyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPropertyResponse`
        """
        return self._list_property_with_http_info(request)

    def _list_property_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_property' in local_var_params:
            query_params.append(('property', local_var_params['_property']))

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
            resource_path='/v1/{project_id}/assets/properties',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPropertyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_asset(self, request):
        """查询资产详情

        查询资产详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAsset
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetResponse`
        """
        return self._show_asset_with_http_info(request)

    def _show_asset_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_asset_version(self, request):
        """查询资产版本详情

        查询资产版本详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAssetVersionResponse`
        """
        return self._show_asset_version_with_http_info(request)

    def _show_asset_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/versions/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAssetVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_asset_version(self, request):
        """更新资产指定版本的信息

        更新资产指定版本的信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAssetVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAssetVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAssetVersionResponse`
        """
        return self._update_asset_version_with_http_info(request)

    def _update_asset_version_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/versions/{version}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAssetVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_auto_job(self, request):
        """创建自动作业模板

        创建自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateAutoJobResponse`
        """
        return self._create_auto_job_with_http_info(request)

    def _create_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_auto_job(self, request):
        """删除自动作业模板

        删除自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteAutoJobResponse`
        """
        return self._delete_auto_job_with_http_info(request)

    def _delete_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_auto_job(self, request):
        """获取自动作业模板列表

        获取自动作业模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListAutoJobResponse`
        """
        return self._list_auto_job_with_http_info(request)

    def _list_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_auto_job(self, request):
        """查询自动作业模板

        查询自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowAutoJobResponse`
        """
        return self._show_auto_job_with_http_info(request)

    def _show_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_auto_job(self, request):
        """启动自动作业

        启动自动作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StartAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartAutoJobResponse`
        """
        return self._start_auto_job_with_http_info(request)

    def _start_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_auto_job(self, request):
        """停止自动作业

        停止自动作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StopAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopAutoJobResponse`
        """
        return self._stop_auto_job_with_http_info(request)

    def _stop_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_auto_job(self, request):
        """更新自动作业模板

        更新自动作业模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateAutoJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateAutoJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateAutoJobResponse`
        """
        return self._update_auto_job_with_http_info(request)

    def _update_auto_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'auto_job_id' in local_var_params:
            path_params['auto_job_id'] = local_var_params['auto_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/auto-jobs/{auto_job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateAutoJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_scale_out_policy(self, request):
        """创建扩容策略

        创建扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateScaleOutPolicyResponse`
        """
        return self._create_scale_out_policy_with_http_info(request)

    def _create_scale_out_policy_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_scale_out_policy(self, request):
        """删除扩容策略

        删除扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteScaleOutPolicyResponse`
        """
        return self._delete_scale_out_policy_with_http_info(request)

    def _delete_scale_out_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_scale_out_policy(self, request):
        """查询扩容策略列表

        查询扩容策略列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ListScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListScaleOutPolicyResponse`
        """
        return self._list_scale_out_policy_with_http_info(request)

    def _list_scale_out_policy_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_scale_in_policy(self, request):
        """查询缩容策略

        查询缩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScaleInPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScaleInPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScaleInPolicyResponse`
        """
        return self._show_scale_in_policy_with_http_info(request)

    def _show_scale_in_policy_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/autoscaler/scale-in-policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowScaleInPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_scale_out_policy(self, request):
        """获取扩容策略详情

        获取扩容策略详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScaleOutPolicyResponse`
        """
        return self._show_scale_out_policy_with_http_info(request)

    def _show_scale_out_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_scale_out_policy(self, request):
        """启动自动扩容策略

        启动自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.StartScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartScaleOutPolicyResponse`
        """
        return self._start_scale_out_policy_with_http_info(request)

    def _start_scale_out_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_scale_out_policy(self, request):
        """停用自动扩容策略

        停用自动扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.StopScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopScaleOutPolicyResponse`
        """
        return self._stop_scale_out_policy_with_http_info(request)

    def _stop_scale_out_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies/{id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_scale_in_policy(self, request):
        """修改缩容策略

        修改缩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScaleInPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScaleInPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScaleInPolicyResponse`
        """
        return self._update_scale_in_policy_with_http_info(request)

    def _update_scale_in_policy_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/autoscaler/scale-in-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateScaleInPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_scale_out_policy(self, request):
        """修改扩容策略

        修改扩容策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScaleOutPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScaleOutPolicyResponse`
        """
        return self._update_scale_out_policy_with_http_info(request)

    def _update_scale_out_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/autoscaler/scale-out-policies/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateScaleOutPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_computing_resource(self, request):
        """购买计算资源

        购买计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateComputingResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateComputingResourceResponse`
        """
        return self._create_computing_resource_with_http_info(request)

    def _create_computing_resource_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/computing-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateComputingResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_computing_resource(self, request):
        """删除计算资源

        删除计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteComputingResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteComputingResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteComputingResourceResponse`
        """
        return self._delete_computing_resource_with_http_info(request)

    def _delete_computing_resource_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteComputingResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_computing_resource_flavors(self, request):
        """查询计算资源规格

        查询计算资源规格
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComputingResourceFlavors
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingResourceFlavorsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingResourceFlavorsResponse`
        """
        return self._list_computing_resource_flavors_with_http_info(request)

    def _list_computing_resource_flavors_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'availability_zone_id' in local_var_params:
            query_params.append(('availability_zone_id', local_var_params['availability_zone_id']))

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
            resource_path='/v1/{project_id}/system/computing-resources/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListComputingResourceFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_computing_resources(self, request):
        """查询计算资源

        查询计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListComputingResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListComputingResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListComputingResourcesResponse`
        """
        return self._list_computing_resources_with_http_info(request)

    def _list_computing_resources_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/computing-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListComputingResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def reboot_node(self, request):
        """重启计算资源

        重启计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RebootNode
        :type request: :class:`huaweicloudsdkeihealth.v1.RebootNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RebootNodeResponse`
        """
        return self._reboot_node_with_http_info(request)

    def _reboot_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/reboot',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RebootNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bms_devices(self, request):
        """查询bms计算资源显卡id列表

        查询bms计算资源显卡id列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBmsDevices
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBmsDevicesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBmsDevicesResponse`
        """
        return self._show_bms_devices_with_http_info(request)

    def _show_bms_devices_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/devices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBmsDevicesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_evs_quota(self, request):
        """获取EVS配额及使用情况

        获取EVS配额及使用情况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEvsQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEvsQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEvsQuotaResponse`
        """
        return self._show_evs_quota_with_http_info(request)

    def _show_evs_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/computing-resources/evs-quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEvsQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_left_quota(self, request):
        """获取节点剩余配额

        获取节点剩余配额
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowLeftQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowLeftQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowLeftQuotaResponse`
        """
        return self._show_left_quota_with_http_info(request)

    def _show_left_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/computing-resources/quota',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowLeftQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_schedule(self, request):
        """查询计算资源调度信息

        查询计算资源调度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSchedule
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowScheduleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowScheduleResponse`
        """
        return self._show_schedule_with_http_info(request)

    def _show_schedule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/schedule',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowScheduleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_node(self, request):
        """启动计算资源

        启动计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartNode
        :type request: :class:`huaweicloudsdkeihealth.v1.StartNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StartNodeResponse`
        """
        return self._start_node_with_http_info(request)

    def _start_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_node(self, request):
        """关闭计算资源

        关闭计算资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopNode
        :type request: :class:`huaweicloudsdkeihealth.v1.StopNodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopNodeResponse`
        """
        return self._stop_node_with_http_info(request)

    def _stop_node_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

        query_params = []
        if 'force' in local_var_params:
            query_params.append(('force', local_var_params['force']))

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopNodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_schedule(self, request):
        """修改计算资源调度信息

        修改计算资源调度信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateSchedule
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateScheduleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateScheduleResponse`
        """
        return self._update_schedule_with_http_info(request)

    def _update_schedule_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/computing-resources/{id}/schedule',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateScheduleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_backup(self, request):
        """归档数据

        将需要归档的重要数据拷贝到数据归档桶
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateBackupResponse`
        """
        return self._create_backup_with_http_info(request)

    def _create_backup_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_backup(self, request):
        """删除归档

        删除指定的归档
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteBackupResponse`
        """
        return self._delete_backup_with_http_info(request)

    def _delete_backup_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_backup(self, request):
        """查询归档列表

        分页查询用户管理的项目的所有历史归档记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBackupResponse`
        """
        return self._list_backup_with_http_info(request)

    def _list_backup_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_backup(self, request):
        """恢复归档

        将指定的归档数据拷贝到目标项目的某个目录下
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreBackup
        :type request: :class:`huaweicloudsdkeihealth.v1.RestoreBackupRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RestoreBackupResponse`
        """
        return self._restore_backup_with_http_info(request)

    def _restore_backup_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}/restore',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreBackupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_backup_path(self, request):
        """获取指定归档的全数据清单

        根据归档ID获取该归档的全数据清单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBackupPath
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBackupPathRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBackupPathResponse`
        """
        return self._show_backup_path_with_http_info(request)

    def _show_backup_path_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/backups/{backup_id}/paths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBackupPathResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_data(self, request):
        """批量删除项目数据

        批量删除项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteData
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteDataResponse`
        """
        return self._batch_delete_data_with_http_info(request)

    def _batch_delete_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def copy_data(self, request):
        """复制项目数据

        复制项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CopyData
        :type request: :class:`huaweicloudsdkeihealth.v1.CopyDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CopyDataResponse`
        """
        return self._copy_data_with_http_info(request)

    def _copy_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/clone',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CopyDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_data(self, request):
        """创建文件夹

        创建文件夹
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDataResponse`
        """
        return self._create_data_with_http_info(request)

    def _create_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_data(self, request):
        """导入项目数据

        导入项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDataResponse`
        """
        return self._import_data_with_http_info(request)

    def _import_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_network_data(self, request):
        """导入网上数据

        导入网上数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportNetworkData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportNetworkDataResponse`
        """
        return self._import_network_data_with_http_info(request)

    def _import_network_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/import-from-network',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportNetworkDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_bucket(self, request):
        """获取桶列表

        获取桶列表(包含当前项目桶和引用项目桶)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListBucketResponse`
        """
        return self._list_bucket_with_http_info(request)

    def _list_bucket_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data(self, request):
        """查询数据列表

        查询指定目录下的数据列表，如果不指定默认查询根目录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataResponse`
        """
        return self._list_data_with_http_info(request)

    def _list_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_data(self, request):
        """发布数据资产

        发布数据资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishData
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishDataResponse`
        """
        return self._publish_data_with_http_info(request)

    def _publish_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def quote_data(self, request):
        """引用项目数据

        引用项目数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for QuoteData
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteDataResponse`
        """
        return self._quote_data_with_http_info(request)

    def _quote_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/quote',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='QuoteDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_bucket_storage(self, request):
        """获取桶存量信息

        获取桶存量信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowBucketStorage
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowBucketStorageResponse`
        """
        return self._show_bucket_storage_with_http_info(request)

    def _show_bucket_storage_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/bucket-storage',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowBucketStorageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data(self, request):
        """获取数据详情

        获取指定数据对象的详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataResponse`
        """
        return self._show_data_with_http_info(request)

    def _show_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

        query_params = []

        header_params = {}
        if 'x_need_content' in local_var_params:
            header_params['X-Need-Content'] = local_var_params['x_need_content']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/{path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_policy(self, request):
        """查询项目级数据权限控制策略

        查询项目级数据权限控制策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataPolicyResponse`
        """
        return self._show_data_policy_with_http_info(request)

    def _show_data_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/policy',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_data(self, request):
        """订阅资产市场数据

        订阅资产市场数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeData
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeDataResponse`
        """
        return self._subscribe_data_with_http_info(request)

    def _subscribe_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SubscribeDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_path_policy(self, request):
        """设置数据对象策略

        设置数据对象策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataPathPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDataPathPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDataPathPolicyResponse`
        """
        return self._update_data_path_policy_with_http_info(request)

    def _update_data_path_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/{path}/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataPathPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_data_policy(self, request):
        """设置项目级权限控制策略

        设置项目级权限控制策略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDataPolicy
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDataPolicyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDataPolicyResponse`
        """
        return self._update_data_policy_with_http_info(request)

    def _update_data_policy_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDataPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_data(self, request):
        """上传数据文件

        上传数据文件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadData
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadDataResponse`
        """
        return self._upload_data_with_http_info(request)

    def _upload_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'target_folder' in local_var_params:
            query_params.append(('target_folder', local_var_params['target_folder']))
        if 'part_number' in local_var_params:
            query_params.append(('part_number', local_var_params['part_number']))
        if 'total_part' in local_var_params:
            query_params.append(('total_part', local_var_params['total_part']))
        if 'multipart_id' in local_var_params:
            query_params.append(('multipart_id', local_var_params['multipart_id']))
        if 'file_name' in local_var_params:
            query_params.append(('file_name', local_var_params['file_name']))
        if 'md5' in local_var_params:
            query_params.append(('md5', local_var_params['md5']))

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/datas/upload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_data_job(self, request):
        """取消数据作业

        取消数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDataJobResponse`
        """
        return self._cancel_data_job_with_http_info(request)

    def _cancel_data_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_data_job(self, request):
        """删除数据作业

        删除数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDataJobResponse`
        """
        return self._delete_data_job_with_http_info(request)

    def _delete_data_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_data_job_log(self, request):
        """下载数据作业执行日志

        下载数据作业执行日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadDataJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataJobLogResponse`
        """
        return self._download_data_job_log_with_http_info(request)

    def _download_data_job_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadDataJobLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_checkpoint(self, request):
        """获取数据作业执行日志

        获取数据作业执行日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCheckpoint
        :type request: :class:`huaweicloudsdkeihealth.v1.ListCheckpointRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListCheckpointResponse`
        """
        return self._list_checkpoint_with_http_info(request)

    def _list_checkpoint_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/checkpoints',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListCheckpointResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_data_job(self, request):
        """获取数据作业列表

        获取数据作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDataJobResponse`
        """
        return self._list_data_job_with_http_info(request)

    def _list_data_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'creator' in local_var_params:
            query_params.append(('creator', local_var_params['creator']))
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'finish_from_time' in local_var_params:
            query_params.append(('finish_from_time', local_var_params['finish_from_time']))
        if 'finish_to_time' in local_var_params:
            query_params.append(('finish_to_time', local_var_params['finish_to_time']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_data_job(self, request):
        """重试数据作业

        重试数据作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryDataJobResponse`
        """
        return self._retry_data_job_with_http_info(request)

    def _retry_data_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_data_job(self, request):
        """获取数据作业详细信息

        获取数据作业详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDataJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDataJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDataJobResponse`
        """
        return self._show_data_job_with_http_info(request)

    def _show_data_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'data_job_id' in local_var_params:
            path_params['data_job_id'] = local_var_params['data_job_id']
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-jobs/{data_job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDataJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database_data(self, request):
        """插入单条数据

        插入单条数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseDataResponse`
        """
        return self._create_database_data_with_http_info(request)

    def _create_database_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/insert',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_instance(self, request):
        """创建数据库实例

        创建数据库实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateInstanceResponse`
        """
        return self._create_instance_with_http_info(request)

    def _create_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database_data(self, request):
        """删除数据

        删除指定行数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseDataResponse`
        """
        return self._delete_database_data_with_http_info(request)

    def _delete_database_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']
        if 'row_num' in local_var_params:
            path_params['row_num'] = local_var_params['row_num']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/{row_num}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_instance(self, request):
        """删除实例

        删除实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteInstanceResponse`
        """
        return self._delete_instance_with_http_info(request)

    def _delete_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_database_data(self, request):
        """导入数据

        导入数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportDatabaseDataResponse`
        """
        return self._import_database_data_with_http_info(request)

    def _import_database_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_data(self, request):
        """查询数据

        查询数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseDataResponse`
        """
        return self._list_database_data_with_http_info(request)

    def _list_database_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'query' in local_var_params:
            query_params.append(('query', local_var_params['query']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_instance(self, request):
        """获取实例列表

        获取实例列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.ListInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListInstanceResponse`
        """
        return self._list_instance_with_http_info(request)

    def _list_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def quote_instance(self, request):
        """引用数据库实例

        引用数据库实例
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for QuoteInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.QuoteInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.QuoteInstanceResponse`
        """
        return self._quote_instance_with_http_info(request)

    def _quote_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/batch-quote',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='QuoteInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance(self, request):
        """查询实例详情

        查询实例详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstance
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowInstanceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowInstanceResponse`
        """
        return self._show_instance_with_http_info(request)

    def _show_instance_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_database_data(self, request):
        """更新数据

        更新数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateDatabaseData
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateDatabaseDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateDatabaseDataResponse`
        """
        return self._update_database_data_with_http_info(request)

    def _update_database_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'database_id' in local_var_params:
            path_params['database_id'] = local_var_params['database_id']
        if 'row_num' in local_var_params:
            path_params['row_num'] = local_var_params['row_num']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/databases/{database_id}/data/{row_num}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateDatabaseDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_database_resource(self, request):
        """购买数据库资源

        购买数据库资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDatabaseResourceResponse`
        """
        return self._create_database_resource_with_http_info(request)

    def _create_database_resource_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/database-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDatabaseResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_database_resource(self, request):
        """删除数据库资源

        删除数据库资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDatabaseResourceResponse`
        """
        return self._delete_database_resource_with_http_info(request)

    def _delete_database_resource_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/database-resources/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDatabaseResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_resource(self, request):
        """查询数据库资源

        查询数据库资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseResource
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceResponse`
        """
        return self._list_database_resource_with_http_info(request)

    def _list_database_resource_with_http_info(self, request):
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

        response_headers = ["X-Resource-Mappings", ]

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system/database-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabaseResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_database_resource_flavor(self, request):
        """获取数据库资源规格列表

        获取数据库资源规格列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDatabaseResourceFlavor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceFlavorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDatabaseResourceFlavorResponse`
        """
        return self._list_database_resource_flavor_with_http_info(request)

    def _list_database_resource_flavor_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/database-resources/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDatabaseResourceFlavorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_docking_job(self, request):
        """创建分子对接作业

        创建分子对接作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDockingJobResponse`
        """
        return self._create_docking_job_with_http_info(request)

    def _create_docking_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/docking',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDockingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_docking_job(self, request):
        """查询分子对接作业详情

        查询分子对接作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDockingJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockingJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockingJobResponse`
        """
        return self._show_docking_job_with_http_info(request)

    def _show_docking_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/docking/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDockingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_drug_ligand_difference(self, request):
        """计算配体间的3D结构差异

        计算配体间的3D结构差异
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckDrugLigandDifference
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckDrugLigandDifferenceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckDrugLigandDifferenceResponse`
        """
        return self._check_drug_ligand_difference_with_http_info(request)

    def _check_drug_ligand_difference_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/diff3d',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckDrugLigandDifferenceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_drug_ligand_interaction2d_svg(self, request):
        """生成相互作用2D图

        生成相互作用2D图，若不提供配体文件，则受体文件中必须包含配体；若提供配体文件，则受体中的配体（若有）则会被忽略
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandInteraction2dSvg
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandInteraction2dSvgRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandInteraction2dSvgResponse`
        """
        return self._create_drug_ligand_interaction2d_svg_with_http_info(request)

    def _create_drug_ligand_interaction2d_svg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/interaction2d',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDrugLigandInteraction2dSvgResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_drug_ligand_preview_task(self, request):
        """创建配体文件预览任务

        创建配体文件预览任务，支持SMI、SDF、PDB、MOL2
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandPreviewTaskResponse`
        """
        return self._create_drug_ligand_preview_task_with_http_info(request)

    def _create_drug_ligand_preview_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/preview',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDrugLigandPreviewTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_drug_ligand_sdf(self, request):
        """生成分子SDF三维结构

        生成分子SDF三维结构
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandSdf
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSdfRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSdfResponse`
        """
        return self._create_drug_ligand_sdf_with_http_info(request)

    def _create_drug_ligand_sdf_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/sdf',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDrugLigandSdfResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_drug_ligand_similarity_graph_task(self, request):
        """创建配体相似性图计算任务

        创建配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSimilarityGraphTaskResponse`
        """
        return self._create_drug_ligand_similarity_graph_task_with_http_info(request)

    def _create_drug_ligand_similarity_graph_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/similarity-graph',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDrugLigandSimilarityGraphTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_drug_ligand_svg(self, request):
        """生成分子SVG图

        生成分子SVG图
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateDrugLigandSvg
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSvgRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateDrugLigandSvgResponse`
        """
        return self._create_drug_ligand_svg_with_http_info(request)

    def _create_drug_ligand_svg_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/svg',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateDrugLigandSvgResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_drug_ligand_preview_task(self, request):
        """删除配体文件预览任务

        删除配体文件预览任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandPreviewTaskResponse`
        """
        return self._delete_drug_ligand_preview_task_with_http_info(request)

    def _delete_drug_ligand_preview_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/preview/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDrugLigandPreviewTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_drug_ligand_similarity_graph_task(self, request):
        """删除配体相似性图计算任务

        删除配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugLigandSimilarityGraphTaskResponse`
        """
        return self._delete_drug_ligand_similarity_graph_task_with_http_info(request)

    def _delete_drug_ligand_similarity_graph_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/similarity-graph/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDrugLigandSimilarityGraphTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def parse_drug_receptor_info(self, request):
        """受体信息解析

        受体信息解析，如果有多个受体蛋白则只处理第一个，如果一个受体蛋白里结合了多个配体，则最多只处理前10个
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ParseDrugReceptorInfo
        :type request: :class:`huaweicloudsdkeihealth.v1.ParseDrugReceptorInfoRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ParseDrugReceptorInfoResponse`
        """
        return self._parse_drug_receptor_info_with_http_info(request)

    def _parse_drug_receptor_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/info',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ParseDrugReceptorInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def recognize_drug_receptor_pocket(self, request):
        """受体口袋检测

        检测受体口袋，检测类型基于配体，基于氨基酸残基，自动检测，自定义和全局对接
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RecognizeDrugReceptorPocket
        :type request: :class:`huaweicloudsdkeihealth.v1.RecognizeDrugReceptorPocketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RecognizeDrugReceptorPocketResponse`
        """
        return self._recognize_drug_receptor_pocket_with_http_info(request)

    def _recognize_drug_receptor_pocket_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/pocket',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RecognizeDrugReceptorPocketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_drug_ligand_to_smiles_conversion(self, request):
        """配体格式转换为SMILES

        配体格式转换为SMILES，若配体文件中存在多个分子，则只取第一个返回
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDrugLigandToSmilesConversion
        :type request: :class:`huaweicloudsdkeihealth.v1.RunDrugLigandToSmilesConversionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunDrugLigandToSmilesConversionResponse`
        """
        return self._run_drug_ligand_to_smiles_conversion_with_http_info(request)

    def _run_drug_ligand_to_smiles_conversion_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/smiles',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunDrugLigandToSmilesConversionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_drug_receptor_preprocess(self, request):
        """受体预处理

        受体预处理，用于前端显示预处理后的受体
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunDrugReceptorPreprocess
        :type request: :class:`huaweicloudsdkeihealth.v1.RunDrugReceptorPreprocessRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RunDrugReceptorPreprocessResponse`
        """
        return self._run_drug_receptor_preprocess_with_http_info(request)

    def _run_drug_receptor_preprocess_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/receptor/preprocess',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunDrugReceptorPreprocessResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_drug_ligand_preview_task(self, request):
        """查询配体文件预览任务

        查询配体文件预览任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDrugLigandPreviewTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandPreviewTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandPreviewTaskResponse`
        """
        return self._show_drug_ligand_preview_task_with_http_info(request)

    def _show_drug_ligand_preview_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/preview/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDrugLigandPreviewTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_drug_ligand_similarity_graph_task(self, request):
        """查询配体相似性图计算任务

        查询配体相似性图计算任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDrugLigandSimilarityGraphTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandSimilarityGraphTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDrugLigandSimilarityGraphTaskResponse`
        """
        return self._show_drug_ligand_similarity_graph_task_with_http_info(request)

    def _show_drug_ligand_similarity_graph_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-common/ligand/similarity-graph/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDrugLigandSimilarityGraphTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_drug_job(self, request):
        """取消药物作业

        取消药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelDrugJobResponse`
        """
        return self._cancel_drug_job_with_http_info(request)

    def _cancel_drug_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/{job_id}/cancel',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelDrugJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_drug_job(self, request):
        """删除药物作业

        删除药物作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteDrugJobResponse`
        """
        return self._delete_drug_job_with_http_info(request)

    def _delete_drug_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteDrugJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_drug_job(self, request):
        """获取药物作业列表

        获取药物作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListDrugJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListDrugJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListDrugJobResponse`
        """
        return self._list_drug_job_with_http_info(request)

    def _list_drug_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'status_list' in local_var_params:
            query_params.append(('status_list', local_var_params['status_list']))
            collection_formats['status_list'] = 'csv'
        if 'type_list' in local_var_params:
            query_params.append(('type_list', local_var_params['type_list']))
            collection_formats['type_list'] = 'csv'
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))
        if 'total_time_range' in local_var_params:
            query_params.append(('total_time_range', local_var_params['total_time_range']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListDrugJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_fep_job(self, request):
        """创建自由能微扰作业

        创建自由能微扰作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateFepJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateFepJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateFepJobResponse`
        """
        return self._create_fep_job_with_http_info(request)

    def _create_fep_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/fep',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateFepJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_fep_job(self, request):
        """查询自由能微扰作业详情

        查询自由能微扰作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFepJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowFepJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowFepJobResponse`
        """
        return self._show_fep_job_with_http_info(request)

    def _show_fep_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/fep/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFepJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_iam_group_users(self, request):
        """查询IAM用户组的用户列表

        查询IAM用户组的用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIamGroupUsers
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamGroupUsersRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamGroupUsersResponse`
        """
        return self._list_iam_group_users_with_http_info(request)

    def _list_iam_group_users_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/iam/groups/{group_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIamGroupUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_iam_groups(self, request):
        """查询IAM用户组列表

        查询IAM用户组列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIamGroups
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamGroupsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamGroupsResponse`
        """
        return self._list_iam_groups_with_http_info(request)

    def _list_iam_groups_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/iam/groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIamGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_iam_users(self, request):
        """查询IAM用户列表

        查询IAM用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListIamUsers
        :type request: :class:`huaweicloudsdkeihealth.v1.ListIamUsersRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListIamUsersResponse`
        """
        return self._list_iam_users_with_http_info(request)

    def _list_iam_users_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/iam/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListIamUsersResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_tag(self, request):
        """批量删除镜像tag

        批量删除镜像tag
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteTagResponse`
        """
        return self._batch_delete_tag_with_http_info(request)

    def _batch_delete_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_image(self, request):
        """创建镜像

        创建镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateImageResponse`
        """
        return self._create_image_with_http_info(request)

    def _create_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_image(self, request):
        """删除镜像仓库

        删除镜像仓库
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteImage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteImageResponse`
        """
        return self._delete_image_with_http_info(request)

    def _delete_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_tag(self, request):
        """删除指定镜像tag

        删除指定镜像tag
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTagResponse`
        """
        return self._delete_tag_with_http_info(request)

    def _delete_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']
        if 'tag' in local_var_params:
            path_params['tag'] = local_var_params['tag']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags/{tag}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_image(self, request):
        """导入镜像

        导入镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportImageResponse`
        """
        return self._import_image_with_http_info(request)

    def _import_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image(self, request):
        """获取镜像列表

        获取镜像列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageResponse`
        """
        return self._list_image_with_http_info(request)

    def _list_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'show_empty' in local_var_params:
            query_params.append(('show_empty', local_var_params['show_empty']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_image_tag(self, request):
        """获取指定镜像的tag列表

        获取指定镜像的tag列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListImageTag
        :type request: :class:`huaweicloudsdkeihealth.v1.ListImageTagRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListImageTagResponse`
        """
        return self._list_image_tag_with_http_info(request)

    def _list_image_tag_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}/tags',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListImageTagResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_image(self, request):
        """发布镜像

        发布镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishImage
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishImageResponse`
        """
        return self._publish_image_with_http_info(request)

    def _publish_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_docker_login(self, request):
        """获取docker login指令

        获取docker login指令
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDockerLogin
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowDockerLoginResponse`
        """
        return self._show_docker_login_with_http_info(request)

    def _show_docker_login_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/docker-login-cmd',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDockerLoginResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_image(self, request):
        """订阅镜像

        订阅镜像
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeImage
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeImageResponse`
        """
        return self._subscribe_image_with_http_info(request)

    def _subscribe_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SubscribeImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_image(self, request):
        """更新镜像描述信息或者类型

        更新镜像描述信息或者类型
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateImage
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateImageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateImageResponse`
        """
        return self._update_image_with_http_info(request)

    def _update_image_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/images/{image_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_config(self, request):
        """获取作业配置

        获取作业配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobConfigResponse`
        """
        return self._show_job_config_with_http_info(request)

    def _show_job_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/job-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job_config(self, request):
        """设置作业配置

        设置作业配置，目前支持修改作业保存条数(1万条-1000万条)，默认设置为500万条；
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJobConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateJobConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateJobConfigResponse`
        """
        return self._update_job_config_with_http_info(request)

    def _update_job_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/job-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateJobConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_cancel_job(self, request):
        """批量取消作业

        批量取消作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchCancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchCancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchCancelJobResponse`
        """
        return self._batch_cancel_job_with_http_info(request)

    def _batch_cancel_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_force' in local_var_params:
            header_params['X-Force'] = local_var_params['x_force']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/batch-terminate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchCancelJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_job(self, request):
        """批量删除作业

        批量删除作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteJobResponse`
        """
        return self._batch_delete_job_with_http_info(request)

    def _batch_delete_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_retry_job(self, request):
        """批量重试作业

        批量重试作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchRetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchRetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchRetryJobResponse`
        """
        return self._batch_retry_job_with_http_info(request)

    def _batch_retry_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/batch-retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchRetryJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def cancel_job(self, request):
        """取消或强制停止作业调度

        取消或强制作业调度
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CancelJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CancelJobResponse`
        """
        return self._cancel_job_with_http_info(request)

    def _cancel_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/terminate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_job(self, request):
        """删除作业

        删除作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteJobResponse`
        """
        return self._delete_job_with_http_info(request)

    def _delete_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_job(self, request):
        """启动作业

        启动作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ExecuteJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ExecuteJobResponse`
        """
        return self._execute_job_with_http_info(request)

    def _execute_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job(self, request):
        """获取作业列表

        获取作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListJobResponse`
        """
        return self._list_job_with_http_info(request)

    def _list_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'tool_name' in local_var_params:
            query_params.append(('tool_name', local_var_params['tool_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_job(self, request):
        """重试作业

        重试作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryJobResponse`
        """
        return self._retry_job_with_http_info(request)

    def _retry_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job(self, request):
        """获取作业详情

        获取作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobResponse`
        """
        return self._show_job_with_http_info(request)

    def _show_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_addition_info' in local_var_params:
            header_params['X-Addition-Info'] = local_var_params['x_addition_info']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_event(self, request):
        """获取作业事件

        获取作业事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobEvent
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobEventRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobEventResponse`
        """
        return self._show_job_event_with_http_info(request)

    def _show_job_event_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobEventResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_log(self, request):
        """获取作业日志

        获取作业日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowJobLogResponse`
        """
        return self._show_job_log_with_http_info(request)

    def _show_job_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'task_name' in local_var_params:
            query_params.append(('task_name', local_var_params['task_name']))
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_events(self, request):
        """获取子任务启动事件

        获取子任务启动事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskEventsResponse`
        """
        return self._show_task_events_with_http_info(request)

    def _show_task_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instance_events(self, request):
        """获取子任务中实例的事件

        获取子任务中实例的事件
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstanceEvents
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceEventsResponse`
        """
        return self._show_task_instance_events_with_http_info(request)

    def _show_task_instance_events_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/events',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskInstanceEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instance_metric_data(self, request):
        """获取子任务中实例的资源监控数据

        获取子任务中实例的资源监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstanceMetricData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceMetricDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstanceMetricDataResponse`
        """
        return self._show_task_instance_metric_data_with_http_info(request)

    def _show_task_instance_metric_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskInstanceMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instance_pod(self, request):
        """获取子任务中实例的pod信息

        获取子任务中实例的pod信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstancePod
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancePodResponse`
        """
        return self._show_task_instance_pod_with_http_info(request)

    def _show_task_instance_pod_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']
        if 'instance_name' in local_var_params:
            path_params['instance_name'] = local_var_params['instance_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances/{instance_name}/pod',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskInstancePodResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_task_instances(self, request):
        """获取子任务实例信息

        获取子任务实例信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTaskInstances
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTaskInstancesResponse`
        """
        return self._show_task_instances_with_http_info(request)

    def _show_task_instances_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []
        if 'task_index' in local_var_params:
            query_params.append(('task_index', local_var_params['task_index']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}/tasks/{task_name}/instances',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTaskInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job(self, request):
        """更新作业

        更新作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateJobResponse`
        """
        return self._update_job_with_http_info(request)

    def _update_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_label(self, request):
        """批量删除标签

        批量删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteLabelResponse`
        """
        return self._batch_delete_label_with_http_info(request)

    def _batch_delete_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/labels/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_label(self, request):
        """创建标签

        创建标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelResponse`
        """
        return self._create_label_with_http_info(request)

    def _create_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_label(self, request):
        """删除标签

        删除标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelResponse`
        """
        return self._delete_label_with_http_info(request)

    def _delete_label_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['label_id'] = local_var_params['label_id']

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
            resource_path='/v1/{project_id}/system/labels/{label_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_label(self, request):
        """获取标签列表

        获取标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelResponse`
        """
        return self._list_label_with_http_info(request)

    def _list_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_label_page(self, request):
        """创建标签页面

        创建标签页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateLabelPageResponse`
        """
        return self._create_label_page_with_http_info(request)

    def _create_label_page_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateLabelPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_label_page(self, request):
        """删除标签页面

        删除标签页面
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteLabelPageResponse`
        """
        return self._delete_label_page_with_http_info(request)

    def _delete_label_page_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'label_page_id' in local_var_params:
            path_params['label_page_id'] = local_var_params['label_page_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages/{label_page_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteLabelPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_label_page(self, request):
        """获取标签页面列表

        获取标签页面列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListLabelPage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListLabelPageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListLabelPageResponse`
        """
        return self._list_label_page_with_http_info(request)

    def _list_label_page_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/label-pages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListLabelPageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_notice(self, request):
        """批量删除通知消息

        批量删除通知消息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteNotice
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteNoticeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteNoticeResponse`
        """
        return self._batch_delete_notice_with_http_info(request)

    def _batch_delete_notice_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/notices/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteNoticeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_notice(self, request):
        """批量更新消息

        批量更新消息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNotice
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNoticeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNoticeResponse`
        """
        return self._batch_update_notice_with_http_info(request)

    def _batch_update_notice_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/notices/batch-update',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateNoticeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_email_connection(self, request):
        """邮箱连通性测试

        邮箱连通性测试
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckEmailConnection
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckEmailConnectionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckEmailConnectionResponse`
        """
        return self._check_email_connection_with_http_info(request)

    def _check_email_connection_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-connection-test',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckEmailConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_message_email_config(self, request):
        """删除消息邮件配置

        删除消息邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMessageEmailConfigResponse`
        """
        return self._delete_message_email_config_with_http_info(request)

    def _delete_message_email_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-server-config',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMessageEmailConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_message(self, request):
        """获取消息列表

        从消息中心获取当前用户有权限查看的消息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMessage
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMessageRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMessageResponse`
        """
        return self._list_message_with_http_info(request)

    def _list_message_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'eihealth_project_name' in local_var_params:
            query_params.append(('eihealth_project_name', local_var_params['eihealth_project_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'message_type' in local_var_params:
            query_params.append(('message_type', local_var_params['message_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'operator' in local_var_params:
            query_params.append(('operator', local_var_params['operator']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v1/{project_id}/messages',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMessageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_message_statistics(self, request):
        """统计消息信息

        统计消息信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMessageStatistics
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMessageStatisticsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMessageStatisticsResponse`
        """
        return self._list_message_statistics_with_http_info(request)

    def _list_message_statistics_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMessageStatisticsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notice(self, request):
        """获取通知消息列表

        获取通知消息列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotice
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNoticeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNoticeResponse`
        """
        return self._list_notice_with_http_info(request)

    def _list_notice_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'is_read' in local_var_params:
            query_params.append(('is_read', local_var_params['is_read']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v1/{project_id}/notices',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNoticeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_clear_rule(self, request):
        """获取消息清理规则

        获取消息清理规则
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMessageClearRule
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageClearRuleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageClearRuleResponse`
        """
        return self._show_message_clear_rule_with_http_info(request)

    def _show_message_clear_rule_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMessageClearRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_email_config(self, request):
        """获取消息邮件配置

        获取消息邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageEmailConfigResponse`
        """
        return self._show_message_email_config_with_http_info(request)

    def _show_message_email_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-server-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMessageEmailConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_message_receive_config(self, request):
        """获取用户邮件配置

        获取用户邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowMessageReceiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowMessageReceiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowMessageReceiveConfigResponse`
        """
        return self._show_message_receive_config_with_http_info(request)

    def _show_message_receive_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-client-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowMessageReceiveConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_message_clear_rule_request_body(self, request):
        """设置消息清理规则

        设置消息清理规则，支持修改记录数(1W-1000W)
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMessageClearRuleRequestBody
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageClearRuleRequestBodyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageClearRuleRequestBodyResponse`
        """
        return self._update_message_clear_rule_request_body_with_http_info(request)

    def _update_message_clear_rule_request_body_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMessageClearRuleRequestBodyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_message_email_config(self, request):
        """设置消息邮件配置

        设置消息邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMessageEmailConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageEmailConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageEmailConfigResponse`
        """
        return self._update_message_email_config_with_http_info(request)

    def _update_message_email_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-server-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMessageEmailConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_message_receive_config(self, request):
        """设置用户邮件配置

        设置用户邮件配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMessageReceiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMessageReceiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMessageReceiveConfigResponse`
        """
        return self._update_message_receive_config_with_http_info(request)

    def _update_message_receive_config_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/messages/email-client-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMessageReceiveConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def clean_nextflow_cache(self, request):
        """清理Nextflow缓存

        清理Nextflow缓存
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CleanNextflowCache
        :type request: :class:`huaweicloudsdkeihealth.v1.CleanNextflowCacheRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CleanNextflowCacheResponse`
        """
        return self._clean_nextflow_cache_with_http_info(request)

    def _clean_nextflow_cache_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/nextflow/clean-cache',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CleanNextflowCacheResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def install_nextflow(self, request):
        """安装Nextflow

        安装Nextflow（file和version参数必须提供其中一种）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InstallNextflow
        :type request: :class:`huaweicloudsdkeihealth.v1.InstallNextflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.InstallNextflowResponse`
        """
        return self._install_nextflow_with_http_info(request)

    def _install_nextflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'part_number' in local_var_params:
            form_params['part_number'] = local_var_params['part_number']
        if 'total_part' in local_var_params:
            form_params['total_part'] = local_var_params['total_part']
        if 'multipart_id' in local_var_params:
            form_params['multipart_id'] = local_var_params['multipart_id']
        if 'file_name' in local_var_params:
            form_params['file_name'] = local_var_params['file_name']
        if 'version' in local_var_params:
            form_params['version'] = local_var_params['version']

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
            resource_path='/v1/{project_id}/nextflow/engines',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='InstallNextflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nextflow_version(self, request):
        """查询Nextflow版本列表

        查询Nextflow版本列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNextflowVersion
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowVersionRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowVersionResponse`
        """
        return self._list_nextflow_version_with_http_info(request)

    def _list_nextflow_version_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/nextflow/versions',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNextflowVersionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow(self, request):
        """查询Nextflow配置详情

        查询Nextflow配置详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowResponse`
        """
        return self._show_nextflow_with_http_info(request)

    def _show_nextflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/nextflow/engines/{id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def uninstall_nextflow(self, request):
        """卸载Nextflow

        卸载Nextflow
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UninstallNextflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UninstallNextflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UninstallNextflowResponse`
        """
        return self._uninstall_nextflow_with_http_info(request)

    def _uninstall_nextflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/nextflow/engines/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UninstallNextflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nextflow_job(self, request):
        """创建nextflow作业

        创建nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNextflowJobResponse`
        """
        return self._create_nextflow_job_with_http_info(request)

    def _create_nextflow_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']
        if 'labels' in local_var_params:
            form_params['labels'] = local_var_params['labels']
            collection_formats['labels'] = 'csv'
        if 'workflow_id' in local_var_params:
            form_params['workflow_id'] = local_var_params['workflow_id']
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNextflowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nextflow_job(self, request):
        """删除Nextflow作业

        删除Nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowJobResponse`
        """
        return self._delete_nextflow_job_with_http_info(request)

    def _delete_nextflow_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNextflowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nextflow_job(self, request):
        """查询nextflow作业列表

        查询nextflow作业列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowJobResponse`
        """
        return self._list_nextflow_job_with_http_info(request)

    def _list_nextflow_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'labels' in local_var_params:
            query_params.append(('labels', local_var_params['labels']))
            collection_formats['labels'] = 'csv'
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'workflow_name' in local_var_params:
            query_params.append(('workflow_name', local_var_params['workflow_name']))
        if 'user_name' in local_var_params:
            query_params.append(('user_name', local_var_params['user_name']))
        if 'create_start_time' in local_var_params:
            query_params.append(('create_start_time', local_var_params['create_start_time']))
        if 'create_end_time' in local_var_params:
            query_params.append(('create_end_time', local_var_params['create_end_time']))
        if 'finish_start_time' in local_var_params:
            query_params.append(('finish_start_time', local_var_params['finish_start_time']))
        if 'finish_end_time' in local_var_params:
            query_params.append(('finish_end_time', local_var_params['finish_end_time']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNextflowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_nextflow_job(self, request):
        """重试Nextflow作业

        重试Nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.RetryNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.RetryNextflowJobResponse`
        """
        return self._retry_nextflow_job_with_http_info(request)

    def _retry_nextflow_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/retry',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryNextflowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow_job(self, request):
        """获取Nextflow作业详情

        获取Nextflow作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobResponse`
        """
        return self._show_nextflow_job_with_http_info(request)

    def _show_nextflow_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow_job_log(self, request):
        """获取Nextflow作业日志

        获取Nextflow作业日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflowJobLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobLogResponse`
        """
        return self._show_nextflow_job_log_with_http_info(request)

    def _show_nextflow_job_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowJobLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow_job_reports(self, request):
        """获取Nextflow作业报告

        获取Nextflow作业报告
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflowJobReports
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobReportsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowJobReportsResponse`
        """
        return self._show_nextflow_job_reports_with_http_info(request)

    def _show_nextflow_job_reports_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/reports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowJobReportsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_nextflow_job(self, request):
        """停止Nextflow作业

        停止Nextflow作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopNextflowJob
        :type request: :class:`huaweicloudsdkeihealth.v1.StopNextflowJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopNextflowJobResponse`
        """
        return self._stop_nextflow_job_with_http_info(request)

    def _stop_nextflow_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopNextflowJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nextflow_task(self, request):
        """获取task列表

        获取task列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNextflowTask
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowTaskResponse`
        """
        return self._list_nextflow_task_with_http_info(request)

    def _list_nextflow_task_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNextflowTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow_task_detail(self, request):
        """获取task详情

        获取task详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflowTaskDetail
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskDetailRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskDetailResponse`
        """
        return self._show_nextflow_task_detail_with_http_info(request)

    def _show_nextflow_task_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowTaskDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow_task_log(self, request):
        """获取Nextflow任务日志

        获取Nextflow任务日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflowTaskLog
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskLogRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowTaskLogResponse`
        """
        return self._show_nextflow_task_log_with_http_info(request)

    def _show_nextflow_task_log_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/jobs/{job_id}/tasks/{task_id}/logs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowTaskLogResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_nextflow_workflow(self, request):
        """创建流程

        创建流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNextflowWorkflowResponse`
        """
        return self._create_nextflow_workflow_with_http_info(request)

    def _create_nextflow_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'workflow_file' in local_var_params:
            form_params['workflow_file'] = local_var_params['workflow_file']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']
        if 'labels' in local_var_params:
            form_params['labels'] = local_var_params['labels']
            collection_formats['labels'] = 'csv'
        if 'main_file' in local_var_params:
            form_params['main_file'] = local_var_params['main_file']
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNextflowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_nextflow_workflow(self, request):
        """删除流程

        删除流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNextflowWorkflowResponse`
        """
        return self._delete_nextflow_workflow_with_http_info(request)

    def _delete_nextflow_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows/{workflow_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNextflowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_nextflow_workflow(self, request):
        """获取流程列表

        获取流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNextflowWorkflowResponse`
        """
        return self._list_nextflow_workflow_with_http_info(request)

    def _list_nextflow_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNextflowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_nextflow_workflow(self, request):
        """获取流程详情

        获取流程详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNextflowWorkflowResponse`
        """
        return self._show_nextflow_workflow_with_http_info(request)

    def _show_nextflow_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows/{workflow_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNextflowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_nextflow_workflow(self, request):
        """更新流程

        更新流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNextflowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateNextflowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateNextflowWorkflowResponse`
        """
        return self._update_nextflow_workflow_with_http_info(request)

    def _update_nextflow_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'workflow_file' in local_var_params:
            form_params['workflow_file'] = local_var_params['workflow_file']
        if 'description' in local_var_params:
            form_params['description'] = local_var_params['description']
        if 'labels' in local_var_params:
            form_params['labels'] = local_var_params['labels']
            collection_formats['labels'] = 'csv'
        if 'main_file' in local_var_params:
            form_params['main_file'] = local_var_params['main_file']
        if 'params' in local_var_params:
            form_params['params'] = local_var_params['params']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/nextflow/workflows/{workflow_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNextflowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_update_node_label(self, request):
        """设置节点标签

        设置节点标签
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchUpdateNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchUpdateNodeLabelResponse`
        """
        return self._batch_update_node_label_with_http_info(request)

    def _batch_update_node_label_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/system/nodes/{server_id}/labels',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchUpdateNodeLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_cluster_all_node_label(self, request):
        """获取节点标签集

        获取节点标签集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListClusterAllNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListClusterAllNodeLabelResponse`
        """
        return self._list_cluster_all_node_label_with_http_info(request)

    def _list_cluster_all_node_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/cluster/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListClusterAllNodeLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_node_label(self, request):
        """获取节点标签集

        获取节点标签集
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNodeLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNodeLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNodeLabelResponse`
        """
        return self._list_node_label_with_http_info(request)

    def _list_node_label_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

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
            resource_path='/v1/{project_id}/system/nodes/{server_id}/labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNodeLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_preset_label(self, request):
        """获取预置标签列表

        获取预置标签列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPresetLabel
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPresetLabelRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPresetLabelResponse`
        """
        return self._list_preset_label_with_http_info(request)

    def _list_preset_label_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/preset-labels',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPresetLabelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_notebook(self, request):
        """创建notebook

        创建notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateNotebookResponse`
        """
        return self._create_notebook_with_http_info(request)

    def _create_notebook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_notebook(self, request):
        """删除notebook

        删除notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteNotebookResponse`
        """
        return self._delete_notebook_with_http_info(request)

    def _delete_notebook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notebook(self, request):
        """获取notebook列表

        获取notebook列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookResponse`
        """
        return self._list_notebook_with_http_info(request)

    def _list_notebook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_notebook_tool(self, request):
        """获取notebook工作环境

        获取notebook工作环境
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListNotebookTool
        :type request: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListNotebookToolResponse`
        """
        return self._list_notebook_tool_with_http_info(request)

    def _list_notebook_tool_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/tools',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListNotebookToolResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_notebook(self, request):
        """获取notebook详情

        获取notebook详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookResponse`
        """
        return self._show_notebook_with_http_info(request)

    def _show_notebook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_notebook_token(self, request):
        """获取notebook鉴权信息

        获取notebook鉴权信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowNotebookToken
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowNotebookTokenResponse`
        """
        return self._show_notebook_token_with_http_info(request)

    def _show_notebook_token_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}/token',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowNotebookTokenResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_or_start_notebook(self, request):
        """启停notebook

        启停notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopOrStartNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.StopOrStartNotebookResponse`
        """
        return self._stop_or_start_notebook_with_http_info(request)

    def _stop_or_start_notebook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopOrStartNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_notebook(self, request):
        """更新notebook

        更新notebook
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateNotebook
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateNotebookResponse`
        """
        return self._update_notebook_with_http_info(request)

    def _update_notebook_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'notebook_id' in local_var_params:
            path_params['notebook_id'] = local_var_params['notebook_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/notebooks/{notebook_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateNotebookResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_data(self, request):
        """文件下载

        文件下载
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadData
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataResponse`
        """
        return self._download_data_with_http_info(request)

    def _download_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data/download',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_obs_bucket(self, request):
        """获取用户OBS桶列表

        获取用户OBS桶列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBucket
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketResponse`
        """
        return self._list_obs_bucket_with_http_info(request)

    def _list_obs_bucket_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/customer-buckets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListObsBucketResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_obs_bucket_object(self, request):
        """获取用户OBS桶内对象

        获取用户OBS桶内对象
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListObsBucketObject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListObsBucketObjectResponse`
        """
        return self._list_obs_bucket_object_with_http_info(request)

    def _list_obs_bucket_object_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'bucket_name' in local_var_params:
            path_params['bucket_name'] = local_var_params['bucket_name']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'search_key' in local_var_params:
            query_params.append(('search_key', local_var_params['search_key']))

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
            resource_path='/v1/{project_id}/customer-buckets/{bucket_name}/objects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListObsBucketObjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_optm_job(self, request):
        """创建分子优化作业

        创建分子优化作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOptmJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateOptmJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateOptmJobResponse`
        """
        return self._create_optm_job_with_http_info(request)

    def _create_optm_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/optimization',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOptmJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_optm_job(self, request):
        """查询分子优化作业详情

        查询分子优化作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOptmJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOptmJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOptmJobResponse`
        """
        return self._show_optm_job_with_http_info(request)

    def _show_optm_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/optimization/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOptmJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_overview(self, request):
        """获取医疗平台信息

        获取医疗平台信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOverview
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOverviewRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOverviewResponse`
        """
        return self._show_overview_with_http_info(request)

    def _show_overview_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/overview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOverviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_performance_resource(self, request):
        """购买性能加速资源

        购买性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreatePerformanceResourceResponse`
        """
        return self._create_performance_resource_with_http_info(request)

    def _create_performance_resource_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/performance-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePerformanceResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_performance_resource(self, request):
        """删除性能加速资源

        删除性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeletePerformanceResourceResponse`
        """
        return self._delete_performance_resource_with_http_info(request)

    def _delete_performance_resource_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/performance-resources/{id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePerformanceResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_performance_resources(self, request):
        """查询性能加速资源

        查询性能加速资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPerformanceResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourcesResponse`
        """
        return self._list_performance_resources_with_http_info(request)

    def _list_performance_resources_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/performance-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPerformanceResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_performance_resource(self, request):
        """更新性能加速资源配置

        更新性能加速资源配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdatePerformanceResource
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdatePerformanceResourceResponse`
        """
        return self._update_performance_resource_with_http_info(request)

    def _update_performance_resource_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']

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
            resource_path='/v1/{project_id}/system/performance-resources/{id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdatePerformanceResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_delete_member(self, request):
        """批量删除项目成员

        批量删除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDeleteMemberResponse`
        """
        return self._batch_delete_member_with_http_info(request)

    def _batch_delete_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/batch-delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_project(self, request):
        """创建项目

        创建项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateProjectResponse`
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
            resource_path='/v1/{project_id}/eihealth-projects',
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

    def delete_member(self, request):
        """移除项目成员

        移除项目成员
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteMember
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteMemberResponse`
        """
        return self._delete_member_with_http_info(request)

    def _delete_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_project(self, request):
        """删除项目

        删除项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteProject
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteProjectResponse`
        """
        return self._delete_project_with_http_info(request)

    def _delete_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_delete_now' in local_var_params:
            header_params['X-Delete-Now'] = local_var_params['x_delete_now']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}',
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

    def list_project(self, request):
        """获取项目列表

        获取项目列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ListProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListProjectResponse`
        """
        return self._list_project_with_http_info(request)

    def _list_project_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/eihealth-projects',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project(self, request):
        """获取项目详情

        获取项目详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProject
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectResponse`
        """
        return self._show_project_with_http_info(request)

    def _show_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_bucket_name' in local_var_params:
            header_params['X-Bucket-Name'] = local_var_params['x_bucket_name']
        if 'x_namespace_name' in local_var_params:
            header_params['X-Namespace-Name'] = local_var_params['x_namespace_name']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}',
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

    def transfer_project(self, request):
        """转移项目

        转移项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for TransferProject
        :type request: :class:`huaweicloudsdkeihealth.v1.TransferProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.TransferProjectResponse`
        """
        return self._transfer_project_with_http_info(request)

    def _transfer_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/transfer',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='TransferProjectResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_member(self, request):
        """更新或者添加项目成员角色

        更新或者添加项目成员角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateMember
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateMemberRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateMemberResponse`
        """
        return self._update_member_with_http_info(request)

    def _update_member_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/members/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateMemberResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project(self, request):
        """更新项目

        更新项目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProject
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectResponse`
        """
        return self._update_project_with_http_info(request)

    def _update_project_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}',
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

    def download_data_trace(self, request):
        """下载近一万条审计日志

        下载近一万条审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadDataTrace
        :type request: :class:`huaweicloudsdkeihealth.v1.DownloadDataTraceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DownloadDataTraceResponse`
        """
        return self._download_data_trace_with_http_info(request)

    def _download_data_trace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/data-traces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadDataTraceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_trace(self, request):
        """获取项目审计日志

        获取项目审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectTrace
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceResponse`
        """
        return self._show_project_trace_with_http_info(request)

    def _show_project_trace_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'path' in local_var_params:
            query_params.append(('path', local_var_params['path']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-traces',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectTraceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_trace_data(self, request):
        """获取指定审计日志

        获取指定审计日志
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectTraceData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTraceDataResponse`
        """
        return self._show_project_trace_data_with_http_info(request)

    def _show_project_trace_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'path' in local_var_params:
            path_params['path'] = local_var_params['path']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-traces/{path}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectTraceDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_project_tracker(self, request):
        """获取项目审计日志追踪器

        获取项目审计日志追踪器
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowProjectTracker
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowProjectTrackerRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowProjectTrackerResponse`
        """
        return self._show_project_tracker_with_http_info(request)

    def _show_project_tracker_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-tracker',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowProjectTrackerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_project_tracker(self, request):
        """更新项目审计日志追踪器配置

        更新项目审计日志追踪器配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateProjectTracker
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateProjectTrackerRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateProjectTrackerResponse`
        """
        return self._update_project_tracker_with_http_info(request)

    def _update_project_tracker_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/project-tracker',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateProjectTrackerResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_download_resource_stat_data(self, request):
        """批量获取资源统计数据

        批量获取资源统计数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchDownloadResourceStatData
        :type request: :class:`huaweicloudsdkeihealth.v1.BatchDownloadResourceStatDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.BatchDownloadResourceStatDataResponse`
        """
        return self._batch_download_resource_stat_data_with_http_info(request)

    def _batch_download_resource_stat_data_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/metric-data/batch-stat-metric-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchDownloadResourceStatDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource_metric_data(self, request):
        """获取资源监控数据

        获取资源监控数据
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResourceMetricData
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowResourceMetricDataRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowResourceMetricDataResponse`
        """
        return self._show_resource_metric_data_with_http_info(request)

    def _show_resource_metric_data_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'from_time' in local_var_params:
            query_params.append(('from_time', local_var_params['from_time']))
        if 'to_time' in local_var_params:
            query_params.append(('to_time', local_var_params['to_time']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'method' in local_var_params:
            query_params.append(('method', local_var_params['method']))
        if 'metric_name' in local_var_params:
            query_params.append(('metric_name', local_var_params['metric_name']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))

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
            resource_path='/v1/{project_id}/metric-data',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceMetricDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_star(self, request):
        """取消收藏

        取消收藏
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStar
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteStarResponse`
        """
        return self._delete_star_with_http_info(request)

    def _delete_star_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/stars',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_star(self, request):
        """获取收藏资产列表

        获取收藏资产列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStar
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStarResponse`
        """
        return self._list_star_with_http_info(request)

    def _list_star_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/assets/stars',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_star(self, request):
        """收藏资产

        收藏资产
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateStar
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateStarRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateStarResponse`
        """
        return self._update_star_with_http_info(request)

    def _update_star_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/stars',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateStarResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_global_workflow_statistic(self, request):
        """统计全局流程、作业信息

        统计全局流程、作业信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListGlobalWorkflowStatistic
        :type request: :class:`huaweicloudsdkeihealth.v1.ListGlobalWorkflowStatisticRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListGlobalWorkflowStatisticResponse`
        """
        return self._list_global_workflow_statistic_with_http_info(request)

    def _list_global_workflow_statistic_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/eihealth-projects/workflow-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListGlobalWorkflowStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_performance_resource_stat(self, request):
        """获取性能加速资源上统计信息

        获取性能加速资源上统计信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPerformanceResourceStat
        :type request: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListPerformanceResourceStatResponse`
        """
        return self._list_performance_resource_stat_with_http_info(request)

    def _list_performance_resource_stat_with_http_info(self, request):
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

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/performance-resources-statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPerformanceResourceStatResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow_statistic(self, request):
        """统计应用、流程、作业数目

        统计应用、流程、作业数目
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflowStatistic
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowStatisticRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowStatisticResponse`
        """
        return self._list_workflow_statistic_with_http_info(request)

    def _list_workflow_statistic_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/statistics',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkflowStatisticResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_storage_resources(self, request):
        """查询存储资源

        查询存储资源
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStorageResources
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStorageResourcesRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStorageResourcesResponse`
        """
        return self._list_storage_resources_with_http_info(request)

    def _list_storage_resources_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/storage-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStorageResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_study(self, request):
        """创建study

        创建study
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateStudyResponse`
        """
        return self._create_study_with_http_info(request)

    def _create_study_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStudyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_study_job(self, request):
        """创建study作业

        创建study作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStudyJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateStudyJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateStudyJobResponse`
        """
        return self._create_study_job_with_http_info(request)

    def _create_study_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateStudyJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_study(self, request):
        """删除study

        删除study
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteStudyResponse`
        """
        return self._delete_study_with_http_info(request)

    def _delete_study_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteStudyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_study(self, request):
        """列举study

        列举study
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStudy
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStudyRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStudyResponse`
        """
        return self._list_study_with_http_info(request)

    def _list_study_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/studies',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStudyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_study_job(self, request):
        """列举study所有作业

        列举study所有作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStudyJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ListStudyJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListStudyJobResponse`
        """
        return self._list_study_job_with_http_info(request)

    def _list_study_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListStudyJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show3d_structure_content(self, request):
        """获取生成study作业3D结构的内容

        获取生成study作业3D结构的内容
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for Show3dStructureContent
        :type request: :class:`huaweicloudsdkeihealth.v1.Show3dStructureContentRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.Show3dStructureContentResponse`
        """
        return self._show3d_structure_content_with_http_info(request)

    def _show3d_structure_content_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'ligand' in local_var_params:
            query_params.append(('ligand', local_var_params['ligand']))
        if 'receptor' in local_var_params:
            query_params.append(('receptor', local_var_params['receptor']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs/{job_id}/3d-structure',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='Show3dStructureContentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_extremum_info(self, request):
        """获取study作业的最值信息

        获取study作业的最值信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowExtremumInfo
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowExtremumInfoRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowExtremumInfoResponse`
        """
        return self._show_extremum_info_with_http_info(request)

    def _show_extremum_info_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'study_id' in local_var_params:
            path_params['study_id'] = local_var_params['study_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/studies/{study_id}/jobs/{job_id}/extremum',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowExtremumInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_synthesis_job(self, request):
        """创建分子合成路径规划作业

        创建分子合成路径规划作业
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSynthesisJob
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisJobResponse`
        """
        return self._create_synthesis_job_with_http_info(request)

    def _create_synthesis_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/synthesis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSynthesisJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_synthesis_job(self, request):
        """查询分子合成路径规划作业详情

        查询分子合成路径规划作业详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSynthesisJob
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisJobRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisJobResponse`
        """
        return self._show_synthesis_job_with_http_info(request)

    def _show_synthesis_job_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/drug-jobs/synthesis/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSynthesisJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_archive_configs(self, request):
        """获取跨域归档配置

        获取跨域归档配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListArchiveConfigs
        :type request: :class:`huaweicloudsdkeihealth.v1.ListArchiveConfigsRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListArchiveConfigsResponse`
        """
        return self._list_archive_configs_with_http_info(request)

    def _list_archive_configs_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/archive-configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListArchiveConfigsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_env(self, request):
        """查询系统配置列表

        获取系统配置列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEnv
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowEnvRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowEnvResponse`
        """
        return self._show_env_with_http_info(request)

    def _show_env_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/configs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEnvResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_vendor(self, request):
        """获取供应商配置

        获取供应商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowVendorResponse`
        """
        return self._show_vendor_with_http_info(request)

    def _show_vendor_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/system/vendor-config',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowVendorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_archive_config(self, request):
        """修改跨域归档设置

        修改跨域归档设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateArchiveConfig
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateArchiveConfigRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateArchiveConfigResponse`
        """
        return self._update_archive_config_with_http_info(request)

    def _update_archive_config_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'region_id' in local_var_params:
            path_params['region_id'] = local_var_params['region_id']

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
            resource_path='/v1/{project_id}/system/archive-configs/{region_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateArchiveConfigResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_vendor(self, request):
        """设置供应商配置

        设置供应商配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateVendorResponse`
        """
        return self._update_vendor_with_http_info(request)

    def _update_vendor_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']
        if 'name' in local_var_params:
            form_params['name'] = local_var_params['name']

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
            resource_path='/v1/{project_id}/system/vendor-config',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateVendorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_quota(self, request):
        """获取当前系统配额及资源使用情况

        获取当前系统配额及资源使用情况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListQuota
        :type request: :class:`huaweicloudsdkeihealth.v1.ListQuotaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListQuotaResponse`
        """
        return self._list_quota_with_http_info(request)

    def _list_quota_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_template(self, request):
        """创建模板

        创建模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateTemplateResponse`
        """
        return self._create_template_with_http_info(request)

    def _create_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_template(self, request):
        """删除模板

        删除模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteTemplateResponse`
        """
        return self._delete_template_with_http_info(request)

    def _delete_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/{template_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_template(self, request):
        """从其他项目导入模板

        从其他项目导入模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportTemplateResponse`
        """
        return self._import_template_with_http_info(request)

    def _import_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/batch-import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_template(self, request):
        """查询模板列表

        查询模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ListTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListTemplateResponse`
        """
        return self._list_template_with_http_info(request)

    def _list_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_template(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowTemplateResponse`
        """
        return self._show_template_with_http_info(request)

    def _show_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_template(self, request):
        """上传模板

        上传模板
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadTemplate
        :type request: :class:`huaweicloudsdkeihealth.v1.UploadTemplateRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UploadTemplateResponse`
        """
        return self._upload_template_with_http_info(request)

    def _upload_template_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []

        header_params = {}

        form_params = {}
        if 'file' in local_var_params:
            form_params['file'] = local_var_params['file']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/templates/upload',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def change_password(self, request):
        """修改密码

        修改密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ChangePassword
        :type request: :class:`huaweicloudsdkeihealth.v1.ChangePasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ChangePasswordResponse`
        """
        return self._change_password_with_http_info(request)

    def _change_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/password',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ChangePasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def check_token_verification(self, request):
        """校验token

        校验token是否可访问当前环境
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckTokenVerification
        :type request: :class:`huaweicloudsdkeihealth.v1.CheckTokenVerificationRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CheckTokenVerificationResponse`
        """
        return self._check_token_verification_with_http_info(request)

    def _check_token_verification_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/users/token-verification',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CheckTokenVerificationResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_code(self, request):
        """发送验证码

        发送验证码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateCodeResponse`
        """
        return self._create_code_with_http_info(request)

    def _create_code_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/verification-code',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_user(self, request):
        """创建用户

        创建用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateUserResponse`
        """
        return self._create_user_with_http_info(request)

    def _create_user_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/users',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_user(self, request):
        """删除用户

        删除用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteUser
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteUserResponse`
        """
        return self._delete_user_with_http_info(request)

    def _delete_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_user(self, request):
        """导入用户

        导入用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportUserResponse`
        """
        return self._import_user_with_http_info(request)

    def _import_user_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/users/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_mfa(self, request):
        """获取可用的认证方法

        获取可用的认证方法
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListMfa
        :type request: :class:`huaweicloudsdkeihealth.v1.ListMfaRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListMfaResponse`
        """
        return self._list_mfa_with_http_info(request)

    def _list_mfa_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/mfa/methods',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListMfaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_user(self, request):
        """获取用户列表

        获取用户列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ListUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListUserResponse`
        """
        return self._list_user_with_http_info(request)

    def _list_user_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/users',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user(self, request):
        """获取指定用户详情

        获取指定用户详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUser
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserResponse`
        """
        return self._show_user_with_http_info(request)

    def _show_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_user_setting(self, request):
        """查询用户设置

        查询用户设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowUserSettingResponse`
        """
        return self._show_user_setting_with_http_info(request)

    def _show_user_setting_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/settings',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowUserSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_init_password(self, request):
        """新用户重置密码

        新用户重置密码
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateInitPassword
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateInitPasswordResponse`
        """
        return self._update_init_password_with_http_info(request)

    def _update_init_password_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/init-password',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateInitPasswordResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user(self, request):
        """修改用户基本信息

        修改用户基本信息（邮箱，手机）
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUser
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserResponse`
        """
        return self._update_user_with_http_info(request)

    def _update_user_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_by_domain(self, request):
        """最终租户修改子用户

        最终租户修改子用户
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserByDomain
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserByDomainResponse`
        """
        return self._update_user_by_domain_with_http_info(request)

    def _update_user_by_domain_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/domain-change-info',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserByDomainResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_role(self, request):
        """更新用户角色

        更新用户角色
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserRole
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserRoleResponse`
        """
        return self._update_user_role_with_http_info(request)

    def _update_user_role_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/role',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserRoleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_user_setting(self, request):
        """更新用户设置

        更新用户设置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateUserSetting
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateUserSettingResponse`
        """
        return self._update_user_setting_with_http_info(request)

    def _update_user_setting_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/settings',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateUserSettingResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def validate_code(self, request):
        """预验证

        预验证
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ValidateCode
        :type request: :class:`huaweicloudsdkeihealth.v1.ValidateCodeRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ValidateCodeResponse`
        """
        return self._validate_code_with_http_info(request)

    def _validate_code_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['user_id'] = local_var_params['user_id']

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
            resource_path='/v1/{project_id}/users/{user_id}/code-verify',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ValidateCodeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_vendor(self, request):
        """获取供应商列表

        获取供应商列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListVendor
        :type request: :class:`huaweicloudsdkeihealth.v1.ListVendorRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListVendorResponse`
        """
        return self._list_vendor_with_http_info(request)

    def _list_vendor_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/vendors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListVendorResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_workflow(self, request):
        """创建流程

        创建流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateWorkflowResponse`
        """
        return self._create_workflow_with_http_info(request)

    def _create_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_workflow(self, request):
        """删除流程

        删除流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.DeleteWorkflowResponse`
        """
        return self._delete_workflow_with_http_info(request)

    def _delete_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_workflow(self, request):
        """导入流程

        导入流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ImportWorkflowResponse`
        """
        return self._import_workflow_with_http_info(request)

    def _import_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_workflow(self, request):
        """获取流程列表

        获取流程列表
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ListWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ListWorkflowResponse`
        """
        return self._list_workflow_with_http_info(request)

    def _list_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def publish_workflow(self, request):
        """发布流程

        发布流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PublishWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.PublishWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.PublishWorkflowResponse`
        """
        return self._publish_workflow_with_http_info(request)

    def _publish_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='PublishWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_workflow(self, request):
        """获取流程详情

        获取流程详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowWorkflowResponse`
        """
        return self._show_workflow_with_http_info(request)

    def _show_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []

        header_params = {}
        if 'show_param_detail' in local_var_params:
            header_params['Show-Param-Detail'] = local_var_params['show_param_detail']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def subscribe_workflow(self, request):
        """订阅流程

        订阅流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SubscribeWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.SubscribeWorkflowResponse`
        """
        return self._subscribe_workflow_with_http_info(request)

    def _subscribe_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/subscribe',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='SubscribeWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_workflow(self, request):
        """更新流程

        更新流程
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateWorkflow
        :type request: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.UpdateWorkflowResponse`
        """
        return self._update_workflow_with_http_info(request)

    def _update_workflow_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eihealth_project_id' in local_var_params:
            path_params['eihealth_project_id'] = local_var_params['eihealth_project_id']
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

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
            resource_path='/v1/{project_id}/eihealth-projects/{eihealth_project_id}/workflows/{workflow_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateWorkflowResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_optimization_task(self, request):
        """新建分子优化任务接口

        输入起始小分子以及属性约束，创建分子优化任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateOptimizationTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateOptimizationTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateOptimizationTaskResponse`
        """
        return self._create_optimization_task_with_http_info(request)

    def _create_optimization_task_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/optimization',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateOptimizationTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_optimization_task_result(self, request):
        """查询分子优化任务

        通过分子优化任务ID查询分子优化任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowOptimizationTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowOptimizationTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowOptimizationTaskResultResponse`
        """
        return self._show_optimization_task_result_with_http_info(request)

    def _show_optimization_task_result_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/optimization/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowOptimizationTaskResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_search_task(self, request):
        """新建分子搜索任务接口

        输入要查询的分子以及查询条件，创建分子搜索任务。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSearchTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSearchTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSearchTaskResponse`
        """
        return self._create_search_task_with_http_info(request)

    def _create_search_task_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/search',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSearchTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_search_task_result(self, request):
        """查询分子搜索任务

        通过分子搜索任务ID查询分子搜索任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSearchTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSearchTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSearchTaskResultResponse`
        """
        return self._show_search_task_result_with_http_info(request)

    def _show_search_task_result_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/search/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSearchTaskResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_synthesis_task(self, request):
        """新建分子合成路径规划任务接口

        输入要进行合成路径规划的分子以及输出可行方案的个数。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSynthesisTask
        :type request: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisTaskRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.CreateSynthesisTaskResponse`
        """
        return self._create_synthesis_task_with_http_info(request)

    def _create_synthesis_task_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/synthesis',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateSynthesisTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_synthesis_task_result(self, request):
        """查询分子合成路径规划任务

        通过分子合成路径规划任务ID查询分子合成路径规划任务状态及结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowSynthesisTaskResult
        :type request: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisTaskResultRequest`
        :rtype: :class:`huaweicloudsdkeihealth.v1.ShowSynthesisTaskResultResponse`
        """
        return self._show_synthesis_task_result_with_http_info(request)

    def _show_synthesis_task_result_with_http_info(self, request):
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
            resource_path='/v1/{project_id}/task/synthesis/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowSynthesisTaskResultResponse',
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

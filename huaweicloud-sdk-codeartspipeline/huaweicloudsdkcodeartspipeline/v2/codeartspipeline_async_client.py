# coding: utf-8

from __future__ import absolute_import

import importlib

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class CodeArtsPipelineAsyncClient(Client):
    def __init__(self):
        super(CodeArtsPipelineAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcodeartspipeline.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CodeArtsPipelineAsyncClient":
                raise TypeError("client type error, support client type is CodeArtsPipelineAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_show_pipelines_status_async(self, request):
        """批量获取流水线状态

        批量获取流水线状态和阶段信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchShowPipelinesStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesStatusResponse`
        """
        return self._batch_show_pipelines_status_with_http_info(request)

    def _batch_show_pipelines_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pipeline_ids' in local_var_params:
            query_params.append(('pipeline_ids', local_var_params['pipeline_ids']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowPipelinesStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_pipeline_by_template_async(self, request):
        """基于模板快速创建流水线及流水线内任务

        基于模板快速创建流水线及流水线内任务
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePipelineByTemplate
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateResponse`
        """
        return self._create_pipeline_by_template_with_http_info(request)

    def _create_pipeline_by_template_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates/task',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePipelineByTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pipeline_simple_info_async(self, request):
        """获取流水线列表接口

        获取流水线列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipelineSimpleInfo
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineSimpleInfoRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineSimpleInfoResponse`
        """
        return self._list_pipeline_simple_info_with_http_info(request)

    def _list_pipeline_simple_info_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPipelineSimpleInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pipleine_build_result_async(self, request):
        """获取项目下流水线执行状况

        获取项目下流水线执行状况
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipleineBuildResult
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipleineBuildResultRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipleineBuildResultResponse`
        """
        return self._list_pipleine_build_result_with_http_info(request)

    def _list_pipleine_build_result_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'project_id' in local_var_params:
            query_params.append(('project_id', local_var_params['project_id']))
        if 'start_date' in local_var_params:
            query_params.append(('start_date', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('end_date', local_var_params['end_date']))
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/build-result',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPipleineBuildResultResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_templates_async(self, request):
        """查询模板列表

        查询模板列表，支持分页查询,支持模板名字模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListTemplatesResponse`
        """
        return self._list_templates_with_http_info(request)

    def _list_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))
        if 'is_build_in' in local_var_params:
            query_params.append(('is_build_in', local_var_params['is_build_in']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'asc' in local_var_params:
            query_params.append(('asc', local_var_params['asc']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def remove_pipeline_async(self, request):
        """删除流水线

        根据id删除流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RemovePipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.RemovePipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RemovePipelineResponse`
        """
        return self._remove_pipeline_with_http_info(request)

    def _remove_pipeline_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/{pipeline_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RemovePipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_instance_status_async(self, request):
        """检查流水线创建状态

        检查流水线创建状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowInstanceStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowInstanceStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowInstanceStatusResponse`
        """
        return self._show_instance_status_with_http_info(request)

    def _show_instance_status_with_http_info(self, request):
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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates/{task_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowInstanceStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_pipleine_status_async(self, request):
        """获取流水线状态

        获取流水线状态,阶段及任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPipleineStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipleineStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipleineStatusResponse`
        """
        return self._show_pipleine_status_with_http_info(request)

    def _show_pipleine_status_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/{pipeline_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPipleineStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_template_detail_async(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTemplateDetail
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowTemplateDetailResponse`
        """
        return self._show_template_detail_with_http_info(request)

    def _show_template_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'template_type' in local_var_params:
            query_params.append(('template_type', local_var_params['template_type']))
        if 'source' in local_var_params:
            query_params.append(('source', local_var_params['source']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowTemplateDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_new_pipeline_async(self, request):
        """启动流水线

        启动流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartNewPipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.StartNewPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.StartNewPipelineResponse`
        """
        return self._start_new_pipeline_with_http_info(request)

    def _start_new_pipeline_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/{pipeline_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartNewPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_pipeline_new_async(self, request):
        """停止流水线

        停止流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopPipelineNew
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineNewRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineNewResponse`
        """
        return self._stop_pipeline_new_with_http_info(request)

    def _stop_pipeline_new_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/{pipeline_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopPipelineNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def batch_show_pipelines_latest_status_async(self, request):
        """批量获取流水线状态

        批量获取流水线状态
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchShowPipelinesLatestStatus
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesLatestStatusRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.BatchShowPipelinesLatestStatusResponse`
        """
        return self._batch_show_pipelines_latest_status_with_http_info(request)

    def _batch_show_pipelines_latest_status_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/api/pipelines/status',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='BatchShowPipelinesLatestStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_pipeline_by_template_id_async(self, request):
        """基于模板创建流水线

        基于模板创建流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreatePipelineByTemplateId
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateIdRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.CreatePipelineByTemplateIdResponse`
        """
        return self._create_pipeline_by_template_id_with_http_info(request)

    def _create_pipeline_by_template_id_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'template_id' in local_var_params:
            path_params['template_id'] = local_var_params['template_id']

        query_params = []
        if 'component_id' in local_var_params:
            query_params.append(('component_id', local_var_params['component_id']))

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
            resource_path='/v5/{project_id}/api/pipeline-templates/{template_id}/create-pipeline',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreatePipelineByTemplateIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_pipeline_async(self, request):
        """删除流水线

        删除流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeletePipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.DeletePipelineResponse`
        """
        return self._delete_pipeline_with_http_info(request)

    def _delete_pipeline_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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
            resource_path='/v5/{project_id}/api/pipelines/{pipeline_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeletePipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pipeline_runs_async(self, request):
        """获取流水线执行记录

        获取流水线执行记录
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipelineRuns
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineRunsRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineRunsResponse`
        """
        return self._list_pipeline_runs_with_http_info(request)

    def _list_pipeline_runs_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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
            resource_path='/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPipelineRunsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pipeline_templates_async(self, request):
        """查询模板列表

        查询流水线模板列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipelineTemplates
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelineTemplatesResponse`
        """
        return self._list_pipeline_templates_with_http_info(request)

    def _list_pipeline_templates_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']

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
            resource_path='/v5/{tenant_id}/api/pipeline-templates/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPipelineTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_pipelines_async(self, request):
        """获取流水线列表/获取项目下流水线执行状况

        获取流水线列表/获取项目下流水线执行状况
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPipelines
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesResponse`
        """
        return self._list_pipelines_with_http_info(request)

    def _list_pipelines_with_http_info(self, request):
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
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v5/{project_id}/api/pipelines/list',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListPipelinesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_pipeline_async(self, request):
        """启动流水线

        启动流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RunPipeline
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineResponse`
        """
        return self._run_pipeline_with_http_info(request)

    def _run_pipeline_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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
            resource_path='/v5/{project_id}/api/pipelines/{pipeline_id}/run',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_pipeline_run_detail_async(self, request):
        """获取流水线状态/获取流水线执行详情

        获取流水线状态/获取流水线执行详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPipelineRunDetail
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineRunDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineRunDetailResponse`
        """
        return self._show_pipeline_run_detail_with_http_info(request)

    def _show_pipeline_run_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'pipeline_run_id' in local_var_params:
            query_params.append(('pipeline_run_id', local_var_params['pipeline_run_id']))

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
            resource_path='/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPipelineRunDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_pipeline_template_detail_async(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPipelineTemplateDetail
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ShowPipelineTemplateDetailResponse`
        """
        return self._show_pipeline_template_detail_with_http_info(request)

    def _show_pipeline_template_detail_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenant_id'] = local_var_params['tenant_id']
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
            resource_path='/v5/{tenant_id}/api/pipeline-templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowPipelineTemplateDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_pipeline_run_async(self, request):
        """停止流水线

        停止流水线
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopPipelineRun
        :type request: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineRunRequest`
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.StopPipelineRunResponse`
        """
        return self._stop_pipeline_run_with_http_info(request)

    def _stop_pipeline_run_with_http_info(self, request):
        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']
        if 'pipeline_run_id' in local_var_params:
            path_params['pipeline_run_id'] = local_var_params['pipeline_run_id']

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
            resource_path='/v5/{project_id}/api/pipelines/{pipeline_id}/pipeline-runs/{pipeline_run_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopPipelineRunResponse',
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

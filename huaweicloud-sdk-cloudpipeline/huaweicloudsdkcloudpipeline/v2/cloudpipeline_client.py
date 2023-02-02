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


class CloudPipelineClient(Client):
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
        super(CloudPipelineClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcloudpipeline.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CloudPipelineClient":
            raise TypeError("client type error, support client type is CloudPipelineClient")

        return ClientBuilder(clazz)

    def batch_show_pipelines_status(self, request):
        """批量获取流水线状态

        批量获取流水线状态和阶段信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowPipelinesStatus
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.BatchShowPipelinesStatusRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.BatchShowPipelinesStatusResponse`
        """
        return self.batch_show_pipelines_status_with_http_info(request)

    def batch_show_pipelines_status_with_http_info(self, request):
        all_params = ['pipeline_ids', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pipeline_ids' in local_var_params:
            query_params.append(('pipeline_ids', local_var_params['pipeline_ids']))

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

    def create_pipeline_by_template(self, request):
        """基于模板快速创建流水线及流水线内任务

        基于模板快速创建流水线及流水线内任务
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreatePipelineByTemplate
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.CreatePipelineByTemplateRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.CreatePipelineByTemplateResponse`
        """
        return self.create_pipeline_by_template_with_http_info(request)

    def create_pipeline_by_template_with_http_info(self, request):
        all_params = ['create_pipeline_by_template_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_pipeline_simple_info(self, request):
        """获取流水线列表接口

        获取流水线列表接口
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineSimpleInfo
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ListPipelineSimpleInfoRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ListPipelineSimpleInfoResponse`
        """
        return self.list_pipeline_simple_info_with_http_info(request)

    def list_pipeline_simple_info_with_http_info(self, request):
        all_params = ['x_language', 'list_pipeline_simple_info_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_pipleine_build_result(self, request):
        """获取项目下流水线执行状况

        获取项目下流水线执行状况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipleineBuildResult
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ListPipleineBuildResultRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ListPipleineBuildResultResponse`
        """
        return self.list_pipleine_build_result_with_http_info(request)

    def list_pipleine_build_result_with_http_info(self, request):
        all_params = ['project_id', 'start_date', 'end_date', 'offset', 'limit', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_templates(self, request):
        """查询模板列表

        查询模板列表，支持分页查询,支持模板名字模糊查询
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTemplates
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ListTemplatesRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ListTemplatesResponse`
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        all_params = ['template_type', 'is_build_in', 'x_language', 'offset', 'limit', 'name', 'sort', 'asc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def remove_pipeline(self, request):
        """删除流水线

        根据id删除流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RemovePipeline
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.RemovePipelineRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.RemovePipelineResponse`
        """
        return self.remove_pipeline_with_http_info(request)

    def remove_pipeline_with_http_info(self, request):
        all_params = ['pipeline_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def show_instance_status(self, request):
        """检查流水线创建状态

        检查流水线创建状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowInstanceStatus
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ShowInstanceStatusRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ShowInstanceStatusResponse`
        """
        return self.show_instance_status_with_http_info(request)

    def show_instance_status_with_http_info(self, request):
        all_params = ['task_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def show_pipleine_status(self, request):
        """获取流水线状态

        获取流水线状态,阶段及任务信息
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipleineStatus
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ShowPipleineStatusRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ShowPipleineStatusResponse`
        """
        return self.show_pipleine_status_with_http_info(request)

    def show_pipleine_status_with_http_info(self, request):
        all_params = ['pipeline_id', 'x_language', 'build_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))

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

    def show_template_detail(self, request):
        """查询模板详情

        查询模板详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowTemplateDetail
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ShowTemplateDetailRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ShowTemplateDetailResponse`
        """
        return self.show_template_detail_with_http_info(request)

    def show_template_detail_with_http_info(self, request):
        all_params = ['template_id', 'template_type', 'x_language', 'source']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def start_new_pipeline(self, request):
        """启动流水线

        启动流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartNewPipeline
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.StartNewPipelineRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.StartNewPipelineResponse`
        """
        return self.start_new_pipeline_with_http_info(request)

    def start_new_pipeline_with_http_info(self, request):
        all_params = ['pipeline_id', 'x_language', 'start_new_pipeline_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def stop_pipeline_new(self, request):
        """停止流水线

        停止流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopPipelineNew
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.StopPipelineNewRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.StopPipelineNewResponse`
        """
        return self.stop_pipeline_new_with_http_info(request)

    def stop_pipeline_new_with_http_info(self, request):
        all_params = ['pipeline_id', 'build_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'build_id' in local_var_params:
            query_params.append(('build_id', local_var_params['build_id']))

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

    def batch_show_pipelines_latest_status(self, request):
        """批量获取流水线状态

        批量获取流水线状态
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchShowPipelinesLatestStatus
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.BatchShowPipelinesLatestStatusRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.BatchShowPipelinesLatestStatusResponse`
        """
        return self.batch_show_pipelines_latest_status_with_http_info(request)

    def batch_show_pipelines_latest_status_with_http_info(self, request):
        all_params = ['project_id', 'pipeline_ids', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def delete_pipeline(self, request):
        """删除流水线

        删除流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeletePipeline
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.DeletePipelineRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.DeletePipelineResponse`
        """
        return self.delete_pipeline_with_http_info(request)

    def delete_pipeline_with_http_info(self, request):
        all_params = ['project_id', 'pipeline_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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

    def list_pipeline_runs(self, request):
        """获取流水线执行记录

        获取流水线执行记录
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelineRuns
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ListPipelineRunsRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ListPipelineRunsResponse`
        """
        return self.list_pipeline_runs_with_http_info(request)

    def list_pipeline_runs_with_http_info(self, request):
        all_params = ['project_id', 'pipeline_id', 'x_language', 'list_pipeline_runs_query']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def list_pipelines(self, request):
        """获取流水线列表/获取项目下流水线执行状况

        获取流水线列表/获取项目下流水线执行状况
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListPipelines
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ListPipelinesRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ListPipelinesResponse`
        """
        return self.list_pipelines_with_http_info(request)

    def list_pipelines_with_http_info(self, request):
        all_params = ['project_id', 'x_language', 'list_pipelines_query']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def run_pipeline(self, request):
        """启动流水线

        启动流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunPipeline
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.RunPipelineRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.RunPipelineResponse`
        """
        return self.run_pipeline_with_http_info(request)

    def run_pipeline_with_http_info(self, request):
        all_params = ['project_id', 'pipeline_id', 'x_language', 'run_pipeline_req']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'project_id' in local_var_params:
            path_params['project_id'] = local_var_params['project_id']
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

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

    def show_pipeline_run_detail(self, request):
        """获取流水线状态/获取流水线执行详情

        获取流水线状态/获取流水线执行详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowPipelineRunDetail
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.ShowPipelineRunDetailRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.ShowPipelineRunDetailResponse`
        """
        return self.show_pipeline_run_detail_with_http_info(request)

    def show_pipeline_run_detail_with_http_info(self, request):
        all_params = ['project_id', 'pipeline_id', 'pipeline_run_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

    def stop_pipeline_run(self, request):
        """停止流水线

        停止流水线
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopPipelineRun
        :type request: :class:`huaweicloudsdkcloudpipeline.v2.StopPipelineRunRequest`
        :rtype: :class:`huaweicloudsdkcloudpipeline.v2.StopPipelineRunResponse`
        """
        return self.stop_pipeline_run_with_http_info(request)

    def stop_pipeline_run_with_http_info(self, request):
        all_params = ['project_id', 'pipeline_id', 'pipeline_run_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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

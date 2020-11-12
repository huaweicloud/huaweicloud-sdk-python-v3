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
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

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

    @staticmethod
    def new_builder(clazz):
        return ClientBuilder(clazz)

    def batch_show_pipelines_status(self, request):
        """获取流水线状态

        批量获取流水线状态和阶段信息

        :param BatchShowPipelinesStatusRequest request
        :return: BatchShowPipelinesStatusResponse
        """
        return self.batch_show_pipelines_status_with_http_info(request)

    def batch_show_pipelines_status_with_http_info(self, request):
        """获取流水线状态

        批量获取流水线状态和阶段信息

        :param BatchShowPipelinesStatusRequest request
        :return: BatchShowPipelinesStatusResponse
        """

        all_params = ['pipeline_ids', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchShowPipelinesStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_pipeline_by_template(self, request):
        """基于模板快速创建流水线及流水线内任务

        基于模板快速创建流水线及流水线内任务

        :param CreatePipelineByTemplateRequest request
        :return: CreatePipelineByTemplateResponse
        """
        return self.create_pipeline_by_template_with_http_info(request)

    def create_pipeline_by_template_with_http_info(self, request):
        """基于模板快速创建流水线及流水线内任务

        基于模板快速创建流水线及流水线内任务

        :param CreatePipelineByTemplateRequest request
        :return: CreatePipelineByTemplateResponse
        """

        all_params = ['create_pipeline_by_template_request_body', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='CreatePipelineByTemplateResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_templates(self, request):
        """查询模板列表

        查询模板列表，支持分页查询,支持模板名字模糊查询

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """
        return self.list_templates_with_http_info(request)

    def list_templates_with_http_info(self, request):
        """查询模板列表

        查询模板列表，支持分页查询,支持模板名字模糊查询

        :param ListTemplatesRequest request
        :return: ListTemplatesResponse
        """

        all_params = ['template_type', 'is_build_in', 'x_language', 'offset', 'limit', 'name', 'sort', 'asc']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTemplatesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def register_agent(self, request):
        """register注册Slave接口

        注册创建Slave接口

        :param RegisterAgentRequest request
        :return: RegisterAgentResponse
        """
        return self.register_agent_with_http_info(request)

    def register_agent_with_http_info(self, request):
        """register注册Slave接口

        注册创建Slave接口

        :param RegisterAgentRequest request
        :return: RegisterAgentResponse
        """

        all_params = ['register_agent_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/agentregister/v1/agent/register',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RegisterAgentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def remove_pipeline(self, request):
        """删除流水线

        根据id删除流水线

        :param RemovePipelineRequest request
        :return: RemovePipelineResponse
        """
        return self.remove_pipeline_with_http_info(request)

    def remove_pipeline_with_http_info(self, request):
        """删除流水线

        根据id删除流水线

        :param RemovePipelineRequest request
        :return: RemovePipelineResponse
        """

        all_params = ['pipeline_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/{pipeline_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='RemovePipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_agent_status(self, request):
        """Agent状态查询

        Agent状态查询

        :param ShowAgentStatusRequest request
        :return: ShowAgentStatusResponse
        """
        return self.show_agent_status_with_http_info(request)

    def show_agent_status_with_http_info(self, request):
        """Agent状态查询

        Agent状态查询

        :param ShowAgentStatusRequest request
        :return: ShowAgentStatusResponse
        """

        all_params = ['agent_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'agent_id' in local_var_params:
            path_params['agent_id'] = local_var_params['agent_id']

        query_params = []

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v1/agents/{agent_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAgentStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_status(self, request):
        """检查流水线创建状态

        检查流水线创建状态

        :param ShowInstanceStatusRequest request
        :return: ShowInstanceStatusResponse
        """
        return self.show_instance_status_with_http_info(request)

    def show_instance_status_with_http_info(self, request):
        """检查流水线创建状态

        检查流水线创建状态

        :param ShowInstanceStatusRequest request
        :return: ShowInstanceStatusResponse
        """

        all_params = ['task_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates/{task_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_pipleine_status(self, request):
        """获取流水线状态

        获取流水线状态,阶段及任务信息

        :param ShowPipleineStatusRequest request
        :return: ShowPipleineStatusResponse
        """
        return self.show_pipleine_status_with_http_info(request)

    def show_pipleine_status_with_http_info(self, request):
        """获取流水线状态

        获取流水线状态,阶段及任务信息

        :param ShowPipleineStatusRequest request
        :return: ShowPipleineStatusResponse
        """

        all_params = ['pipeline_id', 'x_language', 'build_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/{pipeline_id}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPipleineStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_template_detail(self, request):
        """查询模板详情

        查询模板详情

        :param ShowTemplateDetailRequest request
        :return: ShowTemplateDetailResponse
        """
        return self.show_template_detail_with_http_info(request)

    def show_template_detail_with_http_info(self, request):
        """查询模板详情

        查询模板详情

        :param ShowTemplateDetailRequest request
        :return: ShowTemplateDetailResponse
        """

        all_params = ['template_id', 'template_type', 'x_language', 'source']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/templates/{template_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTemplateDetailResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_new_pipeline(self, request):
        """启动流水线

        启动流水线

        :param StartNewPipelineRequest request
        :return: StartNewPipelineResponse
        """
        return self.start_new_pipeline_with_http_info(request)

    def start_new_pipeline_with_http_info(self, request):
        """启动流水线

        启动流水线

        :param StartNewPipelineRequest request
        :return: StartNewPipelineResponse
        """

        all_params = ['pipeline_id', 'x_language', 'start_new_pipeline_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            response_type='StartNewPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_pipeline(self, request):
        """执行流水线

        执行流水线

        :param StartPipelineRequest request
        :return: StartPipelineResponse
        """
        return self.start_pipeline_with_http_info(request)

    def start_pipeline_with_http_info(self, request):
        """执行流水线

        执行流水线

        :param StartPipelineRequest request
        :return: StartPipelineResponse
        """

        all_params = ['pipeline_id', 'x_language']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pipeline_id' in local_var_params:
            query_params.append(('pipeline_id', local_var_params['pipeline_id']))

        header_params = {}
        if 'x_language' in local_var_params:
            header_params['X-Language'] = local_var_params['x_language']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_pipeline(self, request):
        """停止流水线

        停止流水线

        :param StopPipelineRequest request
        :return: StopPipelineResponse
        """
        return self.stop_pipeline_with_http_info(request)

    def stop_pipeline_with_http_info(self, request):
        """停止流水线

        停止流水线

        :param StopPipelineRequest request
        :return: StopPipelineResponse
        """

        all_params = ['pipeline_id', 'x_language', 'build_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pipeline_id' in local_var_params:
            query_params.append(('pipeline_id', local_var_params['pipeline_id']))
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


        auth_settings = ['apig-auth-iam']

        return self.call_api(
            resource_path='/v3/pipelines/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopPipelineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
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
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type)

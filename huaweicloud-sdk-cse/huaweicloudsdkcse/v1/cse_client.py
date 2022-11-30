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


class CseClient(Client):
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
        super(CseClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcse.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "CseClient":
            raise TypeError("client type error, support client type is CseClient")

        return ClientBuilder(clazz)

    def create_engine(self, request):
        """创建微服务引擎专享版

        创建微服务引擎专享版。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateEngine
        :type request: :class:`huaweicloudsdkcse.v1.CreateEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.CreateEngineResponse`
        """
        return self.create_engine_with_http_info(request)

    def create_engine_with_http_info(self, request):
        all_params = ['create_engine_request_body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v2/{project_id}/enginemgr/engines',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateEngineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_engine(self, request):
        """删除微服务引擎专享版

        删除微服务引擎专享版。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEngine
        :type request: :class:`huaweicloudsdkcse.v1.DeleteEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DeleteEngineResponse`
        """
        return self.delete_engine_with_http_info(request)

    def delete_engine_with_http_info(self, request):
        all_params = ['engine_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/enginemgr/engines/{engine_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteEngineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def download_kie(self, request):
        """导出kie配置

        导出kie配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DownloadKie
        :type request: :class:`huaweicloudsdkcse.v1.DownloadKieRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.DownloadKieResponse`
        """
        return self.download_kie_with_http_info(request)

    def download_kie_with_http_info(self, request):
        all_params = ['x_engine_id', 'download_kie_request_body', 'x_enterprise_project_id', 'label', 'match']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'match' in local_var_params:
            query_params.append(('match', local_var_params['match']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']

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
            resource_path='/v1/{project_id}/kie/download',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DownloadKieResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_engines(self, request):
        """查询微服务引擎列表

        查询微服务引擎列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListEngines
        :type request: :class:`huaweicloudsdkcse.v1.ListEnginesRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListEnginesResponse`
        """
        return self.list_engines_with_http_info(request)

    def list_engines_with_http_info(self, request):
        all_params = ['offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

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
            resource_path='/v2/{project_id}/enginemgr/engines',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListEnginesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_flavors(self, request):
        """查询微服务引擎专享版的规格列表

        查询微服务引擎专享版的规格列表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListFlavors
        :type request: :class:`huaweicloudsdkcse.v1.ListFlavorsRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ListFlavorsResponse`
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        all_params = ['spec_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'spec_type' in local_var_params:
            query_params.append(('spec_type', local_var_params['spec_type']))

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
            resource_path='/v2/{project_id}/enginemgr/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def retry_engine(self, request):
        """对微服务引擎专享版进行重试

        对微服务引擎专享版进行重试
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RetryEngine
        :type request: :class:`huaweicloudsdkcse.v1.RetryEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.RetryEngineResponse`
        """
        return self.retry_engine_with_http_info(request)

    def retry_engine_with_http_info(self, request):
        all_params = ['engine_id', 'retry_engine_request_body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v2/{project_id}/enginemgr/engines/{engine_id}/actions',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RetryEngineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_engine(self, request):
        """查询微服务引擎专享版详情

        查询微服务引擎专享版详情
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEngine
        :type request: :class:`huaweicloudsdkcse.v1.ShowEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowEngineResponse`
        """
        return self.show_engine_with_http_info(request)

    def show_engine_with_http_info(self, request):
        all_params = ['engine_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/enginemgr/engines/{engine_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEngineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_engine_job(self, request):
        """查询微服务引擎任务详情

        查询微服务引擎任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowEngineJob
        :type request: :class:`huaweicloudsdkcse.v1.ShowEngineJobRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.ShowEngineJobResponse`
        """
        return self.show_engine_job_with_http_info(request)

    def show_engine_job_with_http_info(self, request):
        all_params = ['engine_id', 'job_id', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/enginemgr/engines/{engine_id}/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowEngineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upgrade_engine(self, request):
        """升级微服务引擎专享版

        升级微服务引擎专享版
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpgradeEngine
        :type request: :class:`huaweicloudsdkcse.v1.UpgradeEngineRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UpgradeEngineResponse`
        """
        return self.upgrade_engine_with_http_info(request)

    def upgrade_engine_with_http_info(self, request):
        all_params = ['engine_id', 'upgrade_engine_request_body', 'x_enterprise_project_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'engine_id' in local_var_params:
            path_params['engine_id'] = local_var_params['engine_id']

        query_params = []

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']

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
            resource_path='/v2/{project_id}/enginemgr/engines/{engine_id}/upgrade',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpgradeEngineResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def upload_kie(self, request):
        """导入kie配置

        导入kie配置
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UploadKie
        :type request: :class:`huaweicloudsdkcse.v1.UploadKieRequest`
        :rtype: :class:`huaweicloudsdkcse.v1.UploadKieResponse`
        """
        return self.upload_kie_with_http_info(request)

    def upload_kie_with_http_info(self, request):
        all_params = ['x_engine_id', 'override', 'upload_file', 'x_enterprise_project_id', 'label']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'override' in local_var_params:
            query_params.append(('override', local_var_params['override']))
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))

        header_params = {}
        if 'x_enterprise_project_id' in local_var_params:
            header_params['X-Enterprise-Project-ID'] = local_var_params['x_enterprise_project_id']
        if 'x_engine_id' in local_var_params:
            header_params['x-engine-id'] = local_var_params['x_engine_id']

        form_params = {}
        if 'upload_file' in local_var_params:
            form_params['upload_file'] = local_var_params['upload_file']

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
            resource_path='/v1/{project_id}/kie/file',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UploadKieResponse',
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

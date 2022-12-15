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


class DlfClient(Client):
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
        super(DlfClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdlf.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "DlfClient":
            raise TypeError("client type error, support client type is DlfClient")

        return ClientBuilder(clazz)

    def cancel_script(self, request):
        """停止脚本实例的执行

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelScript
        :type request: :class:`huaweicloudsdkdlf.v1.CancelScriptRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.CancelScriptResponse`
        """
        return self.cancel_script_with_http_info(request)

    def cancel_script_with_http_info(self, request):
        all_params = ['script_name', 'instance_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_name' in local_var_params:
            path_params['script_name'] = local_var_params['script_name']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/scripts/{script_name}/instances/{instance_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CancelScriptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_connection(self, request):
        """创建连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnection
        :type request: :class:`huaweicloudsdkdlf.v1.CreateConnectionRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.CreateConnectionResponse`
        """
        return self.create_connection_with_http_info(request)

    def create_connection_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/connections',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_job(self, request):
        """创建作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateJob
        :type request: :class:`huaweicloudsdkdlf.v1.CreateJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.CreateJobResponse`
        """
        return self.create_job_with_http_info(request)

    def create_job_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_resource(self, request):
        """创建资源

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResource
        :type request: :class:`huaweicloudsdkdlf.v1.CreateResourceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.CreateResourceResponse`
        """
        return self.create_resource_with_http_info(request)

    def create_resource_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def create_script(self, request):
        """创建脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScript
        :type request: :class:`huaweicloudsdkdlf.v1.CreateScriptRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.CreateScriptResponse`
        """
        return self.create_script_with_http_info(request)

    def create_script_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/scripts',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='CreateScriptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_connction(self, request):
        """删除连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnction
        :type request: :class:`huaweicloudsdkdlf.v1.DeleteConnctionRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.DeleteConnctionResponse`
        """
        return self.delete_connction_with_http_info(request)

    def delete_connction_with_http_info(self, request):
        all_params = ['connection_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_name' in local_var_params:
            path_params['connection_name'] = local_var_params['connection_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/connections/{connection_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteConnctionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_job(self, request):
        """删除作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkdlf.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.DeleteJobResponse`
        """
        return self.delete_job_with_http_info(request)

    def delete_job_with_http_info(self, request):
        all_params = ['job_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}',
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

    def delete_resource(self, request):
        """删除资源

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdkdlf.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.DeleteResourceResponse`
        """
        return self.delete_resource_with_http_info(request)

    def delete_resource_with_http_info(self, request):
        all_params = ['resource_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/resources/{resource_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def delete_script(self, request):
        """删除脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScript
        :type request: :class:`huaweicloudsdkdlf.v1.DeleteScriptRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.DeleteScriptResponse`
        """
        return self.delete_script_with_http_info(request)

    def delete_script_with_http_info(self, request):
        all_params = ['script_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_name' in local_var_params:
            path_params['script_name'] = local_var_params['script_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/scripts/{script_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='DeleteScriptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def execute_script(self, request):
        """执行脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteScript
        :type request: :class:`huaweicloudsdkdlf.v1.ExecuteScriptRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ExecuteScriptResponse`
        """
        return self.execute_script_with_http_info(request)

    def execute_script_with_http_info(self, request):
        all_params = ['script_name', 'body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_name' in local_var_params:
            path_params['script_name'] = local_var_params['script_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/scripts/{script_name}/execute',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExecuteScriptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_connections(self, request):
        """导出连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportConnections
        :type request: :class:`huaweicloudsdkdlf.v1.ExportConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ExportConnectionsResponse`
        """
        return self.export_connections_with_http_info(request)

    def export_connections_with_http_info(self, request):
        all_params = ['workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/connections/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_job(self, request):
        """导出作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportJob
        :type request: :class:`huaweicloudsdkdlf.v1.ExportJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ExportJobResponse`
        """
        return self.export_job_with_http_info(request)

    def export_job_with_http_info(self, request):
        all_params = ['job_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}/export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def export_job_list(self, request):
        """批量导出作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportJobList
        :type request: :class:`huaweicloudsdkdlf.v1.ExportJobListRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ExportJobListResponse`
        """
        return self.export_job_list_with_http_info(request)

    def export_job_list_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs/batch-export',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ExportJobListResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_connections(self, request):
        """导入连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportConnections
        :type request: :class:`huaweicloudsdkdlf.v1.ImportConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ImportConnectionsResponse`
        """
        return self.import_connections_with_http_info(request)

    def import_connections_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/connections/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def import_job(self, request):
        """导入作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportJob
        :type request: :class:`huaweicloudsdkdlf.v1.ImportJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ImportJobResponse`
        """
        return self.import_job_with_http_info(request)

    def import_job_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs/import',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ImportJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_connections(self, request):
        """查询连接列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnections
        :type request: :class:`huaweicloudsdkdlf.v1.ListConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListConnectionsResponse`
        """
        return self.list_connections_with_http_info(request)

    def list_connections_with_http_info(self, request):
        all_params = ['workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/connections',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListConnectionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_job_instances(self, request):
        """查询作业实例列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobInstances
        :type request: :class:`huaweicloudsdkdlf.v1.ListJobInstancesRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListJobInstancesResponse`
        """
        return self.list_job_instances_with_http_info(request)

    def list_job_instances_with_http_info(self, request):
        all_params = ['workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/instances/detail',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_jobs(self, request):
        """查询作业列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkdlf.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListJobsResponse`
        """
        return self.list_jobs_with_http_info(request)

    def list_jobs_with_http_info(self, request):
        all_params = ['workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_resources(self, request):
        """查询资源列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkdlf.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListResourcesResponse`
        """
        return self.list_resources_with_http_info(request)

    def list_resources_with_http_info(self, request):
        all_params = ['workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_script_results(self, request):
        """查询脚本实例执行结果

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptResults
        :type request: :class:`huaweicloudsdkdlf.v1.ListScriptResultsRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListScriptResultsResponse`
        """
        return self.list_script_results_with_http_info(request)

    def list_script_results_with_http_info(self, request):
        all_params = ['script_name', 'instance_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_name' in local_var_params:
            path_params['script_name'] = local_var_params['script_name']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/scripts/{script_name}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListScriptResultsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_scripts(self, request):
        """查询脚本列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScripts
        :type request: :class:`huaweicloudsdkdlf.v1.ListScriptsRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListScriptsResponse`
        """
        return self.list_scripts_with_http_info(request)

    def list_scripts_with_http_info(self, request):
        all_params = ['workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/scripts',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListScriptsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def list_system_tasks(self, request):
        """查询系统任务详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSystemTasks
        :type request: :class:`huaweicloudsdkdlf.v1.ListSystemTasksRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ListSystemTasksResponse`
        """
        return self.list_system_tasks_with_http_info(request)

    def list_system_tasks_with_http_info(self, request):
        all_params = ['task_id', 'workspace']
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
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/system-tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ListSystemTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def restore_job_instance(self, request):
        """重跑作业实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreJobInstance
        :type request: :class:`huaweicloudsdkdlf.v1.RestoreJobInstanceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.RestoreJobInstanceResponse`
        """
        return self.restore_job_instance_with_http_info(request)

    def restore_job_instance_with_http_info(self, request):
        all_params = ['job_name', 'instance_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}/instances/{instance_id}/restart',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RestoreJobInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def run_once(self, request):
        """单次执行作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunOnce
        :type request: :class:`huaweicloudsdkdlf.v1.RunOnceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.RunOnceResponse`
        """
        return self.run_once_with_http_info(request)

    def run_once_with_http_info(self, request):
        all_params = ['job_name', 'workspace', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs/{job_name}/run-immediate',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='RunOnceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_connection(self, request):
        """查询连接详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnection
        :type request: :class:`huaweicloudsdkdlf.v1.ShowConnectionRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowConnectionResponse`
        """
        return self.show_connection_with_http_info(request)

    def show_connection_with_http_info(self, request):
        all_params = ['connection_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_name' in local_var_params:
            path_params['connection_name'] = local_var_params['connection_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/connections/{connection_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_directory_tree(self, request):
        """查询目录树

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowDirectoryTree
        :type request: :class:`huaweicloudsdkdlf.v1.ShowDirectoryTreeRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowDirectoryTreeResponse`
        """
        return self.show_directory_tree_with_http_info(request)

    def show_directory_tree_with_http_info(self, request):
        all_params = ['workspace', 'category', 'directory_id', 'name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'category' in local_var_params:
            query_params.append(('category', local_var_params['category']))
        if 'directory_id' in local_var_params:
            query_params.append(('directory_id', local_var_params['directory_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1.0/{project_id}/directory/tree',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowDirectoryTreeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_file_info(self, request):
        """检查导入作业文件中的作业和脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFileInfo
        :type request: :class:`huaweicloudsdkdlf.v1.ShowFileInfoRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowFileInfoResponse`
        """
        return self.show_file_info_with_http_info(request)

    def show_file_info_with_http_info(self, request):
        all_params = ['body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs/check-file',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowFileInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job(self, request):
        """查询作业详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkdlf.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowJobResponse`
        """
        return self.show_job_with_http_info(request)

    def show_job_with_http_info(self, request):
        all_params = ['job_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}',
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

    def show_job_instance(self, request):
        """查询作业实例详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobInstance
        :type request: :class:`huaweicloudsdkdlf.v1.ShowJobInstanceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowJobInstanceResponse`
        """
        return self.show_job_instance_with_http_info(request)

    def show_job_instance_with_http_info(self, request):
        all_params = ['job_name', 'instance_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}/instances/{instance_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_job_status(self, request):
        """查询实时作业的运行状态

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobStatus
        :type request: :class:`huaweicloudsdkdlf.v1.ShowJobStatusRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowJobStatusResponse`
        """
        return self.show_job_status_with_http_info(request)

    def show_job_status_with_http_info(self, request):
        all_params = ['job_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}/status',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowJobStatusResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_resource(self, request):
        """查询资源详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResource
        :type request: :class:`huaweicloudsdkdlf.v1.ShowResourceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowResourceResponse`
        """
        return self.show_resource_with_http_info(request)

    def show_resource_with_http_info(self, request):
        all_params = ['resource_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/resources/{resource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def show_script(self, request):
        """查询脚本信息

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScript
        :type request: :class:`huaweicloudsdkdlf.v1.ShowScriptRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.ShowScriptResponse`
        """
        return self.show_script_with_http_info(request)

    def show_script_with_http_info(self, request):
        all_params = ['script_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_name' in local_var_params:
            path_params['script_name'] = local_var_params['script_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/scripts/{script_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='ShowScriptResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def start_job(self, request):
        """启动作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartJob
        :type request: :class:`huaweicloudsdkdlf.v1.StartJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.StartJobResponse`
        """
        return self.start_job_with_http_info(request)

    def start_job_with_http_info(self, request):
        all_params = ['job_name', 'workspace', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs/{job_name}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StartJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_job(self, request):
        """停止作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkdlf.v1.StopJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.StopJobResponse`
        """
        return self.stop_job_with_http_info(request)

    def stop_job_with_http_info(self, request):
        all_params = ['job_name', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def stop_job_instance(self, request):
        """停止作业实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJobInstance
        :type request: :class:`huaweicloudsdkdlf.v1.StopJobInstanceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.StopJobInstanceResponse`
        """
        return self.stop_job_instance_with_http_info(request)

    def stop_job_instance_with_http_info(self, request):
        all_params = ['job_name', 'instance_id', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/{project_id}/jobs/{job_name}/instances/{instance_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='StopJobInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_connection(self, request):
        """修改连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConnection
        :type request: :class:`huaweicloudsdkdlf.v1.UpdateConnectionRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.UpdateConnectionResponse`
        """
        return self.update_connection_with_http_info(request)

    def update_connection_with_http_info(self, request):
        all_params = ['connection_name', 'body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_name' in local_var_params:
            path_params['connection_name'] = local_var_params['connection_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/connections/{connection_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateConnectionResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_job(self, request):
        """修改作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkdlf.v1.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.UpdateJobResponse`
        """
        return self.update_job_with_http_info(request)

    def update_job_with_http_info(self, request):
        all_params = ['job_name', 'body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/jobs/{job_name}',
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

    def update_resource(self, request):
        """修改资源

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResource
        :type request: :class:`huaweicloudsdkdlf.v1.UpdateResourceRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.UpdateResourceResponse`
        """
        return self.update_resource_with_http_info(request)

    def update_resource_with_http_info(self, request):
        all_params = ['resource_id', 'workspace', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/resources/{resource_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)

    def update_script(self, request):
        """修改脚本内容

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScript
        :type request: :class:`huaweicloudsdkdlf.v1.UpdateScriptRequest`
        :rtype: :class:`huaweicloudsdkdlf.v1.UpdateScriptResponse`
        """
        return self.update_script_with_http_info(request)

    def update_script_with_http_info(self, request):
        all_params = ['script_name', 'body', 'workspace']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        cname = None

        collection_formats = {}

        path_params = {}
        if 'script_name' in local_var_params:
            path_params['script_name'] = local_var_params['script_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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
            resource_path='/v1/{project_id}/scripts/{script_name}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            cname=cname,
            response_type='UpdateScriptResponse',
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

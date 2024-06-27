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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdgc'")


class DgcClient(Client):
    def __init__(self):
        super(DgcClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdgc.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DgcClient":
                raise TypeError("client type error, support client type is DgcClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def cancel_script(self, request):
        """停止脚本实例的执行

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CancelScript
        :type request: :class:`huaweicloudsdkdgc.v1.CancelScriptRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.CancelScriptResponse`
        """
        http_info = self._cancel_script_http_info(request)
        return self._call_api(**http_info)

    def cancel_script_invoker(self, request):
        http_info = self._cancel_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _cancel_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/scripts/{script_name}/instances/{instance_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "CancelScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def create_connection(self, request):
        """创建连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateConnection
        :type request: :class:`huaweicloudsdkdgc.v1.CreateConnectionRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.CreateConnectionResponse`
        """
        http_info = self._create_connection_http_info(request)
        return self._call_api(**http_info)

    def create_connection_invoker(self, request):
        http_info = self._create_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_connection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "CreateConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_job(self, request):
        """创建作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateJob
        :type request: :class:`huaweicloudsdkdgc.v1.CreateJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.CreateJobResponse`
        """
        http_info = self._create_job_http_info(request)
        return self._call_api(**http_info)

    def create_job_invoker(self, request):
        http_info = self._create_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_resource(self, request):
        """创建资源

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateResource
        :type request: :class:`huaweicloudsdkdgc.v1.CreateResourceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.CreateResourceResponse`
        """
        http_info = self._create_resource_http_info(request)
        return self._call_api(**http_info)

    def create_resource_invoker(self, request):
        http_info = self._create_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_resource_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_script(self, request):
        """创建脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateScript
        :type request: :class:`huaweicloudsdkdgc.v1.CreateScriptRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.CreateScriptResponse`
        """
        http_info = self._create_script_http_info(request)
        return self._call_api(**http_info)

    def create_script_invoker(self, request):
        http_info = self._create_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "CreateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def create_supplementdata(self, request):
        """创建补数据实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateSupplementdata
        :type request: :class:`huaweicloudsdkdgc.v1.CreateSupplementdataRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.CreateSupplementdataResponse`
        """
        http_info = self._create_supplementdata_http_info(request)
        return self._call_api(**http_info)

    def create_supplementdata_invoker(self, request):
        http_info = self._create_supplementdata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_supplementdata_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/supplementdata",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSupplementdataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def delete_connction(self, request):
        """删除连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteConnction
        :type request: :class:`huaweicloudsdkdgc.v1.DeleteConnctionRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.DeleteConnctionResponse`
        """
        http_info = self._delete_connction_http_info(request)
        return self._call_api(**http_info)

    def delete_connction_invoker(self, request):
        http_info = self._delete_connction_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_connction_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/connections/{connection_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnctionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_job(self, request):
        """删除作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteJob
        :type request: :class:`huaweicloudsdkdgc.v1.DeleteJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.DeleteJobResponse`
        """
        http_info = self._delete_job_http_info(request)
        return self._call_api(**http_info)

    def delete_job_invoker(self, request):
        http_info = self._delete_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_job_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/jobs/{job_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_resource(self, request):
        """删除资源

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteResource
        :type request: :class:`huaweicloudsdkdgc.v1.DeleteResourceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.DeleteResourceResponse`
        """
        http_info = self._delete_resource_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_invoker(self, request):
        http_info = self._delete_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_resource_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def delete_script(self, request):
        """删除脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteScript
        :type request: :class:`huaweicloudsdkdgc.v1.DeleteScriptRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.DeleteScriptResponse`
        """
        http_info = self._delete_script_http_info(request)
        return self._call_api(**http_info)

    def delete_script_invoker(self, request):
        http_info = self._delete_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_script_http_info(cls, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/scripts/{script_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def execute_script(self, request):
        """执行脚本

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExecuteScript
        :type request: :class:`huaweicloudsdkdgc.v1.ExecuteScriptRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ExecuteScriptResponse`
        """
        http_info = self._execute_script_http_info(request)
        return self._call_api(**http_info)

    def execute_script_invoker(self, request):
        http_info = self._execute_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _execute_script_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/scripts/{script_name}/execute",
            "request_type": request.__class__.__name__,
            "response_type": "ExecuteScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def export_connections(self, request):
        """导出连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportConnections
        :type request: :class:`huaweicloudsdkdgc.v1.ExportConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ExportConnectionsResponse`
        """
        http_info = self._export_connections_http_info(request)
        return self._call_api(**http_info)

    def export_connections_invoker(self, request):
        http_info = self._export_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_connections_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/connections/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def export_job(self, request):
        """导出作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportJob
        :type request: :class:`huaweicloudsdkdgc.v1.ExportJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ExportJobResponse`
        """
        http_info = self._export_job_http_info(request)
        return self._call_api(**http_info)

    def export_job_invoker(self, request):
        http_info = self._export_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def export_job_list(self, request):
        """批量导出作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ExportJobList
        :type request: :class:`huaweicloudsdkdgc.v1.ExportJobListRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ExportJobListResponse`
        """
        http_info = self._export_job_list_http_info(request)
        return self._call_api(**http_info)

    def export_job_list_invoker(self, request):
        http_info = self._export_job_list_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _export_job_list_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/batch-export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportJobListResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def import_connections(self, request):
        """导入连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportConnections
        :type request: :class:`huaweicloudsdkdgc.v1.ImportConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ImportConnectionsResponse`
        """
        http_info = self._import_connections_http_info(request)
        return self._call_api(**http_info)

    def import_connections_invoker(self, request):
        http_info = self._import_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_connections_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/connections/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportConnectionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def import_job(self, request):
        """导入作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ImportJob
        :type request: :class:`huaweicloudsdkdgc.v1.ImportJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ImportJobResponse`
        """
        http_info = self._import_job_http_info(request)
        return self._call_api(**http_info)

    def import_job_invoker(self, request):
        http_info = self._import_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _import_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_connections(self, request):
        """查询连接列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListConnections
        :type request: :class:`huaweicloudsdkdgc.v1.ListConnectionsRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListConnectionsResponse`
        """
        http_info = self._list_connections_http_info(request)
        return self._call_api(**http_info)

    def list_connections_invoker(self, request):
        http_info = self._list_connections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_connections_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/connections",
            "request_type": request.__class__.__name__,
            "response_type": "ListConnectionsResponse"
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
        if 'connection_name' in local_var_params:
            query_params.append(('connectionName', local_var_params['connection_name']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_job_instances(self, request):
        """查询作业实例列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobInstances
        :type request: :class:`huaweicloudsdkdgc.v1.ListJobInstancesRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListJobInstancesResponse`
        """
        http_info = self._list_job_instances_http_info(request)
        return self._call_api(**http_info)

    def list_job_instances_invoker(self, request):
        http_info = self._list_job_instances_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_job_instances_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/instances/detail",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobInstancesResponse"
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
        if 'min_plan_time' in local_var_params:
            query_params.append(('minPlanTime', local_var_params['min_plan_time']))
        if 'max_plan_time' in local_var_params:
            query_params.append(('maxPlanTime', local_var_params['max_plan_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'precise_query' in local_var_params:
            query_params.append(('preciseQuery', local_var_params['precise_query']))
        if 'job_name' in local_var_params:
            query_params.append(('jobName', local_var_params['job_name']))
        if 'instance_type' in local_var_params:
            query_params.append(('instanceType', local_var_params['instance_type']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_jobs(self, request):
        """查询作业列表

        查询作业列表清单
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkdgc.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
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
        if 'job_type' in local_var_params:
            query_params.append(('jobType', local_var_params['job_type']))
        if 'job_name' in local_var_params:
            query_params.append(('jobName', local_var_params['job_name']))
        if 'tags' in local_var_params:
            query_params.append(('tags', local_var_params['tags']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_resources(self, request):
        """查询资源列表


        :param request: Request instance for ListResources
        :type request: :class:`huaweicloudsdkdgc.v1.ListResourcesRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListResourcesResponse`
        """
        http_info = self._list_resources_http_info(request)
        return self._call_api(**http_info)

    def list_resources_invoker(self, request):
        http_info = self._list_resources_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_resources_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesResponse"
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
        if 'resource_name' in local_var_params:
            query_params.append(('resourceName', local_var_params['resource_name']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_script_results(self, request):
        """查询脚本实例执行结果

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScriptResults
        :type request: :class:`huaweicloudsdkdgc.v1.ListScriptResultsRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListScriptResultsResponse`
        """
        http_info = self._list_script_results_http_info(request)
        return self._call_api(**http_info)

    def list_script_results_invoker(self, request):
        http_info = self._list_script_results_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_script_results_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/scripts/{script_name}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptResultsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_scripts(self, request):
        """查询脚本列表

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListScripts
        :type request: :class:`huaweicloudsdkdgc.v1.ListScriptsRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListScriptsResponse`
        """
        http_info = self._list_scripts_http_info(request)
        return self._call_api(**http_info)

    def list_scripts_invoker(self, request):
        http_info = self._list_scripts_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_scripts_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/scripts",
            "request_type": request.__class__.__name__,
            "response_type": "ListScriptsResponse"
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
        if 'script_name' in local_var_params:
            query_params.append(('scriptName', local_var_params['script_name']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_supplementdata(self, request):
        """查询补数据实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSupplementdata
        :type request: :class:`huaweicloudsdkdgc.v1.ListSupplementdataRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListSupplementdataResponse`
        """
        http_info = self._list_supplementdata_http_info(request)
        return self._call_api(**http_info)

    def list_supplementdata_invoker(self, request):
        http_info = self._list_supplementdata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_supplementdata_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/supplementdata",
            "request_type": request.__class__.__name__,
            "response_type": "ListSupplementdataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))
        if 'size' in local_var_params:
            query_params.append(('size', local_var_params['size']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'user_name' in local_var_params:
            query_params.append(('userName', local_var_params['user_name']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def list_system_tasks(self, request):
        """查询系统任务详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListSystemTasks
        :type request: :class:`huaweicloudsdkdgc.v1.ListSystemTasksRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ListSystemTasksResponse`
        """
        http_info = self._list_system_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_system_tasks_invoker(self, request):
        http_info = self._list_system_tasks_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_system_tasks_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/system-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListSystemTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def restore_job_instance(self, request):
        """重跑作业实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RestoreJobInstance
        :type request: :class:`huaweicloudsdkdgc.v1.RestoreJobInstanceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.RestoreJobInstanceResponse`
        """
        http_info = self._restore_job_instance_http_info(request)
        return self._call_api(**http_info)

    def restore_job_instance_invoker(self, request):
        http_info = self._restore_job_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _restore_job_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/instances/{instance_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestoreJobInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def run_once(self, request):
        """立即执行作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for RunOnce
        :type request: :class:`huaweicloudsdkdgc.v1.RunOnceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.RunOnceResponse`
        """
        http_info = self._run_once_http_info(request)
        return self._call_api(**http_info)

    def run_once_invoker(self, request):
        http_info = self._run_once_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _run_once_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/run-immediate",
            "request_type": request.__class__.__name__,
            "response_type": "RunOnceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_connection(self, request):
        """查询连接详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowConnection
        :type request: :class:`huaweicloudsdkdgc.v1.ShowConnectionRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowConnectionResponse`
        """
        http_info = self._show_connection_http_info(request)
        return self._call_api(**http_info)

    def show_connection_invoker(self, request):
        http_info = self._show_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_connection_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/connections/{connection_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_file_info(self, request):
        """查询作业文件

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowFileInfo
        :type request: :class:`huaweicloudsdkdgc.v1.ShowFileInfoRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowFileInfoResponse`
        """
        http_info = self._show_file_info_http_info(request)
        return self._call_api(**http_info)

    def show_file_info_invoker(self, request):
        http_info = self._show_file_info_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_file_info_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/check-file",
            "request_type": request.__class__.__name__,
            "response_type": "ShowFileInfoResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_job(self, request):
        """查询作业详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkdgc.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'job_name' in local_var_params:
            path_params['job_name'] = local_var_params['job_name']

        query_params = []
        if 'version' in local_var_params:
            query_params.append(('version', local_var_params['version']))

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def show_job_instance(self, request):
        """查询作业实例详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobInstance
        :type request: :class:`huaweicloudsdkdgc.v1.ShowJobInstanceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowJobInstanceResponse`
        """
        http_info = self._show_job_instance_http_info(request)
        return self._call_api(**http_info)

    def show_job_instance_invoker(self, request):
        http_info = self._show_job_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_instance_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/instances/{instance_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_job_status(self, request):
        """查询实时作业的运行状态

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowJobStatus
        :type request: :class:`huaweicloudsdkdgc.v1.ShowJobStatusRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowJobStatusResponse`
        """
        http_info = self._show_job_status_http_info(request)
        return self._call_api(**http_info)

    def show_job_status_invoker(self, request):
        http_info = self._show_job_status_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_job_status_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobStatusResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_resource(self, request):
        """查询资源详情

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowResource
        :type request: :class:`huaweicloudsdkdgc.v1.ShowResourceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowResourceResponse`
        """
        http_info = self._show_resource_http_info(request)
        return self._call_api(**http_info)

    def show_resource_invoker(self, request):
        http_info = self._show_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_resource_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def show_script(self, request):
        """查询脚本信息

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ShowScript
        :type request: :class:`huaweicloudsdkdgc.v1.ShowScriptRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.ShowScriptResponse`
        """
        http_info = self._show_script_http_info(request)
        return self._call_api(**http_info)

    def show_script_invoker(self, request):
        http_info = self._show_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _show_script_http_info(cls, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/scripts/{script_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def start_job(self, request):
        """启动作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StartJob
        :type request: :class:`huaweicloudsdkdgc.v1.StartJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.StartJobResponse`
        """
        http_info = self._start_job_http_info(request)
        return self._call_api(**http_info)

    def start_job_invoker(self, request):
        http_info = self._start_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _start_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def stop_job(self, request):
        """停止作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJob
        :type request: :class:`huaweicloudsdkdgc.v1.StopJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.StopJobResponse`
        """
        http_info = self._stop_job_http_info(request)
        return self._call_api(**http_info)

    def stop_job_invoker(self, request):
        http_info = self._stop_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def stop_job_instance(self, request):
        """停止作业实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopJobInstance
        :type request: :class:`huaweicloudsdkdgc.v1.StopJobInstanceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.StopJobInstanceResponse`
        """
        http_info = self._stop_job_instance_http_info(request)
        return self._call_api(**http_info)

    def stop_job_instance_invoker(self, request):
        http_info = self._stop_job_instance_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_job_instance_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/jobs/{job_name}/instances/{instance_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopJobInstanceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def stop_supplementdata(self, request):
        """停止补数据实例

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for StopSupplementdata
        :type request: :class:`huaweicloudsdkdgc.v1.StopSupplementdataRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.StopSupplementdataResponse`
        """
        http_info = self._stop_supplementdata_http_info(request)
        return self._call_api(**http_info)

    def stop_supplementdata_invoker(self, request):
        http_info = self._stop_supplementdata_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _stop_supplementdata_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1.0/{project_id}/supplementdata/{instanceName}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopSupplementdataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'instance_name' in local_var_params:
            path_params['instanceName'] = local_var_params['instance_name']

        query_params = []

        header_params = {}
        if 'workspace' in local_var_params:
            header_params['workspace'] = local_var_params['workspace']

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

    def update_connection(self, request):
        """修改连接

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateConnection
        :type request: :class:`huaweicloudsdkdgc.v1.UpdateConnectionRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.UpdateConnectionResponse`
        """
        http_info = self._update_connection_http_info(request)
        return self._call_api(**http_info)

    def update_connection_invoker(self, request):
        http_info = self._update_connection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_connection_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/connections/{connection_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_job(self, request):
        """修改作业

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateJob
        :type request: :class:`huaweicloudsdkdgc.v1.UpdateJobRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.UpdateJobResponse`
        """
        http_info = self._update_job_http_info(request)
        return self._call_api(**http_info)

    def update_job_invoker(self, request):
        http_info = self._update_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_job_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/jobs/{job_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_resource(self, request):
        """修改资源

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateResource
        :type request: :class:`huaweicloudsdkdgc.v1.UpdateResourceRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.UpdateResourceResponse`
        """
        http_info = self._update_resource_http_info(request)
        return self._call_api(**http_info)

    def update_resource_invoker(self, request):
        http_info = self._update_resource_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_resource_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/resources/{resource_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateResourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def update_script(self, request):
        """修改脚本内容

        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateScript
        :type request: :class:`huaweicloudsdkdgc.v1.UpdateScriptRequest`
        :rtype: :class:`huaweicloudsdkdgc.v1.UpdateScriptResponse`
        """
        http_info = self._update_script_http_info(request)
        return self._call_api(**http_info)

    def update_script_invoker(self, request):
        http_info = self._update_script_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_script_http_info(cls, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/scripts/{script_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateScriptResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

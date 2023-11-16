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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkges'")


class GesAsyncClient(Client):
    def __init__(self):
        super(GesAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkges.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GesAsyncClient":
                raise TypeError("client type error, support client type is GesAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def attach_eip_async(self, request):
        """绑定EIP(1.0.6)

        可以通过绑定弹性公网IP（简称EIP）访问GES服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachEip
        :type request: :class:`huaweicloudsdkges.v1.AttachEipRequest`
        :rtype: :class:`huaweicloudsdkges.v1.AttachEipResponse`
        """
        http_info = self._attach_eip_http_info(request)
        return self._call_api(**http_info)

    def attach_eip_async_invoker(self, request):
        http_info = self._attach_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "AttachEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def clear_graph_async(self, request):
        """清空图(2.1.2)

        清空图中所有数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ClearGraph
        :type request: :class:`huaweicloudsdkges.v1.ClearGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ClearGraphResponse`
        """
        http_info = self._clear_graph_http_info(request)
        return self._call_api(**http_info)

    def clear_graph_async_invoker(self, request):
        http_info = self._clear_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _clear_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ClearGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))
        if 'clear_metadata' in local_var_params:
            query_params.append(('clear-metadata', local_var_params['clear_metadata']))

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

    def create_backup_async(self, request):
        """新增备份(1.0.0)

        新增备份。当前图数据出现错误或故障时，可以启动备份图进行恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBackup
        :type request: :class:`huaweicloudsdkges.v1.CreateBackupRequest`
        :rtype: :class:`huaweicloudsdkges.v1.CreateBackupResponse`
        """
        http_info = self._create_backup_http_info(request)
        return self._call_api(**http_info)

    def create_backup_async_invoker(self, request):
        http_info = self._create_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_backup_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def create_graph_async(self, request):
        """创建图(2.2.2)

        创建一个图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGraph
        :type request: :class:`huaweicloudsdkges.v1.CreateGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.CreateGraphResponse`
        """
        http_info = self._create_graph_http_info(request)
        return self._call_api(**http_info)

    def create_graph_async_invoker(self, request):
        http_info = self._create_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGraphResponse"
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

    def create_metadata_async(self, request):
        """新增元数据(2.1.18)

        新增元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMetadata
        :type request: :class:`huaweicloudsdkges.v1.CreateMetadataRequest`
        :rtype: :class:`huaweicloudsdkges.v1.CreateMetadataResponse`
        """
        http_info = self._create_metadata_http_info(request)
        return self._call_api(**http_info)

    def create_metadata_async_invoker(self, request):
        http_info = self._create_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_metadata_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/metadatas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMetadataResponse"
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

    def delete_backup_async(self, request):
        """删除备份(1.0.0)

        删除备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackup
        :type request: :class:`huaweicloudsdkges.v1.DeleteBackupRequest`
        :rtype: :class:`huaweicloudsdkges.v1.DeleteBackupResponse`
        """
        http_info = self._delete_backup_http_info(request)
        return self._call_api(**http_info)

    def delete_backup_async_invoker(self, request):
        http_info = self._delete_backup_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backup_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackupResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def delete_graph_async(self, request):
        """删除图(1.0.0)

        删除一个图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGraph
        :type request: :class:`huaweicloudsdkges.v1.DeleteGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.DeleteGraphResponse`
        """
        http_info = self._delete_graph_http_info(request)
        return self._call_api(**http_info)

    def delete_graph_async_invoker(self, request):
        http_info = self._delete_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_graph_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'keep_backup' in local_var_params:
            query_params.append(('keepBackup', local_var_params['keep_backup']))

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

    def delete_metadata_async(self, request):
        """删除元数据(1.0.2)

        删除元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMetadata
        :type request: :class:`huaweicloudsdkges.v1.DeleteMetadataRequest`
        :rtype: :class:`huaweicloudsdkges.v1.DeleteMetadataResponse`
        """
        http_info = self._delete_metadata_http_info(request)
        return self._call_api(**http_info)

    def delete_metadata_async_invoker(self, request):
        http_info = self._delete_metadata_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_metadata_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1.0/{project_id}/graphs/metadatas/{metadata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMetadataResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'metadata_id' in local_var_params:
            path_params['metadata_id'] = local_var_params['metadata_id']

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

    def detach_eip_async(self, request):
        """解绑EIP(1.0.6)

        当无需继续使用EIP时，您可通过解绑EIP来释放网络资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachEip
        :type request: :class:`huaweicloudsdkges.v1.DetachEipRequest`
        :rtype: :class:`huaweicloudsdkges.v1.DetachEipResponse`
        """
        http_info = self._detach_eip_http_info(request)
        return self._call_api(**http_info)

    def detach_eip_async_invoker(self, request):
        http_info = self._detach_eip_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_eip_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "DetachEipResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def expand_graph_async(self, request):
        """扩副本(2.2.23)

        扩副本能力允许动态扩容多个从节点，扩容的从节点可以处理读请求，从而提高读请求性能。
        &gt;一万边和百亿边规格的图暂不支持扩副本。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandGraph
        :type request: :class:`huaweicloudsdkges.v1.ExpandGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ExpandGraphResponse`
        """
        http_info = self._expand_graph_http_info(request)
        return self._call_api(**http_info)

    def expand_graph_async_invoker(self, request):
        http_info = self._expand_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def export_graph_async(self, request):
        """导出图(1.0.5)

        导出图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportGraph
        :type request: :class:`huaweicloudsdkges.v1.ExportGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ExportGraphResponse`
        """
        http_info = self._export_graph_http_info(request)
        return self._call_api(**http_info)

    def export_graph_async_invoker(self, request):
        http_info = self._export_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ExportGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def import_graph_async(self, request):
        """增量导入图(2.1.14)

        增量导入图数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportGraph
        :type request: :class:`huaweicloudsdkges.v1.ImportGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ImportGraphResponse`
        """
        http_info = self._import_graph_http_info(request)
        return self._call_api(**http_info)

    def import_graph_async_invoker(self, request):
        http_info = self._import_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "ImportGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def list_backups_async(self, request):
        """查看所有备份列表(1.0.0)

        查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackups
        :type request: :class:`huaweicloudsdkges.v1.ListBackupsRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListBackupsResponse`
        """
        http_info = self._list_backups_http_info(request)
        return self._call_api(**http_info)

    def list_backups_async_invoker(self, request):
        http_info = self._list_backups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackupsResponse"
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

    def list_graph_backups_async(self, request):
        """查看某个图的备份列表(1.0.0)

        查询某个图下的备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGraphBackups
        :type request: :class:`huaweicloudsdkges.v1.ListGraphBackupsRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListGraphBackupsResponse`
        """
        http_info = self._list_graph_backups_http_info(request)
        return self._call_api(**http_info)

    def list_graph_backups_async_invoker(self, request):
        http_info = self._list_graph_backups_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_graph_backups_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGraphBackupsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def list_graph_metadatas_async(self, request):
        """查询元数据(1.0.2)

        查询某个图下的元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGraphMetadatas
        :type request: :class:`huaweicloudsdkges.v1.ListGraphMetadatasRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListGraphMetadatasResponse`
        """
        http_info = self._list_graph_metadatas_http_info(request)
        return self._call_api(**http_info)

    def list_graph_metadatas_async_invoker(self, request):
        http_info = self._list_graph_metadatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_graph_metadatas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/metadatas/{metadata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListGraphMetadatasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'metadata_id' in local_var_params:
            path_params['metadata_id'] = local_var_params['metadata_id']

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

    def list_graphs_async(self, request):
        """查询图列表(2.1.18)

        查询当前租户所有的图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGraphs
        :type request: :class:`huaweicloudsdkges.v1.ListGraphsRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListGraphsResponse`
        """
        http_info = self._list_graphs_http_info(request)
        return self._call_api(**http_info)

    def list_graphs_async_invoker(self, request):
        http_info = self._list_graphs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_graphs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs",
            "request_type": request.__class__.__name__,
            "response_type": "ListGraphsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

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

    def list_jobs_async(self, request):
        """查询任务中心(1.1.8)

        查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务，该API用于查询这些任务的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkges.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_async_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jobs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('endTime', local_var_params['end_time']))
        if 'graph_name' in local_var_params:
            query_params.append(('graph_name', local_var_params['graph_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('startTime', local_var_params['start_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

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

    def list_metadatas_async(self, request):
        """查询元数据列表(1.0.2)

        查询元数据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetadatas
        :type request: :class:`huaweicloudsdkges.v1.ListMetadatasRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListMetadatasResponse`
        """
        http_info = self._list_metadatas_http_info(request)
        return self._call_api(**http_info)

    def list_metadatas_async_invoker(self, request):
        http_info = self._list_metadatas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metadatas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/metadatas",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetadatasResponse"
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

    def list_quotas_async(self, request):
        """查询配额(1.0.0)

        查询租户配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkges.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
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

    def resize_graph_async(self, request):
        """扩容图(2.2.21)

        扩容图规格。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeGraph
        :type request: :class:`huaweicloudsdkges.v1.ResizeGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ResizeGraphResponse`
        """
        http_info = self._resize_graph_http_info(request)
        return self._call_api(**http_info)

    def resize_graph_async_invoker(self, request):
        http_info = self._resize_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def restart_graph_async(self, request):
        """强制重启图(2.2.21)

        强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图，会将该图执行中的异步任务变为失败，然后停止图、启动图到运行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartGraph
        :type request: :class:`huaweicloudsdkges.v1.RestartGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.RestartGraphResponse`
        """
        http_info = self._restart_graph_http_info(request)
        return self._call_api(**http_info)

    def restart_graph_async_invoker(self, request):
        http_info = self._restart_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "RestartGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def show_graph_async(self, request):
        """查询图详情(1.0.0)

        根据图ID查询某个图详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGraph
        :type request: :class:`huaweicloudsdkges.v1.ShowGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ShowGraphResponse`
        """
        http_info = self._show_graph_http_info(request)
        return self._call_api(**http_info)

    def show_graph_async_invoker(self, request):
        http_info = self._show_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_graph_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def show_job_async(self, request):
        """查询Job状态(1.0.0)-管理面

        查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后，会返回jobId，通过jobId查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob
        :type request: :class:`huaweicloudsdkges.v1.ShowJobRequest`
        :rtype: :class:`huaweicloudsdkges.v1.ShowJobResponse`
        """
        http_info = self._show_job_http_info(request)
        return self._call_api(**http_info)

    def show_job_async_invoker(self, request):
        http_info = self._show_job_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/jobs/{job_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJobResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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

    def start_graph_async(self, request):
        """启动图(1.0.0)

        启动一个图。暂时不用的图可以先关闭，需要使用时再启动。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartGraph
        :type request: :class:`huaweicloudsdkges.v1.StartGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.StartGraphResponse`
        """
        http_info = self._start_graph_http_info(request)
        return self._call_api(**http_info)

    def start_graph_async_invoker(self, request):
        http_info = self._start_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StartGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def stop_graph_async(self, request):
        """关闭图(1.0.0)

        关闭一个图。如果图创建好了，暂时不用可以先关闭，需要使用时再启用。
        &gt;处于关闭状态的图不计算实例费用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopGraph
        :type request: :class:`huaweicloudsdkges.v1.StopGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.StopGraphResponse`
        """
        http_info = self._stop_graph_http_info(request)
        return self._call_api(**http_info)

    def stop_graph_async_invoker(self, request):
        http_info = self._stop_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "StopGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def upgrade_graph_async(self, request):
        """升级图(1.0.5)

        升级图。图引擎服务会定期升级版本，用户可根据需要升级图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeGraph
        :type request: :class:`huaweicloudsdkges.v1.UpgradeGraphRequest`
        :rtype: :class:`huaweicloudsdkges.v1.UpgradeGraphResponse`
        """
        http_info = self._upgrade_graph_http_info(request)
        return self._call_api(**http_info)

    def upgrade_graph_async_invoker(self, request):
        http_info = self._upgrade_graph_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_graph_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/{graph_id}/action",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeGraphResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'action_id' in local_var_params:
            query_params.append(('action_id', local_var_params['action_id']))

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

    def upload_from_obs_async(self, request):
        """从OBS导入元数据(1.0.0)

        从OBS导入元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadFromObs
        :type request: :class:`huaweicloudsdkges.v1.UploadFromObsRequest`
        :rtype: :class:`huaweicloudsdkges.v1.UploadFromObsResponse`
        """
        http_info = self._upload_from_obs_http_info(request)
        return self._call_api(**http_info)

    def upload_from_obs_async_invoker(self, request):
        http_info = self._upload_from_obs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_from_obs_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1.0/{project_id}/graphs/metadata/upload_from_obs",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFromObsResponse"
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

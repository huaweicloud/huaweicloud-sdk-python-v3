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
        self.model_package = importlib.import_module("huaweicloudsdkges.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "GesAsyncClient":
                raise TypeError("client type error, support client type is GesAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def attach_eip2_async(self, request):
        """绑定EIP

        可以通过绑定弹性公网IP（简称EIP）访问GES服务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AttachEip2
        :type request: :class:`huaweicloudsdkges.v2.AttachEip2Request`
        :rtype: :class:`huaweicloudsdkges.v2.AttachEip2Response`
        """
        http_info = self._attach_eip2_http_info(request)
        return self._call_api(**http_info)

    def attach_eip2_async_invoker(self, request):
        http_info = self._attach_eip2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _attach_eip2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/bind-eip",
            "request_type": request.__class__.__name__,
            "response_type": "AttachEip2Response"
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

    def clear_graph2_async(self, request):
        """清空图

        清空图中所有数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ClearGraph2
        :type request: :class:`huaweicloudsdkges.v2.ClearGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ClearGraph2Response`
        """
        http_info = self._clear_graph2_http_info(request)
        return self._call_api(**http_info)

    def clear_graph2_async_invoker(self, request):
        http_info = self._clear_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _clear_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/clear-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ClearGraph2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'clear_metadata' in local_var_params:
            query_params.append(('clear_metadata', local_var_params['clear_metadata']))

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

    def create_backup2_async(self, request):
        """新增备份

        新增备份。当前图数据出现错误或故障时，可以启动备份图进行恢复。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateBackup2
        :type request: :class:`huaweicloudsdkges.v2.CreateBackup2Request`
        :rtype: :class:`huaweicloudsdkges.v2.CreateBackup2Response`
        """
        http_info = self._create_backup2_http_info(request)
        return self._call_api(**http_info)

    def create_backup2_async_invoker(self, request):
        http_info = self._create_backup2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_backup2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "CreateBackup2Response"
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

    def create_graph2_async(self, request):
        """创建图

        创建一个图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateGraph2
        :type request: :class:`huaweicloudsdkges.v2.CreateGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.CreateGraph2Response`
        """
        http_info = self._create_graph2_http_info(request)
        return self._call_api(**http_info)

    def create_graph2_async_invoker(self, request):
        http_info = self._create_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateGraph2Response"
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

    def create_metadata2_async(self, request):
        """新增元数据

        新增元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMetadata2
        :type request: :class:`huaweicloudsdkges.v2.CreateMetadata2Request`
        :rtype: :class:`huaweicloudsdkges.v2.CreateMetadata2Response`
        """
        http_info = self._create_metadata2_http_info(request)
        return self._call_api(**http_info)

    def create_metadata2_async_invoker(self, request):
        http_info = self._create_metadata2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_metadata2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/metadatas",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMetadata2Response"
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

    def delete_backup2_async(self, request):
        """删除备份

        删除备份。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteBackup2
        :type request: :class:`huaweicloudsdkges.v2.DeleteBackup2Request`
        :rtype: :class:`huaweicloudsdkges.v2.DeleteBackup2Response`
        """
        http_info = self._delete_backup2_http_info(request)
        return self._call_api(**http_info)

    def delete_backup2_async_invoker(self, request):
        http_info = self._delete_backup2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_backup2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/backups/{backup_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteBackup2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']
        if 'backup_id' in local_var_params:
            path_params['backup_id'] = local_var_params['backup_id']

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

    def delete_graph2_async(self, request):
        """删除图

        删除一个图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteGraph2
        :type request: :class:`huaweicloudsdkges.v2.DeleteGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.DeleteGraph2Response`
        """
        http_info = self._delete_graph2_http_info(request)
        return self._call_api(**http_info)

    def delete_graph2_async_invoker(self, request):
        http_info = self._delete_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_graph2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteGraph2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

        query_params = []
        if 'keep_backup' in local_var_params:
            query_params.append(('keep_backup', local_var_params['keep_backup']))

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

    def delete_metadata2_async(self, request):
        """删除元数据

        删除元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMetadata2
        :type request: :class:`huaweicloudsdkges.v2.DeleteMetadata2Request`
        :rtype: :class:`huaweicloudsdkges.v2.DeleteMetadata2Response`
        """
        http_info = self._delete_metadata2_http_info(request)
        return self._call_api(**http_info)

    def delete_metadata2_async_invoker(self, request):
        http_info = self._delete_metadata2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_metadata2_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/graphs/metadatas/{metadata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMetadata2Response"
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

    def detach_eip2_async(self, request):
        """解绑EIP

        当无需继续使用EIP时，您可通过解绑EIP来释放网络资源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DetachEip2
        :type request: :class:`huaweicloudsdkges.v2.DetachEip2Request`
        :rtype: :class:`huaweicloudsdkges.v2.DetachEip2Response`
        """
        http_info = self._detach_eip2_http_info(request)
        return self._call_api(**http_info)

    def detach_eip2_async_invoker(self, request):
        http_info = self._detach_eip2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _detach_eip2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/unbind-eip",
            "request_type": request.__class__.__name__,
            "response_type": "DetachEip2Response"
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

    def expand_graph2_async(self, request):
        """扩副本

        扩副本能力允许动态扩容多个从节点，扩容的从节点可以处理读请求，从而提高读请求性能。
        &gt; 1.一万边和百亿边规格的图暂不支持扩副本。
        2.进行扩副本操作后，不支持扩容图操作。
        3.如果要对图进行扩容和扩副本两个操作，需要您先进行扩容图操作，再进行扩副本操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExpandGraph2
        :type request: :class:`huaweicloudsdkges.v2.ExpandGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ExpandGraph2Response`
        """
        http_info = self._expand_graph2_http_info(request)
        return self._call_api(**http_info)

    def expand_graph2_async_invoker(self, request):
        http_info = self._expand_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _expand_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/expand",
            "request_type": request.__class__.__name__,
            "response_type": "ExpandGraph2Response"
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

    def export_graph2_async(self, request):
        """导出图

        导出图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportGraph2
        :type request: :class:`huaweicloudsdkges.v2.ExportGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ExportGraph2Response`
        """
        http_info = self._export_graph2_http_info(request)
        return self._call_api(**http_info)

    def export_graph2_async_invoker(self, request):
        http_info = self._export_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/export-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ExportGraph2Response"
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

    def import_graph2_async(self, request):
        """增量导入图

        增量导入图数据。
        &gt; 为防止系统重启时，不能正常恢复导入图数据，建议在使用图期间，不要删除存储在OBS中的数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportGraph2
        :type request: :class:`huaweicloudsdkges.v2.ImportGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ImportGraph2Response`
        """
        http_info = self._import_graph2_http_info(request)
        return self._call_api(**http_info)

    def import_graph2_async_invoker(self, request):
        http_info = self._import_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/import-graph",
            "request_type": request.__class__.__name__,
            "response_type": "ImportGraph2Response"
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

    def list_backups2_async(self, request):
        """查看所有备份列表

        查询备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListBackups2
        :type request: :class:`huaweicloudsdkges.v2.ListBackups2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListBackups2Response`
        """
        http_info = self._list_backups2_http_info(request)
        return self._call_api(**http_info)

    def list_backups2_async_invoker(self, request):
        http_info = self._list_backups2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_backups2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListBackups2Response"
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

    def list_graph_backups2_async(self, request):
        """查看某个图的备份列表

        查询某个图下的备份列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGraphBackups2
        :type request: :class:`huaweicloudsdkges.v2.ListGraphBackups2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListGraphBackups2Response`
        """
        http_info = self._list_graph_backups2_http_info(request)
        return self._call_api(**http_info)

    def list_graph_backups2_async_invoker(self, request):
        http_info = self._list_graph_backups2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_graph_backups2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/backups",
            "request_type": request.__class__.__name__,
            "response_type": "ListGraphBackups2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'graph_id' in local_var_params:
            path_params['graph_id'] = local_var_params['graph_id']

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

    def list_graphs2_async(self, request):
        """查询图列表

        查询当前租户所有的图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListGraphs2
        :type request: :class:`huaweicloudsdkges.v2.ListGraphs2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListGraphs2Response`
        """
        http_info = self._list_graphs2_http_info(request)
        return self._call_api(**http_info)

    def list_graphs2_async_invoker(self, request):
        http_info = self._list_graphs2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_graphs2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs",
            "request_type": request.__class__.__name__,
            "response_type": "ListGraphs2Response"
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

    def list_jobs2_async(self, request):
        """查询任务中心

        查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务，该API用于查询这些任务的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListJobs2
        :type request: :class:`huaweicloudsdkges.v2.ListJobs2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListJobs2Response`
        """
        http_info = self._list_jobs2_http_info(request)
        return self._call_api(**http_info)

    def list_jobs2_async_invoker(self, request):
        http_info = self._list_jobs2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_jobs2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/jobs",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobs2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'graph_name' in local_var_params:
            query_params.append(('graph_name', local_var_params['graph_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
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

    def list_metadatas2_async(self, request):
        """查询元数据列表

        查询元数据列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMetadatas2
        :type request: :class:`huaweicloudsdkges.v2.ListMetadatas2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListMetadatas2Response`
        """
        http_info = self._list_metadatas2_http_info(request)
        return self._call_api(**http_info)

    def list_metadatas2_async_invoker(self, request):
        http_info = self._list_metadatas2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_metadatas2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/metadatas",
            "request_type": request.__class__.__name__,
            "response_type": "ListMetadatas2Response"
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

    def list_quotas2_async(self, request):
        """查询配额

        查询租户配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas2
        :type request: :class:`huaweicloudsdkges.v2.ListQuotas2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListQuotas2Response`
        """
        http_info = self._list_quotas2_http_info(request)
        return self._call_api(**http_info)

    def list_quotas2_async_invoker(self, request):
        http_info = self._list_quotas2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotas2Response"
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

    def resize_graph2_async(self, request):
        """扩容图

        扩容图规格。
        &gt; 扩容图以后所有索引（复合索引和全文索引）都需要重新创建。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResizeGraph2
        :type request: :class:`huaweicloudsdkges.v2.ResizeGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ResizeGraph2Response`
        """
        http_info = self._resize_graph2_http_info(request)
        return self._call_api(**http_info)

    def resize_graph2_async_invoker(self, request):
        http_info = self._resize_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resize_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/resize",
            "request_type": request.__class__.__name__,
            "response_type": "ResizeGraph2Response"
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

    def restart_graph2_async(self, request):
        """强制重启图

        强制启动一个图。针对导入、导出 、运行中 、清空中的图。强制重启图，会将该图执行中的异步任务变为失败，然后停止图、启动图到运行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RestartGraph2
        :type request: :class:`huaweicloudsdkges.v2.RestartGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.RestartGraph2Response`
        """
        http_info = self._restart_graph2_http_info(request)
        return self._call_api(**http_info)

    def restart_graph2_async_invoker(self, request):
        http_info = self._restart_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _restart_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/restart",
            "request_type": request.__class__.__name__,
            "response_type": "RestartGraph2Response"
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

    def show_graph2_async(self, request):
        """查询图详情

        根据图ID查询某个图详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowGraph2
        :type request: :class:`huaweicloudsdkges.v2.ShowGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ShowGraph2Response`
        """
        http_info = self._show_graph2_http_info(request)
        return self._call_api(**http_info)

    def show_graph2_async_invoker(self, request):
        http_info = self._show_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_graph2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowGraph2Response"
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

    def show_job2_async(self, request):
        """查询Job状态-管理面

        查询Job的执行状态。对创建图、关闭图、启动图、删除图、导入图等异步API命令下发后，会返回jobId，通过jobId查询任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowJob2
        :type request: :class:`huaweicloudsdkges.v2.ShowJob2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ShowJob2Response`
        """
        http_info = self._show_job2_http_info(request)
        return self._call_api(**http_info)

    def show_job2_async_invoker(self, request):
        http_info = self._show_job2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_job2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/jobs/{job_id}/status",
            "request_type": request.__class__.__name__,
            "response_type": "ShowJob2Response"
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

    def show_metadata2_async(self, request):
        """查询元数据

        查询某个元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowMetadata2
        :type request: :class:`huaweicloudsdkges.v2.ShowMetadata2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ShowMetadata2Response`
        """
        http_info = self._show_metadata2_http_info(request)
        return self._call_api(**http_info)

    def show_metadata2_async_invoker(self, request):
        http_info = self._show_metadata2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_metadata2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/metadatas/{metadata_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowMetadata2Response"
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

    def start_graph2_async(self, request):
        """启动图

        启动一个图。暂时不用的图可以先关闭，需要使用时再启动。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StartGraph2
        :type request: :class:`huaweicloudsdkges.v2.StartGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.StartGraph2Response`
        """
        http_info = self._start_graph2_http_info(request)
        return self._call_api(**http_info)

    def start_graph2_async_invoker(self, request):
        http_info = self._start_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _start_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/start",
            "request_type": request.__class__.__name__,
            "response_type": "StartGraph2Response"
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

    def stop_graph2_async(self, request):
        """关闭图

        关闭一个图。如果图创建好了，暂时不用可以先关闭，需要使用时再启用。
        &gt; 处于关闭状态的图不计算实例费用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for StopGraph2
        :type request: :class:`huaweicloudsdkges.v2.StopGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.StopGraph2Response`
        """
        http_info = self._stop_graph2_http_info(request)
        return self._call_api(**http_info)

    def stop_graph2_async_invoker(self, request):
        http_info = self._stop_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _stop_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/stop",
            "request_type": request.__class__.__name__,
            "response_type": "StopGraph2Response"
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

    def upgrade_graph2_async(self, request):
        """升级图

        升级图。图引擎服务会定期升级版本，用户可根据需要升级图。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpgradeGraph2
        :type request: :class:`huaweicloudsdkges.v2.UpgradeGraph2Request`
        :rtype: :class:`huaweicloudsdkges.v2.UpgradeGraph2Response`
        """
        http_info = self._upgrade_graph2_http_info(request)
        return self._call_api(**http_info)

    def upgrade_graph2_async_invoker(self, request):
        http_info = self._upgrade_graph2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upgrade_graph2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/upgrade",
            "request_type": request.__class__.__name__,
            "response_type": "UpgradeGraph2Response"
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

    def upload_from_obs2_async(self, request):
        """从OBS导入元数据

        从OBS导入元数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UploadFromObs2
        :type request: :class:`huaweicloudsdkges.v2.UploadFromObs2Request`
        :rtype: :class:`huaweicloudsdkges.v2.UploadFromObs2Response`
        """
        http_info = self._upload_from_obs2_http_info(request)
        return self._call_api(**http_info)

    def upload_from_obs2_async_invoker(self, request):
        http_info = self._upload_from_obs2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _upload_from_obs2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/metadata/upload-from-obs",
            "request_type": request.__class__.__name__,
            "response_type": "UploadFromObs2Response"
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

    def deregister_scenes2_async(self, request):
        """取消订阅场景分析插件

        取消订阅scenes场景应用分析能力，取消订阅后对应scene下的application业务面API将不能使用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeregisterScenes2
        :type request: :class:`huaweicloudsdkges.v2.DeregisterScenes2Request`
        :rtype: :class:`huaweicloudsdkges.v2.DeregisterScenes2Response`
        """
        http_info = self._deregister_scenes2_http_info(request)
        return self._call_api(**http_info)

    def deregister_scenes2_async_invoker(self, request):
        http_info = self._deregister_scenes2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _deregister_scenes2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/scenes/unregister",
            "request_type": request.__class__.__name__,
            "response_type": "DeregisterScenes2Response"
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

    def list_scenes2_async(self, request):
        """查询获取场景应用分析插件

        查询scenes场景下的应用分析能力详情，可以获得对应场景下的application、参数和功能介绍详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListScenes2
        :type request: :class:`huaweicloudsdkges.v2.ListScenes2Request`
        :rtype: :class:`huaweicloudsdkges.v2.ListScenes2Response`
        """
        http_info = self._list_scenes2_http_info(request)
        return self._call_api(**http_info)

    def list_scenes2_async_invoker(self, request):
        http_info = self._list_scenes2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_scenes2_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/graphs/scenes",
            "request_type": request.__class__.__name__,
            "response_type": "ListScenes2Response"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scene_name' in local_var_params:
            query_params.append(('scene_name', local_var_params['scene_name']))
        if 'application_name' in local_var_params:
            query_params.append(('application_name', local_var_params['application_name']))
        if 'graph_id' in local_var_params:
            query_params.append(('graph_id', local_var_params['graph_id']))

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

    def register_scenes2_async(self, request):
        """订阅场景分析插件

        订阅scenes应用场景分析能力，便于业务面API使用对应功能。
        &gt; 已订阅的不可以重复订阅，需要更新请先取消原有订购，重新订购。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for RegisterScenes2
        :type request: :class:`huaweicloudsdkges.v2.RegisterScenes2Request`
        :rtype: :class:`huaweicloudsdkges.v2.RegisterScenes2Response`
        """
        http_info = self._register_scenes2_http_info(request)
        return self._call_api(**http_info)

    def register_scenes2_async_invoker(self, request):
        http_info = self._register_scenes2_http_info(request)
        return AsyncInvoker(self, http_info)

    def _register_scenes2_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/graphs/{graph_id}/scenes/register",
            "request_type": request.__class__.__name__,
            "response_type": "RegisterScenes2Response"
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

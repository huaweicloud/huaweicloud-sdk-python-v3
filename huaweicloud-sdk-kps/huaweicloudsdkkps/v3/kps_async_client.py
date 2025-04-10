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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkkps'")


class KpsAsyncClient(Client):
    def __init__(self):
        super(KpsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkps.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "KpsAsyncClient":
                raise TypeError("client type error, support client type is KpsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def associate_keypair_async(self, request):
        r"""绑定SSH密钥对

        给指定的虚拟机绑定（替换或重置，替换需提供虚拟机已配置的SSH密钥对私钥；重置不需要提供虚拟机的SSH密钥对私钥）新的SSH密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AssociateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.AssociateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.AssociateKeypairResponse`
        """
        http_info = self._associate_keypair_http_info(request)
        return self._call_api(**http_info)

    def associate_keypair_async_invoker(self, request):
        http_info = self._associate_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _associate_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/associate",
            "request_type": request.__class__.__name__,
            "response_type": "AssociateKeypairResponse"
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

    def batch_associate_keypair_async(self, request):
        r"""批量绑定SSH密钥对

        给指定的虚拟机批量绑定新的SSH密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchAssociateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.BatchAssociateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.BatchAssociateKeypairResponse`
        """
        http_info = self._batch_associate_keypair_http_info(request)
        return self._call_api(**http_info)

    def batch_associate_keypair_async_invoker(self, request):
        http_info = self._batch_associate_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_associate_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/batch-associate",
            "request_type": request.__class__.__name__,
            "response_type": "BatchAssociateKeypairResponse"
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

    def batch_export_private_key_async(self, request):
        r"""批量导出密钥对私钥

        批量导出密钥对私钥，单次最多导出10条数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchExportPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.BatchExportPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.BatchExportPrivateKeyResponse`
        """
        http_info = self._batch_export_private_key_http_info(request)
        return self._call_api(**http_info)

    def batch_export_private_key_async_invoker(self, request):
        http_info = self._batch_export_private_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_export_private_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/private-key/batch-export",
            "request_type": request.__class__.__name__,
            "response_type": "BatchExportPrivateKeyResponse"
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

    def batch_import_keypair_async(self, request):
        r"""批量导入SSH密钥对

        批量导入SSH密钥对,单次批量导入不得超过10条记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchImportKeypair
        :type request: :class:`huaweicloudsdkkps.v3.BatchImportKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.BatchImportKeypairResponse`
        """
        http_info = self._batch_import_keypair_http_info(request)
        return self._call_api(**http_info)

    def batch_import_keypair_async_invoker(self, request):
        http_info = self._batch_import_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_import_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/batch-import",
            "request_type": request.__class__.__name__,
            "response_type": "BatchImportKeypairResponse"
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

    def clear_private_key_async(self, request):
        r"""清除私钥

        清除SSH密钥对私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ClearPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.ClearPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ClearPrivateKeyResponse`
        """
        http_info = self._clear_private_key_http_info(request)
        return self._call_api(**http_info)

    def clear_private_key_async_invoker(self, request):
        http_info = self._clear_private_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _clear_private_key_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/keypairs/{keypair_name}/private-key",
            "request_type": request.__class__.__name__,
            "response_type": "ClearPrivateKeyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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

    def create_keypair_async(self, request):
        r"""创建和导入SSH密钥对

        创建和导入SSH密钥对
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.CreateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.CreateKeypairResponse`
        """
        http_info = self._create_keypair_http_info(request)
        return self._call_api(**http_info)

    def create_keypair_async_invoker(self, request):
        http_info = self._create_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs",
            "request_type": request.__class__.__name__,
            "response_type": "CreateKeypairResponse"
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

    def delete_all_failed_task_async(self, request):
        r"""删除所有失败的任务

        删除操作失败的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteAllFailedTask
        :type request: :class:`huaweicloudsdkkps.v3.DeleteAllFailedTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DeleteAllFailedTaskResponse`
        """
        http_info = self._delete_all_failed_task_http_info(request)
        return self._call_api(**http_info)

    def delete_all_failed_task_async_invoker(self, request):
        http_info = self._delete_all_failed_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_all_failed_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/failed-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAllFailedTaskResponse"
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

    def delete_failed_task_async(self, request):
        r"""删除失败的任务

        删除失败的任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteFailedTask
        :type request: :class:`huaweicloudsdkkps.v3.DeleteFailedTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DeleteFailedTaskResponse`
        """
        http_info = self._delete_failed_task_http_info(request)
        return self._call_api(**http_info)

    def delete_failed_task_async_invoker(self, request):
        http_info = self._delete_failed_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_failed_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/failed-tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteFailedTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def delete_keypair_async(self, request):
        r"""删除SSH密钥对

        删除SSH密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteKeypair
        :type request: :class:`huaweicloudsdkkps.v3.DeleteKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DeleteKeypairResponse`
        """
        http_info = self._delete_keypair_http_info(request)
        return self._call_api(**http_info)

    def delete_keypair_async_invoker(self, request):
        http_info = self._delete_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_keypair_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKeypairResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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

    def disassociate_keypair_async(self, request):
        r"""解绑SSH密钥对

        给指定的虚拟机解除绑定SSH密钥对并恢复SSH密码登录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DisassociateKeypair
        :type request: :class:`huaweicloudsdkkps.v3.DisassociateKeypairRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.DisassociateKeypairResponse`
        """
        http_info = self._disassociate_keypair_http_info(request)
        return self._call_api(**http_info)

    def disassociate_keypair_async_invoker(self, request):
        http_info = self._disassociate_keypair_http_info(request)
        return AsyncInvoker(self, http_info)

    def _disassociate_keypair_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/disassociate",
            "request_type": request.__class__.__name__,
            "response_type": "DisassociateKeypairResponse"
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

    def export_private_key_async(self, request):
        r"""导出私钥

        导出指定密钥对的私钥。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ExportPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.ExportPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ExportPrivateKeyResponse`
        """
        http_info = self._export_private_key_http_info(request)
        return self._call_api(**http_info)

    def export_private_key_async_invoker(self, request):
        http_info = self._export_private_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _export_private_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/private-key/export",
            "request_type": request.__class__.__name__,
            "response_type": "ExportPrivateKeyResponse"
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

    def import_private_key_async(self, request):
        r"""导入私钥

        导入私钥到指定密钥对。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ImportPrivateKey
        :type request: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ImportPrivateKeyResponse`
        """
        http_info = self._import_private_key_http_info(request)
        return self._call_api(**http_info)

    def import_private_key_async_invoker(self, request):
        http_info = self._import_private_key_http_info(request)
        return AsyncInvoker(self, http_info)

    def _import_private_key_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/keypairs/private-key/import",
            "request_type": request.__class__.__name__,
            "response_type": "ImportPrivateKeyResponse"
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

    def list_failed_task_async(self, request):
        r"""查询失败的任务信息

        查询绑定、解绑等操作失败的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListFailedTask
        :type request: :class:`huaweicloudsdkkps.v3.ListFailedTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListFailedTaskResponse`
        """
        http_info = self._list_failed_task_http_info(request)
        return self._call_api(**http_info)

    def list_failed_task_async_invoker(self, request):
        http_info = self._list_failed_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_failed_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/failed-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListFailedTaskResponse"
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

    def list_keypair_detail_async(self, request):
        r"""查询SSH密钥对详细信息

        查询SSH密钥对详细信息
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairDetail
        :type request: :class:`huaweicloudsdkkps.v3.ListKeypairDetailRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListKeypairDetailResponse`
        """
        http_info = self._list_keypair_detail_http_info(request)
        return self._call_api(**http_info)

    def list_keypair_detail_async_invoker(self, request):
        http_info = self._list_keypair_detail_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keypair_detail_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeypairDetailResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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

    def list_keypair_task_async(self, request):
        r"""查询任务信息

        根据SSH密钥对接口返回的task_id，查询SSH密钥对当前任务的执行状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairTask
        :type request: :class:`huaweicloudsdkkps.v3.ListKeypairTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListKeypairTaskResponse`
        """
        http_info = self._list_keypair_task_http_info(request)
        return self._call_api(**http_info)

    def list_keypair_task_async_invoker(self, request):
        http_info = self._list_keypair_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keypair_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/tasks/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeypairTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

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

    def list_keypairs_async(self, request):
        r"""查询SSH密钥对列表

        查询SSH密钥对列表
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListKeypairs
        :type request: :class:`huaweicloudsdkkps.v3.ListKeypairsRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListKeypairsResponse`
        """
        http_info = self._list_keypairs_http_info(request)
        return self._call_api(**http_info)

    def list_keypairs_async_invoker(self, request):
        http_info = self._list_keypairs_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_keypairs_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/keypairs",
            "request_type": request.__class__.__name__,
            "response_type": "ListKeypairsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'marker' in local_var_params:
            query_params.append(('marker', local_var_params['marker']))

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

    def list_running_task_async(self, request):
        r"""查询正在处理的任务信息

        查询正在处理的任务信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListRunningTask
        :type request: :class:`huaweicloudsdkkps.v3.ListRunningTaskRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.ListRunningTaskResponse`
        """
        http_info = self._list_running_task_http_info(request)
        return self._call_api(**http_info)

    def list_running_task_async_invoker(self, request):
        http_info = self._list_running_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_running_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/running-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListRunningTaskResponse"
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

    def update_keypair_description_async(self, request):
        r"""更新SSH密钥对描述

        更新SSH密钥对描述。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateKeypairDescription
        :type request: :class:`huaweicloudsdkkps.v3.UpdateKeypairDescriptionRequest`
        :rtype: :class:`huaweicloudsdkkps.v3.UpdateKeypairDescriptionResponse`
        """
        http_info = self._update_keypair_description_http_info(request)
        return self._call_api(**http_info)

    def update_keypair_description_async_invoker(self, request):
        http_info = self._update_keypair_description_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_keypair_description_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/keypairs/{keypair_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKeypairDescriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

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

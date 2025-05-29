# coding: utf-8

from __future__ import absolute_import

import importlib
import warnings

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest
from huaweicloudsdkkvs.v1.kvs_client_interface import KvsClientInterface
try:
    from huaweicloudsdkcore.invoker.invoker import SyncInvoker
except ImportError as e:
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkkvs'")


class KvsClient(Client, KvsClientInterface):
    def __init__(self):
        super(KvsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkkvs.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "KvsClient":
                raise TypeError("client type error, support client type is KvsClient")
            client_builder = ClientBuilder(clazz)

        
        try:
            from .kvs_exception_handler import KvsExceptionHandler
            client_builder.with_exception_handler(KvsExceptionHandler())
        except (ImportError, AttributeError):
            warnings.warn("failed to import 'KvsExceptionHandler', please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkkvs'")

        return client_builder

    def create_table(self, request):
        r"""创建表

        在指定仓内创建表，表名在仓内唯一；创建表时，指定主键模板及本地二级索引模板及全局二级索引模板。创建表时，如果仓不存在，将会自动创建仓。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateTable
        :type request: :class:`huaweicloudsdkkvs.v1.CreateTableRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.CreateTableResponse`
        """
        http_info = self._create_table_http_info(request)
        return self._call_api(**http_info)

    def create_table_invoker(self, request):
        http_info = self._create_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/create-table",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def delete_table(self, request):
        r"""删除表

        删除指定表及所有kv文档，表标记为删除后，空间不会立刻释放，并发的读写访问仍需继续完成。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteTable
        :type request: :class:`huaweicloudsdkkvs.v1.DeleteTableRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.DeleteTableResponse`
        """
        http_info = self._delete_table_http_info(request)
        return self._call_api(**http_info)

    def delete_table_invoker(self, request):
        http_info = self._delete_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/delete-table",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def describe_table(self, request):
        r"""查询表

        指定仓查询表属性，如容量，规模，配额。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeTable
        :type request: :class:`huaweicloudsdkkvs.v1.DescribeTableRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.DescribeTableResponse`
        """
        http_info = self._describe_table_http_info(request)
        return self._call_api(**http_info)

    def describe_table_invoker(self, request):
        http_info = self._describe_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/describe-table",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def list_store(self, request):
        r"""列举仓

        一个账户下可以创建最多25个仓，每个仓可以创建最多100个store，响应中一次性返回所有仓名称。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStore
        :type request: :class:`huaweicloudsdkkvs.v1.ListStoreRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.ListStoreResponse`
        """
        http_info = self._list_store_http_info(request)
        return self._call_api(**http_info)

    def list_store_invoker(self, request):
        http_info = self._list_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_store_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/list-store",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoreResponse"
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
            ['application/bson'])

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

    def list_table(self, request):
        r"""列举表

        指定仓列举创建的所有表。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListTable
        :type request: :class:`huaweicloudsdkkvs.v1.ListTableRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.ListTableResponse`
        """
        http_info = self._list_table_http_info(request)
        return self._call_api(**http_info)

    def list_table_invoker(self, request):
        http_info = self._list_table_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_table_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/list-table",
            "request_type": request.__class__.__name__,
            "response_type": "ListTableResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def batch_get_kv(self, request):
        r"""批量读请求

        批量读请求，其中可以携带一或多个表的不同kv的查询操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchGetKv
        :type request: :class:`huaweicloudsdkkvs.v1.BatchGetKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.BatchGetKvResponse`
        """
        http_info = self._batch_get_kv_http_info(request)
        return self._call_api(**http_info)

    def batch_get_kv_invoker(self, request):
        http_info = self._batch_get_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_get_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/batch-get-kv",
            "request_type": request.__class__.__name__,
            "response_type": "BatchGetKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def batch_write_kv(self, request):
        r"""批量写请求

        批量写请求，其中可以携带一或多个表的不同kv的写操作，上传kv/删除kv。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for BatchWriteKv
        :type request: :class:`huaweicloudsdkkvs.v1.BatchWriteKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.BatchWriteKvResponse`
        """
        http_info = self._batch_write_kv_http_info(request)
        return self._call_api(**http_info)

    def batch_write_kv_invoker(self, request):
        http_info = self._batch_write_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _batch_write_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/batch-write-kv",
            "request_type": request.__class__.__name__,
            "response_type": "BatchWriteKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def delete_kv(self, request):
        r"""删除单个kv

        指定表，指定主键，删除该文档；允许指定条件执行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteKv
        :type request: :class:`huaweicloudsdkkvs.v1.DeleteKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.DeleteKvResponse`
        """
        http_info = self._delete_kv_http_info(request)
        return self._call_api(**http_info)

    def delete_kv_invoker(self, request):
        http_info = self._delete_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/delete-kv",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def get_kv(self, request):
        r"""查询单个kv

        下载一个kv文档的全部内容，或者部分字段的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetKv
        :type request: :class:`huaweicloudsdkkvs.v1.GetKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.GetKvResponse`
        """
        http_info = self._get_kv_http_info(request)
        return self._call_api(**http_info)

    def get_kv_invoker(self, request):
        http_info = self._get_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/get-kv",
            "request_type": request.__class__.__name__,
            "response_type": "GetKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def put_kv(self, request):
        r"""上传单个kv

        指定表，新建kv或覆盖已有kv，且满足表的key schema描述；允许指定条件执行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for PutKv
        :type request: :class:`huaweicloudsdkkvs.v1.PutKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.PutKvResponse`
        """
        http_info = self._put_kv_http_info(request)
        return self._call_api(**http_info)

    def put_kv_invoker(self, request):
        http_info = self._put_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _put_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/put-kv",
            "request_type": request.__class__.__name__,
            "response_type": "PutKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def scan_kv(self, request):
        r"""扫描所有kv

        指定表，扫描表下所有kv；允许指定过滤条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ScanKv
        :type request: :class:`huaweicloudsdkkvs.v1.ScanKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.ScanKvResponse`
        """
        http_info = self._scan_kv_http_info(request)
        return self._call_api(**http_info)

    def scan_kv_invoker(self, request):
        http_info = self._scan_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _scan_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/scan-kv",
            "request_type": request.__class__.__name__,
            "response_type": "ScanKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def scan_skey_kv(self, request):
        r"""扫描分区键内kv

        指定表及分区键，携带条件查询kv；允许指定过滤条件。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ScanSkeyKv
        :type request: :class:`huaweicloudsdkkvs.v1.ScanSkeyKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.ScanSkeyKvResponse`
        """
        http_info = self._scan_skey_kv_http_info(request)
        return self._call_api(**http_info)

    def scan_skey_kv_invoker(self, request):
        http_info = self._scan_skey_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _scan_skey_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/scan-skey-kv",
            "request_type": request.__class__.__name__,
            "response_type": "ScanSkeyKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def update_kv(self, request):
        r"""更新单个kv

        指定表，指定主键，指定更新文档的部分内容，如果是自描述文档，指定字段名；如果是二进制文档，指定偏移位置和长度；允许指定条件执行。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpdateKv
        :type request: :class:`huaweicloudsdkkvs.v1.UpdateKvRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.UpdateKvResponse`
        """
        http_info = self._update_kv_http_info(request)
        return self._call_api(**http_info)

    def update_kv_invoker(self, request):
        http_info = self._update_kv_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _update_kv_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/update-kv",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateKvResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'store_name' in local_var_params:
            cname = local_var_params['store_name']

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/bson'])

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

    def check_health(self, request):
        r"""网络信道健康检查

        网络信道健康检查，返回response未抛出网络异常即为成功
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CheckHealth
        :type request: :class:`huaweicloudsdkkvs.v1.CheckHealthRequest`
        :rtype: :class:`huaweicloudsdkkvs.v1.CheckHealthResponse`
        """
        http_info = self._check_health_http_info(request)
        return self._call_api(**http_info)

    def check_health_invoker(self, request):
        http_info = self._check_health_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _check_health_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/check-health",
            "request_type": request.__class__.__name__,
            "response_type": "CheckHealthResponse"
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
            ['application/bson'])

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

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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdwr'")


class DwrClient(Client):
    def __init__(self):
        super(DwrClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdwr.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DwrClient":
                raise TypeError("client type error, support client type is DwrClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def create_collection(self, request):
        r"""创建collection

        在知识仓实例下创建collection。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateCollection
        :type request: :class:`huaweicloudsdkdwr.v1.CreateCollectionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.CreateCollectionResponse`
        """
        http_info = self._create_collection_http_info(request)
        return self._call_api(**http_info)

    def create_collection_invoker(self, request):
        http_info = self._create_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/collections/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateCollectionResponse"
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

    def create_index(self, request):
        r"""创建索引

        在指定的collection中，按照参数创建索引。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateIndex
        :type request: :class:`huaweicloudsdkdwr.v1.CreateIndexRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.CreateIndexResponse`
        """
        http_info = self._create_index_http_info(request)
        return self._call_api(**http_info)

    def create_index_invoker(self, request):
        http_info = self._create_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_index_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/indexes/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateIndexResponse"
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

    def create_store(self, request):
        r"""创建知识仓实例

        创建知识仓实例。知识仓实例名称region内唯一。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for CreateStore
        :type request: :class:`huaweicloudsdkdwr.v1.CreateStoreRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.CreateStoreResponse`
        """
        http_info = self._create_store_http_info(request)
        return self._call_api(**http_info)

    def create_store_invoker(self, request):
        http_info = self._create_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _create_store_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stores/create",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStoreResponse"
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

    def delete_collection(self, request):
        r"""删除collection

        在知识仓实例下删除指定的collection。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteCollection
        :type request: :class:`huaweicloudsdkdwr.v1.DeleteCollectionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DeleteCollectionResponse`
        """
        http_info = self._delete_collection_http_info(request)
        return self._call_api(**http_info)

    def delete_collection_invoker(self, request):
        http_info = self._delete_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/collections/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCollectionResponse"
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

    def delete_index(self, request):
        r"""删除索引

        删除指定索引。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteIndex
        :type request: :class:`huaweicloudsdkdwr.v1.DeleteIndexRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DeleteIndexResponse`
        """
        http_info = self._delete_index_http_info(request)
        return self._call_api(**http_info)

    def delete_index_invoker(self, request):
        http_info = self._delete_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_index_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/indexes/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteIndexResponse"
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

    def delete_store(self, request):
        r"""删除知识仓实例

        删除指定的知识仓实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteStore
        :type request: :class:`huaweicloudsdkdwr.v1.DeleteStoreRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DeleteStoreResponse`
        """
        http_info = self._delete_store_http_info(request)
        return self._call_api(**http_info)

    def delete_store_invoker(self, request):
        http_info = self._delete_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_store_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stores/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStoreResponse"
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

    def describe_collection(self, request):
        r"""查询collection

        在知识仓实例下查询指定的collection的信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeCollection
        :type request: :class:`huaweicloudsdkdwr.v1.DescribeCollectionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DescribeCollectionResponse`
        """
        http_info = self._describe_collection_http_info(request)
        return self._call_api(**http_info)

    def describe_collection_invoker(self, request):
        http_info = self._describe_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/collections/describe",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeCollectionResponse"
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

    def describe_index(self, request):
        r"""查询索引

        查询指定索引的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeIndex
        :type request: :class:`huaweicloudsdkdwr.v1.DescribeIndexRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DescribeIndexResponse`
        """
        http_info = self._describe_index_http_info(request)
        return self._call_api(**http_info)

    def describe_index_invoker(self, request):
        http_info = self._describe_index_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_index_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/indexes/describe",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeIndexResponse"
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

    def describe_job(self, request):
        r"""获取指定ID任务信息

        根据指定的jobid查询任务信息。用于在创建和删除知识仓实例操作执行成功后，通过响应中返回的job_id，来查询创建和删除知识仓实例执行的具体结果。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeJob
        :type request: :class:`huaweicloudsdkdwr.v1.DescribeJobRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DescribeJobResponse`
        """
        http_info = self._describe_job_http_info(request)
        return self._call_api(**http_info)

    def describe_job_invoker(self, request):
        http_info = self._describe_job_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_job_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/jobs/describe",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeJobResponse"
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

    def describe_store(self, request):
        r"""查询知识仓实例

        查询指定知识仓实例的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DescribeStore
        :type request: :class:`huaweicloudsdkdwr.v1.DescribeStoreRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DescribeStoreResponse`
        """
        http_info = self._describe_store_http_info(request)
        return self._call_api(**http_info)

    def describe_store_invoker(self, request):
        http_info = self._describe_store_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _describe_store_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stores/describe",
            "request_type": request.__class__.__name__,
            "response_type": "DescribeStoreResponse"
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

    def get_progress(self, request):
        r"""查询索引构建进度

        查询指定索引的构建进度。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for GetProgress
        :type request: :class:`huaweicloudsdkdwr.v1.GetProgressRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.GetProgressResponse`
        """
        http_info = self._get_progress_http_info(request)
        return self._call_api(**http_info)

    def get_progress_invoker(self, request):
        http_info = self._get_progress_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _get_progress_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/indexes/get-progress",
            "request_type": request.__class__.__name__,
            "response_type": "GetProgressResponse"
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

    def list_collections(self, request):
        r"""列举collection

        列举指定知识仓实例中所有的collections。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListCollections
        :type request: :class:`huaweicloudsdkdwr.v1.ListCollectionsRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.ListCollectionsResponse`
        """
        http_info = self._list_collections_http_info(request)
        return self._call_api(**http_info)

    def list_collections_invoker(self, request):
        http_info = self._list_collections_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_collections_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/collections/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListCollectionsResponse"
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

    def list_jobs(self, request):
        r"""查询任务列表

        根据指定条件查询列举任务的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListJobs
        :type request: :class:`huaweicloudsdkdwr.v1.ListJobsRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.ListJobsResponse`
        """
        http_info = self._list_jobs_http_info(request)
        return self._call_api(**http_info)

    def list_jobs_invoker(self, request):
        http_info = self._list_jobs_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_jobs_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/jobs/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListJobsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
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

    def list_stores(self, request):
        r"""列举知识仓实例

        列举租户所有的知识仓实例。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ListStores
        :type request: :class:`huaweicloudsdkdwr.v1.ListStoresRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.ListStoresResponse`
        """
        http_info = self._list_stores_http_info(request)
        return self._call_api(**http_info)

    def list_stores_invoker(self, request):
        http_info = self._list_stores_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _list_stores_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/stores/list",
            "request_type": request.__class__.__name__,
            "response_type": "ListStoresResponse"
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

    def load_collection(self, request):
        r"""加载collection

        加载指定collection的数据。加载成功后，才能执行查询操作。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for LoadCollection
        :type request: :class:`huaweicloudsdkdwr.v1.LoadCollectionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.LoadCollectionResponse`
        """
        http_info = self._load_collection_http_info(request)
        return self._call_api(**http_info)

    def load_collection_invoker(self, request):
        http_info = self._load_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _load_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/collections/load",
            "request_type": request.__class__.__name__,
            "response_type": "LoadCollectionResponse"
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

    def release_collection(self, request):
        r"""卸载collection

        卸载已加载collection的数据。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for ReleaseCollection
        :type request: :class:`huaweicloudsdkdwr.v1.ReleaseCollectionRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.ReleaseCollectionResponse`
        """
        http_info = self._release_collection_http_info(request)
        return self._call_api(**http_info)

    def release_collection_invoker(self, request):
        http_info = self._release_collection_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _release_collection_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/collections/release",
            "request_type": request.__class__.__name__,
            "response_type": "ReleaseCollectionResponse"
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

    def delete_entities(self, request):
        r"""删除向量

        在指定的collection中删除一个或多个Entity。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for DeleteEntities
        :type request: :class:`huaweicloudsdkdwr.v1.DeleteEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.DeleteEntitiesResponse`
        """
        http_info = self._delete_entities_http_info(request)
        return self._call_api(**http_info)

    def delete_entities_invoker(self, request):
        http_info = self._delete_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _delete_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/entities/delete",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEntitiesResponse"
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

    def hybrid_search(self, request):
        r"""混合搜索

        基于相似度匹配的查询方式，用于查找与给定多个向量进行相似性搜索，支持密集向量，稀疏向量等多路召回，并对结果进行重排处理，最终返回指定的 Top K 个最相似的 Entity。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for HybridSearch
        :type request: :class:`huaweicloudsdkdwr.v1.HybridSearchRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.HybridSearchResponse`
        """
        http_info = self._hybrid_search_http_info(request)
        return self._call_api(**http_info)

    def hybrid_search_invoker(self, request):
        http_info = self._hybrid_search_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _hybrid_search_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/entities/hybrid-search",
            "request_type": request.__class__.__name__,
            "response_type": "HybridSearchResponse"
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

    def insert_entities(self, request):
        r"""插入向量

        在指定的collection中插入一个或多个Entity。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for InsertEntities
        :type request: :class:`huaweicloudsdkdwr.v1.InsertEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.InsertEntitiesResponse`
        """
        http_info = self._insert_entities_http_info(request)
        return self._call_api(**http_info)

    def insert_entities_invoker(self, request):
        http_info = self._insert_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _insert_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/entities/insert",
            "request_type": request.__class__.__name__,
            "response_type": "InsertEntitiesResponse"
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

    def query_entities(self, request):
        r"""标量查询

        接口用于精确查找与查询条件完全匹配的向量，此操作使用指定的布尔表达式对标量字段进行筛选。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for QueryEntities
        :type request: :class:`huaweicloudsdkdwr.v1.QueryEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.QueryEntitiesResponse`
        """
        http_info = self._query_entities_http_info(request)
        return self._call_api(**http_info)

    def query_entities_invoker(self, request):
        http_info = self._query_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _query_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/entities/query",
            "request_type": request.__class__.__name__,
            "response_type": "QueryEntitiesResponse"
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

    def search_entities(self, request):
        r"""向量查询

        基于相似度匹配的查询方式，用于查找与给定查询向量相似的向量。返回指定的 Top K 个最相似的 Entity。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for SearchEntities
        :type request: :class:`huaweicloudsdkdwr.v1.SearchEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.SearchEntitiesResponse`
        """
        http_info = self._search_entities_http_info(request)
        return self._call_api(**http_info)

    def search_entities_invoker(self, request):
        http_info = self._search_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _search_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/entities/search",
            "request_type": request.__class__.__name__,
            "response_type": "SearchEntitiesResponse"
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

    def upsert_entities(self, request):
        r"""更新向量

        在指定collection中更新Entity。如果pk列中值存在，则更新Entity，如果不存在，则插入Entity。
        
        Please refer to HUAWEI cloud API Explorer for details.

        :param request: Request instance for UpsertEntities
        :type request: :class:`huaweicloudsdkdwr.v1.UpsertEntitiesRequest`
        :rtype: :class:`huaweicloudsdkdwr.v1.UpsertEntitiesResponse`
        """
        http_info = self._upsert_entities_http_info(request)
        return self._call_api(**http_info)

    def upsert_entities_invoker(self, request):
        http_info = self._upsert_entities_http_info(request)
        return SyncInvoker(self, http_info)

    @classmethod
    def _upsert_entities_http_info(cls, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/entities/upsert",
            "request_type": request.__class__.__name__,
            "response_type": "UpsertEntitiesResponse"
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

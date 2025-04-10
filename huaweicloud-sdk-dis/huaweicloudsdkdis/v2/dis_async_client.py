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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkdis'")


class DisAsyncClient(Client):
    def __init__(self):
        super(DisAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkdis.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "DisAsyncClient":
                raise TypeError("client type error, support client type is DisAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_tags_async(self, request):
        r"""批量添加资源标签

        该接口用于批量添加资源（通道等）标签。此接口为幂等接口：创建时如果请求体中存在重复key则报错。创建时，不允许设置重复key数据，如果数据库已存在该key，就覆盖value的值。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateTags
        :type request: :class:`huaweicloudsdkdis.v2.BatchCreateTagsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.BatchCreateTagsResponse`
        """
        http_info = self._batch_create_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_tags_async_invoker(self, request):
        http_info = self._batch_create_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/stream/{stream_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def batch_delete_tags_async(self, request):
        r"""批量删除资源标签

        该接口用于批量删除资源（通道等）标签。此接口为幂等接口：删除时，如果删除的标签不存在，默认处理成功；删除时不对标签字符集范围做校验。删除时tags结构体不能缺失，key不能为空，或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteTags
        :type request: :class:`huaweicloudsdkdis.v2.BatchDeleteTagsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.BatchDeleteTagsResponse`
        """
        http_info = self._batch_delete_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_tags_async_invoker(self, request):
        http_info = self._batch_delete_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/stream/{stream_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def batch_start_transfer_task_async(self, request):
        r"""批量启动转储任务

        此接口用于批量启动转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStartTransferTask
        :type request: :class:`huaweicloudsdkdis.v2.BatchStartTransferTaskRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.BatchStartTransferTaskResponse`
        """
        http_info = self._batch_start_transfer_task_http_info(request)
        return self._call_api(**http_info)

    def batch_start_transfer_task_async_invoker(self, request):
        http_info = self._batch_start_transfer_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_start_transfer_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/transfer-tasks/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStartTransferTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

    def batch_stop_transfer_task_async(self, request):
        r"""批量暂停转储任务

        此接口用于批量暂停转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchStopTransferTask
        :type request: :class:`huaweicloudsdkdis.v2.BatchStopTransferTaskRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.BatchStopTransferTaskResponse`
        """
        http_info = self._batch_stop_transfer_task_http_info(request)
        return self._call_api(**http_info)

    def batch_stop_transfer_task_async_invoker(self, request):
        http_info = self._batch_stop_transfer_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_stop_transfer_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/transfer-tasks/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchStopTransferTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

    def consume_records_async(self, request):
        r"""下载数据

        本接口用于从DIS通道中下载数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ConsumeRecords
        :type request: :class:`huaweicloudsdkdis.v2.ConsumeRecordsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ConsumeRecordsResponse`
        """
        http_info = self._consume_records_http_info(request)
        return self._call_api(**http_info)

    def consume_records_async_invoker(self, request):
        http_info = self._consume_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _consume_records_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "ConsumeRecordsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'partition_cursor' in local_var_params:
            query_params.append(('partition-cursor', local_var_params['partition_cursor']))
        if 'max_fetch_bytes' in local_var_params:
            query_params.append(('max_fetch_bytes', local_var_params['max_fetch_bytes']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_obs_transfer_task_async(self, request):
        r"""添加OBS转储任务

        本接口用于添加OBS转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateObsTransferTask
        :type request: :class:`huaweicloudsdkdis.v2.CreateObsTransferTaskRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.CreateObsTransferTaskResponse`
        """
        http_info = self._create_obs_transfer_task_http_info(request)
        return self._call_api(**http_info)

    def create_obs_transfer_task_async_invoker(self, request):
        http_info = self._create_obs_transfer_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_obs_transfer_task_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/transfer-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateObsTransferTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_stream_async(self, request):
        r"""创建通道

        本接口用于创建通道。
        
        - 创建通道时，需指定通道类型（普通、高级）、分区数量。
        - 一个账号默认最多可以创建10个高级通道分区和50个普通通道分区，可提交工单增加配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateStream
        :type request: :class:`huaweicloudsdkdis.v2.CreateStreamRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.CreateStreamResponse`
        """
        http_info = self._create_stream_http_info(request)
        return self._call_api(**http_info)

    def create_stream_async_invoker(self, request):
        http_info = self._create_stream_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_stream_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/streams",
            "request_type": request.__class__.__name__,
            "response_type": "CreateStreamResponse"
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

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def create_tag_async(self, request):
        r"""给指定通道添加标签

        本接口用于给指定通道添加标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTag
        :type request: :class:`huaweicloudsdkdis.v2.CreateTagRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.CreateTagResponse`
        """
        http_info = self._create_tag_http_info(request)
        return self._call_api(**http_info)

    def create_tag_async_invoker(self, request):
        http_info = self._create_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/stream/{stream_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def delete_stream_async(self, request):
        r"""删除指定通道

        本接口用于删除指定通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteStream
        :type request: :class:`huaweicloudsdkdis.v2.DeleteStreamRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.DeleteStreamResponse`
        """
        http_info = self._delete_stream_http_info(request)
        return self._call_api(**http_info)

    def delete_stream_async_invoker(self, request):
        http_info = self._delete_stream_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_stream_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/streams/{stream_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_tag_async(self, request):
        r"""删除指定通道的标签

        该接口用于删除指定通道的标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTag
        :type request: :class:`huaweicloudsdkdis.v2.DeleteTagRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.DeleteTagResponse`
        """
        http_info = self._delete_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_tag_async_invoker(self, request):
        http_info = self._delete_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/stream/{stream_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']
        if 'key' in local_var_params:
            path_params['key'] = local_var_params['key']

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

    def delete_transfer_task_async(self, request):
        r"""删除转储任务

        该接口用于删除转储任务。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTransferTask
        :type request: :class:`huaweicloudsdkdis.v2.DeleteTransferTaskRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.DeleteTransferTaskResponse`
        """
        http_info = self._delete_transfer_task_http_info(request)
        return self._call_api(**http_info)

    def delete_transfer_task_async_invoker(self, request):
        http_info = self._delete_transfer_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_transfer_task_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/transfer-tasks/{task_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTransferTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_policies_async(self, request):
        r"""查询权限策略列表

        本接口用于查询指定通道的权限策略列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPolicies
        :type request: :class:`huaweicloudsdkdis.v2.ListPoliciesRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ListPoliciesResponse`
        """
        http_info = self._list_policies_http_info(request)
        return self._call_api(**http_info)

    def list_policies_async_invoker(self, request):
        http_info = self._list_policies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_policies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/policies",
            "request_type": request.__class__.__name__,
            "response_type": "ListPoliciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

    def list_resources_by_tags_async(self, request):
        r"""使用标签过滤资源（通道等）

        该接口用于使用标签过滤资源（通道等）。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourcesByTags
        :type request: :class:`huaweicloudsdkdis.v2.ListResourcesByTagsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ListResourcesByTagsResponse`
        """
        http_info = self._list_resources_by_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resources_by_tags_async_invoker(self, request):
        http_info = self._list_resources_by_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resources_by_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/stream/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourcesByTagsResponse"
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

    def list_streams_async(self, request):
        r"""查询通道列表

        本接口用户查询当前租户创建的所有通道。
        
        查询时，需要指定从哪个通道开始返回通道列表和单次请求需要返回的最大数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListStreams
        :type request: :class:`huaweicloudsdkdis.v2.ListStreamsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ListStreamsResponse`
        """
        http_info = self._list_streams_http_info(request)
        return self._call_api(**http_info)

    def list_streams_async_invoker(self, request):
        http_info = self._list_streams_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_streams_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams",
            "request_type": request.__class__.__name__,
            "response_type": "ListStreamsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_stream_name' in local_var_params:
            query_params.append(('start_stream_name', local_var_params['start_stream_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_tags_async(self, request):
        r"""查询指定区域所有标签集合

        该接口用于查询指定区域所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTags
        :type request: :class:`huaweicloudsdkdis.v2.ListTagsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ListTagsResponse`
        """
        http_info = self._list_tags_http_info(request)
        return self._call_api(**http_info)

    def list_tags_async_invoker(self, request):
        http_info = self._list_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/stream/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListTagsResponse"
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

    def list_transfer_tasks_async(self, request):
        r"""查询转储任务列表

        本接口用于查询转储任务列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTransferTasks
        :type request: :class:`huaweicloudsdkdis.v2.ListTransferTasksRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ListTransferTasksResponse`
        """
        http_info = self._list_transfer_tasks_http_info(request)
        return self._call_api(**http_info)

    def list_transfer_tasks_async_invoker(self, request):
        http_info = self._list_transfer_tasks_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_transfer_tasks_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/transfer-tasks",
            "request_type": request.__class__.__name__,
            "response_type": "ListTransferTasksResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

    def send_records_async(self, request):
        r"""上传数据

        本接口用于上传数据到DIS通道中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for SendRecords
        :type request: :class:`huaweicloudsdkdis.v2.SendRecordsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.SendRecordsResponse`
        """
        http_info = self._send_records_http_info(request)
        return self._call_api(**http_info)

    def send_records_async_invoker(self, request):
        http_info = self._send_records_http_info(request)
        return AsyncInvoker(self, http_info)

    def _send_records_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/records",
            "request_type": request.__class__.__name__,
            "response_type": "SendRecordsResponse"
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

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_cursor_async(self, request):
        r"""获取数据游标

        本接口用于获取数据游标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCursor
        :type request: :class:`huaweicloudsdkdis.v2.ShowCursorRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowCursorResponse`
        """
        http_info = self._show_cursor_http_info(request)
        return self._call_api(**http_info)

    def show_cursor_async_invoker(self, request):
        http_info = self._show_cursor_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_cursor_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/cursors",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCursorResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'stream_name' in local_var_params:
            query_params.append(('stream-name', local_var_params['stream_name']))
        if 'partition_id' in local_var_params:
            query_params.append(('partition-id', local_var_params['partition_id']))
        if 'cursor_type' in local_var_params:
            query_params.append(('cursor-type', local_var_params['cursor_type']))
        if 'starting_sequence_number' in local_var_params:
            query_params.append(('starting-sequence-number', local_var_params['starting_sequence_number']))
        if 'timestamp' in local_var_params:
            query_params.append(('timestamp', local_var_params['timestamp']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_partition_metrics_async(self, request):
        r"""查询分区监控

        本接口用于查询通道指定分区的监控数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowPartitionMetrics
        :type request: :class:`huaweicloudsdkdis.v2.ShowPartitionMetricsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowPartitionMetricsResponse`
        """
        http_info = self._show_partition_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_partition_metrics_async_invoker(self, request):
        http_info = self._show_partition_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_partition_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/partitions/{partition_id}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowPartitionMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']
        if 'partition_id' in local_var_params:
            path_params['partition_id'] = local_var_params['partition_id']

        query_params = []
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'label_list' in local_var_params:
            query_params.append(('label_list', local_var_params['label_list']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_stream_async(self, request):
        r"""查看通道详情

        本接口用于查询指定通道的详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStream
        :type request: :class:`huaweicloudsdkdis.v2.ShowStreamRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowStreamResponse`
        """
        http_info = self._show_stream_http_info(request)
        return self._call_api(**http_info)

    def show_stream_async_invoker(self, request):
        http_info = self._show_stream_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_stream_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams/{stream_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

        query_params = []
        if 'start_partition_id' in local_var_params:
            query_params.append(('start_partitionId', local_var_params['start_partition_id']))
        if 'limit_partitions' in local_var_params:
            query_params.append(('limit_partitions', local_var_params['limit_partitions']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_stream_metrics_async(self, request):
        r"""查询通道监控

        本接口用于查询指定通道的监控数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStreamMetrics
        :type request: :class:`huaweicloudsdkdis.v2.ShowStreamMetricsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowStreamMetricsResponse`
        """
        http_info = self._show_stream_metrics_http_info(request)
        return self._call_api(**http_info)

    def show_stream_metrics_async_invoker(self, request):
        http_info = self._show_stream_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_stream_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/metrics",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStreamMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

        query_params = []
        if 'label' in local_var_params:
            query_params.append(('label', local_var_params['label']))
        if 'label_list' in local_var_params:
            query_params.append(('label_list', local_var_params['label_list']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))

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

    def show_stream_tags_async(self, request):
        r"""查询指定通道的标签信息

        该接口用于查询指定通道的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowStreamTags
        :type request: :class:`huaweicloudsdkdis.v2.ShowStreamTagsRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowStreamTagsResponse`
        """
        http_info = self._show_stream_tags_http_info(request)
        return self._call_api(**http_info)

    def show_stream_tags_async_invoker(self, request):
        http_info = self._show_stream_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_stream_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/stream/{stream_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ShowStreamTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_id' in local_var_params:
            path_params['stream_id'] = local_var_params['stream_id']

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

    def show_transfer_task_async(self, request):
        r"""查询转储任务详情

        查询转储任务详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowTransferTask
        :type request: :class:`huaweicloudsdkdis.v2.ShowTransferTaskRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowTransferTaskResponse`
        """
        http_info = self._show_transfer_task_http_info(request)
        return self._call_api(**http_info)

    def show_transfer_task_async_invoker(self, request):
        http_info = self._show_transfer_task_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_transfer_task_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/streams/{stream_name}/transfer-tasks/{task_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowTransferTaskResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']
        if 'task_name' in local_var_params:
            path_params['task_name'] = local_var_params['task_name']

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

    def update_partition_count_async(self, request):
        r"""修改分区数量

        本接口用于变更指定通道中的分区数量。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdatePartitionCount
        :type request: :class:`huaweicloudsdkdis.v2.UpdatePartitionCountRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.UpdatePartitionCountResponse`
        """
        http_info = self._update_partition_count_http_info(request)
        return self._call_api(**http_info)

    def update_partition_count_async_invoker(self, request):
        http_info = self._update_partition_count_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_partition_count_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/streams/{stream_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdatePartitionCountResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

    def update_stream_async(self, request):
        r"""更新通道信息

        本接口用于更新指定通道的通道信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateStream
        :type request: :class:`huaweicloudsdkdis.v2.UpdateStreamRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.UpdateStreamResponse`
        """
        http_info = self._update_stream_http_info(request)
        return self._call_api(**http_info)

    def update_stream_async_invoker(self, request):
        http_info = self._update_stream_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_stream_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/streams/{stream_name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateStreamResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

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

    def create_app_async(self, request):
        r"""创建消费App

        本接口用于创建消费APP。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApp
        :type request: :class:`huaweicloudsdkdis.v2.CreateAppRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.CreateAppResponse`
        """
        http_info = self._create_app_http_info(request)
        return self._call_api(**http_info)

    def create_app_async_invoker(self, request):
        http_info = self._create_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_app_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAppResponse"
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

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_app_async(self, request):
        r"""删除App

        本接口用于删除App。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApp
        :type request: :class:`huaweicloudsdkdis.v2.DeleteAppRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.DeleteAppResponse`
        """
        http_info = self._delete_app_http_info(request)
        return self._call_api(**http_info)

    def delete_app_async_invoker(self, request):
        http_info = self._delete_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_app_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/apps/{app_name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_name' in local_var_params:
            path_params['app_name'] = local_var_params['app_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def list_app_async(self, request):
        r"""查询App列表

        本接口用于查询APP列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApp
        :type request: :class:`huaweicloudsdkdis.v2.ListAppRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ListAppResponse`
        """
        http_info = self._list_app_http_info(request)
        return self._call_api(**http_info)

    def list_app_async_invoker(self, request):
        http_info = self._list_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apps",
            "request_type": request.__class__.__name__,
            "response_type": "ListAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_app_name' in local_var_params:
            query_params.append(('start_app_name', local_var_params['start_app_name']))
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_app_async(self, request):
        r"""查看App详情

        本接口用于查询APP详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowApp
        :type request: :class:`huaweicloudsdkdis.v2.ShowAppRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowAppResponse`
        """
        http_info = self._show_app_http_info(request)
        return self._call_api(**http_info)

    def show_app_async_invoker(self, request):
        http_info = self._show_app_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_app_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apps/{app_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowAppResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_name' in local_var_params:
            path_params['app_name'] = local_var_params['app_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_consumer_state_async(self, request):
        r"""查看App消费状态

        本接口用于查询APP消费状态。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowConsumerState
        :type request: :class:`huaweicloudsdkdis.v2.ShowConsumerStateRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowConsumerStateResponse`
        """
        http_info = self._show_consumer_state_http_info(request)
        return self._call_api(**http_info)

    def show_consumer_state_async_invoker(self, request):
        http_info = self._show_consumer_state_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_consumer_state_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/apps/{app_name}/streams/{stream_name}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowConsumerStateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'app_name' in local_var_params:
            path_params['app_name'] = local_var_params['app_name']
        if 'stream_name' in local_var_params:
            path_params['stream_name'] = local_var_params['stream_name']

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'start_partition_id' in local_var_params:
            query_params.append(('start_partition_id', local_var_params['start_partition_id']))
        if 'checkpoint_type' in local_var_params:
            query_params.append(('checkpoint_type', local_var_params['checkpoint_type']))

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

    def commit_checkpoint_async(self, request):
        r"""提交Checkpoint

        本接口用于提交Checkpoint。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CommitCheckpoint
        :type request: :class:`huaweicloudsdkdis.v2.CommitCheckpointRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.CommitCheckpointResponse`
        """
        http_info = self._commit_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def commit_checkpoint_async_invoker(self, request):
        http_info = self._commit_checkpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _commit_checkpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/checkpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CommitCheckpointResponse"
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

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def delete_checkpoint_async(self, request):
        r"""删除Checkpoint

        本接口用于删除Checkpoint。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteCheckpoint
        :type request: :class:`huaweicloudsdkdis.v2.DeleteCheckpointRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.DeleteCheckpointResponse`
        """
        http_info = self._delete_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_checkpoint_async_invoker(self, request):
        http_info = self._delete_checkpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_checkpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/checkpoints",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteCheckpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'checkpoint_type' in local_var_params:
            query_params.append(('checkpoint_type', local_var_params['checkpoint_type']))
        if 'partition_id' in local_var_params:
            query_params.append(('partition_id', local_var_params['partition_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

        http_info["cname"] = cname
        http_info["collection_formats"] = collection_formats
        http_info["path_params"] = path_params
        http_info["query_params"] = query_params
        http_info["header_params"] = header_params
        http_info["post_params"] = form_params
        http_info["body"] = body
        http_info["response_headers"] = response_headers

        return http_info

    def show_checkpoint_async(self, request):
        r"""查询Checkpoint详情

        本接口用于查询Checkpoint详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowCheckpoint
        :type request: :class:`huaweicloudsdkdis.v2.ShowCheckpointRequest`
        :rtype: :class:`huaweicloudsdkdis.v2.ShowCheckpointResponse`
        """
        http_info = self._show_checkpoint_http_info(request)
        return self._call_api(**http_info)

    def show_checkpoint_async_invoker(self, request):
        http_info = self._show_checkpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_checkpoint_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/checkpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ShowCheckpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'stream_name' in local_var_params:
            query_params.append(('stream_name', local_var_params['stream_name']))
        if 'partition_id' in local_var_params:
            query_params.append(('partition_id', local_var_params['partition_id']))
        if 'app_name' in local_var_params:
            query_params.append(('app_name', local_var_params['app_name']))
        if 'checkpoint_type' in local_var_params:
            query_params.append(('checkpoint_type', local_var_params['checkpoint_type']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = ['aksk']

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

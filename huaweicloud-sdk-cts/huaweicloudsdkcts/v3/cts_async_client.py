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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkcts'")


class CtsAsyncClient(Client):
    def __init__(self):
        super(CtsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkcts.v3.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "CtsAsyncClient":
                raise TypeError("client type error, support client type is CtsAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def batch_create_resource_tags_async(self, request):
        """批量添加CTS资源标签

        批量添加CTS资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateResourceTags
        :type request: :class:`huaweicloudsdkcts.v3.BatchCreateResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.BatchCreateResourceTagsResponse`
        """
        http_info = self._batch_create_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_resource_tags_async_invoker(self, request):
        http_info = self._batch_create_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/{resource_type}/{resource_id}/tags/create",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def batch_delete_resource_tags_async(self, request):
        """批量删除CTS资源标签

        批量删除CTS资源标签。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteResourceTags
        :type request: :class:`huaweicloudsdkcts.v3.BatchDeleteResourceTagsRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.BatchDeleteResourceTagsResponse`
        """
        http_info = self._batch_delete_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_resource_tags_async_invoker(self, request):
        http_info = self._batch_delete_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_resource_tags_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/{resource_type}/{resource_id}/tags/delete",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def check_obs_buckets_async(self, request):
        """检查已经配置OBS桶是否可以成功转储

        检查已经配置OBS桶是否可以成功转储。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckObsBuckets
        :type request: :class:`huaweicloudsdkcts.v3.CheckObsBucketsRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.CheckObsBucketsResponse`
        """
        http_info = self._check_obs_buckets_http_info(request)
        return self._call_api(**http_info)

    def check_obs_buckets_async_invoker(self, request):
        http_info = self._check_obs_buckets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_obs_buckets_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{domain_id}/checkbucket",
            "request_type": request.__class__.__name__,
            "response_type": "CheckObsBucketsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def create_notification_async(self, request):
        """创建关键操作通知

        配置关键操作通知，可在发生特定操作时，使用预先创建好的SMN主题，向用户手机、邮箱发送消息，也可直接发送http/https消息。常用于实时感知高危操作、触发特定操作或对接用户自有审计分析系统。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNotification
        :type request: :class:`huaweicloudsdkcts.v3.CreateNotificationRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.CreateNotificationResponse`
        """
        http_info = self._create_notification_http_info(request)
        return self._call_api(**http_info)

    def create_notification_async_invoker(self, request):
        http_info = self._create_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notification_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotificationResponse"
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

    def create_tracker_async(self, request):
        """创建追踪器

        云审计服务开通后系统会自动创建一个追踪器，用来关联系统记录的所有操作。目前，一个云账户在一个Region下支持创建一个管理类追踪器和多个数据类追踪器。
        云审计服务支持在管理控制台查询近7天内的操作记录。如需保存更长时间的操作记录，您可以在创建追踪器之后通过对象存储服务（Object Storage Service，以下简称OBS）将操作记录实时保存至OBS桶中。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTracker
        :type request: :class:`huaweicloudsdkcts.v3.CreateTrackerRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.CreateTrackerResponse`
        """
        http_info = self._create_tracker_http_info(request)
        return self._call_api(**http_info)

    def create_tracker_async_invoker(self, request):
        http_info = self._create_tracker_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_tracker_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v3/{project_id}/tracker",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTrackerResponse"
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

    def delete_notification_async(self, request):
        """删除关键操作通知

        云审计服务支持删除已创建的关键操作通知。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNotification
        :type request: :class:`huaweicloudsdkcts.v3.DeleteNotificationRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.DeleteNotificationResponse`
        """
        http_info = self._delete_notification_http_info(request)
        return self._call_api(**http_info)

    def delete_notification_async_invoker(self, request):
        http_info = self._delete_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notification_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotificationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'notification_id' in local_var_params:
            query_params.append(('notification_id', local_var_params['notification_id']))

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

    def delete_tracker_async(self, request):
        """删除追踪器

        云审计服务目前仅支持删除已创建的数据类追踪器。删除追踪器对已有的操作记录没有影响，当您重新开通云审计服务后，依旧可以查看已有的操作记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTracker
        :type request: :class:`huaweicloudsdkcts.v3.DeleteTrackerRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.DeleteTrackerResponse`
        """
        http_info = self._delete_tracker_http_info(request)
        return self._call_api(**http_info)

    def delete_tracker_async_invoker(self, request):
        http_info = self._delete_tracker_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_tracker_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v3/{project_id}/trackers",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTrackerResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tracker_name' in local_var_params:
            query_params.append(('tracker_name', local_var_params['tracker_name']))
        if 'tracker_type' in local_var_params:
            query_params.append(('tracker_type', local_var_params['tracker_type']))

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

    def list_notifications_async(self, request):
        """查询关键操作通知

        查询创建的关键操作通知规则。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListNotifications
        :type request: :class:`huaweicloudsdkcts.v3.ListNotificationsRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListNotificationsResponse`
        """
        http_info = self._list_notifications_http_info(request)
        return self._call_api(**http_info)

    def list_notifications_async_invoker(self, request):
        http_info = self._list_notifications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_notifications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/notifications/{notification_type}",
            "request_type": request.__class__.__name__,
            "response_type": "ListNotificationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'notification_type' in local_var_params:
            path_params['notification_type'] = local_var_params['notification_type']

        query_params = []
        if 'notification_name' in local_var_params:
            query_params.append(('notification_name', local_var_params['notification_name']))

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

    def list_operations_async(self, request):
        """查询云服务的全量操作列表

        查询云服务的全量操作列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListOperations
        :type request: :class:`huaweicloudsdkcts.v3.ListOperationsRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListOperationsResponse`
        """
        http_info = self._list_operations_http_info(request)
        return self._call_api(**http_info)

    def list_operations_async_invoker(self, request):
        http_info = self._list_operations_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_operations_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/operations",
            "request_type": request.__class__.__name__,
            "response_type": "ListOperationsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))

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
        """查询租户追踪器配额信息

        查询租户追踪器配额信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkcts.v3.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/quotas",
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

    def list_trace_resources_async(self, request):
        """查询事件的资源类型列表

        查询事件的资源类型列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTraceResources
        :type request: :class:`huaweicloudsdkcts.v3.ListTraceResourcesRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListTraceResourcesResponse`
        """
        http_info = self._list_trace_resources_http_info(request)
        return self._call_api(**http_info)

    def list_trace_resources_async_invoker(self, request):
        http_info = self._list_trace_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_trace_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{domain_id}/resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListTraceResourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'domain_id' in local_var_params:
            path_params['domain_id'] = local_var_params['domain_id']

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

    def list_traces_async(self, request):
        """查询事件列表

        通过事件列表查询接口，可以查出系统记录的7天内资源操作记录。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTraces
        :type request: :class:`huaweicloudsdkcts.v3.ListTracesRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListTracesResponse`
        """
        http_info = self._list_traces_http_info(request)
        return self._call_api(**http_info)

    def list_traces_async_invoker(self, request):
        http_info = self._list_traces_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_traces_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/traces",
            "request_type": request.__class__.__name__,
            "response_type": "ListTracesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'trace_type' in local_var_params:
            query_params.append(('trace_type', local_var_params['trace_type']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if '_from' in local_var_params:
            query_params.append(('from', local_var_params['_from']))
        if 'next' in local_var_params:
            query_params.append(('next', local_var_params['next']))
        if 'to' in local_var_params:
            query_params.append(('to', local_var_params['to']))
        if 'tracker_name' in local_var_params:
            query_params.append(('tracker_name', local_var_params['tracker_name']))
        if 'service_type' in local_var_params:
            query_params.append(('service_type', local_var_params['service_type']))
        if 'user' in local_var_params:
            query_params.append(('user', local_var_params['user']))
        if 'resource_id' in local_var_params:
            query_params.append(('resource_id', local_var_params['resource_id']))
        if 'resource_name' in local_var_params:
            query_params.append(('resource_name', local_var_params['resource_name']))
        if 'resource_type' in local_var_params:
            query_params.append(('resource_type', local_var_params['resource_type']))
        if 'trace_id' in local_var_params:
            query_params.append(('trace_id', local_var_params['trace_id']))
        if 'trace_name' in local_var_params:
            query_params.append(('trace_name', local_var_params['trace_name']))
        if 'trace_rating' in local_var_params:
            query_params.append(('trace_rating', local_var_params['trace_rating']))

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

    def list_trackers_async(self, request):
        """查询追踪器

        开通云审计服务成功后，您可以在追踪器信息页面查看追踪器的详细信息。详细信息主要包括追踪器名称，用于存储操作事件的OBS桶名称和OBS桶中的事件文件前缀。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTrackers
        :type request: :class:`huaweicloudsdkcts.v3.ListTrackersRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListTrackersResponse`
        """
        http_info = self._list_trackers_http_info(request)
        return self._call_api(**http_info)

    def list_trackers_async_invoker(self, request):
        http_info = self._list_trackers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_trackers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/trackers",
            "request_type": request.__class__.__name__,
            "response_type": "ListTrackersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tracker_name' in local_var_params:
            query_params.append(('tracker_name', local_var_params['tracker_name']))
        if 'tracker_type' in local_var_params:
            query_params.append(('tracker_type', local_var_params['tracker_type']))

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

    def list_user_resources_async(self, request):
        """查询30天事件的操作用户列表

        查询30天事件的操作用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListUserResources
        :type request: :class:`huaweicloudsdkcts.v3.ListUserResourcesRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.ListUserResourcesResponse`
        """
        http_info = self._list_user_resources_http_info(request)
        return self._call_api(**http_info)

    def list_user_resources_async_invoker(self, request):
        http_info = self._list_user_resources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_user_resources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v3/{project_id}/user-resources",
            "request_type": request.__class__.__name__,
            "response_type": "ListUserResourcesResponse"
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

    def update_notification_async(self, request):
        """修改关键操作通知

        云审计服务支持修改已创建关键操作通知配置项，通过notification_id的字段匹配修改对象，notification_id必须已经存在。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotification
        :type request: :class:`huaweicloudsdkcts.v3.UpdateNotificationRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.UpdateNotificationResponse`
        """
        http_info = self._update_notification_http_info(request)
        return self._call_api(**http_info)

    def update_notification_async_invoker(self, request):
        http_info = self._update_notification_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notification_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/notifications",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotificationResponse"
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

    def update_tracker_async(self, request):
        """修改追踪器

        云审计服务支持修改已创建追踪器的配置项，包括OBS桶转储、关键事件通知、事件转储加密、通过LTS对管理类事件进行检索、事件文件完整性校验以及追踪器启停状态等相关参数，修改追踪器对已有的操作记录没有影响。修改追踪器完成后，系统立即以新的规则开始记录操作。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTracker
        :type request: :class:`huaweicloudsdkcts.v3.UpdateTrackerRequest`
        :rtype: :class:`huaweicloudsdkcts.v3.UpdateTrackerResponse`
        """
        http_info = self._update_tracker_http_info(request)
        return self._call_api(**http_info)

    def update_tracker_async_invoker(self, request):
        http_info = self._update_tracker_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_tracker_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v3/{project_id}/tracker",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTrackerResponse"
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

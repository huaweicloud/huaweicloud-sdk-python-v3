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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdkeg'")


class EgAsyncClient(Client):
    def __init__(self):
        super(EgAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkeg.v1.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "EgAsyncClient":
                raise TypeError("client type error, support client type is EgAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def check_put_events_async(self, request):
        """预校验指定事件源发布事件成功

        发布事件到事件源成功需要有订阅等条件，预先校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CheckPutEvents
        :type request: :class:`huaweicloudsdkeg.v1.CheckPutEventsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CheckPutEventsResponse`
        """
        http_info = self._check_put_events_http_info(request)
        return self._call_api(**http_info)

    def check_put_events_async_invoker(self, request):
        http_info = self._check_put_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _check_put_events_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/events/check",
            "request_type": request.__class__.__name__,
            "response_type": "CheckPutEventsResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_agencies_async(self, request):
        """创建服务委托

        按照业务场景，一键创建服务委托授权。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateAgencies
        :type request: :class:`huaweicloudsdkeg.v1.CreateAgenciesRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateAgenciesResponse`
        """
        http_info = self._create_agencies_http_info(request)
        return self._call_api(**http_info)

    def create_agencies_async_invoker(self, request):
        http_info = self._create_agencies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_agencies_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/service-agencies",
            "request_type": request.__class__.__name__,
            "response_type": "CreateAgenciesResponse"
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

    def create_channel_async(self, request):
        """创建自定义事件通道

        创建自定义事件通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateChannel
        :type request: :class:`huaweicloudsdkeg.v1.CreateChannelRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateChannelResponse`
        """
        http_info = self._create_channel_http_info(request)
        return self._call_api(**http_info)

    def create_channel_async_invoker(self, request):
        http_info = self._create_channel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_channel_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/channels",
            "request_type": request.__class__.__name__,
            "response_type": "CreateChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_connection_async(self, request):
        """创建目标连接

        创建目标连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateConnection
        :type request: :class:`huaweicloudsdkeg.v1.CreateConnectionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateConnectionResponse`
        """
        http_info = self._create_connection_http_info(request)
        return self._call_api(**http_info)

    def create_connection_async_invoker(self, request):
        http_info = self._create_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_connection_http_info(self, request):
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

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def create_endpoint_async(self, request):
        """创建访问端点

        创建访问端点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEndpoint
        :type request: :class:`huaweicloudsdkeg.v1.CreateEndpointRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateEndpointResponse`
        """
        http_info = self._create_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_endpoint_async_invoker(self, request):
        http_info = self._create_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEndpointResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_event_source_async(self, request):
        """创建自定义事件源

        创建用户自定义类型的事件源，只能指定自定义通道，不能指定系统通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEventSource
        :type request: :class:`huaweicloudsdkeg.v1.CreateEventSourceRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateEventSourceResponse`
        """
        http_info = self._create_event_source_http_info(request)
        return self._call_api(**http_info)

    def create_event_source_async_invoker(self, request):
        http_info = self._create_event_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_event_source_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/sources",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEventSourceResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_event_streaming_async(self, request):
        """创建事件流

        创建事件流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateEventStreaming
        :type request: :class:`huaweicloudsdkeg.v1.CreateEventStreamingRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateEventStreamingResponse`
        """
        http_info = self._create_event_streaming_http_info(request)
        return self._call_api(**http_info)

    def create_event_streaming_async_invoker(self, request):
        http_info = self._create_event_streaming_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_event_streaming_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eventstreamings",
            "request_type": request.__class__.__name__,
            "response_type": "CreateEventStreamingResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_subscription_async(self, request):
        """创建事件订阅

        创建事件订阅。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubscription
        :type request: :class:`huaweicloudsdkeg.v1.CreateSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateSubscriptionResponse`
        """
        http_info = self._create_subscription_http_info(request)
        return self._call_api(**http_info)

    def create_subscription_async_invoker(self, request):
        http_info = self._create_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_subscription_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/subscriptions",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubscriptionResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def create_subscription_target_async(self, request):
        """创建事件订阅目标

        创建单个事件订阅目标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateSubscriptionTarget
        :type request: :class:`huaweicloudsdkeg.v1.CreateSubscriptionTargetRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.CreateSubscriptionTargetResponse`
        """
        http_info = self._create_subscription_target_http_info(request)
        return self._call_api(**http_info)

    def create_subscription_target_async_invoker(self, request):
        http_info = self._create_subscription_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_subscription_target_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}/targets",
            "request_type": request.__class__.__name__,
            "response_type": "CreateSubscriptionTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def delete_channel_async(self, request):
        """删除自定义事件通道

        删除指定自定义事件通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteChannel
        :type request: :class:`huaweicloudsdkeg.v1.DeleteChannelRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteChannelResponse`
        """
        http_info = self._delete_channel_http_info(request)
        return self._call_api(**http_info)

    def delete_channel_async_invoker(self, request):
        http_info = self._delete_channel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_channel_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/channels/{channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def delete_connection_async(self, request):
        """删除目标连接

        删除目标连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteConnection
        :type request: :class:`huaweicloudsdkeg.v1.DeleteConnectionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteConnectionResponse`
        """
        http_info = self._delete_connection_http_info(request)
        return self._call_api(**http_info)

    def delete_connection_async_invoker(self, request):
        http_info = self._delete_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_connection_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def delete_endpoint_async(self, request):
        """删除访问端点

        删除访问端点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEndpoint
        :type request: :class:`huaweicloudsdkeg.v1.DeleteEndpointRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteEndpointResponse`
        """
        http_info = self._delete_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_endpoint_async_invoker(self, request):
        http_info = self._delete_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def delete_event_source_async(self, request):
        """删除自定义事件源

        删除指定的自定义事件源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEventSource
        :type request: :class:`huaweicloudsdkeg.v1.DeleteEventSourceRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteEventSourceResponse`
        """
        http_info = self._delete_event_source_http_info(request)
        return self._call_api(**http_info)

    def delete_event_source_async_invoker(self, request):
        http_info = self._delete_event_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_event_source_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEventSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def delete_event_streaming_async(self, request):
        """删除事件流

        删除事件流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteEventStreaming
        :type request: :class:`huaweicloudsdkeg.v1.DeleteEventStreamingRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteEventStreamingResponse`
        """
        http_info = self._delete_event_streaming_http_info(request)
        return self._call_api(**http_info)

    def delete_event_streaming_async_invoker(self, request):
        http_info = self._delete_event_streaming_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_event_streaming_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/eventstreamings/{eventstreaming_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteEventStreamingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eventstreaming_id' in local_var_params:
            path_params['eventstreaming_id'] = local_var_params['eventstreaming_id']

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

    def delete_subscription_async(self, request):
        """删除事件订阅

        删除事件订阅。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubscription
        :type request: :class:`huaweicloudsdkeg.v1.DeleteSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteSubscriptionResponse`
        """
        http_info = self._delete_subscription_http_info(request)
        return self._call_api(**http_info)

    def delete_subscription_async_invoker(self, request):
        http_info = self._delete_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_subscription_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

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

    def delete_subscription_target_async(self, request):
        """删除事件订阅目标

        删除事件订阅目标。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteSubscriptionTarget
        :type request: :class:`huaweicloudsdkeg.v1.DeleteSubscriptionTargetRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.DeleteSubscriptionTargetResponse`
        """
        http_info = self._delete_subscription_target_http_info(request)
        return self._call_api(**http_info)

    def delete_subscription_target_async_invoker(self, request):
        http_info = self._delete_subscription_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_subscription_target_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteSubscriptionTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

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

    def list_agencies_async(self, request):
        """查询服务委托

        查询服务委托。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListAgencies
        :type request: :class:`huaweicloudsdkeg.v1.ListAgenciesRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListAgenciesResponse`
        """
        http_info = self._list_agencies_http_info(request)
        return self._call_api(**http_info)

    def list_agencies_async_invoker(self, request):
        http_info = self._list_agencies_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_agencies_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/service-agencies",
            "request_type": request.__class__.__name__,
            "response_type": "ListAgenciesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_channels_async(self, request):
        """查询事件通道列表

        查询事件通道列表，包括系统通道和自定义通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListChannels
        :type request: :class:`huaweicloudsdkeg.v1.ListChannelsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListChannelsResponse`
        """
        http_info = self._list_channels_http_info(request)
        return self._call_api(**http_info)

    def list_channels_async_invoker(self, request):
        http_info = self._list_channels_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_channels_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/channels",
            "request_type": request.__class__.__name__,
            "response_type": "ListChannelsResponse"
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
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'provider_type' in local_var_params:
            query_params.append(('provider_type', local_var_params['provider_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))
        if 'eps_id' in local_var_params:
            query_params.append(('eps_id', local_var_params['eps_id']))

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

    def list_connections_async(self, request):
        """查询目标连接列表

        查询目标连接列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListConnections
        :type request: :class:`huaweicloudsdkeg.v1.ListConnectionsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListConnectionsResponse`
        """
        http_info = self._list_connections_http_info(request)
        return self._call_api(**http_info)

    def list_connections_async_invoker(self, request):
        http_info = self._list_connections_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_connections_http_info(self, request):
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
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))
        if 'instance_id' in local_var_params:
            query_params.append(('instance_id', local_var_params['instance_id']))

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

    def list_endpoints_async(self, request):
        """查询访问端点

        查询访问端点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEndpoints
        :type request: :class:`huaweicloudsdkeg.v1.ListEndpointsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListEndpointsResponse`
        """
        http_info = self._list_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_endpoints_async_invoker(self, request):
        http_info = self._list_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListEndpointsResponse"
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
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))
        if 'subnet_id' in local_var_params:
            query_params.append(('subnet_id', local_var_params['subnet_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_event_sources_async(self, request):
        """查询事件源列表

        支持条件查询，如可以指定事件通道ID来查询某个事件通道下的所有事件源。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventSources
        :type request: :class:`huaweicloudsdkeg.v1.ListEventSourcesRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListEventSourcesResponse`
        """
        http_info = self._list_event_sources_http_info(request)
        return self._call_api(**http_info)

    def list_event_sources_async_invoker(self, request):
        http_info = self._list_event_sources_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_sources_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sources",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventSourcesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'provider_type' in local_var_params:
            query_params.append(('provider_type', local_var_params['provider_type']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))
        if 'fuzzy_label' in local_var_params:
            query_params.append(('fuzzy_label', local_var_params['fuzzy_label']))

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

    def list_event_streaming_async(self, request):
        """查询事件流列表

        查询事件流列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventStreaming
        :type request: :class:`huaweicloudsdkeg.v1.ListEventStreamingRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListEventStreamingResponse`
        """
        http_info = self._list_event_streaming_http_info(request)
        return self._call_api(**http_info)

    def list_event_streaming_async_invoker(self, request):
        http_info = self._list_event_streaming_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_streaming_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eventstreamings",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventStreamingResponse"
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
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_event_target_async(self, request):
        """查询事件目标分类

        查询预置的事件目标分类，获取每个事件目标分类的字段定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListEventTarget
        :type request: :class:`huaweicloudsdkeg.v1.ListEventTargetRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListEventTargetResponse`
        """
        http_info = self._list_event_target_http_info(request)
        return self._call_api(**http_info)

    def list_event_target_async_invoker(self, request):
        http_info = self._list_event_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_event_target_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/target-catalogs",
            "request_type": request.__class__.__name__,
            "response_type": "ListEventTargetResponse"
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
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'fuzzy_label' in local_var_params:
            query_params.append(('fuzzy_label', local_var_params['fuzzy_label']))
        if 'support_types' in local_var_params:
            query_params.append(('support_types', local_var_params['support_types']))
            collection_formats['support_types'] = 'csv'

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

    def list_pub_metrics_async(self, request):
        """查询事件通道监控指标数据

        查询事件通道监控指标数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListPubMetrics
        :type request: :class:`huaweicloudsdkeg.v1.ListPubMetricsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListPubMetricsResponse`
        """
        http_info = self._list_pub_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_pub_metrics_async_invoker(self, request):
        http_info = self._list_pub_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_pub_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/metrics/pub",
            "request_type": request.__class__.__name__,
            "response_type": "ListPubMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))
        if 'provider_type' in local_var_params:
            query_params.append(('provider_type', local_var_params['provider_type']))
        if 'source_name' in local_var_params:
            query_params.append(('source_name', local_var_params['source_name']))

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
        """查询配额

        查询当前租户的配额，未特殊配置过的会返回默认配额。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListQuotas
        :type request: :class:`huaweicloudsdkeg.v1.ListQuotasRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListQuotasResponse`
        """
        http_info = self._list_quotas_http_info(request)
        return self._call_api(**http_info)

    def list_quotas_async_invoker(self, request):
        http_info = self._list_quotas_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_quotas_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/quotas",
            "request_type": request.__class__.__name__,
            "response_type": "ListQuotasResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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

    def list_sub_metrics_async(self, request):
        """查询事件订阅监控指标数据

        查询事件订阅监控指标数据。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubMetrics
        :type request: :class:`huaweicloudsdkeg.v1.ListSubMetricsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListSubMetricsResponse`
        """
        http_info = self._list_sub_metrics_http_info(request)
        return self._call_api(**http_info)

    def list_sub_metrics_async_invoker(self, request):
        http_info = self._list_sub_metrics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_sub_metrics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/metrics/sub",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubMetricsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'period' in local_var_params:
            query_params.append(('period', local_var_params['period']))
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'subscription_id' in local_var_params:
            query_params.append(('subscription_id', local_var_params['subscription_id']))
        if 'provider_type' in local_var_params:
            query_params.append(('provider_type', local_var_params['provider_type']))
        if 'target_id' in local_var_params:
            query_params.append(('target_id', local_var_params['target_id']))

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

    def list_subscriptions_async(self, request):
        """查询事件订阅列表

        查询事件订阅列表，支持指定事件通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubscriptions
        :type request: :class:`huaweicloudsdkeg.v1.ListSubscriptionsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListSubscriptionsResponse`
        """
        http_info = self._list_subscriptions_http_info(request)
        return self._call_api(**http_info)

    def list_subscriptions_async_invoker(self, request):
        http_info = self._list_subscriptions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_subscriptions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscriptions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubscriptionsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))
        if 'connection_id' in local_var_params:
            query_params.append(('connection_id', local_var_params['connection_id']))

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

    def list_traced_events_async(self, request):
        """查询事件追踪列表

        查询事件追踪列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTracedEvents
        :type request: :class:`huaweicloudsdkeg.v1.ListTracedEventsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListTracedEventsResponse`
        """
        http_info = self._list_traced_events_http_info(request)
        return self._call_api(**http_info)

    def list_traced_events_async_invoker(self, request):
        http_info = self._list_traced_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_traced_events_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/traced-events",
            "request_type": request.__class__.__name__,
            "response_type": "ListTracedEventsResponse"
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
        if 'event_id' in local_var_params:
            query_params.append(('event_id', local_var_params['event_id']))
        if 'source_name' in local_var_params:
            query_params.append(('source_name', local_var_params['source_name']))
        if 'event_type' in local_var_params:
            query_params.append(('event_type', local_var_params['event_type']))
        if 'subscription_name' in local_var_params:
            query_params.append(('subscription_name', local_var_params['subscription_name']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_triggers_async(self, request):
        """查询单个函数的EG触发器

        查询触发器，支持指定函数urn，一个以函数urn为目标的订阅为一个触发器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTriggers
        :type request: :class:`huaweicloudsdkeg.v1.ListTriggersRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListTriggersResponse`
        """
        http_info = self._list_triggers_http_info(request)
        return self._call_api(**http_info)

    def list_triggers_async_invoker(self, request):
        http_info = self._list_triggers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_triggers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscription-triggers/{func_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTriggersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'func_urn' in local_var_params:
            path_params['func_urn'] = local_var_params['func_urn']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

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

    def list_workflow_triggers_async(self, request):
        """查询单个函数流的EG触发器

        查询触发器，支持指定函数流id，一个以函数流id为目标的订阅为一个触发器。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListWorkflowTriggers
        :type request: :class:`huaweicloudsdkeg.v1.ListWorkflowTriggersRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListWorkflowTriggersResponse`
        """
        http_info = self._list_workflow_triggers_http_info(request)
        return self._call_api(**http_info)

    def list_workflow_triggers_async_invoker(self, request):
        http_info = self._list_workflow_triggers_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_workflow_triggers_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscription-triggers/workflow/{workflow_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListWorkflowTriggersResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'workflow_id' in local_var_params:
            path_params['workflow_id'] = local_var_params['workflow_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

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

    def operate_subscription_async(self, request):
        """操作事件订阅

        操作事件订阅，支持启用、禁用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for OperateSubscription
        :type request: :class:`huaweicloudsdkeg.v1.OperateSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.OperateSubscriptionResponse`
        """
        http_info = self._operate_subscription_http_info(request)
        return self._call_api(**http_info)

    def operate_subscription_async_invoker(self, request):
        http_info = self._operate_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _operate_subscription_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/subscriptions/operation",
            "request_type": request.__class__.__name__,
            "response_type": "OperateSubscriptionResponse"
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

        response_headers = ["X-Request-Id", ]

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

    def put_events_async(self, request):
        """发布事件到事件通道

        发布事件到事件通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PutEvents
        :type request: :class:`huaweicloudsdkeg.v1.PutEventsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.PutEventsResponse`
        """
        http_info = self._put_events_http_info(request)
        return self._call_api(**http_info)

    def put_events_async_invoker(self, request):
        http_info = self._put_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _put_events_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/channels/{channel_id}/events",
            "request_type": request.__class__.__name__,
            "response_type": "PutEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def put_official_events_async(self, request):
        """发布官方事件到事件通道

        发布官方事件到事件通道。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PutOfficialEvents
        :type request: :class:`huaweicloudsdkeg.v1.PutOfficialEventsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.PutOfficialEventsResponse`
        """
        http_info = self._put_official_events_http_info(request)
        return self._call_api(**http_info)

    def put_official_events_async_invoker(self, request):
        http_info = self._put_official_events_http_info(request)
        return AsyncInvoker(self, http_info)

    def _put_official_events_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/official/sources/{source_name}/events",
            "request_type": request.__class__.__name__,
            "response_type": "PutOfficialEventsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_name' in local_var_params:
            path_params['source_name'] = local_var_params['source_name']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def resume_event_streaming_async(self, request):
        """操作事件流

        操作事件流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ResumeEventStreaming
        :type request: :class:`huaweicloudsdkeg.v1.ResumeEventStreamingRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ResumeEventStreamingResponse`
        """
        http_info = self._resume_event_streaming_http_info(request)
        return self._call_api(**http_info)

    def resume_event_streaming_async_invoker(self, request):
        http_info = self._resume_event_streaming_http_info(request)
        return AsyncInvoker(self, http_info)

    def _resume_event_streaming_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v1/{project_id}/eventstreamings/operate/{eventstreaming_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ResumeEventStreamingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eventstreaming_id' in local_var_params:
            path_params['eventstreaming_id'] = local_var_params['eventstreaming_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def show_detail_of_channel_async(self, request):
        """查询事件通道详情

        查询指定事件通道详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfChannel
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfChannelRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfChannelResponse`
        """
        http_info = self._show_detail_of_channel_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_channel_async_invoker(self, request):
        http_info = self._show_detail_of_channel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_channel_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/channels/{channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

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

    def show_detail_of_connection_async(self, request):
        """查询目标连接详情

        查询目标连接详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfConnection
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfConnectionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfConnectionResponse`
        """
        http_info = self._show_detail_of_connection_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_connection_async_invoker(self, request):
        http_info = self._show_detail_of_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_connection_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

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

    def show_detail_of_event_async(self, request):
        """查询发送事件的内容

        根据事件ID查询事件详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfEvent
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfEventRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfEventResponse`
        """
        http_info = self._show_detail_of_event_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_event_async_invoker(self, request):
        http_info = self._show_detail_of_event_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_event_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/events/detail/{trace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfEventResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'trace_id' in local_var_params:
            path_params['trace_id'] = local_var_params['trace_id']

        query_params = []
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))

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

    def show_detail_of_event_source_async(self, request):
        """查询事件源详情

        查询事件源详情信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfEventSource
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfEventSourceRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfEventSourceResponse`
        """
        http_info = self._show_detail_of_event_source_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_event_source_async_invoker(self, request):
        http_info = self._show_detail_of_event_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_event_source_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfEventSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

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

    def show_detail_of_event_trace_async(self, request):
        """事件轨迹详情

        事件轨迹详情，展示事件源到投递目标的投递情况。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfEventTrace
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfEventTraceRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfEventTraceResponse`
        """
        http_info = self._show_detail_of_event_trace_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_event_trace_async_invoker(self, request):
        http_info = self._show_detail_of_event_trace_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_event_trace_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/events/trace/detail/{trace_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfEventTraceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'trace_id' in local_var_params:
            path_params['trace_id'] = local_var_params['trace_id']

        query_params = []
        if 'channel_id' in local_var_params:
            query_params.append(('channel_id', local_var_params['channel_id']))

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

    def show_detail_of_subscription_async(self, request):
        """查询事件订阅详情

        查询事件订阅详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfSubscription
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfSubscriptionResponse`
        """
        http_info = self._show_detail_of_subscription_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_subscription_async_invoker(self, request):
        http_info = self._show_detail_of_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_subscription_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

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

    def show_detail_of_subscription_target_async(self, request):
        """查询事件订阅目标详情

        查询事件订阅目标详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowDetailOfSubscriptionTarget
        :type request: :class:`huaweicloudsdkeg.v1.ShowDetailOfSubscriptionTargetRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowDetailOfSubscriptionTargetResponse`
        """
        http_info = self._show_detail_of_subscription_target_http_info(request)
        return self._call_api(**http_info)

    def show_detail_of_subscription_target_async_invoker(self, request):
        http_info = self._show_detail_of_subscription_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_detail_of_subscription_target_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowDetailOfSubscriptionTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

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

    def show_event_streaming_async(self, request):
        """查询事件流详情

        查询事件流详情。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowEventStreaming
        :type request: :class:`huaweicloudsdkeg.v1.ShowEventStreamingRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ShowEventStreamingResponse`
        """
        http_info = self._show_event_streaming_http_info(request)
        return self._call_api(**http_info)

    def show_event_streaming_async_invoker(self, request):
        http_info = self._show_event_streaming_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_event_streaming_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/eventstreamings/{eventstreaming_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowEventStreamingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eventstreaming_id' in local_var_params:
            path_params['eventstreaming_id'] = local_var_params['eventstreaming_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_channel_async(self, request):
        """更新自定义事件通道

        更新自定义事件通道定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateChannel
        :type request: :class:`huaweicloudsdkeg.v1.UpdateChannelRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateChannelResponse`
        """
        http_info = self._update_channel_http_info(request)
        return self._call_api(**http_info)

    def update_channel_async_invoker(self, request):
        http_info = self._update_channel_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_channel_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/channels/{channel_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateChannelResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'channel_id' in local_var_params:
            path_params['channel_id'] = local_var_params['channel_id']

        query_params = []
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_connection_async(self, request):
        """更新目标连接

        更新目标连接。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateConnection
        :type request: :class:`huaweicloudsdkeg.v1.UpdateConnectionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateConnectionResponse`
        """
        http_info = self._update_connection_http_info(request)
        return self._call_api(**http_info)

    def update_connection_async_invoker(self, request):
        http_info = self._update_connection_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_connection_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/connections/{connection_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateConnectionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'connection_id' in local_var_params:
            path_params['connection_id'] = local_var_params['connection_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_endpoint_async(self, request):
        """更新访问端点

        更新访问端点。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEndpoint
        :type request: :class:`huaweicloudsdkeg.v1.UpdateEndpointRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateEndpointResponse`
        """
        http_info = self._update_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_endpoint_async_invoker(self, request):
        http_info = self._update_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/endpoints/{endpoint_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_id' in local_var_params:
            path_params['endpoint_id'] = local_var_params['endpoint_id']

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

    def update_event_source_async(self, request):
        """更新自定义事件源

        更新自定义事件源定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEventSource
        :type request: :class:`huaweicloudsdkeg.v1.UpdateEventSourceRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateEventSourceResponse`
        """
        http_info = self._update_event_source_http_info(request)
        return self._call_api(**http_info)

    def update_event_source_async_invoker(self, request):
        http_info = self._update_event_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_event_source_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEventSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_event_streaming_async(self, request):
        """更新事件流

        更新事件流。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateEventStreaming
        :type request: :class:`huaweicloudsdkeg.v1.UpdateEventStreamingRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateEventStreamingResponse`
        """
        http_info = self._update_event_streaming_http_info(request)
        return self._call_api(**http_info)

    def update_event_streaming_async_invoker(self, request):
        http_info = self._update_event_streaming_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_event_streaming_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/eventstreamings/{eventstreaming_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateEventStreamingResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'eventstreaming_id' in local_var_params:
            path_params['eventstreaming_id'] = local_var_params['eventstreaming_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_subscription_async(self, request):
        """更新事件订阅

        更新事件订阅定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubscription
        :type request: :class:`huaweicloudsdkeg.v1.UpdateSubscriptionRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateSubscriptionResponse`
        """
        http_info = self._update_subscription_http_info(request)
        return self._call_api(**http_info)

    def update_subscription_async_invoker(self, request):
        http_info = self._update_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_subscription_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_subscription_source_async(self, request):
        """更新事件订阅源

        更新事件订阅源定义
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubscriptionSource
        :type request: :class:`huaweicloudsdkeg.v1.UpdateSubscriptionSourceRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateSubscriptionSourceResponse`
        """
        http_info = self._update_subscription_source_http_info(request)
        return self._call_api(**http_info)

    def update_subscription_source_async_invoker(self, request):
        http_info = self._update_subscription_source_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_subscription_source_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}/sources/{source_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubscriptionSourceResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']
        if 'source_id' in local_var_params:
            path_params['source_id'] = local_var_params['source_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def update_subscription_target_async(self, request):
        """更新事件订阅目标

        更新事件订阅目标定义。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubscriptionTarget
        :type request: :class:`huaweicloudsdkeg.v1.UpdateSubscriptionTargetRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.UpdateSubscriptionTargetResponse`
        """
        http_info = self._update_subscription_target_http_info(request)
        return self._call_api(**http_info)

    def update_subscription_target_async_invoker(self, request):
        http_info = self._update_subscription_target_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_subscription_target_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v1/{project_id}/subscriptions/{subscription_id}/targets/{target_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubscriptionTargetResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_id' in local_var_params:
            path_params['subscription_id'] = local_var_params['subscription_id']
        if 'target_id' in local_var_params:
            path_params['target_id'] = local_var_params['target_id']

        query_params = []

        header_params = {}

        form_params = {}

        body = None
        if 'body' in local_var_params:
            body = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body = request.get_file_stream()

        response_headers = ["X-Request-Id", ]

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

    def list_api_versions_async(self, request):
        """获取API版本列表

        获取服务支持的API版本列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApiVersions
        :type request: :class:`huaweicloudsdkeg.v1.ListApiVersionsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListApiVersionsResponse`
        """
        http_info = self._list_api_versions_http_info(request)
        return self._call_api(**http_info)

    def list_api_versions_async_invoker(self, request):
        http_info = self._list_api_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_api_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListApiVersionsResponse"
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

    def list_obs_buckets_async(self, request):
        """获取obs桶列表

        获取obs桶列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListObsBuckets
        :type request: :class:`huaweicloudsdkeg.v1.ListObsBucketsRequest`
        :rtype: :class:`huaweicloudsdkeg.v1.ListObsBucketsResponse`
        """
        http_info = self._list_obs_buckets_http_info(request)
        return self._call_api(**http_info)

    def list_obs_buckets_async_invoker(self, request):
        http_info = self._list_obs_buckets_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_obs_buckets_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v1/{project_id}/subscriptions/obsbuckets",
            "request_type": request.__class__.__name__,
            "response_type": "ListObsBucketsResponse"
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
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))

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

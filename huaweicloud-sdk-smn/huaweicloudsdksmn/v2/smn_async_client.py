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
    warnings.warn(str(e) + ", please check if you are using the same versions of 'huaweicloudsdkcore' and 'huaweicloudsdksmn'")


class SmnAsyncClient(Client):
    def __init__(self):
        super(SmnAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdksmn.v2.model")

    @classmethod
    def new_builder(cls, clazz=None):
        if not clazz:
            client_builder = ClientBuilder(cls)
        else:
            if clazz.__name__ != "SmnAsyncClient":
                raise TypeError("client type error, support client type is SmnAsyncClient")
            client_builder = ClientBuilder(clazz)

        

        return client_builder

    def add_subscription_async(self, request):
        r"""订阅

        为指定Topic添加一个订阅者，如果订阅者的状态为未确认，则向订阅者发送一个确认的消息。待订阅者进行ConfirmSubscription确认后，该订阅者才能收到Topic发布的消息。单Topic默认可添加10000个订阅者，高并发场景下，可能会出现订阅者数量超过10000仍添加成功的情况，此为正常现象。接口是幂等的，如果添加已存在的订阅者，则返回成功，且status code为200，否则status code为201。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSubscription
        :type request: :class:`huaweicloudsdksmn.v2.AddSubscriptionRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.AddSubscriptionResponse`
        """
        http_info = self._add_subscription_http_info(request)
        return self._call_api(**http_info)

    def add_subscription_async_invoker(self, request):
        http_info = self._add_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_subscription_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/subscriptions",
            "request_type": request.__class__.__name__,
            "response_type": "AddSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def add_subscription_from_subscription_user_async(self, request):
        r"""导入订阅

        为指定的Topic添加订阅者，订阅者信息来源为订阅用户列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for AddSubscriptionFromSubscriptionUser
        :type request: :class:`huaweicloudsdksmn.v2.AddSubscriptionFromSubscriptionUserRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.AddSubscriptionFromSubscriptionUserResponse`
        """
        http_info = self._add_subscription_from_subscription_user_http_info(request)
        return self._call_api(**http_info)

    def add_subscription_from_subscription_user_async_invoker(self, request):
        http_info = self._add_subscription_from_subscription_user_http_info(request)
        return AsyncInvoker(self, http_info)

    def _add_subscription_from_subscription_user_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/subscriptions/from-subscription-users",
            "request_type": request.__class__.__name__,
            "response_type": "AddSubscriptionFromSubscriptionUserResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def batch_create_or_delete_resource_tags_async(self, request):
        r"""批量添加删除资源标签

        为指定实例批量添加或删除标签。一个资源上最多有10个标签。
        此接口为幂等接口：创建时如果请求体中存在重复key则报错。
        创建时，不允许重复key，如果数据库存在就覆盖。
        删除时，如果删除的标签不存在，默认处理成功，删除时不对标签字符集范围做校验。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateOrDeleteResourceTags
        :type request: :class:`huaweicloudsdksmn.v2.BatchCreateOrDeleteResourceTagsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.BatchCreateOrDeleteResourceTagsResponse`
        """
        http_info = self._batch_create_or_delete_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def batch_create_or_delete_resource_tags_async_invoker(self, request):
        http_info = self._batch_create_or_delete_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_or_delete_resource_tags_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/action",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateOrDeleteResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def batch_create_subscriptions_filter_polices_async(self, request):
        r"""批量创建订阅过滤策略

        创建订阅者的消息过滤策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchCreateSubscriptionsFilterPolices
        :type request: :class:`huaweicloudsdksmn.v2.BatchCreateSubscriptionsFilterPolicesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.BatchCreateSubscriptionsFilterPolicesResponse`
        """
        http_info = self._batch_create_subscriptions_filter_polices_http_info(request)
        return self._call_api(**http_info)

    def batch_create_subscriptions_filter_polices_async_invoker(self, request):
        http_info = self._batch_create_subscriptions_filter_polices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_create_subscriptions_filter_polices_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/subscriptions/filter_polices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchCreateSubscriptionsFilterPolicesResponse"
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

    def batch_delete_subscriptions_filter_polices_async(self, request):
        r"""批量删除订阅过滤策略

        删除订阅者的消息过滤策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchDeleteSubscriptionsFilterPolices
        :type request: :class:`huaweicloudsdksmn.v2.BatchDeleteSubscriptionsFilterPolicesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.BatchDeleteSubscriptionsFilterPolicesResponse`
        """
        http_info = self._batch_delete_subscriptions_filter_polices_http_info(request)
        return self._call_api(**http_info)

    def batch_delete_subscriptions_filter_polices_async_invoker(self, request):
        http_info = self._batch_delete_subscriptions_filter_polices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_delete_subscriptions_filter_polices_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/subscriptions/filter_polices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchDeleteSubscriptionsFilterPolicesResponse"
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

    def batch_update_subscriptions_filter_polices_async(self, request):
        r"""批量更新订阅过滤策略

        更新订阅者的消息过滤策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for BatchUpdateSubscriptionsFilterPolices
        :type request: :class:`huaweicloudsdksmn.v2.BatchUpdateSubscriptionsFilterPolicesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.BatchUpdateSubscriptionsFilterPolicesResponse`
        """
        http_info = self._batch_update_subscriptions_filter_polices_http_info(request)
        return self._call_api(**http_info)

    def batch_update_subscriptions_filter_polices_async_invoker(self, request):
        http_info = self._batch_update_subscriptions_filter_polices_http_info(request)
        return AsyncInvoker(self, http_info)

    def _batch_update_subscriptions_filter_polices_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/subscriptions/filter_polices",
            "request_type": request.__class__.__name__,
            "response_type": "BatchUpdateSubscriptionsFilterPolicesResponse"
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

    def cancel_subscription_async(self, request):
        r"""取消订阅

        删除指定的订阅者。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CancelSubscription
        :type request: :class:`huaweicloudsdksmn.v2.CancelSubscriptionRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CancelSubscriptionResponse`
        """
        http_info = self._cancel_subscription_http_info(request)
        return self._call_api(**http_info)

    def cancel_subscription_async_invoker(self, request):
        http_info = self._cancel_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _cancel_subscription_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/subscriptions/{subscription_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "CancelSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'subscription_urn' in local_var_params:
            path_params['subscription_urn'] = local_var_params['subscription_urn']

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

    def create_logtank_async(self, request):
        r"""绑定云日志

        为指定Topic绑定一个云日志，用于记录主题消息发送状态等信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateLogtank
        :type request: :class:`huaweicloudsdksmn.v2.CreateLogtankRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateLogtankResponse`
        """
        http_info = self._create_logtank_http_info(request)
        return self._call_api(**http_info)

    def create_logtank_async_invoker(self, request):
        http_info = self._create_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_logtank_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/logtanks",
            "request_type": request.__class__.__name__,
            "response_type": "CreateLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def create_message_template_async(self, request):
        r"""创建消息模板

        创建一个模板，用户可以按照模板去发送消息，这样可以减少请求的数据量。
        单用户默认可创建100个消息模板，高并发场景下，可能会出现消息模板数量超过100仍创建成功的情况，此为正常现象。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateMessageTemplate
        :type request: :class:`huaweicloudsdksmn.v2.CreateMessageTemplateRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateMessageTemplateResponse`
        """
        http_info = self._create_message_template_http_info(request)
        return self._call_api(**http_info)

    def create_message_template_async_invoker(self, request):
        http_info = self._create_message_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_message_template_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/message_template",
            "request_type": request.__class__.__name__,
            "response_type": "CreateMessageTemplateResponse"
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

    def create_notify_policy_async(self, request):
        r"""创建通知策略

        创建通知策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateNotifyPolicy
        :type request: :class:`huaweicloudsdksmn.v2.CreateNotifyPolicyRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateNotifyPolicyResponse`
        """
        http_info = self._create_notify_policy_http_info(request)
        return self._call_api(**http_info)

    def create_notify_policy_async_invoker(self, request):
        http_info = self._create_notify_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_notify_policy_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/notify-policy",
            "request_type": request.__class__.__name__,
            "response_type": "CreateNotifyPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def create_resource_tag_async(self, request):
        r"""添加资源标签

        一个资源上最多有10个标签。此接口为幂等接口：创建时，如果创建的标签已经存在（key相同），则覆盖。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateResourceTag
        :type request: :class:`huaweicloudsdksmn.v2.CreateResourceTagRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateResourceTagResponse`
        """
        http_info = self._create_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def create_resource_tag_async_invoker(self, request):
        http_info = self._create_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_resource_tag_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "CreateResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def create_topic_async(self, request):
        r"""创建主题

        创建Topic，单用户默认配额为3000。高并发场景下，可能会出现Topic数量超过3000仍创建成功的情况，此为正常现象。
        接口是幂等的，接口调用返回成功时，若已存在同名的Topic，返回的status code为200，否则返回的status code为201
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateTopic
        :type request: :class:`huaweicloudsdksmn.v2.CreateTopicRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateTopicResponse`
        """
        http_info = self._create_topic_http_info(request)
        return self._call_api(**http_info)

    def create_topic_async_invoker(self, request):
        http_info = self._create_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_topic_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics",
            "request_type": request.__class__.__name__,
            "response_type": "CreateTopicResponse"
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

    def delete_logtank_async(self, request):
        r"""解绑云日志

        解绑指定Topic绑定的云日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteLogtank
        :type request: :class:`huaweicloudsdksmn.v2.DeleteLogtankRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteLogtankResponse`
        """
        http_info = self._delete_logtank_http_info(request)
        return self._call_api(**http_info)

    def delete_logtank_async_invoker(self, request):
        http_info = self._delete_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_logtank_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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

    def delete_message_template_async(self, request):
        r"""删除消息模板

        删除消息模板。删除模板之前的消息请求都可以使用该模板发送，删除之后无法再使用该模板发送消息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteMessageTemplate
        :type request: :class:`huaweicloudsdksmn.v2.DeleteMessageTemplateRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteMessageTemplateResponse`
        """
        http_info = self._delete_message_template_http_info(request)
        return self._call_api(**http_info)

    def delete_message_template_async_invoker(self, request):
        http_info = self._delete_message_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_message_template_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/message_template/{message_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteMessageTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_template_id' in local_var_params:
            path_params['message_template_id'] = local_var_params['message_template_id']

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

    def delete_notify_policy_async(self, request):
        r"""删除通知策略

        删除通知策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteNotifyPolicy
        :type request: :class:`huaweicloudsdksmn.v2.DeleteNotifyPolicyRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteNotifyPolicyResponse`
        """
        http_info = self._delete_notify_policy_http_info(request)
        return self._call_api(**http_info)

    def delete_notify_policy_async_invoker(self, request):
        http_info = self._delete_notify_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_notify_policy_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/notify-policy/{notify_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteNotifyPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'notify_policy_id' in local_var_params:
            path_params['notify_policy_id'] = local_var_params['notify_policy_id']

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

    def delete_resource_tag_async(self, request):
        r"""删除资源标签

        幂等接口：删除时，不对标签做校验。删除的key不存在报404，key不能为空或者空字符串。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteResourceTag
        :type request: :class:`huaweicloudsdksmn.v2.DeleteResourceTagRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteResourceTagResponse`
        """
        http_info = self._delete_resource_tag_http_info(request)
        return self._call_api(**http_info)

    def delete_resource_tag_async_invoker(self, request):
        http_info = self._delete_resource_tag_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_resource_tag_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteResourceTagResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']
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

    def delete_topic_async(self, request):
        r"""删除主题

        删除主题。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTopic
        :type request: :class:`huaweicloudsdksmn.v2.DeleteTopicRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteTopicResponse`
        """
        http_info = self._delete_topic_http_info(request)
        return self._call_api(**http_info)

    def delete_topic_async_invoker(self, request):
        http_info = self._delete_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_topic_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def delete_topic_attribute_by_name_async(self, request):
        r"""删除指定名称的主题策略

        删除指定名称的主题策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTopicAttributeByName
        :type request: :class:`huaweicloudsdksmn.v2.DeleteTopicAttributeByNameRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteTopicAttributeByNameResponse`
        """
        http_info = self._delete_topic_attribute_by_name_http_info(request)
        return self._call_api(**http_info)

    def delete_topic_attribute_by_name_async_invoker(self, request):
        http_info = self._delete_topic_attribute_by_name_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_topic_attribute_by_name_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/attributes/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTopicAttributeByNameResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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

    def delete_topic_attributes_async(self, request):
        r"""删除所有主题策略

        删除所有主题策略。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteTopicAttributes
        :type request: :class:`huaweicloudsdksmn.v2.DeleteTopicAttributesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteTopicAttributesResponse`
        """
        http_info = self._delete_topic_attributes_http_info(request)
        return self._call_api(**http_info)

    def delete_topic_attributes_async_invoker(self, request):
        http_info = self._delete_topic_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_topic_attributes_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/attributes",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteTopicAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def list_logtank_async(self, request):
        r"""查询云日志

        查询指定Topic绑定的云日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListLogtank
        :type request: :class:`huaweicloudsdksmn.v2.ListLogtankRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListLogtankResponse`
        """
        http_info = self._list_logtank_http_info(request)
        return self._call_api(**http_info)

    def list_logtank_async_invoker(self, request):
        http_info = self._list_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_logtank_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/logtanks",
            "request_type": request.__class__.__name__,
            "response_type": "ListLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def list_message_template_details_async(self, request):
        r"""查询消息模板详情

        查询模板详情，包括模板内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessageTemplateDetails
        :type request: :class:`huaweicloudsdksmn.v2.ListMessageTemplateDetailsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListMessageTemplateDetailsResponse`
        """
        http_info = self._list_message_template_details_http_info(request)
        return self._call_api(**http_info)

    def list_message_template_details_async_invoker(self, request):
        http_info = self._list_message_template_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_template_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/message_template/{message_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageTemplateDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_template_id' in local_var_params:
            path_params['message_template_id'] = local_var_params['message_template_id']

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

    def list_message_templates_async(self, request):
        r"""查询消息模板列表

        分页查询模板列表，模板列表按照创建时间进行升序排列。分页查询可以指定offset以及limit。如果不存在模板，则返回空列表。额外的查询参数分别有message_template_name和protocol。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListMessageTemplates
        :type request: :class:`huaweicloudsdksmn.v2.ListMessageTemplatesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListMessageTemplatesResponse`
        """
        http_info = self._list_message_templates_http_info(request)
        return self._call_api(**http_info)

    def list_message_templates_async_invoker(self, request):
        http_info = self._list_message_templates_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_message_templates_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/message_template",
            "request_type": request.__class__.__name__,
            "response_type": "ListMessageTemplatesResponse"
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
        if 'message_template_name' in local_var_params:
            query_params.append(('message_template_name', local_var_params['message_template_name']))
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))

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

    def list_project_tags_async(self, request):
        r"""查询项目标签

        查询租户在指定Region和实例类型的所有标签集合。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListProjectTags
        :type request: :class:`huaweicloudsdksmn.v2.ListProjectTagsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListProjectTagsResponse`
        """
        http_info = self._list_project_tags_http_info(request)
        return self._call_api(**http_info)

    def list_project_tags_async_invoker(self, request):
        http_info = self._list_project_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_project_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListProjectTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']

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

    def list_resource_instances_async(self, request):
        r"""查询资源实例

        使用标签过滤实例。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceInstances
        :type request: :class:`huaweicloudsdksmn.v2.ListResourceInstancesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListResourceInstancesResponse`
        """
        http_info = self._list_resource_instances_http_info(request)
        return self._call_api(**http_info)

    def list_resource_instances_async_invoker(self, request):
        http_info = self._list_resource_instances_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_instances_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/{resource_type}/resource_instances/action",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceInstancesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
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

    def list_resource_tags_async(self, request):
        r"""查询资源标签

        查询指定实例的标签信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListResourceTags
        :type request: :class:`huaweicloudsdksmn.v2.ListResourceTagsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListResourceTagsResponse`
        """
        http_info = self._list_resource_tags_http_info(request)
        return self._call_api(**http_info)

    def list_resource_tags_async_invoker(self, request):
        http_info = self._list_resource_tags_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_resource_tags_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/{resource_type}/{resource_id}/tags",
            "request_type": request.__class__.__name__,
            "response_type": "ListResourceTagsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'resource_type' in local_var_params:
            path_params['resource_type'] = local_var_params['resource_type']
        if 'resource_id' in local_var_params:
            path_params['resource_id'] = local_var_params['resource_id']

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

    def list_subscriptions_async(self, request):
        r"""查询订阅者列表

        分页返回请求者的所有的订阅列表，订阅列表按照订阅创建时间进行升序排列。分页查询可以指定offset以及limit。如果订阅者不存在，返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubscriptions
        :type request: :class:`huaweicloudsdksmn.v2.ListSubscriptionsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListSubscriptionsResponse`
        """
        http_info = self._list_subscriptions_http_info(request)
        return self._call_api(**http_info)

    def list_subscriptions_async_invoker(self, request):
        http_info = self._list_subscriptions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_subscriptions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/subscriptions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubscriptionsResponse"
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
        if 'protocol' in local_var_params:
            query_params.append(('protocol', local_var_params['protocol']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'endpoint' in local_var_params:
            query_params.append(('endpoint', local_var_params['endpoint']))
        if 'fuzzy_remark' in local_var_params:
            query_params.append(('fuzzy_remark', local_var_params['fuzzy_remark']))

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

    def list_subscriptions_by_topic_async(self, request):
        r"""查询指定Topic的订阅者列表

        分页获取特定Topic的订阅列表，订阅列表按照订阅创建时间进行升序排列。分页查询可以指定offset以及limit。如果指定Topic不存在订阅者，返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListSubscriptionsByTopic
        :type request: :class:`huaweicloudsdksmn.v2.ListSubscriptionsByTopicRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListSubscriptionsByTopicResponse`
        """
        http_info = self._list_subscriptions_by_topic_http_info(request)
        return self._call_api(**http_info)

    def list_subscriptions_by_topic_async_invoker(self, request):
        http_info = self._list_subscriptions_by_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_subscriptions_by_topic_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/subscriptions",
            "request_type": request.__class__.__name__,
            "response_type": "ListSubscriptionsByTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'fuzzy_remark' in local_var_params:
            query_params.append(('fuzzy_remark', local_var_params['fuzzy_remark']))

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

    def list_topic_attributes_async(self, request):
        r"""查询主题策略

        查询主题的策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicAttributes
        :type request: :class:`huaweicloudsdksmn.v2.ListTopicAttributesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListTopicAttributesResponse`
        """
        http_info = self._list_topic_attributes_http_info(request)
        return self._call_api(**http_info)

    def list_topic_attributes_async_invoker(self, request):
        http_info = self._list_topic_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topic_attributes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/attributes",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

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

    def list_topic_details_async(self, request):
        r"""查询主题详情

        查询Topic的详细信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicDetails
        :type request: :class:`huaweicloudsdksmn.v2.ListTopicDetailsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListTopicDetailsResponse`
        """
        http_info = self._list_topic_details_http_info(request)
        return self._call_api(**http_info)

    def list_topic_details_async_invoker(self, request):
        http_info = self._list_topic_details_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topic_details_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicDetailsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def list_topic_message_statistics_async(self, request):
        r"""查询主题的发送详情

        查询Topic的发送数据详情，最多支持查询31天内所有计量数据
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopicMessageStatistics
        :type request: :class:`huaweicloudsdksmn.v2.ListTopicMessageStatisticsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListTopicMessageStatisticsResponse`
        """
        http_info = self._list_topic_message_statistics_http_info(request)
        return self._call_api(**http_info)

    def list_topic_message_statistics_async_invoker(self, request):
        http_info = self._list_topic_message_statistics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topic_message_statistics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/statistics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicMessageStatisticsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

        query_params = []
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

    def list_topics_async(self, request):
        r"""查询主题列表

        分页查询Topic列表，Topic列表按照Topic创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在Topic，则返回空列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListTopics
        :type request: :class:`huaweicloudsdksmn.v2.ListTopicsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListTopicsResponse`
        """
        http_info = self._list_topics_http_info(request)
        return self._call_api(**http_info)

    def list_topics_async_invoker(self, request):
        http_info = self._list_topics_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_topics_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics",
            "request_type": request.__class__.__name__,
            "response_type": "ListTopicsResponse"
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
        if 'enterprise_project_id' in local_var_params:
            query_params.append(('enterprise_project_id', local_var_params['enterprise_project_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'fuzzy_name' in local_var_params:
            query_params.append(('fuzzy_name', local_var_params['fuzzy_name']))
        if 'topic_id' in local_var_params:
            query_params.append(('topic_id', local_var_params['topic_id']))
        if 'fuzzy_display_name' in local_var_params:
            query_params.append(('fuzzy_display_name', local_var_params['fuzzy_display_name']))

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

    def list_version_async(self, request):
        r"""查询SMN API V2版本信息

        查询SMN API V2版本信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVersion
        :type request: :class:`huaweicloudsdksmn.v2.ListVersionRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListVersionResponse`
        """
        http_info = self._list_version_http_info(request)
        return self._call_api(**http_info)

    def list_version_async_invoker(self, request):
        http_info = self._list_version_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_version_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2",
            "request_type": request.__class__.__name__,
            "response_type": "ListVersionResponse"
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

    def list_versions_async(self, request):
        r"""查询SMN支持的API版本号信息

        查询SMN开放API支持的版本号。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListVersions
        :type request: :class:`huaweicloudsdksmn.v2.ListVersionsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListVersionsResponse`
        """
        http_info = self._list_versions_http_info(request)
        return self._call_api(**http_info)

    def list_versions_async_invoker(self, request):
        http_info = self._list_versions_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_versions_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/",
            "request_type": request.__class__.__name__,
            "response_type": "ListVersionsResponse"
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

    def publish_http_detect_async(self, request):
        r"""发布探测消息

        基于主题发送http/https探测消息，探测当前http/https 终端是否可用，SMN出口是否能够正常访问该终端。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishHttpDetect
        :type request: :class:`huaweicloudsdksmn.v2.PublishHttpDetectRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.PublishHttpDetectResponse`
        """
        http_info = self._publish_http_detect_http_info(request)
        return self._call_api(**http_info)

    def publish_http_detect_async_invoker(self, request):
        http_info = self._publish_http_detect_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_http_detect_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/detection",
            "request_type": request.__class__.__name__,
            "response_type": "PublishHttpDetectResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def publish_message_async(self, request):
        r"""消息发布

        将消息发送给Topic的所有订阅端点。当返回消息ID时，该消息已被保存并开始尝试将其推送给Topic的订阅者。为确保您的消息能够成功推送到各个订阅者，请确保您的消息内容符合当地法律法规要求。
        三种消息发送方式
        
        message
        
        message_structure
        
        message_template_name
        
        只需要设置其中一个，如果同时设置，生效的优先级为
        message_structure &gt; message_template_name &gt; message。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishMessage
        :type request: :class:`huaweicloudsdksmn.v2.PublishMessageRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.PublishMessageResponse`
        """
        http_info = self._publish_message_http_info(request)
        return self._call_api(**http_info)

    def publish_message_async_invoker(self, request):
        http_info = self._publish_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def show_http_detect_result_async(self, request):
        r"""获取http探测结果

        根据http探测发送返回的task_id查询探测结果。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowHttpDetectResult
        :type request: :class:`huaweicloudsdksmn.v2.ShowHttpDetectResultRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ShowHttpDetectResultResponse`
        """
        http_info = self._show_http_detect_result_http_info(request)
        return self._call_api(**http_info)

    def show_http_detect_result_async_invoker(self, request):
        http_info = self._show_http_detect_result_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_http_detect_result_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/detection/{task_id}",
            "request_type": request.__class__.__name__,
            "response_type": "ShowHttpDetectResultResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
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

    def show_notify_policy_async(self, request):
        r"""查询通知策略

        查询通知策略
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ShowNotifyPolicy
        :type request: :class:`huaweicloudsdksmn.v2.ShowNotifyPolicyRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ShowNotifyPolicyResponse`
        """
        http_info = self._show_notify_policy_http_info(request)
        return self._call_api(**http_info)

    def show_notify_policy_async_invoker(self, request):
        http_info = self._show_notify_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _show_notify_policy_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/notify-policy",
            "request_type": request.__class__.__name__,
            "response_type": "ShowNotifyPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def update_logtank_async(self, request):
        r"""更新云日志

        更新指定Topic绑定的云日志。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateLogtank
        :type request: :class:`huaweicloudsdksmn.v2.UpdateLogtankRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateLogtankResponse`
        """
        http_info = self._update_logtank_http_info(request)
        return self._call_api(**http_info)

    def update_logtank_async_invoker(self, request):
        http_info = self._update_logtank_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_logtank_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/logtanks/{logtank_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateLogtankResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'logtank_id' in local_var_params:
            path_params['logtank_id'] = local_var_params['logtank_id']

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

    def update_message_template_async(self, request):
        r"""更新消息模板

        修改消息模板的内容。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateMessageTemplate
        :type request: :class:`huaweicloudsdksmn.v2.UpdateMessageTemplateRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateMessageTemplateResponse`
        """
        http_info = self._update_message_template_http_info(request)
        return self._call_api(**http_info)

    def update_message_template_async_invoker(self, request):
        http_info = self._update_message_template_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_message_template_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/message_template/{message_template_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateMessageTemplateResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'message_template_id' in local_var_params:
            path_params['message_template_id'] = local_var_params['message_template_id']

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

    def update_notify_policy_async(self, request):
        r"""修改通知策略

        修改通知策略，该接口仅支持全量修改，不支持部分修改。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateNotifyPolicy
        :type request: :class:`huaweicloudsdksmn.v2.UpdateNotifyPolicyRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateNotifyPolicyResponse`
        """
        http_info = self._update_notify_policy_http_info(request)
        return self._call_api(**http_info)

    def update_notify_policy_async_invoker(self, request):
        http_info = self._update_notify_policy_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_notify_policy_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/notify-policy/{notify_policy_id}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateNotifyPolicyResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'notify_policy_id' in local_var_params:
            path_params['notify_policy_id'] = local_var_params['notify_policy_id']

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

    def update_subscription_async(self, request):
        r"""更新订阅者

        更新订阅者备注。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateSubscription
        :type request: :class:`huaweicloudsdksmn.v2.UpdateSubscriptionRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateSubscriptionResponse`
        """
        http_info = self._update_subscription_http_info(request)
        return self._call_api(**http_info)

    def update_subscription_async_invoker(self, request):
        http_info = self._update_subscription_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_subscription_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/subscriptions/{subscription_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateSubscriptionResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'subscription_urn' in local_var_params:
            path_params['subscription_urn'] = local_var_params['subscription_urn']

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

    def update_topic_async(self, request):
        r"""更新主题

        更新显示名。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopic
        :type request: :class:`huaweicloudsdksmn.v2.UpdateTopicRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateTopicResponse`
        """
        http_info = self._update_topic_http_info(request)
        return self._call_api(**http_info)

    def update_topic_async_invoker(self, request):
        http_info = self._update_topic_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_topic_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopicResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']

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

    def update_topic_attribute_async(self, request):
        r"""更新主题策略

        更新主题的策略信息。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateTopicAttribute
        :type request: :class:`huaweicloudsdksmn.v2.UpdateTopicAttributeRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateTopicAttributeResponse`
        """
        http_info = self._update_topic_attribute_http_info(request)
        return self._call_api(**http_info)

    def update_topic_attribute_async_invoker(self, request):
        http_info = self._update_topic_attribute_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_topic_attribute_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/topics/{topic_urn}/attributes/{name}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateTopicAttributeResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'topic_urn' in local_var_params:
            path_params['topic_urn'] = local_var_params['topic_urn']
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']

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

    def create_application_async(self, request):
        r"""创建Application

        创建平台应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApplication
        :type request: :class:`huaweicloudsdksmn.v2.CreateApplicationRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateApplicationResponse`
        """
        warnings.warn("Method 'create_application_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_application_http_info(request)
        return self._call_api(**http_info)

    def create_application_async_invoker(self, request):
        warnings.warn("Method 'create_application_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_application_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/applications",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationResponse"
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

    def delete_application_async(self, request):
        r"""删除Application

        删除平台应用。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApplication
        :type request: :class:`huaweicloudsdksmn.v2.DeleteApplicationRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteApplicationResponse`
        """
        warnings.warn("Method 'delete_application_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_application_http_info(request)
        return self._call_api(**http_info)

    def delete_application_async_invoker(self, request):
        warnings.warn("Method 'delete_application_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_application_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/applications/{application_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_urn' in local_var_params:
            path_params['application_urn'] = local_var_params['application_urn']

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

    def list_application_attributes_async(self, request):
        r"""查询Application属性

        获取应用平台属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplicationAttributes
        :type request: :class:`huaweicloudsdksmn.v2.ListApplicationAttributesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListApplicationAttributesResponse`
        """
        warnings.warn("Method 'list_application_attributes_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_application_attributes_http_info(request)
        return self._call_api(**http_info)

    def list_application_attributes_async_invoker(self, request):
        warnings.warn("Method 'list_application_attributes_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_application_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_application_attributes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/applications/{application_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_urn' in local_var_params:
            path_params['application_urn'] = local_var_params['application_urn']

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

    def list_applications_async(self, request):
        r"""查询Application

        查询应用平台列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplications
        :type request: :class:`huaweicloudsdksmn.v2.ListApplicationsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListApplicationsResponse`
        """
        warnings.warn("Method 'list_applications_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_applications_http_info(request)
        return self._call_api(**http_info)

    def list_applications_async_invoker(self, request):
        warnings.warn("Method 'list_applications_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_applications_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_applications_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/applications",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationsResponse"
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
        if 'platform' in local_var_params:
            query_params.append(('platform', local_var_params['platform']))

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

    def publish_app_message_async(self, request):
        r"""App消息发布

        将消息直发给endpoint设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for PublishAppMessage
        :type request: :class:`huaweicloudsdksmn.v2.PublishAppMessageRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.PublishAppMessageResponse`
        """
        warnings.warn("Method 'publish_app_message_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._publish_app_message_http_info(request)
        return self._call_api(**http_info)

    def publish_app_message_async_invoker(self, request):
        warnings.warn("Method 'publish_app_message_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._publish_app_message_http_info(request)
        return AsyncInvoker(self, http_info)

    def _publish_app_message_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/endpoints/{endpoint_urn}/publish",
            "request_type": request.__class__.__name__,
            "response_type": "PublishAppMessageResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_urn' in local_var_params:
            path_params['endpoint_urn'] = local_var_params['endpoint_urn']

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

    def update_application_async(self, request):
        r"""更新Application

        更新应用平台。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApplication
        :type request: :class:`huaweicloudsdksmn.v2.UpdateApplicationRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateApplicationResponse`
        """
        warnings.warn("Method 'update_application_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_application_http_info(request)
        return self._call_api(**http_info)

    def update_application_async_invoker(self, request):
        warnings.warn("Method 'update_application_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_application_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_application_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/applications/{application_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_urn' in local_var_params:
            path_params['application_urn'] = local_var_params['application_urn']

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

    def create_application_endpoint_async(self, request):
        r"""创建Application endpoint

        创建应用平台的endpoint终端。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for CreateApplicationEndpoint
        :type request: :class:`huaweicloudsdksmn.v2.CreateApplicationEndpointRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.CreateApplicationEndpointResponse`
        """
        warnings.warn("Method 'create_application_endpoint_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_application_endpoint_http_info(request)
        return self._call_api(**http_info)

    def create_application_endpoint_async_invoker(self, request):
        warnings.warn("Method 'create_application_endpoint_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._create_application_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _create_application_endpoint_http_info(self, request):
        http_info = {
            "method": "POST",
            "resource_path": "/v2/{project_id}/notifications/applications/{application_urn}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "CreateApplicationEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_urn' in local_var_params:
            path_params['application_urn'] = local_var_params['application_urn']

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

    def delete_application_endpoint_async(self, request):
        r"""删除Application endpoint

        删除设备。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for DeleteApplicationEndpoint
        :type request: :class:`huaweicloudsdksmn.v2.DeleteApplicationEndpointRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.DeleteApplicationEndpointResponse`
        """
        warnings.warn("Method 'delete_application_endpoint_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_application_endpoint_http_info(request)
        return self._call_api(**http_info)

    def delete_application_endpoint_async_invoker(self, request):
        warnings.warn("Method 'delete_application_endpoint_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._delete_application_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _delete_application_endpoint_http_info(self, request):
        http_info = {
            "method": "DELETE",
            "resource_path": "/v2/{project_id}/notifications/endpoints/{endpoint_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "DeleteApplicationEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_urn' in local_var_params:
            path_params['endpoint_urn'] = local_var_params['endpoint_urn']

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

    def list_application_endpoint_attributes_async(self, request):
        r"""查询Application的Endpoint属性

        获取endpoint的属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplicationEndpointAttributes
        :type request: :class:`huaweicloudsdksmn.v2.ListApplicationEndpointAttributesRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListApplicationEndpointAttributesResponse`
        """
        warnings.warn("Method 'list_application_endpoint_attributes_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_application_endpoint_attributes_http_info(request)
        return self._call_api(**http_info)

    def list_application_endpoint_attributes_async_invoker(self, request):
        warnings.warn("Method 'list_application_endpoint_attributes_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_application_endpoint_attributes_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_application_endpoint_attributes_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/endpoints/{endpoint_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationEndpointAttributesResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_urn' in local_var_params:
            path_params['endpoint_urn'] = local_var_params['endpoint_urn']

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

    def list_application_endpoints_async(self, request):
        r"""查询Application的Endpoint列表

        查询平台的endpoint列表。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for ListApplicationEndpoints
        :type request: :class:`huaweicloudsdksmn.v2.ListApplicationEndpointsRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.ListApplicationEndpointsResponse`
        """
        warnings.warn("Method 'list_application_endpoints_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_application_endpoints_http_info(request)
        return self._call_api(**http_info)

    def list_application_endpoints_async_invoker(self, request):
        warnings.warn("Method 'list_application_endpoints_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._list_application_endpoints_http_info(request)
        return AsyncInvoker(self, http_info)

    def _list_application_endpoints_http_info(self, request):
        http_info = {
            "method": "GET",
            "resource_path": "/v2/{project_id}/notifications/applications/{application_urn}/endpoints",
            "request_type": request.__class__.__name__,
            "response_type": "ListApplicationEndpointsResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'application_urn' in local_var_params:
            path_params['application_urn'] = local_var_params['application_urn']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'enabled' in local_var_params:
            query_params.append(('enabled', local_var_params['enabled']))
        if 'token' in local_var_params:
            query_params.append(('token', local_var_params['token']))
        if 'user_data' in local_var_params:
            query_params.append(('user_data', local_var_params['user_data']))

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

    def update_application_endpoint_async(self, request):
        r"""更新Application endpoint

        更新设备属性。
        
        Please refer to HUAWEI cloud API Explorer for details.


        :param request: Request instance for UpdateApplicationEndpoint
        :type request: :class:`huaweicloudsdksmn.v2.UpdateApplicationEndpointRequest`
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateApplicationEndpointResponse`
        """
        warnings.warn("Method 'update_application_endpoint_async' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_application_endpoint_http_info(request)
        return self._call_api(**http_info)

    def update_application_endpoint_async_invoker(self, request):
        warnings.warn("Method 'update_application_endpoint_async_invoker' of SmnAsyncClient is deprecated and will be removed in the future versions", DeprecationWarning)
        http_info = self._update_application_endpoint_http_info(request)
        return AsyncInvoker(self, http_info)

    def _update_application_endpoint_http_info(self, request):
        http_info = {
            "method": "PUT",
            "resource_path": "/v2/{project_id}/notifications/endpoints/{endpoint_urn}",
            "request_type": request.__class__.__name__,
            "response_type": "UpdateApplicationEndpointResponse"
            }

        local_var_params = {attr: getattr(request, attr) for attr in request.attribute_map if hasattr(request, attr)}

        cname = None

        collection_formats = {}

        path_params = {}
        if 'endpoint_urn' in local_var_params:
            path_params['endpoint_urn'] = local_var_params['endpoint_urn']

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
